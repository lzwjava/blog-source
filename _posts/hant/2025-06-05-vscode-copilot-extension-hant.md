---
audio: false
generated: true
lang: hant
layout: post
title: 如何從 VSCode 擴充功能呼叫 GitHub Copilot
translated: true
type: note
---

GitHub Copilot 是一個強大的 AI 編程助手，透過相應的外掛程式整合到 Visual Studio Code (VSCode) 和 IntelliJ IDEA 中。雖然沒有公開的 REST API 可直接呼叫 Copilot，但開發者可以在 VSCode 擴充功能中使用 VSCode Chat API、Language Model API 或基於指令的互動來程式化地使用其功能。本篇部落格文章將逐步講解如何建立一個 VSCode 擴充功能，用自訂提示觸發 Copilot 的聊天功能，有效模擬對 Copilot 的「API 呼叫」，並說明如何利用 Copilot 本身來簡化開發流程。

## 理解 Copilot 在 VSCode 中的整合方式

GitHub Copilot 並未提供傳統 API（例如 REST 端點）供直接程式化存取。相反地，其功能可透過以下方式使用：
- **VSCode Chat API**：讓擴充功能建立自訂聊天參與者，與 Copilot 的聊天系統互動以處理自然語言查詢。
- **VSCode Language Model API**：允許擴充功能存取 Copilot 的大型語言模型 (LLMs)，用於程式碼生成或分析等任務。
- **VSCode 指令**：允許觸發 Copilot 的內建功能，例如以預定義提示開啟聊天視窗。

本指南重點在於使用 `workbench.action.chat.open` 指令來觸發 Copilot 的聊天介面，因為這是將 Copilot 功能整合到擴充功能中最簡單的方法。

## 逐步指南：建立觸發 Copilot 聊天的 VSCode 擴充功能

以下是建立 VSCode 擴充功能的逐步指南，該擴充功能會以自訂提示開啟 Copilot 的聊天視窗，從而有效地「呼叫」Copilot 處理使用者定義的查詢。

### 1. 設定 VSCode 擴充功能

1. **建立專案骨架**：
   - 安裝 Yeoman VSCode 擴充功能生成器：`npm install -g yo generator-code`。
   - 執行 `yo code` 並選擇「New Extension (TypeScript)」來建立基於 TypeScript 的擴充功能。
   - 為擴充功能命名，例如 `copilot-api-caller`。

2. **設定 `package.json`**：
   - 定義一個指令來觸發 Copilot 的聊天功能。
   - `package.json` 範例：

```json
{
  "name": "copilot-api-caller",
  "displayName": "Copilot API Caller",
  "description": "Triggers GitHub Copilot Chat with a custom prompt",
  "version": "0.0.1",
  "engines": {
    "vscode": "^1.85.0"
  },
  "categories": ["Other"],
  "activationEvents": [
    "onCommand:copilot-api-caller.triggerCopilotChat"
  ],
  "main": "./out/extension.js",
  "contributes": {
    "commands": [
      {
        "command": "copilot-api-caller.triggerCopilotChat",
        "title": "Trigger Copilot Chat"
      }
    ]
  },
  "scripts": {
    "vscode:prepublish": "npm run compile",
    "compile": "tsc -p ./",
    "watch": "tsc -watch -p ./"
  },
  "devDependencies": {
    "@types/vscode": "^1.85.0",
    "@types/node": "^20.2.5",
    "typescript": "^5.1.3"
  }
}
```

   - **使用 Copilot**：在編輯 `package.json` 時，Copilot 可能會在你輸入時建議 `contributes.commands` 或 `activationEvents` 等欄位。使用 `Tab` 鍵接受這些建議以加速設定。

### 2. 編寫擴充功能程式碼

建立擴充功能邏輯，以註冊一個指令，該指令會以使用者提供的提示開啟 Copilot 的聊天功能。

- **檔案**：`src/extension.ts`
- **程式碼**：

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // 註冊指令以觸發 Copilot Chat
  let disposable = vscode.commands.registerCommand('copilot-api-caller.triggerCopilotChat', async () => {
    // 取得使用者輸入的提示
    const prompt = await vscode.window.showInputBox({
      prompt: 'Enter your query for GitHub Copilot',
      placeHolder: 'e.g., Write a JavaScript function to sort an array'
    });

    if (prompt) {
      try {
        // 執行指令以使用提示開啟 Copilot Chat
        await vscode.commands.executeCommand('workbench.action.chat.open', prompt);
        vscode.window.showInformationMessage('Sent prompt to Copilot Chat!');
      } catch (error) {
        vscode.window.showErrorMessage(`Failed to trigger Copilot Chat: ${error}`);
      }
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

- **運作方式**：
  - 註冊一個指令 `copilot-api-caller.triggerCopilotChat`。
  - 提示使用者輸入查詢（例如「Write a Python function to reverse a string」）。
  - 使用 `vscode.commands.executeCommand('workbench.action.chat.open', prompt)` 以提示開啟 Copilot 的聊天視窗。
- **使用 Copilot**：在 VSCode 中輸入 `import * as vscode`，Copilot 會建議完整的導入語句。加入註解如 `// Register a command to open Copilot Chat`，Copilot 可能會建議 `vscode.commands.registerCommand` 結構。對於指令執行，輸入 `// Open Copilot Chat with a prompt`，Copilot 可能會建議 `executeCommand` 呼叫。

### 3. 加入上下文以增強功能（可選）

為了使擴充功能更加強大，可以包含編輯器中的上下文，例如選取的程式碼，以提供 Copilot 更多資訊。

- **修改後的程式碼** (`src/extension.ts`)：

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  let disposable = vscode.commands.registerCommand('copilot-api-caller.triggerCopilotChat', async () => {
    // 從當前編輯器取得選取的文字
    const editor = vscode.window.activeTextEditor;
    let context = '';
    if (editor) {
      const selection = editor.selection;
      context = editor.document.getText(selection);
    }

    // 提示使用者輸入
    const prompt = await vscode.window.showInputBox({
      prompt: 'Enter your query for GitHub Copilot',
      placeHolder: 'e.g., Explain this code',
      value: context ? `Regarding this code: \n\`\`\`\n${context}\n\`\`\`\n` : ''
    });

    if (prompt) {
      try {
        await vscode.commands.executeCommand('workbench.action.chat.open', prompt);
        vscode.window.showInformationMessage('Sent prompt to Copilot Chat!');
      } catch (error) {
        vscode.window.showErrorMessage(`Failed to trigger Copilot Chat: ${error}`);
      }
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

- **運作方式**：
  - 從當前編輯器取得選取的文字，並將其作為上下文包含在提示中。
  - 在輸入框中預先填入選取的程式碼，並格式化為 Markdown 程式碼區塊。
  - 將組合後的提示傳送到 Copilot 的聊天介面。
- **使用 Copilot**：註解 `// Get selected text from editor`，Copilot 可能會建議 `vscode.window.activeTextEditor`。對於格式化，輸入 `// Format code as markdown`，Copilot 可能會建議三重反引號語法。

### 4. 測試擴充功能

1. 在 VSCode 中按 `F5` 啟動擴充功能開發主機。
2. 開啟指令選擇區 (`Ctrl+Shift+P` 或 `Cmd+Shift+P`) 並執行 `Trigger Copilot Chat`。
3. 輸入提示（例如「Generate a REST API client in TypeScript」）或選取程式碼並執行指令。
4. 確認 Copilot 的聊天視窗以你的提示開啟並提供回應。
5. **使用 Copilot**：如果發生錯誤，加入註解如 `// Handle errors for command execution`，Copilot 可能會建議 try-catch 區塊或錯誤訊息。

### 5. 進階：使用 VSCode Chat API

為了更精細的控制，可以使用 VSCode Chat API 建立自訂聊天參與者，該參與者與 Copilot 的語言模型整合，允許在擴充功能內進行自然語言處理。

- **範例程式碼** (`src/extension.ts`)：

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // 註冊聊天參與者
  const participant = vscode.chat.createChatParticipant('copilot-api-caller.myParticipant', async (request, context, stream, token) => {
    stream.markdown('Processing your query...\n');
    // 使用 Language Model API 生成回應
    const model = await vscode.lm.selectChatModels({ family: 'gpt-4' })[0];
    if (model) {
      const response = await model.sendRequest([{ text: request.prompt }], {}, token);
      for await (const chunk of response.stream) {
        stream.markdown(chunk);
      }
    } else {
      stream.markdown('No suitable model available.');
    }
  });

  participant.iconPath = new vscode.ThemeIcon('sparkle');
  context.subscriptions.push(participant);
}

export function deactivate() {}
```

- **運作方式**：
  - 建立一個聊天參與者 (`@copilot-api-caller.myParticipant`)，可在 Copilot Chat 視圖中呼叫。
  - 使用 Language Model API 存取 Copilot 的 `gpt-4` 模型（或其他可用模型）來處理提示。
  - 將回應串流回聊天視圖。
- **使用 Copilot**：註解 `// Create a chat participant for Copilot`，Copilot 可能會建議 `vscode.chat.createChatParticipant` 結構。對於 Language Model API，註解 `// Access Copilot’s LLM`，Copilot 可能會建議 `vscode.lm.selectChatModels`。

### 6. 封裝與部署

1. 安裝 `vsce`：`npm install -g @vscode/vsce`。
2. 執行 `vsce package` 以建立 `.vsix` 檔案。
3. 透過擴充功能視圖在 VSCode 中安裝擴充功能，或與他人分享 `.vsix` 檔案。
4. **使用 Copilot**：在 `package.json` 中加入註解如 `// Add script to package extension`，Copilot 可能會建議 `vscode:prepublish` 指令碼。

## 在開發過程中利用 Copilot

GitHub Copilot 可以顯著加速擴充功能開發：
- **程式碼建議**：當你在 `src/extension.ts` 中輸入時，Copilot 會建議導入語句、指令註冊和錯誤處理。例如，輸入 `vscode.commands.` 會提示如 `registerCommand` 的建議。
- **提示工程**：使用清晰的註解如 `// Trigger Copilot Chat with a user prompt` 來引導 Copilot 的建議。如果建議不準確，請優化註解。
- **除錯**：如果擴充功能失敗，加入註解如 `// Log error details`，Copilot 可能會建議 `console.log` 或 `vscode.window.showErrorMessage`。

## 限制

- **無直接 API 存取**：Copilot 未公開公共 REST API。VSCode Chat 和 Language Model API 是主要的程式化介面。
- **身份驗證**：使用者必須擁有有效的 Copilot 訂閱（免費或付費）並在 VSCode 中使用 GitHub 帳戶登入。
- **Chat API 範圍**：Chat API 僅限於聊天介面；無法程式化存取 Copilot 的程式碼補全引擎。
- **環境**：確保擴充功能符合任何有關自訂 VSCode 擴充功能的組織政策。

## 結論

透過使用 VSCode 的指令系統或 Chat API，開發者可以從自訂擴充功能中有效地「呼叫」GitHub Copilot，實現與其 AI 功能的程式化互動。上述範例展示了如何以自訂提示觸發 Copilot 的聊天功能，並透過編輯器上下文增強，為使用 Language Model API 進行更進階的整合提供了基礎。在 Copilot 的協助下，建立此類擴充功能變得更快速且更直觀。

為了進一步探索，可以嘗試使用 Chat API 建立自訂參與者，或整合更多編輯器上下文以獲得更豐富的提示。編程愉快！