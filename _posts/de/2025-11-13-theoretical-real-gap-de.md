---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Die Kluft zwischen theoretischer und realer Leistung
translated: true
type: note
---

Die Diskrepanz entsteht, weil **theoretische Spitzen-FLOPS** (Gleitkommaoperationen pro Sekunde) den rohen Rechendurchsatz unter idealen Bedingungen messen – unter der Annahme einer perfekten Auslastung aller Ausführungseinheiten, ohne Engpässe im Speicher und mit unendlicher Bandbreite. In realen Workloads (insbesondere bei KI/Training/Inferenz) wird die Leistung durch **Ineffizienzen im Speichersubsystem** begrenzt, nicht nur durch die Rechenleistung. Die 2010er Fermi-GPUs (z.B. GTX 480) waren hierfür besonders anfällig und vergrößerten die "erwartete" Kluft im Vergleich zu modernen Karten wie der RTX 4090.

### Hauptgründe für die Unterauslastung der theoretischen FLOPS bei Fermi
1. **Schlechtes Cache-Hierarchy und Memory Coalescing**
   - Fermi hatte nur 64 KB L1-Cache pro SM (mit Registern geteilt) und einen winzigen 768 KB L2-Cache (für den gesamten Chip).
   - Keine ordnungsgemäße Cache-Kohärenz; Zugriffe auf den globalen Speicher waren nicht zusammengefasst → **~10–30 % der effektiven Bandbreite** in realen Kernels.
   - Moderne GPUs (Ampere/Ada) haben **massiven L1-Cache (192 KB/SM)**, **dedizierte Texturcaches** und **aggressives Prefetching** und erreichen 70–90 % der theoretischen Bandbreite.

2. **Hohe Latenz, geringe Bandbreite ECC DDR5/GDDR5**
   - Fermi: ~170 GB/s GDDR5, **384-Bit-Bus, aber ECC-Overhead** → effektiv ~130 GB/s.
   - RTX 4090: **1 TB/s GDDR6X**, 384-Bit, aber **kein ECC-Aufschlag im Consumer-Modus**, plus **bessere Kompression**.
   - Reale KI-Kernels sind **speichergebunden** (z.B. GEMM mit großen Matrizen); FLOPS sind irrelevant, wenn Daten warten müssen.

3. **Ineffiziente Register File und Warp Scheduling**
   - Fermi: 32k 32-Bit-Register/SM → **max. 1536 Threads**, aber nur **~50 % Auslastung** in der Praxis aufgrund von Register Spilling.
   - Ada: 256 KB Register File → **2048 Threads/SM**, nahezu 100 % Auslastung.
   - Geringere Divergenz, bessere ILP-Extraktion.

4. **Power/Thermal Throttling**
   - GTX 480: 250 W TDP, **starkes Throttling unter anhaltender Last** (Takt reduzierte sich um 10–20 %).
   - RTX 4090: 450 W, aber **~3x bessere Leistung pro Watt** durch 4nm-Prozess, DLSS und dynamisches Boosting.

### Gemessene Gewinne in der Praxis (KI-Workloads)

| Metrik | GTX 480 (Fermi, 2010) | RTX 4090 (Ada, 2022) | Beschleunigung |
|--------|------------------------|----------------------|---------|
| FP32 TFLOPS (Spitze) | 1,35 | 82,6 | **61x** |
| FP16 TFLOPS (Spitze) | ~0,7 (emuliert) | 330 (Tensor) | **>400x** |
| **ResNet-50 Training (Bilder/s)** | ~60 | ~1.050 | **~17x** |
| **GPT-2 Inferenz (Tokens/s)** | ~8 | ~140 | **~17x** |
| **Stable Diffusion (Iterationen/s)** | <0,1 | ~1,6 | **>16x** |

*Quellen: NVIDIA-Papiere, MLPerf-Benchmarks, AnandTech.*

### Fazit
Theoretische FLOPS gingen davon aus, dass Fermi ~70 % Auslastung halten könnte – was nicht gelang (real ~15–25 %). Moderne Architekturen schließen diese Lücke auf **~70–90 %**, sodass **effektive Rechenleistung näher am Mooreschen Gesetz plus Architekturverbesserungen** skaliert (~10–17x über 12 Jahre), und nicht an den 60x+, die die Spitzen-FLOPS suggerieren. Der Rest ist "Papierleistung".