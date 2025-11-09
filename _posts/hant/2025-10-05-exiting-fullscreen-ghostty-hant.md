---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 退出 Ghostty 全螢幕模式
translated: true
type: note
---

在 Ubuntu 的 Ghostty 終端中退出全螢幕模式，請按 **Ctrl + Enter**。這是切換全螢幕模式的預設按鍵綁定。

若該方法無效（例如因自訂設定導致），可嘗試以下替代方案：
- 在終端視窗內右擊，從右鍵選單中尋找「離開全螢幕」或類似選項
- 若選單列可見：前往 **檢視 > 離開全螢幕**（可能需要將游標移至螢幕頂部以顯示選單）
- 最後手段：透過其他終端輸入 `ghostty` 重新開啟程式，或使用 `pkill ghostty` 終止程序後重啟

[ghostty-shortcuts.md](https://gist.github.com/hensg/43bc71c21d1f79385892352a390aa2ca)  
[Keybindings for Midnight Commander (Reddit)](https://www.reddit.com/r/Ghostty/comments/1lfxvsf/keybindings_for_midnight_commander/)