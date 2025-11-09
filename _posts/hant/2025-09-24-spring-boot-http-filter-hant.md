---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: Spring Boot HTTP 請求日誌記錄篩選器
translated: true
type: note
---

以下是如何在 Spring（例如 Spring Boot 或 Spring MVC）中實作自訂 Servlet Filter 以記錄傳入 HTTP 請求的結構化資料範例。此篩選器將擷取並記錄：

- **HTTP 方法**：例如 GET、POST。
- **查詢參數**：以映射形式提取。
- **請求主體**：適用於 POST/PUT 等方法（注意：主體是串流，因此我們封裝請求以便讀取，且不消耗其內容以供後續處理）。

日誌輸出將採用結構化的 JSON 格式。我們將使用：
- **SLF4J** 進行日誌記錄（Spring 中常用）。
- **Jackson** 將資料序列化為 JSON（Spring Boot 預設包含）。
- 自訂的 `HttpServletRequestWrapper` 以安全地讀取主體。

此篩選器可全域註冊以攔截所有請求。

### 步驟 1：依賴項
若使用 Spring Boot，請確保您的 `pom.xml`（Maven）或 `build.gradle`（Gradle）中包含以下內容：
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <!-- Jackson 已包含，但為清晰起見明確列出 -->
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
    </dependency>
</dependencies>
```

### 步驟 2：自訂請求封裝器
此封裝器允許多次讀取請求主體（透過將其快取為字串）。

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

    // 輔助方法：以映射形式提取查詢參數
    public Map<String, String[]> getQueryParams() {
        Map<String, String[]> params = new LinkedHashMap<>();
        // 加入查詢字串參數
        String queryString = getQueryString();
        if (queryString != null) {
            // 簡單解析；複雜情況可使用 Apache Commons 等函式庫
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
        // 與參數映射合併
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

### 步驟 3：自訂篩選器
此篩選器使用 SLF4J 以 JSON 格式記錄結構化資料。它應用於所有請求。

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

        // 僅對具有主體的方法（例如 POST、PUT）封裝請求
        ContentCachingRequestWrapper wrappedRequest = null;
        String body = "";
        if ("GET".equalsIgnoreCase(request.getMethod()) == false) {
            wrappedRequest = new ContentCachingRequestWrapper(request);
            body = wrappedRequest.getRequestBodyAsString();
        } else {
            wrappedRequest = new ContentCachingRequestWrapper(request);
        }

        // 建立結構化資料映射
        Map<String, Object> logData = new HashMap<>();
        logData.put("httpMethod", request.getMethod());
        logData.put("requestUri", request.getRequestURI());
        logData.put("queryParams", wrappedRequest.getQueryParams());
        logData.put("requestBody", body); // 僅對 POST 類方法非空

        // 以 JSON 格式記錄
        String jsonLog = objectMapper.writeValueAsString(logData);
        logger.info("傳入請求: {}", jsonLog);

        // 使用封裝後的請求繼續處理
        filterChain.doFilter(wrappedRequest != null ? wrappedRequest : request, response);
    }
}
```

### 步驟 4：註冊篩選器（在 Spring Boot 中自動註冊）
在 Spring Boot 中，篩選器上的 `@Component` 註解會自動註冊它。若使用純 Spring MVC（非 Boot），可手動註冊：

```java
// 在 @Configuration 類別中
@Bean
public FilterRegistrationBean<LoggingFilter> loggingFilter() {
    FilterRegistrationBean<LoggingFilter> registrationBean = new FilterRegistrationBean<>();
    registrationBean.setFilter(new LoggingFilter());
    registrationBean.addUrlPatterns("/*"); // 應用於所有 URL
    registrationBean.setOrder(1);
    return registrationBean;
}
```

### 日誌輸出範例
當收到如 `POST /api/users` 且主體為 `{"name": "John"}`、查詢為 `?id=123` 的請求時，日誌將如下所示（假設您的日誌記錄器配置為 JSON 輸出，例如透過帶有 JSON 附加器的 Logback）：

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

- **日誌記錄器配置**：要獲得完整的 JSON 日誌，請使用 JSON 編碼器（如 `net.logstash.logback.encoder.LogstashEncoder`）配置 Logback（在 `logback-spring.xml` 或 `application.properties` 中）。例如，在 `application.yml` 中：
  ```yaml
  logging:
    pattern:
      console: "%msg%n"  # 或使用 JSON 附加器以獲得結構化輸出
  ```

### 注意事項
- **主體讀取限制**：我們僅讀取非 GET 方法的主體。對於 GET，主體為空。這可避免大型主體或多次讀取的問題。
- **安全性**：記錄敏感資料（例如主體/查詢中的密碼）時請謹慎。您可能需要遮罩欄位。
- **效能**：快取主體會使用記憶體；對於非常大的主體，請考慮限制（例如僅讀取前 N 位元組）。
- **測試**：將此加入 Spring Boot 應用程式，並透過 curl 傳送 POST 請求：`curl -X POST http://localhost:8080/api/users?id=123 -d '{"name":"John"}' -H "Content-Type: application/json"`。
- **替代方案**：對於更高級的日誌記錄，請考慮使用 Spring Boot Actuator 或帶有結構化日誌記錄的函式庫，如 `spring-boot-starter-logging`。

這是一個可投入生產的起點。根據需要進行自訂！如需更多詳細資訊，請告知。