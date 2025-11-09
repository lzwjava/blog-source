---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 溫度引發放大器零點漂移
translated: true
type: note
---

**C. 溫度對電晶體參數的影響**

在直接耦合的多級放大電路中，由於無需耦合電容器即可同時傳遞交流與直流信號，微小的直流偏壓變化會在各級間被放大，導致零點漂移（在零輸入時出現非預期輸出偏移）。雖然電源波動或元件誤差等因素都會造成影響，但溫度變化才是引發此類漂移的主因。電晶體參數如基極-射極電壓（V_BE）和電流增益（β）會隨溫度顯著變化——通常 V_BE 會以約 2 mV/°C 的幅度下降——這在多級放大結構中會產生累積偏移，使得熱效應成為最關鍵且最難抑制的問題。

[如何抑制直接耦合放大電路的零點漂移](https://en.eeworld.com.cn/news/mndz/eic73044.html)  
[第五講 - 放大器](https://feng.stafpu.bu.edu.eg/Electrical%20Engineering/2460/crs-13711/Files/EEDP_Lect%2005_Amplifiers_2m.pdf)