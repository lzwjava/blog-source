---
audio: false
generated: true
lang: hant
layout: post
title: 安裝與使用 Gemini 命令行工具
translated: true
type: note
---

以下是一份關於安裝、設定及使用 **Google Gemini CLI** 的簡明指南。這是一個開源 AI 代理，能將 Gemini 的功能整合到您的終端機中，用於編碼、任務自動化等用途。本指南基於截至 2025 年 6 月 29 日的最新可用資訊。

---

## **Google Gemini CLI 指南**

### **什麼是 Gemini CLI？**
Gemini CLI 是由 Google 開發的開源命令列工具，將 Gemini 2.5 Pro 模型（擁有 100 萬個 token 的上下文視窗）的強大功能帶到您的終端機。它支援編碼、除錯、內容生成、任務自動化以及多模態任務（例如圖像和影片生成）。使用 Google 帳戶即可免費使用，並能與 Google 搜尋及 Model Context Protocol (MCP) 伺服器等工具整合。

---

### **先決條件**
- **Node.js**：版本 18 或更高。使用 `node -v` 檢查。如需安裝，請至 [nodejs.org](https://nodejs.org)。
- **Google 帳戶**：免費使用 Gemini 2.5 Pro 所必需（每分鐘 60 個請求，每日 1,000 個請求）。
- （可選）**API 金鑰**：如需更高限制或使用特定模型，請從 [Google AI Studio](https://aistudio.google.com) 生成。
- （可選）**Docker**：用於 MCP 伺服器整合（例如 GitHub 工具）。

---

### **安裝**
有兩種方式可以開始使用 Gemini CLI：

1. **全域安裝**：
   ```bash
   npm install -g @google/gemini-cli
   gemini
   ```
   這會全域安裝 CLI，並使用 `gemini` 命令執行。

2. **無需安裝直接執行**：
   ```bash
   npx https://github.com/google-gemini/gemini-cli
   ```
   這會直接執行 CLI，無需安裝，適合測試用途。

---

### **設定**
1. **啟動 CLI**：
   - 在終端機中執行 `gemini`。
   - 首次執行時，選擇主題（例如 ASCII、dark、light）並按 Enter。

2. **驗證**：
   - 選擇 **Login with Google** 以獲得免費存取（建議大多數使用者使用）。
   - 瀏覽器視窗將會開啟；使用您的 Google 帳戶登入。
   - 或者，使用 API 金鑰：
     - 從 [Google AI Studio](https://aistudio.google.com) 生成金鑰。
     - 將其設為環境變數：
       ```bash
       export GEMINI_API_KEY=YOUR_API_KEY
       ```
     - 這對於更高限制或企業用途很有用。

3. **導航至您的專案**：
   - 在您的專案根目錄中執行 `gemini`，以便為程式碼相關任務提供上下文。

---

### **基本用法**
Gemini CLI 在互動式的 Read-Eval-Print Loop (REPL) 環境中運作。輸入命令或自然語言提示來與 Gemini 模型互動。以下是一些常見任務：

1. **程式碼解釋**：
   - 導航至專案資料夾並執行：
     ```bash
     gemini
     ```
   - 提示：`Explain the architecture of this project` 或 `Describe the main function in main.py`。
   - CLI 會讀取檔案並提供結構化解釋。

2. **程式碼生成**：
   - 提示：`Create a simple to-do app in HTML, CSS, and JavaScript`。
   - CLI 會生成程式碼，並可應要求儲存至檔案。

3. **除錯**：
   - 貼上錯誤訊息或堆疊追蹤並詢問：`What’s causing this error?`。
   - CLI 會分析錯誤並建議修復，可能使用 Google 搜尋來獲取額外上下文。

4. **檔案管理**：
   - 提示：`Organize my PDF invoices by month of expenditure`。
   - CLI 可以操作檔案或轉換格式（例如將圖像轉為 PNG）。

5. **GitHub 整合**：
   - 使用 MCP 伺服器進行 GitHub 任務（例如列出 issue）：
     - 在 `.gemini/settings.json` 中使用 Personal Access Token (PAT) 設定 GitHub MCP 伺服器。
     - 提示：`Get all open issues assigned to me in the foo/bar repo`。
   - 執行 `/mcp` 以列出已設定的 MCP 伺服器和工具。

6. **多模態任務**：
   - 使用 Imagen 或 Veo 等工具生成媒體：
     - 提示：`Create a short video of a cat’s adventures in Australia using Veo`。

---

### **主要功能**
- **上下文檔案 (GEMINI.md)**：在您的專案根目錄中添加 `GEMINI.md` 檔案，以定義編碼風格、專案規則或偏好設定（例如「對 JavaScript 使用 async/await」）。CLI 會使用此檔案來提供量身訂製的回應。
- **內建工具**：
   - `/tools`：列出可用工具（例如 Google 搜尋、檔案操作）。
   - `/compress`：總結聊天上下文以節省 token。
   - `/bug`：直接向 Gemini CLI GitHub 儲存庫提交 issue。
- **非互動模式**：用於腳本編寫，透過管道傳遞命令：
   ```bash
   echo "Write a Python script" | gemini
   ```
- **對話記憶**：使用 `/save <tag>` 儲存對話歷史，並使用 `/restore <tag>` 恢復。
- **自訂設定**：
   - 編輯 `~/.gemini/settings.json` 以進行全域設定，或在專案中編輯 `.gemini/settings.json` 以進行本地設定。
   - 範例：設定 MCP 伺服器或自訂主題。

---

### **提示與技巧**
- **從計劃開始**：對於複雜任務，先要求計劃：`Create a detailed implementation plan for a login system`。這能確保結構化輸出。
- **使用本地上下文**：在 `GEMINI.md` 中編碼專案特定細節，而不是依賴 MCP 伺服器，以獲得更快、可靠的回應。
- **除錯**：使用 `DEBUG=true gemini` 啟用詳細日誌記錄，以獲取詳細的請求/回應資訊。
- **審查變更**：在批准前始終審查檔案修改或命令（輸入 `y` 確認）。
- **探索工具**：執行 `/tools` 以發現內建功能，例如網路搜尋或記憶體儲存。

---

### **疑難排解**
- **驗證問題**：確保您的 Google 帳戶或 API 金鑰有效。使用 `/auth` 切換方法。
- **速率限制**：免費層級允許每分鐘 60 個請求和每日 1,000 個請求。如需更高限制，請使用 API 金鑰或 Vertex AI。
- **錯誤**：查看 GitHub 上的[疑難排解指南](https://github.com/google-gemini/gemini-cli/docs/troubleshooting.md)。
- **回應緩慢**：CLI 處於預覽階段，進行 API 呼叫時可能較慢。請在 GitHub 上提交意見回饋。

---

### **進階用法**
- **MCP 伺服器整合**：
  - 設定 GitHub MCP 伺服器以進行儲存庫互動：
    - 建立具有必要範圍的 GitHub PAT。
    - 添加到 `.gemini/settings.json`：
      ```json
      {
        "mcpServers": [
          {
            "name": "github",
            "url": "http://localhost:8080",
            "type": "github"
          }
        ]
      }
      ```
    - 為 MCP 伺服器執行 Docker 容器（請參閱 GitHub 文件）。
- **腳本編寫**：透過將 Gemini CLI 整合到腳本中來自動化任務：
  ```bash
  gemini --non-interactive "Generate a bash script to backup my files"
  ```
- **多模態提示**：
  - 範例：`Describe this image: path/to/image.jpg`（需要支援視覺的模型，如 `gemini-pro-vision`）。

---

### **限制**
- **預覽階段**：Gemini CLI 處於正式發布前階段，可能支援有限或存在錯誤。
- **非完全開源**：僅 CLI UI 是 Apache 2.0 授權；Gemini 模型是專有的。
- **配額共享**：如果使用 Gemini Code Assist，限制是共享的。
- **未來定價**：預覽階段後的定價尚不明確；進階功能可能需要付費。

---

### **資源**
- **官方 GitHub**：[github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- **文件**：[gemini-cli.click](https://gemini-cli.click) 或 GitHub 文件
- **部落格公告**：[blog.google](https://blog.google)
- **意見回饋**：在 GitHub 上提交錯誤或建議。

---

### **範例工作流程**
1. 安裝：`npm install -g @google/gemini-cli`
2. 執行：`cd my-project && gemini`
3. 驗證：使用 Google 登入。
4. 提示：`Write a Python script for a REST API with FastAPI`。
5. 審查並儲存生成的程式碼。
6. 使用 `/tools` 探索其他功能，例如 GitHub 整合。

---

Gemini CLI 是一個功能強大的工具，為開發者提供無縫的 AI 終端機整合。從簡單開始，利用 `GEMINI.md` 提供上下文，並探索其多模態功能以提升生產力。如需更多範例，請查看 [GitHub 教程](https://github.com/google-gemini/gemini-cli/docs/cli/tutorials.md)。

如果您需要特定範例或對某個功能有疑問，請告訴我！