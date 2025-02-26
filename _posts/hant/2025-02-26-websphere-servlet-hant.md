---
audio: true
lang: hant
layout: post
title: WebSphere Liberty Profile 中的 Servlet 版本
translated: true
---

### 了解錯誤

`console.log` 的錯誤訊息指出 `DDParser ParseException` 相關於 `spring-web-6.2.3.jar` 中的 `web-fragment.xml` 文件。具體來說，部署描述符指定版本 "50"（對應 Servlet 5.0），但 WebSphere Liberty Profile (WLP) 伺服器目前配置為版本 "40"（Servlet 4.0）。這種不匹配的原因是：

- **Servlet 5.0** 是 Jakarta EE 9 的一部分，並且是新版本的 Spring Boot（例如 Spring Boot 3.x，包括 `spring-web-6.2.3.jar`）所需的。
- **Servlet 4.0** 是 Java EE 8 的一部分，WLP 可能配置了 `javaee-8.0` 功能，這不支持 Servlet 5.0。

要解決這個問題，您需要將 WLP 支持的 Servlet 版本與應用程序所需的版本對齊。推薦的解決方案是更新 WLP 以支持 Servlet 5.0，方法是啟用 `jakartaee-9.1` 功能。

---

### 解決方案：更新 WLP 以支持 Servlet 5.0

以下是通過更新 WLP 使用 `jakartaee-9.1` 功能來解決問題的方法，該功能包括對 Servlet 5.0 的支持：

#### 1. **定位 `server.xml` 文件**
- `server.xml` 配置文件定義了 WLP 中啟用的功能。
- 它通常位於伺服器目錄中，例如 `/opt/ibm/wlp/usr/servers/myServer/server.xml`，其中 `myServer` 是您的伺服器名稱。

#### 2. **編輯 `server.xml` 文件**
- 使用文本編輯器打開 `server.xml` 文件。
- 找到 `<featureManager>` 部分，該部分列出了伺服器啟用的功能。它可能看起來像這樣：
  ```xml
  <featureManager>
      <feature>javaee-8.0</feature>
  </featureManager>
  ```
- 將 `javaee-8.0` 功能替換為 `jakartaee-9.1` 以啟用 Servlet 5.0 支持：
  ```xml
  <featureManager>
      <feature>jakartaee-9.1</feature>
  </featureManager>
  ```
- 保存文件。

#### 3. **在 WLP 開發模式下應用更改（如果適用）**
- 如果您在 **開發模式** 下運行 WLP（例如使用 `wlp/bin/server run` 命令或 IDE 集成），可以按以下方法應用更改：
  - **手動重啟：**
    - 停止伺服器：
      ```bash
      /opt/ibm/wlp/bin/server stop myServer
      ```
    - 再次啟動伺服器：
      ```bash
      /opt/ibm/wlp/bin/server start myServer
      ```
  - **開發模式熱重載：**
    - 如果 WLP 在開發模式下運行（例如通過 `server run` 或 IDE），它可能會自動檢測到 `server.xml` 的更改。但是，為了確保新功能被加載，建議重啟。

#### 4. **驗證修復**
- 重啟伺服器後，重新部署您的應用程序（例如，將 WAR 文件複製到 `dropins` 目錄或使用您的部署方法）。
- 檢查伺服器日誌以確認成功部署。查找類似以下的消息：
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  ```
  CWWKZ0001I: Application myapp started in X.XXX seconds.
  ```
- 訪問您的應用程序（例如 `http://localhost:9080/myapp/`）以確認它沒有錯誤運行。

---

### 替代解決方案：降級 Spring Boot

如果將 WLP 更新到 `jakartaee-9.1` 不是選項（例如，由於與其他應用程序的兼容性約束），您可以將 Spring Boot 應用程序降級到與 Servlet 4.0 兼容的版本：

#### 1. **切換到 Spring Boot 2.7.x**
- Spring Boot 2.7.x 支持 Servlet 4.0（以及早期版本如 Servlet 3.1）。
- 更新您的 `pom.xml` 以使用 Spring Boot 2.7.x：
  ```xml
  <parent>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-parent</artifactId>
      <version>2.7.18</version> <!-- 使用最新的 2.7.x 版本 -->
      <relativePath/>
  </parent>
  ```

#### 2. **重新構建和重新部署**
- 重新構建您的應用程序：
  ```bash
  mvn clean package
  ```
- 將生成的 WAR 文件重新部署到 WLP，並驗證它在沒有錯誤的情況下啟動。

---

### 摘要
- **錯誤原因：** 您的應用程序 (`spring-web-6.2.3.jar`) 需要 Servlet 5.0，但 WLP 配置為 Servlet 4.0。
- **首選修復方法：** 更新 WLP 以使用 `jakartaee-9.1` 功能，方法是修改 `server.xml` 並重啟伺服器。
- **替代修復方法：** 降級到 Spring Boot 2.7.x 以匹配 WLP 的 Servlet 4.0 支持。

首選解決方案（更新 WLP）確保您的應用程序可以使用 Spring Boot 3.x 和 Jakarta EE 9 的最新功能。按照上述步驟解決問題並成功部署您的應用程序。