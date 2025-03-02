---
audio: false
generated: false
lang: hant
layout: post
title: 追蹤我們的家庭財務
translated: true
---

最近，我創建了一個markdown文件來記錄我們房子的財務交易。

這房子屬於我和我妻子。我的父母給了我們錢，我們還向我姐姐和我的舅舅借了錢。雖然我的舅舅把錢轉給了我，但後來我父親還了那筆錢。

我們支付了房子總價的50%作為首付，另外一半是從中國農業銀行借的。合同期限為20年，目前的利率是3.65%。

當我失業時，我的妻子和父親提供了資金來支付每月的房貸。因此，涉及了許多交易。

我使用招商銀行作為我的主要銀行。招商銀行允許按交易是收入還是支出以及最小金額來過濾交易。它還支持按關鍵字過濾，這非常有幫助。

另一個有幫助的方面是AI的普及。它也可以協助完成這項任務。使用AI驅動的OCR，特別是Grok，我能夠從與廣州電力局的交易記錄中提取文本。

由於後面的表格是基於前面的數字，最好先檢查數字，確保一切正確，然後再繼續。

下面的代碼幫助從markdown生成PDF。它有一些特殊設置來支持PDF中的中文字符渲染。

```python
import os
import subprocess

# 配置
CJK_FONT = "Heiti SC"
GEOMETRY = "margin=1in"
input_markdown_path = "mortgage.md"  # 替換為你的輸入Markdown文件
output_pdf_path = "mortgage.pdf"    # 替換為你想要的輸出PDF文件

# 檢查輸入文件是否存在
if not os.path.exists(input_markdown_path):
    raise Exception(f"輸入文件不存在: {input_markdown_path}")

# 構建Pandoc命令
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

# 運行Pandoc命令
try:
    subprocess.run(command, check=True)
    print(f"PDF成功生成: {output_pdf_path}")
except subprocess.CalledProcessError as e:
    print(f"生成PDF時出錯: {e}")
```