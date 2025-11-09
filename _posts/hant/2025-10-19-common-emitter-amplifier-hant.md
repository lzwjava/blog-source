---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 共發射極放大器分析
translated: true
type: note
---

### 集電極電流 \\( I_C \\)

對於發射極接地的共射極BJT放大器，其輸入電阻 \\( R_{in} \\) 約等於小信號基極電阻 \\( r_\pi = \frac{\beta V_T}{I_C} \\)，其中 \\( V_T = 0.026 \\) V（室溫下的熱電壓）且 \\( \beta = 100 \\)。

給定 \\( R_{in} = 1 \\) k\\( \Omega = 1000 \\) \\( \Omega \\)，

\\[
r_\pi = \frac{100 \times 0.026}{I_C} = 1000
\\]

\\[
\frac{2.6}{I_C} = 1000
\\]

\\[
I_C = \frac{2.6}{1000} = 0.0026 \text{ A} = 2.6 \text{ mA}
\\]

此偏壓點產生的集電極-發射極電壓 \\( V_{CE} = V_{CC} - I_C R_C = 12 - (0.0026 \times 2200) \approx 12 - 5.72 = 6.28 \\) V，接近電源電壓的中點，可實現合理的線性度。

### 電壓增益 \\( A_V \\)

共射極放大器（無發射極電阻）的小信號電壓增益為 \\( A_V = -g_m R_C \\)，其中跨導 \\( g_m = \frac{I_C}{V_T} \\)。

\\[
g_m = \frac{0.0026}{0.026} = 0.1 \text{ A/V（或 S）}
\\]

\\[
A_V = - (0.1 \times 2200) = -220
\\]

負號表示相位反轉。