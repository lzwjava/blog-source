---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4.1-fast
title: 12GB VRAMでのAIモデル学習
translated: true
type: note
---

以下は、単一のRTX 4070（12GB VRAM）で完全に（あるいは大部分を）学習（またはファインチューニング）できる、真に「ハードコア」なオープンソースプロジェクトです。これらは、単にデモを実行するだけではなく、内部で実際にどのように動作するかを深く理解するのに優れています。

| プロジェクト | 種類 | 教育的かつハードコアな理由 | 学習に必要な概算VRAM | 4070での概算学習時間 | リンク |
|---------|------|----------------------------------|-------------------------------------|-----------------------------|------|
| Karpathyの **nanoGPT** (既知) | LLM (GPT-2スタイル, スクラッチから) | 「最小限でクリーンなコード」のゴールドスタンダードGPT | ～10 GB (124Mモデル) | 数時間 | https://github.com/karpathy/nanoGPT |
| Karpathyの **minGPT** | LLM | さらに小さく、各行をデバッグするのに最適 | <6 GB | 数分～数時間 | https://github.com/karpathy/minGPT |
| Karpathyの **llm.c** | 生のCUDA GPT-2 | まともなGPT-2を生のCUDAで完全に学習（PyTorch不使用）。低レベルGPUプログラミングにとって非常に教育的 | 8–10 GB (124Mモデル) | 124Mモデルでシェイクスピアデータ1–3日 | https://github.com/karpathy/llm.c |
| OpenLLaMA / LLaMA-Adapter / Lit-GPT (ファインチューニング) | LLM ファインチューニング | 3B–7BモデルをLoRA/QLoRAで単一の4070でファインチューニング | 7B QLoRA ≈ 8–10 GB | Alpaca/ShareGPTで数時間 | https://github.com/Lightning-AI/lit-gpt |
| Hiero **OpenDiT** / **PixArt-alpha** | DiTベースのテキストから画像へ (Stable Diffusionの代替, スクラッチから学習) | U-Netの代わりにDiffusion Transformerをスクラッチから学習。現代のSOTAアーキテクチャ | 24M DiT ≈ 10–11 GB (勾配チェックポイント使用) | LAION aestheticsサブセットで1–2週間 | https://github.com/NVIDIA/OpenDiT |
| **Stable Diffusion from scratch** (小型版) | U-Net diffusion | 小型SDモデルを（単なるファインチューニングではなく）学習できるリポジトリが複数存在 | 64×64 小型 SD ≈ 6–9 GB | 数日 | https://github.com/tea-mang/nano-diffusion, https://github.com/huggingface/diffusers (学習例を参照) |
| **BitNet** (1-bit Transformers) | 1-bit LLM | Microsoftの1-bit重みモデル。独自のBitNet b1.58を学習（LLaMAに似ているが3値重み） | 3Bモデルが <6 GBに収まる | 数時間～数日 | https://github.com/microsoft/BitNet |
| **Mamba** (状態空間モデル) | Transformerの次世代アーキテクチャ | Transformerに対する非常に注目の代替案。独自のMambaをスクラッチから学習 | 130M–2.8Bモデルが容易に収まる | 数時間 | https://github.com/state-spaces/mamba (学習スクリプト含む) |
| **RWKV** (TransformerのようにスケールするRNN) | Raven / Eagle / Finch モデル | Transformerのように振る舞うが、一定のVRAMを使用する真のリカレントモデルを学習 | 3B–7B学習が12GBで可能 (chunkwise使用) | 数日 | https://github.com/BlinkDL/RWKV-LM |
| **Grok-1** オープンウェイトクローン試行 (340B 混合エキスパート) | MoE スクラッチ理解 | 完全な314Bは学習できないが、小型MoE版を学習しルーティングを理解可能 | 8エキスパート小型MoE ≈ 10 GB | 数時間 | https://github.com/cg123/mergekit (独自のFrankenstein MoEを構築) + https://github.com/EleutherAI/gpt-neox (MoEコード用) |
| **RetNet** (MicrosoftのTransformer代替) | リテンションネットワーク | もう一つの強力なTransformer代替案 | Mambaと同様 | | https://github.com/microsoft/torchscale (RetNet学習含む) |

### 私の個人的なトップ5「最も教育的で4070で実行可能」ランキング

1.  **llm.c** – GPT-2を純粋なC+CUDAで学習。逆伝播、カーネル、Flash Attentionの実装をこれ以上なく理解させてくれる。
2.  **Mamba** – 状態空間モデルはおそらく未来であり、コードがクリーンだから。
3.  **BitNet b1.58** – 1-bit LLMの学習は衝撃的で、非常にVRAM効率が良い。
4.  **OpenDiT / PixArt-alpha** – Diffusionを、2015年のU-Netではなく現代のTransformerバックボーンで学びたい場合。
5.  **RWKV** – 同じサイズのTransformerを凌駕し、線形に学習するリカレントアーキテクチャ。

これらはすべて、単一のRTX 4070で快適に実行されます（場合によっては、flash-attention、bitsandbytes/QLoRA、勾配チェックポイント、または新しいchunkwise RWKVの技法を使用します）。

一つを選んで深く掘り下げてください。多くの研究者さえ到達しないレベルでこれらのモデルを理解できるようになるでしょう。ハッピーハッキング！