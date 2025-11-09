---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: WebSphere 開發專用 IntelliJ IDEA
translated: true
type: note
---

### 使用 IntelliJ IDEA 進行 IBM WebSphere Application Server (WAS) 開發

IntelliJ IDEA 是開發針對 IBM WebSphere Application Server (WAS) 的 Java EE 應用程式的可靠選擇。它支援 WAS 所遵循的 Java EE 標準，並提供出色的工具來建置、部署和偵錯企業級應用程式。雖然 Eclipse 透過 IBM 的工具具有更多原生 WAS 整合功能，但 IntelliJ 經過一些設定後也能良好運作。以下我將介紹基礎設定、遠端偵錯（是的，你可以附加到 WAS JVM）以及其他實用技巧。

#### 1. 在 IntelliJ 中進行 WAS 開發的初始設定
- **安裝必要外掛**：
  - 前往 **File > Settings > Plugins**，在 JetBrains Marketplace 中搜尋 "WebSphere Server" 並安裝，以獲得更好的本機伺服器管理功能（例如從 IntelliJ 啟動/停止 WAS）。此外掛並非內建，因此是可選的，但建議用於本機開發。
  - 確保已啟用 Java EE 和 Jakarta EE 外掛（它們通常是預先安裝的）。
  
- **建立專案**：
  - 建立一個新的 **Java Enterprise** 專案（或匯入現有專案）。
  - 選擇 **Web Application** 原型，並針對 Java EE 進行設定（例如，根據你的 WAS 版本如 9.x，選擇版本 8 或 9）。
  - 如果需要，新增 WAS 特定函式庫的依賴項（例如，透過 Maven/Gradle：`com.ibm.websphere.appserver.api:jsp-2.3` 以獲得 JSP 支援）。

- **設定本機 WAS 伺服器（可選，用於本機執行）**：
  - 前往 **Run > Edit Configurations > + > WebSphere Server > Local**。
  - 指向你的本機 WAS 安裝目錄（例如 `/opt/IBM/WebSphere/AppServer`）。
  - 設定伺服器名稱、JRE（如果 WAS 附帶了 IBM 的 JDK，請使用它）和部署選項（例如，用於熱重載的展開式 WAR）。
  - 對於部署：在 **Deployment** 標籤中，新增你的成品（例如 WAR 檔案）並設定上下文路徑。

此設定讓你能直接從 IntelliJ 執行/部署，以進行本機測試。

#### 2. 遠端偵錯：將 IntelliJ 附加到 WAS JVM
是的，你絕對可以將 IntelliJ 偵錯器附加到遠端 WAS JVM。這是透過 JDWP (Java Debug Wire Protocol) 進行的標準 Java 遠端偵錯。它適用於本機和遠端 WAS 實例——將伺服器視為「遠端 JVM」。

**步驟 1：在 WAS 伺服器上啟用偵錯功能**
- **透過管理控制台（推薦用於類似生產環境的設定）**：
  - 登入 WAS 管理控制台（例如 `https://your-host:9043/ibm/console`）。
  - 導覽至 **Servers > Server Types > WebSphere Application Servers > [你的伺服器] > Debugging Service**。
  - 勾選 **Enable service at server startup**。
  - 設定 **JVM debug port**（預設為 7777；選擇一個未使用的端口，如 8000，以避免衝突）。
  - 儲存並重新啟動伺服器。

- **透過 server.xml（適用於獨立或快速編輯）**：
  - 編輯 `$WAS_HOME/profiles/[設定檔]/config/cells/[Cell]/nodes/[節點]/servers/[伺服器]/server.xml`。
  - 在 `<processDefinitions>` 下的 `<jvmEntries>` 區段中，新增或更新：
    ```
    <jvmEntries xmi:id="..." debugMode="true">
      <debugArgs>-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:8000</debugArgs>
    </jvmEntries>
    ```
    - `suspend=n` 會正常啟動伺服器（使用 `suspend=y` 則會在啟動時暫停）。
    - 將 `8000` 替換為你的端口。
  - 儲存後重新啟動伺服器：`./startServer.sh [伺服器名稱]`（或透過控制台）。

- 驗證：檢查伺服器日誌中是否有 "JDWP: transport=dt_socket, address=*:8000" 或類似訊息。

**步驟 2：在 IntelliJ 中設定遠端偵錯**
- 前往 **Run > Edit Configurations > + > Remote JVM Debug**。
- 為其命名（例如 "WAS Remote Debug"）。
- 將 **Debugger mode** 設定為 "Attach to remote JVM"。
- **Host**：你的 WAS 伺服器 IP/主機名稱（例如，本機用 `localhost`，遠端用 `192.168.1.100`）。
- **Port**：JVM 偵錯端口（例如 8000）。
- 可選：如果你的專案有特定函式庫，請設定 **Use module classpath**。
- 套用並關閉。

**步驟 3：附加並偵錯**
- 在你的程式碼中設定中斷點（例如，在 servlet 或 EJB 中）。
- 將你的應用程式部署到 WAS（透過管理控制台或 wsadmin 指令碼手動部署）。
- 執行偵錯設定（**Run > Debug 'WAS Remote Debug'**）。
- 觸發你的應用程式（例如透過 HTTP 請求）。IntelliJ 將會附加，並且執行會在中斷點處暫停。
- 常見問題：防火牆阻擋端口、JDK 版本不匹配（在 IntelliJ 中使用 WAS 的 IBM JDK）或伺服器在設定變更後未重新啟動。

這適用於 WAS 7+（包括 Liberty profile）。對於遠端伺服器，請確保可以存取偵錯端口的網路。

#### 3. 高效 WAS 開發的其他技巧
- **熱部署/熱替換**：為了更快的迭代，以「展開式」WAR（解壓縮）形式部署。WAS 支援 JSP 和部分類別的熱重載，但對於完整的熱替換（無需重啟即可變更程式碼），請使用 JRebel 外掛（付費）或 DCEVM + HotSwapAgent（免費，但需測試與 WAS 的 IBM JDK 的相容性）。
  
- **建置工具**：使用 Maven 或 Gradle 管理依賴項。將 WAS 執行期函式庫以 provided 範圍加入，以避免類別路徑膨脹：
  ```
  <dependency>
    <groupId>com.ibm.websphere.appserver.runtime</groupId>
    <artifactId>shared</artifactId>
    <version>9.0.5</version>
    <scope>provided</scope>
  </dependency>
  ```
  執行 `mvn clean package` 並透過管理控制台部署 WAR。

- **記錄和分析**：整合 SLF4J/Logback 用於應用程式記錄。對於效能分析，使用 VisualVM 或 YourKit（像偵錯一樣遠端附加）。WAS 的 PMI (Performance Monitoring Infrastructure) 非常出色——在管理控制台中啟用以獲取指標。

- **測試**：使用 Arquillian 針對遠端 WAS 進行整合測試。或者嵌入 Open Liberty（與 WAS 相容）以進行本機單元測試，無需完整的 WAS。

- **版本特定注意事項**：對於 WAS 9.x+，利用 IntelliJ 中的 Jakarta EE 遷移工具。如果使用 WAS Liberty（以微設定檔為重點），Liberty Tools 外掛會新增帶有自動重載的開發模式。

- **常見陷阱**：
  - 類別路徑問題：確保 IntelliJ 的專案 SDK 與 WAS 的 JDK 匹配。
  - 安全性：遠端偵錯會暴露端口——僅在開發/受信任的網路中使用。
  - 外掛限制：WebSphere 外掛功能較基礎；對於進階功能，請考慮使用 IBM 的 Rational Application Developer（但為了其 UX，請堅持使用 IntelliJ）。

這應該能讓你順利上手。如果你使用的是特定 WAS 版本，請分享詳細資訊以獲得更有針對性的建議。

#### 參考資料
- [Run/Debug Configuration: WebSphere Server | IntelliJ IDEA](https://www.jetbrains.com/help/idea/run-debug-configuration-websphere-server.html)
- [WebSphere remote server debug configuration in IntelliJ Idea](https://stackoverflow.com/questions/33013860/websphere-remote-server-debug-configuration-in-intellij-idea)
- [Debug code running on IBM Websphere using Eclipse / Intellij IDEA](https://davanum.wordpress.com/2009/11/20/debug-code-running-on-ibm-websphere-using-eclipse-intellij-idea/)
- [Debugging applications - IBM](https://www.ibm.com/docs/en/was/9.0.5?topic=applications-debugging)
- [Remote Debugging with IntelliJ IDEA | Baeldung](https://www.baeldung.com/intellij-remote-debugging)