---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 計算模型回應等待時間
translated: true
type: note
---

我們可以逐步推算。

根據記錄：

* **tokens_completion** = 9532
* 這裡雖未顯示 **throughput**，但你問的是「tokens ÷ tokens per second」

此請求包含：

* `generation_time = 203477 ms` → 203.477 秒
* `tokens_completion = 9532`

現在計算實際吞吐量：

$$
\text{每秒令牌數} = \frac{9532}{203.477} \approx 46.8
$$

因此用戶需要等待約 **203 秒（約 3 分 23 秒）** 才能獲得回應。

若已知模型的吞吐量（每秒令牌數），則等待時間可直接計算為：

$$
\text{等待時間} = \frac{\text{完成令牌數}}{\text{每秒令牌數}}
$$

在此案例中，日誌已提供時間與令牌數兩項數據，故計算結果相符。

👉 簡要說明：用戶為獲得 9532 個令牌等待了約 **203 秒（約 3 分 23 秒）**，處理速度約為每秒 47 個令牌。

需要我同時展示適用於其他日誌的**通用公式**嗎（使用延遲、吞吐量及令牌數進行計算）？