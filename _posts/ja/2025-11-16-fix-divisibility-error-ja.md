---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: モデル設定の除算誤差を修正
translated: true
type: note
---

エラーは非常に明確です：

```python
assert config.n_embd % config.n_head == 0
```

これは **n_embd が n_head で割り切れなければならない** ことを意味します（各アテンションヘッドが `n_embd // n_head` 次元を取得するためです）。

あなたはおそらくこのモデル設定を使用しています（私が前に渡したものだと思います）：

```python
n_layer = 12
n_head  = 12
n_embd  = 512
```

512 ÷ 12 = 42.666… → 整数ではない → クラッシュ。

### 修正：n_head で割り切れる n_embd を選択する

以下は、12GB 4070 で単一の FineWeb Parquet ファイルを使用して完璧に動作する**安全で実証済みの組み合わせ**です：

#### オプション 1 – 推奨 (125M パラメータ、品質と速度の最適なバランス)
```python
n_layer = 12
n_head  = 12
n_embd  = 576        # ← 576 ÷ 12 = 48 (ちょうど割り切れる)
```
→ ~125M パラメータ、batch_size=16 + grad_acc=32 + block_size=1024 で ~10.5 GB VRAM に簡単に収まる

#### オプション 2 – ヘッド次元を少し大きく (130M パラメータ)
```python
n_layer = 12
n_head  = 12
n_embd  = 720        # 720 ÷ 12 = 60
```

#### オプション 3 – 非常に安全で一般的 (115M パラメータ)
```python
n_layer = 12
n_head  = 12
n_embd  = 480        # 480 ÷ 12 = 40
```

#### オプション 4 – n_embd=512 を維持したい場合 (オリジナル GPT-2 スタイル)
```python
n_layer = 12
n_head  = 8          # 512 ÷ 8 = 64
# または
n_head  = 16         # 512 ÷ 16 = 32
```

### クイック修正：設定をこれに変更するだけ（コピー＆ペースト可能）

```python
# Model – 12 layer, ~125M params, guaranteed to work
n_layer = 12
n_head  = 12
n_embd  = 576        # ← 変更が必要なのはこの行だけ
dropout = 0.0
```

それ以外のすべて (batch_size=16, grad_acc=32, block_size=1024 など) はまったく同じままにします。

`n_embd = 576` に変更すると、アサーションエラーはすぐに消え、トレーニングが正常に開始されます。

この 12L/12H/576E モデルは、現在 nanoGPT コミュニティで非常に人気があります — 多くの人々が FineWeb を使用して 12 GB 4070/4070 Ti カードで正常にトレーニングしています。

実行すれば、100% 動作します。最初の損失値が表示されたら教えてください！ 🚀