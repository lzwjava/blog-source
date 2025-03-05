---
audio: false
generated: true
lang: hant
layout: post
title: 使用 PostCSS 進行 CSS 轉換
translated: true
---

我會解釋如何在前端項目中使用 PostCSS。PostCSS 是一個用於用 JavaScript 插件轉換 CSS 的工具，提供自動前綴、最小化和未來 CSS 語法支持等功能。以下是逐步指南：

### 1. **設置您的項目**
確保您有一個安裝了 Node.js 的前端項目。如果沒有，請初始化一個：
```bash
mkdir my-project
cd my-project
npm init -y
```

### 2. **安裝 PostCSS 和所需工具**
安裝 PostCSS、PostCSS CLI 和您想要使用的任何插件（例如，`autoprefixer` 用於供應商前綴或 `cssnano` 用於最小化）：
```bash
npm install --save-dev postcss postcss-cli autoprefixer cssnano
```

### 3. **創建一個 CSS 文件**
創建一個源 CSS 文件，例如 `src/styles.css`：
```css
/* src/styles.css */
.container {
  display: flex;
  transition: all 0.3s ease;
}
```

### 4. **配置 PostCSS**
在項目根目錄中創建一個 `postcss.config.js` 文件以指定插件：
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'), // 添加供應商前綴
    require('cssnano')({ preset: 'default' }) // 最小化 CSS
  ]
};
```

### 5. **添加構建腳本**
在 `package.json` 中添加一個腳本來用 PostCSS 處理您的 CSS：
```json
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```
- `src/styles.css`：輸入文件
- `dist/styles.css`：輸出文件

### 6. **運行 PostCSS**
運行構建命令：
```bash
npm run build:css
```
這將處理 `src/styles.css` 並將轉換後的 CSS 输出到 `dist/styles.css`。例如，`autoprefixer` 可能會添加前綴，`cssnano` 會最小化它：
```css
/* dist/styles.css */
.container{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-transition:all .3s ease;transition:all .3s ease}
```

### 7. **與構建工具集成（可選）**
為了更強大的設置，將 PostCSS 與 Webpack、Vite 或 Gulp 等工具集成：

#### **與 Vite**
如果使用 Vite，安裝 `postcss` 並在 `vite.config.js` 中配置它：
```javascript
// vite.config.js
import postcss from 'postcss';
import autoprefixer from 'autoprefixer';

export default {
  css: {
    postcss: {
      plugins: [autoprefixer()]
    }
  }
};
```
當您導入 CSS 文件時，Vite 會自動處理 PostCSS。

#### **與 Webpack**
安裝 `postcss-loader`：
```bash
npm install --save-dev postcss-loader
```
更新您的 `webpack.config.js`：
```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader', 'postcss-loader']
      }
    ]
  }
};
```

### 8. **監視變更（可選）**
為了在開發過程中自動處理 CSS，修改您的 `package.json` 腳本：
```json
"scripts": {
  "watch:css": "postcss src/styles.css -o dist/styles.css --watch"
}
```
運行 `npm run watch:css` 以監視文件變更。

### 9. **常見插件**
以下是一些流行的 PostCSS 插件：
- `autoprefixer`：根據瀏覽器支持添加供應商前綴。
- `cssnano`：最小化 CSS。
- `postcss-preset-env`：讓您今天就能使用未來的 CSS 功能。
- `postcss-import`：解析 `@import` 規則。
按需安裝它們：
```bash
npm install --save-dev postcss-preset-env postcss-import
```
將它們添加到 `postcss.config.js`：
```javascript
module.exports = {
  plugins: [
    require('postcss-import'),
    require('postcss-preset-env'),
    require('autoprefixer'),
    require('cssnano')({ preset: 'default' })
  ]
};
```

### 範例工作流程
1. 在 `src/styles.css` 中編寫現代 CSS：
```css
@custom-media --viewport-medium (width >= 768px);

:root {
  --main-color: #1a73e8;
}

.container {
  color: var(--main-color);
  display: grid;
}

@media (--viewport-medium) {
  .container {
    grid-template-columns: 1fr 1fr;
  }
}
```
2. 運行 `npm run build:css`。
3. 在 `dist/styles.css` 中獲取處理過的 CSS，帶有前綴、解析變量和最小化。

### 提示
- 在 CLI 中使用 `--map`（`postcss src/styles.css -o dist/styles.css --map`）以生成源映射以進行調試。
- 查看插件文檔以獲取特定配置選項。
- 通過將輸出 CSS 鏈接到您的 HTML 或打包器來與前端框架（React、Vue 等）結合。

如果您需要幫助設置或插件，請告訴我！