---
audio: false
generated: true
lang: hant
layout: post
title: 精通JMeter：效能測試
translated: true
type: note
---

Apache JMeter 是一款功能強大的開源工具，主要用於效能測試，但也可用於功能測試。它廣泛用於測試網頁應用程式、API、資料庫及其他服務的效能，透過模擬多個使用者並測量系統在負載下的回應情況。以下是如何有效使用 JMeter 的逐步指南，從安裝到執行基本測試及分析結果。

---

## 步驟 1：安裝 JMeter
在使用 JMeter 之前，您需要先將其安裝到您的電腦上。方法如下：

1. **先決條件**：  
   JMeter 是一個基於 Java 的應用程式，因此您必須安裝 Java Development Kit (JDK) 或 Java Runtime Environment (JRE)。建議使用版本 8 或更高版本。您可以在終端機或命令提示字元中執行 `java -version` 來確認。如果未安裝 Java，請從 [官方 Java 網站](https://www.java.com) 下載並安裝。

2. **下載 JMeter**：  
   前往 [Apache JMeter 網站](https://jmeter.apache.org/download_jmeter.cgi) 下載最新的二進位版本（通常是 `.zip` 或 `.tgz` 檔案）。

3. **解壓縮檔案**：  
   將下載的檔案解壓縮到您選擇的目錄（例如 Windows 上的 `C:\JMeter` 或 Unix 系統上的 `~/JMeter`）。解壓縮後的資料夾包含執行 JMeter 所需的所有檔案。

4. **啟動 JMeter**：  
   - 進入解壓縮目錄中的 `bin` 資料夾（例如 `C:\JMeter\apache-jmeter-5.x\bin`）。
   - 執行相應的可執行檔：
     - **Windows**：雙擊 `jmeter.bat` 或在命令提示字元中執行。
     - **Unix/Linux/macOS**：在終端機中執行 `./jmeter.sh`。
   - 這將開啟 JMeter 圖形使用者介面 (GUI)，您可以在其中建立和管理測試計劃。

---

## 步驟 2：建立測試計劃
JMeter 中的**測試計劃**定義了您要測試的內容及測試方式。它是效能測試的藍圖。以下是設定基本測試計劃的方法：

### 新增線程組
1. 在 JMeter GUI 中，右鍵點擊左側窗格中的**測試計劃**節點，選擇**新增 > Threads (Users) > Thread Group**。
2. 配置線程組：
   - **Number of Threads (Users)**：要模擬的虛擬使用者數量（例如 10）。
   - **Ramp-Up Period (seconds)**：JMeter 啟動所有線程所需的時間（例如 10 秒表示 10 個線程將在 10 秒內每秒啟動 1 個）。
   - **Loop Count**：每個線程重複測試的次數（例如 1 表示單次執行，或勾選「Forever」以持續循環）。

線程組模擬使用者流量。例如，10 個線程、10 秒加速時間和 1 次循環表示 10 個使用者將在 10 秒內訪問應用程式，每個使用者執行一次測試。

### 新增取樣器
取樣器定義 JMeter 發送到目標系統的請求。對於網頁測試，最常用的是 HTTP 請求取樣器：
1. 右鍵點擊線程組，選擇**新增 > Sampler > HTTP Request**。
2. 配置 HTTP 請求：
   - **Protocol**：`http` 或 `https`。
   - **Server Name or IP**：目標系統的網域或 IP（例如 `example.com`）。
   - **Port Number**：通常 HTTP 為 `80` 或 HTTPS 為 `443`（若為標準端口可留空）。
   - **Method**：`GET`、`POST` 等，依請求類型而定。
   - **Path**：特定端點或頁面（例如主頁為 `/`）。
   - 如有需要，可新增參數或請求主體（例如 POST 請求）。

此取樣器告訴 JMeter 每個虛擬使用者應執行的操作。

### 新增監聽器
監聽器收集並顯示測試結果：
1. 右鍵點擊線程組，選擇**新增 > Listener > View Results Tree**（或其他監聽器如 **Summary Report**）。
2. **View Results Tree** 顯示每個請求的詳細結果，包括回應時間、狀態碼和回應資料。

監聽器對於分析應用程式在測試期間的效能至關重要。

### 儲存測試計劃
點擊**檔案 > Save Test Plan As** 並儲存您的 `.jmx` 檔案（例如 `mytest.jmx`）。這允許您後續重複使用或修改。

---

## 步驟 3：執行測試
要執行測試：
1. 在 JMeter GUI 中，點擊工具列中的綠色**播放**按鈕 (▶)，或前往**執行 > Start**。
2. JMeter 將模擬線程組中定義的使用者，發送配置的 HTTP 請求。
3. 在測試執行時，觀察監聽器（例如 View Results Tree）中的結果填充情況。

對於小型測試，透過 GUI 執行即可。對於較大測試，請參閱下方的「進階用法」章節以了解非 GUI 模式。

---

## 步驟 4：分析結果
測試完成後，使用監聽器檢視結果：
- **View Results Tree**：顯示每個請求的成功/失敗、回應時間和回應資料。
- **Summary Report**：提供聚合指標，如平均回應時間、吞吐量（每秒請求數）和錯誤率。

這些指標幫助您評估應用程式的效能（例如在負載下的回應速度，或在特定使用者數量下是否失敗）。

---

## 範例：測試簡單網頁
讓我們用 10 個使用者測試 `example.com`：
1. 啟動 JMeter。
2. 新增線程組：
   - 線程數：10
   - 加速時間：10 秒
   - 循環次數：1
3. 新增 HTTP 請求取樣器：
   - 協定：`http`
   - 伺服器名稱：`example.com`
   - 方法：`GET`
   - 路徑：`/`
4. 新增 View Results Tree 監聽器。
5. 儲存並執行測試。
6. 在 View Results Tree 中檢查結果，查看回應時間和狀態碼（例如 200 OK）。

此簡單測試測量 `example.com` 在 10 個同時使用者下的效能表現。

---

## 進階用法
對於更複雜的場景，JMeter 提供額外功能：

### 參數化
使用 **CSV Data Set Config** 從 CSV 檔案將不同資料（例如使用者名稱、密碼）輸入測試：
1. 在線程組中新增**Config Element > CSV Data Set Config**。
2. 指定檔案路徑和變數名稱（例如 `${username}`），然後在 HTTP 請求中使用這些變數。

### 關聯處理
處理動態值（例如工作階段 ID、令牌）：
1. 在請求後新增 **Post-Processor > Regular Expression Extractor** 或 **JSON Extractor**。
2. 將值（例如令牌）提取到變數中（例如 `${token}`）。
3. 在後續請求中使用 `${token}`（例如在標頭或參數中）。

### 斷言
驗證回應：
1. 在取樣器中新增 **Assertion > Response Assertion**。
2. 檢查特定文字、回應碼（例如 200），或使用 JSONPath 進行 API 測試。

### 非 GUI 模式
適用於大型測試或自動化：
- 從命令列執行 JMeter：
  ```
  jmeter -n -t mytest.jmx -l results.jtl
  ```
  - `-n`：非 GUI 模式。
  - `-t`：測試計劃檔案。
  - `-l`：結果記錄檔（例如 `.jtl`）。
- 產生 HTML 報告：
  ```
  jmeter -n -t mytest.jmx -l results.jtl -e -o report_folder
  ```
  - `-e`：產生報告。
  - `-o`：HTML 報告的輸出資料夾。

### 分散式測試
適用於高負載：
1. 在不同機器上設定多個 JMeter 實例。
2. 配置主機的 `jmeter.properties` 檔案以包含從屬 IP。
3. 從主機執行測試以協調負載生成。

---

## 額外提示
- **支援的協定**：除了 HTTP，JMeter 還支援 FTP、JDBC、JMS 等，使其適用於各種系統。
- **伺服器監控**：將 JMeter 與伺服器端工具（例如 PerfMon）配對，以在測試期間監控 CPU、記憶體和資料庫效能。
- **真實模擬**：新增 **HTTP Cookie Manager**、**HTTP Cache Manager** 或 **Timers** 以模擬瀏覽器行為或使用者思考時間。
- **功能測試**：使用斷言驗證回應正確性，而不僅僅是效能。

---

## 結論
使用 JMeter 的步驟：
1. 安裝並與 Java 一起啟動 GUI。
2. 建立包含線程組、取樣器和監聽器的測試計劃。
3. 配置測試元素（使用者、請求等）。
4. 執行測試並分析結果。

對於簡單入門，可如上所述測試網頁如 `example.com`。隨著經驗積累，探索進階功能如參數化、關聯處理和分散式測試，以處理複雜的現實場景。JMeter 的靈活性和廣泛文件使其成為對初學者和進階測試人員都有價值的工具。