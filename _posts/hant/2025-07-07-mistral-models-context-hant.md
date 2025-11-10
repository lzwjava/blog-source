---
audio: false
generated: true
lang: hant
layout: post
title: Mistral AI 2025 年模型上下文長度
translated: true
type: note
---

截至2025年6月，Mistral AI 已發布多款具備不同上下文長度的模型。以下為部分關鍵模型及其上下文窗口的摘要：

* **Magistral Small (magistral-small-2506)：** 這款開放權重模型擁有 128k 上下文窗口，但超過 40k 後性能可能下降，因此建議最大長度為 40k tokens。
* **Magistral Medium (magistral-medium-2506)：** 這款僅限 API 使用的推理模型同樣建議使用 40k 上下文窗口。
* **Mistral Small 3.1 (mistral-small-2503) / Mistral Small 3.2 (mistral-small-2506)：** 這些模型的上下文窗口最高可達 128,000 tokens。
* **Codestral (codestral-2501)：** 這款專注於編碼的模型擁有 256,000 tokens 的顯著上下文窗口。
* **Mistral Large 2 (mistral-large-2407 / mistral-large-2411)：** Mistral 的旗艦大型模型具備 128k 上下文窗口。
* **Mistral NeMo (open-mistral-nemo-2407)：** 這款與 NVIDIA 合作開發的 12B 模型提供高達 128,000 tokens 的大上下文窗口。
* **Mistral Medium 3 (mistral-medium-2505)：** 這款多模態模型同樣支援 128k 上下文窗口。

需注意雖然部分模型標榜極大的上下文窗口（例如 128k），但實際性能可能在稍小範圍內（例如 Magistral 系列的 40k）才能達到最佳化。