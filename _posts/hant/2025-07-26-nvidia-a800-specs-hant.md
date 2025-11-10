---
audio: false
generated: true
lang: hant
layout: post
title: NVIDIA A800 GPU：A100 變體
translated: true
type: note
---

NVIDIA A800 是一款由 NVIDIA 開發的專業級圖形處理單元（GPU），主要針對高效能運算（HPC）、人工智能（AI）、數據科學及工作站工作流程而設計。它基於 NVIDIA Ampere 架構，採用 GA100 圖形處理器，並使用 7 納米製程製造。A800 於 2022 年 11 月推出，作為 NVIDIA A100 GPU 的變體版本，專門為符合美國對特定地區（如中國）先進 AI 晶片的出口限制而調整。與 A100 的主要區別在於降低的 NVLink 互連速度（A800 為 400 GB/s，A100 為 600 GB/s），這影響了多 GPU 擴展效能，但在單 GPU 任務中仍保持類似的核心性能。

### 關鍵規格（以 A800 PCIe 40GB 版本為例）：
- **CUDA 核心**：6,912
- **Tensor 核心**：432（第三代）
- **記憶體**：40 GB HBM2（高頻寬記憶體）；部分版本提供 80 GB
- **記憶體頻寬**：最高 1.55 TB/s
- **性能**：
  - 單精度（FP32）：最高 19.5 TFLOPS
  - 雙精度（FP64）：最高 9.7 TFLOPS
  - Tensor 性能（TF32）：最高 312 TFLOPS
- **介面**：PCIe 4.0 x16
- **功耗**：約 250-300W TDP（熱設計功耗）
- **外形規格**：提供被動或主動散熱版本，適用於伺服器及工作站

A800 在加速機器學習訓練、推論、科學模擬及視覺化等 demanding 任務方面表現卓越。在基準測試中，其性能通常為 A100 的 70-100%，具體取決於工作負載——在單精度和雙精度運算上幾乎相同，但在需要高速多 GPU 通訊的場景中，由於受限的 NVLink，性能會稍遜一籌。

變體版本包括 A800 40GB 主動散熱版（適用於工作站）及面向伺服器的型號如 A800 PCIe 80GB。此產品並非針對消費級遊戲，而是專為企業及專業用途設計。

[NVIDIA A800 40GB 主動散熱顯示卡](https://www.nvidia.com/en-us/design-visualization/a800/)  
[NVIDIA A800 PCIe 40 GB 規格](https://www.techpowerup.com/gpu-specs/a800-pcie-40-gb.c3964)  
[NVIDIA 推出 A800 GPU 以替代在中國禁售的 A100](https://analyticsdrift.com/nvidia-introduces-a800-gpu-chips-to-replace-banned-a100-chips-for-china/)  
[ThinkSystem NVIDIA A800 PCIe 4.0 GPU](https://lenovopress.lenovo.com/lp1813-thinksystem-nvidia-a800-pcie-gpu)  
[Nvidia AI 晶片：A100 A800 H100 H800 B200](https://www.fibermall.com/blog/nvidia-ai-chip.htm)