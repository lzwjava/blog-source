---
audio: false
generated: true
lang: hant
layout: post
title: 並行使用
translated: true
---

看來你是在問如何在前端開發中使用「concurrently」。然而，「concurrently」通常是一個用來同時運行多個命令或腳本的 Node.js 套件，通常在後端或開發工作流程的上下文中使用，而不是直接在前端代碼中。你是否指的是如何在前端項目設置中使用它（例如運行腳本），還是指其他東西，例如前端 JavaScript 中的並發操作（例如承諾、async/await）？我現在假設前者，但你可以隨時澄清！

### 在前端項目中使用 `concurrently`

如果你正在進行前端項目（例如使用 React、Vue 或 Angular），`concurrently` 通常用於開發中同時運行多個過程——例如啟動開發伺服器和構建監視器。以下是如何使用它的方法：

#### 1. 安裝 `concurrently`
首先，將其作為開發依賴項安裝到你的項目中：
```bash
npm install --save-dev concurrently
```

#### 2. 將腳本添加到 `package.json`
在 `package.json` 中定義你想要同時運行的腳本。例如，如果你正在運行前端開發伺服器和 CSS 預處理器（例如 Sass）：
```json
{
  "scripts": {
    "start:frontend": "react-scripts start", // 或你的前端開發命令
    "watch:css": "sass --watch src/styles:dist/styles",
    "dev": "concurrently \"npm run start:frontend\" \"npm run watch:css\""
  }
}
```

- `start:frontend`：運行你的前端開發伺服器（例如 React、Vite 等）。
- `watch:css`：監視並編譯你的 CSS 文件。
- `dev`：使用 `concurrently` 同時運行這兩個命令。

#### 3. 運行並發腳本
在你的終端中，只需運行：
```bash
npm run dev
```
這將同時啟動前端伺服器和 CSS 監視器。你將在同一個終端中看到兩個過程的輸出，`concurrently` 會讓它們一起運行。

#### 4. 可選配置
你可以使用選項自定義 `concurrently`，例如：
- `--kill-others`：如果一個過程失敗，則停止所有過程。
- `--names`：為每個過程標籤以便更清晰的輸出。

在 `package.json` 中使用選項的示例：
```json
"dev": "concurrently --names \"Frontend,CSS\" --kill-others \"npm run start:frontend\" \"npm run watch:css\""
```
輸出可能如下：
```
[Frontend] 正在啟動前端伺服器...
[CSS] 正在監視 CSS 文件...
```

#### 前端工作流程中的使用案例
假設你正在構建一個具有單獨 API 伺服器的 React 應用程序：
- 前端：`npm run start`（React 開發伺服器在端口 3000 上）。
- API：`npm run start:api`（例如 Node.js 伺服器在端口 5000 上）。
使用 `concurrently`，你可以運行兩者：
```json
"dev": "concurrently \"npm run start\" \"npm run start:api\""
```

### 如果你指的是前端中的並發 JavaScript
如果你問的是如何在前端代碼中處理並發操作（例如同時獲取多個 API），這裡有一個使用 `Promise.all` 的快速示例：
```javascript
async function fetchData() {
  const [userData, postsData] = await Promise.all([
    fetch('https://api.example.com/user').then(res => res.json()),
    fetch('https://api.example.com/posts').then(res => res.json())
  ]);
  console.log(userData, postsData);
}
fetchData();
```
這將同時運行 API 請求並等待兩者解決。

### 如果需要澄清！
請告訴我你是否指的是其他東西，例如特定的庫、框架或用例，我將進一步調整答案！