---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Ghostty 視窗切換快捷鍵
translated: true
type: note
---

確實，在 Ghostty 中使用 Cmd + `（波浪號/反引號）來循環切換視窗，操作起來既流暢又直覺——特別當你把它們視為輕量級獨立工作階段使用，而非把所有內容塞進分頁時。這種循環流暢感完全避免了分頁列雜亂造成的思維負擔。相比之下，系統預設的 Cmd + Shift + [ / ] 分頁導航（或用 Cmd + [ / ] 切換窗格）在 Mac 上確實顯得笨重，畢竟要同時按住 Cmd 和 Shift，而且括號鍵的位置對手部來說也不夠友善。

你說得一點沒錯：對多數人而言，單手就能快速準確觸發的 Cmd + 單鍵組合確實更簡潔高效。Ghostty 的預設設定其實已考慮到這點（例如用 Cmd + 1–8 直接跳轉特定分頁），但如果你更偏愛視窗模式而非分頁，完全可以將循環切換映射到更簡潔的組合，例如 Cmd + J/K（Vim 風格）或 Cmd + ←/→ 來切換上/下個視窗。只要在設定檔加入幾行就能自訂：

```
keybind = "cmd-j", "window:previous"
keybind = "cmd-k", "window:next"
```

這樣就能維持單修飾鍵配單按鍵的極簡操作。你目前主要如何使用 Ghostty——是讓多個視窗散佈在不同桌面空間，還是全部固定在同個桌面上？如果有特定操作想綁定（例如快速窗格切換），我很樂意幫你構思更多調整方案。