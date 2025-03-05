---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Chokidar 進行檔案監視
translated: true
---

Chokidar 是一個主要為伺服器端文件監視設計的 Node.js 庫，因此直接在前端（即瀏覽器環境）使用並不是其典型用例。瀏覽器沒有像 Node.js 那樣直接訪問文件系統的權限，這是為什麼 Chokidar 更適合後端或構建時環境。然而，如果你正在使用像 Webpack、Vite 或 Parcel 這樣的打包工具進行開發設置，或者你正在構建一個 Electron 應用程序（它將 Node.js 與前端結合），你可以間接利用 Chokidar。讓我根據上下文來解釋你可能會如何進行。

### 為什麼 Chokidar 無法直接在瀏覽器中運行
- Chokidar 依賴於 Node.js API 如 `fs`（文件系統）來監視文件，這些 API 在瀏覽器環境中不可用。
- 前端代碼在沙盒環境（瀏覽器）中運行，文件系統訪問受到限制，以確保安全。

### 在「前端」上下文中使用 Chokidar 的可能情況
以下是你可能在前端開發中使用 Chokidar 的方式：

#### 1. **在開發過程中使用構建工具**
如果你問的是在前端開發過程中使用 Chokidar 來監視文件（例如，用於熱重載或即時更新），你會將其整合到構建過程中，而不是瀏覽器運行時。

使用自定義 Node.js 腳本的範例：
```javascript
const chokidar = require('chokidar');

// 監視前端源文件的變化
chokidar.watch('./src/**/*.{html,js,css}').on('all', (event, path) => {
  console.log(event, path);
  // 觸發重新構建或通知前端開發伺服器
});
```
- **用例**：你可以將其與 WebSocket 連接配對，以在開發過程中將更新推送到瀏覽器。
- **工具**：將其與 `esbuild` 或開發伺服器（例如，Vite 已經內建了文件監視，但你可以使用 Chokidar 自定義它）結合使用。

#### 2. **在 Electron 應用中**
如果你的「前端」是 Electron 應用的一部分，你可以在主進程（Node.js）中使用 Chokidar，並將變更通知傳遞到渲染進程（前端）。

範例：
```javascript
// main.js (Electron 主進程)
const { ipcMain } = require('electron');
const chokidar = require('chokidar');

chokidar.watch('./files').on('change', (path) => {
  ipcMain.send('file-changed', path); // 將事件發送到渲染器
});
```
```javascript
// renderer.js (前端)
const { ipcRenderer } = require('electron');

ipcRenderer.on('file-changed', (event, path) => {
  console.log(`文件變更: ${path}`);
  // 相應地更新 UI
});
```

#### 3. **前端與後端代理**
如果你正在構建一個 Web 應用程序並希望具有文件監視功能，你可以在 Node.js 後端運行 Chokidar，並通過 WebSocket 或 Server-Sent Events 將更新發送到前端。

範例（使用 Express 和 WebSocket 的後端）：
```javascript
const express = require('express');
const WebSocket = require('ws');
const chokidar = require('chokidar');

const app = express();
const server = app.listen(3000);
const wss = new WebSocket.Server({ server });

chokidar.watch('./public').on('change', (path) => {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(`文件變更: ${path}`);
    }
  });
});
```
前端（React 範例）：
```javascript
const socket = new WebSocket('ws://localhost:3000');
socket.onmessage = (event) => {
  console.log(event.data); // "文件變更: ..."
  // 更新狀態或 UI
};
```

### 安裝
在任何這些設置中使用 Chokidar，你首先需要在 Node.js 專案中安裝它：
```bash
npm install chokidar
```

### Chokidar 的關鍵方法
- `chokidar.watch(path, [options])`：開始監視文件或目錄。
- 事件：`.on('add', callback)`、`.on('change', callback)`、`.on('unlink', callback)`、`.on('all', (event, path) => {})`。
- 選項：`{ ignored: /node_modules/, persistent: true }`（根據需要自定義）。

### 如果你指的是其他內容
如果你根本不使用 Node.js 環境，並且希望在瀏覽器中獲得類似文件監視的行為（例如，監視 `<input type="file">` 變化），請告訴我！這將涉及 `File` API 和事件監聽器，而不是 Chokidar。

你的具體設置或目標是什麼？我可以進一步針對這些內容進行調整！