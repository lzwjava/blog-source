---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Deriva del Punto Cero del Amplificador Inducida por la Temperatura
translated: true
type: note
---

**C. Efectos de la temperatura en los parámetros del transistor**

En los circuitos amplificadores multietapa de acoplamiento directo, que pasan tanto señales de CA como de CC sin condensadores de acoplamiento, los pequeños cambios en los voltajes de polarización de CC se amplifican a través de las etapas, lo que conduce a la deriva del punto cero (desplazamiento no deseado en la salida con entrada cero). Si bien factores como las variaciones de la fuente de alimentación o las discrepancias entre componentes contribuyen, los cambios de temperatura son la causa principal de esta deriva. Los parámetros del transistor, como el voltaje base-emisor (V_BE) y la ganancia de corriente (β), varían significativamente con la temperatura—típicamente, V_BE disminuye aproximadamente 2 mV/°C—causando desplazamientos acumulativos en configuraciones multietapa. Esto convierte a los efectos térmicos en el problema dominante y más difícil de mitigar.

[Cómo suprimir la deriva del cero en circuitos amplificadores de acoplamiento directo](https://en.eeworld.com.cn/news/mndz/eic73044.html)  
[Conferencia 5 - Amplificadores](https://feng.stafpu.bu.edu.eg/Electrical%20Engineering/2460/crs-13711/Files/EEDP_Lect%2005_Amplifiers_2m.pdf)