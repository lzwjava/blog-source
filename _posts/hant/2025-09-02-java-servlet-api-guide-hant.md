---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Java Servlet API 指南精要
translated: true
type: note
---

這是一份實用的 Java **Servlet** API 端到端指南，涵蓋經典的 **`javax.servlet.*`** 命名空間（Servlet 2.x–4.x 時代）。我也會說明遷移至 **`jakarta.servlet.*`** 後的變化，讓你的程式碼具備未來兼容性。

# 1) 什麼是 Servlet？

**Servlet** 是一個在 **Servlet 容器**（Tomcat、Jetty、WebSphere、WebLogic 等）內運行的 Java 類別，用於處理 HTTP 請求/回應。容器負責管理：

* 生命週期（載入、初始化、服務、銷毀）
* 多線程和請求路由
* 會話、安全性、資源和配置

# 2) 核心套件與關鍵介面 (javax.\*)

* `javax.servlet.Servlet`、`ServletConfig`、`ServletContext`
* `javax.servlet.http.HttpServlet`、`HttpServletRequest`、`HttpServletResponse`、`HttpSession`、`Cookie`
* `javax.servlet.Filter`、`FilterChain`、`FilterConfig`
* `javax.servlet.ServletRequestListener` 及其他監聽器
* `javax.servlet.annotation.*`（自 3.0 起：`@WebServlet`、`@WebFilter`、`@WebListener`、`@MultipartConfig`）
* 自 3.0 起：**非同步**（`AsyncContext`）、程式化註冊
* 自 3.1 起：**非阻塞 I/O**（`ServletInputStream`/`ServletOutputStream` 與 `ReadListener`/`WriteListener`）
* 自 4.0 起：HTTP/2 支援（例如 `PushBuilder`）

> Jakarta 轉換：從 **Servlet 5.0**（Jakarta EE 9）開始，套件名稱改為 `jakarta.servlet.*`。大多數 API 保持不變；遷移時請更新導入語句和依賴項。

# 3) Servlet 生命週期與線程模型

* **載入**：容器載入類別，每個宣告建立單一實例。
* **`init(ServletConfig)`**：呼叫一次。讀取初始化參數，快取重型資源。
* **`service(req, res)`**：每個請求呼叫一次。`HttpServlet` 會分派到 `doGet`、`doPost` 等方法。
* **`destroy()`**：在關閉/重新部署時呼叫一次。

**線程**：容器在同一實例上並行呼叫 `service`。
**規則**：避免可變的實例欄位；如果必須使用，請使用線程安全結構或適當的同步機制。優先使用局部變數。

# 4) 最小化 Servlet（註解）

```java
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import javax.servlet.ServletException;
import java.io.IOException;

@WebServlet(name = "HelloServlet", urlPatterns = "/hello")
public class HelloServlet extends HttpServlet {
  @Override protected void doGet(HttpServletRequest req, HttpServletResponse resp)
      throws ServletException, IOException {
    resp.setContentType("text/plain;charset=UTF-8");
    resp.getWriter().println("Hello, Servlet!");
  }
}
```

# 5) `web.xml` 與註解

**註解（3.0+）** 最適合簡單應用程式。
**`web.xml`** 仍然適用於排序、覆蓋或舊版容器。

最小化 `web.xml`：

```xml
<web-app xmlns="http://java.sun.com/xml/ns/javaee" version="3.0">
  <servlet>
    <servlet-name>HelloServlet</servlet-name>
    <servlet-class>com.example.HelloServlet</servlet-class>
    <init-param>
      <param-name>greeting</param-name>
      <param-value>Hi</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
  </servlet>
  <servlet-mapping>
    <servlet-name>HelloServlet</servlet-name>
    <url-pattern>/hello</url-pattern>
  </servlet-mapping>
</web-app>
```

# 6) HTTP 請求/回應基礎

## 讀取請求資料

```java
String q = req.getParameter("q");        // 查詢/表單欄位
Enumeration<String> names = req.getParameterNames();
BufferedReader reader = req.getReader(); // 原始主體文字
ServletInputStream in = req.getInputStream(); // 二進位主體
String header = req.getHeader("X-Token");
```

**提示**：讀取參數前務必設定編碼：

```java
req.setCharacterEncoding("UTF-8");
```

## 寫入回應

```java
resp.setStatus(HttpServletResponse.SC_OK);
resp.setContentType("application/json;charset=UTF-8");
resp.setHeader("Cache-Control", "no-store");
try (PrintWriter out = resp.getWriter()) {
  out.write("{\"ok\":true}");
}
```

# 7) doGet 與 doPost 及其他方法

* `doGet`：冪等讀取；使用查詢字串。
* `doPost`：透過表單或 JSON 主體建立/更新。
* `doPut`/`doDelete`/`doPatch`：RESTful 語義（客戶端必須支援）。
* 始終驗證輸入並明確處理內容類型。

# 8) 會話與 Cookies

```java
HttpSession session = req.getSession(); // 如果不存在則建立
session.setAttribute("userId", 123L);
Long userId = (Long) session.getAttribute("userId");
session.invalidate(); // 登出
```

透過容器或程式化方式設定會話 Cookie 標誌：

* `HttpOnly`（防止 JS 存取）、`Secure`（HTTPS）、`SameSite=Lax/Strict`
  考慮使用無狀態令牌進行水平擴展；否則使用黏性會話或外部會話儲存。

# 9) 過濾器（橫切關注點）

使用**過濾器**處理日誌記錄、身份驗證、CORS、壓縮、編碼等。

```java
import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import java.io.IOException;

@WebFilter(urlPatterns = "/*")
public class LoggingFilter implements Filter {
  public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
      throws IOException, ServletException {
    long start = System.nanoTime();
    try {
      chain.doFilter(req, res);
    } finally {
      long ms = (System.nanoTime() - start) / 1_000_000;
      req.getServletContext().log("Handled in " + ms + " ms");
    }
  }
}
```

# 10) 監聽器（應用程式與請求掛鉤）

常見監聽器：

* `ServletContextListener`：應用程式啟動/關閉（初始化連接池、預熱快取）
* `HttpSessionListener`：建立/銷毀會話（指標、清理）
* `ServletRequestListener`：每個請求的掛鉤（追蹤 ID）

範例：

```java
@WebListener
public class AppBoot implements javax.servlet.ServletContextListener {
  public void contextInitialized(javax.servlet.ServletContextEvent sce) {
    sce.getServletContext().log("App starting...");
  }
  public void contextDestroyed(javax.servlet.ServletContextEvent sce) {
    sce.getServletContext().log("App stopping...");
  }
}
```

# 11) 非同步與非阻塞 I/O

## 非同步（Servlet 3.0）

允許在後端呼叫運行時釋放容器線程。

```java
@WebServlet(urlPatterns="/async", asyncSupported=true)
public class AsyncDemo extends HttpServlet {
  protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
    AsyncContext ctx = req.startAsync();
    ctx.start(() -> {
      try {
        // 呼叫慢速服務...
        ctx.getResponse().getWriter().println("done");
      } catch (Exception e) {
        ctx.complete();
      } finally {
        ctx.complete();
      }
    });
  }
}
```

## 非阻塞（Servlet 3.1）

在串流上註冊 `ReadListener`/`WriteListener` 以實現事件驅動 I/O。適用於串流大型主體而不阻塞線程。

# 12) 檔案上傳（Multipart）

```java
import javax.servlet.annotation.MultipartConfig;

@MultipartConfig(maxFileSize = 10 * 1024 * 1024)
@WebServlet("/upload")
public class UploadServlet extends HttpServlet {
  protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException, ServletException {
    Part file = req.getPart("file");
    String filename = file.getSubmittedFileName();
    try (InputStream is = file.getInputStream()) {
      // 儲存...
    }
    resp.getWriter().println("Uploaded " + filename);
  }
}
```

確保客戶端發送 `Content-Type: multipart/form-data`。

# 13) 分派與模板化

* **轉發**：伺服器端內部調度；原始 URL 保持不變。

  ```java
  req.getRequestDispatcher("/WEB-INF/view.jsp").forward(req, resp);
  ```
* **包含**：包含另一個資源的輸出。

  ```java
  req.getRequestDispatcher("/fragment").include(req, resp);
  ```
* **重定向**：客戶端 302/303/307 到新 URL。

  ```java
  resp.sendRedirect(req.getContextPath() + "/login");
  ```

# 14) 字元編碼與國際化

一個簡單的**編碼過濾器**可以防止亂碼：

```java
@WebFilter("/*")
public class Utf8Filter implements Filter {
  public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
      throws IOException, ServletException {
    req.setCharacterEncoding("UTF-8");
    res.setCharacterEncoding("UTF-8");
    chain.doFilter(req, res);
  }
}
```

使用 `HttpServletRequest#getLocale()` 取得的 `Locale` 和資源包進行國際化。

# 15) 安全性基礎

* **傳輸**：始終使用 HTTPS；設定 `Secure` Cookie。
* **身份驗證**：容器管理（FORM/BASIC/DIGEST），或使用帶有 JWT/會話的自定義過濾器。
* **CSRF**：產生每個會話的令牌；在狀態變更請求上驗證。
* **XSS**：HTML 轉義輸出；設定 `Content-Security-Policy`。
* **點擊劫持**：`X-Frame-Options: DENY` 或 CSP `frame-ancestors 'none'`。
* **CORS**：在過濾器中添加標頭：

  ```java
  resp.setHeader("Access-Control-Allow-Origin", "https://example.com");
  resp.setHeader("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE");
  resp.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
  ```

# 16) 錯誤處理

* 在 `web.xml` 或透過框架映射錯誤頁面：

```xml
<error-page>
  <error-code>404</error-code>
  <location>/WEB-INF/errors/404.jsp</location>
</error-page>
<error-page>
  <exception-type>java.lang.Throwable</exception-type>
  <location>/WEB-INF/errors/500.jsp</location>
</error-page>
```

* 在程式碼中，設定狀態碼並為 API 呈現一致的 JSON 錯誤結構。

# 17) 日誌記錄與可觀測性

* 使用 `ServletContext#log`，或更好的選擇：SLF4J + Logback/Log4j2。
* 在過濾器中添加請求 ID（UUID）；包含在日誌和回應標頭中。
* 暴露健康狀態端點；透過過濾器/Servlet 與 Prometheus 整合。

# 18) 打包與部署

**WAR 佈局**：

```
myapp/
  WEB-INF/
    web.xml
    classes/            # 編譯後的 .class 檔案
    lib/                # 第三方 jar
  index.html
  static/...
```

使用 Maven/Gradle 建置，產生 **WAR**，部署到容器的 `webapps`（Tomcat）或透過管理控制台。對於嵌入式風格，使用 **Jetty** 或 **Tomcat embedded** 並透過 `main()` 啟動伺服器。

# 19) 測試 Servlet

* **單元測試**：模擬 `HttpServletRequest/Response`。

  * Spring 的 `org.springframework.mock.web.*` 即使沒有使用 Spring 也很方便。
  * 或者使用 Mockito 建立自己的存根。
* **整合測試**：啟動嵌入式 Jetty/Tomcat 並使用 HTTP 客戶端（REST Assured/HttpClient）呼叫端點。
* **端到端測試**：使用瀏覽器自動化（Selenium/WebDriver）進行完整流程測試。

# 20) 效能提示

* 重用昂貴資源（透過 `DataSource` 的資料庫連接池）；在 `destroy()` 中清理。
* 為靜態內容設定快取標頭；將靜態資源卸載到反向代理/CDN。
* 使用 GZIP 壓縮（容器設定或過濾器）。
* 避免長時間操作阻塞 I/O；考慮非同步或佇列。
* 分析記憶體分配和 GC；對於大型負載保持回應串流。

# 21) 常見陷阱

* **實例欄位** 非線程安全 → 競爭條件。
* 在讀取參數前忘記 `req.setCharacterEncoding("UTF-8")`。
* 未經緩衝兩次讀取主體。
* 吞掉異常而不設定 `5xx` 狀態。
* 在同一回應中混用 `getWriter()` 和 `getOutputStream()`。

# 22) 從 `javax.servlet.*` 到 `jakarta.servlet.*`

如果你升級到 Jakarta EE 9+：

* 更改導入 `javax.servlet.*` → `jakarta.servlet.*`。
* 使用支援 Jakarta 的容器（Tomcat 10+、Jetty 11+）。
* 重新建置；大多數程式碼變更僅是導入重新命名。
* 函式庫也必須兼容 Jakarta（注意傳遞依賴項）。

# 23) 最小化 REST 風格範例

```java
@WebServlet(name="UsersApi", urlPatterns="/api/users/*")
public class UsersApi extends HttpServlet {
  @Override protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    resp.setContentType("application/json;charset=UTF-8");
    String id = pathParam(req, 1); // 例如 /api/users/42
    if (id == null) {
      resp.getWriter().write("[{\"id\":1,\"name\":\"A\"}]");
    } else {
      resp.getWriter().write("{\"id\":"+id+",\"name\":\"A\"}");
    }
  }
  private String pathParam(HttpServletRequest req, int idx) {
    String path = req.getPathInfo();        // "/42"
    if (path == null) return null;
    String[] parts = path.split("/");
    return parts.length > idx ? parts[idx] : null;
  }
}
```

# 24) 建置依賴項（經典 `javax.servlet`）

在 Maven 中使用 **Provided** 範圍，因為容器在運行時提供 API：

```xml
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

對於 **Jakarta**：

```xml
<dependency>
  <groupId>jakarta.servlet</groupId>
  <artifactId>jakarta.servlet-api</artifactId>
  <version>6.0.0</version>
  <scope>provided</scope>
</dependency>
```

---

如果你告訴我你的目標容器（Tomcat/Jetty/Liberty）、Java 版本，以及你希望使用同步、非同步還是非阻塞 I/O，我可以為你量身定制一個生產就緒的骨架（包含日誌記錄、CORS、安全性標頭和整潔的 Maven/Gradle 佈局）——沒有表格，只有精簡的程式碼和步驟。