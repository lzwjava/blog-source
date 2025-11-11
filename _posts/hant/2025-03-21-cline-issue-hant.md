---
audio: false
generated: true
lang: hant
layout: post
title: Visual Studio Code 中的 Cline 擴充功能問題
translated: true
type: note
---

看來你在 Visual Studio Code (VSCode) 中遇到 Cline 擴充功能的問題，它無法偵測到新建的檔案，也無法識別 `@mention` 功能。根據 Cline 作為 AI 驅動的編碼助手背景，以下是疑難排解和潛在解決這些問題的方法：

---

### 1. Cline 無法偵測到新建的檔案
Cline 可能無法偵測到新建檔案，原因可能是工作區索引延遲、權限問題，或是擴充功能的檔案監控機制存在錯誤。以下是修復方法：

#### 疑難排解步驟：
- **重新整理工作區**：建立新檔案後，手動重新整理 VSCode 的工作區，確保 Cline 能讀取到。
  - 按下 `Ctrl+Shift+P`（Mac 上是 `Cmd+Shift+P`）開啟命令選擇區。
  - 輸入 `Reload Window` 並選擇。這會重新載入 VSCode，強制 Cline 重新索引工作區。
  
- **檢查檔案建立方式**：如果你在 VSCode 外部建立檔案（例如透過終端機或其他編輯器），VSCode 的檔案監控可能無法立即偵測到。
  - 嘗試直接在 VSCode 中建立檔案（在 Explorer 中右鍵 > New File），看看 Cline 是否能識別。
  - 如果使用外部工具，請確保檔案儲存在 Cline 監控的工作區目錄中。

- **驗證權限**：Cline 需要讀取/寫入權限才能與檔案互動。
  - 在 VSCode 中開啟 Cline 的設定（透過 Extensions 側邊欄或命令選擇區：`Cline: Open Settings`）。
  - 確保你已授予它讀取和修改檔案的權限。如果在執行任務時出現提示，請批准該操作。

- **檢查工作區快照**：Cline 會對工作區建立快照以追蹤變更。如果它沒有更新：
  - 在 Cline 標籤頁中開始新任務（點擊 "+" 按鈕），看看重新分析工作區後是否能偵測到檔案。
  - 或者，使用 Cline 中的 `Restore` 或 `Compare` 按鈕強制重新整理工作區。

- **更新 Cline 和 VSCode**：確保你使用的是最新版本，因為與檔案偵測相關的錯誤可能已經修復。
  - 更新 VSCode：`Help > Check for Updates`。
  - 更新 Cline：在 VSCode 中前往 Extensions，找到 Cline，如果有更新按鈕則點擊它。

- **透過日誌除錯**：檢查 Cline 的日誌以尋找錯誤。
  - 在 VSCode 中開啟 Output 面板（`Ctrl+Shift+U` 或 `Cmd+Shift+U`）。
  - 從下拉選單中選擇 “Cline” 以查看其日誌。尋找有關檔案偵測失敗的訊息，並解決提到的任何特定問題（例如路徑錯誤）。

#### 可能原因：
Cline 依賴 VSCode 的檔案系統 API 來偵測變更。如果檔案未被索引或監控程式延遲，Cline 在工作區更新之前將無法看到它。

---

### 2. Cline 無法使用 @mention
Cline 中的 `@mention` 語法通常用於呼叫特定工具或功能（例如 `@url` 用於獲取網頁，或 `@problems` 用於處理工作區錯誤）。如果它無法運作，可能是由於配置錯誤、不支援的模型，或是語法誤解。

#### 疑難排解步驟：
- **驗證語法**：確保你使用的是正確的 `@mention` 語法。
  - Cline 文件中的範例：
    - `@url`：獲取 URL 並將其轉換為 markdown。
    - `@problems`：包含工作區錯誤/警告供 Cline 修復。
  - 在任務輸入欄位中完全按照文件中的方式輸入 `@mention`（區分大小寫）。例如，如果它預期的是 `@url`，則 `@Url` 或 `@URL` 可能無法運作。

- **檢查模型支援**：並非所有 Cline 支援的 AI 模型都能處理 `@mention` 功能。Claude 3.5 Sonnet（Cline 推薦）支援代理功能，但其他模型可能不支援。
  - 開啟 Cline 的設定並確認你的 API 供應商和模型。
  - 如果使用 OpenRouter 或其他供應商，請切換到 Claude 3.5 Sonnet 並重新測試。

- **使用簡單任務測試**：開始一個新任務並嘗試基本的 `@mention`：
  - 範例："Fix issues listed in @problems."
  - 如果它沒有回應，該功能可能被停用或配置錯誤。

- **啟用工具擴充功能**：某些 `@mentions`（例如自訂工具如 `@jira` 或 `@aws`）需要 Model Context Protocol (MCP) 伺服器。
  - 檢查你使用的 `@mention` 是否對應到自訂工具。如果是：
    - 要求 Cline "add a tool"（例如 "add a tool that fetches Jira tickets"）並按照提示進行設定。
    - 新增工具後重新啟動 VSCode，確保它已註冊。

- **檢查 API 金鑰**：如果 `@mention` 涉及外部請求（例如 `@url`），你的 API 金鑰可能權限不足或餘額不足。
  - 在 Cline 的設定中驗證你的 API 金鑰（例如 Anthropic 或 OpenRouter 金鑰）。
  - 確保你的帳戶有足夠的資金或存取所請求功能的權限。

- **回報錯誤**：如果上述步驟無效，可能是錯誤。
  - 造訪 Cline 的 GitHub（github.com/cline/cline）並檢查現有問題。
  - 如果沒有類似問題，請提交新問題並提供詳細資訊：你的 Cline 版本、VSCode 版本、使用的模型，以及嘗試的具體 `@mention`。

#### 可能原因：
`@mention` 功能可能未在你的設定中完全實作，或者模型的功能與預期行為之間存在不匹配。

---

### 一般提示
- **重新啟動 VSCode**：完全重新啟動可以解決擴充功能的暫時性故障。
- **重新安裝 Cline**：如果問題持續存在，請從 VSCode Marketplace 解除安裝並重新安裝該擴充功能。
- **加入 Cline 社群**：如需即時協助，請加入他們的 Discord（連結在他們的 GitHub 上），並在 #support 或 #contributors 頻道中提問。

---

### 測試修復的範例工作流程
1. 在 VSCode 中建立新檔案（例如 `test.txt`）。
2. 重新載入視窗（`Ctrl+Shift+P > Reload Window`）。
3. 開啟 Cline，開始新任務，並輸入："Read the contents of test.txt and use @problems to list any issues."
4. 批准任何權限，並檢查 Cline 是否偵測到檔案並處理 `@mention`。

如果這些步驟無法解決問題，請告訴我你的具體設定（Cline 版本、模型，以及你嘗試的 `@mention`），我會進一步深入調查！