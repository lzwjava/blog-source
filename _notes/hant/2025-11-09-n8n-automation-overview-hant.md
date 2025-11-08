---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: n8n 工作流程自動化平台概覽
translated: true
type: note
---

n8n（讀音為 "n-eight-n"）是一款開源的工作流程自動化平台，專為技術團隊和開發者設計。它能讓您連接不同的應用程式、服務和 API，自動化重複性任務、資料流和複雜流程，無需重度依賴自定義代碼——儘管在需要時仍支援代碼編寫。您可以將其視為 Zapier 或 Make 等工具的自託管替代方案，但具有更高的靈活性，包括能夠構建多步驟 AI 代理、整合任何大型語言模型（LLM），並在自有基礎設施上運行所有內容，以實現更好的資料隱私和控制。

n8n 的核心採用視覺化、基於節點的介面，透過拖放和連接「節點」（代表觸發器、操作或轉換的構建模組）來構建工作流程。它採用公平代碼許可（原始碼可在 GitHub 上取得），支援超過 400 種預建整合（例如 Google Sheets、Slack、OpenAI、GitHub），並能處理從簡單通知到進階 AI 驅動自動化的所有內容，例如總結工單或生成內容。

### 主要功能
- **視覺化工作流程建構器**：透過拖放節點實現無代碼設置，並可嵌入 JavaScript、Python 甚至 npm/Python 函式庫以實現自定義邏輯。
- **AI 整合**：使用 LangChain 等工具構建多步驟代理，連接任何 LLM（本地或雲端），並建立用於查詢資料或透過 Slack、SMS 或語音執行任務的聊天介面。
- **自託管與安全性**：透過 Docker 或 npm 實現完整的本地部署；支援 SSO、加密密鑰、RBAC 和審計日誌。無供應商鎖定——亦可自行託管 AI 模型。
- **混合開發**：將 UI 與代碼結合；重播資料進行測試、內嵌日誌進行除錯，並提供 1,700 多個模板以供快速入門。
- **可擴展性**：企業級功能如工作流程歷史記錄、Git 版本控制、隔離環境以及面向客戶的自動化嵌入。
- **效能實例**：例如 Delivery Hero 每月節省 200 多小時；StepStone 將數週工作壓縮至數小時內完成。

與 Zapier 相比，n8n 對開發者更友好（可存取代碼、自託管）、成本效益更高（核心免費，無按任務收費）且更注重隱私（資料不經第三方路由）。非常適合處理金融、醫療或內部運營中敏感資料的團隊。

# 如何使用 n8n：完整指南

本指南將引導您從設定到進階使用的所有步驟。我們將使用一個實際範例：一個每日發送新文章郵件的 RSS 摘要監控器（可擴展至 AI 摘要）。假設您具備基本技術知識；n8n 運行於 Node.js 環境。

## 1. 安裝與設定

n8n 輕量且啟動迅速。先決條件：本地安裝需 Node.js（建議 v18+）；容器化部署需 Docker。生產環境請使用 VPS，如 DigitalOcean 或 AWS。

### 快速本地啟動（開發/測試）
1. 開啟終端機。
2. 執行：`npx n8n`
   - 這將暫時下載並啟動 n8n。
3. 在瀏覽器中存取編輯器：`http://localhost:5678`
   - 預設登入：初始無需憑證（後續為安全性請設定）。

### 持久本地安裝（npm）
1. 全域安裝：`npm install n8n -g`
2. 啟動：`n8n start`
3. 存取：`http://localhost:5678`。

### Docker（推薦用於生產環境）
1. 拉取映像：`docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n`
   - 此命令映射儲存卷以實現資料持久化。
2. 進階設定（例如 PostgreSQL 資料庫）：使用文件中的 `docker-compose.yml`。
3. 存取：`http://localhost:5678`。

### 雲端選項
- **n8n Cloud**：在 n8n.io 上的託管服務——註冊後數分鐘內即可部署，免費版有限制。
- **第三方 PaaS**：使用 Render、Railway 或 Sevalla（一鍵模板）。Sevalla 範例：
  1. 在 sevalla.com 註冊。
  2. 選擇 "n8n" 模板，部署資源（例如 1 CPU、1GB RAM）。
  3. 獲得類似 `https://your-n8n.sevalla.app` 的 URL。

**提示**：自託管時，請使用 HTTPS 確保安全（透過反向代理如 Nginx），設定環境變數（例如 `N8N_BASIC_AUTH_ACTIVE=true`），並備份 `~/.n8n` 資料夾。高負載工作流程可使用隊列模式進行擴展。

## 2. 使用者介面概覽

開啟後：
- **畫布**：用於工作流程的空白工作區。點擊 "+" 添加節點。
- **節點面板**：可搜尋的 400 多個節點庫（例如 "Schedule Trigger"）。
- **執行面板**：測試期間即時顯示資料流。
- **側邊欄**：工作流程設定、執行歷史、模板。
- **頂部欄**：儲存、啟用/停用切換、分享/匯出選項。

工作流程會自動儲存；團隊中使用 Git 進行版本控制。

## 3. 核心概念

- **工作流程**：一系列連接的節點，定義自動化邏輯。啟用的工作流程在觸發時運行；停用的用於測試。
- **節點**：模組化區塊：
  - **觸發器**：啟動工作流程（例如 Schedule 用於定時任務、Webhook 用於 HTTP 事件、RSS Read 用於摘要）。
  - **操作**：執行工作（例如 Send Email、HTTP Request 用於 API、Function 用於自定義代碼）。
  - **核心節點**：IF（條件判斷）、Merge（合併資料）、Set（操作變數）。
- **連接**：節點間的箭頭顯示資料流（JSON 格式）。一個節點的資料供下一個節點使用。
- **表達式**：動態佔位符，如 `{{ $json.title }}` 用於將資料（例如文章標題）拉取到欄位中。使用 `$now` 取得時間戳記或 `$input.all()` 用於批次處理。
- **憑證**：用於 API 金鑰/OAuth 的安全儲存。每個服務設定一次（例如 Gmail OAuth）並在節點間重複使用。
- **執行**：工作流程的運行；檢視日誌、重播資料或除錯錯誤。

## 4. 建立您的第一個工作流程：逐步指南

讓我們構建「每日 RSS 摘要郵件」。

1. **建立新工作流程**：
   - 點擊 "New" > 命名為 "RSS Digest"。
   - 畫布開啟。

2. **添加觸發器節點**：
   - 點擊 "+" > 搜尋 "Schedule Trigger"。
   - 設定：觸發器 "Every Day" 於 9:00 AM（cron：`0 9 * * *`）。
   - 測試：點擊 "Execute Node"（立即執行一次）。

3. **添加資料獲取節點**：
   - 點擊觸發器後的 "+" > "RSS Read"。
   - URL：`https://blog.cloudflare.com/rss/`。
   - 執行：獲取項目（例如帶有 title、link、pubDate 的 JSON）。

4. **轉換資料（可選的 Function 節點）**：
   - "+" > "Function"。
   - 代碼：
     ```
     // 限制為前 3 個項目
     return items.slice(0, 3);
     ```
   - 這將對傳入資料執行 JS。

5. **添加操作節點**：
   - "+" > "Gmail"（或 "Email Send" 用於 SMTP）。
   - 憑證：點擊 "Create New" > 為 Gmail 進行 OAuth（遵循 Google 驗證流程）。
   - 收件人：您的郵箱。
   - 主旨：`Daily Digest: {{ $input.first().json.title }}`
   - 訊息：使用表達式循環項目：
     ```
     {{#each $input.all()}}
     - {{ $json.title }}: {{ $json.link }} ({{ $json.pubDate }})
     {{/each}}
     ```
   - （使用類似 Handlebars 的語法進行循環。）

6. **連接與測試**：
   - 拖曳箭頭：Trigger → RSS → Function → Email。
   - "Execute Workflow"：觀察資料流；檢查收件箱。
   - 修復錯誤：紅色節點突顯問題（例如無效憑證）。

7. **啟用**：
   - 切換 "Active" 為開啟。現在它將每日運行。

儲存並匯出為 JSON 以供分享。

## 5. 構建更複雜的工作流程

- **條件判斷**：在 RSS 後添加 "IF" 節點：`{{ $json.pubDate }} > {{ $now.minus({days:1}) }}` 以篩選新項目。
- **循環與批次**：使用 "Split In Batches" 處理大型資料集。
- **錯誤處理**：添加 "Error Trigger" 工作流程或 "IF" 進行重試。使用 "Set" 記錄錯誤。
- **API 整合**："HTTP Request" 節點用於自定義端點（例如 POST 到 Slack webhook）。
- **資料操作**："Edit Fields" 或 Function 節點用於 JSON 調整。
- **測試**：重播特定執行；在節點中模擬資料。

範例：Twitter 監控
1. 觸發器："Twitter Trigger" 於提及時觸發。
2. AI 節點："OpenAI" 用於分類情感。
3. IF：正面 → 新增至 CRM；負面 → Slack 警報。

## 6. 進階使用與最佳實踐

- **AI 工作流程**：添加 "AI Agent" 節點 > 與工具鏈結（例如搜尋、總結）。透過 "Ollama" 節點整合本地 LLM。
- **自定義節點**：透過 JS 構建（文件教程）；發布至社群。
- **擴展**：使用隊列模式（`N8N_WORKER=1`）、外部資料庫（PostgreSQL）和 webhook 實現即時處理。
- **安全性**：加密密鑰、為團隊使用 RBAC、審計日誌。
- **除錯**：在 Functions 中使用內嵌日誌（`console.log(items)`）；使用 Git 進行版本控制。
- **常見陷阱**：注意資料類型（全部為 JSON）；在節點中處理速率限制；在引入 AI 前從簡單開始。
- **擴充功能**：嵌入應用程式、使用模板（超過 1700 個可用）或 npm 獲取額外功能。

對於生產環境，透過外部工具進行監控；自託管可節省成本（相較於 Zapier 的 20+ 美元/月）。

## 參考資料
- [n8n 官方網站](https://n8n.io/)
- [n8n 文件 - 安裝](https://docs.n8n.io/hosting/installation/)
- [freeCodeCamp 初學者指南](https://www.freecodecamp.org/news/a-beginners-guide-to-automation-with-n8n/)
- [n8n 工作流程文件](https://docs.n8n.io/workflows/)
- [Medium：精通 n8n 指南](https://medium.com/data-science-collective/mastering-n8n-from-scratch-a-step-by-step-guide-for-beginners-its-easier-than-you-think-2d7ca5d47277)
- [維基百科：n8n](https://en.wikipedia.org/wiki/N8n)