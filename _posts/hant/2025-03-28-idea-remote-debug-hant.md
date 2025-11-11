---
audio: false
generated: true
lang: hant
layout: post
title: IntelliJ IDEA 內置遠端除錯功能
translated: true
type: note
---

要將 IntelliJ IDEA 連接到您使用 `server debug default` 啟動的 WebSphere Liberty 伺服器的除錯端口，而無需使用 WebSphere Liberty 外掛程式，您可以利用 IntelliJ IDEA 的內建遠端除錯功能。此方法之所以有效，是因為 WebSphere Liberty 在除錯模式下啟動時，會暴露一個除錯端口（預設通常為 7777），任何 JVM 除錯器（包括 IntelliJ IDEA）都可以連接到該端口。以下是實現此操作的詳細步驟：

---

### 步驟 1：在除錯模式下啟動 WebSphere Liberty 伺服器
當您執行 `server debug default`（假設 "default" 是您的伺服器名稱；如果不同，請替換為實際的伺服器名稱）時，WebSphere Liberty 會啟用除錯功能並啟動。預設情況下，此命令會配置伺服器在端口 **7777** 上監聽除錯連接。

- **指令**：
  ```bash
  server debug default
  ```
- **功能**：這會在除錯模式下啟動 "default" 伺服器，自動啟用 JVM 除錯選項（例如 `-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=7777`）。
- **驗證**：執行指令後，檢查伺服器控制台輸出或日誌（例如 `messages.log`），以確認伺服器正在除錯端口上監聽。尋找指示除錯端口的訊息（通常是 7777，除非被覆寫或不可用）。

---

### 步驟 2：確認除錯端口
WebSphere Liberty 的預設除錯端口是 **7777**。但是，如果該端口已被使用或已自訂：
- 檢查啟動伺服器後的控制台輸出。它可能會顯示類似「正在端口 7777 上監聽除錯器連接」的訊息。
- 如果端口不同（例如，由於衝突而分配了隨機端口），請記下實際端口號以供在 IntelliJ IDEA 中使用。

在本指南中，除非您的設定另有指示，否則我們將假設使用預設端口 **7777**。

---

### 步驟 3：在 IntelliJ IDEA 中配置遠端除錯
IntelliJ IDEA 的遠端除錯功能允許您連接到伺服器的 JVM，而無需特定的 WebSphere 外掛程式。設定方法如下：

1. **開啟執行/除錯配置**：
   - 在 IntelliJ IDEA 中，前往頂部選單並選擇 **Run > Edit Configurations**。

2. **新增遠端除錯配置**：
   - 點擊左上角的 **+** 按鈕（或「新增配置」）。
   - 從清單中選擇 **Remote JVM Debug**（根據您的 IntelliJ 版本，可能只顯示 "Remote"）。

3. **設定配置詳細資訊**：
   - **名稱**：給予一個有意義的名稱，例如 "WebSphere Liberty Debug"。
   - **主機**：設定為 `localhost`（假設伺服器與 IntelliJ IDEA 在同一台機器上執行；如果是遠端伺服器，請使用伺服器的 IP 位址）。
   - **端口**：設定為 `7777`（如果實際除錯端口不同，則使用該端口）。
   - **傳輸**：確保設定為 **Socket**。
   - **除錯器模式**：選擇 **Attach**（這告訴 IntelliJ 連接到已執行的 JVM）。
   - 除非需要特定的 JVM 選項，否則將其他設定（如「遠端 JVM 的命令列參數」）保留為預設值。

4. **儲存配置**：
   - 點擊 **Apply**，然後點擊 **OK** 儲存。

---

### 步驟 4：開始除錯
在伺服器以除錯模式執行且配置設定完成後：
- 前往 **Run > Debug**（或點擊錯誤圖示）並選擇您的新配置（例如 "WebSphere Liberty Debug"）。
- IntelliJ IDEA 將嘗試連接到指定主機和端口上的伺服器 JVM。
- 如果成功，您將在除錯視窗中看到類似「已連接到目標 VM，位址：'localhost:7777'」的訊息。

---

### 步驟 5：對您的應用程式進行除錯
- **設定中斷點**：在您的原始碼中，點擊行號旁邊的裝訂線以在您希望執行暫停的位置新增中斷點。
- **觸發執行**：與您的應用程式互動（例如，向伺服器發送請求）以觸達中斷點。
- **除錯**：一旦觸達中斷點，使用 IntelliJ 的除錯工具（逐步執行、步入、恢復等）來檢查變數並控制執行。

---

### 補充說明
- **本地與遠端伺服器**：如果 WebSphere Liberty 在不同的機器上執行，請在遠端除錯配置中將 `localhost` 替換為伺服器的 IP 位址。確保除錯端口（例如 7777）是開放的且未被防火牆阻擋。
- **端口衝突**：如果伺服器啟動時端口 7777 不可用，WebSphere Liberty 可能會選擇隨機端口。檢查伺服器輸出以確認端口，並相應地更新 IntelliJ 配置。
- **無需外掛程式**：此方法使用 IntelliJ IDEA 的標準遠端除錯功能，因此不需要 WebSphere Liberty 外掛程式。

---

### 總結
通過使用 `server debug default` 啟動您的 WebSphere Liberty 伺服器（預設在端口 7777 上啟用除錯），並在 IntelliJ IDEA 中配置遠端除錯設定，您可以在沒有 WebSphere Liberty 外掛程式的情況下連接到伺服器的除錯端口。這使您能夠直接在 IntelliJ IDEA 中擁有完整的除錯功能——中斷點、變數檢查和逐步執行。

---

在 IntelliJ IDEA 中執行和除錯 WebSphere Liberty 應用程式而無需專用的 Liberty Tools 外掛程式，是通過手動設定 Liberty 執行環境並配置 IntelliJ IDEA 進行遠端除錯和外部工具執行來實現的。與使用整合外掛程式相比，此方法需要一些手動步驟，但它提供了開發和疑難排解 Liberty 應用程式所需的必要功能。

以下是過程的細分：

**1. 取得並安裝 WebSphere Liberty 執行環境：**

由於您沒有外掛程式來為您管理執行環境，您需要手動下載並安裝 WebSphere Liberty 執行環境。您可以從官方 IBM 網站取得執行環境，或者如果您使用 Maven 或 Gradle 管理專案，也可以通過這些工具進行分發。

通常，手動安裝涉及下載 ZIP 或 JAR 檔案並將其解壓縮到系統上的目錄。該目錄將是您的 Liberty 安裝主目錄（`<LIBERTY_HOME>`）。

**2. 配置 Liberty 伺服器以進行除錯：**

要對應用程式進行除錯，您需要在使用除錯功能啟用的情況下啟動 Liberty 伺服器。這是在伺服器啟動時透過新增特定的 JVM 選項來完成的。這些選項告訴 Java Virtual Machine (JVM) 在特定端口上監聽除錯器連接。

在您的 Liberty 伺服器配置目錄（`<LIBERTY_HOME>/usr/servers/<your_server_name>/`）中找到 `jvm.options` 檔案。如果此檔案不存在，您可以建立它。將以下行新增至 `jvm.options` 檔案：

```
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005
```

  * `-agentlib:jdwp`：載入 Java Debug Wire Protocol (JDWP) 函式庫。
  * `transport=dt_socket`：指定除錯器將使用 socket 進行連接。
  * `server=y`：指示 JVM 將作為伺服器，監聽除錯器連接。
  * `suspend=n`：指定 JVM 不應在啟動前等待除錯器連接。如果您需要對在伺服器啟動期間執行的程式碼進行除錯，可以將其更改為 `suspend=y`。
  * `address=5005`：設定除錯器將連接的端口號。您可以將其更改為任何可用的端口。

**3. 配置 IntelliJ IDEA 以執行 Liberty：**

您可以使用 IntelliJ IDEA 的「External Tools」配置從 IDE 內部啟動您的 Liberty 伺服器。

  * 前往 `File` > `Settings`（或在 macOS 上為 `IntelliJ IDEA` > `Preferences`）。
  * 導航至 `Tools` > `External Tools`。
  * 點擊 `+` 圖示以新增外部工具。
  * 使用以下詳細資訊配置工具：
      * **名稱**：給予一個描述性名稱，例如 "Start Liberty Server"。
      * **程式**：瀏覽至 Liberty 伺服器指令碼。這通常是 Linux/macOS 的 `<LIBERTY_HOME>/bin/server` 或 Windows 的 `<LIBERTY_HOME>\bin\server.bat`。
      * **參數**：新增參數以啟動您的特定伺服器實例。這通常是 `start <your_server_name>`，其中 `<your_server_name>` 是您在 `<LIBERTY_HOME>/usr/servers/` 中的伺服器目錄名稱。
      * **工作目錄**：將其設定為 `<LIBERTY_HOME>/bin`。

現在，您可以通過前往 `Tools` > `External Tools` 並選擇您剛剛配置的工具來啟動 Liberty 伺服器。

**4. 配置 IntelliJ IDEA 進行遠端除錯：**

要對在手動啟動的 Liberty 伺服器上執行的應用程式進行除錯，您將使用 IntelliJ IDEA 的「Remote JVM Debug」配置。

  * 前往 `Run` > `Edit Configurations`。
  * 點擊 `+` 圖示並選擇 `Remote JVM Debug`。
  * 配置設定：
      * **名稱**：給予一個描述性名稱，例如 "Debug Liberty Server"。
      * **除錯器模式**：選擇 `Attach to remote JVM`。
      * **主機**：輸入 `localhost`（如果執行 Liberty 的機器不在本地，則輸入其 IP 位址）。
      * **端口**：輸入您在 `jvm.options` 檔案中配置的端口號（例如 `5005`）。
      * **使用模組類別路徑**：選擇您在 IntelliJ IDEA 專案中包含 Liberty 應用程式程式碼的模組。這有助於 IntelliJ IDEA 將執行的程式碼映射到您的原始檔以進行除錯。

**5. 執行與除錯：**

1.  使用您在 IntelliJ IDEA 中建立的「External Tools」配置啟動 Liberty 伺服器。
2.  等待伺服器啟動並指示它正在配置的端口上監聽除錯器（您應該在伺服器控制台輸出中看到訊息）。
3.  在 IntelliJ IDEA 內的應用程式程式碼中設定中斷點。
4.  前往 `Run` > `Debug` 並選擇您建立的「Debug Liberty Server」配置。

IntelliJ IDEA 將嘗試連接到指定端口上執行的 Liberty 伺服器。一旦連接，您可以使用 IntelliJ IDEA 的所有除錯功能，例如逐步執行程式碼、檢查變數和評估表達式。

通過遵循這些步驟，您可以在 IntelliJ IDEA 中有效地執行和除錯 WebSphere Liberty 應用程式，而無需依賴專用的 Liberty Tools 外掛程式，從而讓您直接控制伺服器生命週期和除錯過程。