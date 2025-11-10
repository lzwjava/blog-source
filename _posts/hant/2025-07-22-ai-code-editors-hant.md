---
audio: false
generated: true
lang: hant
layout: post
title: 人工智能驅動的程式碼編輯工具
translated: true
type: note
---

### Visual Studio Code (VS Code) 與 GitHub Copilot
VS Code 透過 GitHub Copilot（一款 AI 擴充功能）強化功能，支援選取程式碼（例如函式）並使用 AI 進行修復、編輯或重構。主要功能包括：
- **行內聊天**：選取程式碼，按下 `Ctrl+I`（Windows/Linux）或 `Cmd+I`（Mac），輸入提示如「修復此錯誤」或「重構為使用 async/await」。Copilot 會直接在編輯器中建議修改。
- **修復錯誤**：針對編譯器錯誤（紅色波浪底線），懸停並選擇「使用 Copilot 修復」以取得 AI 產生的修復方案。
- **聊天視窗**：開啟 Copilot 聊天（`Ctrl+Alt+I`），選取程式碼，並要求解釋、編輯或生成測試。在代理模式下可處理多檔案編輯。
- **操作選單**：在選取的程式碼上按右鍵，選擇 AI 操作如解釋、重新命名或檢閱。

Copilot 有限制免費使用，或付費享有無限使用。

### Cursor AI 程式碼編輯器
Cursor 是一款以 AI 為優先的程式碼編輯器，衍生自 VS Code，專為 AI 輔助編輯設計。它在選取和修改程式碼方面表現卓越：
- **使用 Ctrl+K 編輯**：選取函式或程式碼區塊，按下 `Ctrl+K`（或 Mac 上的 `Cmd+K`），並描述變更（例如「優化此函式的效能」）。Cursor 會生成可預覽和應用的差異。
- **作曲者模式**：對於跨檔案的複雜編輯，使用作曲者介面提示多檔案變更、檢閱差異並迭代。
- **代理模式**：按下 `Ctrl+I`，指示更廣泛的任務（例如「修復此模組中的錯誤」），它會自主規劃、編輯和執行命令，同時保持您的參與。
- **下一步編輯建議**：AI 根據您的變更預測並建議後續編輯。

Cursor 基礎功能免費，高級模型需使用 Pro 方案。它無縫匯入 VS Code 擴充功能。

### IntelliJ IDEA 與 JetBrains AI Assistant
IntelliJ IDEA（及其他 JetBrains IDE）內建 AI Assistant 外掛，允許選取程式碼並使用 AI 進行修復或編輯：
- **AI 操作選單**：選取程式碼，按下 `Alt+Enter` 或右鍵點選，選擇「AI 操作」> 選項如「建議重構」、「尋找問題」或「使用 AI 修復」。它會分析上下文並在差異檢視器中建議變更。
- **行內提示**：直接在編輯器中輸入提示（例如「重構此函式」），按下 `Tab`，AI 會行內生成/編輯程式碼。
- **錯誤修復**：針對高亮顯示的錯誤，選擇「使用 AI 修復」以取得上下文感知建議。
- **程式碼生成/重構**：透過選單呼叫以解釋程式碼、添加型別註釋或重新生成部分程式碼。

AI Assistant 需要 JetBrains AI 授權（提供免費試用），並由 Mellum 等模型提供完成功能。

所有這些工具都深度整合了 AI，但 Cursor 最以 AI 為核心，VS Code/Copilot 靈活且廣泛使用，而 IntelliJ 的 AI 則專為企業/Java 重度工作流程量身定制。請根據您偏好的生態系統選擇。

參考資料：  
[GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)  
[Get started with GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/getting-started)  
[Features | Cursor - The AI Code Editor](https://cursor.com/en/features)  
[Cursor AI: A Guide With 10 Practical Examples](https://www.datacamp.com/tutorial/cursor-ai-code-editor)  
[Use AI in editor | IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/use-ai-in-editor.html)  
[AI Assistant in JetBrains IDEs | IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/ai-assistant-in-jetbrains-ides.html)  
[Use AI prompts to explain and refactor your code | IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/use-prompts-to-explain-and-refactor-your-code.html)