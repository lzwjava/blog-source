---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 停用 Ghostty 的響鈴通知
translated: true
type: note
---

### 什麼是 Ghostty 的「通知標籤」？

在 Ghostty（一款 GPU 加速的終端機模擬器）中，「通知標籤」很可能指的是視覺鈴聲通知功能。當終端機中運行的指令或應用程式發送鈴聲字元（`\a`）時（例如來自長時間運行的進程或錯誤），Ghostty 可以在受影響的標籤或視窗標題前加上鈴聲表情符號（🔔）。這是一個微妙的提醒，旨在將你的注意力拉回該標籤，特別是當終端機未處於焦點狀態或你正在其他標籤中工作時。這是 Ghostty 鈴聲處理系統的一部分，旨在提供非侵入式通知，而不僅僅依賴音頻或系統彈出視窗。

此行為在 `bell-features` 配置下預設啟用，特別是 `title` 選項。它對於像背景作業完成這樣的工作流程很有幫助，但在標籤欄中可能會被視為不必要的「通知」。

### 如何停用它

要取消或停用此鈴聲標題通知（以及可能的其他鈴聲行為），請編輯你的 Ghostty 配置檔案。預設位置在 Linux 上是 `~/.config/ghostty/config`，在 macOS 上是 `~/Library/Application Support/com.mitchellh.Ghostty/config`。

1. 在你喜歡的編輯器中開啟配置檔案。
2. 新增或修改以下行以專門停用標題表情符號（同時保留其他鈴聲功能，如注意力請求）：
   ```
   bell-features = no-title
   ```
   - 這會從標籤標題中移除 🔔，但允許其他鈴聲效果（例如系統音頻或視窗高亮顯示）。

3. 要更徹底地停用（無標題表情符號、無注意力請求等），請使用：
   ```
   bell-features = false
   ```
   - 這會完全關閉所有鈴聲功能。

4. 儲存檔案並在 Ghostty 中重新載入配置：
   - 按下 `Cmd/Ctrl + Shift + ,`（或在另一個終端機中執行 `ghostty --reload-config`）。
   - 新視窗/標籤將使用更新後的設定；現有的視窗/標籤可能需要重啟。

如果這不是你指的具體通知（例如，如果是應用程式內部的彈出提示，如「已複製到剪貼簿」或來自應用程式的桌面通知），你也可以停用它們：
- 對於應用程式內部提示（僅限 Linux GTK）：`app-notifications = false`
- 對於來自終端機應用程式的桌面通知：`desktop-notifications = false`

透過執行觸發鈴聲的指令進行測試，例如 `echo -e '\a'`。

[Ghostty 配置參考](https://ghostty.org/docs/config/reference)  
[Ghostty 鈴聲功能討論](https://github.com/ghostty-org/ghostty/discussions/3242)