---
audio: false
generated: true
lang: hant
layout: post
title: VSCode 遠端偵錯
translated: true
type: note
---

若要在 Visual Studio Code (VSCode) 中對運行於除錯模式的 WebSphere Liberty Server 進行遠端除錯，您可以使用 VSCode 內建的 Java 除錯功能。以下詳細步驟將說明如何在不安裝任何 WebSphere Liberty 專用外掛的情況下完成設定，前提是您已安裝標準的 **Java Extension Pack**（包含 **Debugger for Java**）。

---

### 步驟 1：以除錯模式啟動 WebSphere Liberty Server
1. 開啟終端機或命令提示字元。
2. 導航至您的 WebSphere Liberty 安裝目錄。
3. 執行以下指令以除錯模式啟動伺服器：
   ```
   server debug default
   ```
   - 若您的伺服器名稱不同，請將 `default` 替換為實際名稱。
4. 伺服器將啟動除錯模式，通常監聽 **7777** 連接埠。
5. 檢查伺服器控制台輸出或日誌中是否出現如下訊息：
   ```
   Listening for transport dt_socket at address: 7777
   ```
   - 此訊息確認除錯連接埠。若因衝突使用其他連接埠，請記下顯示的埠號。

---

### 步驟 2：在 VSCode 中設定遠端除錯
1. **在 VSCode 中開啟專案**：
   - 確保您的 Java 專案（包含部署至伺服器的原始碼）已在 VSCode 中開啟，這能讓除錯器將中斷點對應至運行中的程式碼。

2. **存取執行與除錯視圖**：
   - 點擊左側導覽列的 **Run and Debug** 圖示（帶有錯誤符號的播放按鈕），或按下 `Ctrl+Shift+D`（Windows/Linux）或 `Cmd+Shift+D`（Mac）。

3. **建立或編輯 `launch.json` 檔案**：
   - 在 **Run and Debug** 視圖中，點擊設定下拉選單旁的 **齒輪圖示**。
   - 若系統提示選擇環境，請選擇 **Java**。這會在您工作區的 `.vscode` 資料夾中建立 `launch.json` 檔案。
   - 若檔案已存在，將會開啟供編輯。

4. **新增除錯設定**：
   - 在 `launch.json` 檔案中，確保包含連接至遠端 JVM 的設定。範例如下：
     ```json
     {
         "version": "0.2.0",
         "configurations": [
             {
                 "type": "java",
                 "name": "Attach to WebSphere Liberty",
                 "request": "attach",
                 "hostName": "localhost",
                 "port": 7777
             }
         ]
     }
     ```
   - **欄位說明**：
     - `"type": "java"`：指定 Java 除錯器。
     - `"name": "Attach to WebSphere Liberty"`：此設定的描述名稱。
     - `"request": "attach"`：表示 VSCode 將連接至現有的 JVM 程序。
     - `"hostName": "localhost"`：運行伺服器的主機名稱。若伺服器位於其他機器，請使用該伺服器的 IP 位址或主機名稱。
     - `"port": 7777`：來自步驟 1 的除錯連接埠。若伺服器使用其他埠號，請更新此值。

5. **儲存檔案**：
   - 新增或編輯設定後，儲存 `launch.json` 檔案。

---

### 步驟 3：啟動除錯工作階段
1. **確認伺服器運行狀態**：
   - 確認 WebSphere Liberty Server 仍以除錯模式運行（如步驟 1 所述）。

2. **選擇設定**：
   - 在 **Run and Debug** 視圖中，從頂部下拉選單選擇 **"Attach to WebSphere Liberty"**。

3. **啟動除錯器**：
   - 點擊綠色 **播放按鈕** 或按下 `F5`。VSCode 將連接至伺服器的 JVM 程序。

4. **設定中斷點**：
   - 在 VSCode 中開啟您的 Java 原始碼檔案。
   - 於行號左側的邊欄點擊，即可在需要暫停執行的位置設定中斷點。

5. **與應用程式互動**：
   - 使用您的應用程式（例如傳送 HTTP 請求）來觸發設有中斷點的程式路徑。當觸及中斷點時，VSCode 將暫停執行，讓您能檢查變數、逐步執行程式碼並進行除錯。

---

### 補充說明
- **本地與遠端伺服器**：
  - 若伺服器運行於其他機器，請將 `launch.json` 中的 `"localhost"` 替換為該伺服器的主機名稱或 IP 位址。確保除錯連接埠可透過網路存取（例如未被防火牆阻擋）。

- **除錯連接埠確認**：
  - 若不確定連接埠號，請在執行 `server debug default` 後檢查伺服器輸出，該訊息會明確顯示監聽中的連接埠。

- **原始碼匹配性**：
  - VSCode 中的原始碼必須與伺服器上運行的程式碼一致，中斷點才能正確運作。請確保您的專案為最新版本，且編譯時包含除錯資訊（大多數 Java 建置預設啟用）。

- **伺服器行為**：
  - 使用 `server debug default` 時，伺服器會立即啟動（無需等待除錯器連接）。您可在其運行期間隨時連接 VSCode。

- **必要條件**：
  - 必須在 VSCode 中安裝 **Java Extension Pack**（或至少 **Debugger for Java** 擴充功能）。這是 Java 開發的標準工具，提供必要的除錯功能。

---

透過遵循這些步驟，您無需安裝 WebSphere 專用外掛，即可使用 VSCode 的內建功能有效對 WebSphere Liberty Server 進行遠端除錯。