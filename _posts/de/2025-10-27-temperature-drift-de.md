---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Temperaturbedingte Nullpunktdrift von Verstärkern
translated: true
type: note
---

**C. Temperatureffekte auf Transistorparameter**

In direkt gekoppelten Mehrstufenverstärkerschaltungen, die sowohl AC- als auch DC-Signale ohne Koppelkondensatoren übertragen, werden kleine Änderungen der DC-Bias-Spannungen über die Stufen hinweg verstärkt, was zu Nullpunktdrift (unerwünschter Ausgangsoffset bei Null-Eingang) führt. Während Faktoren wie Netzteilsschwankungen oder Bauteiltoleranzen dazu beitragen, sind hauptsächlich Temperaturänderungen die Ursache für diese Drift. Transistorparameter wie die Basis-Emitter-Spannung (V_BE) und die Stromverstärkung (β) variieren erheblich mit der Temperatur – typischerweise sinkt V_BE um etwa 2 mV/°C – was zu kumulativen Offsets in Mehrstufenaufbauten führt. Dies macht thermische Effekte zum dominierenden und am schwierigsten zu beherrschenden Problem.

[Wie man die Nullpunktdrift in direktgekoppelten Verstärkerschaltungen unterdrückt](https://en.eeworld.com.cn/news/mndz/eic73044.html)  
[Vorlesung 5 - Verstärker](https://feng.stafpu.bu.edu.eg/Electrical%20Engineering/2460/crs-13711/Files/EEDP_Lect%2005_Amplifiers_2m.pdf)