---
audio: false
generated: true
lang: hant
layout: post
title: 建立 VSCode 擴充功能
translated: true
type: note
---

建立 Visual Studio Code（VSCode）擴充功能是提升開發工作流程或貢獻社群的絕佳方式。以下是一份完整指南，協助您開始編寫 VSCode 外掛：

### 1. 前置準備
- **Node.js 與 npm**：請確保已安裝 Node.js 與 npm。您可從 [nodejs.org](https://nodejs.org/) 下載。
- **Yeoman 與 VSCode 擴充功能生成器**：使用 npm 全域安裝 Yeoman 與 VSCode 擴充功能生成器。

```bash
npm install -g yo generator-code
```

### 2. 設定開發環境
- **安裝 Visual Studio Code**：請確保已安裝 VSCode。您可從 [code.visualstudio.com](https://code.visualstudio.com/) 下載。

### 3. 生成新擴充功能
使用 Yeoman 生成器搭建擴充功能架構。開啟終端機並執行：

```bash
yo code
```

依照提示設定擴充功能。系統將詢問：
- 擴充功能類型（例如：新擴充功能、新色彩主題等）
- 擴充功能名稱
- 識別碼（例如 `my-extension`）
- 描述
- 是否初始化 git 儲存庫
- 選擇語言（TypeScript 或 JavaScript）
- 是否安裝必要依賴套件

### 4. 理解專案結構
新建立的擴充功能將包含以下結構：
- `.vscode/`：包含除錯用的啟動設定。
- `src/`：包含擴充功能的原始碼。
- `package.json`：擴充功能的清單檔案。
- `tsconfig.json`：TypeScript 設定檔案（若使用 TypeScript）。

### 5. 編寫擴充功能
- **啟動時機**：在 `package.json` 的 `activationEvents` 欄位中定義擴充功能的啟動時機。
- **貢獻點**：在 `package.json` 的 `contributes` 區段定義擴充功能對 VSCode 的貢獻內容，例如指令、視圖或語言支援。

### 6. 實作指令
建立可供使用者呼叫的指令。在 `package.json` 中定義指令，並在主擴充功能檔案（例如 `src/extension.ts` 或 `src/extension.js`）中實作。

在 `package.json` 中定義指令的範例：

```json
"contributes": {
    "commands": [
        {
            "command": "extension.sayHello",
            "title": "Say Hello"
        }
    ]
}
```

在 `src/extension.ts` 中實作指令：

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('extension.sayHello', () => {
        vscode.window.showInformationMessage('Hello, World!');
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
```

### 7. 除錯擴充功能
- 按下 `F5` 鍵開啟載入擴充功能的新 VSCode 視窗。
- 設定中斷點並使用除錯主控台測試擴充功能。

### 8. 封裝與發佈
- **封裝擴充功能**：使用 `vsce` 工具封裝擴充功能。

```bash
npm install -g vsce
vsce package
```

- **發佈至市集**：請遵循 [VSCode 市集](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) 的指示發佈擴充功能。

### 9. 文件與最佳實踐
- **文件**：在 `README.md` 檔案中為擴充功能提供清晰說明文件。
- **測試**：編寫測試以確保擴充功能正常運作。
- **版本管理**：遵循語意化版本規範進行擴充功能發佈。

### 10. 補充資源
- **VSCode API 文件**：[vscode-api](https://code.visualstudio.com/api)
- **擴充功能範例**：[vscode-extension-samples](https://github.com/microsoft/vscode-extension-samples)

遵循這些步驟，您將能順利建立實用且功能完善的 VSCode 擴充功能。編程愉快！