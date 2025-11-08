---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 混合精度訓練的梯度縮放器
translated: true
type: note
---

`torch.cuda.amp.GradScaler` 是 PyTorch 的實用類別，專為在使用**自動混合精度 (AMP)** 的混合精度訓練期間**自動縮放梯度**而設計。它有助於防止使用 `float16`（半精度）張量時梯度出現下溢，否則梯度可能會變得過小而無法準確表示。

---

### 為何使用 `GradScaler`？

在混合精度訓練中：
- **前向/反向傳播**使用 `float16` 以節省速度和記憶體。
- 以 `float16` 計算的**梯度**可能變得非常小 → **下溢至零**。
- `GradScaler` 在反向傳播前將**損失**按係數（例如 2¹⁵ = 32768）縮放。
- 梯度按比例縮放 → 保持在可表示的範圍內。
- 在優化器步驟之前，梯度會被**還原**至正常範圍。

---

### 基本用法

```python
import torch
from torch.cuda.amp import autocast, GradScaler

model = MyModel().cuda()
optimizer = torch.optim.Adam(model.parameters())
scaler = GradScaler()  # 預設 init_scale=2**16

for data, target in dataloader:
    optimizer.zero_grad()

    # 1. 使用 autocast 進行前向傳播
    with autocast():
        output = model(data)
        loss = loss_fn(output, target)

    # 2. 縮放損失並執行反向傳播
    scaler.scale(loss).backward()

    # 3. 還原梯度 + 優化器步驟
    scaler.step(optimizer)

    # 4. 更新縮放因子以用於下一次迭代
    scaler.update()
```

---

### 主要方法

| 方法 | 用途 |
|-------|--------|
| `scaler.scale(loss)` | 在 `.backward()` 前縮放損失 |
| `scaler.step(optimizer)` | 還原梯度並呼叫 `optimizer.step()` |
| `scaler.update()` | 調整下一次迭代的縮放因子 |
| `scaler.unscale_(optimizer)` | 手動還原梯度（較少使用） |
| `scaler.get_scale()` | 返回當前縮放因子 |

---

### 縮放工作原理（內部）

1. **初始縮放**：通常為 `2**16 = 65536`
2. 在 `backward()` 後，檢查梯度中的 **inf/NaN**。
3. 如果**沒有 inf/NaN** → 下次縮放可能**增加**（例如 ×2）。
4. 如果**發現 inf/NaN** → 跳過 `optimizer.step()`，**降低縮放**（例如 ÷2），並稍後重試。

這使得訓練對偶爾的溢出具有**魯棒性**。

---

### 常用參數

```python
scaler = GradScaler(
    init_scale=2.**16,     # 起始縮放值
    growth_factor=2.0,     # 無 inf 時乘以係數
    backoff_factor=0.5,    # 有 inf 時除以係數
    growth_interval=2000,  # 增加縮放前的步數
    enabled=True
)
```

---

### 梯度裁剪範例

```python
scaler.scale(loss).backward()
scaler.unscale_(optimizer)  # 裁剪前需還原梯度
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
scaler.step(optimizer)
scaler.update()
```

> **注意**：在裁剪或檢查梯度之前，務必先執行 `unscale_`。

---

### 最佳實踐

- 與 `torch.cuda.amp.autocast()` 一起使用
- 僅將**前向傳播 + 損失**包裝在 `autocast()` 中
- **每次迭代**都呼叫 `scaler.update()`
- 使用 `torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction=True` 以提升速度

---

### 不適用的情況

- 純 `float32` 訓練
- CPU 訓練
- 手動處理縮放的自訂訓練循環

---

### 官方文件

[https://pytorch.org/docs/stable/amp.html#torch.cuda.amp.GradScaler](https://pytorch.org/docs/stable/amp.html#torch.cuda.amp.GradScaler)

---

如需完整的訓練循環範例或與手動縮放的比較，請告訴我！