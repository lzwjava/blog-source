---
audio: false
generated: true
lang: hant
layout: post
title: 如何使用 JMeter
translated: true
type: note
---

JMeter 是一款開源軟件工具，專為負載測試及測量網絡應用程式的效能而設計，同時亦可用於測試其他類型的系統，例如數據庫和 FTP 伺服器。以下提供清晰的分步指南，協助你開始使用 JMeter 進行效能測試，主要聚焦於網絡應用程式。

---

#### **步驟 1：安裝 JMeter**
- **前置需求**：JMeter 是基於 Java 的應用程式，因此必須先在你的電腦上安裝 Java（版本 8 或以上）。你可以在命令行中執行 `java -version` 來驗證。
- **下載**：請瀏覽 [Apache JMeter 網站](https://jmeter.apache.org/) 並下載最新版本（.zip 或 .tgz 檔案）。
- **安裝**：將下載的檔案解壓縮至你選擇的目錄（例如 Windows 上的 `C:\JMeter` 或 Linux/Mac 上的 `/opt/jmeter`）。無需其他安裝步驟。

---

#### **步驟 2：啟動 JMeter**
- 進入 JMeter 資料夾內的 `bin` 目錄（例如 `C:\JMeter\apache-jmeter-x.x\bin`）。
- **Windows**：雙擊 `jmeter.bat` 或透過命令行執行。
- **Linux/Mac**：開啟終端機，進入 `bin` 目錄，並執行 `./jmeter.sh`。
- 圖形用戶界面（GUI）將會開啟，顯示 JMeter 工作台。

---

#### **步驟 3：建立測試計劃**
- **測試計劃** 是你的效能測試基礎，它概述了你想測試的內容及方式。
- 在 JMeter GUI 中，左側窗格已顯示測試計劃。右鍵點擊它來重新命名（例如「網絡效能測試」）或保留原名。

---

#### **步驟 4：加入線程組**
- **線程組** 模擬將請求傳送至伺服器的用戶。
- 右鍵點擊測試計劃 > **加入** > **Threads (Users)** > **Thread Group**。
- 配置：
  - **Number of Threads (users)**：設定你想要的虛擬用戶數量（例如 10）。
  - **Ramp-Up Period (seconds)**：啟動所有線程所需的時間（例如 10 秒代表每秒啟動 1 個線程）。
  - **Loop Count**：重複測試的次數（例如 1，或勾選「Forever」以進行連續測試）。

---

#### **步驟 5：加入取樣器**
- **取樣器** 定義傳送至伺服器的請求。對於網絡測試，請使用 HTTP Request 取樣器。
- 右鍵點擊線程組 > **加入** > **Sampler** > **HTTP Request**。
- 配置：
  - **Server Name or IP**：輸入目標網站（例如 `example.com`）。
  - **Path**：指定端點（例如 `/login`）。
  - **Method**：根據你的測試場景選擇 `GET`、`POST` 等。

---

#### **步驟 6：加入監聽器**
- **監聽器** 顯示並分析測試結果。
- 右鍵點擊線程組 > **加入** > **Listener** > （例如 **View Results Tree** 或 **Summary Report**）。
- 常用選項：
  - **View Results Tree**：顯示詳細的請求/回應數據。
  - **Summary Report**：提供聚合指標，例如平均回應時間和錯誤率。

---

#### **步驟 7：配置測試**
- 使用其他元素增強你的測試（可選但實用）：
  - **計時器**：在請求之間加入延遲（例如右鍵點擊線程組 > **加入** > **Timer** > **Constant Timer**）。
  - **斷言**：驗證伺服器回應（例如右鍵點擊 HTTP Request > **加入** > **Assertions** > **Response Assertion**）。
  - **配置元素**：設定變數或 HTTP 預設值（例如 **HTTP Request Defaults**）。

---

#### **步驟 8：執行測試**
- 將你的測試計劃儲存為 `.jmx` 檔案以便重複使用（**檔案** > **儲存**）。
- 點擊工具列中的綠色 **Run** 按鈕（三角形）或前往 **Run** > **Start**。
- JMeter 將根據你的線程組設定執行測試。

---

#### **步驟 9：分析結果**
- 測試完成後，檢查監聽器：
  - **View Results Tree**：檢查個別請求的成功/失敗。
  - **Summary Report**：檢視吞吐量、回應時間和錯誤百分比等指標。
- 找出需要調查的瓶頸（例如緩慢的回應時間）或錯誤。

---

#### **步驟 10：優化測試**
- 根據結果調整你的測試計劃：
  - 增加/減少線程數量。
  - 加入更真實的場景（例如多個 HTTP 請求）。
  - 微調計時器或斷言以提升準確性。
- 儲存並重新執行測試以驗證改進。

---

### 額外提示
- **儲存與載入**：使用 `.jmx` 檔案儲存測試計劃，並透過 **檔案** > **開啟** 載入。
- **GUI 與非 GUI 模式**：對於大型測試，請在非 GUI 模式下執行 JMeter（例如 `jmeter -n -t test.jmx -l results.jtl`）以節省系統資源。
- **深入學習**：隨著經驗累積，探索進階功能，例如參數化（用於動態數據）或關聯（用於動態網絡應用程式）。

本指南提供了有效開始使用 JMeter 的基本知識。透過練習，你可以根據特定的效能測試需求自訂測試！