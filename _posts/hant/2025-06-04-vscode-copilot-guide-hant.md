---
audio: false
generated: true
lang: hant
layout: post
title: 在 Visual Studio Code 中使用 GitHub Copilot
translated: true
type: note
---

GitHub Copilot 是由 GitHub 與 OpenAI 共同開發的人工智慧編碼輔助工具，旨在提升開發者在 Visual Studio Code (VS Code) 中的生產力。它提供情境感知的程式碼補全、自然語言對話及進階編輯功能。本指南將引導您設定 Copilot、探索其功能，並透過技巧與最佳實踐來優化工作流程。

## 1. GitHub Copilot 簡介
GitHub Copilot 如同一位 AI 協作程式設計師，提供即時代碼建議、解答編碼問題，並自動化重複性任務。其背後的強大語言模型經過海量公開程式碼資料訓練，能支援多種程式語言與框架，包括 Python、JavaScript、TypeScript、Ruby、Go、C# 及 C++。

主要功能包括：
- **程式碼補全**：在您輸入時建議程式碼片段，從單行到完整函式皆涵蓋。
- **Copilot 對話**：透過自然語言查詢來解釋程式碼、生成片段或除錯問題。
- **代理模式**：自動化多步驟編碼任務，如重構程式碼或建立應用程式。
- **自訂指示**：根據您的編碼風格或專案需求調整建議內容。

## 2. 在 VS Code 中設定 GitHub Copilot

### 前置準備
- **VS Code**：從[官方網站](https://code.visualstudio.com/)下載並安裝 Visual Studio Code。請確保使用相容版本（所有近期版本皆支援 Copilot）。
- **GitHub 帳戶**：您需要一個具備 Copilot 存取權的 GitHub 帳戶。選項包括：
  - **Copilot 免費版**：每月有限度的補全與對話次數。
  - **Copilot Pro/Pro+**：付費方案提供更高使用上限與進階功能。
  - **組織存取**：若由您的組織提供，請向管理員查詢詳細存取資訊。
- **網路連線**：Copilot 需保持連線狀態以提供建議。

### 安裝步驟
1. **開啟 VS Code**：
   在您的電腦上啟動 Visual Studio Code。

2. **安裝 GitHub Copilot 擴充功能**：
   - 前往 **擴充功能** 視圖 (Ctrl+Shift+X 或 macOS 的 Cmd+Shift+X)。
   - 在擴充功能市集中搜尋 "GitHub Copilot"。
   - 點擊官方 GitHub Copilot 擴充功能的 **安裝**。此操作將自動安裝 Copilot 對話擴充功能。

3. **登入 GitHub**：
   - 安裝後，VS Code 狀態列（右下角）可能會顯示設定 Copilot 的提示。
   - 點擊 Copilot 圖示並選擇 **登入**，以透過您的 GitHub 帳戶進行驗證。
   - 若未顯示提示，請開啟命令選擇區 (Ctrl+Shift+P 或 Cmd+Shift+P) 並執行 `GitHub Copilot: Sign in` 命令。
   - 依照瀏覽器驗證流程，將 VS Code 提供的代碼複製到 GitHub。

4. **驗證啟用狀態**：
   - 登入後，狀態列上的 Copilot 圖示應轉為綠色，表示已啟用。
   - 若您沒有 Copilot 訂閱，將自動加入 Copilot 免費版方案，享有每月有限的使用額度。

5. **選項：停用遙測資料收集**：
   - 預設情況下，Copilot 會收集遙測資料。若要停用，請前往 **設定** (Ctrl+, 或 Cmd+,)，搜尋 `telemetry.telemetryLevel` 並設為 `off`。或於 `GitHub Copilot Settings` 中調整 Copilot 相關設定。

> **注意**：若您的組織已停用 Copilot 對話或限制功能，請聯絡管理員。疑難排解請參閱 [GitHub Copilot 疑難排解指南](https://docs.github.com/en/copilot/troubleshooting)。[](https://code.visualstudio.com/docs/copilot/setup)

## 3. GitHub Copilot 在 VS Code 中的核心功能

### 3.1 程式碼補全
Copilot 會根據您的程式碼情境與檔案結構，在您輸入時建議程式碼，從單行到完整函式或類別皆涵蓋。
- **運作方式**：
  - 在支援的語言中開始輸入（如 JavaScript、Python、C#）。
  - Copilot 會以灰階「幽靈文字」顯示建議。
  - 按下 **Tab** 接受建議，或繼續輸入以忽略。
  - 使用 **Alt+]**（下一個）或 **Alt+[**（上一個）循環檢視多個建議。
- **範例**：
  ```javascript
  // 計算數字的階乘
  function factorial(n) {
  ```
  Copilot 可能建議：
  ```javascript
  if (n === 0) return 1;
  return n * factorial(n - 1);
  }
  ```
  按下 **Tab** 接受建議。

- **技巧**：
  - 使用描述性函式名稱或註解引導 Copilot（例如 `// 以升序排序陣列`）。
  - 對於多個建議，可將滑鼠懸停於建議上，開啟補全面板 (Ctrl+Enter) 檢視所有選項。

### 3.2 Copilot 對話
Copilot 對話讓您能以自然語言與 Copilot 互動，詢問問題、生成程式碼或除錯問題。
- **開啟對話**：
  - 從活動列開啟 **對話視圖**，或使用 **Ctrl+Alt+I** (Windows/Linux) 或 **Cmd+Ctrl+I** (macOS)。
  - 亦可使用 **行內對話** (Ctrl+I 或 Cmd+I) 在編輯器中直接進行情境相關查詢。
- **使用情境**：
  - **解釋程式碼**：選取程式碼區塊，開啟行內對話，輸入 `explain this code`。
  - **生成程式碼**：在對話視圖中輸入 `write a Python function to reverse a string`。
  - **除錯**：將錯誤訊息貼至對話中並請求修復。
- **範例**：
  在對話視圖中輸入：
  ```
  What is recursion?
  ```
  Copilot 會回覆詳細解釋，通常包含 Markdown 格式的程式碼範例。

- **斜線命令**：
  使用如 `/explain`、`/doc`、`/fix`、`/tests` 或 `/optimize` 等命令指定任務。例如：
  ```
  /explain this function
  ```
  搭配選取的函式將生成詳細解釋。

### 3.3 代理模式 (預覽)
代理模式讓 Copilot 能自主處理多步驟編碼任務，例如建立應用程式、重構程式碼或撰寫測試。
- **使用方式**：
  - 在 VS Code Insiders 或 Stable 版本中開啟 **Copilot Edits View**。
  - 從模式下拉選單中選擇 **Agent**。
  - 輸入提示，例如 `Create a React form component with name and email fields`。
  - Copilot 將分析您的程式庫，建議編輯，並可執行終端機命令或測試。
- **功能**：
  - 跨多檔案生成程式碼。
  - 監控錯誤並迭代修復問題。
  - 整合新函式庫或遷移程式碼至現代框架。

> **注意**：代理模式為實驗性功能，在小型程式庫中表現最佳。請透過 VS Code GitHub 程式庫回饋意見。[](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)

### 3.4 自訂指示
自訂 Copilot 以符合您的編碼風格或專案需求。
- **設定**：
  - 在您的工作區建立 `.github/copilot-instructions.md` 檔案。
  - 以 Markdown 格式加入指示，例如 `Use snake_case for Python variable names`。
  - 在 **設定** > **GitHub** > **Copilot** > **Enable custom instructions** 中啟用自訂指示（需 VS Code 17.12 或更新版本）。
- **範例**：
  ```markdown
  # Copilot 自訂指示
  - JavaScript 變數使用 camelCase。
  - 對於 Promise，優先使用 async/await 而非 .then()。
  ```
  Copilot 將根據這些偏好調整建議。

### 3.5 使用 @workspace 查詢工作區情境
使用 `@workspace` 命令查詢整個程式庫。
- **範例**：
  在對話視圖中輸入：
  ```
  @workspace Where is the database connection string configured?
  ```
  Copilot 將搜尋您的工作區並參考相關檔案。

### 3.6 下一步編輯建議 (預覽)
Copilot 根據您最近的變更預測並建議下一步邏輯編輯。
- **運作方式**：
  - 當您編輯程式碼時，Copilot 會突顯潛在的下一步編輯。
  - 使用 **Tab** 接受建議，或透過行內對話修改。
- **使用情境**：適合用於迭代重構或完成相關程式碼變更。

## 4. 優化 Copilot 使用的技巧與訣竅

### 4.1 撰寫有效的提示
- 具體明確：與其輸入 `write a function`，嘗試 `write a Python function to sort a list of dictionaries by the 'age' key`。
- 提供情境：包含框架或函式庫細節（例如 `use React hooks`）。
- 使用註解：撰寫 `// Generate a REST API endpoint in Express` 來引導補全。

### 4.2 善用情境
- **參考檔案/符號**：在對話提示中使用 `#filename`、`#folder` 或 `#symbol` 來限定情境範圍。
  ```
  /explain #src/utils.js
  ```
- **拖放功能**：將檔案或編輯器分頁拖曳至對話提示中以提供情境。
- **附加圖片**：在 VS Code 17.14 Preview 1 或更新版本中，可附加螢幕截圖說明問題（例如 UI 錯誤）。

### 4.3 使用斜線命令
- `/doc`：為函式生成文件。
- `/fix`：針對錯誤建議修復方式。
- `/tests`：為選取的程式碼建立單元測試。
- 範例：
  ```
  /tests Generate Jest tests for this function
  ```

### 4.4 儲存與重複使用提示
- 在 `.github/prompts/` 中建立 `.prompt.md` 檔案以儲存可重複使用的提示。
- 範例：
  ```markdown
  # React 元件提示
  生成一個使用 Tailwind CSS 樣式的 React 功能元件。若未提供元件名稱與屬性，請主動詢問。
  ```
- 在對話中附加提示以跨專案重複使用。

### 4.5 選擇合適的模型
- Copilot 支援多種語言模型（例如 GPT-4o、Claude Sonnet）。
- 在對話視圖下拉選單中選擇模型，以實現更快的編碼或更深層的推理。
- 對於複雜任務，Claude Sonnet 在代理模式中可能表現更佳。[](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)

### 4.6 為工作區建立索引
- 啟用工作區索引以實現更快速、更精準的程式碼搜尋。
- 對於 GitHub 程式庫使用遠端索引，或對大型程式庫使用本地索引。

## 5. 最佳實踐
- **檢視建議**：始終驗證 Copilot 的建議是否準確且符合專案標準。
- **與 IntelliCode 結合**：在 Visual Studio 中，Copilot 與 IntelliCode 互補以增強補全功能。[](https://devblogs.microsoft.com/visualstudio/github-copilot-in-visual-studio-2022/)
- **檢查安全性**：Copilot 可能建議含有弱點的程式碼。請檢視建議，特別是在敏感專案中，並確認符合組織政策。[](https://medium.com/%40codebob75/how-to-use-copilot-in-visual-studio-a-step-by-step-guide-b2a5db3b54ba)
- **使用有意義的名稱**：描述性變數與函式名稱可提升建議品質。
- **透過對話迭代**：若初始建議不理想，請精煉提示內容。
- **監控使用限制**：使用 Copilot 免費版時，可透過 GitHub 帳戶設定或 VS Code 中的 Copilot 徽章追蹤每月補全與對話次數。[](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-free-plan?view=vs-2022)

## 6. 常見問題疑難排解
- **Copilot 未啟用**：請確保您已使用具備 Copilot 存取權的 GitHub 帳戶登入。透過 Copilot 狀態列下拉選單重新整理憑證。
- **無建議顯示**：檢查網路連線或切換至支援的語言。於 **工具** > **選項** > **GitHub Copilot** 中調整設定。
- **功能受限**：若達到 Copilot 免費版使用上限，將恢復為 IntelliCode 建議。請升級至付費方案或檢查您的狀態。[](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-free-plan?view=vs-2022)
- **網路問題**：請參閱 [GitHub Copilot 疑難排解指南](https://docs.github.com/en/copilot/troubleshooting)。

## 7. 進階使用情境
- **資料庫查詢**：要求 Copilot 生成 SQL 查詢（例如 `Write a SQL query to join two tables`）。
- **API 開發**：請求 API 端點程式碼（例如 `Create a Flask route to handle POST requests`）。
- **單元測試**：使用 `/tests` 為 Jest 或 Pytest 等框架生成測試。
- **重構**：使用代理模式跨檔案重構程式碼（例如 `Migrate this jQuery code to React`）。

## 8. 隱私與安全性考量
- **資料使用**：Copilot 會即時傳輸程式碼片段至 GitHub 伺服器以生成建議，但不會保留這些片段（Copilot for Business 會立即丟棄片段）。[](https://medium.com/%40codebob75/how-to-use-copilot-in-visual-studio-a-step-by-step-guide-b2a5db3b54ba)
- **公開程式碼匹配**：Copilot 可能建議與公開 GitHub 程式庫匹配的程式碼。啟用程式碼參考功能以檢視授權詳細資訊。[](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-extension?view=vs-2022)
- **組織政策**：確認您的組織是否允許使用 Copilot，因部分組織可能停用對話或限制建議。[](https://docs.github.com/en/copilot/quickstart)
- **遙測資料**：若需要，可在 VS Code 設定中停用遙測。[](https://code.visualstudio.com/docs/copilot/setup)

## 9. 進一步學習資源
- [GitHub Copilot 文件](https://docs.github.com/en/copilot)
- [VS Code Copilot 快速入門](https://code.visualstudio.com/docs/copilot/copilot-quickstart)
- [Copilot 對話教學](https://code.visualstudio.com/docs/copilot/copilot-chat)
- [VS Code Copilot 系列 YouTube 影片](https://www.youtube.com/playlist?list=PLj6YeMhvp2S6X0vF4TrRkpZ7GIqM3oPWp)
- [GitHub Copilot 常見問題](https://docs.github.com/en/copilot/faq)

## 10. 結論
GitHub Copilot 在 VS Code 中是一個強大的工具，透過提供智慧建議、解答問題及自動化複雜任務，使編碼流程更順暢。透過正確設定、善用其功能並遵循最佳實踐，您能顯著提升生產力，專注於創意編碼任務。嘗試 Copilot 的各項功能，根據工作流程自訂它，並留意安全性與使用限制，以充分發揮這位 AI 協作程式設計師的潛力。