---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: 理解 JSESSIONID 與網頁工作階段
translated: true
type: note
---

### 什麼是 Web 應用程式中的 Sessions？

Sessions 讓 Web 應用程式能在原本無狀態的 HTTP 請求之間維持狀態。在 Java servlets 和 Spring 中，sessions 將用戶專屬資料（例如登入狀態或購物車項目）儲存在伺服器端，並透過唯一識別符連結，該識別符會以 cookie 或 URL 參數形式傳送給客戶端。

JSESSIONID 是 Java EE 容器（例如 Tomcat、Jetty）及基於 servlets 構建的 Spring 應用程式所使用的標準 session 識別符 cookie 名稱。

### JSESSIONID 的運作原理

1. **Session 建立**：
   - 當用戶首次存取 Web 應用程式時，servlet 容器（或 Spring 透過 `HttpSession`）會在伺服器上建立新的 `HttpSession` 物件。
   - 它會分配一個唯一 ID（例如 "A1B2C3D4E5F6"）作為 session ID。
   - 此 ID 透過 `Set-Cookie` header 傳送給客戶端：`JSESSIONID=A1B2C3D4E5F6; Path=/; HttpOnly`。

2. **客戶端-伺服器互動**：
   - 在後續請求中，客戶端會在 `Cookie` header 中包含 `JSESSIONID`（若使用 cookies），或將其附加至 URL（例如 `/app/page;jsessionid=A1B2C3D4E5F6`，用於 URL 重寫，但現已較少使用）。
   - 容器使用此 ID 從記憶體或儲存空間（如資料庫或 Redis，若已配置）中擷取對應的 `HttpSession`。
   - 資料在請求之間持續存在，並限定於該 session 範圍內。

3. **過期與清理**：
   - Sessions 在閒置一段時間後會過期（Tomcat 預設約 30 分鐘，可透過 `web.xml` 或 Spring 的 `server.servlet.session.timeout` 配置）。
   - 逾時後，session 會失效，且 ID 將變得無用。
   - `HttpOnly` 標記可防止 JavaScript 存取，增強安全性；可添加 `Secure` 標記以用於 HTTPS。

Sessions 預設儲存在記憶體中（例如 Tomcat 的 `StandardManager`），但為實現可擴展性，可使用 `PersistentManager` 或外部儲存進行持久化。

### 在 Java Servlets 中管理 Sessions

在純 servlets 中（例如 javax.servlet）：

- **取得 Session**：
  ```java
  HttpServletRequest request = // 來自 doGet/doPost
  HttpSession session = request.getSession(); // 若不存在則建立
  HttpSession session = request.getSession(false); // 擷取現有 session 或傳回 null
  ```

- **儲存/擷取資料**：
  ```java
  session.setAttribute("username", "exampleUser");
  String user = (String) session.getAttribute("username");
  ```

- **失效處理**：
  ```java
  session.invalidate();
  ```

在 `web.xml` 中配置逾時設定：
```xml
<session-config>
    <session-timeout>30</session-timeout> <!-- 單位為分鐘 -->
</session-config>
```

### 在 Spring Framework 中管理 Sessions

Spring 基於 servlet sessions 構建，但提供了抽象層：

- **直接使用 HttpSession**：
  與 servlets 類似；在控制器中注入：
  ```java
  @Controller
  public class MyController {
      @RequestMapping("/login")
      public String login(HttpSession session) {
          session.setAttribute("user", "example");
          return "redirect:/dashboard";
      }
  }
  ```

- **Spring Security 整合**：
  若使用 Spring Security，sessions 會管理認證。在 `application.properties` 中配置：
  ```
  server.servlet.session.timeout=30m
  ```

- **分散式 Sessions**：
  針對分散式環境，可使用 Spring Session 搭配 Redis 或 JDBC：
  - 添加依賴：`spring-session-data-redis`。
  - 在 `@Configuration` 類別中配置：
    ```java
    @EnableRedisHttpSession
    public class SessionConfig { }
    ```
  這使得 sessions 能在伺服器之間擴展，將 JSESSIONID 連結儲存在 Redis 中。

### 最佳實踐與安全性

- **安全性**：始終使用 `HttpOnly` 和 `Secure` cookies。避免在 sessions 中儲存敏感資料；使用伺服器端加密。
- **逾時設定**：設定合理的逾時時間以減少記憶體使用。
- **可擴展性**：針對負載平衡應用，使用黏性 sessions（例如透過 AWS ELB）或共享儲存（如 Redis）以防止 session 遺失。
- **測試**：使用 Postman 等工具檢查 JSESSIONID cookies 或模擬請求。
- **替代方案**：針對 REST API，可考慮使用 JWTs 代替伺服器端 sessions 以避免狀態維護。

此機制在 Java EE 規範中已標準化；詳情請參閱 Oracle Java EE 文檔或 Spring Boot 參考資料。若您的應用程式運行於容器中，請查閱其文檔以了解特定行為（例如 Tomcat 的 session 管理）。