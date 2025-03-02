---
audio: true
generated: true
lang: hant
layout: post
title: WebSphere Liberty Profile 部署問題排除
translated: true
---

當你嘗試訪問你的 Spring Boot 應用程序於 `http://localhost:9080/myapp/` 並遇到 WebSphere Liberty Profile (WLP) 上的「上下文根未找到」錯誤，這表示 WLP 沒有成功在預期的上下文根 (`/myapp`) 下部署你的應用程序。這個問題通常是由於部署配置、伺服器設置或 WAR 文件本身的問題引起的。以下是一個全面的指南來排查和解決這個問題。

---

### 了解問題
「上下文根未找到」錯誤意味著 WLP 無法找到部署在 `/myapp` 的應用程序。通常，當你將一個名為 `myapp.war` 的 WAR 文件放在 WLP 的 `dropins` 目錄中時，它應該自動部署並以上下文根 `/myapp` 可訪問於 `http://localhost:9080/myapp/`。由於這沒有發生，我們需要調查部署失敗的原因。

---

### 排查步驟

#### 1. **檢查伺服器日誌以獲取部署消息**
第一步是確認 WLP 是否已部署你的應用程序。

- **定位日誌:**
  - 如果你的伺服器名為 `myServer`，檢查日誌於：
    ```
    /opt/ibm/wlp/usr/servers/myServer/logs/messages.log
    ```
    或
    ```
    /opt/ibm/wlp/usr/servers/myServer/logs/console.log
    ```
  - 如果你使用的是預設伺服器，將 `myServer` 替換為 `defaultServer`。

- **查找部署確認:**
  - 你應該看到一條消息如下：
    ```
    [AUDIT   ] CWWKT0016I: Web 應用程序可用 (default_host): http://localhost:9080/myapp/
    ```
    這表示應用程序已部署並可用。
  - 此外，查找：
    ```
    CWWKZ0001I: 應用程序 myapp 在 X.XXX 秒內啟動。
    ```
    這確認應用程序已成功啟動。

- **操作:**
  - 如果這些消息不存在，應用程序沒有部署。查找日誌中的任何 `ERROR` 或 `WARNING` 消息，這些消息可能會指出原因（例如，缺少功能、文件權限或啟動失敗）。
  - 如果你看到 Spring Boot 啟動日誌（例如，Spring Boot 標語），應用程序正在加載，問題可能與上下文根或 URL 映射有關。

#### 2. **驗證 WAR 文件的位置和權限**
確保 WAR 文件正確放置在 `dropins` 目錄中並對 WLP 可訪問。

- **檢查路徑:**
  - 對於名為 `myServer` 的伺服器，WAR 文件應位於：
    ```
    /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```
  - 如果使用 `defaultServer`，相應調整：
    ```
    /opt/ibm/wlp/usr/servers/defaultServer/dropins/myapp.war
    ```

- **驗證權限:**
  - 確保 WLP 進程對文件具有讀取權限。在類 Unix 系統上，運行：
    ```bash
    ls -l /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```
    文件應該可被運行 WLP 的用戶讀取（例如，`rw-r--r--`）。

- **操作:**
  - 如果文件丟失或放置錯誤，將其複製到正確的 `dropins` 目錄：
    ```bash
    cp target/myapp.war /opt/ibm/wlp/usr/servers/myServer/dropins/
    ```
  - 如果需要，修正權限：
    ```bash
    chmod 644 /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```

#### 3. **確認 `dropins` 監控在 `server.xml` 中**
WLP 的 `dropins` 目錄默認啟用，但自定義配置可能會禁用它。

- **檢查 `server.xml`:**
  - 打開伺服器配置文件：
    ```
    /opt/ibm/wlp/usr/servers/myServer/server.xml
    ```
  - 查找 `applicationMonitor` 元素：
    ```xml
    <applicationMonitor updateTrigger="polled" pollingRate="5s" dropins="dropins" />
    ```
    這確認 WLP 每 5 秒監控 `dropins` 目錄以獲取新應用程序。

- **操作:**
  - 如果不存在，在 `<server>` 標籤內添加上述行，或確保沒有覆蓋配置禁用 `dropins`。
  - 更改後重啟伺服器：
    ```bash
    /opt/ibm/wlp/bin/server stop myServer
    /opt/ibm/wlp/bin/server start myServer
    ```

#### 4. **確保啟用所需功能**
WLP 需要特定功能來部署 Spring Boot WAR 文件，例如 Servlet 支持。

- **檢查 `server.xml`:**
  - 驗證 `featureManager` 部分包含：
    ```xml
    <featureManager>
        <feature>javaee-8.0</feature>
    </featureManager>
    ```
    `javaee-8.0` 功能包括 Servlet 4.0，與 Spring Boot 兼容。或者，至少應存在 `servlet-4.0`。

- **操作:**
  - 如果缺失，添加功能並重啟伺服器。

#### 5. **驗證 WAR 文件結構**
腐敗或結構不正確的 WAR 文件可能會阻止部署。

- **檢查 WAR:**
  - 解壓縮 WAR 文件以驗證其內容：
    ```bash
    unzip -l myapp.war
    ```
  - 查找：
    - `WEB-INF/classes/com/example/demo/HelloController.class`（你的控制器類）。
    - `WEB-INF/lib/` 包含 Spring Boot 依賴（例如，`spring-web-x.x.x.jar`）。

- **操作:**
  - 如果結構不正確，重建 WAR：
    ```bash
    mvn clean package
    ```
    確保你的 `pom.xml` 設置 `<packaging>war</packaging>` 並將 `spring-boot-starter-tomcat` 設置為 `<scope>provided</scope>`。

#### 6. **通過 `apps` 目錄進行替代部署**
如果 `dropins` 失敗，嘗試通過 `apps` 目錄明確部署應用程序。

- **步驟:**
  - 移動 WAR 文件：
    ```bash
    mv /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war /opt/ibm/wlp/usr/servers/myServer/apps/
    ```
  - 編輯 `server.xml` 以添加：
    ```xml
    <application id="myapp" name="myapp" type="war" location="${server.config.dir}/apps/myapp.war">
        <context-root>/myapp</context-root>
    </application>
    ```
  - 重啟伺服器：
    ```bash
    /opt/ibm/wlp/bin/server restart myServer
    ```

- **再次測試:**
  - 訪問 `http://localhost:9080/myapp/`。如果成功，問題出在 `dropins`。

#### 7. **驗證伺服器狀態**
確保伺服器正確運行。

- **檢查狀態:**
  ```bash
  /opt/ibm/wlp/bin/server status myServer
  ```
  - 如果已停止，啟動它：
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **測試 WLP 本身:**
  - 訪問 `http://localhost:9080/`。如果 WLP 運行，你將看到一個歡迎頁面（除非被覆蓋）。如果這失敗，則存在更廣泛的伺服器問題。

---

### 解決方案
要修復「上下文根未找到」錯誤：

1. **從這裡開始:**
   - 檢查伺服器日誌（`messages.log` 或 `console.log`）以獲取部署消息或錯誤。
   - 確保 `myapp.war` 在 `dropins` 目錄中並具有正確權限。

2. **下一步:**
   - 驗證 `server.xml` 啟用 `javaee-8.0` 功能並監控 `dropins`。
   - 如果未解決，通過 `apps` 目錄部署，並在 `server.xml` 中添加明確的 `<application>` 配置。

3. **最終驗證:**
   - 更改後重啟 WLP 並訪問 `http://localhost:9080/myapp/`。如果部署成功，你應該看到「Hello World!」。

通過遵循這些步驟，你將識別問題是否與伺服器配置、WAR 放置或 WAR 文件本身有關，並相應解決。