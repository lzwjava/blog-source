---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: アンナプルナ・ラボ： AWS カスタムシリコン
translated: true
type: note
---

### Annapurna Labsとは

**Annapurna Labs**は、クラウドコンピューティング、ネットワーキング、ストレージ、AIワークロード向けの**高性能でエネルギー効率の高いプロセッサ**を専門とするイスラエルの半導体企業です。**2015年1月にAmazonに約3億5000万～3億7000万ドルで買収**され、現在は**Amazon Web Services (AWS)** の完全子会社として運営されています。

Annapurna Labsは、AWSインフラの多くを支える**カスタムシリコン**を設計しており、Amazonが特定のワークロードにおいてIntel、Broadcom、NVIDIAなどのサードパーティ製チップベンダーへの依存を軽減することを可能にしています。

---

### Annapurna Labsが設計した主要チップ (AWSで使用)

| チップファミリー | 種類 | 主な特徴 | AWSでの主な使用例 |
|-------------|------|--------------|-----------------------|
| **Alpine** | ARMベースSoC | マルチコアARMv8 CPU、低消費電力、統合ネットワーキング/ストレージ | 初期のEC2インスタンス、ストレージコントローラー |
| **Graviton** | ARMベースCPU | 64ビットARM Neoverseコア (AWS設計)、高コア数、DDR5、PCIe Gen4/5 | **EC2 Gravitonインスタンス** (汎用コンピュート) |
| **Nitro** | SmartNIC / オフロード | ARM CPU + 仮想化、セキュリティ、ストレージ、ネットワーキング向けカスタムアクセラレーター | **EC2 Nitro System**、EBS、VPC、セキュリティオフロード |
| **Inferentia** | AI推論 | 高スループットなテンソル処理、低レイテンシ、ニューロンコア | **EC2 Inf1/Inf2インスタンス** (ML推論用) |
| **Trainium** | AI学習 | 大規模言語モデル向けにスケーラブル、高メモリ帯域幅、NeuronLinkインターコネクト | **EC2 Trn1/Trn2インスタンス** (LLM学習用) |

---

### 主要チップファミリー (2025年現在)

#### 1. **AWS Graviton (CPU)**
- **アーキテクチャ**: カスタムARM Neoverseベースコア (既製品ではない)
- **世代**:
  - **Graviton1** (2018): 16コア ARMv8、A1インスタンスで使用
  - **Graviton2** (2020): 64コア Neoverse N1、x86比で約40%優れた価格性能比
  - **Graviton3** (2022): Neoverse V1、DDR5、bfloat16、Graviton2比最大60%向上
  - **Graviton4** (2024): Neoverse V2、96コア、Graviton3比2.7倍の性能/ワット
- **用途**: **AWS EC2ワークロードの約30～40%** (特にコンテナ、マイクロサービス、データベース) を駆動

#### 2. **AWS Inferentia (AI推論)**
- **Inferentia2** (2023): Inferentia1比4倍の性能、FP16/BF16/INT8をサポート
- **リアルタイム推論** (レコメンデーションエンジン、音声、画像) に最適化
- **SageMaker**、**EC2 Inf2** で使用

#### 3. **AWS Trainium (AI学習)**
- **Trainium2** (2024年発表、2025年出荷予定): Trainium1比4倍の学習性能
- LLM学習において **NVIDIA H100** と競合するように設計
- **数兆パラメータモデル**、高帯域幅メモリ (HBM) をサポート

#### 4. **Nitro System (SmartNIC / DPU)**
- ハードウェアアクセラレーターを搭載したカスタムARM SoC
- ハイパーバイザ、ネットワーキング、ストレージ、暗号化をオフロード
- 仮想化環境における**ベアメタル性能**を実現

---

### Annapurnaが重要な理由

- **コストと効率性**: AWSはx86比で**最大40%優れた価格性能比**を主張
- **垂直統合**: Amazonがシリコンを管理 → より迅速な革新、低コスト化
- **AI推進**: Trainium/InferentiaはクラウドAIにおけるNVIDIAの支配に直接挑戦
- **サプライチェーン強靭化**: Intel/TSMCのみの供給への依存を軽減

---

### まとめ

> **Annapurna Labs = AWSの秘密のシリコン兵器。**  
> 彼らは**ARMベースのGraviton CPU**、**Inferentia (推論)**、**Trainium (学習)**、**Nitroオフロードチップ**を構築 — これらはすべてクラウド向けに最適化されています。  
> これらは**より安価で、高速で、環境負荷の小さい**AWSサービスを支え、AWSが価格で競合他社を凌駕しながらAIをスケールできる主要な理由です。

特定のチップ (例: Graviton4 vs Apple M4, Trainium2 vs H100) について詳しく知りたい場合は、お知らせください。