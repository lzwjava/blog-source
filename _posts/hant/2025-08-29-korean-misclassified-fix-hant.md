---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 韓裔誤判為華裔驗證修正
translated: true
type: note
---

明白了 — 在這段除錯輸出中：

```
Debug: raw langdetect output: [('ko', 0.9999995211930662)]
...
Detected languages: [('ko', 0.9999995211930662)]
```

代碼 **`ko`** 是 **韓語** 的 ISO 639-1 語言代碼。 🇰🇷

所以 `langdetect` 的意思是：

* 它認為該文本是韓語（`ko`）
* 概率約為 **0.9999995**（基本上是 100%）

這就解釋了錯誤原因：你的驗證器預期是 `"zh-tw"`（繁體中文），但檢測器卻判定輸入內容看起來像韓語。

👉 快速複習 `langdetect` / ISO 639-1 的對應關係：

* `zh` → 中文（未指定）
* `zh-cn` → 簡體中文（中國）
* `zh-tw`（或你映射中的 `hant`）→ 繁體中文（台灣）
* `ja` → 日語
* `ko` → 韓語
* `ne` → 尼泊爾語
* `hi` → 印地語

你是否需要我建議如何**強化你的驗證器**，以便在 `langdetect` 誤判時不會失敗（例如，當目標文字明顯是中文但檢測結果卻顯示為 `ko` 時，允許使用後備方案）？