---
audio: false
generated: true
lang: hant
layout: post
title: 開發提示
translated: true
type: note
---

以下是一些針對您提及主題的常用開發工程師提示詞，涵蓋：**在 Visual Studio Code 中使用 GitHub Copilot**、**在 Visual Studio Code 中調試 Spring Boot 應用程式**、**IBM Db2 資料庫的鎖定機制**、**在 VSCode 中配置 Spring Boot 的 launch.json**，以及**為 WebSphere Liberty 指定 JDK**。這些提示詞遵循常見模式，例如配置路徑、啟用詳細輸出，並涉及調試、優化和安全性等程式設計各方面。它們設計靈活，可根據您的具體需求進行調整。

---

### 在 Visual Studio Code 中使用 GitHub Copilot
這些提示詞幫助您在 Visual Studio Code (VSCode) 中利用 GitHub Copilot 進行編碼、調試和理解任務：

- **程式碼生成**  
  - 「生成一個計算數字階乘的 Python 函數。」  
  - 「創建一個帶有用戶名和密碼欄位的 React 登入組件。」  

- **重構**  
  - 「重構此程式碼，使用 async/await 替代 promises。」  
  - 「將這個大型函數拆分為更小、可重用的輔助函數。」  

- **理解程式碼**  
  - 「解釋這段程式碼的作用：[貼上程式碼片段]。」  
  - 「這個變數在程式中的用途是什麼？」  

- **調試協助**  
  - 「對此錯誤建議修復方法：[貼上錯誤訊息]。」  
  - 「如何添加日誌記錄來追蹤此函數的執行流程？」  

---

### 在 Visual Studio Code 中調試 Spring Boot 應用程式
這些提示詞專注於在 VSCode 中設置和排查 Spring Boot 應用程式的調試：

- **設置調試**  
  - 「如何在 VSCode 中設置 launch.json 來調試 Spring Boot 應用程式？」  
  - 「示範如何在 VSCode 中的 Spring Boot 控制器添加斷點。」  

- **問題排查**  
  - 「為什麼我的 Spring Boot 應用程式在 VSCode 的調試模式下啟動失敗？」  
  - 「在調試 Spring Boot 應用程式時，如何檢查變數值？」  

- **詳細輸出**  
  - 「如何在 Spring Boot 調試會話中啟用詳細日誌記錄？」  
  - 「示範如何在 VSCode 中配置異常的詳細堆疊追蹤。」  

- **進階調試**  
  - 「如何在 VSCode 中對 Spring Boot 應用程式使用條件斷點？」  
  - 「調試多線程的 Spring Boot 應用程式的最佳方法是什麼？」  

---

### IBM Db2 資料庫的鎖定機制
這些提示詞幫助您理解和管理 IBM Db2 中的鎖定機制：

- **理解鎖定**  
  - 「IBM Db2 中有哪些不同的鎖定類型？」  
  - 「Db2 如何處理行級鎖定與表級鎖定？」  

- **管理鎖定**  
  - 「如何檢查 IBM Db2 資料庫中的活動鎖？」  
  - 「我可以採取哪些步驟來預防 Db2 中的鎖競爭？」  

- **問題排查**  
  - 「如何識別和解決 IBM Db2 中的死結？」  
  - 「為什麼我的 Db2 查詢在等待鎖定，如何解決？」  

- **詳細輸出**  
  - 「如何在 Db2 日誌中啟用詳細的鎖定資訊？」  
  - 「示範如何配置 Db2 以輸出鎖等待詳情。」  

---

### 在 VSCode 中配置 Spring Boot 的 launch.json
這些提示詞協助設置和排查 VSCode 中 Spring Boot 應用程式的 `launch.json` 文件：

- **基本配置**  
  - 「提供一個 VSCode 中 Spring Boot 應用程式的基本 launch.json 範例。」  
  - 「如何在 launch.json 中為 Spring Boot 項目設置主類別？」  

- **路徑配置**  
  - 「如何在 launch.json 中配置 Spring Boot 調試的 JDK 路徑？」  
  - 「示範如何在 launch.json 中指定項目路徑。」  

- **進階配置**  
  - 「如何為調試在 launch.json 中添加環境變數？」  
  - 「在 VSCode 中遠程調試 Spring Boot 應用程式的設置是什麼？」  

- **問題排查**  
  - 「為什麼 VSCode 提示 '找不到主類別'，儘管我的 launch.json 配置正確？」  
  - 「如何修復 launch.json 中的 '調試器未附加' 問題？」  

---

### 為 WebSphere Liberty 指定 JDK
這些提示詞幫助配置和排查 WebSphere Liberty 的 JDK：

- **路徑配置**  
  - 「如何在環境中為 WebSphere Liberty 設置 JDK 路徑？」  
  - 「示範如何更新 WebSphere Liberty 以使用 JDK 11。」  

- **問題排查**  
  - 「為什麼 WebSphere Liberty 未檢測到我安裝的 JDK？」  
  - 「如何檢查 WebSphere Liberty 正在使用的 JDK 版本？」  

- **詳細輸出**  
  - 「如何在 WebSphere Liberty 中啟用詳細的 JDK 日誌記錄？」  
  - 「哪個命令可以在 Liberty 中顯示詳細的 JDK 啟動資訊？」  

- **最佳實踐**  
  - 「WebSphere Liberty 推薦使用哪些 JDK 版本？」  
  - 「如何確保我的應用程式在 Liberty 中使用正確的 JDK？」  

---

### 通用程式設計提示模式
這些提示詞涵蓋程式設計任務中的常見模式，例如配置、詳細輸出，以及優化和安全性等其他方面：

- **路徑配置**  
  - 「如何在 [環境] 中配置 [工具/庫] 的路徑？」  
  - 「示範如何設置 [應用程式/框架] 的 classpath。」  

- **詳細輸出**  
  - 「如何啟用 [工具/應用程式] 的詳細日誌記錄？」  
  - 「如何從 [命令/進程] 獲取詳細輸出？」  

- **調試**  
  - 「建議調試此問題的步驟：[描述問題]。」  
  - 「如何在 [語言/框架] 中追蹤執行流程？」  

- **性能優化**  
  - 「如何優化此程式碼以加快執行速度？」  
  - 「有哪些方法可以減少 [應用程式] 的記憶體使用？」  

- **安全性**  
  - 「如何保護 [應用程式/組件] 防範 [漏洞]？」  
  - 「[技術] 的安全最佳實踐是什麼？」  

---

這些提示詞實用、可重複使用，並針對您指定的任務量身定制。您可以通過添加具體細節（例如錯誤訊息、程式碼片段或工具版本）來修改它們，以適應項目需求。無論您是使用 GitHub Copilot 編碼、調試 Spring Boot、管理 Db2 鎖定、配置 VSCode，還是設置 WebSphere Liberty，這些提示詞都將幫助簡化您的開發工作流程。