---
audio: false
generated: true
lang: ja
layout: post
title: NVIDIA A800 GPU：A100の派生モデル
translated: true
type: note
---

NVIDIA A800は、NVIDIAが開発したプロフェッショナル向けグラフィックスプロセッシングユニット（GPU）であり、主にハイパフォーマンスコンピューティング（HPC）、人工知能（AI）、データサイエンス、ワークステーションワークフロー向けに設計されています。NVIDIA Ampereアーキテクチャを基盤としており、7nmプロセスで製造されたGA100グラフィックスプロセッサを採用しています。A800は2022年11月に、特定の地域（中国など）への先進的AIチップの米国輸出規制に準拠するために特別に調整された、NVIDIA A100 GPUの亜種として導入されました。A100との主な違いは、NVLink相互接続速度の低下（A800で400GB/s、A100で600GB/s）であり、これはマルチGPUスケーリングに影響を与えますが、シングルGPUタスクにおけるコア性能は同程度を維持しています。

### 主な仕様（例: A800 PCIe 40GB バリアント）
- **CUDAコア**: 6,912
- **Tensorコア**: 432 (第3世代)
- **メモリ**: 40 GB HBM2 (高帯域メモリ); 80 GBを提供するバリアントもあり
- **メモリ帯域幅**: 最大 1.55 TB/s
- **性能**:
  - 単精度 (FP32): 最大 19.5 TFLOPS
  - 倍精度 (FP64): 最大 9.7 TFLOPS
  - Tensor性能 (TF32): 最大 312 TFLOPS
- **インターフェース**: PCIe 4.0 x16
- **消費電力**: 約 250-300W TDP (熱設計電力)
- **フォームファクタ**: サーバーおよびワークステーション向けのパッシブまたはアクティブ冷却バージョンで利用可能

A800は、機械学習トレーニング、推論、科学技術シミュレーション、可視化などの要求の厳しいタスクの高速化に優れています。ベンチマークでは、その性能はワークロードに応じてA100の70〜100%の範囲に収まることが多く、単精度および倍精度演算ではほぼ同等ですが、高速なマルチGPU通信を必要とするシナリオでは、抑制されたNVLinkにより遅延が生じます。

バリアントには、A800 40GB Active (アクティブ冷却を備えたワークステーション向け) や、A800 PCIe 80GBなどのサーバー向けモデルが含まれます。コンシューマー向けゲーミングではなく、エンタープライズおよびプロフェッショナル用途を目的としています。

[NVIDIA A800 40GB Active グラフィックスカード](https://www.nvidia.com/en-us/design-visualization/a800/)  
[NVIDIA A800 PCIe 40 GB 仕様](https://www.techpowerup.com/gpu-specs/a800-pcie-40-gb.c3964)  
[NVIDIA、中国向けに禁止されたA100の代替としてA800 GPUを導入](https://analyticsdrift.com/nvidia-introduces-a800-gpu-chips-to-replace-banned-a100-chips-for-china/)  
[ThinkSystem NVIDIA A800 PCIe 4.0 GPU](https://lenovopress.lenovo.com/lp1813-thinksystem-nvidia-a800-pcie-gpu)  
[Nvidia AIチップ: A100 A800 H100 H800 B200](https://www.fibermall.com/blog/nvidia-ai-chip.htm)