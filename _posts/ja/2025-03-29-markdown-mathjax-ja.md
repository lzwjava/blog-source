---
audio: false
generated: true
lang: ja
layout: post
title: MathJaxまたはKaTeXを用いたMarkdownレンダリング
translated: true
type: note
---

WebページでLaTeX数式レンダリングと**Markdown**レンダリングを組み合わせるには、通常、JavaScriptライブラリ（**MathJax**や**KaTeX**など）と、標準のMarkdown構文を処理できるMarkdownパーサーを併用します。目的は、ユーザーがMarkdown内でLaTeXで数式を記述し、ページ上で適切にレンダリングされるようにすることです。

以下に、これを実現する方法を示します。

### 1. **MathJaxまたはKaTeXを用いたMarkdownレンダリング**

基本的なMarkdownコンテンツをレンダリングするために、**marked.js**や**remarkable.js**などの**Markdownパーサー**を使用できます。Markdownコンテンツをレンダリングした後、MathJaxまたはKaTeXを使用してその中のLaTeX数式をレンダリングします。

以下に、これを実現するための段階的なアプローチを示します。

---

### **ステップ 1: ライブラリの読み込み**

HTMLファイルに、**Markdownパーサー**と**数式レンダリングライブラリ**（MathJaxまたはKaTeX）の両方を含める必要があります。

以下のようにしてそれらを含めることができます：

```html
<!-- LaTeXレンダリング用にKaTeX (または MathJax) を含める -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.css">
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.js"></script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/contrib/auto-render.min.js"></script>

<!-- Markdownパーサー (marked.jsなど) を含める -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.0.10/marked.min.js"></script>
```

あるいは、KaTeXの代わりに**MathJax**を希望する場合は、以下のようにMathJaxを含めることができます：

```html
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

---

### **ステップ 2: MarkdownからLaTeXへのレンダリングプロセスの設定**

次に、HTML構造を作成し、JavaScriptを使用してMarkdownをレンダリングし、そのMarkdown内のLaTeX数式を処理します。

以下は簡単な例です：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Markdown + Math Rendering</title>

  <!-- 数式レンダリング用にKaTeXを含める -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/contrib/auto-render.min.js"></script>

  <!-- Markdownレンダリング用にmarked.jsを含める -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.0.10/marked.min.js"></script>
</head>
<body>

  <h1>Markdown + 数式レンダリングの例</h1>

  <!-- Markdown入力用のテキストエリア -->
  <textarea id="markdownInput" rows="10" cols="50">
これはMarkdownエディタです。以下のようにLaTeX数式を追加できます：

インライン数式: \( E = mc^2 \)

ブロック数式:
\[
\int_0^1 x^2 \, dx = \frac{1}{3}
\]
  </textarea>

  <hr>

  <!-- レンダリングされたMarkdown用のコンテナ -->
  <div id="markdownOutput"></div>

  <script>
    // Markdown + 数式をレンダリングする関数
    function renderMarkdown() {
      // 入力されたMarkdownを取得
      const markdownText = document.getElementById('markdownInput').value;

      // Markdownコンテンツをレンダリング
      const htmlContent = marked(markdownText);

      // レンダリングされたHTMLを出力用のdivに挿入
      document.getElementById('markdownOutput').innerHTML = htmlContent;

      // KaTeXを使用してHTMLコンテンツ内の数式をレンダリング
      renderMathInElement(document.getElementById('markdownOutput'), {
        delimiters: [
          { left: "\\(", right: "\\)", display: false }, // インライン数式
          { left: "\\[", right: "\\]", display: true }   // ブロック数式
        ]
      });
    }

    // ページ読み込み時およびユーザーが入力を変更したときにrenderMarkdown関数を呼び出す
    renderMarkdown();
    document.getElementById('markdownInput').addEventListener('input', renderMarkdown);
  </script>
</body>
</html>
```

### **コードの説明:**

1. **Markdownのパース:**
   - `marked.js`ライブラリを使用して、`<textarea>`に入力されたMarkdownをHTMLに変換します。Markdown構文は処理され、`<div id="markdownOutput"></div>`コンテナ内でHTMLに変換されます。

2. **数式のレンダリング:**
   - Markdown内のLaTeX方程式（インライン `\( ... \)` およびブロック `\[ ... \]`）は、**KaTeX**の`renderMathInElement()`関数を使用してレンダリングされます。
   - **KaTeX**は、HTMLコンテンツ内のインライン数式用の `\( ... \)` とブロック数式用の `\[ ... \]` を探し、自動的にそれらをレンダリングします。

3. **インタラクティブなMarkdownエディタ:**
   - ユーザーが`<textarea>`に入力すると、`renderMarkdown`関数が呼び出され、Markdownの解析とLaTeX数式のレンダリングを行ってコンテンツが動的に更新されます。

---

### **ステップ 3: 異なるフロントエンドフレームワーク用のカスタマイズ**

このソリューションは、**React**、**Vue**、**Angular**などの任意のフロントエンドフレームワークで動作するように適応させることができます。例えば、以下はリアルタイムのMarkdown + LaTeXレンダリングのための**React**実装例です。

#### **Reactの例**

1. **npm経由でKaTeXとmarkedをインストール:**

```bash
npm install katex marked
```

2. **Markdown + 数式レンダリング用のReactコンポーネント:**

```jsx
import React, { useState, useEffect } from 'react';
import marked from 'marked';
import katex from 'katex';
import 'katex/dist/katex.min.css';

const MarkdownEditor = () => {
  const [markdown, setMarkdown] = useState('');

  useEffect(() => {
    // コンポーネントマウント後にKaTeXを使用して数式をレンダリング
    renderMath();
  }, [markdown]);

  const renderMath = () => {
    const renderedHTML = marked(markdown);
    document.getElementById('markdownOutput').innerHTML = renderedHTML;

    // KaTeXでLaTeX数式をレンダリング
    katex.renderMathInElement(document.getElementById('markdownOutput'), {
      delimiters: [
        { left: "\\(", right: "\\)", display: false }, // インライン数式
        { left: "\\[", right: "\\]", display: true }   // ブロック数式
      ]
    });
  };

  return (
    <div>
      <h1>Markdown + 数式レンダリング</h1>
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

Reactバージョンでは、`marked`ライブラリを使用してMarkdownテキストをHTMLに変換し、KaTeXの`renderMathInElement()`関数を使用してHTML内のLaTeX数式を処理およびレンダリングします。

---

### **まとめ**
- **Markdownパーサー**（`marked.js`など）を使用して、Markdown構文をHTMLに変換します。
- **MathJax**または**KaTeX**を使用して、Markdownコンテンツに埋め込まれたLaTeX数式をレンダリングします。
- MarkdownをHTMLにレンダリングし、KaTeX/MathJaxを使用して数式を動的に処理することで、両者を組み合わせます。

このアプローチにより、ユーザーはブログエディタ、ナレッジベースシステム、教育ツールなどのアプリケーションに最適な、数式を含むMarkdownコンテンツをリアルタイムで記述およびプレビューすることができます！