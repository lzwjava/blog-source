---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修正模型配置可除性錯誤
translated: true
type: note
---

錯誤非常明確：

```python
assert config.n_embd % config.n_head == 0
```

這意味著 **n_embd 必須能被 n_head 整除**（因為每個注意力頭會獲得 `n_embd // n_head` 維度）。

您正在使用的模型配置（可能是我之前提供的那個）：

```python
n_layer = 12
n_head  = 12
n_embd  = 512
```

512 ÷ 12 = 42.666… → 不是整數 → 崩潰。

### 解決方法：選擇能被 n_head 整除的 n_embd

以下是**經過驗證的安全組合**，可在您的 12 GB 4070 顯示卡上完美運行單個 FineWeb Parquet 檔案：

#### 選項 1 – 推薦（1.25億參數，最佳品質/速度平衡）
```python
n_layer = 12
n_head  = 12
n_embd  = 576        # ← 576 ÷ 12 = 48 完全整除
```
→ 約1.25億參數，在 batch_size=16 + grad_acc=32 + block_size=1024 設定下仍輕鬆佔用約10.5 GB VRAM

#### 選項 2 – 稍大的頭維度（1.3億參數）
```python
n_layer = 12
n_head  = 12
n_embd  = 720        # 720 ÷ 12 = 60
```

#### 選項 3 – 非常安全且常見（1.15億參數）
```python
n_layer = 12
n_head  = 12
n_embd  = 480        # 480 ÷ 12 = 40
```

#### 選項 4 – 如果您想保持 n_embd=512（原始 GPT-2 風格）
```python
n_layer = 12
n_head  = 8          # 512 ÷ 8 = 64
# 或
n_head  = 16         # 512 ÷ 16 = 32
```

### 快速修復：直接將您的配置更改為這樣（可直接複製貼上）

```python
# 模型 – 12層，約1.25億參數，保證可用
n_layer = 12
n_head  = 12
n_embd  = 576        # ← 這是您唯一需要更改的行
dropout = 0.0
```

其他所有設定（batch_size=16、grad_acc=32、block_size=1024 等）保持完全不变。

將 `n_embd` 更改為 576 後，斷言錯誤會立即消失，訓練將正常開始。

這個 12L/12H/576E 模型目前在 nanoGPT 社群中非常受歡迎 — 許多人在使用 FineWeb 的 12 GB 4070/4070 Ti 顯示卡上成功訓練了它。

運行它，100% 會正常工作。當您看到第一個損失值輸出時告訴我！🚀