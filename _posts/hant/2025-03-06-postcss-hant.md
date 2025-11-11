---
audio: false
generated: true
lang: hant
layout: post
title: 使用 PostCSS 轉換 CSS
translated: true
type: note
---

我將解釋如何在前端專案中使用 PostCSS。PostCSS 是一個透過 JavaScript 外掛來轉換 CSS 的工具，提供自動前綴添加、程式碼壓縮和未來 CSS 語法支援等功能。以下是逐步指南：

### 1. **設定專案**
確保您有一個已安裝 Node.js 的前端專案。如果沒有，請初始化一個：
```bash
mkdir my-project
cd my-project
npm init -y
```

### 2. **安裝 PostCSS 與必要工具**
安裝 PostCSS、PostCSS CLI 以及您要使用的外掛（例如用於供應商前綴的 `autoprefixer` 或用於壓縮的 `cssnano`）：
```bash
npm install --save-dev postcss postcss-cli autoprefixer cssnano
```

### 3. **建立 CSS 檔案**
建立來源 CSS 檔案，例如 `src/styles.css`：
```css
/* src/styles.css */
.container {
  display: flex;
  transition: all 0.3s ease;
}
```

### 4. **配置 PostCSS**
在專案根目錄建立 `postcss.config.js` 檔案來指定外掛：
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'), // 添加供應商前綴
    require('cssnano')({ preset: 'default' }) // 壓縮 CSS
  ]
};
```

### 5. **添加建置指令**
在 `package.json` 中添加處理 CSS 的 PostCSS 指令：
```json
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```
- `src/styles.css`：輸入檔案
- `dist/styles.css`：輸出檔案

### 6. **執行 PostCSS**
執行建置指令：
```bash
npm run build:css
```
這會處理 `src/styles.css` 並將轉換後的 CSS 輸出到 `dist/styles.css`。例如，`autoprefixer` 可能會添加前綴，而 `cssnano` 會進行壓縮：
```css
/* dist/styles.css */
.container{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-transition:all .3s ease;transition:all .3s ease}
```

### 7. **與建置工具整合（可選）**
為了更完善的設定，可將 PostCSS 與 Webpack、Vite 或 Gulp 等工具整合：

#### **使用 Vite**
如果使用 Vite，請安裝 `postcss` 並在 `vite.config.js` 中配置：
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
當您匯入 CSS 檔案時，Vite 會自動處理 PostCSS。

#### **使用 Webpack**
安裝 `postcss-loader`：
```bash
npm install --save-dev postcss-loader
```
更新 `webpack.config.js`：
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

### 8. **監聽檔案變更（可選）**
若要在開發期間自動處理 CSS，請修改 `package.json` 中的指令：
```json
"scripts": {
  "watch:css": "postcss src/styles.css -o dist/styles.css --watch"
}
```
執行 `npm run watch:css` 即可監聽檔案變更。

### 9. **常用外掛**
以下是一些熱門的 PostCSS 外掛：
- `autoprefixer`：根據瀏覽器支援度添加供應商前綴
- `cssnano`：壓縮 CSS
- `postcss-preset-env`：讓您立即使用未來的 CSS 功能
- `postcss-import`：解析 `@import` 規則
按需安裝：
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
2. 執行 `npm run build:css`
3. 在 `dist/styles.css` 中獲得已處理的 CSS，包含前綴、解析後的變數和壓縮效果

### 實用技巧
- 在 CLI 中使用 `--map` 參數（`postcss src/styles.css -o dist/styles.css --map`）來生成除錯用的原始碼對應檔
- 查閱外掛文件以獲取特定配置選項
- 透過將輸出 CSS 連結到 HTML 或打包工具，與前端框架（React、Vue 等）結合使用

如果您需要特定設定或外掛的協助，請隨時告訴我！