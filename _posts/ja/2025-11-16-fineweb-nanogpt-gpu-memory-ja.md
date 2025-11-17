---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: FineWeb NanoGPT GPUメモリガイド
translated: true
type: note
---

限られたGPUメモリ（おそらく16〜24 GB、RTX 3090/4090やA6000など）で、**FineWeb**データセット（LLaMAやMistralのトレーニングに使用されたCommon Crawlのクリーン版100Bトークン）を使って小さなGPT（nanoGPTスタイル）をトレーニングしている状況です。

現在の設定はすでに控えめで、単一のコンシューマーGPUには適していますが、**nanoGPTをFineWebで使用する際の最適なパラメータ選択方法**について、重要度とメモリへの影響順に詳しく説明します。

### GPUメモリ別の推奨設定

| GPU VRAM       | モデルサイズ（パラメータ） | n_layer | n_head | n_embd | batch_size | grad_acc | 実効BS | block_size | 備考 |
|----------------|---------------------|---------|--------|--------|------------|----------|--------------|------------|-------|
| 80 GB (A100/H100) | ~350M              | 12      | 12     | 768    | 64         | 8        | 512          | 1024       | 元のGPT-2 mediumに近く、良好にトレーニング |
| 48 GB (A6000/3090) | ~250–300M         | 12      | 12     | 672    | 32         | 16       | 512          | 1024       | 非常に良いバランス |
| 24 GB (4090/3090) | ~160–200M          | 10      | 10     | 640    | 32         | 12–16    | 384–512      | 1024       | 最適な設定 |
| 16–20 GB (4080, 3090 Ti) | ~125M        | 8       | 8      | 512    | 32         | 12       | 384          | 1024       | 安定 |
| <16 GB (4070 Ti, etc.) | ~84M           | 6       | 6      | 384    | 16–32      | 16–24    | 256–512      | 512–1024   | 現在の設定 |

現在の設定（`6L 6H 384embd`）は安全ですが、少し小さいです。より大きくすることができます。

### 24 GB GPU (RTX 4090 / 3090) でのFineWeb用最適設定
これは現在のnanoGPTコミュニティで最も人気のあるセットアップです：

```python
out_dir = 'out-fineweb-160M'
eval_interval = 1000
eval_iters = 200
log_interval = 100
always_save_checkpoint = True

wandb_log = True
wandb_project = 'fineweb'
wandb_run_name = '160M-fineweb'

dataset = 'fineweb'
gradient_accumulation_steps = 16   # 32 * 16 = 512 実効バッチサイズ
batch_size = 32
block_size = 1024                  # 重要: FineWebは1024+でトレーニングされました

n_layer = 10
n_head = 10
n_embd = 640
dropout = 0.0                      # 後で0.1を試すことも可能
learning_rate = 6e-4               # 小さなモデルでは少し高め
max_iters = 50000                  # 合計〜50–100Bトークンが理想的
warmup_iters = 2000
lr_decay_iters = 50000
min_lr = 6e-5
beta2 = 0.99
```

→ これは約160Mパラメータで、4090で快適に動作し、VRAM使用量は約20–22 GBです。

### さらに良い: 200M+ モデル (24 GB+ の場合)
```python
n_layer = 12
n_head = 12
n_embd = 768    # → ~350M パラメータ (元のGPT-2 mediumサイズ)
batch_size = 32
gradient_accumulation_steps = 16   # 実効BS 512
block_size = 1024
learning_rate = 5e-4
max_iters = 60000
```
多くの人が単一の4090でこれを正常にトレーニングしています。

### FineWeb + nanoGPT のための重要な経験則

1. **block_size = 1024** を強く推奨  
   FineWebは1024コンテキストでフィルタリングおよびトレーニングされました。512を使用すると、思っている以上にパープレキシティが悪化します。

2. **実効バッチサイズ ≈ 512** が最適  
   元のLLaMAはバッチあたり約4Mトークンを使用しました。nanoGPTの場合、512シーケンス × 1024トークン = 約0.5Mトークン/バッチ → スケーリング則に十分近い値です。

3. **学習率**  
   - ~100M パラメータ: 6e–8e-4  
   - ~350M パラメータ: 5e–6e-4  
   - ~770M パラメータ: 3e-4  

4. **少なくとも50Bトークン（できれば100B+）トレーニングする**  
   160Mモデルの場合：  
   - 50k iters × 32 × 16 × 1024 トークン = ~83B トークン  
   良好な収束が得られます。

5. **公式のFineWebデータセットを使用（openwebtextではない）**  
   スクリプトはすでに正しいです：  
   FineWebは品質でOpenWebTextを上回ります。  
   100Bサブセット：`fineweb100B` またはフル `fineweb`（ディスク容量に応じて切り詰めて）を使用してください。

6. **オプションですが有用**
```python
compile = True          # PyTorch 2.0 compile, ~20–30% 高速化
bias = False            # Linear層でのバイアスなし (LLaMAのように)
weight_decay = 0.1
```

### FineWeb (100B版) ダウンロード用クイックコマンド
```bash
pip install datasets
python -c "
from datasets import load_dataset
ds = load_dataset('HuggingFaceFW/fineweb', name='sample-100BT', split='train')
ds.save_to_disk('data/fineweb100B')
"
```
その後、nanoGPTをそのフォルダに向けてください。

### まとめ: 現在の設定をアップグレード
現在のモデル部分を以下に置き換えてください（24 GB GPU用）：

```python
n_layer = 10
n_head = 10
n_embd = 640
batch_size = 32
gradient_accumulation_steps = 16
block_size = 1024
learning_rate = 6e-4
max_iters = 50000
```

ほとんど追加コストなしで、はるかに強力なモデルが得られます。

これらの設定で、FineWeb上で**非常に優れた160M–350Mモデル**が得られています — 多くの場合、元のGPT-2の性能を凌駕します。

使用している正確なGPUを教えていただければ、最適な設定をお伝えします！ 🚀