---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 理解 PyTorch 丟棄層
translated: true
type: note
---

### 理解 `drop = nn.Dropout(config.dropout)`

在 PyTorch（一個流行的深度學習庫）中，`nn.Dropout` 是一個內建模組，用於在模型訓練期間應用 **dropout 正則化**。這種技術通過在每次前向傳播時隨機「丟棄」（即設為零）張量中的一部分輸入元素，來幫助防止過擬合。它僅在訓練期間激活；在評估/推理期間，它不會丟棄任何元素，並縮放剩餘值以維持預期的輸出幅度。

分解你的代碼行：
```python
drop = nn.Dropout(config.dropout)
```
- `nn.Dropout`：這是 PyTorch 中 dropout 層的類。
- `config.dropout`：這通常是一個來自配置物件/字典的浮點數值（例如 0.1 或 0.5），代表 **dropout 概率** `p`。它表示「丟棄此比例的元素」。
  - 例如，如果 `config.dropout = 0.2`，則輸入中 20% 的元素將被隨機設為零。
- `drop = ...`：這創建了一個 dropout 模組的實例，並將其賦值給變數 `drop`。然後你可以像在神經網路中使用任何其他層一樣使用它（例如，在 `nn.Sequential` 或 forward 方法中）。

#### 當你呼叫 `drop(x)` 時 Dropout 如何運作
不，`drop(x)` 並 **不** 意味著「將所有元素設為 0」。相反：
- 它接受一個輸入張量 `x`（例如，來自前一層的激活值）。
- 根據概率 `p`（來自 `config.dropout`）**隨機** 選擇要丟棄的元素。
  - 被丟棄的元素設為 0。
  - 未被丟棄的元素按 `1 / (1 - p)` 縮放，以保持總和的期望值不變（這避免了訓練期間的下溢問題）。
- 這 **僅在訓練期間**（`model.train()` 模式）發生。在評估模式（`model.eval()`）下，它會直接傳遞 `x` 而不做更改。
- 範例：如果 `x` 是一個像 `[1.0, 2.0, 3.0, 4.0]` 的張量，且 `p=0.5`，一個可能的輸出可能是 `[0.0, 4.0, 0.0, 8.0]`（50% 被丟棄，倖存者縮放 2 倍）。但由於是隨機的，每次結果都會不同。

#### 簡單代碼範例
這是一個最小的 PyTorch 程式碼片段來說明：
```python
import torch
import torch.nn as nn

# 假設 config.dropout = 0.5 (50% dropout)
config = type('Config', (), {'dropout': 0.5})()
drop = nn.Dropout(config.dropout)

# 樣本輸入張量
x = torch.tensor([1.0, 2.0, 3.0, 4.0])

# 訓練期間
torch.manual_seed(42)  # 為了可重現性
print(drop(x))  # 可能輸出: tensor([0., 0., 0., 8.])  # 隨機丟棄 + 縮放

# 評估期間
drop.eval()
print(drop(x))  # 輸出: tensor([1., 2., 3., 4.])  # 無更改
```

#### 為什麼使用 Dropout？
- **防止過擬合**：迫使模型不過度依賴任何單一神經元。
- 常見於前饋/MLP 層、RNN 或嵌入層之後（例如，在 transformers 中）。
- 通過超參數搜索來調整 `p`；過高（例如 >0.5）可能導致欠擬合。

完整文檔請查閱 [PyTorch nn.Dropout 參考](https://pytorch.org/docs/stable/generated/torch.nn.Dropout.html)。如果這來自特定模型（例如 BERT），請告訴我以獲取更多上下文！