---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Chokidar 進行檔案監控
translated: true
type: note
---

Chokidar 是一個主要為伺服器端檔案監視而設計的 Node.js 函式庫，因此直接在前端（即瀏覽器環境）使用並非其典型應用場景。瀏覽器不像 Node.js 那樣直接存取檔案系統，這就是為什麼 Chokidar 更適合後端或建置時環境。不過，如果您在開發環境中使用像 Webpack、Vite 或 Parcel 這樣的打包工具，或者正在建構 Electron 應用程式（結合了 Node.js 與前端），您可以間接利用 Chokidar。讓我根據具體情境說明可能的實現方式。

### 為什麼 Chokidar 無法直接在瀏覽器中運行
- Chokidar 依賴 Node.js 的 `fs`（檔案系統）等 API 來監視檔案，這些 API 在瀏覽器環境中不可用。
- 前端程式碼在沙盒環境（瀏覽器）中運行，出於安全原因，檔案系統存取受到限制。

### 在「前端」情境中使用 Chokidar 的可能場景
以下是如何在與前端開發相關的情境中使用 Chokidar：

#### 1. **在開發階段使用建置工具**
如果您想在開發前端時使用 Chokidar 監視檔案（例如用於熱重載或即時更新），應將其整合到建置流程中，而非瀏覽器運行時。

自訂 Node.js 腳本範例：
```javascript
const chokidar = require('chokidar');

// 監視前端原始碼檔案的變更
chokidar.watch('./src/**/*.{html,js,css}').on('all', (event, path) => {
  console.log(event, path);
  // 在此觸發重建或通知前端開發伺服器
});
```
- **應用場景**：可搭配 WebSocket 連線，在開發期間將更新推送至瀏覽器。
- **工具**：可結合 `esbuild` 或開發伺服器（例如 Vite 已內建檔案監視功能，但您也能用 Chokidar 自訂）。

#### 2. **在 Electron 應用程式中**
如果您的「前端」是 Electron 應用程式的一部分，可以在主進程（Node.js）中使用 Chokidar，並將變更通知轉發至渲染進程（前端）。

範例：
```javascript
// main.js (Electron 主進程)
const { ipcMain } = require('electron');
const chokidar = require('chokidar');

chokidar.watch('./files').on('change', (path) => {
  ipcMain.send('file-changed', path); // 傳送事件至渲染進程
});
```
```javascript
// renderer.js (前端)
const { ipcRenderer } = require('electron');

ipcRenderer.on('file-changed', (event, path) => {
  console.log(`檔案已變更：${path}`);
  // 據此更新 UI
});
```

#### 3. **搭配後端代理的前端**
如果您正在建置網頁應用程式並需要檔案監視功能，應在 Node.js 後端運行 Chokidar，並透過 WebSockets 或 Server-Sent Events 將更新傳送至前端。

範例（使用 Express 與 WebSocket 的後端）：
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
      client.send(`檔案已變更：${path}`);
    }
  });
});
```
前端（React 範例）：
```javascript
const socket = new WebSocket('ws://localhost:3000');
socket.onmessage = (event) => {
  console.log(event.data); // "檔案已變更：..."
  // 更新狀態或 UI
};
```

### 安裝方式
若要在上述任何設定中使用 Chokidar，請先在 Node.js 專案中安裝：
```bash
npm install chokidar
```

### 關鍵 Chokidar 方法
- `chokidar.watch(path, [options])`：開始監視檔案或目錄。
- 事件：`.on('add', callback)`、`.on('change', callback)`、`.on('unlink', callback)`、`.on('all', (event, path) => {})`。
- 選項：`{ ignored: /node_modules/, persistent: true }`（可根據需求自訂）。

### 其他可能性
如果您完全未使用 Node.js 環境，而是想在純瀏覽器環境中實現類似的檔案監視行為（例如監視 `<input type="file">` 的變更），請告知！這將涉及 `File` API 和事件監聽器，而非 Chokidar。

您的具體設定或目標是什麼？我可以提供更進一步的客製化說明！