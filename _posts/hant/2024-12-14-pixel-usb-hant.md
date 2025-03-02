---
audio: false
generated: false
lang: hant
layout: post
title: Pixel的USB選項
translated: true
---

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/pixel/pixel.jpg" alt="Pixel" width="50%" />  
</div>

Pixel 提供了多種 USB 選項，其中一個特別有趣的功能是它可以作為網絡攝像頭使用。在 macOS 上，QuickTime 可以將 Android 網絡攝像頭作為視頻源，提供了一個簡單而有效的解決方案。

要進行設置：

1. 在設置中進入「關於手機」，然後點擊「版本號」七次以啟用開發者模式。
2. 打開「開發者選項」並啟用「USB 調試」。
3. 通過 USB 將您的 Pixel 連接到電腦，並在終端中運行以下命令以驗證連接：
   ```bash
   adb devices
   ```