---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Claude 4 Sonnet 完成指標詳解
translated: true
type: note
---

簡短來說：它正常結束了。
`finish_reason: "stop"` 表示模型已達到其回覆的自然終點（觸發了停止序列，例如助理結束標記），並且**沒有**遇到長度限制、錯誤或取消。

以下是用簡單英文解釋該記錄其餘部分的內容：

* **模型與路徑**
  您透過 **Google Vertex** (`provider_name: "Google"`) 呼叫了 **anthropic/claude-4-sonnet-20250522**。這就是您看到帶有狀態 200 的 `provider_responses` 條目的原因。

* **計時 / 速度**

  * `latency: 2850` → 大約 **2.85 秒** 後**第一個標記**出現。
  * `generation_time: 76365` → 總共大約 **76.4 秒** 完成回覆。
  * 配合 `tokens_completion: 2376`，這表示整個生成過程的吞吐量大約是 **31 個標記/秒** (2376 ÷ 76.4 ≈ 31.1)。

* **標記計數（兩組）**

  * `tokens_prompt: 8446`, `tokens_completion: 2376` → 您的聚合器的計數。
  * `native_tokens_prompt: 9007`, `native_tokens_completion: 2511` → **供應商**自己的標記化工具/計帳方式。這些數字通常因不同的標記化工具、系統封裝或隱藏的控制標記而有所差異。
  * `native_tokens_reasoning: 0` → 此執行未使用「推理標記」計量（當特殊推理模式開啟時，某些供應商會公開此數據）。
  * `native_tokens_cached: 0` → 沒有提示快取命中。

* **串流與取消**

  * `streamed: true` → 標記是以串流方式傳送給您的。
  * `cancelled: false` → 您沒有中斷它。

* **為什麼不是「length」？**
  如果它達到了最大標記限制，您會看到 `finish_reason: "length"`。您沒有看到，所以模型在任何限制之前就完成了。

* **這是什麼時候發生的？**
  `created_at: "2025-09-02T17:26:45.92824+00:00"` (UTC)。在您的時區 (Asia/Taipei, UTC+8)，那是 **2025-09-03 01:26:45**。

* **成本/使用量欄位**

  * `usage: 0.064686` → 您系統的成本/使用量指標（單位取決於您的計費層）。
  * 幾個 `null` 欄位僅表示您的路由器沒有記錄額外細節（審核延遲、搜尋結果等）。

* **雜項**

  * `finish_reason: "stop"`（再次強調）是關鍵：透過停止標記正常停止。
  * `origin: ""`, `app_id: null` → 沒有特定的應用程式標籤。
  * `is_byok: false` → 不是自帶金鑰的呼叫。

如果您願意，可以貼上第二個您看到 `length` 或 `cancelled` 的範例，我會逐行對比它們（不使用表格）。