---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: NVIDIA GPU-Leistungsentwicklung im Vergleich
translated: true
type: note
---

### NVIDIA-GPUs: 2010 DirectX-11-Flaggschiffe vs. Moderne RTX-Karten

Um 2010 waren die besten Consumer-Grafikkarten von NVIDIA mit DirectX-11-Unterstützung die **GeForce GTX 480** (März 2010, erste DX11-Karte) und die **GTX 580** (November 2010, schnellste ihrer Zeit). Diese basierten auf der Fermi-Architektur, hatten 480–512 CUDA-Cores, 1,5 GB GDDR5-Speicher und eine TDP von ~250W.

Moderne Vergleiche: **RTX 3090** (Ampere, 2020), **RTX 4070** (Ada Lovelace, 2023) und **RTX 4090** (Ada Lovelace, 2022). **Eine RTX 4090 Ti wurde nie veröffentlicht** – sie war 2023 Gerüchten zufolge in Planung, wurde aber abgesagt, und es gab auch bis 2025 keine Neuigkeiten.

#### FP32 TFLOPS (Theoretische Spitzenleistung in Einfachgenauigkeit)
Dies misst die reine Shader-Rechenleistung (höher = bessere theoretische FLOPS).

| GPU          | Architektur | FP32 TFLOPS | Multiplikator vs. GTX 480 |
|--------------|--------------|-------------|-------------------------|
| GTX 480     | Fermi       | 1,345      | 1x                     |
| GTX 580     | Fermi 2.0   | 1,581      | 1,18x                  |
| RTX 4070    | Ada         | 29,15      | 21,7x                  |
| RTX 3090    | Ampere      | 35,58      | 26,5x                  |
| RTX 4090    | Ada         | 82,58      | 61,4x                  |

Moderne Karten liefern **20–60x** mehr rohe FLOPS, dank massiver Core-Anzahlen (5.888–16.384 Shader), höherer Taktraten und architektonischer Effizienz.

#### Leistung in der Praxis (Relativ zur RTX 4090 = 100%)
- **TechPowerUp Relative Performance**: Durchschnitt über 1.000+ Spiele/Benchmarks (1080p/1440p, Fokus auf Rasterisierung). Neuere Architekturen schneiden in realen Workloads aufgrund besserer Ablaufplanung, Caching und Features wie DLSS/RT besser ab.
- **PassMark G3D Mark**: Zusammengefasster synthetischer Benchmark (Durchschnitt eingereichter Benutzerwerte).

| GPU          | TechPowerUp Relativ (RTX 4090 = 100%) | PassMark G3D Mark (Durchs.) | Multiplikator vs. GTX 480 (PassMark) |
|--------------|----------------------------------------|--------------------------|-----------------------------------|
| GTX 480     | 6%                                    | ~4.075                  | 1x                               |
| GTX 580     | ~7%                                   | ~4.500                  | ~1,1x                            |
| RTX 4070    | 53%                                   | ~26.900                 | ~6,6x                            |
| RTX 3090    | 58%                                   | ~26.600                 | ~6,5x                            |
| RTX 4090    | 100%                                  | ~38.400                 | ~9,4x                            |

- **Wichtige Erkenntnisse**:
  - **Theoretische FLOPS übertreibt Gewinne**: Die tatsächliche Leistung ist "nur" **10–17x** höher für die RTX 4090 vs. 2010er Karten, aufgrund von Fermis Ineffizienzen (schlechtes Caching, hohe Leistung/Wärme).
  - In modernen Spielen (1440p/4K, DX12 Ultimate, Raytracing): Die Multiplikatoren sind **20–50x+** höher, da alte Karten mit VRAM-Limits (1,5 GB vs. 12–24 GB) kämpfen und RT/DLSS fehlt.
  - Energieeffizienz: RTX 4090 (450W) hat eine ~4x höhere Leistung pro Watt als die GTX 480 (250W).
  - Spielbeispiel: In Titeln von 2010 erreichte die GTX 480 ~60 FPS bei 1080p hoch. Die RTX 4090 schafft heute 4K Ultra + RT bei 200+ FPS.

**Referenzen**:
- [TechPowerUp GTX 480 Specs](https://www.techpowerup.com/gpu-specs/geforce-gtx-480.c268)
- [TechPowerUp GTX 580 Specs](https://www.techpowerup.com/gpu-specs/geforce-gtx-580.c270)
- [TechPowerUp RTX 3090 Specs](https://www.techpowerup.com/gpu-specs/geforce-rtx-3090.c3622)
- [TechPowerUp RTX 4070 Specs](https://www.techpowerup.com/gpu-specs/geforce-rtx-4070.c3924)
- [TechPowerUp RTX 4090 Specs](https://www.techpowerup.com/gpu-specs/geforce-rtx-4090.c3889)
- [PassMark Video Card Benchmarks](https://www.videocardbenchmark.net)