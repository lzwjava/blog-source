---
audio: false
lang: hant
layout: post
title: Ubuntu 安裝指南
translated: true
---

我之前曾經寫過[如何建立一台電腦](./computer-en)。讓我們試試不同的東西。今天，我在一台預裝了Windows 10的Lenovo 小新 14IAH8筆記本電腦上安裝Ubuntu 24.04。

```bash
sudo dd if=ubuntu-24.04.1-desktop-amd64.iso of=/dev/rdisk6 bs=1m
```

必須進入設定並禁用裝置加密，因為Ubuntu安裝程式需要它。

如果裝置加密已啟用且BIOS中的安全啟動已禁用，Windows會提示輸入BitLocker密碼以進行恢復。

因此，首先需要在BIOS中啟用安全啟動，登錄Windows，然後進入設定以禁用裝置加密。之後，可以再次禁用安全啟動以開始Ubuntu安裝程式。