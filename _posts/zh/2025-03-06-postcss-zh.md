---
audio: false
generated: true
lang: zh
layout: post
title: 使用 PostCSS 进行 CSS 转换
translated: true
---

我将解释如何在前端项目中使用 PostCSS。PostCSS 是一个用于用 JavaScript 插件转换 CSS 的工具，提供了自动添加前缀、压缩和支持未来 CSS 语法等功能。以下是一个逐步指南：

### 1. **设置项目**
确保你有一个安装了 Node.js 的前端项目。如果没有，初始化一个：
```bash
mkdir my-project
cd my-project
npm init -y
```

### 2. **安装 PostCSS 和所需工具**
安装 PostCSS、PostCSS CLI 以及你想要使用的任何插件（例如 `autoprefixer` 用于供应商前缀或 `cssnano` 用于压缩）：
```bash
npm install --save-dev postcss postcss-cli autoprefixer cssnano
```

### 3. **创建一个 CSS 文件**
创建一个源 CSS 文件，例如 `src/styles.css`：
```css
/* src/styles.css */
.container {
  display: flex;
  transition: all 0.3s ease;
}
```

### 4. **配置 PostCSS**
在项目根目录下创建一个 `postcss.config.js` 文件以指定插件：
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'), // 添加供应商前缀
    require('cssnano')({ preset: 'default' }) // 压缩 CSS
  ]
};
```

### 5. **添加构建脚本**
在你的 `package.json` 中添加一个脚本来使用 PostCSS 处理你的 CSS：
```json
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```
- `src/styles.css`：输入文件
- `dist/styles.css`：输出文件

### 6. **运行 PostCSS**
运行构建命令：
```bash
npm run build:css
```
这将处理 `src/styles.css` 并将转换后的 CSS 输出到 `dist/styles.css`。例如，`autoprefixer` 可能会添加前缀，`cssnano` 会压缩它：
```css
/* dist/styles.css */
.container{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-transition:all .3s ease;transition:all .3s ease}
```

### 7. **与构建工具集成（可选）**
为了更强大的设置，将 PostCSS 与 Webpack、Vite 或 Gulp 等工具集成：

#### **与 Vite**
如果使用 Vite，安装 `postcss` 并在 `vite.config.js` 中配置它：
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
Vite 在你导入 CSS 文件时会自动处理 PostCSS。

#### **与 Webpack**
安装 `postcss-loader`：
```bash
npm install --save-dev postcss-loader
```
更新你的 `webpack.config.js`：
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

### 8. **监视变化（可选）**
为了在开发过程中自动处理 CSS，修改你的 `package.json` 脚本：
```json
"scripts": {
  "watch:css": "postcss src/styles.css -o dist/styles.css --watch"
}
```
运行 `npm run watch:css` 以监视文件变化。

### 9. **常用插件**
以下是一些流行的 PostCSS 插件：
- `autoprefixer`：根据浏览器支持添加供应商前缀。
- `cssnano`：压缩 CSS。
- `postcss-preset-env`：让你今天就能使用未来的 CSS 功能。
- `postcss-import`：解析 `@import` 规则。
根据需要安装它们：
```bash
npm install --save-dev postcss-preset-env postcss-import
```
将它们添加到 `postcss.config.js`：
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

### 示例工作流
1. 在 `src/styles.css` 中编写现代 CSS：
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
2. 运行 `npm run build:css`。
3. 在 `dist/styles.css` 中获取处理后的 CSS，带有前缀、解析的变量和压缩。

### 提示
- 在 CLI 中使用 `--map`（`postcss src/styles.css -o dist/styles.css --map`）以生成源映射文件进行调试。
- 检查插件文档以获取特定的配置选项。
- 通过将输出 CSS 链接到你的 HTML 或打包器与前端框架（React、Vue 等）结合使用。