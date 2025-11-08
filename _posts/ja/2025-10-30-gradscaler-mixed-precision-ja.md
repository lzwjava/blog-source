---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 混合精度トレーニングのためのGradScaler
translated: true
type: note
---

`torch.cuda.amp.GradScaler`は、**Automatic Mixed Precision (AMP)**を使用した混合精度トレーニング中に**勾配を自動的にスケーリング**するために設計されたPyTorchユーティリティクラスです。`float16`（半精度）テンソルを使用する際に、勾配が正確に表現できなくなるほど小さくなる**アンダーフローを防止**します。

---

### `GradScaler`を使用する理由

混合精度トレーニングでは：
- **順方向/逆方向パス**は速度とメモリ節約のため`float16`を使用
- `float16`で計算された**勾配**は非常に小さくなる可能性 → **アンダーフローでゼロに**
- `GradScaler`は逆方向パスの前に**損失**を係数（例：2¹⁵ = 32768）でスケーリング
- 勾配は比例してスケーリング → 表現可能な範囲に維持
- オプティマイザステップの前に、勾配は**元のスケールに戻される**

---

### 基本的な使用方法

```python
import torch
from torch.cuda.amp import autocast, GradScaler

model = MyModel().cuda()
optimizer = torch.optim.Adam(model.parameters())
scaler = GradScaler()  # デフォルト init_scale=2**16

for data, target in dataloader:
    optimizer.zero_grad()

    # 1. 順方向のためのautocast
    with autocast():
        output = model(data)
        loss = loss_fn(output, target)

    # 2. 損失をスケーリングして逆方向伝播
    scaler.scale(loss).backward()

    # 3. スケール解除 + オプティマイザステップ
    scaler.step(optimizer)

    # 4. 次のイテレーションのためのスケール更新
    scaler.update()
```

---

### 主要なメソッド

| メソッド | 目的 |
|-------|--------|
| `scaler.scale(loss)` | `.backward()`の前に損失をスケーリング |
| `scaler.step(optimizer)` | 勾配のスケール解除と`optimizer.step()`の呼び出し |
| `scaler.update()` | 次のイテレーションのためのスケーリング係数を調整 |
| `scaler.unscale_(optimizer)` | 手動で勾配のスケール解除（まれに必要） |
| `scaler.get_scale()` | 現在のスケール係数を返す |

---

### スケーリングの仕組み（内部）

1. **初期スケール**: 通常`2**16 = 65536`
2. `backward()`後、勾配内の**inf/NaN**をチェック
3. **inf/NaNがない**場合 → 次回スケールを**増加**（例：×2）
4. **inf/NaNが見つかった**場合 → `optimizer.step()`をスキップ、**スケールを減少**（例：÷2）、後で再試行

これにより、オーバーフローが時々発生してもトレーニングが**ロバスト**になります。

---

### 一般的なパラメータ

```python
scaler = GradScaler(
    init_scale=2.**16,     # 開始スケール
    growth_factor=2.0,     # infなし時の乗算係数
    backoff_factor=0.5,    # inf発生時の除算係数
    growth_interval=2000,  # スケール増加前のステップ数
    enabled=True
)
```

---

### 勾配クリッピングの例

```python
scaler.scale(loss).backward()
scaler.unscale_(optimizer)  # クリッピング前にスケール解除が必要
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
scaler.step(optimizer)
scaler.update()
```

> **注意**: 勾配のクリッピングや検査の前には常に`unscale_`を実行してください。

---

### ベストプラクティス

- `torch.cuda.amp.autocast()`と併用
- `autocast()`内では**順方向 + 損失計算のみ**をラップ
- `scaler.update()`を**毎イテレーション**呼び出し
- 速度向上のため`torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction=True`を使用

---

### 使用しない場合

- 純粋な`float32`トレーニング
- CPUトレーニング
- スケーリングを手動で処理するカスタムトレーニングループ

---

### 公式ドキュメント

[https://pytorch.org/docs/stable/amp.html#torch.cuda.amp.GradScaler](https://pytorch.org/docs/stable/amp.html#torch.cuda.amp.GradScaler)

---

完全なトレーニングループの例や手動スケーリングとの比較が必要な場合はお知らせください！