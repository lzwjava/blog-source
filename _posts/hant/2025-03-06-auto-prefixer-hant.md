---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Autoprefixer
translated: true
---

我會解釋如何在前端開發中使用 Autoprefixer。Autoprefixer 是一個 PostCSS 插件，能自動為你的 CSS 添加供應商前綴，確保跨瀏覽器兼容性。

以下是將 Autoprefixer 集成到前端工作流程的主要方法：

1. 使用 npm（最常見的方法）
```bash
# 安裝 autoprefixer 和 postcss
npm install autoprefixer postcss --save-dev
```

2. 基本設置與 PostCSS CLI
```bash
# 安裝 postcss-cli
npm install postcss-cli --save-dev

# 創建一個 postcss.config.js 文件
module.exports = {
  plugins: [
    require('autoprefixer')
  ]
}

# 添加到 package.json 腳本
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```

3. 使用構建工具：

a) Webpack 使用 postcss-loader
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

b) Vite（內建支持）
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
      flexbox: 'no-2009' // Flexbox 支持選項
    })
  ]
}
```

5. CSS 中的示例使用
```css
/* 输入 */
.container {
  display: flex;
  justify-content: space-between;
}

/* 输出（經過 Autoprefixer 後） */
.container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
```

主要特點和技巧：
- 自動根據 Can I Use 數據添加前綴
- 由 browserslist 控制（通常在 package.json 中）
- 移除舊版 CSS 的過時前綴
- 適用於現代 CSS 功能，如自定義屬性

package.json 中的基本 browserslist 示例：
```json
{
  "browserslist": [
    "> 1%",
    "last 2 versions",
    "not dead"
  ]
}
```

運行：
```bash
# 使用 PostCSS CLI
npx postcss src/*.css --dir dist

# 或使用你的 npm 腳本
npm run build:css
```

根據你的項目現有設置（Webpack、Vite 等）選擇集成方法。Webpack 或 Vite 方法在現代前端開發中最常見，因為它們能很好地與現有的構建過程集成。