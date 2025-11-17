---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Consumo y Coste Estimado de la GPU
translated: true
type: note
---

Usando el número mostrado en tu salida:

Tu GPU está consumiendo **aproximadamente 205 vatios** durante la ejecución.

Un "grado de electricidad" = **1 kWh**.

**Si solo se contara la GPU:**

* **1 hora:** 205 W ≈ **0.205 kWh**
* **24 horas:** 0.205 × 24 ≈ **4.92 kWh**

Sin embargo, una máquina real también incluye CPU, placa base, RAM, ventiladores, SSD, pérdidas de la fuente de alimentación, etc.
Un equipo de entrenamiento típico con una 4070 suele consumir **300–380 W en total** en la toma de pared.

Si usamos una estimación más realista de todo el sistema, digamos alrededor de **320 W** en promedio:

* **1 hora:** 0.32 kWh
* **24 horas:** 7.68 kWh

Si tu carga de trabajo mantiene la GPU al 100% todo el tiempo, espera que tu factura real esté en ese rango de todo el sistema en lugar del número de solo la GPU.

Si quieres, puedes decirme tu modelo de fuente de alimentación, tipo de CPU y cuántos ventiladores/discos tienes, y puedo estimarlo con mayor precisión.