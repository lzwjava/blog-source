---
audio: false
generated: true
lang: hant
layout: post
title: 在 VSCode 中使用 Cline
translated: true
type: note
---

### 重點摘要
- Cline 似乎可透過安裝擴充功能在 VSCode 中使用，只需建立帳戶並透過自然語言指令互動即可。
- 研究顯示配置 API 供應商（如 OpenRouter）可增強功能，但需要 API 金鑰。
- 現有證據傾向支持 Cline 具備程式碼生成與終端機指令執行等進階功能，並可選配設定特定模型。

---

### 安裝與設定
要在 VSCode 中開始使用 Cline，請先確保已從[官方網站](https://code.visualstudio.com)安裝 VSCode。接著開啟 VSCode，進入擴充功能檢視畫面（點擊擴充功能圖示或按 `Ctrl+Shift+X`（Windows/Linux）／`Cmd+Shift+X`（macOS）），搜尋「Cline」後點擊「安裝」。安裝完成後，點擊活動列中的 Cline 圖示或使用指令選擇器（`Ctrl+Shift+P` 或 `Cmd+Shift+P`）開啟 Cline，然後在 [app.cline.bot](https://app.cline.bot) 建立帳戶登入，即可獲得免費點數且無需綁定信用卡。

### 使用 Cline
設定完成後，可在聊天視窗輸入自然語言指令與 Cline 互動，例如「生成排序陣列的函式」或「建立名為 'hello-world' 的新專案資料夾，並加入顯示藍色大字 'Hello World' 的簡易網頁」。Cline 能生成程式碼、解釋內容、除錯，甚至經您許可後執行終端機指令（如安裝套件）。由於 AI 建議偶有謬誤，套用變更前請務必審查所有修改內容。

### 配置 API 供應商
若要強化功能，可配置 OpenRouter 等 API 供應商。請從 [OpenRouter.ai](https://openrouter.ai) 取得 API 金鑰，接著在 Cline 設定中輸入基礎 URL（例如 `https://openrouter.ai/api/v1`）與模型 ID（例如 `deepseek/deepseek-chat`），並貼上 API 金鑰。此設定能存取特定模型以提升效能，但屬選配功能，因 Cline 預設模型開箱即用。

---

---

### 調查備註：VSCode 中使用 Cline 的完整指南

本節將基於直接回答的內容，結合截至 2025 年 3 月 21 日的最新網路研究，詳細檢視如何在 Visual Studio Code (VSCode) 中使用 AI 編程助手 Cline，全面剖析安裝、設定、使用及進階配置等環節。

#### Cline 與 VSCode 整合背景
Cline 是開源 AI 編程助手，旨在透過提供程式碼生成、除錯及終端機指令執行等功能提升開發者效率。其支援多種 AI 模型並可配置各類 API 供應商，成為 GitHub Copilot 等工具的靈活替代方案。使用者可用自然語言指令與 Cline 互動，並透過自訂指令與設定適應專案特定需求。

#### 逐步安裝與設定指南
請遵循以下詳細步驟在 VSCode 中使用 Cline：

1. **安裝 VSCode**：
   - 從[官方網站](https://code.visualstudio.com)下載並安裝 VSCode。啟動時若出現提示，請允許擴充功能執行。

2. **安裝 Cline 擴充功能**：
   - 開啟 VSCode 並導航至擴充功能檢視畫面（點擊活動列中的擴充功能圖示或按 `Ctrl+Shift+X`（Windows/Linux）／`Cmd+Shift+X`（macOS））。
   - 在搜尋欄輸入「Cline」尋找擴充功能。
   - 點擊由 saoudrizwan 開發的 Cline 擴充功能旁的「安裝」按鈕，該擴充功能可在 [VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) 取得。

3. **開啟 Cline 資料夾**：
   - 為保持結構化設定，建議開啟文件目錄中的「Cline」資料夾：
     - macOS：`/Users/[您的使用者名稱]/Documents/Cline`
     - Windows：`C:\Users\\[您的使用者名稱]\Documents\Cline`
   - 此步驟為組織專案之建議，但基礎使用時可省略。

4. **建立 Cline 帳戶並登入**：
   - 安裝後點擊活動列中的 Cline 圖示開啟擴充功能，或使用指令選擇器（`Ctrl+Shift+P` 或 `Cmd+Shift+P`）輸入「Cline: Open In New Tab」獲得最佳檢視效果。
   - 點擊 Cline 介面中的「Sign In」，將重新導向至 [app.cline.bot](https://app.cline.bot) 建立帳戶。此流程提供免費點數且無需信用卡，方便新使用者入手。

#### 配置 API 供應商以增強功能
Cline 支援多種 API 供應商以運用不同 AI 模型，配置後可提升效能並存取特定模型。此過程屬選配但建議需要進階功能的使用者設定：

- **支援的 API 供應商**：Cline 可整合 OpenRouter、Anthropic、OpenAI、Google Gemini、AWS Bedrock、Azure、GCP Vertex 等供應商，以及任何 OpenAI 相容 API 或透過 LM Studio/Ollama 的本地模型。
- **配置步驟**：
  - 在 VSCode 中開啟 Cline 擴充功能，通常透過齒輪圖標或 VSCode 設定選單存取設定。
  - 選擇偏好的 API 供應商。以 OpenRouter 為例：
    - 從 [OpenRouter.ai](https://openrouter.ai) 取得 API 金鑰，務必啟用支出限制以控制成本。
    - 輸入基礎 URL：`https://openrouter.ai/api/v1`。
    - 指定模型 ID，例如 DeepSeek Chat 的 `deepseek/deepseek-chat`。
    - 將 API 金鑰貼至指定欄位並儲存設定。
  - 若為本地設定（如使用 Ollama）：
    - 從 [ollama.com](https://ollama.com) 安裝 Ollama。
    - 拉取所需模型（例如 `ollama pull deepseek-r1:14b`），並在 Cline 中配置基礎 URL `http://localhost:11434` 與對應模型 ID。

- **效能考量**：模型選擇會根據硬體影響效能。以下表格列出不同模型規模的硬體需求：

| **模型規模** | **所需記憶體** | **建議顯示卡**       |
|--------------|----------------|---------------------|
| 1.5B         | 4GB            | 整合式顯示卡        |
| 7B           | 8–10GB         | NVIDIA GTX 1660     |
| 14B          | 16GB+          | RTX 3060/3080       |
| 70B          | 40GB+          | RTX 4090/A100       |

- **成本考量**：OpenRouter 等雲端供應商成本約為每百萬輸入 token 0.01 美元，詳細定價請參閱 [OpenRouter 定價](https://openrouter.ai/pricing)。使用 Ollama 的本地設定免費但需充足硬體支援。

#### 使用 Cline 進行編程輔助
安裝配置完成後，Cline 提供多種功能協助編程任務。以下為有效使用方式：

- **與 Cline 互動**：
  - 點擊活動列中的 Cline 圖示或使用指令選擇器在新分頁中開啟 Cline 聊天視窗。
  - 輸入自然語言指令請求協助。範例包括：
    - 「生成排序陣列的函式」。
    - 「解釋這段程式碼」。
    - 「建立名為 'hello-world' 的新專案資料夾，並製作顯示藍色大字 'Hello World' 的簡易網頁」。
  - 處理複雜任務時，提供專案目標或具體操作等上下文資訊以獲得更精準回覆。

- **進階功能**：
  - **程式碼生成與編輯**：Cline 能生成程式碼並編輯檔案。使用「Please edit /path/to/file.js」或「@filename」等指令指定檔案。它會在套用前以差異檢視顯示變更，確保您能審查修改內容。
  - **終端機指令執行**：Cline 經使用者許可後可執行終端機指令，例如安裝套件或執行建置腳本。舉例來說，您可要求「安裝最新版 Node.js」，Cline 會先確認再執行。
  - **自訂指令**：在 Cline 設定中設定自訂指令以引導其行為，例如強制執行編碼標準、定義錯誤處理偏好或建立文件規範。這些指令可專案專用，並儲存在專案根目錄的 `.clinerules` 檔案中。

- **審查與套用變更**：由於 AI 生成程式碼可能看似合理實則有誤，請務必在套用前審查。Cline 的檢查點系統可在需要時回滾變更，確保進程可控。

#### 其他訣竅與最佳實踐
為最大化 Cline 效用，請考慮以下建議：

- **提問技巧**：若不確定，可直接在 Cline 聊天視窗輸入問題，例如「如何修復此錯誤？」。提供螢幕截圖或複製的錯誤訊息等額外上下文可獲得更佳協助。
- **使用限制與透明度**：Cline 會追蹤整個任務循環與個別請求的總 token 數與 API 使用成本，讓您掌握支出狀況，尤其對使用雲端供應商時特別實用。
- **社群支援**：如需進一步協助，請加入 [Cline Discord 社群](https://discord.gg/cline)，此處可找到疑難排解指南並與其他使用者交流。
- **模型選擇**：根據需求選擇模型，選項包括 Anthropic Claude 3.5-Sonnet、DeepSeek Chat 與 Google Gemini 2.0 Flash 等，各自在編程任務中具備不同優勢。

#### 意外細節：模型部署的靈活性
Cline 有個值得玩味的特點是同時支援雲端與本地模型部署的靈活性。雖然多數使用者可能預期雲端 AI 助手會佔主導地位，但 Cline 透過 Ollama 整合本地設定的能力，讓具備充足硬體的用戶能享受免費、注重隱私的編程輔助。這種雙軌模式滿足了從預算考量開發者到重視資料安全用戶的多元需求，對開源愛好者尤其相關。

#### 結論
總括而言，在 VSCode 中使用 Cline 需安裝擴充功能、建立帳戶，並透過自然語言指令互動獲得編程輔助。配置 OpenRouter 等 API 供應商可透過存取特定模型增強功能，另可選配透過 Ollama 進行本地設定以節省成本。Cline 的程式碼生成、終端機指令執行與自訂指令等進階功能，使其成為開發者的強大工具，但建議審慎檢查 AI 生成輸出。截至 2025 年 3 月 21 日，本指南提供了運用 Cline 提升編程效率的全面指引。

---

### 主要參考文獻
- [Cline 官方網站新手入門指南](https://docs.cline.bot/getting-started/getting-started-new-coders)
- [Cline AI 自動化編程代理 for VS Code](https://cline.bot/)
- [Cline GitHub 儲存庫](https://github.com/cline/cline)
- [如何在 VSCode 中使用 Cline 搭配 DeepSeek R1](https://apidog.com/blog/free-deepseek-r1-vscode-cline/)
- [VSCode Marketplace Cline 擴充功能](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev)
- [Cline Discord 社群](https://discord.gg/cline)
- [OpenRouter AI 平台](https://openrouter.ai)
- [Ollama 官方網站](https://ollama.com)
- [OpenRouter AI 定價](https://openrouter.ai/pricing)