---
audio: false
generated: true
lang: hant
layout: post
title: 從使用 Kramdown 轉換為 Marked
translated: true
type: note
---

要將你的 Jekyll 博客從使用 Kramdown 切換到 Marked，你需要對 Jekyll 配置和設定進行一些更改。Marked 是一個用於解析和編譯 Markdown 的 JavaScript 函式庫，它可以與 MathJax 結合使用以實現更好的數學公式渲染。以下是切換的逐步指南：

### 步驟 1：安裝 Marked
首先，你需要將 Marked 函式庫加入你的 Jekyll 專案中。你可以透過在佈局檔案（例如 `default.html`）的 `<head>` 區段中加入它來實現。

```html
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
```

### 步驟 2：停用 Kramdown
在你的 `_config.yml` 檔案中，將 `markdown` 選項設定為 `none` 來停用 Kramdown，或者如果它原本設定為 Kramdown，直接移除該設定即可。

```yaml
markdown: none
```

### 步驟 3：配置 Marked 與 MathJax
你需要配置 Marked 以使其與 MathJax 協同工作。在你的 Jekyll 專案中建立一個 JavaScript 檔案（例如 `marked-mathjax.js`），並包含以下程式碼：

```javascript
document.addEventListener("DOMContentLoaded", function() {
  // 使用 Marked 渲染 Markdown 內容
  const elements = document.querySelectorAll('.markdown-content');
  elements.forEach(element => {
    const html = marked(element.textContent);
    element.innerHTML = html;
  });

  // 渲染 MathJax
  MathJax.typesetPromise().then(() => {
    console.log('MathJax 渲染完成！');
  }).catch((err) => console.log('排版失敗：', err));
});
```

在佈局檔案中包含此腳本，位置應在引入 Marked 和 MathJax 之後：

```html
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script src="{{ '/assets/js/marked-mathjax.js' | relative_url }}"></script>
```

### 步驟 4：更新你的 Markdown 內容
確保你的 Markdown 內容被包裹在一個具有 `markdown-content` 類別的容器中，以便 JavaScript 能夠針對其進行渲染。

```html
<div class="markdown-content">
  <!-- 你的 Markdown 內容在此 -->
</div>
```

### 步驟 5：測試你的設定
在本機建構並啟動你的 Jekyll 網站，以確保 Marked 正確渲染了你的 Markdown，並且 MathJax 能正常顯示數學公式。

```bash
bundle exec jekyll serve
```

### 補充說明
- 確保你的 MathJax 配置與你的 Markdown 內容相容。你可能需要根據具體需求調整配置。
- 如果遇到任何問題，請檢查瀏覽器控制台中的錯誤訊息，並相應地調整你的 JavaScript 程式碼。

遵循這些步驟，你應該能夠在 Jekyll 博客中從 Kramdown 切換到 Marked，並利用更好的 MathJax 支援來顯示數學公式。