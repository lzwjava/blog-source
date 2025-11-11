---
audio: false
generated: true
lang: hant
layout: post
title: 並行使用
translated: true
type: note
---

看來您是在詢問前端開發中使用 "concurrently" 的情境。不過，"concurrently" 通常是 Node.js 套件，用於同時執行多個指令或腳本，通常用於後端或開發工作流程，而非直接在前端程式碼中使用。您是指在前端專案設定中使用它（例如執行腳本），還是指其他概念，像是前端 JavaScript 中的並行操作（例如 promises、async/await）？我暫時假設是前者，但歡迎您進一步說明！

### 在前端專案中使用 `concurrently`

如果您正在開發前端專案（例如使用 React、Vue 或 Angular），`concurrently` 常用於開發過程中同時執行多個程序——例如啟動開發伺服器和建置監視工具。以下是使用方式：

#### 1. 安裝 `concurrently`
首先，將它安裝為專案的開發依賴項：
```bash
npm install --save-dev concurrently
```

#### 2. 在 `package.json` 中添加腳本
在 `package.json` 中定義您要同時執行的腳本。例如，如果您要執行前端開發伺服器和 CSS 預處理器（如 Sass）：
```json
{
  "scripts": {
    "start:frontend": "react-scripts start", // 或您的前端開發指令
    "watch:css": "sass --watch src/styles:dist/styles",
    "dev": "concurrently \"npm run start:frontend\" \"npm run watch:css\""
  }
}
```

- `start:frontend`：執行您的前端開發伺服器（例如 React、Vite 等）。
- `watch:css`：監視並編譯您的 CSS 檔案。
- `dev`：使用 `concurrently` 同時執行兩個指令。

#### 3. 執行並行腳本
在終端機中直接執行：
```bash
npm run dev
```
這將同時啟動前端伺服器和 CSS 監視工具。您會在同一個終端機中看到兩個程序的輸出，`concurrently` 會讓它們同時運行。

#### 4. 可選配置
您可以使用選項自訂 `concurrently`，例如：
- `--kill-others`：如果一個程序失敗，停止所有程序。
- `--names`：為每個程序加上標籤，使輸出更清晰。

在 `package.json` 中使用選項的範例：
```json
"dev": "concurrently --names \"Frontend,CSS\" --kill-others \"npm run start:frontend\" \"npm run watch:css\""
```
輸出可能如下：
```
[Frontend] 正在啟動前端伺服器...
[CSS] 正在監視 CSS 檔案...
```

#### 在前端工作流程中的使用案例
假設您正在開發一個 React 應用程式，並有一個獨立的 API 伺服器：
- 前端：`npm run start`（React 開發伺服器，端口 3000）。
- API：`npm run start:api`（例如 Node.js 伺服器，端口 5000）。
使用 `concurrently`，您可以同時執行兩者：
```json
"dev": "concurrently \"npm run start\" \"npm run start:api\""
```

### 如果您是指前端中的並行 JavaScript
如果您是詢問在前端程式碼中處理並行操作（例如同時呼叫多個 API），以下是使用 `Promise.all` 的簡易範例：
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
這會並行執行 API 呼叫，並等待兩者都完成。

### 如需進一步說明請告知！
如果您所說的 "concurrently in frontend" 是指其他內容——例如特定的函式庫、框架或使用情境——請告訴我，我會進一步調整回答！