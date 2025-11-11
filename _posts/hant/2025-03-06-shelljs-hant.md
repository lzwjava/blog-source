---
audio: false
generated: true
lang: hant
layout: post
title: 使用 ShellJS 執行 Shell 指令
translated: true
type: note
---

ShellJS 是一個 JavaScript 程式庫，提供 Unix shell 指令（如 `cp`、`mkdir`、`exec` 等）供 Node.js 專案使用。它讓你能直接在 JavaScript 中執行熟悉的 shell 指令，簡化了跨平台腳本的編寫。然而，在前端開發（通常指在瀏覽器中執行的程式碼）中，ShellJS 並不直接適用，因為它依賴的 Node.js API 在瀏覽器環境中並不可用。以下我將解釋原因，並說明如何在前端開發工作流程中有效運用 ShellJS。

### 為何 ShellJS 無法直接在瀏覽器中運行
- **Node.js 依賴性**：ShellJS 建基於 Node.js 運行環境，該環境提供檔案系統存取、程序執行等系統級操作的 API。由於瀏覽器的沙盒安全模型，這些 API 在瀏覽器中不可用。
- **瀏覽器安全限制**：為保護用戶免受惡意腳本侵害，瀏覽器禁止 JavaScript 存取本機檔案系統或執行任意指令。由於 ShellJS 的指令（如執行外部程序的 `exec` 或複製檔案的 `cp`）依賴這些功能，它們無法在瀏覽器環境中運作。

因此，你無法在瀏覽器中執行的客戶端 JavaScript 直接使用 ShellJS。不過，透過將 ShellJS 整合到建置流程或開發工具中（這些工具通常運行於 Node.js），它仍能在前端開發中發揮價值。

### 如何在前端開發工作流程中使用 ShellJS
雖然 ShellJS 不在瀏覽器中執行，但你可透過 Node.js 腳本利用它來自動化支援前端開發的任務。前端專案常依賴 Webpack、Gulp 或 Grunt 等建置工具，這些工具運行於 Node.js 並可整合 ShellJS 以簡化工作流程。具體方法如下：

#### 1. 安裝 ShellJS
首先確保系統已安裝 Node.js，然後透過 npm 或 yarn 將 ShellJS 加入專案：

```bash
npm install shelljs
```

或

```bash
yarn add shelljs
```

#### 2. 建立使用 ShellJS 的 Node.js 腳本
編寫腳本，使用 ShellJS 執行與前端專案相關的任務，例如複製檔案、建立目錄或執行命令列工具。將此腳本儲存為 `.js` 檔案（例如 `build.js`）。

以下是一個準備前端資源的範例腳本：

```javascript
const shell = require('shelljs');

// 如果建置目錄不存在則建立
shell.mkdir('-p', 'build');

// 將 HTML 檔案複製到建置目錄
shell.cp('-R', 'src/*.html', 'build/');

// 編譯 Sass 為 CSS
shell.exec('sass src/styles.scss build/styles.css');

// 複製 JavaScript 檔案
shell.cp('-R', 'src/*.js', 'build/');
```

- **`shell.mkdir('-p', 'build')`**：建立 `build` 目錄，`-p` 參數確保目錄已存在時不報錯。
- **`shell.cp('-R', 'src/*.html', 'build/')`**：將所有 HTML 檔案從 `src` 複製到 `build`，`-R` 參數表示遞歸複製。
- **`shell.exec('sass src/styles.scss build/styles.css')`**：執行 Sass 編譯器以生成 CSS。

#### 3. 將腳本整合至工作流程
你可透過以下方式執行此腳本：
- **直接透過 Node.js 執行**：
  ```bash
  node build.js
  ```
- **作為 npm 腳本**：將其加入 `package.json`：
  ```json
  "scripts": {
    "build": "node build.js"
  }
  ```
  然後執行：
  ```bash
  npm run build
  ```
- **與建置工具結合**：將 ShellJS 整合到 Gulp 等工具中。例如：
  ```javascript
  const gulp = require('gulp');
  const shell = require('shelljs');

  gulp.task('build', function(done) {
    shell.exec('sass src/styles.scss build/styles.css');
    shell.cp('-R', 'src/*.js', 'build/');
    done();
  });
  ```

#### 4. 前端開發中的應用場景
ShellJS 可自動化前端工作流程中的多種任務：
- **資源管理**：將圖片、字型等靜態檔案複製到建置目錄。
- **CSS/JavaScript 處理**：透過 `shell.exec` 執行 Sass、PostCSS 或 UglifyJS 等工具。
- **測試與程式碼檢查**：執行測試運行器或檢查工具（例如 `shell.exec('eslint src/*.js')`）。
- **部署準備**：打包檔案或清理目錄（例如 `shell.rm('-rf', 'build/*')`）。

### 範例：自動化前端建置流程
假設你正在建置一個包含 HTML、Sass 和 JavaScript 的簡單網頁應用程式，以下是使用 ShellJS 自動化建置的範例：

**目錄結構**：
```
project/
├── src/
│   ├── index.html
│   ├── styles.scss
│   └── app.js
├── build.js
└── package.json
```

**build.js**：
```javascript
const shell = require('shelljs');

// 清理建置目錄
shell.rm('-rf', 'build/*');

// 建立建置目錄
shell.mkdir('-p', 'build');

// 複製 HTML
shell.cp('src/index.html', 'build/');

// 編譯 Sass
shell.exec('sass src/styles.scss build/styles.css');

// 複製 JavaScript
shell.cp('src/app.js', 'build/');
```

**package.json**：
```json
{
  "scripts": {
    "build": "node build.js"
  },
  "dependencies": {
    "shelljs": "^0.8.5"
  }
}
```

執行 `npm run build`，ShellJS 將準備好包含編譯和複製檔案的 `build` 目錄，隨時可部署。

### 重點總結
- **不適用於瀏覽器**：由於依賴 Node.js 和系統級操作，ShellJS 無法在瀏覽器中運行。
- **完美適用於建置腳本**：在基於 Node.js 的腳本中使用它，可自動化檔案操作和指令執行等前端任務。
- **跨平台相容**：ShellJS 確保你的腳本在 Windows、Linux 和 macOS 上一致運作，適合多樣化的開發環境。

透過將 ShellJS 整合到 Node.js 驅動的建置流程中，即使它不直接在瀏覽器運行，你仍能透過強大的自動化功能提升前端開發工作流程。