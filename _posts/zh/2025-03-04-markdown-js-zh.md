---
audio: false
generated: true
lang: zh
layout: post
title: Markdown 的 JavaScript 库
translated: true
---

看起来你在询问如何使用 `marked` 库的版本 `^0.3.6`，这是一个用于解析 Markdown 文本并将其转换为 HTML 的 JavaScript 库。由于你引用了一个特定版本的 `^0.3.6` 表示法（可能来自一个 Node.js 项目中的 `package.json` 文件），我将指导你使用这个较旧版本的 `marked`。请注意，版本 `0.3.6` 非常旧（大约在 2016 年发布），库自那时以来已经发展得非常大。不过，我会坚持使用该版本的功能。

### 第 1 步：安装
如果你在 Node.js 环境中工作，可以使用 npm 安装 `marked` 版本 `0.3.6`：

```bash
npm install marked@0.3.6
```

`package.json` 中的 `^0.3.6` 表示它将安装 `0.3.6` 或任何兼容的补丁更新（例如 `0.3.7`），但为了明确起见，上述命令将其锁定为 `0.3.6`。

### 第 2 步：基本使用
以下是如何在不同环境中使用 `marked` 版本 `0.3.6`：

#### 在 Node.js 中
1. **引入库**：
   创建一个文件（例如 `index.js`）并添加以下内容：

   ```javascript
   var marked = require('marked');
   ```

2. **将 Markdown 转换为 HTML**：
   通过将 Markdown 字符串传递给 `marked()` 函数来使用它。例如：

   ```javascript
   var markdownString = '# Hello World\nThis is **bold** text.';
   var html = marked(markdownString);
   console.log(html);
   ```

   **输出**：
   ```html
   <h1>Hello World</h1>
   <p>This is <strong>bold</strong> text.</p>
   ```

#### 在浏览器中
1. **包含库**：
   你可以使用 CDN 或下载 `marked@0.3.6` 并通过 `<script>` 标签包含它。例如，使用历史 CDN 链接（如果可用）或本地文件：

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **在 JavaScript 中使用**：
   包含脚本后，`marked` 将全局可用：

   ```html
   <script>
     var markdownString = '# Hello World\nThis is **bold** text.';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### 第 3 步：选项（适用于版本 0.3.6）
版本 `0.3.6` 支持一些自定义选项。你可以将选项对象作为 `marked()` 的第二个参数传递。以下是一个示例：

```javascript
var markdownString = '# Hello\nThis is *text* with `code`.';
var html = marked(markdownString, {
  gfm: true,         // 启用 GitHub Flavored Markdown
  tables: true,      // 启用 GFM 表格
  breaks: false,     // 如果为 true，在单行换行处添加 <br>
  pedantic: false,   // 如果为 true，遵循严格的 Markdown 规范
  sanitize: false,   // 如果为 true，为安全起见剥离 HTML 标签
  smartLists: true,  // 改进列表渲染
  smartypants: false // 如果为 true，使用“智能”排版（例如，弯曲引号）
});
console.log(html);
```

### 0.3.6 的关键功能
- **基本 Markdown**：支持标题（`#`）、粗体（`**`）、斜体（`*`）、列表、代码块（```）等。
- **GFM 支持**：如果设置 `gfm: true`，则可用 GitHub Flavored Markdown（如表格和任务列表）。
- **无渲染器自定义**：与较新版本不同，`0.3.6` 不支持自定义渲染器，因此你只能使用其默认输出。

### 带有更多 Markdown 的示例
以下是 Node.js 中的完整示例：

```javascript
var marked = require('marked');

var markdown = `
# My Title
## Subtitle

- Item 1
- Item 2

\`\`\`
console.log("Hello");
\`\`\`

| Name  | Age |
|-------|-----|
| Alice | 25  |
| Bob   | 30  |
`;

var html = marked(markdown, { gfm: true, tables: true });
console.log(html);
```

**输出**：
```html
<h1>My Title</h1>
<h2>Subtitle</h2>
<ul>
<li>Item 1</li>
<li>Item 2</li>
</ul>
<pre><code>console.log("Hello");
</code></pre>
<table>
<thead>
<tr>
<th>Name</th>
<th>Age</th>
</tr>
</thead>
<tbody>
<tr>
<td>Alice</td>
<td>25</td>
</tr>
<tr>
<td>Bob</td>
<td>30</td>
</tr>
</tbody>
</table>
```

### 注意事项
- **清理**：如果你渲染用户输入，请设置 `sanitize: true` 以剥离原始 HTML 以确保安全（例如 `<script>` 标签）。不过，这在 `0.3.6` 中是基本的，不如现代替代方案那样强大。
- **限制**：这个版本缺少后续发布中添加的功能（例如异步解析、自定义标记器），因此如果你需要更多功能，请考虑升级到较新版本（例如 `5.x`）。
- **调试**：如果它不起作用，请确保库已正确加载并检查 Markdown 语法。