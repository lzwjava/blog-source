---
audio: false
generated: true
lang: ja
layout: post
title: 中程度の太さの段落スタイルを再定義
translated: true
type: note
---

`cvparagraph` 環境全体を `\bodyfontlight` の代わりに `\mdseries` を使用するように変更するには、`\paragraphstyle` コマンドを再定義する必要があります。awesome-cv クラスを読み込んだ後、プリアンブルに以下を追加してください：

```latex
\renewcommand*{\paragraphstyle}{\fontsize{11pt}{1em}\mdseries\upshape\color{text}}
```

これにより、段落スタイルが以下から：
- `\bodyfontlight`（ライトウェイト）

以下へ変更されます：
- `\mdseries`（ミディアムウェイト、description スタイルと同様）

この方法により、`cvparagraph` 環境全体が `\descriptionstyle` と同様にミディアムウェイトのフォントシリーズを使用するようになります。