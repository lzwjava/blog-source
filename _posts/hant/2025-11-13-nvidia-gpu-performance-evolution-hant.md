---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: NVIDIA GPU 性能演進對比
translated: true
type: note
---

### NVIDIA 顯示卡：2010年 DirectX 11 旗艦型號 vs 現代 RTX 顯示卡

大約在2010年，NVIDIA支援DirectX 11的頂級消費級顯示卡是**GeForce GTX 480**（2010年3月發布，首款DX11顯示卡）和**GTX 580**（2010年11月發布，當時速度最快）。這些顯示卡基於Fermi架構，擁有480–512個CUDA核心、1.5 GB GDDR5記憶體，以及約250W的TDP。

現代對比型號：**RTX 3090**（Ampere架構，2020年）、**RTX 4070**（Ada Lovelace架構，2023年）和**RTX 4090**（Ada Lovelace架構，2022年）。**從未發布過RTX 4090 Ti**——雖然2023年曾有傳言，但該型號已被取消，即使到2025年也未有更新消息。

#### FP32 TFLOPS（理論峰值單精度效能）
此指標衡量原始著色器計算能力（數值越高代表理論FLOPS效能越好）。

| 顯示卡         | 架構          | FP32 TFLOPS | 相對於 GTX 480 的倍數 |
|---------------|---------------|-------------|----------------------|
| GTX 480      | Fermi        | 1.345      | 1x                   |
| GTX 580      | Fermi 2.0    | 1.581      | 1.18x                |
| RTX 4070     | Ada          | 29.15      | 21.7x                |
| RTX 3090     | Ampere       | 35.58      | 26.5x                |
| RTX 4090     | Ada          | 82.58      | 61.4x                |

現代顯示卡提供了**20–60倍**的原始FLOPS效能，這得益於龐大的核心數量（5,888–16,384個著色器）、更高的時脈速度以及架構效率的提升。

#### 實際效能表現（以 RTX 4090 = 100% 為基準）
- **TechPowerUp 相對效能**：基於1,000多款遊戲/基準測試的平均值（專注於1080p/1440p光柵化）。由於更好的調度、快取技術以及DLSS/光線追蹤等功能，新架構在實際工作負載中表現更出色。
- **PassMark G3D Mark**：綜合性基準測試匯總（平均用戶提交分數）。

| 顯示卡         | TechPowerUp 相對效能 (RTX 4090 = 100%) | PassMark G3D Mark (平均) | 相對於 GTX 480 的倍數 (PassMark) |
|---------------|----------------------------------------|--------------------------|----------------------------------|
| GTX 480      | 6%                                    | ~4,075                  | 1x                              |
| GTX 580      | ~7%                                   | ~4,500                  | ~1.1x                           |
| RTX 4070     | 53%                                   | ~26,900                 | ~6.6x                           |
| RTX 3090     | 58%                                   | ~26,600                 | ~6.5x                           |
| RTX 4090     | 100%                                  | ~38,400                 | ~9.4x                           |

- **關鍵洞察**：
  - **理論FLOPS高估了實際增益**：由於Fermi架構的效率問題（快取效能差、功耗/發熱高），RTX 4090相對於2010年顯示卡的實際效能增益「僅為」**10–17倍**。
  - 在現代遊戲中（1440p/4K解析度、DX12 Ultimate、光線追蹤）：由於舊款顯示卡受限于VRAM容量（1.5 GB vs 12–24 GB）且缺乏RT/DLSS支援，效能倍數可達**20–50倍以上**。
  - 能源效率：RTX 4090（450W）的每瓦效能約為GTX 480（250W）的**4倍**。
  - 遊戲範例：在2010年的遊戲中，GTX 480可在1080p高畫質下達到約60 FPS。而現今的RTX 4090則能在4K超高畫質加上光線追蹤下達到200+ FPS。

**參考資料**：
- [TechPowerUp GTX 480 規格](https://www.techpowerup.com/gpu-specs/geforce-gtx-480.c268)
- [TechPowerUp GTX 580 規格](https://www.techpowerup.com/gpu-specs/geforce-gtx-580.c270)
- [TechPowerUp RTX 3090 規格](https://www.techpowerup.com/gpu-specs/geforce-rtx-3090.c3622)
- [TechPowerUp RTX 4070 規格](https://www.techpowerup.com/gpu-specs/geforce-rtx-4070.c3924)
- [TechPowerUp RTX 4090 規格](https://www.techpowerup.com/gpu-specs/geforce-rtx-4090.c3889)
- [PassMark 顯示卡基準測試](https://www.videocardbenchmark.net)