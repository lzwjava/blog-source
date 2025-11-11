---
audio: false
generated: true
lang: hant
layout: post
title: IntelliJ IDEA 遠端記錄
translated: true
type: note
---

聽起來您正在從使用 Eclipse 搭配 Liberty Tools 外掛，轉向使用 IntelliJ IDEA 進行遠端偵錯，並且希望複製在 WebSphere Liberty 伺服器中檢視、清除及篩選由前端操作觸發的新日誌的能力，類似於您在 Eclipse 中使用主控台或在 VS Code 中監控日誌的方式。您特別詢問 IntelliJ IDEA 是否支援遠端日誌記錄，以及如何有效率地檢視和管理由前端點擊產生的新日誌，就像您在 VS Code 中將游標置於日誌檔案結尾處所做的那樣。

下面，我將說明如何在 IntelliJ IDEA 中設定，以便在遠端偵錯工作階段期間，檢視和管理來自 WebSphere Liberty 伺服器的遠端日誌，包括清除日誌和專注於由前端操作觸發的新日誌。我還會說明如何實現類似於您在 VS Code 中設定用於選取新日誌的工作流程。

---

### 了解您的需求
1.  **Eclipse Liberty Tools 的行為**：在 Eclipse 搭配 Liberty Tools 外掛中，您使用主控台檢視來查看 WebSphere Liberty 伺服器的日誌、清除它們，並觀察由前端互動觸發的新日誌。
2.  **VS Code 工作流程**：您在 VS Code 中開啟 WebSphere Liberty (`wlp`) 目錄，將游標置於日誌檔案（例如 `messages.log`）的結尾處，並且在與前端互動時，可以輕鬆選取或檢視附加的新日誌。
3.  **IntelliJ IDEA 目標**：您已在 IntelliJ IDEA 中設定好遠端偵錯，並希望：
    - 即時檢視來自遠端 WebSphere Liberty 伺服器的日誌。
    - 清除日誌或專注於由前端操作觸發的新日誌。
    - 複製在 VS Code 中輕鬆選取新日誌的體驗。

### IntelliJ IDEA 是否支援遠端日誌記錄？
是的，IntelliJ IDEA 支援在遠端偵錯工作階段期間檢視來自遠端伺服器（包括 WebSphere Liberty）的日誌。然而，與 Eclipse 的 Liberty Tools 外掛（它為 Liberty 伺服器日誌提供專用的主控台）不同，IntelliJ IDEA 需要手動設定才能在 **Run** 或 **Debug** 工具視窗中顯示遠端日誌。您可以透過在 Run/Debug 設定中設定 **Logs 標籤**，或整合外部工具來 tail 遠端日誌檔案來實現此目的。IntelliJ IDEA 也允許您清除日誌和篩選新項目，儘管體驗與 Eclipse 或 VS Code 有所不同。

---

### 在 IntelliJ IDEA 中設定遠端日誌記錄
為了複製您的 Eclipse 和 VS Code 工作流程，您需要設定 IntelliJ IDEA 以存取和顯示來自遠端 WebSphere Liberty 伺服器日誌檔案（例如 `wlp/usr/servers/<serverName>/logs` 目錄中的 `messages.log` 或 `console.log`）的日誌。以下是操作步驟：

#### 步驟 1：設定遠端偵錯
由於您已經在 IntelliJ IDEA 中設定了遠端偵錯，我假設您已經有一個 **Remote JVM Debug** 設定。如果沒有，這裡快速回顧一下：
1.  前往 **Run > Edit Configurations**。
2.  點擊 **+** 圖示並選擇 **Remote JVM Debug**。
3.  設定以下項目：
    - **Name**：例如 "Liberty Remote Debug"。
    - **Host**：遠端伺服器的位址（例如 `localhost` 或像 `192.168.1.100` 的 IP）。
    - **Port**：偵錯埠（Liberty 的預設值通常是 `7777`，除非有自訂）。
    - **Command-line arguments for remote JVM**：複製產生的參數（例如 `-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:7777`）並確保它們已應用於 Liberty 伺服器的 JVM。
4.  應用並儲存設定。
5.  使用偵錯參數啟動 Liberty 伺服器（例如，修改 `jvm.options` 或使用 `server debug` 指令）。

#### 步驟 2：在 IntelliJ IDEA 中設定日誌檔案顯示
為了在 IntelliJ IDEA 的 Debug 工具視窗中檢視遠端日誌，您需要在 Run/Debug 設定中指定日誌檔案的位置。由於日誌位於遠端伺服器上，您需要透過掛載的資料夾、SSH 或外掛來存取它們。

**選項 1：透過掛載的資料夾或本機副本存取日誌**
如果遠端伺服器的日誌目錄是可存取的（例如，透過網路共用、SFTP 或複製到本機），您可以設定 IntelliJ 來顯示日誌：
1.  **掛載或複製日誌**：
    - 使用 SSHFS、NFS 或其他方法，將遠端伺服器的日誌目錄（例如 `wlp/usr/servers/<serverName>/logs`）掛載到您的本機機器。
    - 或者，使用像 `rsync` 或 `scp` 這樣的工具，定期將 `messages.log` 或 `console.log` 複製到您的本機機器。
2.  **將日誌檔案新增至 Run/Debug 設定**：
    - 前往 **Run > Edit Configurations** 並選擇您的 Remote JVM Debug 設定。
    - 開啟 **Logs** 標籤。
    - 點擊 **+** 圖示以新增日誌檔案。
    - 指定：
        - **Log file location**：日誌檔案的路徑（例如 `/path/to/mounted/wlp/usr/servers/defaultServer/logs/messages.log`）。
        - **Alias**：日誌標籤的名稱（例如 "Liberty Logs"）。
        - **Show all files coverable by pattern**：取消勾選此項以僅顯示最新的日誌檔案（對於像 `messages.log` 這樣的滾動日誌很有用）。
        - **Skip Content**：勾選此項以僅顯示目前工作階段的新日誌項目，類似於在 Eclipse 中清除日誌。
    - 點擊 **Apply** 和 **OK**。
3.  **執行偵錯器**：
    - 透過選擇設定並點擊 **Debug** 按鈕來啟動遠端偵錯工作階段。
    - **Debug** 工具視窗中將會出現一個新標籤（例如 "Liberty Logs"），顯示日誌檔案的內容。
    - 如果檔案是可存取的，由前端點擊觸發的新日誌項目將會即時附加到此標籤。

**選項 2：使用 SSH 來 Tail 遠端日誌**
如果掛載或複製日誌不可行，您可以使用 IntelliJ 內建的 SSH 終端機或外掛來直接 tail 遠端日誌檔案：
1.  **啟用 SSH 存取**：
    - 確保您具有對託管 Liberty 的遠端伺服器的 SSH 存取權限。
    - 透過 **File > Settings > Tools > SSH Configurations** 在 IntelliJ IDEA 中設定 SSH。
2.  **使用內建終端機**：
    - 在 IntelliJ IDEA 中開啟 **Terminal** 工具視窗 (Alt+F12)。
    - 執行指令來 tail 日誌檔案：
      ```bash
      ssh user@remote-server tail -f /path/to/wlp/usr/servers/<serverName>/logs/messages.log
      ```
    - 這會將日誌檔案即時串流到終端機，類似於您在 VS Code 中將游標置於結尾處的工作流程。
3.  **清除日誌**：
    - IntelliJ 的終端機沒有像 Eclipse 主控台那樣的直接「清除日誌」按鈕。相反，您可以：
        - 停止 tail 指令 (Ctrl+C) 並重新啟動它以模擬清除。
        - 使用終端機工具列中的 **Clear All** 按鈕來清除終端機輸出。
4.  **篩選新日誌**：
    - 使用 `grep` 來篩選特定前端觸發事件的日誌：
      ```bash
      ssh user@remote-server tail -f /path/to/wlp/usr/servers/<serverName>/logs/messages.log | grep "specific-pattern"
      ```
    - 例如，如果前端點擊觸發帶有特定關鍵字（例如 "INFO"）的日誌，則篩選這些日誌。

**選項 3：使用外掛來增強日誌檢視**
**Log4JPlugin** 或 **Grep Console** 外掛可以增強 IntelliJ IDEA 中的日誌檢視：
1.  **安裝外掛**：
    - 前往 **File > Settings > Plugins**，搜尋 "Log4JPlugin" 或 "Grep Console" 並安裝。
    - 重新啟動 IntelliJ IDEA。
2.  **設定 Log4JPlugin**：
    - 設定好遠端偵錯設定後，使用 Log4JPlugin 指向遠端日誌檔案（需要 SSH 或掛載的資料夾）。
    - 此外掛允許您在專用標籤中檢視和篩選日誌，類似於 Eclipse 的 Liberty Tools 主控台。
3.  **設定 Grep Console**：
    - Grep Console 讓您可以根據模式來突顯和篩選日誌訊息，使得專注於由前端操作觸發的新日誌變得更加容易。
    - 在 **Run/Debug Configurations > Logs** 標籤中，透過指定日誌檔案並啟用外掛來進行設定。

#### 步驟 3：複製 VS Code 的「游標置於結尾」工作流程
為了模仿 VS Code 中將游標置於日誌檔案結尾並選取新日誌的行為：
1.  **自動滾動至結尾**：
    - 在 **Debug** 工具視窗的日誌標籤（來自選項 1）中，IntelliJ IDEA 會在新項目加入時自動滾動到日誌檔案的結尾，類似於 `tail -f`。
    - 確保日誌標籤工具列中的 **Scroll to the end**（一個指向下方的小箭頭圖示）已啟用。
2.  **選取新日誌**：
    - 點擊日誌標籤的結尾處以放置游標。
    - 當您與前端互動時，新的日誌項目將會出現，您可以透過拖曳滑鼠或使用鍵盤快捷鍵（例如 Shift+方向鍵）來選取它們。
    - 或者，使用日誌標籤中的 **Search** 功能（放大鏡圖示）來根據關鍵字或時間戳記篩選新項目。
3.  **清除日誌以顯示新項目**：
    - 在 Run/Debug 設定的 Logs 標籤中勾選 **Skip Content** 選項，以僅顯示目前工作階段的新日誌項目，有效地「清除」舊日誌。
    - 如果使用 SSH 終端機，停止並重新啟動 `tail -f` 指令，以將檢視重設為新日誌。

#### 步驟 4：偵錯和監控前端觸發的日誌
1.  **設定中斷點**：
    - 在 IntelliJ IDEA 中，開啟相關的 Java 原始碼檔案（例如，處理前端請求的後端控制器）。
    - 透過點擊程式碼行旁邊的裝訂線（或按 Ctrl+F8 / Cmd+F8）來設定中斷點。
2.  **開始偵錯**：
    - 執行遠端偵錯設定。
    - Debug 工具視窗將會顯示日誌標籤（如果已設定），並在前端點擊觸發的中斷點處暫停。
3.  **將日誌與中斷點關聯**：
    - 當命中中斷點時，檢查日誌標籤或終端機以尋找對應的日誌項目。
    - IntelliJ IDEA 能識別像 SLF4J 或 Log4J（在 Liberty 應用程式中常見）這樣的日誌記錄框架，並在日誌標籤中提供可點擊的連結，以便跳轉到產生日誌的原始碼。
4.  **篩選前端操作**：
    - 使用日誌標籤中的搜尋列來篩選特定的日誌訊息（例如 "INFO [frontend]" 或 "POST /endpoint"）。
    - 如果使用 Grep Console，設定模式以突顯與前端相關的日誌。

---

### 與 Eclipse 和 VS Code 的差異
-   **Eclipse Liberty Tools**：為 Liberty 日誌提供專用的主控台，具有內建的清除和篩選選項。IntelliJ IDEA 需要手動設定或外掛來實現類似的功能。
-   **VS Code**：在 VS Code 中 tail 日誌檔案是輕量級且手動的，游標置於結尾的方法對於快速檢查日誌很簡單。IntelliJ IDEA 的日誌標籤或終端機整合度更高，但對於手動游標放置的靈活性較差。
-   **清除日誌**：
    - Eclipse：主控台中的一鍵清除按鈕。
    - IntelliJ IDEA：使用 **Skip Content** 或重新啟動終端機 tail 指令。
    - VS Code：手動清除終端機或重新啟動 `tail -f`。
-   **即時日誌檢視**：
    - 所有三個 IDE 都支援即時日誌檢視，但 IntelliJ IDEA 的日誌標籤需要掛載的檔案或外掛，而 VS Code 則依賴終端機指令。

---

### 建議
1.  **首選方法**：使用**選項 1（掛載的資料夾）**以獲得最接近 Eclipse 主控台的體驗。它將日誌整合到 Debug 工具視窗中，支援自動滾動，並允許篩選。**Skip Content** 選項模仿了清除日誌。
2.  **對於 VS Code 類似的簡潔性**：使用**選項 2（SSH 終端機）**搭配 `tail -f`，以獲得輕量級、游標置於結尾的體驗。結合 `grep` 來篩選前端觸發的日誌。
3.  **使用外掛增強**：安裝 **Grep Console** 以獲得更好的日誌篩選和突顯功能，特別是對於前端特定的日誌。
4.  **效能注意事項**：如果遠端伺服器的日誌量很大，掛載或複製日誌可能比透過 SSH tail 慢。測試兩種方法以找到最適合的方案。

---

### 疑難排解
-   **日誌標籤為空**：確保日誌檔案路徑正確且可存取。如果使用掛載的資料夾，請確認掛載處於活動狀態。如果使用 SSH，請檢查 `tail -f` 指令語法。
-   **日誌未更新**：確認 Liberty 伺服器正在寫入指定的日誌檔案（例如 `messages.log`）。檢查檔案權限或滾動日誌問題。
-   **沒有前端日誌**：驗證前端操作是否到達後端（使用中斷點），並且日誌記錄框架（例如 SLF4J）已設定為輸出相關訊息。
-   **外掛問題**：如果 Log4JPlugin 或 Grep Console 無法工作，請確保它們與您的 IntelliJ IDEA 版本（例如 2024.1 或更新版本）相容。

---

### 範例工作流程
1.  使用日誌檔案 `/path/to/mounted/wlp/usr/servers/defaultServer/logs/messages.log` 設定 Remote JVM Debug。
2.  啟動偵錯工作階段。
3.  開啟 **Debug** 工具視窗，切換到 "Liberty Logs" 標籤，並啟用 **Scroll to the end**。
4.  點擊前端按鈕以觸發後端請求。
5.  在日誌標籤中觀察新項目（例如 "INFO [frontend] Button clicked"）。
6.  使用搜尋列來篩選特定關鍵字，或選取新的日誌行進行檢查。
7.  如果需要，停止並重新啟動偵錯工作階段，並啟用 **Skip Content** 以清除舊日誌。

---

### 補充說明
-   **Liberty 特定日誌**：WebSphere Liberty 通常會寫入 `wlp/usr/servers/<serverName>/logs` 中的 `messages.log` 或 `console.log`。確保您的 Run/Debug 設定指向正確的檔案。
-   **前後端關聯**：如果前端點擊沒有產生預期的日誌，請檢查後端端點的日誌記錄設定（例如，確保存在 `logger.info()` 陳述式）。
-   **替代工具**：如果 IntelliJ 的日誌檢視不令人滿意，考慮在 IntelliJ 旁邊執行一個單獨的終端機或 VS Code 來執行 `tail -f` 以進行日誌監控，同時使用 IntelliJ 進行偵錯。

如果您需要有關特定設定步驟、外掛設定或針對特定前端操作篩選日誌的幫助，請提供更多詳細資訊（例如 Liberty 版本、日誌檔案路徑或前端技術），我可以進一步調整說明！