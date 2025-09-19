---
audio: false
generated: false
image: true
lang: ja
layout: post
title: 'Markdownの問題点: KramdownとXeLaTeX'
translated: true
---

私のJekyllブログでMarkdownを使ってPDFを生成するために、以下のPandocコマンドを使用しています:

```python
command = [
    'pandoc',
    input_markdown_path,
    '-o', output_pdf_path,
    '-f', 'markdown',
    '--pdf-engine', 'xelatex',
    '--resource-path=.:assets',
    '-V', f'CJKmainfont={CJK_FONT}',
    '-V', f'CJKsansfont={CJK_FONT}',
    '-V', f'CJKmonofont={CJK_FONT}',
    '-V', f'geometry:{GEOMETRY}',
    '-V', 'classoption=16pt',
    '-V', 'CJKoptions=Scale=1.1',
    '-V', 'linestretch=1.5'
]
```

KramdownとXeLaTeXの両方をサポート

kramdown（JekyllのHTML出力用）とXeLaTeX（Pandoc経由のPDF出力用）の両方で動作するMarkdownを書く際には、いくつかの考慮点があります:

1. 画像パスの互換性
	•	Kramdown (HTML): アセットを参照する際に、パスが `/` で始まることを好みます。
	•	XeLaTeX (PDF): 先頭に `/` のない相対パスを好みます。

解決策: 両方で動作する相対パスを使用する:

```
![](assets/images/chatgpt/block.jpg)
```

2. kramdown属性の扱い
	•	{:.responsive} は、HTML出力のスタイリングに特化したkramdownの機能です。
	•	XeLaTeXはこれらの属性をサポートしておらず、エラーが発生します。

解決策: PDF生成用のMarkdownからkramdown固有の属性を削除します。例えば:

```markdown
![](assets/images/chatgpt/block.jpg){: .responsive }
```

<!-- 両方に対応 -->
```
![](assets/images/chatgpt/block.jpg)
```

もし `{:.responsive}` があなたの Jekyll HTML レイアウトにとって重要である場合、ウェブ出力には選択的に追加しつつ、PDF 生成プロセスではそれを省略することを検討してください。

デュアル互換性のためのワークフロー

1. kramdown固有の機能への依存を最小限に抑えてMarkdownコンテンツを作成します。
2. HTMLでの高度なスタイリングには、Markdown内でインラインで適用するのではなく、Jekyllテンプレート内で直接CSSクラスを適用します。
3. Markdownの移植性を維持しながら、Pandocオプションを使用してPDFのフォーマットを制御します。

これらのプラクティスに従うことで、MarkdownコンテンツはJekyllのHTMLレンダリングとXeLaTeXによるPDF生成の両方で互換性を保ち、マルチフォーマット出版のためのシームレスなワークフローを確保します。