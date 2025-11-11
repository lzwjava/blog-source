---
audio: false
generated: true
lang: hant
layout: post
title: Markdown 數學公式渲染
translated: true
type: note
---

要在網頁上結合 LaTeX 數學渲染與 **Markdown** 渲染，通常需要使用 JavaScript 函式庫（如 **MathJax** 或 **KaTeX**）搭配能處理標準 Markdown 語法的解析器。目標是讓使用者能在 Markdown 中編寫 LaTeX 數學公式，並在頁面上正確渲染。

以下是實現方法：

### 1. **使用 MathJax 或 KaTeX 進行 Markdown 渲染**

您可以使用 **Markdown 解析器**（如 **marked.js** 或 **remarkable.js**）來渲染基礎 Markdown 內容，接著在渲染完成後，使用 MathJax 或 KaTeX 來渲染其中的 LaTeX 數學公式。

以下是逐步實現方法。

---

### **步驟 1：引入函式庫**

您需要在 HTML 檔案中同時引入 **Markdown 解析器**和**數學渲染函式庫**（MathJax 或 KaTeX）。

引入方式如下：

```html
<!-- 引入 KaTeX（或 MathJax）進行 LaTeX 渲染 -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.css">
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.js"></script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/contrib/auto-render.min.js"></script>

<!-- 引入 Markdown 解析器（如 marked.js） -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.0.10/marked.min.js"></script>
```

若您偏好使用 **MathJax** 而非 KaTeX，可以這樣引入：

```html
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

---

### **步驟 2：設定 Markdown 轉 LaTeX 的渲染流程**

現在，您可以編寫 HTML 結構，並使用 JavaScript 來渲染 Markdown，然後處理 Markdown 中的 LaTeX 公式。

以下是一個簡單範例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Markdown + Math Rendering</title>

  <!-- 引入 KaTeX 進行數學渲染 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/contrib/auto-render.min.js"></script>

  <!-- 引入 marked.js 進行 Markdown 渲染 -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.0.10/marked.min.js"></script>
</head>
<body>

  <h1>Markdown + Math Rendering Example</h1>

  <!-- 用於輸入 Markdown 的文字區域 -->
  <textarea id="markdownInput" rows="10" cols="50">
這是一個 Markdown 編輯器。您可以加入 LaTeX 數學公式，例如：

行內數學：\( E = mc^2 \)

區塊數學：
\[
\int_0^1 x^2 \, dx = \frac{1}{3}
\]
  </textarea>

  <hr>

  <!-- 用於顯示渲染後 Markdown 的容器 -->
  <div id="markdownOutput"></div>

  <script>
    // 用於渲染 Markdown + 數學的函式
    function renderMarkdown() {
      // 取得輸入的 Markdown
      const markdownText = document.getElementById('markdownInput').value;

      // 渲染 Markdown 內容
      const htmlContent = marked(markdownText);

      // 將渲染後的 HTML 插入輸出 div
      document.getElementById('markdownOutput').innerHTML = htmlContent;

      // 使用 KaTeX 渲染 HTML 內容中的數學公式
      renderMathInElement(document.getElementById('markdownOutput'), {
        delimiters: [
          { left: "\\(", right: "\\)", display: false }, // 行內數學
          { left: "\\[", right: "\\]", display: true }   // 區塊數學
        ]
      });
    }

    // 在頁面載入時及使用者變更輸入時呼叫 renderMarkdown 函式
    renderMarkdown();
    document.getElementById('markdownInput').addEventListener('input', renderMarkdown);
  </script>
</body>
</html>
```

### **程式碼說明：**

1. **Markdown 解析：**
   - 使用 `marked.js` 函式庫將 `<textarea>` 中的輸入 Markdown 轉換為 HTML。Markdown 語法將被處理並轉換為 HTML，顯示在 `<div id="markdownOutput"></div>` 容器中。

2. **數學渲染：**
   - Markdown 中的 LaTeX 方程式（行內 `\( ... \)` 與區塊 `\[ ... \]`）使用 **KaTeX** 的 `renderMathInElement()` 函式進行渲染。
   - **KaTeX** 會在 HTML 內容中尋找 `\( ... \)`（行內數學）和 `\[ ... \]`（區塊數學）並自動渲染它們。

3. **互動式 Markdown 編輯器：**
   - 當使用者在 `<textarea>` 中輸入時，會呼叫 `renderMarkdown` 函式來動態更新內容，解析 Markdown 並渲染 LaTeX 公式。

---

### **步驟 3：針對不同前端框架進行客製化**

您可以將此解決方案調整適用於任何前端框架，如 **React**、**Vue** 或 **Angular**。以下是一個 **React** 實現即時 Markdown + LaTeX 渲染的範例：

#### **React 範例**

1. **透過 npm 安裝 KaTeX 與 marked：**

```bash
npm install katex marked
```

2. **用於 Markdown + 數學渲染的 React 元件：**

```jsx
import React, { useState, useEffect } from 'react';
import marked from 'marked';
import katex from 'katex';
import 'katex/dist/katex.min.css';

const MarkdownEditor = () => {
  const [markdown, setMarkdown] = useState('');

  useEffect(() => {
    // 在元件掛載後使用 KaTeX 渲染數學公式
    renderMath();
  }, [markdown]);

  const renderMath = () => {
    const renderedHTML = marked(markdown);
    document.getElementById('markdownOutput').innerHTML = renderedHTML;

    // 使用 KaTeX 渲染 LaTeX 數學公式
    katex.renderMathInElement(document.getElementById('markdownOutput'), {
      delimiters: [
        { left: "\\(", right: "\\)", display: false }, // 行內數學
        { left: "\\[", right: "\\]", display: true }   // 區塊數學
      ]
    });
  };

  return (
    <div>
      <h1>Markdown + Math Rendering</h1>
      <textarea
        value={markdown}
        onChange={(e) => setMarkdown(e.target.value)}
        rows="10"
        cols="50"
      />
      <hr />
      <div id="markdownOutput"></div>
    </div>
  );
};

export default MarkdownEditor;
```

在 React 版本中，我們使用 `marked` 函式庫將 Markdown 文字轉換為 HTML，並使用 KaTeX 的 `renderMathInElement()` 函式來處理和渲染 HTML 中的 LaTeX 數學公式。

---

### **總結**
- 使用 **Markdown 解析器**（如 `marked.js`）將 Markdown 語法轉換為 HTML。
- 使用 **MathJax** 或 **KaTeX** 來渲染嵌入在 Markdown 內容中的 LaTeX 數學表達式。
- 結合兩者：將 Markdown 渲染為 HTML，並使用 KaTeX/MathJax 動態處理數學公式。

這種方法讓使用者能夠即時編寫和預覽包含數學方程式的 Markdown 內容，非常適用於部落格編輯器、知識庫系統或教育工具等應用場景！