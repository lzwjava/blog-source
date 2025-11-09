---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast:free
title: Spring Boot HTTPリクエストロギングフィルター
translated: true
type: note
---

以下は、Spring（例: Spring Boot または Spring MVC）でカスタム Servlet フィルターを実装し、受信 HTTP リクエストから構造化データをログ出力する例です。このフィルターは以下をキャプチャしてログ出力します:

- **HTTP メソッド**: 例: GET、POST
- **クエリパラメータ**: マップとして抽出
- **リクエストボディ**: POST/PUT などのメソッド用（ボディはストリームであるため、下流の処理で消費されないようリクエストをラップして読み取り）

ログ出力は構造化 JSON 形式になります。以下を使用します:
- **SLF4J**: ロギング用（Spring で一般的）
- **Jackson**: データを JSON にシリアライズするため（Spring Boot にはデフォルトで含まれる）
- カスタム `HttpServletRequestWrapper`: ボディを安全に読み取るため

このフィルターは、すべてのリクエストをインターセプトするようにグローバルに登録できます。

### ステップ 1: 依存関係
Spring Boot を使用する場合、`pom.xml`（Maven）または `build.gradle`（Gradle）に以下があることを確認してください:
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <!-- Jackson は含まれていますが、明確化のために明示的に記載 -->
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
    </dependency>
</dependencies>
```

### ステップ 2: カスタムリクエストラッパー
このラッパーは、リクエストボディを複数回読み取ることを可能にします（文字列としてキャッシュすることにより）。

```java
package com.example.filter;

import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.servlet.ReadListener;
import jakarta.servlet.ServletInputStream;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletRequestWrapper;
import org.springframework.util.StreamUtils;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.Map;

public class ContentCachingRequestWrapper extends HttpServletRequestWrapper {
    private final byte[] cachedBody;
    private final ObjectMapper objectMapper = new ObjectMapper();

    public ContentCachingRequestWrapper(HttpServletRequest request) throws IOException {
        super(request);
        InputStream requestInputStream = request.getInputStream();
        this.cachedBody = StreamUtils.copyToByteArray(requestInputStream);
    }

    @Override
    public ServletInputStream getInputStream() throws IOException {
        return new CachedServletInputStream(this.cachedBody);
    }

    @Override
    public BufferedReader getReader() throws IOException {
        byte[] requestBodyBytes = getRequestBody();
        return new BufferedReader(new InputStreamReader(new ByteArrayInputStream(requestBodyBytes),
                StandardCharsets.UTF_8));
    }

    public String getRequestBodyAsString() {
        if (cachedBody.length > 0) {
            return new String(cachedBody, StandardCharsets.UTF_8);
        }
        return "";
    }

    public byte[] getRequestBody() {
        return cachedBody;
    }

    // クエリパラメータをマップとして抽出するヘルパー
    public Map<String, String[]> getQueryParams() {
        Map<String, String[]> params = new LinkedHashMap<>();
        // クエリ文字列パラメータを追加
        String queryString = getQueryString();
        if (queryString != null) {
            // シンプルな解析。複雑なケースでは Apache Commons などのライブラリを使用
            String[] pairs = queryString.split("&");
            for (String pair : pairs) {
                String[] keyValue = pair.split("=", 2);
                if (keyValue.length == 2) {
                    params.put(keyValue[0], new String[]{keyValue[1]});
                } else {
                    params.put(keyValue[0], new String[]{});
                }
            }
        }
        // パラメータマップとマージ
        params.putAll(getParameterMap());
        return params;
    }

    private static class CachedServletInputStream extends ServletInputStream {
        private final ByteArrayInputStream cachedBodyInputStream;

        public CachedServletInputStream(byte[] cachedBody) {
            this.cachedBodyInputStream = new ByteArrayInputStream(cachedBody);
        }

        @Override
        public boolean isFinished() {
            return cachedBodyInputStream.available() == 0;
        }

        @Override
        public boolean isReady() {
            return true;
        }

        @Override
        public void setReadListener(ReadListener readListener) {
            throw new UnsupportedOperationException();
        }

        @Override
        public int read() throws IOException {
            return cachedBodyInputStream.read();
        }
    }
}
```

### ステップ 3: カスタムフィルター
このフィルターは、構造化データを SLF4J を使用して JSON としてログ出力します。すべてのリクエストに適用されます。

```java
package com.example.filter;

import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import org.springframework.util.StreamUtils;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@Component
public class LoggingFilter extends OncePerRequestFilter {

    private static final Logger logger = LoggerFactory.getLogger(LoggingFilter.class);
    private final ObjectMapper objectMapper = new ObjectMapper();

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {

        // ボディを持つメソッド（例: POST、PUT）のみリクエストをラップ
        ContentCachingRequestWrapper wrappedRequest = null;
        String body = "";
        if ("GET".equalsIgnoreCase(request.getMethod()) == false) {
            wrappedRequest = new ContentCachingRequestWrapper(request);
            body = wrappedRequest.getRequestBodyAsString();
        } else {
            wrappedRequest = new ContentCachingRequestWrapper(request);
        }

        // 構造化データマップを構築
        Map<String, Object> logData = new HashMap<>();
        logData.put("httpMethod", request.getMethod());
        logData.put("requestUri", request.getRequestURI());
        logData.put("queryParams", wrappedRequest.getQueryParams());
        logData.put("requestBody", body); // POST のようなメソッドでのみ空でない

        // JSON としてログ出力
        String jsonLog = objectMapper.writeValueAsString(logData);
        logger.info("Incoming Request: {}", jsonLog);

        // ラップされたリクエストで処理を継続
        filterChain.doFilter(wrappedRequest != null ? wrappedRequest : request, response);
    }
}
```

### ステップ 4: フィルターの登録（Spring Boot では自動）
Spring Boot では、フィルターの `@Component` アノテーションにより自動的に登録されます。プレーンな Spring MVC（Boot ではない）を使用する場合は、手動で登録できます:

```java
// @Configuration クラス内
@Bean
public FilterRegistrationBean<LoggingFilter> loggingFilter() {
    FilterRegistrationBean<LoggingFilter> registrationBean = new FilterRegistrationBean<>();
    registrationBean.setFilter(new LoggingFilter());
    registrationBean.addUrlPatterns("/*"); // すべての URL に適用
    registrationBean.setOrder(1);
    return registrationBean;
}
```

### ログ出力例
`POST /api/users` リクエストで、ボディ `{"name": "John"}`、クエリ `?id=123` が送信されると、ログは以下のようになります（ロガーが JSON 出力用に設定されている場合、例: Logback with JSON appender）:

```json
{
  "httpMethod": "POST",
  "requestUri": "/api/users",
  "queryParams": {
    "id": ["123"]
  },
  "requestBody": "{\"name\": \"John\"}"
}
```

- **ロガー設定**: 完全な JSON ログを取得するには、Logback（`logback-spring.xml` または `application.properties` 内）を `net.logstash.logback.encoder.LogstashEncoder` のような JSON エンコーダーで設定します。例: `application.yml` 内:
  ```yaml
  logging:
    pattern:
      console: "%msg%n"  # または構造化出力用に JSON アペンダーを使用
  ```

### 注意点
- **ボディ読み取り制限**: 非 GET メソッドのボディのみ読み取ります。GET の場合は空です。これにより、大きなボディや複数回の読み取りの問題を回避します。
- **セキュリティ**: 機密データ（ボディ/クエリ内のパスワードなど）のログ出力には注意してください。フィールドをマスクする必要がある場合があります。
- **パフォーマンス**: ボディのキャッシュはメモリを使用します。非常に大きなボディの場合、制限を検討してください（例: 最初の N バイトのみ読み取り）。
- **テスト**: これを Spring Boot アプリに追加し、curl で POST リクエストを送信します: `curl -X POST http://localhost:8080/api/users?id=123 -d '{"name":"John"}' -H "Content-Type: application/json"`
- **代替案**: より高度なロギングには、Spring Boot Actuator や `spring-boot-starter-logging` と構造化ロギングを使用したライブラリを検討してください。

これはプロダクション対応の出発点です。必要に応じてカスタマイズしてください！詳細が必要な場合はお知らせください。