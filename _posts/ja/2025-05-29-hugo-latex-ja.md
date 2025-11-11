---
audio: false
generated: true
lang: ja
layout: post
title: HugoにおけるLaTeXレンダリング
translated: true
type: note
---

あなたが説明している問題は、**Jekyll** で **Kramdown** を **MathJax** を数式エンジンとして使用する際に発生します。Kramdown は `math_engine: mathjax` で設定されていると、Markdown コンテンツ内の括弧 `( )` をインライン数式の LaTeX 区切り文字（例: `\( \)`）として解釈し、括弧を含む通常のテキストを壊す可能性があります。これは、あなたの設定で示されているように、MathJax がインライン数式用に `\( \)` または `$ $` を解析するように設定されているためです。

**Hugo** では、この問題はデフォルトでは発生しにくいですが、Hugo の Markdown プロセッサと MathJax 統合の設定方法に依存します。以下では、Hugo がほとんどの場合でこの問題を回避する理由、Jekyll でそれを防止または修正する方法、そして Hugo で発生しないようにする方法を説明します。

---

### **Hugo はこの問題を抱えているか？**
Hugo は通常、この問題を回避します。なぜなら：
1.  **Markdown プロセッサ**: Hugo はデフォルトの Markdown レンダラーとして **Goldmark**（またはオプションで Blackfriday）を使用します。これらはデフォルトでは MathJax や LaTeX のパーシングを有効にしません。Hugo に MathJax を使用するように明示的に設定し、`\( \)` のようなインライン数式の区切り文字を設定しない限り、コンテンツ内の通常の括弧 `( )` は LaTeX として誤解釈されません。
2.  **MathJax 統合**: Hugo はネイティブで LaTeX をパースしません。MathJax サポートが必要な場合は、MathJax スクリプト（あなたが提供したものなど）をテーマのテンプレート（例: `layouts/partials/head.html`）に手動で追加し、区切り文字を設定する必要があります。Hugo の柔軟性により、MathJax がコンテンツを処理する方法を制御でき、明示的に有効にしない限り `( )` の自動パーシングを回避できます。
3.  **数式用ショートコード**: Hugo ユーザーは、多くの場合、ショートコード（例: `{{< math >}}...{{< /math >}}`）を使用して LaTeX レンダリングを実装します。これにより、数式コンテンツが明示的に指定されるため、通常の括弧が LaTeX と間違えられるのを防ぎます。

要約すると、Hugo は、同じインライン区切り文字 (`\( \)`) で MathJax を設定し、適切な安全策なしで自動パーシングを有効にしない限り、この問題は発生しません。ショートコードを使用するか、区切り文字として `\( \)` を使用することを避けることで、Hugo はこの問題を完全に回避できます。

---

### **Jekyll での問題の修正**
Jekyll では、Kramdown の `math_engine: mathjax` 設定とあなたの MathJax 設定が組み合わさり、`( )` が LaTeX としてパースされることで問題が発生します。修正方法は以下の通りです：

#### **1. MathJax のインライン区切り文字を変更する**
MathJax の設定を変更して、通常の括弧との競合を避けるために、`\( \)` の代わりに `$ $` のような異なるインライン数式の区切り文字を使用します。Jekyll サイトの HTML（例: `_includes/head.html`）内のスクリプトを更新してください：

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [['$','$']], // インライン数式に $ $ を使用
      displayMath: [['$$','$$'], ['\[','\]']],
      processEscapes: true // $ をエスケープしてリテラルとして使用できるようにする
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": { linebreaks: { automatic: true } },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```

-   **なぜ動作するのか**: `inlineMath` から `['\(','\)']` を削除することで、MathJax は `( )` を LaTeX 区切り文字として解釈しなくなり、通常のテキスト用に保持します。`processEscapes: true` 設定により、必要に応じて Markdown 内で `\$` と書いてリテラルの `$` を表示できるようになります。
-   **Markdown 内での使用**: インライン数式に `\(x^2\)` の代わりに `$x^2$` を使用します。例：
    ```markdown
    これは数式です: $x^2 + y^2 = z^2$。通常のテキスト (パースされない)。
    ```

#### **2. Markdown 内の括弧をエスケープする**
`\( \)` を区切り文字として維持したい場合は、Markdown コンテンツ内の括弧をエスケープして、Kramdown/MathJax がそれらを LaTeX としてパースするのを防ぎます。各括弧の前にバックスラッシュ `\` を使用します：

```markdown
通常のテキスト \(数式ではない\)。これは本当の数式です: \(x^2 + y^2\)。
```

-   **出力**: エスケープされた `\(not a formula\)` は `(not a formula)` としてレンダリングされ、`\(x^2 + y^2\)` は LaTeX 数式としてレンダリングされます。
-   **欠点**: コンテンツ内の `( )` のすべてのインスタンスを手動でエスケープする必要があり、面倒です。

#### **3. 特定のページで MathJax を無効にする**
特定のページ（例: 数学が多い投稿）でのみ MathJax が必要な場合は、デフォルトでは無効にし、必要な場合にのみ有効にします：
-   グローバルな `_layouts/default.html` または `_includes/head.html` から MathJax スクリプトを削除します。
-   レイアウトまたはページのフロントマターに条件付きインクルードを追加します。例: `_layouts/post.html` 内：

```html
{% if page.mathjax %}
  <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      tex2jax: {
        inlineMath: [['$','$']],
        displayMath: [['$$','$$'], ['\[','\]']],
        processEscapes: true
      }
    });
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
{% endif %}
```

-   特定のページでのみ MathJax を有効にするには、Markdown ファイルのフロントマターに以下を追加します：
    ```yaml
    ---
    title: 私の数学の投稿
    mathjax: true
    ---
    ```

-   **なぜ動作するのか**: `mathjax: true` がないページは MathJax を読み込まないため、`( )` は LaTeX としてパースされません。

#### **4. 別の数式エンジンを使用する**
MathJax から、Kramdown がサポートする別の数式エンジン、例えば **KaTeX** に切り替えます。KaTeX は高速で、明示的に設定しない限り括弧を誤解釈しにくいです。Jekyll サイトに KaTeX をインストールします：
-   `_includes/head.html` に KaTeX スクリプトを追加します：
    ```html
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/auto-render.min.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false }
          ]
        });
      });
    </script>
    ```
-   `_config.yml` を更新します：
    ```yaml
    kramdown:
      math_engine: katex
      input: GFM
      syntax_highlighter: rouge
    ```

-   **なぜ動作するのか**: KaTeX はパーシングに関してより厳格で、インライン数式にはデフォルトで `$ $` を使用するため、`( )` との競合が減少します。また、MathJax よりも高速です。

---

### **Hugo でこの問題を回避するための確認**
Hugo で MathJax を使用する際に `( )` のパーシング問題に遭遇しないようにするには、以下の手順に従ってください：

1.  **Hugo に MathJax を追加する**:
    -   MathJax スクリプトをテーマのパーシャル（例: `layouts/partials/head.html`）に配置します：
        ```html
        {{ if .Params.mathjax }}
        <script type="text/x-mathjax-config">
          MathJax.Hub.Config({
            tex2jax: {
              inlineMath: [['$','$']],
              displayMath: [['$$','$$'], ['\[','\]']],
              processEscapes: true
            },
            "HTML-CSS": { linebreaks: { automatic: true } },
            "CommonHTML": { linebreaks: { automatic: true } },
            TeX: { equationNumbers: { autoNumber: "AMS" } }
          });
        </script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
        {{ end }}
        ```
    -   特定のページで MathJax を有効にするには、フロントマターに追加します：
        ```yaml
        ---
        title: 私の数学の投稿
        mathjax: true
        ---
        ```

2.  **数式用にショートコードを使用する**:
    数式コンテンツを明示的にラップするためのショートコード（例: `layouts/shortcodes/math.html`）を作成します：
    ```html
    {{ if .IsNamedParams }}
      <span class="math">{{ .Get "content" | safeHTML }}</span>
    {{ else }}
      <span class="math">{{ .Inner | safeHTML }}</span>
    {{ end }}
    ```
    これをあなたの Markdown で使用します：
    ```markdown
    通常のテキスト (パースされない)。数式: {{< math >}}$x^2 + y^2${{< /math >}}。
    ```
    -   **なぜ動作するのか**: ショートコードは、明示的にマークされたコンテンツのみが数式として処理されることを保証し、通常のテキスト内の `( )` をそのままにします。

3.  **代わりに KaTeX を使用する**:
    Hugo ユーザーはその速度から KaTeX を好むことが多いです。`layouts/partials/head.html` に KaTeX を追加します：
    ```html
    {{ if .Params.math }}
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/auto-render.min.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false }
          ]
        });
      });
    </script>
    {{ end }}
    ```
    フロントマターで有効にします：
    ```yaml
    math: true
    ```
    `( )` の競合を避けるために、インライン数式に `$ $` を使用します。

---

### **推奨事項**
-   **Jekyll の場合**: `( )` のパーシング問題を避けるために、MathJax の区切り文字を `$ $` に切り替えるか、KaTeX を使用してください。括弧のエスケープは、大規模なサイトでは実用的ではないため、代替手段としてください。
-   **Hugo の場合**: MathJax を `\( \)` 区切り文字で明示的に設定しない限り、この問題に遭遇する可能性は低いです。通常の括弧が安全であることを保証するために、数式レンダリングにはショートコードまたは KaTeX を使用してください。

Jekyll から Hugo に移行していて、数式コンテンツを維持したい場合は、Hugo でショートコードとともに KaTeX を使用して、明示的な制御を行うことをお勧めします。Hugo の MathJax/KaTeX 統合の設定や、Jekyll サイトの数式コンテンツの変換にヘルプが必要な場合は、お知らせください！