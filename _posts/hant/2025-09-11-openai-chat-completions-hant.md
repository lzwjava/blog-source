---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 使用 OpenAI 聊天完成模型
translated: true
type: note
---

你已連結到 Microsoft Learn 文章 **「使用聊天完成模型」**（發佈於 **2025 年 9 月 1 日**）。以下是其核心要點的清晰簡明摘要：

---

### 重點摘要

* **聊天導向模型**
  較新的聊天模型與早期的 GPT-3 模型不同。它們採用 **對話輸入、訊息輸出** 格式，而非「文字輸入、文字輸出」。基本上，輸入結構類似對話記錄（包含 *system*、*user*、*assistant* 等角色），而模型會返回一條訊息以繼續對話 ([Microsoft Learn][1])。

* **專為對話設計**
  此結構針對多輪來回對話進行了優化。它同樣適用於單次提示場景，但對話格式能實現更流暢的互動 ([Microsoft Learn][1])。

* **勿以舊模型方式使用**
  這些聊天模型回應較為詳盡，若以 GPT-3 的方式使用，往往會產生較不實用的回答。建議使用新的聊天風格介面以獲得最佳效果 ([Microsoft Learn][1])。

* **範例程式碼片段**
  文章包含使用 Python 風格語法的基礎程式碼範例，用於呼叫 Azure 的聊天完成 API：

  ```python
  from openai import OpenAI
  import os

  client = OpenAI(
      api_key=os.getenv("AZURE_OPENAI_API_KEY"),
      base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/"
  )

  response = client.chat.completions.create(
      model="gpt-4o",  # or deployment_name
      messages=[
          {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
          {"role": "user", "content": "Who were the founders of Microsoft?"}
      ]
  )

  print(response.model_dump_json(indent=2))
  print(response.choices[0].message.content)
  ```

  這展示了如何正確發送訊息（含角色區分）並獲取模型的回答 ([Microsoft Learn][1])。

---

### 重要性

1. **增強對話上下文** — 聊天模型能更好地維持多輪互動中的流程和上下文。
2. **提升可用性** — 使用角色（system、user、assistant）允許更清晰的指令、個性設定或限制。
3. **避免陷阱** — 以舊世代模型的方式使用聊天模型可能導致回應品質不佳；請按設計意圖使用聊天 API 介面。

---

如果你需要協助逐步理解程式碼範例、將其調整至你的設定，或探索相關指南，請告訴我——我很樂意深入探討！

根據你的偏好，我保持了簡單易讀的格式，未使用表格。

[1]: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/chatgpt?utm_source=chatgpt.com "Work with chat completion models - Azure OpenAI in ..."