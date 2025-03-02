---
audio: false
generated: false
lang: ja
layout: post
title: 家計の追跡
translated: true
---

最近、家計の取引を記録するためにマークダウンのドキュメントを作成しました。

この家は妻と私のものです。私の両親からお金をもらい、姉と母方の叔父からもお金を借りました。母方の叔父は私にお金を送ってくれましたが、後で父がその金額を返済しました。

家の総額の50%を頭金として支払い、残りの半分は中国農業銀行から借り入れました。契約期間は20年で、現在の金利は3.65%です。

私が無職だった時、妻と父が毎月の住宅ローン支払いをカバーするための資金を提供してくれました。そのため、多くの取引が発生しています。

私は中国招商銀行をメインバンクとして使用しています。中国招商銀行では、入金か出金か、および最低金額で取引をフィルタリングすることができます。また、キーワードによるフィルタリングもサポートしており、非常に便利です。

もう一つの便利な点は、AIの普及です。AIもこの作業を支援できます。AIを活用したOCR、特にGrokを使用して、広州電力局との取引記録からテキストを抽出することができました。

後の表は前の数字に基づいているため、進む前に数字を確認してすべてが正しいことを確認する方が良いです。

以下のコードは、マークダウンからPDFを生成するのに役立ちます。PDFでの中国語文字のレンダリングをサポートするための特別な設定があります。

```python
import os
import subprocess

# 設定
CJK_FONT = "Heiti SC"
GEOMETRY = "margin=1in"
input_markdown_path = "mortgage.md"  # 入力マークダウンファイルに置き換えてください
output_pdf_path = "mortgage.pdf"    # 希望する出力PDFファイルに置き換えてください

# 入力ファイルが存在するか確認
if not os.path.exists(input_markdown_path):
    raise Exception(f"入力ファイルが存在しません: {input_markdown_path}")

# Pandocコマンドを構築
command = [
    'pandoc',
    input_markdown_path,
    '-o', output_pdf_path,
    '-f', 'markdown',
    '--pdf-engine', 'xelatex',
    '-V', f'CJKmainfont={CJK_FONT}',
    '-V', f'CJKsansfont={CJK_FONT}',
    '-V', f'CJKmonofont={CJK_FONT}',
    '-V', f'geometry:{GEOMETRY}',
    '-V', 'classoption=16pt',
    '-V', 'CJKoptions=Scale=1.1',
    '-V', 'linestretch=1.5'
]

# Pandocコマンドを実行
try:
    subprocess.run(command, check=True)
    print(f"PDFが正常に生成されました: {output_pdf_path}")
except subprocess.CalledProcessError as e:
    print(f"PDF生成中にエラーが発生しました: {e}")
```