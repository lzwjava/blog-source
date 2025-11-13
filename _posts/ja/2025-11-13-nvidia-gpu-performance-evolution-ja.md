---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: NVIDIA GPUの性能進化比較
translated: true
type: note
---

### NVIDIA GPU：2010年DirectX 11フラグシップ vs 現代のRTXカード

2010年頃、NVIDIAのDirectX 11をサポートするトップコンシューマー向けグラフィックスカードは、**GeForce GTX 480**（2010年3月発売、初のDX11カード）と**GTX 580**（2010年11月発売、当時最速）でした。これらはFermiアーキテクチャに基づき、480–512 CUDAコア、1.5 GB GDDR5メモリ、~250W TDPを備えていました。

現代のカードとの比較：**RTX 3090**（Ampere、2020年）、**RTX 4070**（Ada Lovelace、2023年）、**RTX 4090**（Ada Lovelace、2022年）。**RTX 4090 Tiは一度も発売されていません**—2023年に噂されましたがキャンセルされ、2025年になっても更新はありません。

#### FP32 TFLOPS（理論上のピーク単精度演算性能）
これは生のシェーダー演算能力を測定します（高いほど理論上のFLOPS性能が優れています）。

| GPU          | アーキテクチャ | FP32 TFLOPS | GTX 480との倍率 |
|--------------|--------------|-------------|-------------------------|
| GTX 480     | Fermi       | 1.345      | 1x                     |
| GTX 580     | Fermi 2.0   | 1.581      | 1.18x                  |
| RTX 4070    | Ada         | 29.15      | 21.7x                  |
| RTX 3090    | Ampere      | 35.58      | 26.5x                  |
| RTX 4090    | Ada         | 82.58      | 61.4x                  |

現代のカードは、膨大なコア数（5,888–16,384シェーダー）、高いクロック、アーキテクチャの効率化により、**20–60倍**の生のFLOPS性能を提供します。

#### 実世界での性能（RTX 4090 = 100% とした相対値）
- **TechPowerUp 相対性能**：1,000以上のゲーム/ベンチマークの平均（1080p/1440p ラスタライゼーション中心）。新しいアーキテクチャは、より優れたスケジューリング、キャッシング、およびDLSS/RTのような機能により、実際のワークロードでより高い性能を発揮します。
- **PassMark G3D Mark**：集約的な合成ベンチマーク（平均ユーザー提出スコア）。

| GPU          | TechPowerUp 相対性能 (RTX 4090 = 100%) | PassMark G3D Mark (平均) | GTX 480との倍率 (PassMark) |
|--------------|----------------------------------------|--------------------------|-----------------------------------|
| GTX 480     | 6%                                    | ~4,075                  | 1x                               |
| GTX 580     | ~7%                                   | ~4,500                  | ~1.1x                            |
| RTX 4070    | 53%                                   | ~26,900                 | ~6.6x                            |
| RTX 3090    | 58%                                   | ~26,600                 | ~6.5x                            |
| RTX 4090    | 100%                                  | ~38,400                 | ~9.4x                            |

- **主な洞察**：
  - **理論上のFLOPSは性能向上を過大評価**：実際の性能は、Fermiの非効率性（キャッシングの貧弱さ、高い電力/発熱）により、RTX 4090対2010年製カードで「わずか」**10–17倍**の高速化に留まります。
  - 現代のゲーム（1440p/4K、DX12 Ultimate、レイトレーシング）では：古いカードはVRAM制限（1.5 GB vs 12–24 GB）やRT/DLSSの欠如に苦しむため、倍率は**20–50倍以上**高くなります。
  - 電力効率：RTX 4090 (450W) は GTX 480 (250W) と比べて約4倍の性能/ワットを実現。
  - ゲーミング例：2010年のタイトルでは、GTX 480は1080p 高設定で~60 FPSを達成。RTX 4090は今日、4K 超高設定 + RT で200+ FPSを実現。

**参考文献**:
- [TechPowerUp GTX 480 Specs](https://www.techpowerup.com/gpu-specs/geforce-gtx-480.c268)
- [TechPowerUp GTX 580 Specs](https://www.techpowerup.com/gpu-specs/geforce-gtx-580.c270)
- [TechPowerUp RTX 3090 Specs](https://www.techpowerup.com/gpu-specs/geforce-rtx-3090.c3622)
- [TechPowerUp RTX 4070 Specs](https://www.techpowerup.com/gpu-specs/geforce-rtx-4070.c3924)
- [TechPowerUp RTX 4090 Specs](https://www.techpowerup.com/gpu-specs/geforce-rtx-4090.c3889)
- [PassMark Video Card Benchmarks](https://www.videocardbenchmark.net)