---
audio: false
generated: true
lang: hant
layout: post
title: 使用 BrowserSync
translated: true
---

BrowserSync 是一個非常棒的工具，能夠通過同步瀏覽器操作、自動重新加載文件和提供本地開發伺服器來簡化前端開發。以下是如何在前端工作流程中使用 BrowserSync 的分步指南：

---

### 1. **安裝 Node.js 和 npm**
BrowserSync 是一個 Node.js 工具，因此你需要安裝 Node.js 和 npm（Node Package Manager）。如果你還沒有安裝：
- 從 [nodejs.org](https://nodejs.org/) 下載並安裝。
- 驗證安裝：
  ```bash
  node -v
  npm -v
  ```

---

### 2. **安裝 BrowserSync**
你可以全局或在專案中本地安裝 BrowserSync。

#### 選項 1：全局安裝
在終端中運行以下命令以全局安裝 BrowserSync：
```bash
npm install -g browser-sync
```
這樣你就可以從任何地方使用 `browser-sync` 命令。

#### 選項 2：本地安裝（專案推薦）
如果你希望將依賴項綁定到特定專案：
```bash
npm install browser-sync --save-dev
```
這將 BrowserSync 添加到你的專案的 `node_modules` 並列在 `package.json` 中。

---

### 3. **啟動 BrowserSync**
根據你的設置，你可以以不同的方式使用 BrowserSync：

#### 基本使用（靜態文件）
如果你正在使用靜態 HTML、CSS 和 JS 文件，導航到你的專案文件夾並運行：
```bash
browser-sync start --server --files "*.html, css/*.css, js/*.js"
```
- `--server`：運行本地伺服器（從當前目錄提供文件）。
- `--files`：監視這些文件的變化並自動重新加載瀏覽器。

例如，如果你的文件夾結構是：
```
my-project/
├── index.html
├── css/
│   └── style.css
└── js/
    └── script.js
```
運行上述命令將：
- 在 `http://localhost:3000`（默認端口）啟動伺服器。
- 打開你的默認瀏覽器。
- 當 `index.html`、`style.css` 或 `script.js` 發生變化時重新加載頁面。

#### 代理模式（現有伺服器）
如果你使用後端伺服器（例如 Node.js、PHP 或 Python），使用代理選項：
```bash
browser-sync start --proxy "http://localhost:8000" --files "*.html, css/*.css, js/*.js"
```
- `--proxy`：將請求代理到你的現有伺服器（用你的伺服器的 URL 替換 `http://localhost:8000`）。
- BrowserSync 將其功能（如自動重新加載）覆蓋在上面。

---

### 4. **主要功能**
一旦 BrowserSync 運行，你將獲得：
- **即時重新加載**：監視文件的變化會觸發瀏覽器的即時刷新。
- **跨設備同步**：滾動、點擊和表單輸入在所有連接的設備（例如桌面、手機、平板）之間同步。
- **UI 控制面板**：在 `http://localhost:3001`（默認）訪問控制面板以調整設置或停止伺服器。

---

### 5. **與構建工具集成（可選）**
如果你使用像 Gulp 或 Webpack 這樣的工具，BrowserSync 可以無縫集成。

#### 使用 Gulp 的示例
安裝 Gulp 和 BrowserSync：
```bash
npm install --save-dev gulp browser-sync
```
創建一個 `gulpfile.js`：
```javascript
const gulp = require('gulp');
const browserSync = require('browser-sync').create();

gulp.task('serve', function() {
  browserSync.init({
    server: './', // 從當前目錄提供文件
  });

  gulp.watch(['*.html', 'css/*.css', 'js/*.js']).on('change', browserSync.reload);
});

gulp.task('default', gulp.series('serve'));
```
運行它：
```bash
gulp
```

---

### 6. **常見命令和選項**
- 更改端口：`--port 8080`
- 禁用自動打開：`--no-open`
- 監視特定文件：`--files "path/to/files/*"`
- 完整列表：運行 `browser-sync --help`

---

### 7. **故障排除**
- **端口已使用**：使用 `--port <number>` 更改端口。
- **無重新加載**：確保 `--files` 中的文件路徑與你的專案結構匹配。
- **權限**：如果全局安裝，你可能需要 `sudo`（例如在 Linux/macOS 上 `sudo npm install -g browser-sync`）。

---

就這樣！BrowserSync 現在已經準備好為你的前端開發提速。從基本命令開始，根據需要進行調整，享受更流暢的工作流程。如果你需要幫助進行特定設置，請告訴我！