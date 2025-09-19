---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 使用庫時考慮升級
translated: true
---

在我的初創項目[Fun Live](https://github.com/lzwjava/live-server)中，我使用了CodeIgniter。雖然項目已經結束，但幾年後，我想重啟它以作紀念。然而，2016年時我使用的是CodeIgniter 3，而現在的最新版本是CodeIgniter 4。

升級過程相當麻煩，因為我的代碼與CodeIgniter框架緊密耦合。根據[CodeIgniter 4升級指南](https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html)顯示，更新代碼庫需要付出相當大的努力。

這次經歷給了我一個重要的教訓：在編寫代碼時，我們應該仔細考慮如何處理未來的更新。關鍵是要思考我們控制代碼的哪些部分，以及哪些部分是由第三方依賴控制的。