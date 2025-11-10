---
audio: false
generated: true
image: false
lang: ja
layout: post
title: ロギングのためのJavaリクエストラッパー
translated: true
type: note
---

Java Webアプリケーションでは、サーブレットコンテナの実装に手を加えずに標準の`HttpServletRequest`の動作を装飾または変更したい場合、通常 **`HttpServletRequestWrapper`** を使用します。

### `HttpServletRequestWrapper`の仕組み

* これは元の`HttpServletRequest`を**装飾（デコレータ）** するクラスです。
* `HttpServletRequestWrapper`をサブクラス化し、`getInputStream()`、`getReader()`、`getParameter()`などのメソッドをオーバーライドします。
* これは**リクエストボディを読み取りまたはキャッシュ**したい場合（デフォルトでは1回しか読み取れない）や、リクエストパラメータを変更/クエリする場合に便利です。

### ロギングに必要な理由

* デフォルトでは、サーブレットリクエストボディ（`InputStream`）は1回しか消費できません。フィルタで直接ログに記録すると、コントローラは後でそれを読み取ることができなくなります。
* ラッピングにより、ボディを**キャッシュ**して複数回読み取ることが可能になります：1回はロギング用、1回は下流処理用。
* URLパラメータは、`request.getParameterMap()`または`request.getQueryString()`にアクセスしてログに記録できます。

---

### 例: ボディとURLパラメータのロギング

カスタムラッパーを使用したフィルタの例：

```java
public class CachedBodyHttpServletRequest extends HttpServletRequestWrapper {
    private byte[] cachedBody;

    public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
        super(request);
        InputStream requestInputStream = request.getInputStream();
        this.cachedBody = requestInputStream.readAllBytes();
    }

    @Override
    public ServletInputStream getInputStream() {
        ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(this.cachedBody);
        return new ServletInputStream() {
            @Override
            public int read() {
                return byteArrayInputStream.read();
            }
            @Override
            public boolean isFinished() {
                return byteArrayInputStream.available() == 0;
            }
            @Override
            public boolean isReady() {
                return true;
            }
            @Override
            public void setReadListener(ReadListener readListener) {}
        };
    }

    @Override
    public BufferedReader getReader() {
        return new BufferedReader(new InputStreamReader(this.getInputStream()));
    }

    public String getBody() {
        return new String(this.cachedBody, StandardCharsets.UTF_8);
    }
}
```

次に、これをフィルタで使用します：

```java
@WebFilter("/*")
public class LoggingFilter implements Filter {
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {

        CachedBodyHttpServletRequest wrappedRequest = new CachedBodyHttpServletRequest((HttpServletRequest) request);

        // URLをログに記録
        String url = wrappedRequest.getRequestURL().toString();
        String query = wrappedRequest.getQueryString();

        // パラメータをログに記録
        Map<String, String[]> params = wrappedRequest.getParameterMap();

        // ボディをログに記録
        String body = wrappedRequest.getBody();

        System.out.println("Request URL: " + url + (query != null ? "?" + query : ""));
        System.out.println("Parameters: " + params);
        System.out.println("Body: " + body);

        // フィルタチェインを継続
        chain.doFilter(wrappedRequest, response);
    }
}
```

---

### 主なポイント

* **`HttpServletRequestWrapper`** を使用すると、ボディを安全に複数回読み取ることができます。
* URLパラメータの場合：`getParameterMap()`または`getQueryString()`で十分です。
* **大きなボディ**には注意が必要です（ストリーミングやサイズ制限を検討する必要があるかもしれません）。
* 本番環境では、`System.out`の代わりにロギングフレームワーク（SLF4J + Logback/Log4J2）を使用してください。

---

**Spring Bootスタイルのソリューション**（`OncePerRequestFilter`と`ContentCachingRequestWrapper`を使用）も紹介しましょうか？そちらの方がはるかにシンプルです。