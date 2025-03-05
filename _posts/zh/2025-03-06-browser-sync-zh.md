---
audio: false
generated: true
lang: zh
layout: post
title: 使用 BrowserSync
translated: true
---

BrowserSync 是一个非常棒的工具，可以通过同步浏览器操作、自动重新加载文件和提供本地开发服务器来简化前端开发。以下是如何在前端工作流中使用 BrowserSync 的分步指南：

---

### 1. **安装 Node.js 和 npm**
BrowserSync 是一个 Node.js 工具，因此你需要安装 Node.js 和 npm（Node 包管理器）。如果你还没有安装：
- 从 [nodejs.org](https://nodejs.org/) 下载并安装。
- 验证安装：
  ```bash
  node -v
  npm -v
  ```

---

### 2. **安装 BrowserSync**
你可以全局或在项目中本地安装 BrowserSync。

#### 选项 1：全局安装
在终端中运行以下命令以全局安装 BrowserSync：
```bash
npm install -g browser-sync
```
这将允许你从任何地方使用 `browser-sync` 命令。

#### 选项 2：本地安装（推荐用于项目）
如果你希望将依赖项绑定到特定项目：
```bash
npm install browser-sync --save-dev
```
这将 BrowserSync 添加到项目的 `node_modules` 并列在 `package.json` 中。

---

### 3. **启动 BrowserSync**
根据你的设置，你可以以不同的方式使用 BrowserSync：

#### 基本用法（静态文件）
如果你使用静态的 HTML、CSS 和 JS 文件，导航到你的项目文件夹并运行：
```bash
browser-sync start --server --files "*.html, css/*.css, js/*.js"
```
- `--server`：运行本地服务器（从当前目录提供文件）。
- `--files`：监视这些文件的更改并自动重新加载浏览器。

例如，如果你的文件夹结构是：
```
my-project/
├── index.html
├── css/
│   └── style.css
└── js/
    └── script.js
```
运行上述命令将：
- 在 `http://localhost:3000`（默认端口）启动服务器。
- 打开你的默认浏览器。
- 当 `index.html`、`style.css` 或 `script.js` 发生变化时重新加载页面。

#### 代理模式（现有服务器）
如果你使用后端服务器（例如 Node.js、PHP 或 Python），使用代理选项：
```bash
browser-sync start --proxy "http://localhost:8000" --files "*.html, css/*.css, js/*.js"
```
- `--proxy`：将请求代理到你的现有服务器（将 `http://localhost:8000` 替换为你的服务器的 URL）。
- BrowserSync 将其功能（如自动重新加载）覆盖在顶部。

---

### 4. **关键功能**
一旦 BrowserSync 运行，你将获得：
- **实时重新加载**：监视文件的更改会触发浏览器的即时刷新。
- **跨设备同步**：滚动、点击和表单输入在所有连接的设备（例如桌面、手机、平板）之间同步。
- **UI 仪表盘**：在 `http://localhost:3001`（默认）访问控制面板以调整设置或停止服务器。

---

### 5. **与构建工具集成（可选）**
如果你使用 Gulp 或 Webpack 等工具，BrowserSync 可以无缝集成。

#### 与 Gulp 的示例
安装 Gulp 和 BrowserSync：
```bash
npm install --save-dev gulp browser-sync
```
创建一个 `gulpfile.js`：
```javascript
const gulp = require('gulp');
const browserSync = require('browser-sync').create();

gulp.task('serve', function() {
  browserSync.init({
    server: './', // 从当前目录提供文件
  });

  gulp.watch(['*.html', 'css/*.css', 'js/*.js']).on('change', browserSync.reload);
});

gulp.task('default', gulp.series('serve'));
```
运行它：
```bash
gulp
```

---

### 6. **常用命令和选项**
- 更改端口：`--port 8080`
- 禁用自动打开：`--no-open`
- 监视特定文件：`--files "path/to/files/*"`
- 完整列表：运行 `browser-sync --help`

---

### 7. **故障排除**
- **端口被占用**：使用 `--port <number>` 更改端口。
- **无重新加载**：确保 `--files` 中的文件路径与项目结构匹配。
- **权限**：如果全局安装，你可能需要 `sudo`（例如，在 Linux/macOS 上 `sudo npm install -g browser-sync`）。

---

这就是了！BrowserSync 现在已经准备好为你的前端开发提供动力。从基本命令开始，根据需要进行调整，享受更流畅的工作流程。如果你需要帮助进行特定设置，请告诉我！