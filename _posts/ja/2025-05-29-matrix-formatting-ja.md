---
audio: false
generated: true
lang: ja
layout: post
title: Jekyllブログでのマトリックス表示の修正
translated: true
type: note
---

あなたが直面している問題は、Markdown（kramdown）が MathJax によるレンダリングの前にコンテンツを処理する方法に関連しています。行列内の二重バックスラッシュ（`\\`）は、MathJax が処理する前に Markdown によって解釈されるため、行列のフォーマットが崩れてしまいます。

これを修正するためのいくつかの解決策を以下に示します：

### 解決策 1: バックスラッシュをエスケープする
各バックスラッシュを別のバックスラッシュでエスケープできます：

```latex
$A - I = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\\ 0 & 1 & 0 \\\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\\ 2 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$
```

### 解決策 2: 数式ブロック内で `\\` を使用する
ディスプレイ数式（インラインではない）には、`$$` または `\\\[ \\\]` を使用します：

```latex
$$
A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
```

### 解決策 3: HTML タグを使用して Markdown の処理を防ぐ
数式を HTML の `div` タグで囲んで、Markdown の処理を防ぎます：

```html
<div>
$$
A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
</div>
```

### 解決策 4: kramdown の設定を変更する
`_config.yml` に以下を追加して、kramdown が数式ブロックを処理しないようにします：

```yaml
kramdown:
  math_engine: mathjax
  syntax_highlighter: rouge
```

その後、以下を使用できます：

```latex
$$ A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
```

これらの解決策を一つずつ試して、あなたの Jekyll 環境で最も効果的なものを見つけてください。行列やその他の複雑な数式には、インライン数式（`$`）ではなく、ディスプレイ数式（`$$` または `\\\[ \\\]`）を使用するのが一般的に最も信頼性の高い解決策です。