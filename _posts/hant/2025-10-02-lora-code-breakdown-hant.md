---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: LoRA 程式碼剖析與解說
translated: true
type: note
---

我將把 LoRA 示範程式碼分解成幾個關鍵部分，逐一詳細解釋每個部分，再繼續下一個。這將有助於以清晰、逐步的方式說明 LoRA 的工作原理。此程式碼基於先前的範例，使用 PyTorch 為簡單的線性層實現 LoRA。

### 程式碼部分 1：LoRA 層定義
```python
import torch
import torch.nn as nn

class LoRALayer(nn.Module):
    def __init__(self, in_features, out_features, rank=4):
        super(LoRALayer, self).__init__()
        # 原始凍結權重
        self.linear = nn.Linear(in_features, out_features)
        self.linear.weight.requires_grad = False  # 凍結原始權重
        # LoRA 參數：低秩矩陣 A 和 B
        self.lora_A = nn.Parameter(torch.randn(in_features, rank))
        self.lora_B = nn.Parameter(torch.randn(rank, out_features))
        self.scaling = 1.0  # LoRA 更新的縮放因子
```

#### 解釋
此部分定義了 `LoRALayer` 類別，它實現了 LoRA 技術。以下是其運作方式：

- **導入和類別設置**：我們導入 PyTorch (`torch`) 及其神經網絡模組 (`nn`)。`LoRALayer` 類別繼承自 `nn.Module`，使其成為可以整合到更大模型中的 PyTorch 模組。
- **原始線性層**：`self.linear = nn.Linear(in_features, out_features)` 創建一個標準的線性層（類似神經網絡中的全連接層），具有 `in_features` 個輸入和 `out_features` 個輸出。這代表了我們想要調整的預訓練權重。
- **凍結權重**：`self.linear.weight.requires_grad = False` 凍結線性層的原始權重，確保它們在訓練期間不會更新。這是 LoRA 效率的關鍵，因為它避免了修改大型預訓練模型。
- **LoRA 參數**：`self.lora_A` 和 `self.lora_B` 是低秩矩陣。`lora_A` 的形狀為 `(in_features, rank)`，`lora_B` 的形狀為 `(rank, out_features)`。`rank` 參數（預設=4）控制這些矩陣的大小，使它們遠小於原始權重矩陣（形狀 `in_features x out_features`）。這些矩陣是可訓練的（`nn.Parameter`）並以隨機值初始化（`torch.randn`）。
- **縮放因子**：`self.scaling = 1.0` 是一個超參數，用於縮放 LoRA 調整，允許微調適應強度。

此設置確保在訓練期間僅更新小的 `lora_A` 和 `lora_B` 矩陣，從而大幅減少可訓練參數的數量。

---

### 程式碼部分 2：LoRA 前向傳播
```python
    def forward(self, x):
        # 原始線性轉換 + LoRA 調整
        original = self.linear(x)
        lora_adjustment = self.scaling * torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)
        return original + lora_adjustment
```

#### 解釋
此部分定義了 `LoRALayer` 的前向傳播，它計算該層的輸出：

- **輸入**：輸入 `x` 是一個形狀為 `(batch_size, in_features)` 的張量，代表一批輸入數據。
- **原始輸出**：`original = self.linear(x)` 計算凍結線性層的輸出，將預訓練權重應用於輸入。
- **LoRA 調整**：項式 `torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)` 計算低秩適應。首先，`x` 乘以 `lora_A`（形狀 `in_features x rank`），產生一個形狀為 `(batch_size, rank)` 的張量。然後，將其乘以 `lora_B`（形狀 `rank x out_features`），產生一個形狀為 `(batch_size, out_features)` 的張量——與原始輸出形狀相同。此調整代表了任務特定的更新。
- **縮放和組合**：調整由 `self.scaling` 縮放並添加到原始輸出中，產生最終輸出。這確保模型保留預訓練知識，同時整合任務特定的適應。

低秩結構（`rank` 很小，例如 4）確保調整在計算上成本低廉且參數效率高，相比更新完整權重矩陣。

---

### 程式碼部分 3：玩具數據集和訓練
```python
def create_toy_dataset(n_samples=1000):
    X = torch.randn(n_samples, 64)  # 隨機輸入特徵
    y = torch.randn(n_samples, 10)  # 隨機目標輸出
    return X, y

def train_model(model, X, y, epochs=10, lr=0.01):
    criterion = nn.MSELoss()
    optimizer = optim.Adam([param for param in model.parameters() if param.requires_grad], lr=lr)
    
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")
```

#### 解釋
此部分創建一個玩具數據集並訓練 LoRA 適應模型：

- **玩具數據集**：`create_toy_dataset` 函數生成合成數據以供示範。`X` 是一個形狀為 `(1000, 64)` 的張量（1000 個樣本，64 個特徵），`y` 是一個形狀為 `(1000, 10)` 的張量（1000 個樣本，10 個輸出維度）。這些是隨機張量，用於模擬輸入-輸出對。
- **訓練函數**：`train_model` 函數設置一個簡單的訓練循環：
  - **損失函數**：`nn.MSELoss()` 定義均方誤差作為損失，適用於此類似回歸的玩具任務。
  - **優化器**：`optim.Adam` 僅優化可訓練參數（`param.requires_grad` 為 `True`），即 `lora_A` 和 `lora_B`。凍結的 `linear.weight` 被排除在外，確保效率。
  - **訓練循環**：對於每個 epoch，模型計算輸出，計算損失，執行反向傳播（`loss.backward()`），並更新 LoRA 參數（`optimizer.step()`）。打印損失以監控訓練進度。

此設置展示了 LoRA 如何僅微調低秩矩陣，保持過程輕量。

---

### 程式碼部分 4：主執行和參數計數
```python
def main():
    # 設置隨機種子以確保可重現性
    torch.manual_seed(42)
    
    # 創建玩具數據集
    X, y = create_toy_dataset()
    
    # 使用 LoRA 初始化模型
    model = LoRALayer(in_features=64, out_features=10, rank=4)
    
    # 計算可訓練參數
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Trainable parameters: {trainable_params}")
    print(f"Total parameters: {total_params}")
    
    # 訓練模型
    train_model(model, X, y)

if __name__ == "__main__":
    main()
```

#### 解釋
此部分將所有內容結合在一起，並突顯 LoRA 的效率：

- **隨機種子**：`torch.manual_seed(42)` 確保隨機初始化的可重現性。
- **數據集和模型**：創建玩具數據集，並初始化一個 `LoRALayer`，其 `in_features=64`、`out_features=10` 和 `rank=4`。
- **參數計數**：程式碼計算：
  - **可訓練參數**：僅 `lora_A` (64 × 4 = 256) 和 `lora_B` (4 × 10 = 40)，總計 296 個參數。
  - **總參數**：包括凍結的 `linear.weight` (64 × 10 = 640) 和 `linear.bias` (10)，加上 LoRA 參數，總計 946。
  - 這顯示了 LoRA 的效率：僅約 31% (296/946) 的參數是可訓練的，相比之下，完整微調是 100%。
- **訓練**：調用 `train_model` 函數在玩具數據集上微調 LoRA 參數。

當你運行此程式時，你會看到可訓練參數的數量遠少於總參數，並且由於低秩更新，模型訓練迅速。

---

### 運行程式碼
要運行此程式，你需要安裝 PyTorch (`pip install torch`)。將完整程式碼保存為 `.py` 文件並執行。輸出將顯示參數數量和 10 個 epoch 的訓練損失，展示 LoRA 在微調中的效率。

[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

如果你想深入了解任何部分或修改範例，請告訴我！