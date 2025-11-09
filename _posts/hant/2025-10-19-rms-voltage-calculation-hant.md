---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 理解均方根電壓計算
translated: true
type: note
---

### 說明

均方根（RMS）電壓 \\( V_{RMS} \\) 代表交流電壓的有效值，其在一電阻性負載中所產生的功率消耗與同等大小的直流電壓相同。對於正弦波形 \\( v(t) = V_{max} \sin(\omega t) \\)，其中 \\( V_{max} \\) 為峰值（最大）電壓，RMS 值的推導如下：

1. **均方值**：瞬時電壓的平方在一個週期 \\( T \\) 內為 \\( v^2(t) = V_{max}^2 \sin^2(\omega t) \\)。\\( \sin^2(\omega t) \\) 在一個週期內的平均值為 \\( \frac{1}{2} \\)，因此均方電壓為 \\( \frac{V_{max}^2}{2} \\)。

2. **RMS 計算**：取均方值的平方根：  
   \\[
   V_{RMS} = \sqrt{\frac{V_{max}^2}{2}} = \frac{V_{max}}{\sqrt{2}}
   \\]

3. **數值近似**：由於 \\( \sqrt{2} \approx 1.414 \\)，因此 \\( \frac{1}{\sqrt{2}} \approx 0.707 \\)。所以，\\( V_{RMS} \approx 0.707 \times V_{max} \\)。

這確認了選項 **B** 是正確的。其他選項不正確：  
- A 高估了（忽略了平均過程）。  
- C 倒置了係數（那是 \\( V_{max} = \sqrt{2} \times V_{RMS} \\)）。  
- D 低估了（那是全波整流正弦波的平均值，而非 RMS）。