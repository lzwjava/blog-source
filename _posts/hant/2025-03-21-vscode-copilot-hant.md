---
audio: false
generated: true
lang: hant
layout: post
title: 在 VS Code 中使用 GitHub Copilot 入門指南
translated: true
type: note
---

在 Visual Studio Code (VS Code) 中使用 GitHub Copilot 一旦設定完成後便十分簡單。以下是截至 2025 年 3 月 20 日的逐步指南：

---

### 步驟 1：安裝 VS Code
- 確保你已安裝 Visual Studio Code。如果尚未安裝，請從 [code.visualstudio.com](https://code.visualstudio.com/) 下載。
- 為獲得最佳相容性，請將 VS Code 更新至最新版本（前往 `說明 > 檢查更新`）。

---

### 步驟 2：安裝 GitHub Copilot 擴充功能
1. **開啟 VS Code**。
2. **前往擴充功能市集**：
   - 點擊左側活動列上的擴充功能圖示（或按 `Ctrl+Shift+X` / Mac 上按 `Cmd+Shift+X`）。
3. **搜尋 "GitHub Copilot"**：
   - 在搜尋列中輸入 "GitHub Copilot"。
   - 尋找由 GitHub 官方提供的擴充功能（會帶有驗證標記）。
4. **安裝擴充功能**：
   - 點擊 "GitHub Copilot" 旁邊的 `安裝` 按鈕。
5. **選擇性：安裝 Copilot Chat（推薦）**：
   - 搜尋 "GitHub Copilot Chat" 並安裝。這將增加對話式 AI 功能，例如透過聊天提問或生成程式碼。

---

### 步驟 3：登入 GitHub Copilot
1. **驗證 GitHub 帳戶**：
   - 安裝後，會出現提示要求你登入。
   - 在彈出視窗中點擊 `Sign in to GitHub`，或前往 Copilot 狀態圖示（VS Code 右下角）並選擇 "Sign in"。
2. **在瀏覽器中授權**：
   - 瀏覽器視窗將會開啟，要求你登入 GitHub 帳戶。
   - 點擊 `Authorize Git hypoxia` 批准授權請求。
3. **複製驗證碼**：
   - GitHub 將提供一次性驗證碼。複製該驗證碼並在 VS Code 提示時貼上。
4. **確認啟用**：
   - 登入後，狀態列上的 Copilot 圖示應轉為綠色，表示已啟用。你還會看到確認存取權限的通知。

---

### 步驟 4：設定 Copilot（選擇性）
- **啟用/停用建議**：
  - 前往 `檔案 > 偏好設定 > 設定`（或按 `Ctrl+,` / `Cmd+,`）。
  - 搜尋 "Copilot" 以調整設定，例如啟用行內建議或針對特定語言停用。
- **檢查訂閱狀態**：
  - Copilot 在 30 天試用期後需要訂閱（每月 $10 美元或每年 $100 美元）。學生、教師和開源維護者可透過 [GitHub Education](https://education.github.com/) 或 Copilot 設定申請免費存取。

---

### 步驟 5：開始使用 Copilot
以下是如何在編碼工作流程中運用 Copilot：

#### 1. **程式碼建議**
- **行內自動完成**：
  - 在檔案中開始輸入（例如在 Python 中輸入 `def calculate_sum(`），Copilot 將以灰色文字顯示建議完成內容。
  - 按 `Tab` 接受建議，或繼續輸入以忽略。
- **多行建議**：
  - 撰寫註解如 `// Function to sort an array` 然後按 Enter。Copilot 可能會建議完整實作（例如排序演算法）。
  - 使用 `Alt+]`（或 Mac 上按 `Option+]`）循環檢視多個建議。

#### 2. **從註解生成程式碼**
- 輸入描述性註解如：
  ```javascript
  // Fetch data from an API and handle errors
  ```
  按 Enter 後，Copilot 可能會生成：
  ```javascript
  async function fetchData(url) {
    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error('Network response was not ok');
      return await response.json();
    } catch (error) {
      console.error('Fetch error:', error);
    }
  }
  ```
- 按 `Tab` 接受或根據需要調整。

#### 3. **Copilot Chat（如已安裝）**
- **開啟聊天**：
  - 點擊側邊欄的聊天圖示或使用 `Ctrl+Alt+C`（可自訂）。
- **提問**：
  - 輸入如「Explain how Promises work in JavaScript」或「Write a Python script to read a CSV file」。
  - Copilot 將在聊天面板中回應，並可直接將程式碼插入編輯器。
- **上下文幫助**：
  - 反白程式碼，右鍵點擊並選擇「Ask Copilot」以解釋或重構該程式碼。

#### 4. **除錯與測試**
- 撰寫註解如 `// Write unit tests for this function`，Copilot 可使用 Jest 或 PyTest 等框架生成測試案例。

---

### 有效使用技巧
- **具體明確**：提供的上下文越多（例如註解、變數名稱），Copilot 的建議就越準確。
- **檢視建議**：Copilot 並非完美無缺—請務必檢查其程式碼的準確性和安全性。
- **語言支援**：它最適合熱門語言（Python、JavaScript、Java 等），但也支援數十種其他語言。
- **鍵盤快捷鍵**：
  - `Alt+\`（或 Mac 上按 `Option+\`）：手動顯示所有建議。
  - `Ctrl+Enter`：開啟建議面板。

---

### 疑難排解
- **無法運作？**：
  - 確保你已登入（檢查狀態列）。
  - 在 GitHub 帳戶設定中確認訂閱狀態為有效。
  - 如果問題持續，請重新啟動 VS Code 或重新安裝擴充功能。
- **沒有建議？**：
  - 檢查 Copilot 是否在當前語言中啟用（設定中的 `editor.inlineSuggest.enabled` 應為 true）。

---

就是這樣！你現在已經準備好在 VS Code 中使用 GitHub Copilot。開始開啟檔案，輸入一些程式碼或註解，讓 Copilot 協助你。祝編碼更智能！