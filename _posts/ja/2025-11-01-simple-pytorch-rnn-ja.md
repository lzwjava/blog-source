---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: シンプルなPyTorch RNNの例
translated: true
type: note
---

### PyTorchでのシンプルなRNNの例

リカレントニューラルネットワーク（RNN）は、時系列データやテキストなどのシーケンシャルデータを扱うのに適しています。以下は、PyTorchを使用してシンプルなRNNを構築し、シーケンス分類（例：ランダムシーケンスの二値分類）を行う基本的な例です。PyTorchがインストールされていることを前提としています（`import torch` および `import torch.nn as nn`）。

```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# ハイパーパラメータ
input_size = 1      # 特徴量のサイズ（例：単変量時系列）
hidden_size = 32    # 隠れ状態のサイズ
output_size = 1     # 二値出力（分類用シグモイド）
sequence_length = 10  # 各シーケンスの長さ
batch_size = 32
num_epochs = 10

# ダミーデータの生成：長さ10のシーケンス、合計に基づく二値ラベル
def generate_data(num_samples):
    X = torch.randn(num_samples, sequence_length, input_size)
    y = (torch.sum(X, dim=1) > 0).float().unsqueeze(1)
    return X, y

# シンプルなRNNモデル
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        # xの形状: (batch, seq_len, input_size)
        h0 = torch.zeros(1, x.size(0), self.hidden_size)  # 初期隠れ状態
        out, _ = self.rnn(x, h0)
        # 分類のために最後の出力を使用
        out = self.fc(out[:, -1, :])  # 最終タイムステップ
        return self.sigmoid(out)

# モデル、損失関数、オプティマイザの初期化
model = SimpleRNN(input_size, hidden_size, output_size)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# トレーニングループ
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

# 推論の例
test_seq = torch.randn(1, sequence_length, input_size)
prediction = model(test_seq)
print(f'Prediction: {prediction.item():.4f}')
```

#### 仕組み：
- **データ生成**：長さ10のランダムシーケンスを作成し、二値ラベル（合計 > 0 なら1、それ以外は0）を付与します。
- **モデル**：`nn.RNN`（基本RNNセル）を使用します。フォワードパスはシーケンスをステップごとに処理し、最後の隠れ状態を出力に使用します。
- **トレーニング**：二値分類のためのBCE損失を用いた標準的なPyTorchループです。
- **出力**：シグモイド活性化関数により、0から1の間の確率が得られます。

これは基本的なRNNです。長いシーケンスに対してより良い性能を発揮させるには、LSTMやGRUのバリアントを検討してください（例：`nn.RNN` を `nn.LSTM` に置き換える）。

### LSTMバリアント（簡単な拡張）
勾配消失問題に対処するためにLSTMに切り替える場合：

```python
# モデルクラス内で以下を置き換え：
self.rnn = nn.LSTM(input_size, hidden_size, batch_first=True)

# フォワード関数内で：
h0 = torch.zeros(1, x.size(0), self.hidden_size)
c0 = torch.zeros(1, x.size(0), self.hidden_size)  # LSTMはセル状態を必要とする
out, (hn, cn) = self.rnn(x, (h0, c0))
```

PyTorch環境で実行して実験してみてください！

[PyTorch RNN Documentation](https://pytorch.org/docs/stable/generated/torch.nn.RNN.html)  
[PyTorch LSTM Documentation](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)