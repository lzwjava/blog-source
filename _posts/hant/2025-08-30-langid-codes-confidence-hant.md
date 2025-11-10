---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 語言識別代碼與置信度
translated: true
type: note
---

在 `langid` 中，`classify(text)` 函數會返回一個元組 `(lang, confidence)`，其中：

* **`lang`** 是兩個字母的 ISO 639-1 語言代碼（有時會擴展包含區域代碼，例如 `zh-cn` 或 `zh-tw`）。
* **`confidence`** 是介於 0 到 1 之間的浮點數，表示模型的置信度。

`lang` 的可能值集合來自 `langid.py` 支援的語言。預設情況下包含 **97 種語言**。一些常見範例：

* `en` → 英文
* `zh` / `zh-cn` / `zh-tw` → 中文（通用 / 簡體 / 繁體）
* `ja` → 日文
* `ko` → 韓文
* `fr` → 法文
* `de` → 德文
* `es` → 西班牙文
* `hi` → 印地文
* `ar` → 阿拉伯文
* `ru` → 俄文

以及其他許多語言——完整列表涵蓋了大多數世界主要語言（南非荷蘭文、孟加拉文、希臘文、希伯來文、意大利文、葡萄牙文、斯瓦希里文、泰文、土耳其文、越南文等）。

👉 如果你需要，我可以提供 `langid` 支援的 **97 種代碼完整列表**。需要我輸出嗎？