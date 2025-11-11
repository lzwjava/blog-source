---
audio: false
generated: true
lang: hant
layout: post
title: Markdown 的 JavaScript 程式庫
translated: true
type: note
---

看來您是想了解如何使用 `marked` 函式庫（版本 `^0.3.6`），這是一個用於解析 Markdown 文字並轉換為 HTML 的 JavaScript 函式庫。由於您透過 `^0.3.6` 標記法（可能來自 Node.js 專案中的 `package.json` 檔案）引用了特定版本，我將指導您使用這個舊版 `marked`。請注意，版本 `0.3.6` 相當老舊（約在 2016 年發布），此後函式庫已有顯著發展。但我將以適用於該版本的內容為主。

### 步驟 1：安裝
如果您在 Node.js 環境中工作，可以使用 npm 安裝 `marked` 版本 `0.3.6`：

```bash
npm install marked@0.3.6
```

在 `package.json` 中的 `^0.3.6` 表示它將安裝 `0.3.6` 或任何相容的修補更新（例如 `0.3.7`），但為了清晰起見，上述指令將其鎖定為確切的 `0.3.6`。

### 步驟 2：基本用法
以下是如何在不同環境中使用 `marked` 版本 `0.3.6`：

#### 在 Node.js 中
1. **引入函式庫**：
   建立一個檔案（例如 `index.js`）並加入以下內容：

   ```javascript
   var marked = require('marked');
   ```

2. **將 Markdown 轉換為 HTML**：
   透過傳遞 Markdown 字串給 `marked()` 函式來使用。例如：

   ```javascript
   var markdownString = '# Hello World\n這是 **粗體** 文字。';
   var html = marked(markdownString);
   console.log(html);
   ```

   **輸出**：
   ```html
   <h1>Hello World</h1>
   <p>這是 <strong>粗體</strong> 文字。</p>
   ```

#### 在瀏覽器中
1. **引入函式庫**：
   您可以使用 CDN 或下載 `marked@0.3.6` 並透過 `<script>` 標籤引入。例如，使用歷史 CDN 連結（如果可用）或本地檔案：

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **在 JavaScript 中使用**：
   引入腳本後，`marked` 將在全域可用：

   ```html
   <script>
     var markdownString = '# Hello World\n這是 **粗體** 文字。';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### 步驟 3：選項（適用於版本 0.3.6）
版本 `0.3.6` 支援一些自訂選項。您可以將選項物件作為第二個參數傳遞給 `marked()`。以下是一個範例：

```javascript
var markdownString = '# Hello\n這是帶有 `code` 的 *文字*。';
var html = marked(markdownString, {
  gfm: true,         // 啟用 GitHub Flavored Markdown
  tables: true,      // 啟用 GFM 表格
  breaks: false,     // 如果為 true，在單行換行處添加 <br>
  pedantic: false,   // 如果為 true，遵循嚴格的 Markdown 規範
  sanitize: false,   // 如果為 true，為安全起見移除 HTML 標籤
  smartLists: true,  // 改進列表渲染
  smartypants: false // 如果為 true，使用「智慧」排版（例如彎引號）
});
console.log(html);
```

### 0.3.6 版本的主要功能
- **基本 Markdown**：支援標題（`#`）、粗體（`**`）、斜體（`*`）、列表、程式碼區塊（```）等。
- **GFM 支援**：如果設定 `gfm: true`，則可使用 GitHub Flavored Markdown（例如表格和任務列表）。
- **無渲染器自訂**：與新版本不同，`0.3.6` 不支援自訂渲染器，因此您僅限於其預設輸出。

### 更多 Markdown 範例
以下是 Node.js 中的完整範例：

```javascript
var marked = require('marked');

var markdown = `
# 我的標題
## 副標題

- 項目 1
- 項目 2

\`\`\`
console.log("Hello");
\`\`\`

| 名稱    | 年齡 |
|---------|------|
| Alice   | 25   |
| Bob     | 30   |
`;

var html = marked(markdown, { gfm: true, tables: true });
console.log(html);
```

**輸出**：
```html
<h1>我的標題</h1>
<h2>副標題</h2>
<ul>
<li>項目 1</li>
<li>項目 2</li>
</ul>
<pre><code>console.log("Hello");
</code></pre>
<table>
<thead>
<tr>
<th>名稱</th>
<th>年齡</th>
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
- **消毒處理**：如果您要渲染使用者輸入，請設定 `sanitize: true` 以移除原始 HTML 以確保安全（例如 `<script>` 標籤）。但這在 `0.3.6` 中是基本功能，不如現代替代方案穩健。
- **限制**：此版本缺少後續版本中添加的功能（例如非同步解析、自訂分詞器），因此如果您需要更多功能，請考慮升級到新版本，例如 `5.x`。
- **除錯**：如果無法運作，請確保函式庫正確載入並檢查 Markdown 語法。