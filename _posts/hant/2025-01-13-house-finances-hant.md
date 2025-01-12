---
audio: true
lang: hant
layout: post
title: 追踪我们的家庭财务
---

最近，我创建了一份Markdown文档来记录我们家庭的财务交易情况。

房子是我和妻子共有的。我父母给了我们钱，我们还向我姐姐和舅舅借了钱。虽然舅舅把钱寄给了我，但我父亲后来还了这笔钱。

我们购房时支付了总房价的50%作为首付款，另外一半则向中国农业银行申请了贷款。贷款合同期限为20年，目前的贷款利率是3.65%。

在我失业期间，我的妻子和父亲为我提供了资金来支付每月的房贷。因此，涉及到了许多交易。

我主要使用招商银行作为我的主要银行。招商银行允许根据交易是收入还是支出以及最小金额进行筛选。它还支持通过关键词进行筛选，这非常有用。

另一个有帮助的方面是人工智能的普及。它也能协助完成这项任务。通过使用AI驱动的OCR技术，特别是Grok，我成功地从与广州电力局的交易记录中提取了文本。

由于后续表格是基于先前的数据构建的，最好先核对数据，确保一切准确无误后再继续推进。

以下代码有助于从Markdown生成PDF。它包含一些特殊设置，以支持PDF中的中文字符渲染。

```python
import os
import subprocess
```

# 配置
CJK_FONT = "黑体-简"  # 设置中文字体为黑体简体
GEOMETRY = "margin=1in"  # 设置页面边距为1英寸
input_markdown_path = "mortgage.md"  # 替换为你的输入Markdown文件路径
output_pdf_path = "mortgage.pdf"    # 替换为你期望的输出PDF文件路径

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

# 執行 Pandoc 命令
try:
    subprocess.run(command, check=True)
    print(f"PDF 成功生成: {output_pdf_path}")
except subprocess.CalledProcessError as e:
    print(f"生成 PDF 時出錯: {e}")
```