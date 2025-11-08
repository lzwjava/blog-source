---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GitHub Copilot 自訂聊天模式
translated: true
type: note
---

### 什麼是 chatmode.md？

在 Visual Studio Code（VS Code）的 GitHub Copilot 擴充功能中，`chatmode.md` 檔案用於定義**自訂聊天模式**。這些模式可讓你配置 Copilot Chat，使其針對特定任務（如規劃、安全審查或程式碼實作）採用特定角色或行為。每個模式可指定指令、可用工具（例如搜尋、擷取或 GitHub 儲存庫存取），甚至使用的 AI 模型。此功能在 VS Code 1.101 中處於預覽狀態，有助於調整回應以確保工作流程的一致性。

自訂模式以 Markdown 檔案形式儲存，副檔名為 `.chatmode.md`，可存放在工作區（供團隊共享）或使用者設定檔（供個人重複使用）。

### 為何使用自訂聊天模式？
- **客製化回應**：強制執行指南，例如生成計劃而不編輯程式碼。
- **工具控制**：在規劃時限制工具為唯讀，或在實作時啟用編輯功能。
- **效率提升**：重複使用常見角色（如架構師、審查員）的設定。

### 如何建立 chatmode.md 檔案

1. 在 VS Code 中開啟**聊天視圖**：
   - 點擊標題列中的 Copilot Chat 圖示，或使用 `Ctrl+Alt+I`（Windows/Linux） / `Cmd+Option+I`（macOS）。

2. 在聊天視圖中，點擊**配置聊天 > 模式**，然後選擇**建立新的自訂聊天模式檔案**。或者，開啟命令選擇區（`Ctrl+Shift+P` / `Cmd+Shift+P`）並執行**Chat: New Mode File**。

3. 選擇儲存位置：
   - **工作區**：預設儲存至 `.github/chatmodes/`（可與團隊共享）。可透過 `chat.modeFilesLocations` 設定自訂資料夾。
   - **使用者設定檔**：儲存至你的設定檔資料夾，以便跨裝置同步。

4. 為檔案命名（例如 `planning.chatmode.md`）並在 VS Code 中編輯。

若要管理現有模式，請使用**配置聊天 > 模式**或**Chat: Configure Chat Modes** 指令。

### 檔案結構與語法

`.chatmode.md` 檔案使用 Markdown，並可選擇性地包含 YAML frontmatter 作為元資料。以下是基本結構：

- **YAML Frontmatter**（以 `---` 行包圍，可選）：
  - `description`：在聊天輸入框的佔位符和下拉懸停提示中顯示的簡短文字。
  - `tools`：工具名稱陣列（例如 `['fetch', 'search']`）。可使用內建工具（如 `githubRepo`）或擴充功能工具；透過**配置工具**進行設定。
  - `model`：AI 模型（例如 `"Claude Sonnet 4"`）。預設為你選擇的模型。

- **正文**：用於 AI 的 Markdown 指令，包括提示、指南或外部檔案連結。

工具優先級：提示檔案 > 參考模式 > 預設模式工具。

### chatmode.md 檔案範例

以下建立一個「規劃」模式，用於生成實作計劃而不進行程式碼變更：

```
---
description: 為新功能或重構現有程式碼生成實作計劃。
tools: ['fetch', 'githubRepo', 'search', 'usages']
model: Claude Sonnet 4
---
# 規劃模式指令

你處於規劃模式。你的任務是為新功能或重構現有程式碼生成實作計劃。請勿進行任何程式碼編輯——僅生成計劃。

計劃包含以下部分的 Markdown 文件：

* **概述**：功能或重構的簡要描述。
* **需求**：需求列表。
* **實作步驟**：詳細的實作步驟。
* **測試**：用於驗證的測試列表。
```

儲存檔案後，它將出現在聊天模式下拉選單中。

### 如何使用自訂聊天模式

1. 開啟**聊天視圖**（如上所述）。

2. 在聊天視圖頂部的下拉選單中（模式選擇器旁邊），選擇你的自訂模式（例如「規劃」）。

3. 模式的 `description` 將作為佔位符顯示在輸入框中。輸入你的提示（例如「規劃用戶認證功能」）。

4. Copilot 將根據模式的指令和工具進行回應。可隨時透過下拉選單切換模式——內建模式（詢問、編輯、代理）仍可用。

更多範例可查看 [Awesome Copilot 儲存庫](https://github.com/github/awesome-copilot/tree/main)中的社群貢獻。

### 參考資料
- [VS Code 中的自訂聊天模式](https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes)
- [開始使用 VS Code 中的聊天功能](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)