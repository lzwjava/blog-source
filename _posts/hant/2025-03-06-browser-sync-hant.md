---
audio: false
generated: true
lang: hant
layout: post
title: 使用 BrowserSync
translated: true
type: note
---

BrowserSync 是一款極佳的工具，能透過同步瀏覽器操作、自動重新載入檔案及提供本地開發伺服器，來簡化前端開發流程。以下是在您的前端工作流程中使用 BrowserSync 的逐步指南：

---

### 1. **安裝 Node.js 與 npm**
BrowserSync 是基於 Node.js 的工具，因此您需要先安裝 Node.js 與 npm（Node 套件管理器）。若尚未安裝：
- 請至 [nodejs.org](https://nodejs.org/) 下載並安裝。
- 驗證安裝是否成功：
  ```bash
  node -v
  npm -v
  ```

---

### 2. **安裝 BrowserSync**
您可以將 BrowserSync 全域安裝或本地安裝於專案中。

#### 選項 1：全域安裝
在終端機中執行以下指令，將 BrowserSync 全域安裝：
```bash
npm install -g browser-sync
```
此後您便可從任何位置使用 `browser-sync` 指令。

#### 選項 2：本地安裝（建議用於專案）
若希望將相依套件限制在特定專案內：
```bash
npm install browser-sync --save-dev
```
這會將 BrowserSync 加入專案的 `node_modules` 並列於 `package.json` 中。

---

### 3. **啟動 BrowserSync**
根據您的設定，可以多種方式使用 BrowserSync：

#### 基礎用法（靜態檔案）
若您正在處理靜態 HTML、CSS 與 JS 檔案，請導航至專案資料夾並執行：
```bash
browser-sync start --server --files "*.html, css/*.css, js/*.js"
```
- `--server`：啟動本地伺服器（從當前目錄提供檔案）。
- `--files`：監控這些檔案的變更並自動重新載入瀏覽器。

例如，若您的資料夾結構如下：
```
my-project/
├── index.html
├── css/
│   └── style.css
└── js/
    └── script.js
```
執行上述指令後會：
- 在 `http://localhost:3000`（預設連接埠）啟動伺服器。
- 開啟您的預設瀏覽器。
- 當 `index.html`、`style.css` 或 `script.js` 變更時重新載入頁面。

#### 代理模式（現有伺服器）
若您正在使用後端伺服器（例如 Node.js、PHP 或 Python），請使用代理選項：
```bash
browser-sync start --proxy "http://localhost:8000" --files "*.html, css/*.css, js/*.js"
```
- `--proxy`：將請求代理至您現有的伺服器（請將 `http://localhost:8000` 替換為您的伺服器 URL）。
- BrowserSync 將在此基礎上疊加其功能（如自動重新載入）。

---

### 4. **主要功能**
BrowserSync 運行後，您將獲得：
- **即時重新載入**：監控的檔案變更會立即觸發瀏覽器刷新。
- **跨裝置同步**：在所有連接的裝置（例如桌面電腦、手機、平板）間同步滾動、點擊及表單輸入。
- **UI 控制面板**：可透過 `http://localhost:3001`（預設）存取控制面板以調整設定或停止伺服器。

---

### 5. **與建置工具整合（選用）**
若您使用 Gulp 或 Webpack 等工具，BrowserSync 可無縫整合。

#### 以 Gulp 為例
安裝 Gulp 與 BrowserSync：
```bash
npm install --save-dev gulp browser-sync
```
建立 `gulpfile.js`：
```javascript
const gulp = require('gulp');
const browserSync = require('browser-sync').create();

gulp.task('serve', function() {
  browserSync.init({
    server: './', // 從當前目錄提供檔案
  });

  gulp.watch(['*.html', 'css/*.css', 'js/*.js']).on('change', browserSync.reload);
});

gulp.task('default', gulp.series('serve'));
```
執行：
```bash
gulp
```

---

### 6. **常用指令與選項**
- 變更連接埠：`--port 8080`
- 停用自動開啟：`--no-open`
- 監控特定檔案：`--files "path/to/files/*"`
- 完整清單：執行 `browser-sync --help`

---

### 7. **疑難排解**
- **連接埠被佔用**：使用 `--port <數字>` 變更連接埠。
- **未重新載入**：請確認 `--files` 中的檔案路徑與您的專案結構相符。
- **權限問題**：若為全域安裝，可能需要使用 `sudo`（例如在 Linux/macOS 上執行 `sudo npm install -g browser-sync`）。

---

就是這麼簡單！BrowserSync 現已準備好提升您的前端開發效率。從基礎指令開始，根據需求調整，享受更流暢的工作流程。若有任何特定設定需要協助，請隨時告知！