---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hant
layout: post
title: 選擇正確的 IntelliJ 版本
translated: true
type: note
---

從你的 `uname -a` 輸出：

```
Linux to 6.8.0-60-generic ... x86_64 x86_64 x86_64 GNU/Linux
```

其中的 `x86_64` 表示你的 CPU 架構是 **64 位元 Intel/AMD (x86-64)**，而非 ARM。

因此當下載 IntelliJ IDEA（或任何 JetBrains IDE）時，你應該選擇 **Linux (x64 / x86-64)** 版本，而不是 ARM64 版本。

**Linux ARM64** 版本僅適用於搭載 ARM 處理器的裝置（例如 Apple Silicon Mac、某些新款伺服器或 ARM 筆記型電腦）。

👉 簡而言之：

* **你的機器** → `x86_64` → 使用 **Linux x64**
* **非你的機器** → ARM 晶片（M1/M2 Mac、某些 ARM 伺服器）→ 使用 **Linux ARM64**

需要我同時示範一個快速指令來雙重確認你的 CPU 類型嗎（例如 `lscpu` 或 `arch`）？這樣你就能百分百確定了。