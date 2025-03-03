---
audio: false
generated: true
lang: zh
layout: post
title: GitHub 的 Markdown 样式
translated: true
---

### 关键点
- 使用 "github-markdown-css" npm 包似乎需要先通过 `npm install github-markdown-css` 安装。
- 研究表明，接下来需要将 CSS 文件导入到项目中，并将 Markdown 内容包裹在一个带有类 "markdown-body" 的 div 中。
- 证据倾向于设置可选的宽度和填充以匹配 GitHub 的样式，并确保 DOctype 以避免样式问题。

### 安装
在项目目录中使用 npm 安装包：
- 运行 `npm install github-markdown-css` 将其添加到依赖项中。

### 使用
安装后，将 CSS 集成到项目中：
- 例如，在 JavaScript/React 中导入 CSS 文件 `import 'github-markdown-css';`。
- 将渲染的 Markdown 内容包裹在 `<div class="markdown-body">...</div>` 中以应用样式。
- 可选地，添加 CSS 以设置宽度和填充，以模仿 GitHub 的外观：
  ```css
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  ```
- 确保 HTML 包含 DOctype（例如 `<!DOCTYPE html>`），以防止怪异模式问题，这可能会影响样式。

### 意外细节
你可能不会预料到，该包还支持通过相关包 [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) 生成自定义 CSS，如果你需要定制样式。

---

### 调查笔记：使用 github-markdown-css npm 包的全面指南

本详细指南探讨了使用 "github-markdown-css" npm 包在 Web 项目中复制 GitHub 的 Markdown 样式。它提供了安装和集成的逐步方法，以及在各种开发环境（如 React 或纯 HTML）中优化使用的附加考虑因素。信息来源于官方包文档、GitHub 仓库和相关网络资源，确保开发人员在各个层次上都能全面理解。

#### 背景和目的
由 [sindresorhus](https://github.com/sindresorhus) 维护的 "github-markdown-css" 包提供了一组最小的 CSS，以模仿 GitHub 的 Markdown 渲染样式。这对于希望其 Markdown 内容（如文档或博客文章）外观与 GitHub 的熟悉和干净呈现一致的开发人员特别有用。该包在 npm 仓库中被 1,168 个其他项目使用，表明其流行和可靠性。

#### 安装过程
首先，需要通过 npm 安装包，Node.js 包管理器。命令非常简单：
- 在项目目录中执行 `npm install github-markdown-css`。这将包添加到 `node_modules` 文件夹中，并更新 `package.json` 以包含依赖项。

该包的最新版本（截至最近检查）是 5.8.1，大约三个月前发布，这表明其活跃维护和更新。这确保了与现代 Web 开发实践和框架的兼容性。

#### 集成和使用
安装后，下一步是将 CSS 集成到项目中。该包提供了一个名为 `github-markdown.css` 的文件，可以根据项目设置进行导入：

- **对于 JavaScript/现代框架（例如 React、Vue）：**
  - 在 JavaScript 或 TypeScript 文件中使用导入语句，例如 `import 'github-markdown-css';`。这与 Webpack 或 Vite 等处理 CSS 导入的捆绑器配合得很好。
  - 对于 React，开发人员可能会看到在组件文件中导入它的示例，确保样式全局可用或按需作用域。

- **对于纯 HTML：**
  - 在 HTML 头部直接链接 CSS 文件：
    ```html
    <link rel="stylesheet" href="node_modules/github-markdown-css/github-markdown.css">
    ```
  - 请注意，路径可能会根据项目结构有所不同；确保相对路径正确指向 `node_modules` 目录。

导入后，通过将渲染的 Markdown 内容包裹在带有类 "markdown-body" 的 `<div>` 中来应用样式。例如：
```html
<div class="markdown-body">
  <h1>独角兽</h1>
  <p>所有的事情</p>
</div>
```
这个类是关键的，因为 CSS 将样式应用于 `.markdown-body` 内的元素，包括排版、代码块、表格等。

#### 样式考虑
为了完全复制 GitHub 的 Markdown 外观，考虑为 `.markdown-body` 类设置宽度和填充。文档建议：
- 最大宽度为 980px，大屏幕上填充 45px，移动设备（屏幕 ≤ 767px）填充 15px。
- 可以通过以下 CSS 实现：
  ```css
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  ```
这确保了响应性，并与 GitHub 的设计一致，增强了可读性和用户体验。

#### 技术说明和最佳实践
- **DOctype 要求：** 文档强调了潜在的样式问题，例如在浏览器进入怪异模式时，暗模式下的表格可能会渲染不正确。为了防止这一点，始终在 HTML 顶部包含一个 DOctype，例如 `<!DOCTYPE html>`。这确保了标准兼容的渲染，并避免了意外行为。
- **Markdown 解析：** 该包提供了 CSS，但不将 Markdown 转换为 HTML。你需要一个 Markdown 解析器，例如 [marked.js](https://marked.js.org/) 或 [react-markdown](https://github.com/remarkjs/react-markdown) 来将 Markdown 文本转换为 HTML，然后可以使用此 CSS 进行样式设置。
- **自定义 CSS 生成：** 对于高级用户，相关包 [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) 允许生成自定义 CSS，这对于特定主题或修改可能有用。这是一个意外的细节，对于那些可能认为该包仅用于直接使用的人来说。

#### 特定上下文中的使用
- **React 项目：** 在 React 中，将 `github-markdown-css` 与 `react-markdown` 结合使用是常见的。安装两者后，导入 CSS 并使用组件：
  ```javascript
  import React from 'react';
  import ReactMarkdown from 'react-markdown';
  import 'github-markdown-css';

  const MarkdownComponent = () => (
    <div className="markdown-body">
      <ReactMarkdown># 你好，世界！</ReactMarkdown>
    </div>
  );
  ```
  确保你也设置了宽度和填充 CSS，如上所述，以获得完整的 GitHub 样式。

- **使用 CDN 的纯 HTML：** 对于快速原型设计，可以使用 [cdnjs](https://cdnjs.com/libraries/github-markdown-css) 上的 CDN 版本，通过直接链接：
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css">
  ```
  然后像以前一样应用 `.markdown-body` 类。

#### 潜在问题和解决方案
- **样式冲突：** 如果你的项目使用其他 CSS 框架（例如 Tailwind、Bootstrap），请确保没有特异性冲突。`.markdown-body` 类应该覆盖大多数样式，但要彻底测试。
- **暗模式支持：** 该包包括对暗模式的支持，但请确保你的 Markdown 解析器和项目设置正确处理主题切换，特别是代码块和表格。
- **浏览器兼容性：** 由于该包的广泛使用，兼容性通常很好，但始终在主要浏览器（Chrome、Firefox、Safari）上测试，以确保一致的渲染。

#### 比较分析
与其他 Markdown CSS 选项（如 [Markdown CSS](https://markdowncss.github.io/)）相比，"github-markdown-css" 以直接复制 GitHub 的样式而脱颖而出，使其非常适合镜像 GitHub 样式的文档。然而，它在没有额外定制的情况下缺乏内置主题选项，而一些替代方案则提供多个主题。

#### 表：关键功能和考虑因素

| 功能                  | 描述                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| 安装命令     | `npm install github-markdown-css`                                           |
| CSS 导入方法        | `import 'github-markdown-css';` 或 `<link>` 在 HTML 中                         |
| 所需类           | `.markdown-body` 用于样式应用                                    |
| 宽度和填充        | 最大 980px，桌面 45px 填充；移动设备（≤ 767px）15px 填充            |
| DOctype 要求      | 确保避免怪异模式并确保正确渲染                  |
| 自定义 CSS 生成    | 通过 [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) 可能 |
| 兼容性            | 与 marked.js、react-markdown 等 Markdown 解析器兼容；广泛的浏览器支持 |

#### 结论
使用 "github-markdown-css" 对于希望复制 GitHub 的 Markdown 样式的开发人员来说非常简单。通过遵循安装和集成步骤，并考虑附加样式和技术说明，你可以实现 Markdown 内容的一致和专业外观。对于高级定制，探索生成包，并始终测试兼容性和渲染问题，特别是在复杂项目中。

#### 关键引用
- [github-markdown-css npm 包页面](https://www.npmjs.com/package/github-markdown-css)
- [最小 CSS 以复制 GitHub Markdown 样式 GitHub 仓库](https://github.com/sindresorhus/github-markdown-css)
- [GitHub Markdown CSS 演示页面](https://sindresorhus.com/github-markdown-css/)
- [生成 github-markdown-css npm 包的 CSS](https://www.npmjs.com/package/generate-github-markdown-css)
- [github-markdown-css CDN 由 cdnjs](https://cdnjs.com/libraries/github-markdown-css)