---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Autoprefixer
translated: true
type: note
---

我將解釋如何在前端開發中使用 Autoprefixer。Autoprefixer 是一個 PostCSS 插件，能自動為你的 CSS 添加供應商前綴，確保跨瀏覽器兼容性。

以下是將 Autoprefixer 整合到前端工作流程的主要方式：

1. 使用 npm（最常見的方法）
```bash
# 安裝 autoprefixer 和 postcss
npm install autoprefixer postcss --save-dev
```

2. 使用 PostCSS CLI 的基本設置
```bash
# 安裝 postcss-cli
npm install postcss-cli --save-dev

# 創建 postcss.config.js 文件
module.exports = {
  plugins: [
    require('autoprefixer')
  ]
}

# 添加到 package.json 的 scripts
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```

3. 與建構工具搭配使用：

a) Webpack 與 postcss-loader
```bash
npm install postcss-loader --save-dev
```

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader',
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: ['autoprefixer']
              }
            }
          }
        ]
      }
    ]
  }
}
```

b) Vite（內置支援）
```javascript
// vite.config.js
import autoprefixer from 'autoprefixer'

export default {
  css: {
    postcss: {
      plugins: [autoprefixer()]
    }
  }
}
```

4. 配置選項
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer')({
      overrideBrowserslist: ['> 1%', 'last 2 versions'], // 目標瀏覽器
      grid: true, // 啟用網格前綴
      flexbox: 'no-2009' // Flexbox 支援選項
    })
  ]
}
```

5. CSS 中的使用範例
```css
/* 輸入 */
.container {
  display: flex;
  justify-content: space-between;
}

/* 輸出（經過 Autoprefixer 處理後） */
.container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
```

主要功能和提示：
- 根據 Can I Use 數據自動添加前綴
- 由 browserslist 控制（通常在 package.json 中）
- 從舊版 CSS 中移除過時的前綴
- 支援現代 CSS 功能如自定義屬性

package.json 中的基本 browserslist 範例：
```json
{
  "browserslist": [
    "> 1%",
    "last 2 versions",
    "not dead"
  ]
}
```

執行方式：
```bash
# 使用 PostCSS CLI
npx postcss src/*.css --dir dist

# 或使用 npm script
npm run build:css
```

請根據專案現有設置（Webpack、Vite 等）選擇整合方法。在現代前端開發中，Webpack 或 Vite 方法最為常見，因為它們能很好地與現有建構流程整合。