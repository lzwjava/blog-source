---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 恢復 zsh 中已暫停的工作
translated: true
type: note
---

要恢復一個暫停的工作（例如你使用 Ctrl+Z 暫停的 `bundle exec jekyll serve --incremental` 指令），請在 Ghostty 的同一個 zsh 終端機工作階段中按照以下步驟操作：

1. 列出所有背景/暫停的工作以確認它存在：
   ```
   jobs
   ```
   這會顯示類似 `[1]+  Suspended  bundle exec jekyll serve --incremental` 的內容。

2. 在前景中恢復它（它將再次接管你的終端機）：
   ```
   fg
   ```
   - 如果你有多個工作，請使用 `fg %1` 指定你想要的那個（將 `1` 替換為 `jobs` 輸出中的工作編號）。

如果你想改為在背景中運行它（以便在它運行的同時你可以使用終端機做其他事情），請使用 `bg %1`（同樣使用工作編號）。

恢復後，Jekyll 應該會從中斷的地方繼續運行，前提是沒有遇到重大中斷。如果程序似乎卡住或出錯，你可能需要使用 `kill %1` 終止它並重新啟動。