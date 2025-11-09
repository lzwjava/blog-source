---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Dérive du point zéro de l'amplificateur induite par la température
translated: true
type: note
---

**C. Effets de la température sur les paramètres des transistors**

Dans les circuits amplificateurs multi-étages à couplage direct, qui transmettent à la fois les signaux AC et DC sans condensateurs de couplage, de petits changements dans les tensions de polarisation DC sont amplifiés à travers les étages, conduisant à une dérive du point zéro (décalage de sortie non désiré lorsque l'entrée est nulle). Bien que des facteurs comme les variations de l'alimentation ou les mismatches des composants y contribuent, les changements de température en sont la cause principale. Les paramètres des transistors tels que la tension base-émetteur (V_BE) et le gain en courant (β) varient significativement avec la température—typiquement, V_BE diminue d'environ 2 mV/°C—provoquant des décalages cumulatifs dans les configurations multi-étages. Cela fait des effets thermiques le problème dominant et le plus difficile à atténuer.

[Comment supprimer la dérive du zéro dans les circuits amplificateurs à couplage direct](https://en.eeworld.com.cn/news/mndz/eic73044.html)  
[Lecture 5 - Amplificateurs](https://feng.stafpu.bu.edu.eg/Electrical%20Engineering/2460/crs-13711/Files/EEDP_Lect%2005_Amplifiers_2m.pdf)