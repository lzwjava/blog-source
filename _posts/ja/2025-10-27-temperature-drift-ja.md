---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 温度誘起増幅器零点ドリフト
translated: true
type: note
---

**C. トランジスタパラメータに及ぼす温度影響**

直接結合型多段増幅回路では、結合コンデンサを使用せずに交流信号と直流信号の両方を通過させるため、直流バイアス電圧の微小な変動が各段で増幅され、零点ドリフト（入力ゼロ時の望ましくない出力オフセット）を引き起こします。電源変動や部品のばらつきなどの要因も寄与しますが、温度変化がこのドリフトの主な原因です。ベース-エミッタ間電圧（V_BE）や電流増幅率（β）などのトランジスタパラメータは温度によって大きく変動します。一般的に、V_BEは約2 mV/°Cで低下し、多段構成では累積的なオフセットを生じさせます。このため、熱の影響が最も支配的で、緩和が困難な問題となります。

[直接結合増幅回路における零点ドリフトの抑制方法](https://en.eeworld.com.cn/news/mndz/eic73044.html)  
[Lecture 5 - 増幅器](https://feng.stafpu.bu.edu.eg/Electrical%20Engineering/2460/crs-13711/Files/EEDP_Lect%2005_Amplifiers_2m.pdf)