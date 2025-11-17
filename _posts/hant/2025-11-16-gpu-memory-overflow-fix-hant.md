---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 解決評估期間的GPU記憶體溢出問題
translated: true
type: note
---

你在 RTX 4070（12 GB 顯存）上訓練一個約 77M 參數的 GPT 模型（原為 125M，但你將 n_embd 降至 576 → 約 77M）時，遇到了典型的記憶體不足問題。設定為 batch_size=16、block_size=1024、gradient_accumulation_steps=32 且使用 FP16 模式。

儘管 77M 模型規模不大，但由於 nanoGPT 在 `estimate_loss()` 中計算損失的方式，導致有效微批次規模變得巨大——它在評估批次上執行完整的正向/反向傳播，沒有使用梯度累積技巧，因此在評估期間會突然嘗試將更大的有效批次放入記憶體。

### 根本原因

在 `estimate_loss()` 中，nanoGPT 預設執行以下操作：

```python
for _ in range(eval_iters):  # 循環 200 次！
    x, y = get_batch('train')
    ...
    logits, loss = model(x, y)
```

每次 `get_batch` 返回 `batch_size × block_size` 個 token → 16 × 1024  
當 eval_iters = 200 → 200 次獨立的正向傳播，但 PyTorch 會將整個評估循環的計算圖和中間激活值保留在記憶體中（如果未妥善處理）。再加上巨大的 KV 快取（12 層 × 12 頭 × 1024 × 576 × 2 位元組 FP16 ≈ 1.6 GB，僅用於快取），以及 logits（16×1024×50304 × 2 位元組 ≈ 1.6 GB 每次正向傳播），即使訓練本身正常，你也很容易超過 12 GB 顯存。

### 快速解決方案（可單選或組合使用）

**選項 1：大幅降低評估批次大小（最快修復）**
在配置中添加以下行（或透過 CLI 覆寫）：

```python
eval_batch_size = 4        # 添加此行
# 如果仍記憶體不足，甚至可設為 2
eval_iters = 100           # 可再進一步降低
```

nanoGPT（近期版本）會遵循 `eval_batch_size` 設定。這使得評估時僅使用 4 個序列而非 16 個 → 評估期間記憶體使用減少約 4 倍。

**選項 2：僅降低評估用的 block_size（保持準確度）**
```python
eval_block_size = 512      # 或 256
```
將此加入配置——部分分支版本支援此設定，或者修補 `get_batch` 在 split=='val' 時使用不同的區塊大小。

**選項 3：降低 eval_iters 並接受稍具噪聲的評估損失**
```python
eval_iters = 50   # 仍能獲得合理的估計值
```

**選項 4：進一步縮小模型規模（仍保持良好品質）**
你已將模型降至 77M，但可以安全地進一步縮減：

```python
n_layer = 12
n_head  = 12
n_embd  = 512     # → 約 62M 參數，更安全
# 或甚至 n_embd = 448 → 約 53M
```

**選項 5：啟用梯度檢查點（記憶體節省效果最顯著）**
在模型創建時添加（編輯 model.py 或傳遞標誌）：

```python
model = GPT(GPTConfig(..., grad_checkpoint=True))
```

或在 train.py 中於訓練前進行猴子修補：

```python
if config.grad_checkpoint:
    model.gradient_checkpointing_enable()
```

這將減少約 50-60% 的激活記憶體使用，但代價是訓練速度降低約 20-25%。

### 針對你的 4070 12 GB 的推薦組合設定

```python
# 在 config/train_fineweb.py 中
batch_size = 16
gradient_accumulation_steps = 32   # 保持有效 512 序列
block_size = 1024

eval_batch_size = 4        # 關鍵設定
eval_iters = 100
eval_interval = 500

n_embd = 512               # 約 62M 模型，非常安全
# 可選：添加梯度檢查點
grad_checkpoint = True     # 如果你的 nanoGPT 分支支援
```

或者，如果你不想調整 n_embd，僅需：

```python
eval_batch_size = 2
eval_iters = 100
```

僅此設定幾乎肯定能解決記憶體不足問題。

同時設定以下環境變數以幫助減少記憶體碎片：

```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

首先嘗試 eval_batch_size=4（或 =2）——95% 使用 12 GB 4070 顯卡且在 FineWeb 上訓練 nanoGPT 時遇到此錯誤的使用者，透過這種方式解決了問題。