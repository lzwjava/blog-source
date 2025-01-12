---
audio: true
lang: hant
layout: post
title: Markdown 问题：Kramdown 与 XeLaTeX
---

为了使用Markdown为我的Jekyll博客生成PDF，我使用以下Pandoc命令：

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

支持Kramdown与XeLaTeX

在编写需要同时适用于kramdown（用于Jekyll生成HTML）和XeLaTeX（通过Pandoc生成PDF）的Markdown时，有几点需要注意：

1. 图片路径兼容性
	•	Kramdown (HTML): 倾向于使用以 / 开头的路径来引用资源。
	•	XeLaTeX (PDF): 倾向于使用不带前导 / 的相对路径。

解决方案：使用适用于两者的相对路径

```
![](assets/images/chatgpt/block.jpg)
```

2. 处理kramdown属性
	•	{:.responsive} 是kramdown特有的，用于样式化HTML输出。
	•	XeLaTeX不支持这些属性，会抛出错误。

解决方案：移除用于生成PDF的Markdown中特定于kramdown的属性。例如：

<!-- Kramdown 專用 -->
```
![](assets/images/chatgpt/block.jpg){: .responsive }
```

<!-- 兼容兩者 -->
```
![](assets/images/chatgpt/block.jpg)
```

如果 `{:.responsive}` 对您的 Jekyll HTML 布局至关重要，可以考虑在网页输出时选择性添加，而在 PDF 生成过程中省略它。

雙重兼容性工作流程

1. 編寫Markdown內容時，盡量減少對kramdown特有功能的依賴。
2. 對於HTML中的高級樣式，直接在Jekyll模板中應用CSS類，而非在Markdown內聯使用。
3. 利用Pandoc選項控制PDF格式，同時保持Markdown的可移植性。

遵循这些实践，Markdown内容在Jekyll的HTML渲染与XeLaTeX的PDF生成之间保持兼容，确保了多格式出版流程的无缝衔接。