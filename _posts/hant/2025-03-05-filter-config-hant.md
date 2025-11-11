---
audio: false
generated: true
lang: hant
layout: post
title: Java Servlet 篩選器配置
translated: true
type: note
---

### `javax.servlet.FilterConfig` 的運作原理是怎樣的？

在使用 Servlet API 建構的 Java 網路應用程式中，`javax.servlet.FilterConfig` 介面在配置過濾器方面扮演著關鍵角色。過濾器是能在請求到達 servlet 前或離開 servlet 後攔截並處理 HTTP 請求與回應的元件。`FilterConfig` 提供了一種標準化方式，讓網路容器（例如 Tomcat、Jetty）在初始化過濾器時將配置資訊傳遞給它。以下我將解釋 `FilterConfig` 的運作方式、其用途以及如何使用它。

---

#### **什麼是 `FilterConfig`？**
`FilterConfig` 是 `javax.servlet` 套件中的一個介面。網路容器在過濾器的初始化階段使用它來向過濾器提供配置資料。當過濾器在網路應用程式中定義（透過 `web.xml` 或註解）時，容器會建立過濾器的實例，並將一個 `FilterConfig` 物件傳遞給它的 `init` 方法。此物件允許過濾器存取：
- 其自身的初始化參數。
- 網路應用程式的 `ServletContext`。
- 其在配置中定義的名稱。

過濾器實作了 `javax.servlet.Filter` 介面，該介面包含三個方法：`init`、`doFilter` 和 `destroy`。`FilterConfig` 物件專門在 `init` 方法中用於在過濾器開始處理請求前進行設定。

---

#### **過濾器與 `FilterConfig` 的生命週期**
要理解 `FilterConfig` 的運作方式，讓我們看看它在過濾器生命週期中的角色：
1. **容器啟動**：當網路應用程式啟動時，容器讀取過濾器定義（從 `web.xml` 或 `@WebFilter` 註解）並建立每個過濾器的實例。
2. **過濾器初始化**：對於每個過濾器，容器呼叫 `init` 方法，並傳遞一個 `FilterConfig` 物件作為參數。這是每個過濾器實例的一次性操作。
3. **請求處理**：初始化後，過濾器的 `doFilter` 方法會針對每個符合的請求被呼叫。雖然 `FilterConfig` 不會傳遞給 `doFilter`，但過濾器可以在 `init` 期間將來自 `FilterConfig` 的配置資料儲存在實例變數中以供後續使用。
4. **過濾器關閉**：當應用程式關閉時，會呼叫 `destroy` 方法，但 `FilterConfig` 在此階段不參與。

`FilterConfig` 物件在初始化階段至關重要，它使過濾器能夠為請求處理做好準備。

---

#### **`FilterConfig` 的關鍵方法**
`FilterConfig` 介面定義了四個方法，用於提供對配置資訊的存取：

1. **`String getFilterName()`**
   - 傳回過濾器的名稱，該名稱在 `web.xml` 檔案中（在 `<filter-name>` 下）或在 `@WebFilter` 註解中指定。
   - 這對於日誌記錄、除錯或在過濾器鏈中識別過濾器非常有用。

2. **`ServletContext getServletContext()`**
   - 傳回 `ServletContext` 物件，該物件代表整個網路應用程式。
   - `ServletContext` 允許過濾器存取應用程式範圍的資源，例如上下文屬性、日誌記錄設施或用於轉發請求的 `RequestDispatcher`。

3. **`String getInitParameter(String name)`**
   - 透過名稱擷取特定初始化參數的值。
   - 初始化參數是在 `web.xml` 中（在 `<init-param>` 下）或在 `@WebFilter` 註解的 `initParams` 屬性中為過濾器定義的鍵值對。
   - 如果參數不存在，則傳回 `null`。

4. **`Enumeration<String> getInitParameterNames()`**
   - 傳回為過濾器定義的所有初始化參數名稱的 `Enumeration`。
   - 這允許過濾器遍歷其所有參數，並使用 `getInitParameter` 擷取它們的值。

這些方法由網路容器提供的具體類別（例如 Tomcat 內部的 `FilterConfigImpl`）實作。作為開發者，您僅透過此介面與 `FilterConfig` 互動。

---

#### **如何配置 `FilterConfig`**
過濾器及其配置可以透過兩種方式定義：
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
   - `<init-param>` 將初始化參數指定為鍵值對。

2. **使用註解（Servlet 3.0 及更高版本）**：
   ```java
   import javax.servlet.annotation.WebFilter;
   import javax.servlet.annotation.WebInitParam;

   @WebFilter(
       filterName = "MyFilter",
       urlPatterns = "/*",
       initParams = @WebInitParam(name = "excludeURLs", value = "/login,/signup")
   )
   public class MyFilter implements Filter {
       // Implementation
   }
   ```
   - `@WebFilter` 註解定義了過濾器的名稱、URL 模式以及初始化參數。

在這兩種情況下，容器都會使用此配置來建立一個 `FilterConfig` 物件，並將其傳遞給過濾器的 `init` 方法。

---

#### **實際範例**
以下是一個過濾器在實踐中如何使用 `FilterConfig` 的範例：

```java
import javax.servlet.*;
import java.io.IOException;

public class MyFilter implements Filter {
    private String excludeURLs; // 用於儲存配置資料的實例變數

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // 取得過濾器的名稱
        String filterName = filterConfig.getFilterName();
        System.out.println("Initializing filter: " + filterName);

        // 取得初始化參數
        excludeURLs = filterConfig.getInitParameter("excludeURLs");
        if (excludeURLs != null) {
            System.out.println("Exclude URLs: " + excludeURLs);
        }

        // 可選擇性地儲存 ServletContext 以供後續使用
        ServletContext context = filterConfig.getServletContext();
        context.log("Filter " + filterName + " initialized");
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // 使用 excludeURLs 來決定是否過濾該請求
        chain.doFilter(request, response); // 繼續到下一個過濾器或 servlet
    }

    @Override
    public void destroy() {
        // 清理程式碼
    }
}
```

- **在 `init` 中**：過濾器擷取其名稱、一個初始化參數（`excludeURLs`）以及 `ServletContext`。它將 `excludeURLs` 儲存在一個實例變數中，以便在 `doFilter` 中使用。
- **在 `doFilter` 中**：過濾器可以使用儲存的配置（例如 `excludeURLs`）來處理請求。

---

#### **關於 `FilterConfig` 的關鍵點**
- **過濾器特定範圍**：`FilterConfig` 中的初始化參數是針對過濾器實例的。不同的過濾器可以擁有同名但不同值的參數。
- **與 `ServletContext` 的對比**：`ServletContext`（透過 `getServletContext()` 存取）提供應用程式範圍的初始化參數和資源，與 `FilterConfig` 中過濾器特定的參數不同。
- **生命週期中的單次使用**：`FilterConfig` 僅在 `init` 中被傳遞一次。如果過濾器後續需要其資料（例如在 `doFilter` 中），則必須將資料儲存在實例變數中。
- **容器提供**：`FilterConfig` 是一個介面，具體實作由網路容器提供。

---

#### **總結**
`javax.servlet.FilterConfig` 的運作方式是透過在過濾器初始化期間向其提供配置資訊。網路容器將一個 `FilterConfig` 物件傳遞給過濾器的 `init` 方法，允許過濾器：
- 存取其名稱（`getFilterName`）。
- 擷取初始化參數（`getInitParameter`、`getInitParameterNames`）。
- 透過 `ServletContext`（`getServletContext`）與網路應用程式互動。

這使得過濾器能夠靈活配置——透過 `web.xml` 或註解——並使它們能夠有效地處理 HTTP 請求和回應。無論您是排除特定 URL、設定逾時還是記錄訊息，`FilterConfig` 都是過濾器配置與其運行時行為之間的橋樑。