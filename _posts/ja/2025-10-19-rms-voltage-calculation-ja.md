---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 実効電圧計算の理解
translated: true
type: note
---

### 説明

実効電圧（RMS電圧）\\( V_{RMS} \\)は、同じ大きさの直流（DC）電圧が抵抗負荷で発生するのと同じ電力消費を生み出す交流電圧の実効値を表します。正弦波波形 \\( v(t) = V_{max} \sin(\omega t) \\)（\\( V_{max} \\)はピーク（最大）電圧）の場合、RMS値は以下のように導出されます。

1. **平均二乗値**: 1周期 \\( T \\) にわたる瞬時電圧の二乗は \\( v^2(t) = V_{max}^2 \sin^2(\omega t) \\) です。\\( \sin^2(\omega t) \\) の1周期にわたる平均は \\( \frac{1}{2} \\) なので、平均二乗電圧は \\( \frac{V_{max}^2}{2} \\) となります。

2. **RMS計算**: 平均二乗値の平方根を取ります:  
   \\[
   V_{RMS} = \sqrt{\frac{V_{max}^2}{2}} = \frac{V_{max}}{\sqrt{2}}
   \\]

3. **数値近似**: \\( \sqrt{2} \approx 1.414 \\) なので、\\( \frac{1}{\sqrt{2}} \approx 0.707 \\) となります。したがって、\\( V_{RMS} \approx 0.707 \times V_{max} \\) です。

これにより、選択肢 **B** が確認されます。他の選択肢は誤りです:  
- A は過大評価しています（平均化を無視しています）。  
- C は係数を逆にしています（これは \\( V_{max} = \sqrt{2} \times V_{RMS} \\) の場合です）。  
- D は過小評価しています（これは全波整流された正弦波の平均値であり、RMS値ではありません）。