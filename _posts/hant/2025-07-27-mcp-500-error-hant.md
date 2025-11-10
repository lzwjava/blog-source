---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 修復MCP伺服器500錯誤
translated: true
type: note
---

您遇到的錯誤是來自本地 API 端點 `http://127.0.0.1:3456` 的 500 內部伺服器錯誤，該端點似乎是 Model Context Protocol (MCP) 伺服器。這通常用於橋接本地大型語言模型 (LLMs)，例如由 Ollama 管理的模型，到應用程式如 Claude Desktop、VS Code 擴充功能 (例如 Copilot) 或 IDE 如 Cursor，以進行 AI 輔助編碼任務。底層的 JavaScript/TypeScript 錯誤—"Cannot read properties of undefined (reading 'includes')"—表明伺服器代碼在處理請求、處理響應或與 Ollama 互動時，試圖在未定義或為 null 的變數上存取 `.includes()` 方法。

此問題通常發生在呼叫 API 來分析或修復代碼（在您的情況下是 `recommend_posts.py` 腳本）時，但伺服器由於配置問題、缺少依賴項或來自後端 LLM 的意外響應而失敗。

### 疑難排解與修復步驟
1. **驗證 Ollama 是否正在執行並已配置**：
   - Ollama（本地 LLM 引擎）通常是 MCP 伺服器的後端。確保它已安裝並在其預設端口 (11434) 上執行。
   - 在終端機中執行 `curl http://localhost:11434/api/tags` 來測試。這應該會列出已安裝的模型。如果失敗或返回空列表，請使用 `ollama pull <model-name>`（例如 `ollama pull llama3`）安裝一個模型。
   - 如果 Ollama 沒有響應，請使用 `ollama serve` 啟動它，並確認沒有端口衝突。

2. **重新啟動 MCP 伺服器**：
   - 端口 3456 上的 MCP 伺服器可能處於不良狀態。終止進程：`kill -9 $(lsof -t -i:3456)`。
   - 根據您的設定重新啟動它（例如，如果使用像 `ollama-mcp` 這樣的工具，請從其文件中執行啟動命令）。檢查啟動日誌以確認與 Ollama 的成功連接。

3. **檢查端口衝突或 Claude Desktop 干擾**：
   - Claude Desktop（如果已安裝）通常使用端口 3456 進行身份驗證或 MCP。如果它正在執行，請關閉應用程式或如上所述終止其進程。
   - 如果您使用 Cursor 或 VS Code，請確認您的 settings.json 具有正確的 API 基礎 URL 且沒有拼寫錯誤。在啟動 MCP 伺服器時，通過設置環境變數（如 `PORT=4567`）暫時切換到不同的端口，然後更新您的 API 基礎以匹配。

4. **更新軟體並檢查日誌**：
   - 更新 Ollama：`ollama update`。
   - 如果使用特定的 MCP 橋接（例如來自 GitHub 儲存庫如 emgeee/mcp-ollama 或 patruff/ollama-mcp-bridge），請拉取最新版本並重新建置/重新安裝。
   - 使用詳細日誌記錄執行 MCP 伺服器（如果支援，添加標誌如 `--debug`），並檢查輸出以獲取關於什麼是未定義的線索（例如，來自 Ollama 的響應缺失或無效的請求負載）。
   - 在 Cursor 或您的 IDE 中，檢查開發者控制台（在 Cursor 中按 Ctrl+Shift+I）以獲取其他錯誤詳細資訊。

5. **直接測試 API**：
   - 使用 curl 模擬一個簡單的請求到 API：`curl -X POST http://127.0.0.1:3456/v1/chat/completions -H "Content-Type: application/json" -d '{"model": "your-model-name", "messages": [{"role": "user", "content": "Hello"}]}'`。
   - 如果它返回相同的 500 錯誤，則問題在伺服器端。如果它有效，則問題可能與您的 IDE 格式化請求的方式有關（例如，在包含檔案內容時格式錯誤的負載）。

6. **解決方法**：
   - 切換到直接的 Ollama OpenAI 相容端點：將您的 API 基礎設置為 `http://127.0.0.1:11434/v1`（Ollama 支援此功能），如果不需要 MCP 進行高級上下文功能，則繞過 MCP。
   - 使用不同的 MCP 實作或工具。例如，嘗試一個沒有 MCP 的最小 Ollama 設定來進行代碼修復。
   - 如果這是在 Cursor 中，通過移除自訂基礎 URL 暫時回退到基於雲端的模型（例如，通過官方 API 使用 Claude）。
   - 重新安裝依賴項：如果您的 MCP 伺服器使用 Node.js，請在其目錄中執行 `npm install` 以修復任何缺少的模組。

如果這些方法無法解決問題，則錯誤可能源於您特定 MCP 橋接版本中的錯誤，特別是在處理檔案內容或帖子推薦時觸發它。在 GitHub issues 中搜尋您的確切 MCP 儲存庫及錯誤訊息，或使用您的設定詳細資訊開啟一個新 issue。

[Failed to register Ollama model: TypeError: Cannot read properties of undefined (reading 'includes')](https://github.com/microsoft/vscode-copilot-release/issues/8461)  
[Ollama MCP Server on GitHub](https://github.com/emgeee/mcp-ollama)  
[Model Context Protocol Documentation](https://modelcontextprotocol.io/introduction)  
[Ollama Documentation](https://github.com/ollama/ollama)