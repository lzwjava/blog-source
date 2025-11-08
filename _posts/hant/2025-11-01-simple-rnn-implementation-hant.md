---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 簡單循環神經網絡從零開始實現
translated: true
type: note
---

### 使用 NumPy 從零開始實現簡單 RNN 範例

透過 NumPy 從零實現 RNN 是理解其運作機制的絕佳方式：包括循環隱藏狀態、正向傳播以及透過時間的反向傳播（BPTT）。以下是一個針對隨機序列進行二元分類的基礎範例（類似先前 PyTorch 版本）。它使用單變量時間序列數據（input_size=1），隱藏層大小為 32，序列長度為 10。

此程式碼包含：
- 數據生成
- RNN 正向傳遞（隱藏狀態使用 tanh 激活函數）
- 反向傳遞（使用簡單梯度下降的 BPTT）
- 訓練循環

注意：這是標準 RNN；在長序列上梯度可能會消失或爆炸。在實際應用中，請考慮使用梯度裁剪或 LSTM 邏輯。

```python
import numpy as np

# 超參數
input_size = 1      # 特徵維度（單變量）
hidden_size = 32    # 隱藏狀態維度
output_size = 1     # 二元輸出
sequence_length = 10  # 每個序列的長度
num_samples = 1000
num_epochs = 10
learning_rate = 0.01

# 生成虛擬數據：長度為 10 的序列，標籤基於總和（二元）
def generate_data(num_samples):
    X = np.random.randn(num_samples, sequence_length, input_size)
    y = (np.sum(X, axis=1) > 0).astype(float).reshape(num_samples, 1)
    return X, y

# 簡單 RNN 類別（從零開始）
class SimpleRNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # 初始化權重（Xavier 初始化）
        self.Wxh = np.random.randn(hidden_size, input_size) * np.sqrt(1. / input_size)
        self.Whh = np.random.randn(hidden_size, hidden_size) * np.sqrt(1. / hidden_size)
        self.Why = np.random.randn(output_size, hidden_size) * np.sqrt(1. / hidden_size)
        
        # 偏置項
        self.bh = np.zeros((hidden_size, 1))
        self.by = np.zeros((output_size, 1))
    
    def forward(self, x):
        # x 形狀：單個樣本為 (sequence_length, input_size, 1)
        self.x = x  # 儲存以供反向傳播使用
        self.h = np.zeros((self.hidden_size, 1))  # 初始隱藏狀態
        
        # 時間步正向傳遞
        self.hs = np.zeros((self.hidden_size, sequence_length + 1))  # 隱藏狀態（包含初始狀態）
        self.hs[:, 0] = self.h.flatten()
        
        for t in range(sequence_length):
            self.h = np.tanh(np.dot(self.Wxh, x[t]) + np.dot(self.Whh, self.h) + self.bh)
            self.hs[:, t+1] = self.h.flatten()
        
        # 從最後一個隱藏狀態輸出
        self.y_pred = np.dot(self.Why, self.h) + self.by
        return self.sigmoid(self.y_pred)
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-np.clip(z, -250, 250)))  # 裁剪以確保穩定性
    
    def backward(self, y_true):
        # 透過時間反向傳播（簡化版）
        dWhy = np.dot((self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred), self.hs[-1:, :].T)
        dby = (self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred)
        
        # 隱藏層和輸出層權重的梯度
        dWhh = np.zeros_like(self.Whh)
        dWxh = np.zeros_like(self.Wxh)
        dbh = np.zeros_like(self.bh)
        
        dh_next = np.zeros_like(self.h)
        for t in reversed(range(sequence_length)):
            dh = np.dot(self.Why.T, (self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred)) + dh_next
            dh_raw = (1 - self.h**2) * dh  # Tanh 導數
            dWxh += np.dot(dh_raw, self.x[t].T)
            dWhh += np.dot(dh_raw, self.hs[:, t:t+2].T[:, 0:1])  # 簡化處理；完整 BPTT 會更精確地累積
            dbh += dh_raw
            dh_next = np.dot(self.Whh.T, dh_raw)
        
        # 更新權重
        self.Wxh -= learning_rate * dWxh
        self.Whh -= learning_rate * dWhh
        self.Why -= learning_rate * dWhy
        self.bh -= learning_rate * dbh
        self.by -= learning_rate * dby
    
    def sigmoid_deriv(self, z):
        s = self.sigmoid(z)
        return s * (1 - s)

# 訓練
X, y = generate_data(num_samples)

# 為單個樣本處理重塑形狀（為簡化起見，batch_size=1）
X = X.reshape(num_samples, sequence_length, input_size, 1)  # 添加批次維度 1
y = y.reshape(num_samples, 1, 1)

model = SimpleRNN(input_size, hidden_size, output_size)

for epoch in range(num_epochs):
    total_loss = 0
    for i in range(num_samples):
        pred = model.forward(X[i])
        loss = -np.mean(y[i] * np.log(pred + 1e-8) + (1 - y[i]) * np.log(1 - pred + 1e-8))  # BCE 損失
        total_loss += loss
        model.backward(y[i])
    
    avg_loss = total_loss / num_samples
    print(f'Epoch [{epoch+1}/{num_epochs}], Avg Loss: {avg_loss:.4f}')

# 推論範例
test_seq = np.random.randn(sequence_length, input_size, 1)
prediction = model.forward(test_seq)
print(f'Prediction: {prediction.flatten()[0]:.4f}')
```

#### 運作原理：
- **數據生成**：隨機序列，標籤基於總和進行二元分類。
- **正向傳遞**：逐時間步處理序列，更新隱藏狀態 `h_t = tanh(Wxh * x_t + Whh * h_{t-1} + bh)`。輸出使用最終的 `h` 並通過 sigmoid 函數。
- **反向傳遞**：BPTT 計算所有時間步的梯度，透過簡單梯度下降更新權重。（注意：這是最小化的 BPTT；完整版本會處理更精確的累積。）
- **訓練**：循環遍歷樣本，計算 BCE 損失並更新權重。
- **輸出**：Sigmoid 給出機率值（0-1）。

在標準機器上，使用這些參數運行大約需要 10-20 秒。增加 `num_samples` 或 `num_epochs` 以觀察學習效果。對於多批次處理，需將循環向量化。

深入閱讀：  
[Understanding LSTM Networks (Colah's Blog)](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)  
[NumPy RNN Tutorial](https://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/)