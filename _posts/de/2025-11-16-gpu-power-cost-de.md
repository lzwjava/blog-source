---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GPU-Leistungsaufnahme und Kostenkalkulation
translated: true
type: note
---

Ihre GPU zieht **etwa 205 Watt** während des Laufs.

Eine „Kilowattstunde“ Strom = **1 kWh**.

**Wenn nur die GPU berücksichtigt würde:**

*   **1 Stunde:** 205 W ≈ **0,205 kWh**
*   **24 Stunden:** 0,205 × 24 ≈ **4,92 kWh**

In der Realität verbraucht eine komplette Maschine jedoch auch CPU, Mainboard, RAM, Lüfter, SSD, Netzteilverluste usw.
Ein typischer Trainingsrechner mit einer 4070 zieht usually **300–380 W gesamt** an der Steckdose.

Wenn wir eine realistischere Schätzung für das Gesamtsystem zugrunde legen, sagen wir etwa **320 W** im Durchschnitt:

*   **1 Stunde:** 0,32 kWh
*   **24 Stunden:** 7,68 kWh

Wenn Ihre Workload die GPU die ganze Zeit auf 100 % auslastet, können Sie erwarten, dass Ihre tatsächliche Stromrechnung in diesem Bereich für das Gesamtsystem liegt und nicht bei der reinen GPU-Zahl.

Wenn Sie möchten, können Sie mir Ihr Netzteilmmodell, Ihren CPU-Typ und die Anzahl der Lüfter/Festplatten nennen, dann kann ich es genauer abschätzen.