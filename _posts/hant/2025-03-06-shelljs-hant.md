---
audio: true
generated: true
lang: hant
layout: post
title: 使用 ShellJS 執行 Shell 指令
translated: true
---

ShellJS 是一個 JavaScript 圖書館，提供 Unix shell 命令（如 `cp`、`mkdir`、`exec` 等）供 Node.js 專案使用。它通過允許你直接在 JavaScript 中執行熟悉的 shell 命令，簡化了跨平台腳本的編寫。然而，在前端開發中——通常指在瀏覽器中運行的代碼——ShellJS 不能直接應用，因為它依賴於瀏覽器環境中不可用的 Node.js API。以下，我將解釋原因，並說明如何在前端開發工作流中有效使用 ShellJS。

### 為什麼 ShellJS 無法直接在瀏覽器中運行
- **Node.js 依賴性**：ShellJS 基於 Node.js 運行時，提供文件系統訪問、進程執行和其他系統級操作的 API。這些 API 由於瀏覽器的沙盒安全模型而不可用。
- **瀏覽器安全限制**：瀏覽器防止 JavaScript 訪問本地文件系統或執行任意命令，以保護用戶免受惡意腳本的侵害。由於 ShellJS 命令如 `exec`（運行外部進程）或 `cp`（複製文件）依賴於這些功能，因此無法在瀏覽器環境中運行。

因此，你不能在客戶端 JavaScript 中直接使用 ShellJS。然而，ShellJS 仍然可以在前端開發中發揮有價值的作用，通過將其集成到你的構建過程或開發工具中，這些工具通常在 Node.js 上運行。

### 如何在前端開發工作流中使用 ShellJS
雖然 ShellJS 不會在瀏覽器中執行，但你可以在 Node.js 基於的腳本中利用它來自動化支持你的前端開發的任務。前端項目通常依賴於像 Webpack、Gulp 或 Grunt 這樣的構建工具，這些工具在 Node.js 上運行並可以集成 ShellJS 來簡化工作流程。以下是如何做到的：

#### 1. 安裝 ShellJS
首先，確保你的系統上已安裝 Node.js。然後，使用 npm 或 yarn 將 ShellJS 添加到你的項目中：

```bash
npm install shelljs
```

或

```bash
yarn add shelljs
```

#### 2. 創建一個使用 ShellJS 的 Node.js 腳本
編寫一個使用 ShellJS 來執行與你的前端項目相關的任務的腳本，例如複製文件、創建目錄或運行命令行工具。將此腳本保存為 `.js` 文件（例如 `build.js`）。

以下是一個準備前端資產的示例腳本：

```javascript
const shell = require('shelljs');

// 如果不存在則創建一個構建目錄
shell.mkdir('-p', 'build');

// 將 HTML 文件複製到構建目錄
shell.cp('-R', 'src/*.html', 'build/');

// 編譯 Sass 為 CSS
shell.exec('sass src/styles.scss build/styles.css');

// 將 JavaScript 文件複製
shell.cp('-R', 'src/*.js', 'build/');
```

- **`shell.mkdir('-p', 'build')`**：創建一個 `build` 目錄，`-p` 確保如果已存在則不會出錯。
- **`shell.cp('-R', 'src/*.html', 'build/')`**：將所有 HTML 文件從 `src` 複製到 `build`，`-R` 表示遞歸複製。
- **`shell.exec('sass src/styles.scss build/styles.css')`**：運行 Sass 編譯器以生成 CSS。

#### 3. 將腳本集成到你的工作流中
你可以以多種方式運行此腳本：
- **直接通過 Node.js**：
  ```bash
  node build.js
  ```
- **作為 npm 腳本**：將其添加到你的 `package.json` 中：
  ```json
  "scripts": {
    "build": "node build.js"
  }
  ```
  然後運行：
  ```bash
  npm run build
  ```
- **與構建工具一起**：將 ShellJS 集成到像 Gulp 這樣的工具中。例如：
  ```javascript
  const gulp = require('gulp');
  const shell = require('shelljs');

  gulp.task('build', function(done) {
    shell.exec('sass src/styles.scss build/styles.css');
    shell.cp('-R', 'src/*.js', 'build/');
    done();
  });
  ```

#### 4. 前端開發中的使用案例
ShellJS 可以自動化前端工作流中的各種任務：
- **資產管理**：將圖像、字體或其他靜態文件複製到構建目錄。
- **CSS/JavaScript 處理**：通過 `shell.exec` 運行工具如 Sass、PostCSS 或 UglifyJS。
- **測試和檢查**：執行測試運行器或檢查器（例如 `shell.exec('eslint src/*.js')`）。
- **部署準備**：打包文件或清理目錄（例如 `shell.rm('-rf', 'build/*')`）。

### 示例：自動化前端構建過程
假設你正在構建一個簡單的網頁應用程序，使用 HTML、Sass 和 JavaScript。以下是你如何使用 ShellJS 來自動化構建的方法：

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

// 清理構建目錄
shell.rm('-rf', 'build/*');

// 創建構建目錄
shell.mkdir('-p', 'build');

// 將 HTML 文件複製
shell.cp('src/index.html', 'build/');

// 編譯 Sass
shell.exec('sass src/styles.scss build/styles.css');

// 將 JavaScript 文件複製
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

運行 `npm run build`，ShellJS 將準備好你的 `build` 目錄，其中包含編譯和複製的文件，準備好進行部署。

### 關鍵要點
- **不適用於瀏覽器使用**：由於其依賴於 Node.js 和系統級操作，ShellJS 無法在瀏覽器中運行。
- **適合構建腳本**：在 Node.js 基於的腳本中使用它來自動化前端任務，如文件操作和命令執行。
- **跨平台**：ShellJS 確保你的腳本在 Windows、Linux 和 macOS 上一致運行，使其適合多樣化的開發環境。

通過將 ShellJS 集成到你的 Node.js 運行的構建過程中，你可以通過強大的自動化來增強你的前端開發工作流程，即使它不直接在瀏覽器中運行。