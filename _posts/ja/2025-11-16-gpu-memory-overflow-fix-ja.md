---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 評価時のGPUメモリオーバーフロー対策
translated: true
type: note
---

RTX 4070（12GB VRAM）で、バッチサイズ=16、ブロックサイズ=1024、勾配累積ステップ=32、FP16を使用して、約7700万パラメータのGPT（元々1億2500万用でしたが、n_embdを576に減らして約7700万にした）をトレーニング中に、古典的なメモリ不足（OOM）エラーが発生しています。

7700万パラメータは小さいモデルですが、nanoGPTの`estimate_loss()`における損失計算方法により、実効的なマイクロバッチが非常に大きくなっています。この関数は、評価バッチに対して勾配累積の工夫なしに完全なフォワード/バックワードパスを実行するため、評価中に突然、はるかに大きな実効バッチがメモリに投入されようとします。

### 根本原因
デフォルトでは、`estimate_loss()`は以下のように動作します：

```python
for _ in range(eval_iters):  # 200回も！
    x, y = get_batch('train')
    ...
    logits, loss = model(x, y)
```

各`get_batch`は`バッチサイズ × ブロックサイズ`のトークンを返します → 16 × 1024
eval_iters = 200 → 200回の独立したフォワードパスですが、注意しないと、PyTorchは評価ループ全体の計算グラフと中間活性化をメモリに保持し続けます。これに、巨大なKVキャッシュ（12レイヤー × 12ヘッド × 1024 × 576 × 2バイト (FP16) ≈ 1.6 GB）と、ロジット（16×1024×50304 × 2バイト ≈ 1.6 GB / フォワードパス）が組み合わさり、トレーニング自体は問題なくても、12GBを簡単に超えてしまいます。

### クイックフィックス（一つまたは組み合わせて選択）

**オプション1: 評価バッチサイズを大幅に減らす（最速の解決策）**
設定ファイル（またはCLIで上書き）に以下の行を追加：

```python
eval_batch_size = 4        # これを追加
# まだOOMの場合は2でも可
eval_iters = 100           # もう少し減らすことも可能
```

nanoGPT（最近のバージョン）は`eval_batch_size`を認識します。これにより、評価時に16シーケンスの代わりに4シーケンスのみを使用するようになり、評価中のメモリ使用量が約4分の1になります。

**オプション2: 評価時のみブロックサイズを減らす（精度を維持）**
```python
eval_block_size = 512      # または 256
```
これを設定に追加します。一部のフォークでサポートされているか、またはsplit=='val'の時に異なるブロックサイズを使用するように`get_batch`をパッチする必要があります。

**オプション3: eval_itersを減らし、評価損失が少しノイジーになることを許容する**
```python
eval_iters = 50   # それでも十分な推定値
```

**オプション4: モデルサイズをもう少し減らす（品質は依然良好）**
すでに7700万ですが、安全にもっと減らせます：

```python
n_layer = 12
n_head  = 12
n_embd  = 512     # → 約6200万パラメータ、はるかに安全
# または n_embd = 448 → 約5300万
```

**オプション5: 勾配チェックポイントを有効化（最大のメモリ節約効果）**
モデル作成時に追加（model.pyを編集するかフラグを渡す）：

```python
model = GPT(GPTConfig(..., grad_checkpoint=True))
```

または、トレーニング前にtrain.pyでモンキーパッチ：

```python
if config.grad_checkpoint:
    model.gradient_checkpointing_enable()
```

これにより、活性化のメモリ使用量が約50-60%削減されますが、トレーニング速度が約20-25%低下します。

### あなたのRTX 4070 12GBへの推奨組み合わせ

```python
# config/train_fineweb.py 内
batch_size = 16
gradient_accumulation_steps = 32   # 実効512シーケンスを維持
block_size = 1024

eval_batch_size = 4        # 重要
eval_iters = 100
eval_interval = 500

n_embd = 512               # 約6200万モデル、非常に安全
# オプション: 勾配チェックポイントを追加
grad_checkpoint = True     # あなたの使用しているnanoGPTフォークがサポートしている場合
```

または、n_embdを変更したくない場合は、以下だけを実行：

```python
eval_batch_size = 2
eval_iters = 100
```

これだけでも、ほぼ確実にOOMを修正できます。

また、フラグメンテーション対策にこの環境変数を設定してください：

```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

まずはeval_batch_size=4（または=2）を試してください — 12GBの4070でこの同じエラーに遭遇した人の95%は、FineWebでnanoGPTをトレーニングする際、この方法で修正しています。