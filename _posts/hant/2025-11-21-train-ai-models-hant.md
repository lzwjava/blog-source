---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4.1-fast
title: 以12GB VRAM訓練AI模型
translated: true
type: note
---

以下是一些真正「硬核」的開源專案，你可以在單張 RTX 4070（12 GB 顯示記憶體）上完整訓練（或微調大部分內容）。它們非常適合深入理解底層運作原理——遠超僅僅運行示範。

| 專案 | 類型 | 為何具教育意義且硬核 | 訓練所需約略顯示記憶體 | 在 4070 上的約略訓練時間 | 連結 |
|---------|------|----------------------------------|-------------------------------------|-----------------------------|------|
| Karpathy 的 **nanoGPT**（你已熟悉）| LLM（從零開始的 GPT-2 風格）| 黃金標準「極簡潔程式碼」GPT | ~10 GB（適用於 124M 模型）| 數小時 | https://github.com/karpathy/nanoGPT |
| Karpathy 的 **minGPT** | LLM | 更輕量，極適合逐行除錯 | <6 GB | 數分鐘至數小時 | https://github.com/karpathy/minGPT |
| Karpathy 的 **llm.c** | 純 CUDA GPT-2 | 完全使用原始 CUDA 訓練一個像樣的 GPT-2（無 PyTorch）。對底層 GPU 程式設計極具教育意義 | 8–10 GB（124M 模型）| 1–3 天（124M 於莎士比亞資料集）| https://github.com/karpathy/llm.c |
| OpenLLaMA / LLaMA-Adapter / Lit-GPT（微調）| LLM 微調 | 使用 LoRA/QLoRA 在單張 4070 上微調 3B–7B 模型 | 7B QLoRA ≈ 8–10 GB | 數小時（於 Alpaca/ShareGPT）| https://github.com/Lightning-AI/lit-gpt |
| Hiero **OpenDiT** / **PixArt-alpha** | 基於 DiT 的文字生成影像（從零訓練的 Stable Diffusion 替代方案）| 從零訓練 Diffusion Transformer 而非 U-Net。現代 SOTA 架構 | 24M DiT ≈ 10–11 GB（含梯度檢查點）| 1–2 週（於 LAION 美學子集）| https://github.com/NVIDIA/OpenDiT |
| **從零開始的 Stable Diffusion**（輕量版）| U-Net 擴散模型 | 多個程式庫允許訓練輕量 SD 模型（而非僅微調）| 64×64 輕量 SD ≈ 6–9 GB | 數天 | https://github.com/tea-mang/nano-diffusion, https://github.com/huggingface/diffusers（參見訓練範例）|
| **BitNet**（1-bit Transformers）| 1-bit LLM | 微軟的 1-bit 權重模型。訓練你自己的 BitNet b1.58（類似 LLaMA 但使用三元權重）| 3B 模型僅需 <6 GB | 數小時至數天 | https://github.com/microsoft/BitNet |
| **Mamba**（狀態空間模型）| Transformers 的次世代架構 | 熱門的 Transformers 替代方案。從零訓練你自己的 Mamba | 130M–2.8B 模型輕鬆容納 | 數小時 | https://github.com/state-spaces/mamba（含訓練指令碼）|
| **RWKV**（具 Transformers 擴展能力的 RNN）| Raven / Eagle / Finch 模型 | 訓練真正循環模型，行為類似 Transformer 但使用固定顯示記憶體 | 3B–7B 訓練可在 12 GB 上透過分塊技術實現 | 數天 | https://github.com/BlinkDL/RWKV-LM |
| **Grok-1** 開放權重克隆嘗試（340B 專家混合模型）| 從零理解 MoE | 雖無法訓練完整 314B 模型，但可訓練輕量 MoE 版本並理解路由機制 | 8 專家輕量 MoE ≈ 10 GB | 數小時 | https://github.com/cg123/mergekit（構建你自己的 Frankenstein MoE）+ https://github.com/EleutherAI/gpt-neox（含 MoE 程式碼）|
| **RetNet**（微軟的 Transformer 替代方案）| 保留網絡 | 另一個強大的 Transformer 替代方案 | 與 Mamba 相似 | | https://github.com/microsoft/torchscale（含 RetNet 訓練）|

### 我個人推薦的「最具教育意義且可在 4070 上實現」前五名

1. **llm.c** – 使用純 C+CUDA 訓練 GPT-2。沒有比這更能教你理解反向傳播、核心程式與閃電注意力實作的方式。
2. **Mamba** – 因為狀態空間模型很可能代表未來，且程式碼簡潔。
3. **BitNet b1.58** – 訓練 1-bit LLM 令人驚嘆且顯示記憶體效率極高。
4. **OpenDiT / PixArt-alpha** – 如果你想要擴散模型，但採用現代 Transformer 骨幹而非 2015 年的 U-Net。
5. **RWKV** – 循環架構，擊敗同規模 Transformers 且訓練線性增長。

所有專案均可在單張 RTX 4070 上流暢運行（有時需搭配閃電注意力、bitsandbytes/QLORA、梯度檢查點或最新的 RWKV 分塊技巧）。

選擇一個深入鑽研——你將對這些模型的理解達到多數研究人員未曾觸及的層次。編程愉快！