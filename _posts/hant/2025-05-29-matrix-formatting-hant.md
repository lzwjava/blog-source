---
audio: false
generated: true
lang: hant
layout: post
title: 修復 Jekyll 部落格的矩陣格式
translated: true
type: note
---

您遇到的問題與 Markdown（kramdown）在 MathJax 渲染內容前的處理方式有關。您矩陣中的雙反斜線（`\\`）在 MathJax 處理之前，先被 Markdown 解讀了，這導致矩陣格式被破壞。

以下提供幾種解決方案：

### 解決方案 1：跳脫反斜線
您可以使用另一個反斜線來跳脫每個反斜線：

```latex
$A - I = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\\ 0 & 1 & 0 \\\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\\ 2 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$
```

### 解決方案 2：在數學區塊內使用 `\\`
對於展示型數學（非行內數學），請使用 `$$` 或 `\\\[ \\\]`：

```latex
$$
A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
```

### 解決方案 3：使用 HTML 標籤防止 Markdown 處理
將您的數學內容包裹在 HTML `div` 標籤中，以防止 Markdown 處理：

```html
<div>
$$
A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
</div>
```

### 解決方案 4：修改您的 kramdown 配置
在您的 `_config.yml` 中加入以下設定，以防止 kramdown 處理數學區塊：

```yaml
kramdown:
  math_engine: mathjax
  syntax_highlighter: rouge
```

然後您可以使用：

```latex
$$ A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
```

請逐一嘗試這些解決方案，看看哪一種最適合您的 Jekyll 設定。通常最可靠的方法是對矩陣和其他複雜方程式使用展示型數學（`$$` 或 `\\\[ \\\]`），而不是行內數學（`$`）。