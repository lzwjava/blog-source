---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 春季會話、JSESSIONID 與伺服器偵測
translated: true
type: note
---

讓我們將這個問題拆解為兩部分：**Spring Session/JSESSIONID** 的運作原理，以及如何判斷 Spring 應用程式是運行在 **Tomcat 還是 Netty** 上。

---

## 1. Spring Session 與 `JSESSIONID` 的運作方式

* **JSESSIONID** 是 servlet 容器（Tomcat、Jetty、Undertow 等）使用的標準 HTTP 工作階段識別符。
* 當客戶端首次發出需要建立工作階段的請求時，容器（或使用 Spring Session 時由它負責）會產生一個隨機工作階段 ID，將工作階段資料儲存在伺服器端，並透過 `Set-Cookie` 標頭將 ID 傳回給客戶端。
* 客戶端在後續請求中會攜帶這個 `JSESSIONID` cookie，讓伺服器能夠找到對應的工作階段。
* 預設情況下，工作階段資料會**儲存在 servlet 容器的記憶體中**。例如：

  * Tomcat 會將工作階段儲存在記憶體中（除非你配置了持久化設定）。
  * 如果你使用 **Spring Session**，工作階段儲存可以被外部化（Redis、JDBC、Hazelcast 等），同時仍使用 `JSESSIONID` cookie 來識別使用者。
* Spring Security 及其他 Spring 功能都依賴此工作階段機制來處理身份驗證與狀態管理。

---

## 2. 如何判斷 Spring 使用的是 Tomcat 還是 Netty

Spring Boot 可以在不同的嵌入式伺服器上運行：

* **Tomcat**（Spring Boot starter-web 的預設選項）
* **Jetty**（若你替換了相依套件）
* **Undertow**（替代的 servlet 容器）
* **Netty**（由 Spring WebFlux 使用，非基於 servlet）

### 檢查方法：

1. **檢查你的相依套件**

   * 如果你的 `pom.xml` 或 `build.gradle` 包含 `spring-boot-starter-web`，則預設使用 **Tomcat**。
   * 如果包含 `spring-boot-starter-webflux`，則預設使用 **Netty**。

2. **查看啟動日誌**

   * 當應用程式啟動時，Spring Boot 會記錄所使用的嵌入式伺服器。
   * 範例（Tomcat）：

     ```
     Tomcat started on port(s): 8080 (http)
     ```
   * 範例（Netty）：

     ```
     Netty started on port(s): 8080
     ```

3. **檢查運行時類別**

   * 透過程式碼或 Actuator 端點，檢查載入了哪些伺服器類別。
   * Tomcat 類別以 `org.apache.catalina.` 開頭。
   * Netty 類別以 `io.netty.` 開頭。

---

✅ **總結**：

* `JSESSIONID` 僅是一個指向伺服器端工作階段的 cookie，由 Tomcat（預設）或 Spring Session（Redis/資料庫）管理。
* 你可以透過檢查相依套件、啟動日誌或運行時類別，來判斷 Spring 使用的是 **Tomcat 還是 Netty**。

---

你是否也希望我解釋 **Spring MVC（Tomcat）與 Spring WebFlux（Netty）在工作階段處理上的差異**？這正是兩者區別最關鍵的地方。