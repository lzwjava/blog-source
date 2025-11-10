---
audio: false
generated: true
image: false
lang: hant
layout: post
title: GitHub Copilot 指令行介面整合
translated: true
type: note
---

你無法直接透過像 `code --plugin copilot "hi"` 這樣的語法從命令列調用 GitHub Copilot 作為插件來獲得回應。不過，GitHub Copilot 確實透過 GitHub CLI 的 `gh copilot` 擴充功能提供了命令列整合，該功能提供了一個類似聊天的介面用於命令建議和解釋。這與透過 `code` 命令調用的通用插件並不完全相同，但對於命令列互動來說，它起到了類似的作用。

### GitHub Copilot 在 CLI 中的詳細資訊
- **要求**：你需要擁有 GitHub Copilot 訂閱、安裝了 GitHub CLI (`gh`) 以及安裝了 `gh-copilot` 擴充功能。設定說明可在 GitHub CLI 儲存庫或文件中找到 [GitHub CLI 安裝](https://cli.github.com/) 和 [在 CLI 中安裝 GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)。
- **使用方法**：設定完成後，你可以使用如下命令：
  - `gh copilot suggest -t shell "hi"` 來獲得 shell 命令建議。
  - `gh copilot explain "hi"` 來獲得命令的解釋。
  - 例如：執行 `gh copilot suggest -t shell "say hello"` 可能會建議 `echo "hello"` 或在 macOS 上建議文字轉語音命令如 `say "hello"`，具體取決於上下文。
- **限制**：CLI 介面專為命令列相關任務（例如 shell、Git 或 GitHub CLI 命令）設計，不支援像聊天機器人那樣的通用對話回應。它也只支援英文提示 [在 CLI 中負責任地使用 GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/responsible-use-of-github-copilot-in-the-cli)。[](https://docs.github.com/en/copilot/responsible-use/copilot-in-the-cli)[](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-in-the-cli)
- **互動模式**：執行 `suggest` 命令後，Copilot 會啟動一個互動式會話，你可以在其中完善建議、執行它（複製到剪貼簿）或對其進行評分。要自動執行，你需要設定 `ghcs` 別名 [在命令列中使用 GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)。[](https://docs.github.com/en/copilot/how-tos/use-copilot-for-common-tasks/use-copilot-in-the-cli)[](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)

### 為什麼 `code --plugin copilot "hi"` 不起作用
- **Visual Studio Code CLI**：`code` 命令（用於 VS Code）支援像 `--install-extension` 這樣的選項來安裝擴充功能，但它沒有 `--plugin` 標誌來直接使用像 `"hi"` 這樣的輸入調用擴充功能。像 GitHub Copilot 這樣的擴充功能通常在 VS Code 編輯器內運行，提供內嵌建議或聊天介面，而不是作為獨立的 CLI 工具 [VS Code 中的 GitHub Copilot](https://code.visualstudio.com/docs/copilot/overview)。[](https://code.visualstudio.com/docs/copilot/overview)
- **Copilot 的架構**：GitHub Copilot 的 VS Code 插件與語言伺服器和 GitHub 的後端通訊以獲取程式碼補全和聊天功能。沒有公開的 API 或 CLI 機制可以從命令列直接將像 `"hi"` 這樣的任意字串傳遞給插件並獲得回應 [如何以程式方式調用 Github Copilot？](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically)。[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
- **通用輸入的替代方案**：如果你想將像 `"hi"` 這樣的提示發送給 Copilot 並獲得回應，你需要使用 VS Code 或其他支援的 IDE 中的 Copilot Chat，或者探索其他支援對話式提示的 AI CLI 工具（例如，微軟用於 Azure CLI 的 AI Shell）[在 Azure 中使用 Microsoft Copilot 與 AI Shell](https://learn.microsoft.com/en-us/azure/copilot/use-copilot-cli)。[](https://learn.microsoft.com/en-us/azure/copilot/ai-shell-overview)

### 針對你目標的解決方法
如果你的目標是從命令列調用像 Copilot 這樣的 AI 助手，並使用像 `"hi"` 這樣的提示來獲得回應，你可以：
1. **使用 `gh copilot` 處理命令列任務**：
   - 安裝 GitHub CLI 和 Copilot 擴充功能。
   - 執行 `gh copilot suggest -t shell "greet with hi"` 來獲得像 `echo "hi"` 這樣的命令。
   - 這僅限於命令列上下文，因此單獨的 `"hi"` 可能不會產生有意義的回應，除非將其構建為命令請求。
2. **使用 VS Code 的 Copilot Chat**：
   - 打開 VS Code，使用 Copilot Chat 介面（可透過 `⌃⌘I` 或聊天圖示訪問），然後輸入 `"hi"` 來獲得對話式回應。
   - 這需要在編輯器內進行手動互動，而不是 CLI 調用 [GitHub Copilot in VS Code 速查表](https://code.visualstudio.com/docs/copilot/copilot-cheat-sheet)。[](https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features)
3. **探索其他 AI CLI 工具**：
   - **AI Shell**：微軟的 AI Shell 允許在 CLI 中使用自然語言提示處理 Azure 相關任務。你可以安裝它並嘗試像 `"hi"` 這樣的提示，儘管它針對 Azure CLI 和 PowerShell 命令進行了優化 [在 Azure 中使用 Microsoft Copilot 與 AI Shell](https://learn.microsoft.com/en-us/azure/copilot/use-copilot-cli)。[](https://learn.microsoft.com/en-us/azure/copilot/ai-shell-overview)
   - **自訂腳本**：你可以編寫一個腳本來與 AI 模型的 API（例如，如果可訪問，則使用 OpenAI 的 API）互動，以處理像 `"hi"` 這樣的提示。然而，GitHub Copilot 的 API 並未公開用於此類用途 [如何以程式方式調用 Github Copilot？](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically)。[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
4. **模擬插件行為**：
   - 建立一個 shell 腳本或別名，將輸入傳遞給 `gh copilot suggest` 或其他 AI CLI 工具。
   - 例如：
     ```bash
     alias ai='gh copilot suggest -t shell'
     ai "greet with hi"
     ```
     這將建議一個像 `echo "hi"` 或類似的命令。

### 以程式方式調用
如果你正在尋找以程式方式調用類似 Copilot 的功能（如你的示例所暗示），請注意：
- GitHub Copilot 並未公開用於直接程式訪問的公共 API。一些社群努力已經對語言伺服器進行了逆向工程或使用代理來捕獲建議，但這些方法複雜且存在風險（例如，可能導致帳戶被封禁） [如何以程式方式調用 Github Copilot？](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically)。[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
- 你可以探索開源替代方案或其他具有 CLI 整合的 AI 模型（例如，Hugging Face 的 CLI 工具或帶有自訂包裝器的本地 LLM，如 LLaMA）。

### 結論
雖然 `code --plugin copilot "hi"` 不受支援，但你可以使用 `gh copilot` 處理命令列任務或使用 VS Code 中的 Copilot Chat 處理對話式提示來實現類似功能。對於通用的 CLI AI 體驗，可以考慮使用像 AI Shell 這樣的工具或使用其他 AI API 的自訂腳本。請務必驗證建議，因為 Copilot 的 CLI 回應可能包含訓練數據中的錯誤或偏見 [在 CLI 中負責任地使用 GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/responsible-use-of-github-copilot-in-the-cli)。[](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-in-the-cli)

如果你有特定的使用案例（例如，對話式 AI 與命令生成），請告訴我，我可以進一步定制解決方案！