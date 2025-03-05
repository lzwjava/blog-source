---
audio: false
generated: true
lang: zh
layout: post
title: 并发使用
translated: true
---

看起来你是在问如何在前端开发中使用 "concurrently"。然而，"concurrently" 通常是一个用于同时运行多个命令或脚本的 Node.js 包，通常在后端或开发工作流程的上下文中使用，而不是直接在前端代码中使用。你是指在前端项目设置中如何使用它（例如，运行脚本），还是指前端 JavaScript 中的并发操作（例如，promises、async/await）？我暂时假设是前者，但你可以随时澄清！

### 在前端项目中使用 `concurrently`

如果你正在进行前端项目（例如，使用 React、Vue 或 Angular），`concurrently` 通常在开发中用于同时运行多个进程——例如启动开发服务器和构建监视器。以下是如何使用它的方法：

#### 1. 安装 `concurrently`
首先，将其作为开发依赖项安装到你的项目中：
```bash
npm install --save-dev concurrently
```

#### 2. 向 `package.json` 添加脚本
在 `package.json` 中定义你想要并发运行的脚本。例如，如果你正在运行前端开发服务器和 CSS 预处理器（如 Sass）：
```json
{
  "scripts": {
    "start:frontend": "react-scripts start", // 或你的前端开发命令
    "watch:css": "sass --watch src/styles:dist/styles",
    "dev": "concurrently \"npm run start:frontend\" \"npm run watch:css\""
  }
}
```

- `start:frontend`：运行你的前端开发服务器（例如，React、Vite 等）。
- `watch:css`：监视并编译你的 CSS 文件。
- `dev`：使用 `concurrently` 同时运行这两个命令。

#### 3. 运行并发脚本
在你的终端中，只需运行：
```bash
npm run dev
```
这将同时启动前端服务器和 CSS 监视器。你将在同一个终端中看到两个进程的输出，`concurrently` 会将它们一起运行。

#### 4. 可选配置
你可以使用选项自定义 `concurrently`，例如：
- `--kill-others`：如果一个进程失败，停止所有进程。
- `--names`：为每个进程标记以便更清晰的输出。

在 `package.json` 中使用选项的示例：
```json
"dev": "concurrently --names \"Frontend,CSS\" --kill-others \"npm run start:frontend\" \"npm run watch:css\""
```
输出可能如下：
```
[Frontend] 启动前端服务器...
[CSS] 监视 CSS 文件...
```

#### 前端工作流中的用例
假设你正在构建一个带有单独 API 服务器的 React 应用：
- 前端：`npm run start`（React 开发服务器在端口 3000 上）。
- API：`npm run start:api`（例如，Node.js 服务器在端口 5000 上）。
使用 `concurrently`，你可以运行两者：
```json
"dev": "concurrently \"npm run start\" \"npm run start:api\""
```

### 如果你指的是前端中的并发 JavaScript
如果你问的是如何在前端代码中处理并发操作（例如，同时获取多个 API），以下是使用 `Promise.all` 的快速示例：
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
这将并发运行 API 调用并等待两者都解析。

### 如果需要澄清！
告诉我你是否指的是其他内容，例如特定的库、框架或用例，我将进一步定制答案！