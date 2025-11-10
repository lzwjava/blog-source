---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Java 請求封裝器用於日誌記錄
translated: true
type: note
---

在 Java web 應用程式中，當您想要修飾或修改標準 `HttpServletRequest` 的行為，而不觸及 servlet 容器的實作時，通常會使用 **`HttpServletRequestWrapper`**。

### `HttpServletRequestWrapper` 的運作原理

* 它是原始 `HttpServletRequest` 的**裝飾器**。
* 您可以繼承 `HttpServletRequestWrapper` 並覆寫方法，例如 `getInputStream()`、`getReader()` 或 `getParameter()`。
* 當您想要**讀取或快取請求主體**（預設只能讀取一次）或修改/查詢請求參數時，這非常有用。

### 為何需要它來進行日誌記錄

* 預設情況下，servlet 請求主體（`InputStream`）只能被消耗一次。如果您在過濾器中直接記錄它，控制器將無法在之後讀取它。
* 包裝允許您**快取主體**，以便可以多次讀取：一次用於日誌記錄，一次用於下游處理。
* URL 參數可以通過存取 `request.getParameterMap()` 或 `request.getQueryString()` 來記錄。

---

### 範例：記錄主體和 URL 參數

以下是一個使用自訂包裝器的過濾器：

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

然後在過濾器中使用它：

```java
@WebFilter("/*")
public class LoggingFilter implements Filter {
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {

        CachedBodyHttpServletRequest wrappedRequest = new CachedBodyHttpServletRequest((HttpServletRequest) request);

        // 記錄 URL
        String url = wrappedRequest.getRequestURL().toString();
        String query = wrappedRequest.getQueryString();

        // 記錄參數
        Map<String, String[]> params = wrappedRequest.getParameterMap();

        // 記錄主體
        String body = wrappedRequest.getBody();

        System.out.println("Request URL: " + url + (query != null ? "?" + query : ""));
        System.out.println("Parameters: " + params);
        System.out.println("Body: " + body);

        // 繼續過濾器鏈
        chain.doFilter(wrappedRequest, response);
    }
}
```

---

### 關鍵點

* **`HttpServletRequestWrapper`** 讓您可以安全地多次讀取主體。
* 對於 URL 參數：`getParameterMap()` 或 `getQueryString()` 已足夠。
* 對於**大型主體**要小心（您可能需要串流處理或大小限制）。
* 在生產環境中，請使用日誌記錄框架（SLF4J + Logback/Log4J2）而不是 `System.out`。

---

您是否也希望我展示一個 **Spring Boot 風格的解決方案**（使用 `OncePerRequestFilter` 和 `ContentCachingRequestWrapper`），因為那會簡單得多？