---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 配置 Copilot 以使用自訂模型
translated: true
type: note
---

當你在 GitHub Copilot 中選擇「託管模型」時，如果仍然看到 GPT-4.1 作為預設模型，或者無法如預期使用 OpenRouter 提供的 Grok 或 Kimi 模型，可能有以下幾個原因及解決步驟。以下是問題分析及如何透過 OpenRouter 配置 Copilot 使用 Grok 或 Kimi 模型：

### 為何仍使用 GPT-4.1
1. **預設模型設定**：GitHub Copilot 預設在 Copilot Chat、Edits 和 Agent Mode 中使用 GPT-4.1，除非明確變更。即使選擇了「託管模型」，如果未完全配置 OpenRouter 整合或選擇特定模型，預設模型可能仍會保留。[](https://github.blog/changelog/2025-05-08-openai-gpt-4-1-is-now-generally-available-in-github-copilot-as-the-new-default-model/)
2. **情境特定模型使用**：Copilot 的「修復框」（內嵌聊天或程式碼補全）在某些情境下可能不支援切換到自訂模型（如 Grok 或 Kimi）。例如，Copilot Chat 面板或內嵌建議可能使用預設模型（GPT-4.1），除非你在沉浸式視圖或 Agent Mode 中明確切換到自訂模型。[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
3. **OpenRouter 整合限制**：OpenRouter 允許存取如 Grok（由 xAI 創建）和 Kimi（來自 Moonshot AI）等模型，但 Copilot 與 OpenRouter 的整合需要特定設定，且由於 API 限制或配置問題，並非所有模型都能立即使用。例如，OpenRouter 的 API 可能未對所有模型宣布工具支援，這會阻止 Agent Mode 或某些功能與 Grok 或 Kimi 協作。[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)
4. **訂閱或配置限制**：如果你使用免費層級或非 Pro/Business 的 Copilot 訂閱，可能會受限於預設模型（如 GPT-4.1）。此外，某些模型（例如 Grok 或 Kimi）可能需要透過 OpenRouter 進行特定配置或高級存取。[](https://www.reddit.com/r/LocalLLaMA/comments/1jslnxb/github_copilot_now_supports_ollama_and_openrouter/)[](https://github.com/microsoft/vscode-copilot-release/issues/10193)

### 如何透過 OpenRouter 在 Copilot 中使用 Grok 或 Kimi 模型
要透過 OpenRouter 在 Copilot 中使用 Grok 或 Kimi 模型（特別是「修復框」的內嵌聊天或程式碼補全），請遵循以下步驟：

1. **設定 Copilot 與 OpenRouter**：
   - **取得 OpenRouter API 金鑰**：在 [openrouter.ai](https://openrouter.ai) 註冊並取得 API 金鑰。確保你有點數或支援存取 Grok (xAI) 和 Kimi (Moonshot AI K2) 模型的方案。[](https://openrouter.ai/models)[](https://openrouter.ai)
   - **在 VS Code 中配置 OpenRouter**：
     - 開啟 Visual Studio Code (VS Code) 並確保已安裝最新版 GitHub Copilot 擴充功能 (v1.100.2 或更新版本)。[](https://github.com/microsoft/vscode-copilot-release/issues/10193)
     - 前往狀態列中的 Copilot 儀表板，或開啟命令選擇區 (`Ctrl+Shift+P` 或 Mac 上的 `Command+Shift+P`) 並輸入 `GitHub Copilot: Manage Models`。
     - 新增你的 OpenRouter API 金鑰並配置端點以包含 OpenRouter 模型。你可能需要遵循 OpenRouter 的文件來整合 VS Code 的 Copilot 擴充功能。[](https://www.reddit.com/r/LocalLLaMA/comments/1jslnxb/github_copilot_now_supports_ollama_and_openrouter/)
   - **驗證模型可用性**：新增 OpenRouter 端點後，在 Copilot 的「Manage Models」部分檢查。模型選擇器中應出現如 `openrouter/xai/grok` 或 `openrouter/moonshotai/kimi-k2` 等模型。如果沒有出現，請確保你的 OpenRouter 帳戶有權存取這些模型且沒有限制（例如免費層級限制）。[](https://github.com/microsoft/vscode-copilot-release/issues/10193)

2. **為修復框切換模型**：
   - **對於內嵌聊天 (修復框)**：「修復框」很可能指的是 Copilot 的內嵌聊天或程式碼補全功能。要變更內嵌聊天的模型：
     - 在 VS Code 中開啟 Copilot Chat 介面（透過標題列或側邊欄的圖示）。
     - 在聊天視圖中，選擇 `CURRENT-MODEL` 下拉選單（通常在右下角），並選擇 `openrouter/xai/grok` 或 `openrouter/moonshotai/kimi-k2`（如果可用）。[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
     - 如果下拉選單未顯示 Grok 或 Kimi，可能是因為 OpenRouter 的 API 未對這些模型宣布工具支援，這會限制它們在 Copilot 某些功能（如 Agent Mode 或內嵌修復）中的使用。[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)
   - **對於程式碼補全**：要變更程式碼補全（不僅僅是聊天）的模型：
     - 開啟命令選擇區 (`Ctrl+Shift+P` 或 `Command+Shift+P`) 並輸入 `GitHub Copilot: Change Completions Model`。
     - 從清單中選擇所需的 OpenRouter 模型（例如 Grok 或 Kimi）。請注意，由於 VS Code 目前僅支援 Ollama 端點用於自訂模型，並非所有 OpenRouter 模型都支援程式碼補全，儘管 OpenRouter 可以透過代理解決方法運作。[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-completion-model)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)

3. **OpenRouter 模型的解決方法**：
   - **代理解決方案**：由於 OpenRouter 的 API 並非總是宣布工具支援（Agent Mode 或進階功能所需），你可以使用如 `litellm` 的代理來在 Copilot 中啟用 Grok 或 Kimi。編輯 `config.yaml` 檔案以包含：
     ```yaml
     model_list:
       - model_name: grok
         litellm_params:
           model: openrouter/xai/grok
       - model_name: kimi-k2
         litellm_params:
           model: openrouter/moonshotai/kimi-k2
     ```
     - 遵循如 [Bas codes](https://bas.codes) 或 [DEV Community](https://dev.to) 等來源的設定說明，以獲取配置代理的詳細步驟。[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)
   - **重新啟動 VS Code**：配置代理後，重新啟動 VS Code 以確保新模型在模型選擇器中可用。

4. **檢查訂閱與權限**：
   - **Copilot 訂閱**：確保你有 Copilot Pro 或 Business 訂閱，因為免費層級使用者可能無法新增自訂模型。[](https://www.reddit.com/r/LocalLLaMA/comments/1jslnxb/github_copilot_now_supports_ollama_and_openrouter/)
   - **商業限制**：如果你使用 Copilot Business 訂閱，你的組織必須啟用模型切換功能。請向管理員查詢或參考 GitHub 關於管理 Copilot 政策的文件。[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
   - **OpenRouter 點數**：確認你的 OpenRouter 帳戶有足夠點數存取高級模型（如 Grok 或 Kimi），因為這些模型可能消耗比其他模型更多的點數。[](https://www.reddit.com/r/GithubCopilot/comments/1la87wr/why_are_gh_copilot_pro_models_so_much_worse_than/)

5. **修復框疑難排解**：
   - 如果修復框仍使用 GPT-4.1，可能是因為內嵌聊天功能在某些情境下（例如非沉浸式視圖）鎖定為預設模型。嘗試切換到 Copilot Chat 的沉浸式視圖 (`https://github.com/copilot`) 以明確選擇 Grok 或 Kimi。[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
   - 如果 Grok 或 Kimi 未出現在模型選擇器中，請再次檢查 `Manage Models` 中的 OpenRouter 整合。你可能需要重新整理模型清單或重新新增 OpenRouter API 金鑰。[](https://github.com/microsoft/vscode-copilot-release/issues/10193)
   - 如果問題持續存在，請先在 Copilot 的 Agent Mode 或聊天介面中測試模型以確認它們能正常運作，然後再嘗試將它們應用於內嵌修復。

6. **替代工具**：
   - 如果 Copilot 與 OpenRouter 的整合仍然有問題，考慮直接透過 [grok.com](https://grok.com) 或 Grok iOS/Android 應用程式使用 Grok，它們提供帶有使用配額的免費存取。Kimi 模型也可以透過 OpenRouter 的聊天介面測試以確保可存取性。[](https://openrouter.ai)
   - 為了更流暢的體驗，你可以探索其他 IDE 或工具，如 Cursor，據悉它能與 OpenRouter 的 Kimi K2 模型良好協作。[](https://openrouter.ai)

### 補充說明
- **模型效能**：Grok 針對推理和求真進行了優化，使其適合複雜的除錯或架構任務，而 Kimi (K2) 可能在特定編碼情境中表現出色。測試兩者以查看哪個更適合你的使用情境。[](https://github.blog/ai-and-ml/github-copilot/which-ai-model-should-i-use-with-github-copilot/)
- **社群回饋**：一些使用者回報 OpenRouter 模型未出現在 Copilot 的模型選擇器中的問題，特別是免費層級帳戶。這可能需要付費的 OpenRouter 方案或 Copilot Pro 訂閱來解決。[](https://github.com/microsoft/vscode-copilot-release/issues/10193)[](https://www.reddit.com/r/GithubCopilot/comments/1la87wr/why_are_gh_copilot_pro_models_so_much_worse_than/)
- **持續限制**：關於在 Copilot 中直接啟用自訂 API 端點的討論仍在進行中（參見 [microsoft/vscode-copilot-release#7518](https://github.com/microsoft/vscode-copilot-release/issues/7518)）。在此功能實現之前，代理解決方法是使用 Grok 或 Kimi 最可靠的方法。[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)

### 引用來源
- [Changing the AI model for Copilot Chat - GitHub Docs](https://docs.github.com/en/copilot/managing-copilot/changing-the-ai-model-for-copilot-chat)[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
- [How to Use Third Party Models in GitHub Copilot Agent Mode - Bas codes](https://bas.codes)[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)
- [Openrouter - openrouter.ai](https://openrouter.ai)[](https://openrouter.ai/models)
- [Agent Mode With Third-Party Models in Copilot - DEV Community](https://dev.to)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)
- [Openrouter - openrouter.ai](https://openrouter.ai)[](https://openrouter.ai)
- [r/LocalLLaMA on Reddit: Github Copilot now supports Ollama and OpenRouter Models](https://www.reddit.com)[](https://www.reddit.com/r/LocalLLaMA/comments/1jslnxb/github_copilot_now_supports_ollama_and_openrouter/)
- [Which AI model should I use with GitHub Copilot? - The GitHub Blog](https://github.blog)[](https://github.blog/ai-and-ml/github-copilot/which-ai-model-should-i-use-with-github-copilot/)
- [OpenAI GPT-4.1 is now generally available in GitHub Copilot - GitHub Changelog](https://github.blog)[](https://github.blog/changelog/2025-05-08-openai-gpt-4-1-is-now-generally-available-in-github-copilot-as-the-new-default-model/)
- [OpenRouter (free) Models Missing from Manage Models - GitHub Issues](https://github.com/microsoft/vscode-copilot-release/issues/10193)[](https://github.com/microsoft/vscode-copilot-release/issues/10193)

如果你遇到特定錯誤或需要進一步協助設定，請提供更多詳細資訊（例如錯誤訊息、VS Code 版本或訂閱類型），我可以進一步量身定制解決方案！