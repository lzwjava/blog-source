---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 簡單 PyTorch RNN 範例
translated: true
type: note
---

### 使用 PyTorch 建立簡單 RNN 範例

循環神經網絡（RNNs）非常適合處理時序數據或文本等序列數據。以下是一個使用 PyTorch 構建簡單 RNN 進行序列分類的基礎範例（例如對隨機序列進行二元分類）。此範例假設您已安裝 PyTorch（`import torch` 和 `import torch.nn as nn`）。

```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# 超參數設定
input_size = 1      # 特徵維度（例如單變量時間序列）
hidden_size = 32    # 隱藏狀態維度
output_size = 1     # 二元輸出（使用 sigmoid 進行分類）
sequence_length = 10  # 序列長度
batch_size = 32
num_epochs = 10

# 生成虛擬數據：長度為 10 的序列，標籤基於序列總和（二元分類）
def generate_data(num_samples):
    X = torch.randn(num_samples, sequence_length, input_size)
    y = (torch.sum(X, dim=1) > 0).float().unsqueeze(1)
    return X, y

# 簡單 RNN 模型
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        # x 形狀：(batch, seq_len, input_size)
        h0 = torch.zeros(1, x.size(0), self.hidden_size)  # 初始隱藏狀態
        out, _ = self.rnn(x, h0)
        # 取最後一個輸出進行分類
        out = self.fc(out[:, -1, :])  # 最後時間步
        return self.sigmoid(out)

# 初始化模型、損失函數、優化器
model = SimpleRNN(input_size, hidden_size, output_size)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 訓練循環
num_samples = 1000
X, y = generate_data(num_samples)
dataset = torch.utils.data.TensorDataset(X, y)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

for epoch in range(num_epochs):
    for batch_X, batch_y in dataloader:
        optimizer.zero_grad()
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# 推論範例
test_seq = torch.randn(1, sequence_length, input_size)
prediction = model(test_seq)
print(f'Prediction: {prediction.item():.4f}')
```

#### 運作原理：
- **數據生成**：創建長度為 10 的隨機序列，並根據序列總和設定二元標籤（總和 > 0 為 1，否則為 0）。
- **模型**：使用 `nn.RNN`（基礎 RNN 單元）。前向傳播逐步處理序列，並使用最後的隱藏狀態進行輸出。
- **訓練**：標準 PyTorch 訓練循環，使用 BCE 損失進行二元分類。
- **輸出**：Sigmoid 激活函數輸出 0 到 1 之間的機率值。

這是基礎版 RNN；若需處理長序列並提升效能，可考慮使用 LSTM 或 GRU 變體（例如將 `nn.RNN` 替換為 `nn.LSTM`）。

### LSTM 變體（快速擴展）
為解決梯度消失問題，可改用 LSTM：

```python
# 在模型類別中替換：
self.rnn = nn.LSTM(input_size, hidden_size, batch_first=True)

# 並在前向傳播中：
h0 = torch.zeros(1, x.size(0), self.hidden_size)
c0 = torch.zeros(1, x.size(0), self.hidden_size)  # LSTM 需要細胞狀態
out, (hn, cn) = self.rnn(x, (h0, c0))
```

請在 PyTorch 環境中運行此程式碼進行實驗！

[PyTorch RNN 文檔](https://pytorch.org/docs/stable/generated/torch.nn.RNN.html)  
[PyTorch LSTM 文檔](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)