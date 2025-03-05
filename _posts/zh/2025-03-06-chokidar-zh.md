---
audio: false
generated: true
lang: zh
layout: post
title: 使用 Chokidar 进行文件监控
translated: true
---

Chokidar 是一个主要为服务器端文件监视设计的 Node.js 库，因此直接在前端（即浏览器环境）使用它并不是其典型用例。浏览器没有像 Node.js 那样直接访问文件系统的能力，这也是为什么 Chokidar 更适合后端或构建时环境。然而，如果你正在使用 Webpack、Vite 或 Parcel 等打包工具进行开发设置，或者你正在构建一个 Electron 应用（它将 Node.js 与前端结合），你可以间接利用 Chokidar。让我根据上下文解释你可能的方法。

### 为什么 Chokidar 不能直接在浏览器中运行
- Chokidar 依赖于 Node.js API 如 `fs`（文件系统）来监视文件，这些 API 在浏览器环境中不可用。
- 前端代码在一个沙盒环境（浏览器）中运行，文件系统访问受到安全限制。

### 在“前端”上下文中使用 Chokidar 的可能场景
以下是你可能在前端开发中使用 Chokidar 的方式：

#### 1. **在开发过程中使用构建工具**
如果你在前端开发过程中使用 Chokidar 来监视文件（例如，用于热重载或实时更新），你会将其集成到构建过程中，而不是浏览器运行时。

示例（自定义 Node.js 脚本）：
```javascript
const chokidar = require('chokidar');

// 监视前端源文件的更改
chokidar.watch('./src/**/*.{html,js,css}').on('all', (event, path) => {
  console.log(event, path);
  // 在这里触发重新构建或通知前端开发服务器
});
```
- **用例**：你可以将其与 WebSocket 连接配对，在开发过程中将更新推送到浏览器。
- **工具**：将其与 `esbuild` 或开发服务器（例如，Vite 已经内置了文件监视，但你可以使用 Chokidar 进行自定义）结合使用。

#### 2. **在 Electron 应用中**
如果你的“前端”是 Electron 应用的一部分，你可以在主进程（Node.js）中使用 Chokidar，并将更改通知到渲染进程（前端）。

示例：
```javascript
// main.js (Electron 主进程)
const { ipcMain } = require('electron');
const chokidar = require('chokidar');

chokidar.watch('./files').on('change', (path) => {
  ipcMain.send('file-changed', path); // 将事件发送到渲染器
});
```
```javascript
// renderer.js (前端)
const { ipcRenderer } = require('electron');

ipcRenderer.on('file-changed', (event, path) => {
  console.log(`文件更改: ${path}`);
  // 相应地更新 UI
});
```

#### 3. **前端与后端代理**
如果你正在构建一个 Web 应用并希望具有文件监视功能，你可以在 Node.js 后端运行 Chokidar，并通过 WebSocket 或服务器发送事件（SSE）将更新发送到前端。

示例（带有 Express 和 WebSocket 的后端）：
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
      client.send(`文件更改: ${path}`);
    }
  });
});
```
前端（React 示例）：
```javascript
const socket = new WebSocket('ws://localhost:3000');
socket.onmessage = (event) => {
  console.log(event.data); // "文件更改: ..."
  // 更新状态或 UI
};
```

### 安装
在任何这些设置中使用 Chokidar，你首先需要在 Node.js 项目中安装它：
```bash
npm install chokidar
```

### 关键 Chokidar 方法
- `chokidar.watch(path, [options])`：开始监视文件或目录。
- 事件：`.on('add', callback)`，`.on('change', callback)`，`.on('unlink', callback)`，`.on('all', (event, path) => {})`。
- 选项：`{ ignored: /node_modules/, persistent: true }`（根据需要自定义）。

### 如果你指的是其他内容
如果你根本不使用 Node.js 环境，并且希望在浏览器中获得类似文件监视的行为（例如，监视 `<input type="file">` 更改），请告诉我！这将涉及 `File` API 和事件监听器，而不是 Chokidar。

你的具体设置或目标是什么？我可以进一步定制！