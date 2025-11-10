---
audio: false
generated: true
lang: hant
layout: post
title: 重新定義中粗體段落樣式
translated: true
type: note
---

要將整個 `cvparagraph` 環境改為使用 `\mdseries` 而非 `\bodyfontlight`，您需要重新定義 `\paragraphstyle` 指令。請在載入 awesome-cv 類別後，將以下代碼加入您的導言區：

```latex
\renewcommand*{\paragraphstyle}{\fontsize{11pt}{1em}\mdseries\upshape\color{text}}
```

這會將段落樣式從：
- `\bodyfontlight`（細體字重）

更改為：
- `\mdseries`（中等字重，類似描述樣式）

如此一來，您的整個 `cvparagraph` 環境就會像 `\descriptionstyle` 一樣使用中等字重的字體系列。