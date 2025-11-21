---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4.1-fast
title: 網頁容器與Spring Boot請求過濾器比較
translated: true
type: note
---

### 概述
IBM WebSphere Application Server（WAS，傳統版或 Liberty）與 Spring Boot 均基於標準 Java Servlet API 的 `javax.servlet.Filter` 和 `FilterChain`，支援**請求處理鏈**的概念。在此機制中，傳入的 HTTP 請求會經過一系列篩選器，才到達 servlet（或控制器/處理器），而回應在返回途中亦可被修改。

- 篩選器允許對請求/回應進行預處理（例如身份驗證、日誌記錄、壓縮）和後處理。
- 核心機制 — 實作 `Filter`，呼叫 `chain.doFilter(request, response)` 以繼續處理 — **完全相同**，因為兩者均在 Servlet 容器中運行（WAS 擁有其完整的 Java EE 網頁容器；Spring Boot 預設嵌入 Tomcat/Jetty/Undertow）。

基本的「請求鏈篩選器」運作方式並無根本差異。然而，由於各平台的架構不同，篩選器的配置、排序與整合方式存在顯著區別。

### 關鍵比較

| 面向                  | IBM WebSphere Application Server（傳統版/Liberty） | Spring Boot |
|-------------------------|---------------------------------------------------------|-------------|
| **底層機制** | 標準 Servlet 篩選器（`javax.servlet.Filter`）。WAS 在某些情境下（例如入口網站或自訂 IBM API）還擁有專有擴展，如 `ChainedRequest`/`ChainedResponse`，用於內部請求轉發/鏈接。 | 標準 Servlet 篩選器。Spring Boot 會自動註冊任何帶有 `@Component` 的篩選器 Bean，或您可透過 `FilterRegistrationBean` 明確註冊。 |
| **配置**       | 主要透過 `web.xml`（宣告式）或程式化註冊。對於全域篩選器（跨所有應用）：配置複雜 — 需要共享函式庫、自訂監聽器或 IBM 特定擴展（無類似 Tomcat 的簡單伺服器範圍 web.xml）。 | 約定優於配置：使用 `@Component` + `@Order` 註解即可自動註冊，或使用 `FilterRegistrationBean` 進行細粒度控制（URL 模式、分派器類型）。對開發者極為友好。 |
| **排序**            | 在 `web.xml` 中定義順序，或透過程式化方式使用 `@Order`。全域排序較為棘手。 | 使用 `@Order(n)`（數值越低越優先）或 `Ordered` 介面輕鬆實現。Spring Boot 自動管理鏈接順序。 |
| **安全篩選器鏈** | 使用標準 Servlet 篩選器或 IBM 特定安全機制（例如 TAI、JEE 角色）。無內建如 Spring Security 的安全鏈。 | Spring Security 提供強大的 `SecurityFilterChain`（透過 `FilterChainProxy`），包含 15+ 個有序篩選器（CSRF、身份驗證、會話管理等）。可高度自訂，支援每個路徑多個鏈接。 |
| **添加自訂篩選器的便利性** | 配置較為繁瑣，尤其是對於全域/跨應用篩選器。通常需要管理主控台調整或共享函式庫。 | 極其簡單 — 僅需一個 `@Component` Bean 或配置類別。自動整合至嵌入式容器中。 |
| **部署模式**    | 傳統完整 Java EE 伺服器。應用以 WAR/EAR 形式部署。支援重量級企業功能（集群、事務、JMS）。 | 嵌入式容器（預設為獨立可執行 JAR）。可將 WAR 部署至外部伺服器（包括 WAS）。輕量級/面向微服務。 |
| **效能/開銷**| 較高開銷（完整應用伺服器）。傳輸鏈、網頁容器通道增加層次。 | 較低開銷（嵌入式輕量級容器）。啟動更快，資源使用更少。 |
| **篩選器運行時機**     | 在 WAS 網頁容器入站鏈中運行。可擁有伺服器層級的傳輸篩選器（例如 TCP 通道上的 IP 篩選）。 | 在嵌入式容器的篩選器鏈中運行。Spring Boot 會添加自身的篩選器（錯誤處理、字元編碼等）。 |
| **常見使用場景**    | 企業單體應用、入口網站、需要全域安全/日誌記錄的傳統 Java EE 應用。 | 現代微服務、REST API、結合 Spring Security 的快速開發。 |

### 實務範例

**標準自訂篩選器（相同程式碼在兩者中均可運行）：**
```java
@Component  // 僅 Spring Boot 使用；在 WAS 中需於 web.xml 宣告
@Order(1)
public class LoggingFilter implements Filter {
    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
            throws IOException, ServletException {
        System.out.println("Request: " + ((HttpServletRequest) req).getRequestURI());
        chain.doFilter(req, res);  // 關鍵：傳遞給下一個篩選器/servlet
    }
    // init/destroy...
}
```

**在 Spring Boot 中（自動註冊）：**
僅需上述類別 + `@Component`。

**在 WAS 中：**
於 `web.xml` 中添加：
```xml
<filter>
    <filter-name>LoggingFilter</filter-name>
    <filter-class>com.example.LoggingFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>LoggingFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

### 何時選擇何者
- **使用 WAS 篩選器** 若您處於傳統 IBM 環境、需要完整 Java EE 功能，或必須在不修改程式碼的情況下對多個應用應用全域篩選器。
- **使用 Spring Boot 篩選器**（特別是結合 Spring Security）適用於新專案/綠地專案、微服務、快速迭代，或當您需要多個安全鏈和簡便排序時。

總而言之，**請求鏈篩選器的概念是相同的**（Servlet 規範），但**對於大多數現代使用場景，Spring Boot 使其更簡單且功能更強大**，而 WAS 則更偏向企業級重量級和配置密集型。

[IBM WAS Servlet 篩選文件](https://www.ibm.com/docs/en/was/9.0.5?topic=extensions-servlet-filtering)  
[Spring Boot 自訂篩選器](https://www.baeldung.com/spring-boot-add-filter)  
[Spring Security 篩選器鏈](https://docs.spring.io/spring-security/reference/servlet/architecture.html)