---
audio: false
generated: true
lang: ja
layout: post
title: JekyllでのKaTeXの利用
translated: true
type: note
---

現在のセットアップで Jekyll の数式レンダリングに MathJax の代わりに KaTeX を使用するには、MathJax スクリプトを KaTeX に置き換え、Jekyll の設定を調整する必要があります。KaTeX は MathJax よりも高速で軽量ですが、MathJax のすべての機能をサポートしているわけではないため（例えば、自動的な数式番号付けはより手動での操作が必要です）、異なるアプローチが必要です。以下に、Jekyll サイトで KaTeX に切り替えるためのステップバイステップガイドを示します：

### 1. Jekyll の設定を更新する
`_config.yml` を修正して、Kramdown の数式エンジンとして KaTeX を使用するようにします。`kramdown` セクションを以下のように更新します：

```yaml
kramdown:
  math_engine: katex
  input: GFM
  syntax_highlighter: rouge
```

これにより、Kramdown は MathJax の代わりに KaTeX を使用して LaTeX の数式をレンダリングするようになります。

### 2. HTML に KaTeX を含める
HTML から MathJax スクリプトを削除し、KaTeX に置き換えます。CDN 経由で KaTeX を含めることができます。Jekyll のレイアウトファイル（例： `_layouts/default.html`）の `<head>` セクションに以下を追加します：

```html
<!-- KaTeX CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" integrity="sha384-nB0miv6/jRmo5SLY8cTjmnkA3wC7o1L0jOey4Cki5N3kdjdPD/mW59G1Qsxa8c3y" crossorigin="anonymous">

<!-- KaTeX JS -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" integrity="sha384-7zkKLzPD3M4y9W8FWsN4Z0yO5eLu8qUn0QHY6hZ2r3fDzqjk0McYc3vJrmE2h6cZ" crossorigin="anonymous"></script>

<!-- Auto-render extension (オプション、数式の自動レンダリング用) -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" integrity="sha384-43gviWU0YVjaDtb/GhzOouOXtZMP/7XUzwPTL0xF3iS9Ho94fSc31UyUyIDgWvB4" crossorigin="anonymous"></script>

<!-- Auto-render 設定 -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: "$$", right: "$$", display: true}, // ブロック数式
        {left: "\\[", right: "\\]", display: true}, // ブロック数式
        {left: "\\(", right: "\\)", display: false}, // インライン数式
        {left: "$", right: "$", display: false} // インライン数式
      ],
      throwOnError: false
    });
  });
</script>
```

### 3. MathJax の設定を削除する
レイアウトファイルから、`<script type="text/x-mathjax-config">` ブロックや MathJax CDN スクリプトなど、MathJax 関連のコードを削除します。KaTeX は MathJax の `tex2jax` のような設定を使用せず、上記の auto-render スクリプトが同様の機能を処理します。

### 4. Markdown で数式を記述する
KaTeX と Kramdown が設定されると、以前と同じ区切り文字を使用して Markdown ファイルで LaTeX 数式を記述できます：

- **インライン数式**: `$...$` または `\(...\)` を使用します（例： `$E=mc^2$` または `\(E=mc^2\)`）。
- **ディスプレイ数式**: `$$...$$` または `\[...\]` を使用します（例： `$$E=mc^2$$` または `\[E=mc^2\]`）。

例：

```markdown
インライン数式: $E=mc^2$ または \(E=mc^2\).

ディスプレイ数式:
$$E=mc^2$$

または

\[E=mc^2\]
```

Kramdown と KaTeX 数式エンジンは、これらを KaTeX がレンダリングする HTML に処理します。

### 5. KaTeX と MathJax に関する注意点
- **自動的な数式番号付け**: KaTeX は MathJax の `autoNumber: "AMS"` のような自動的な数式番号付けをサポートしていません。数式番号が必要な場合は、LaTeX コード内で `\tag{}` を使用して手動で追加する必要があります（例： `$$E=mc^2 \tag{1}$$`）。
- **パフォーマンス**: KaTeX は MathJax よりも大幅に高速であり、Jekyll のような静的サイトに理想的です。
- **機能セット**: KaTeX は MathJax よりもサポートする LaTeX コマンドが少なくなっています。使用する数式が互換性があることを確認するために、[KaTeX がサポートする関数](https://katex.org/docs/supported.html)を確認してください。
- **レンダリング**: 上記の auto-render スクリプトは、指定された区切り文字内の数式を自動的にレンダリングすることで、MathJax の動作を模倣します。区切り文字を変更または制限したい場合は、スクリプト内の `delimiters` 配列を調整してください。

### 6. セットアップをテストする
Jekyll サイトをローカルで実行し（`jekyll serve`）、数式が正しくレンダリングされることを確認してください。問題が発生した場合：
- ブラウザのコンソールで KaTeX 関連のエラーを確認してください。
- KaTeX CDN の URL が最新であることを確認してください（上記のものは、この文書作成時点の最新版であるバージョン 0.16.11 を使用しています）。
- Markdown ファイルが有効な KaTeX 互換の LaTeX 構文を使用していることを確認してください。

### 7. オプション：ローカルの KaTeX ファイル
CDN への依存を避けるために、KaTeX ファイルをローカルでホストしたい場合：
1. [KaTeX GitHub リリース](https://github.com/KaTeX/KaTeX/releases) から `katex.min.css`, `katex.min.js`, `auto-render.min.js` をダウンロードします。
2. それらを Jekyll のアセットフォルダ（例： `assets/katex/`）に配置します。
3. `<link>` タグと `<script>` タグをローカルファイルを指すように更新します（例： `/assets/katex/katex.min.css`）。

### 8. トラブルシューティング
- **数式がレンダリングされない**: KaTeX スクリプトが正しく読み込まれていること、および `kramdown.math_engine` が `katex` に設定されていることを確認してください。
- **区切り文字の問題**: auto-render スクリプト内の区切り文字が Markdown 内のものと一致していることを確認してください。
- **サポートされていないコマンド**: LaTeX コマンドが失敗する場合は、KaTeX のドキュメントでサポートされているコマンドを確認するか、数式を書き直してください。

特定の数式や設定に関する具体的なヘルプが必要な場合は、詳細を共有していただければ、具体的なガイダンスを提供できます！