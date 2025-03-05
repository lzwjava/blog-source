---
audio: true
generated: true
lang: hant
layout: post
title: Java Servlet 篩選器配置
translated: true
---

### `javax.servlet.FilterConfig` 的工作原理

在使用 Servlet API 构建的 Java Web 應用程式中，`javax.servlet.FilterConfig` 介面在配置過濾器方面扮演著關鍵角色。過濾器是拦截和處理 HTTP 要求和回應的組件，在它們到達 servlet 或離開 servlet 之前。`FilterConfig` 提供了一種標準化的方式來在過濾器被 Web 容器（例如 Tomcat、Jetty）初始化時將配置信息傳遞給過濾器。以下，我將解釋 `FilterConfig` 的工作原理、其目的以及如何使用它。

---

#### **什麼是 `FilterConfig`？**
`FilterConfig` 是 `javax.servlet` 包中的一個介面。它由 Web 容器用來在過濾器的初始化階段向過濾器提供配置數據。當過濾器在 Web 應用程式中定義（通過 `web.xml` 或註解）時，容器會創建過濾器的實例並將 `FilterConfig` 對象傳遞給其 `init` 方法。這個對象允許過濾器訪問：
- 它自己的初始化參數。
- Web 應用程式的 `ServletContext`。
- 它在配置中定義的自己的名稱。

過濾器實現 `javax.servlet.Filter` 介面，該介面包括三個方法：`init`、`doFilter` 和 `destroy`。`FilterConfig` 對象特別在 `init` 方法中用來在過濾器開始處理要求之前設置過濾器。

---

#### **過濾器和 `FilterConfig` 的生命週期**
要理解 `FilterConfig` 的工作原理，讓我們看看它在過濾器生命週期中的角色：
1. **容器啟動**：當 Web 應用程式啟動時，容器讀取過濾器定義（從 `web.xml` 或 `@WebFilter` 注解）並創建每個過濾器的實例。
2. **過濾器初始化**：對於每個過濾器，容器調用 `init` 方法，並將 `FilterConfig` 對象作為參數傳遞。這是每個過濾器實例的一次操作。
3. **要求處理**：初始化後，過濾器的 `doFilter` 方法會對每個匹配的要求進行調用。雖然 `FilterConfig` 不是傳遞給 `doFilter`，但過濾器可以在 `init` 中將配置數據存儲在實例變量中以便稍後使用。
4. **過濾器關閉**：當應用程式關閉時，調用 `destroy` 方法，但 `FilterConfig` 此時不涉及。

`FilterConfig` 對象在初始化階段至關重要，使過濾器能夠為要求處理做好準備。

---

#### **`FilterConfig` 的關鍵方法**
`FilterConfig` 介面定義了四個方法，提供對配置信息的訪問：

1. **`String getFilterName()`**
   - 返回在 `web.xml` 文件（在 `<filter-name>` 下）或 `@WebFilter` 注解中指定的過濾器名稱。
   - 這對於記錄、調試或在過濾器鏈中識別過濾器很有用。

2. **`ServletContext getServletContext()`**
   - 返回 `ServletContext` 對象，該對象表示整個 Web 應用程式。
   - `ServletContext` 允許過濾器訪問應用程式範圍的資源，例如上下文屬性、記錄設施或 `RequestDispatcher` 以轉發要求。

3. **`String getInitParameter(String name)`**
   - 通過其名稱檢索特定初始化參數的值。
   - 初始化參數是為過濾器在 `web.xml`（在 `<init-param>` 下）或 `@WebFilter` 注解的 `initParams` 屬性中定義的鍵值對。
   - 如果參數不存在，則返回 `null`。

4. **`Enumeration<String> getInitParameterNames()`**
   - 返回為過濾器定義的所有初始化參數名稱的 `Enumeration`。
   - 這允許過濾器遍歷所有其參數並使用 `getInitParameter` 獲取其值。

這些方法由 Web 容器（例如 Tomcat 的內部 `FilterConfigImpl`）提供的具體類實現。作為開發者，您僅通過這個介面與 `FilterConfig` 互動。

---

#### **如何配置 `FilterConfig`**
過濾器及其配置可以通過兩種方式定義：
1. **使用 `web.xml`（部署描述符）**：
   ```xml
   <filter>
       <filter-name>MyFilter</filter-name>
       <filter-class>com.example.MyFilter</filter-class>
       <init-param>
           <param-name>excludeURLs</param-name>
           <param-value>/login,/signup</param-value>
       </init-param>
   </filter>
   <filter-mapping>
       <filter-name>MyFilter</filter-name>
       <url-pattern>/*</url-pattern>
   </filter-mapping>
   ```
   - `<filter-name>` 定義過濾器的名稱。
   - `<init-param>` 指定初始化參數作為鍵值對。

2. **使用註解（Servlet 3.0 及以後）**：
   ```java
   import javax.servlet.annotation.WebFilter;
   import javax.servlet.annotation.WebInitParam;

   @WebFilter(
       filterName = "MyFilter",
       urlPatterns = "/*",
       initParams = @WebInitParam(name = "excludeURLs", value = "/login,/signup")
   )
   public class MyFilter implements Filter {
       // 實現
   }
   ```
   - `@WebFilter` 注解定義過濾器的名稱、URL 模式和初始化參數。

在兩種情況下，容器都使用這些配置來創建 `FilterConfig` 對象並將其傳遞給過濾器的 `init` 方法。

---

#### **實際範例**
以下是過濾器如何在實踐中使用 `FilterConfig`：

```java
import javax.servlet.*;
import java.io.IOException;

public class MyFilter implements Filter {
    private String excludeURLs; // 實例變量以存儲配置數據

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // 獲取過濾器的名稱
        String filterName = filterConfig.getFilterName();
        System.out.println("初始化過濾器: " + filterName);

        // 獲取一個初始化參數
        excludeURLs = filterConfig.getInitParameter("excludeURLs");
        if (excludeURLs != null) {
            System.out.println("排除 URL: " + excludeURLs);
        }

        // 可選地將 ServletContext 存儲以便稍後使用
        ServletContext context = filterConfig.getServletContext();
        context.log("過濾器 " + filterName + " 初始化");
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // 使用 excludeURLs 來決定是否過濾要求
        chain.doFilter(request, response); // 繼續到下一個過濾器或 servlet
    }

    @Override
    public void destroy() {
        // 清理代碼
    }
}
```

- **在 `init`**：過濾器檢索其名稱、一個初始化參數（`excludeURLs`）和 `ServletContext`。它將 `excludeURLs` 存儲在實例變量中以便在 `doFilter` 中使用。
- **在 `doFilter`**：過濾器可以使用存儲的配置（例如 `excludeURLs`）來處理要求。

---

#### **關於 `FilterConfig` 的關鍵點**
- **過濾器特定範圍**：`FilterConfig` 中的初始化參數是特定於過濾器實例的。不同的過濾器可以具有相同名稱但不同值的參數。
- **與 `ServletContext` 對比**：`ServletContext`（通過 `getServletContext()` 訪問）提供應用程式範圍的初始化參數和資源，與 `FilterConfig` 中的過濾器特定參數不同。
- **生命週期中的單次使用**：`FilterConfig` 只傳遞給 `init`。如果過濾器稍後需要其數據（例如在 `doFilter` 中），則必須將數據存儲在實例變量中。
- **容器提供**：`FilterConfig` 是一個介面，Web 容器提供具體實現。

---

#### **摘要**
`javax.servlet.FilterConfig` 通過在初始化過濾器時向過濾器提供配置信息來工作。Web 容器將 `FilterConfig` 對象傳遞給過濾器的 `init` 方法，使過濾器能夠：
- 訪問其名稱（`getFilterName`）。
- 檢索初始化參數（`getInitParameter`、`getInitParameterNames`）。
- 通過 `ServletContext` 互動與 Web 應用程式（`getServletContext`）。

這使過濾器能夠靈活配置（通過 `web.xml` 或註解）並準備有效地處理 HTTP 要求和回應。無論您是排除某些 URL、設置超時還是記錄消息，`FilterConfig` 都是過濾器配置和其運行行為之間的橋樑。