---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 理解大型語言模型溫度參數基礎
translated: true
type: note
---

在 LLM API（如 OpenAI、Copilot API、Anthropic 等）中，**temperature** 是一個用於控制模型輸出*隨機性*或*確定性*程度的參數。

---

### Temperature 的作用

* **低 temperature（接近 0）：**
  模型會變得確定性，總是選擇最可能的下一詞元。
  範例：若要求定義，每次都會給出最標準/預期的答案。

* **高 temperature（接近 1 或更高）：**
  模型會更自由地取樣，探索可能性較低的詞元。這會增加多樣性、創造力和不可預測性。
  範例：對於腦力激盪、故事創作或生成程式碼變體，較高的 temperature 可能更合適。

---

### 「0.7」的意義

* `temperature = 0.7` 是一個**適中平衡點**。

  * 允許一定的隨機性和多樣性。
  * 模型不會像 `0` 那樣僵化，也不會像 `1.2` 那樣「狂野」。
  * 這就是為什麼**許多 API（包括類 Copilot 系統）常將 0.7 設為預設值**——它能提供具創造力且仍可靠的結果。

---

### 如何使用

在多數 API 中，可透過請求參數傳遞。例如：

**OpenAI API（聊天完成）：**

```json
{
  "model": "gpt-4.1",
  "messages": [
    {"role": "user", "content": "寫一個關於龍與機械人的短篇故事。"}
  ],
  "temperature": 0.7
}
```

**GitHub Copilot API：**
參數運作方式類似。Copilot 內部使用 temperature 來決定要提供更直白的補全還是更具探索性的建議。多數 IDE 整合會設定在 `0.7` 左右，但某些情境（如程式碼補全）可能為求穩定性而使用較低值。

---

✅ **經驗法則：**

* **0–0.3** → 確定性、事實性、可預測。適用於數學、API 文檔、配置、單元測試。
* **0.4–0.7** → 平衡、自然書寫、標準編碼。多數情況的良好預設值。
* **0.8–1.2** → 創造性、探索性、勇於嘗試。適用於腦力激盪、故事、詩歌。

---

您是否也想了解 **temperature 如何與 `top_p`（核取樣）互動**？這兩者在 Copilot/LLM API 中通常都可同時使用。