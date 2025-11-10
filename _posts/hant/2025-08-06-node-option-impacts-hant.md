---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 節點選項對 VS Code 的影響
translated: true
type: note
---

### 1. **關於更新查詢的快速說明**
感謝指正——`--openssl-legacy-provider` 確實是有效的 Node.js 運行時選項（根據版本在 Node.js v15/v17 中引入），與 `--legacy-peer-deps` 不同（後者是 npm 安裝程式標誌，不屬於 `NODE_OPTIONS`）。您的問題現在似乎是：為什麼使用 `code .`（在 VS Code 中開啟當前目錄的 CLI 指令）有時會受到 `NODE_OPTIONS="--openssl-legacy-provider"` 的影響，以及兩者之間有何關聯？

總結我的回應：此 Node 選項解決了新版 Node.js 中的 OpenSSL 3.0 相容性問題，而 VS Code 依賴於此（因為它基於 Electron，一個基於 Node.js 的框架）。通過 `NODE_OPTIONS` 全域設定此選項可能會導致 VS Code 的行為變化，特別是當從終端機啟動時。我將在下面解釋原因和機制。

### 2. **`--openssl-legacy-provider` 的作用是什麼？**
- **目的**：在 Node.js v17+（以及某些 v15 版本）中，OpenSSL 升級到 v3.0，出於安全和現代標準的考慮，棄用了某些舊版加密演算法和提供者。標誌 `--openssl-legacy-provider` 告訴 Node.js 載入舊版 OpenSSL 提供者，允許繼續使用舊版加密方法（例如 MD5 雜湊，以保持向後相容性）。如果沒有此標誌，依賴這些舊版方法的應用程式可能會拋出錯誤，例如 `Error: error:0308010C:digital envelope routines::unsupported`。
- **何時需要**：通常用於具有未更新到 OpenSSL 3.0 的舊版函式庫、建置工具或依賴項的開發環境中。例如：
  - 如 React（帶有某些 Webpack 配置）的框架。
  - 舊版 SSL/TLS 憑證或客戶端函式庫。
  - VS Code 中處理檔案加密、驗證或建置的擴充功能或工具。
- **並非總是必要**：這是一個臨時解決方案。許多專案正在更新依賴項，但如果您使用舊版工具（例如 Node 基礎擴充功能的舊版本），此標誌可以保持運行。

### 3. **為什麼 VS Code 會受到影響**
VS Code 運行在 Electron 上，後者將 Node.js 作為其運行時捆綁。當 VS Code 啟動（或其子進程如擴充功能或集成終端機運行）時，它使用 Node.js 並繼承環境變數如 `NODE_OPTIONS`。以下是可能發生的情況：
- **加密相關錯誤**：某些 VS Code 功能或擴充功能（例如 JavaScript/TypeScript 的語言伺服器、Git 集成、偵錯工具，或處理加密檔案/憑證的擴充功能）可能使用舊版加密 API。如果 Node.js 無法在沒有 `--openssl-legacy-provider` 的情況下訪問它們，您可能會看到：
  - 擴充功能載入失敗（例如「無法載入憑證」或「錯誤：不支援的操作」）。
  - 集成終端機中的建置/偵錯進程崩潰。
  - 開發人員工具中的效能緩慢或警告（幫助 > 切換開發人員工具）。
- **效能或不穩定性**：載入舊版提供者會增加輕微開銷，因此可能導致 VS Code「受到影響」（例如，如果提供者不必要地啟用，則啟動稍慢或記憶體使用量增加）。
- **並非總是問題**：如果 VS Code 使用沒有 OpenSSL 3.0 嚴格性的 Node 版本建置，或者您的專案/擴充功能是最新的，此選項可能無效甚至導致細微問題（例如，在現代選項可用時強制使用舊版模式）。

關鍵點：VS Code 的核心並非本身「損壞」——它設計用於支援各種 Node 版本和環境——但全域 `NODE_OPTIONS` 覆蓋可能與其捆綁的運行時衝突。

### 4. **這與使用 `code .` 開啟目錄的關聯**
- **直接連結**：`code .` 從您的終端機工作階段啟動 VS Code 作為子進程。它繼承了您的 shell 環境（包括 `NODE_OPTIONS`），因此任何全域 Node 運行時標誌（如 `--openssl-legacy-provider`）都會傳遞給 VS Code 的 Node 進程。
  - **為什麼僅限終端機？** 如果您雙擊 VS Code 應用程式圖示或使用 GUI 開啟資料夾，它會啟動自己的進程而不繼承 bash/zsh/PowerShell 環境變數。這意味著問題可能僅在使用終端機中的 `code .` 時出現，其他情況下不會。
  - **示例流程**：
    - 您在 shell 中設定 `export NODE_OPTIONS="--openssl-legacy-provider"`（例如在 `~/.bashrc` 或 `~/.zshrc` 中）。
    - 在帶有 Node 基礎工具的目錄中運行 `code .`（例如具有舊版加密函式庫的專案）。
    - VS Code 啟動，但 Node 進程（例如用於擴充功能的進程）現在強制使用舊版 OpenSSL 模式，導致相容性問題或錯誤，而如果 VS Code 在沒有該標誌的情況下運行則不會發生。
- **為什麼「有時」？** 這取決於：
  - **VS Code 版本**：舊版本（捆綁 Node <17）不需要此標誌，而新版本（例如帶有 Electron/Node 18+ 的 VS Code 1.70+）如果您的依賴項是舊版，則可能在不使用此標誌時觸發問題。
  - **您的專案內容**：開啟普通目錄（例如沒有 npm/專案檔案）可能沒有影響，但具有加密密集型擴充功能的 Node.js 專案（例如 ESLint、Prettier 或偵錯工具）可能會暴露問題。
  - **作業系統/Node 設定**：在 Linux/macOS/Windows 上工作，但全域環境變數行為不同（例如 PowerShell vs. Bash）。

如果 VS Code 在沒有此標誌的情況下遇到不支援的加密操作，它會記錄錯誤或細微失敗——因此在使用 `code .` 時會「受到影響」。

### 5. **疑難排解與修復**
- **測試不使用 NODE_OPTIONS**：暫時取消設定（`unset NODE_OPTIONS` 或匯出為空）並運行 `code .` 查看問題是否持續。
- **專案特定修復**：將 `--openssl-legacy-provider` 添加到 `.nvmrc`、`package.json` 腳本或本地環境檔案中，而不是全域設定。例如，在 VS Code 中：開啟集成終端機並直接使用該標誌運行 Node 指令。
- **更新依賴項/擴充功能**：檢查 VS Code/擴充功能是否需要更新（幫助 > 檢查更新）。許多問題源於過時的函式庫——如果可能，升級 Node/npm。
- **檢查版本**：運行 `node --version` 和 `code --version` 以確認。如果您使用 Node 18+，該標誌可能解決錯誤；否則，可能不需要。
- **日誌和詳細模式**：使用 `code --verbose .` 或檢查 VS Code 的開發人員工具以查找 Node/遊戲相關錯誤。

如果這仍然不清楚（或出現錯誤），請分享您的作業系統、VS Code/Node 版本或具體錯誤訊息以獲得更多精確建議。VS Code 關於運行時問題和 Node 相容性的文件很有用：https://code.visualstudio.com/docs/supporting/troubleshoot。