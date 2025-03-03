---
audio: false
generated: true
lang: hant
layout: post
title: JavaScript 圖書館用於 Markdown
translated: true
---

看來你是在詢問如何使用 `marked` 圖書館，版本 `^0.3.6`，這是一個用於解析 Markdown 文本並將其轉換為 HTML 的 JavaScript 圖書館。由於你引用了特定版本的 `^0.3.6` 記號（可能來自 Node.js 專案中的 `package.json` 文件），我將指導你使用這個較舊的版本。請注意，版本 `0.3.6` 非常舊（約於 2016 年發布），圖書館自那時以來已經發展得非常大。然而，我將遵循該版本的使用方法。

### 第 1 步：安裝
如果你在 Node.js 環境中工作，可以使用 npm 安裝 `marked` 版本 `0.3.6`：

```bash
npm install marked@0.3.6
```

`package.json` 中的 `^0.3.6` 表示它將安裝 `0.3.6` 或任何兼容的補丁更新（例如 `0.3.7`），但為了明確起見，上述命令將其鎖定在 `0.3.6`。

### 第 2 步：基本使用
以下是如何在不同環境中使用 `marked` 版本 `0.3.6`：

#### 在 Node.js 中
1. **要求圖書館**：
   創建一個文件（例如 `index.js`）並添加以下內容：

   ```javascript
   var marked = require('marked');
   ```

2. **將 Markdown 轉換為 HTML**：
   使用 `marked()` 函數，將 Markdown 字符串傳遞給它。例如：

   ```javascript
   var markdownString = '# Hello World\nThis is **bold** text.';
   var html = marked(markdownString);
   console.log(html);
   ```

   **輸出**：
   ```html
   <h1>Hello World</h1>
   <p>This is <strong>bold</strong> text.</p>
   ```

#### 在瀏覽器中
1. **包含圖書館**：
   你可以使用 CDN 或下載 `marked@0.3.6` 並通過 `<script>` 標籤包含它。例如，使用歷史 CDN 鏈接（如果可用）或本地文件：

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **在 JavaScript 中使用**：
   包含腳本後，`marked` 將全局可用：

   ```html
   <script>
     var markdownString = '# Hello World\nThis is **bold** text.';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### 第 3 步：選項（適用於版本 0.3.6）
版本 `0.3.6` 支持一些自定義選項。你可以將選項對象作為 `marked()` 的第二個參數傳遞。以下是一個示例：

```javascript
var markdownString = '# Hello\nThis is *text* with `code`.';
var html = marked(markdownString, {
  gfm: true,         // 啟用 GitHub Flavored Markdown
  tables: true,      // 啟用 GFM 表格
  breaks: false,     // 如果為 true，則在單行斷行處添加 <br>
  pedantic: false,   // 如果為 true，則遵循嚴格的 Markdown 規範
  sanitize: false,   // 如果為 true，則為安全起見剔除 HTML 標籤
  smartLists: true,  // 改進列表渲染
  smartypants: false // 如果為 true，則使用 "智能" 印刷（例如，彎曲引號）
});
console.log(html);
```

### 0.3.6 的關鍵功能
- **基本 Markdown**：支持標題 (`#`)、粗體 (`**`)、斜體 (`*`)、列表、代碼塊 (```) 等。
- **GFM 支持**：如果設置 `gfm: true`，則可用 GitHub Flavored Markdown（例如表格和任務列表）。
- **無渲染器自定義**：與較新版本不同，`0.3.6` 不支持自定義渲染器，因此你受限於其默認輸出。

### 更多 Markdown 的示例
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

**輸出**：
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

### 注意事項
- **消毒**：如果你渲染用戶輸入，請設置 `sanitize: true` 以剔除原始 HTML 以保證安全（例如 `<script>` 標籤）。然而，這在 `0.3.6` 中是基本的，並不如現代替代方案那麼強大。
- **限制**：此版本缺少後來版本中添加的功能（例如異步解析、自定義標記器），因此如果你需要更多功能，請考慮升級到較新版本（例如 `5.x`）。
- **調試**：如果它不工作，請確保圖書館已正確加載並檢查 Markdown 語法。