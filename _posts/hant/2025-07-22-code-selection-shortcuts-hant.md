---
audio: false
generated: true
lang: hant
layout: post
title: 快速代碼選擇與AI編輯
translated: true
type: note
---

以下概述如何在 **Visual Studio Code (VS Code)**、**Cursor** 和 **IntelliJ IDEA** 中使用快捷鍵快速選取函數或方法，接著利用它們的 AI 功能來修復或編輯所選程式碼。

### Visual Studio Code (VS Code)
VS Code 沒有直接快捷鍵可在游標位於函數/方法內時選取整個函數/方法，但您可以使用以下方法：
- **擴展選取範圍**：按下 `Ctrl+Shift+.` (Windows/Linux) 或 `Cmd+Shift+.` (Mac) 以擴展選取範圍。重複按下可選取封閉區塊（例如：函數主體，然後是整個函數）。這在 JavaScript、Python 等語言中效果良好。
- **智慧選取**：使用 `Ctrl+Shift+向右箭頭` (Windows/Linux) 或 `Cmd+Shift+向右箭頭` (Mac) 根據語法擴展選取範圍（可能需要多次按鍵以捕捉整個函數）。
- **擴充功能：Select By**：安裝 "Select By" 擴充功能並設定按鍵綁定（例如 `Ctrl+K, Ctrl+S`），以根據語言特定模式選取封閉的函數/方法。

**使用 GitHub Copilot 進行 AI 編輯**：
- 選取函數後，按下 `Ctrl+I` (Windows/Linux) 或 `Cmd+I` (Mac) 開啟 Copilot 的內嵌聊天。輸入提示，例如「修復此函數中的錯誤」或「重構為使用箭頭函數」。
- 或者，在選取範圍上按右鍵，選擇「Copilot > 修復」或「Copilot > 重構」以取得 AI 建議。
- 在 Copilot Chat 視圖 (`Ctrl+Alt+I`) 中，貼上所選程式碼並要求編輯（例如「優化此函數」）。

### Cursor AI 程式碼編輯器
Cursor 基於 VS Code 構建，增強了選取和 AI 整合功能：
- **選取封閉區塊**：按下 `Ctrl+Shift+.` (Windows/Linux) 或 `Cmd+Shift+.` (Mac) 以擴展選取範圍至封閉的函數/方法，類似於 VS Code。Cursor 的語言模型感知通常使這在 Python 或 TypeScript 等語言中更為精確。
- **自訂按鍵綁定**：您可以在 `settings.json` 中設定自訂按鍵綁定（例如 `editor.action.selectToBracket`）以直接選取函數範圍。

**在 Cursor 中進行 AI 編輯**：
- 選取函數後，按下 `Ctrl+K` (Windows/Linux) 或 `Cmd+K` (Mac)，然後描述變更（例如「為此函數新增錯誤處理」）。Cursor 會顯示 AI 生成編輯的差異預覽。
- 使用 `Ctrl+I` 進入 Agent Mode，以自主修復或優化跨檔案的函數，並提供迭代回饋。
- Composer Mode（可透過 UI 存取）允許在函數影響程式碼庫其他部分時進行多檔案編輯。

### IntelliJ IDEA
IntelliJ IDEA 提供強大的快捷鍵來選取函數/方法：
- **選取程式碼區塊**：當游標位於方法內時，按下 `Ctrl+W` (Windows/Linux) 或 `Cmd+W` (Mac) 以逐步選取封閉區塊。重複按下可擴展至整個方法（包括簽章）。這在 Java、Kotlin、Python 等語言中均適用。
- **縮小選取範圍**：使用 `Ctrl+Shift+W` (Windows/Linux) 或 `Cmd+Shift+W` (Mac) 在選取過度時縮小選取範圍。
- **結構感知選取**：按下 `Ctrl+Alt+Shift+向上箭頭` (Windows/Linux) 或 `Cmd+Option+Shift+向上箭頭` (Mac) 透過結構樹直接選取封閉方法。

**使用 JetBrains AI Assistant 進行 AI 編輯**：
- 選取方法後，按下 `Alt+Enter` 或按右鍵並選擇「AI Actions > 使用 AI 修復」或「建議重構」。AI Assistant 會在差異檢視器中提供情境感知建議。
- 使用內嵌提示（輸入 `/` 後跟您的請求，例如 `/refactor to use streams`，然後按下 `Tab`）直接編輯所選方法。
- 開啟 AI Assistant 工具視窗以描述複雜變更（例如「為此方法新增日誌記錄」）並套用生成的程式碼。

### 總結
- **VS Code**：使用 `Ctrl+Shift+.` 擴展選取範圍，然後使用 `Ctrl+I` 進行 Copilot AI 編輯。
- **Cursor**：相同的選取快捷鍵 (`Ctrl+Shift+.`)，並使用 `Ctrl+K` 進行精確的 AI 驅動編輯。
- **IntelliJ IDEA**：使用 `Ctrl+W` 快速選取方法，然後使用 `Alt+Enter` 進行 AI Assistant 修復。

IntelliJ 具有最精確的內建快捷鍵來選取方法 (`Ctrl+W`)，而 Cursor 的 AI 整合在編輯所選程式碼方面最為無縫。VS Code 靈活，但可能需要擴充功能以實現更快的函數選取。

參考資料：  
[Visual Studio Code 中的程式碼導覽](https://code.visualstudio.com/docs/editor/editingevolved)  
[Cursor AI：包含 10 個實用範例的指南](https://www.datacamp.com/tutorial/cursor-ai-code-editor)  
[IntelliJ IDEA 中的程式碼編輯](https://www.jetbrains.com/help/idea/working-with-source-code.html)  
[在編輯器中使用 AI | IntelliJ IDEA 文件](https://www.jetbrains.com/help/idea/use-ai-in-editor.html)