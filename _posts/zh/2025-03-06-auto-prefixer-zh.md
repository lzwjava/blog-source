---
audio: false
generated: true
lang: zh
layout: post
title: 使用 Autoprefixer
translated: true
---

我将解释如何在前端开发中使用 Autoprefixer。Autoprefixer 是一个 PostCSS 插件，它会自动为你的 CSS 添加供应商前缀，确保跨浏览器兼容性。

以下是将 Autoprefixer 集成到前端工作流程中的主要方法：

1. 使用 npm（最常见的方法）
```bash
# 安装 autoprefixer 和 postcss
npm install autoprefixer postcss --save-dev
```

2. 使用 PostCSS CLI 的基本设置
```bash
# 安装 postcss-cli
npm install postcss-cli --save-dev

# 创建一个 postcss.config.js 文件
module.exports = {
  plugins: [
    require('autoprefixer')
  ]
}

# 添加到 package.json 脚本
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```

3. 使用构建工具：

a) Webpack 与 postcss-loader
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

b) Vite（内置支持）
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

4. 配置选项
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer')({
      overrideBrowserslist: ['> 1%', 'last 2 versions'], // 目标浏览器
      grid: true, // 启用网格前缀
      flexbox: 'no-2009' // Flexbox 支持选项
    })
  ]
}
```

5. CSS 中的示例用法
```css
/* 输入 */
.container {
  display: flex;
  justify-content: space-between;
}

/* 输出（经过 Autoprefixer 处理） */
.container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
```

关键特性和技巧：
- 根据 Can I Use 数据自动添加前缀
- 由 browserslist 控制（通常在 package.json 中）
- 移除旧的 CSS 前缀
- 与现代 CSS 特性（如自定义属性）一起工作

在 package.json 中的基本 browserslist 示例：
```json
{
  "browserslist": [
    "> 1%",
    "last 2 versions",
    "not dead"
  ]
}
```

运行：
```bash
# 使用 PostCSS CLI
npx postcss src/*.css --dir dist

# 或使用你的 npm 脚本
npm run build:css
```

根据你的项目现有设置（Webpack、Vite 等）选择集成方法。Webpack 或 Vite 方法在现代前端开发中最为常见，因为它们与现有的构建流程集成得很好。