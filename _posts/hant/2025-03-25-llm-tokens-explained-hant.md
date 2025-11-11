---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 大型語言模型代幣淺談
translated: true
type: note
---

很好的問題——LLM API 中的「token」概念起初確實有點令人困惑。讓我來清楚解釋一下。

---

## 什麼是 Token

* **Token** 是模型處理文本的最小單位。
* **它不完全等同於單字**。Token 通常是單字的一部分、完整單字、標點符號，甚至空格（取決於語言和分詞器）。
* LLM（如 OpenAI GPT 模型）使用預定義的 **分詞器** 將文本分割成 token。

例如：

* `"cat"` → 1 個 token
* `"cats"` → 可能分割為 `"cat"` + `"s"` → 2 個 token
* `"You're handsome."` → 會分割成類似 `"You"`、`"'re"`、`" handsome"`、`"."` → **4 個 token**

因此，token 是 **子詞單位**，經過優化後能讓模型高效處理多種語言和罕見詞彙。

---

## Token 在 API 中的重要性

1. **計費** – 大多數 LLM API 按 token 收費（輸入 + 輸出）。
2. **限制** – 模型有最大 token 限制（例如 GPT-4 Turbo 的 128k 代表輸入 + 輸出總共最多 128,000 個 token）。
3. **效率** – 你希望盡量減少發送提示時的 token 數量，以降低成本和避免超出限制。

---

## 實際處理 Token

* **估算 token**：一個粗略規則是英文約每 4 個字符對應 1 個 token。所以一篇 1,000 字的英文文章（≈5,000 字符）約為 1,200–1,300 個 token。
* **精確檢查 token**：大多數 SDK（如 OpenAI 的 Python 套件 `tiktoken`）讓你在發送前計算 token 數量。
* **優化提示**：

  * 移除不必要的空格/詞語。
  * 使用簡潔的指令。
  * 總結上下文而非直接傾倒原始文本。

---

## 範例

```python
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
text = "You're handsome."
tokens = enc.encode(text)
print(tokens)        # token ID 列表
print(len(tokens))   # token 數量
```

這會輸出類似 `[9125, 3938, 13]` → 3 個 token（具體取決於分詞器版本）。

---

✅ 所以：**token ≠ 單字**。它們是 LLM 所見的基礎構件。`"You're handsome."` 大約是 3–4 個 token，而不是 2 個單字。

---

需要我示範 **如何計算你自己文本（如逐字稿、文章、程式碼）的 token 數量**，以便在調用 API 前了解成本/限制嗎？