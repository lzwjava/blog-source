---
audio: false
generated: true
lang: hant
layout: post
title: 修復 LaTeX 撇號渲染問題
translated: true
type: note
---

您遇到的「HSBC's」中撇號顯示問題，很可能與 LaTeX 在 PDF 輸出中處理特定引號/撇號字符的方式有關。以下是幾種改善渲染效果的方法：

## 1. 使用正確的 LaTeX 撇號
將直撇號 (') 替換為標準的 LaTeX 撇號：
```latex
\item {透過 TEKsystems 外派至滙豐銀行的後端工程師，負責開發和優化滙豐企業科技部門中 \href{https://www.google.com/search?q=Finance+Transformation+Platform+HSBC}{Finance Transformation Platform} 的後端系統。}
```
改為：
```latex
\item {透過 TEKsystems 外派至滙豐銀行的後端工程師，負責開發和優化滙豐企業科技部門中 \href{https://www.google.com/search?q=Finance+Transformation+Platform+HSBC}{Finance Transformation Platform} 的後端系統。}
```

## 2. 使用 `\textquotesingle` 指令
```latex
HSBC\textquotesingle{}s
```

## 3. 採用 `\textasciigrave` 與 `\textquotesingle` 組合方案
```latex
HSBC\textquotesingle{}s
```

## 4. 添加 `textcomp` 套件
在導言區加入：
```latex
\usepackage{textcomp}
```
隨後使用：
```latex
HSBC\textquotesingle{}s
```

## 5. 採用 UTF-8 編碼（若未啟用）
確保文件使用 UTF-8 編碼：
```latex
\usepackage[utf8]{inputenc}
```

## 6. 嘗試使用 `babel` 套件提升排版品質
```latex
\usepackage[british]{babel}
```

## 最可靠解決方案：
為獲得最佳效果，建議採用反引號-撇號組合（這是 LaTeX 實現專業排版的傳統方式）：

```latex
\item {透過 TEKsystems 外派至滙豐銀行的後端工程師，負責開發和優化滙豐企業科技部門中 \href{https://www.google.com/search?q=Finance+Transformation+Platform+HSBC}{Finance Transformation Platform} 的後端系統。}
```

此方式能在 PDF 輸出中呈現具有正確間距和彎曲度的專業排版效果。反引號 (`) 後接撇號 (') 的組合，能為 LaTeX 中的所有格形式創造出最理想的視覺呈現。