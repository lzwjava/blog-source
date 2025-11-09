---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: 使用 PyTorch 的 LoRA 實作範例
translated: true
type: note
---

以下是一個使用 PyTorch 實現 LoRA（低秩適應）的 Python 程式碼範例，用於微調簡單神經網路。此範例重點在於使用 LoRA 適應預訓練的線性層，保持原始權重凍結並引入低秩更新矩陣。程式碼包含使用玩具資料集的基本設置和最小訓練循環，以說明概念。

<xaiArtifact artifact_id="1327e99b-24b5-4b0d-9ffd-5b4c2d1472af" artifact_version_id="4053525d-2225-4913-a3b9-b7d66b48daea" title="lora_demo.py" contentType="text/python">
import torch
import torch.nn as nn
import torch.optim as optim

# 定義 LoRA 層
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

    def forward(self, x):
        # 原始線性轉換 + LoRA 調整
        original = self.linear(x)
        lora_adjustment = self.scaling * torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)
        return original + lora_adjustment

# 用於示範的玩具資料集
def create_toy_dataset(n_samples=1000):
    X = torch.randn(n_samples, 64)  # 隨機輸入特徵
    y = torch.randn(n_samples, 10)  # 隨機目標輸出
    return X, y

# 訓練函數
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

# 主執行函數
def main():
    # 設置隨機種子以確保可重現性
    torch.manual_seed(42)
    
    # 創建玩具資料集
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
</xaiArtifact>

此程式碼定義了一個 `LoRALayer`，它使用低秩適應矩陣（`lora_A` 和 `lora_B`）包裝標準線性層。原始權重被凍結，只有 LoRA 參數在訓練期間更新。玩具資料集和訓練循環展示了 LoRA 如何在允許微調的同時減少可訓練參數的數量。您可以在安裝了 PyTor 的環境中運行此程式碼，以查看訓練過程和參數效率的實際效果。

[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)