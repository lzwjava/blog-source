---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Verständnis der Modell-FLOPs-Auslastung
translated: true
type: note
---

In NanoGPT steht **MFU** für **Model FLOPs Utilization**.

Es zeigt dir, **wie viel der theoretischen Rechenleistung (FLOPs) deiner GPU das Modell während des Trainings tatsächlich nutzt**.
Man kann es als groben "GPU-Effizienz"-Indikator betrachten.

Hier ist die praktische Bedeutung:

**• 0–20 % MFU:**
Typisch für kleine Modelle, kleine Batch-Größen oder wenn die GPU nicht voll ausgelastet ist.

**• 30–50 % MFU:**
Ziemlich gut für ein einfaches Modell auf Consumer-GPUs.

**• 50–70 % MFU:**
Sehr starke Auslastung – normalerweise bei großen Batch-Größen und gut optimierten Kerneln.

**• 80 %+ MFU:**
Nahe am Limit; tritt nur bei großen Modellen mit optimierten Kerneln auf (FlashAttention, fused ops, bf16, etc.).

Dein Wert:

```
mfu 10.69%
```

Das ist normal für ein 125M-Parameter-Modell auf einer 4070. Kleine Modelle nutzen die GPU nicht vollständig aus, weil:

* Die Matmuls zu klein sind, um die SMs zu sättigen
* Die Batch-Größe klein ist
* Ein gewisser Overhead (Dataloader, Python) dominiert
* Die GPU für riesige Matrixmultiplikationen gebaut ist, nicht für winzige

Wenn du die MFU erhöhen möchtest, kannst du versuchen:

* Die **Batch-Größe** zu erhöhen (max Tokens pro Batch)
* Die **Modellgröße** zu erhöhen
* **FlashAttention** zu verwenden
* **CUDA Graph Capture** zu verwenden (wird in neueren Configs bereits genutzt)

Aber für kleine Modelle ist eine MFU von ~10–20 % erwartet und völlig in Ordnung.

Falls du möchtest, kann ich dir helfen, deine Config auszulesen und genau zu zeigen, wie deine MFU mit deiner Batch-Größe und Parameteranzahl zusammenhängt.