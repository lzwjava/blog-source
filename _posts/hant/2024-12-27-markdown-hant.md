---
audio: false
generated: false
lang: hant
layout: post
title: Markdown 問題：Kramdown 與 XeLaTeX
translated: true
---

要為我的 Jekyll 博客使用 Markdown 生成 PDF，我使用以下 Pandoc 命令：

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

### 支持 Kramdown 和 XeLaTeX

在編寫需要與 kramdown（用於 Jekyll HTML 輸出）和 XeLaTeX（用於通過 Pandoc 生成 PDF 輸出）兼容的 Markdown 時，有幾點需要注意：

1. **圖片路徑兼容性**
   - **Kramdown (HTML)**：偏好以 `/` 開頭的路徑來引用資源。
   - **XeLaTeX (PDF)**：偏好沒有前導 `/` 的相對路徑。

**解決方案**：使用對兩者都有效的相對路徑：

```
![](assets/images/chatgpt/block.jpg)
```

2. **處理 kramdown 屬性**
   - `{:.responsive}` 是 kramdown 特有的，用於樣式化 HTML 輸出。
   - XeLaTeX 不支持這些屬性，會拋出錯誤。

**解決方案**：在為 PDF 生成而編寫的 Markdown 中移除 kramdown 特有的屬性。例如：

<!-- Kramdown-specific -->
```
![](assets/images/chatgpt/block.jpg){: .responsive }
```

<!-- Compatible with both -->
```
![](assets/images/chatgpt/block.jpg)
```

如果 `{:.responsive}` 對你的 Jekyll HTML 佈局至關重要，考慮在網頁輸出時選擇性添加，而在 PDF 生成過程中省略它。

### 雙重兼容的工作流程

1. **編寫 Markdown 內容**，盡量減少對 kramdown 特有功能的依賴。
2. **對於 HTML 中的高級樣式**，直接在 Jekyll 模板中應用 CSS 類，而不是在 Markdown 中內聯使用。
3. **使用 Pandoc 選項** 來控制 PDF 格式，同時保持 Markdown 的可移植性。

通過遵循這些實踐，Markdown 內容在 Jekyll HTML 渲染和 XeLaTeX PDF 生成之間保持兼容，確保多格式出版的無縫工作流程。