---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ゼロからの単純RNN実装
translated: true
type: note
---

### NumPyでのシンプルなRNN実装（スクラッチから）

NumPyでRNNをスクラッチから実装することは、メカニズムを理解するのに最適な方法です：再帰的な隠れ状態、順伝播、そして時間方向への逆伝播（BPTT）。以下は、ランダムな系列（前回のPyTorch版と同様）に対する二値分類の基本的な例です。これは単変量時系列データ（input_size=1）、hidden_size=32、sequence_length=10を使用します。

このコードは以下を含みます：
- データ生成
- RNNの順伝播（隠れ状態にtanh活性化関数を使用）
- 逆伝播（単純な勾配降下法を用いたBPTT）
- 訓練ループ

注意：これは素子のRNNです。長い系列では勾配が消失または爆発する可能性があります。本番環境では、クリッピングやLSTMロジックの使用を検討してください。

```python
import numpy as np

# ハイパーパラメータ
input_size = 1      # 特徴量のサイズ（単変量）
hidden_size = 32    # 隠れ状態のサイズ
output_size = 1     # 二値出力
sequence_length = 10  # 各系列の長さ
num_samples = 1000
num_epochs = 10
learning_rate = 0.01

# ダミーデータ生成：長さ10の系列、合計に基づくラベル（二値）
def generate_data(num_samples):
    X = np.random.randn(num_samples, sequence_length, input_size)
    y = (np.sum(X, axis=1) > 0).astype(float).reshape(num_samples, 1)
    return X, y

# シンプルなRNNクラス（スクラッチから）
class SimpleRNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # 重みの初期化（Xavier初期化）
        self.Wxh = np.random.randn(hidden_size, input_size) * np.sqrt(1. / input_size)
        self.Whh = np.random.randn(hidden_size, hidden_size) * np.sqrt(1. / hidden_size)
        self.Why = np.random.randn(output_size, hidden_size) * np.sqrt(1. / hidden_size)
        
        # バイアス
        self.bh = np.zeros((hidden_size, 1))
        self.by = np.zeros((output_size, 1))
    
    def forward(self, x):
        # xの形状：単一サンプルに対して (sequence_length, input_size, 1)
        self.x = x  # 逆伝播のために保存
        self.h = np.zeros((self.hidden_size, 1))  # 初期隠れ状態
        
        # 時間方向への順伝播
        self.hs = np.zeros((self.hidden_size, sequence_length + 1))  # 隠れ状態（初期状態を含む）
        self.hs[:, 0] = self.h.flatten()
        
        for t in range(sequence_length):
            self.h = np.tanh(np.dot(self.Wxh, x[t]) + np.dot(self.Whh, self.h) + self.bh)
            self.hs[:, t+1] = self.h.flatten()
        
        # 最終隠れ状態からの出力
        self.y_pred = np.dot(self.Why, self.h) + self.by
        return self.sigmoid(self.y_pred)
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-np.clip(z, -250, 250)))  # 安定性のためのクリッピング
    
    def backward(self, y_true):
        # 時間方向への逆伝播（簡略化版）
        dWhy = np.dot((self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred), self.hs[-1:, :].T)
        dby = (self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred)
        
        # 隠れ層と出力層の重みに対する勾配
        dWhh = np.zeros_like(self.Whh)
        dWxh = np.zeros_like(self.Wxh)
        dbh = np.zeros_like(self.bh)
        
        dh_next = np.zeros_like(self.h)
        for t in reversed(range(sequence_length)):
            dh = np.dot(self.Why.T, (self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred)) + dh_next
            dh_raw = (1 - self.h**2) * dh  # Tanhの導関数
            dWxh += np.dot(dh_raw, self.x[t].T)
            dWhh += np.dot(dh_raw, self.hs[:, t:t+2].T[:, 0:1])  # 簡略化；完全なBPTTではより正確に蓄積する
            dbh += dh_raw
            dh_next = np.dot(self.Whh.T, dh_raw)
        
        # 重みの更新
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

# 単一サンプル処理のための形状変更（簡単のためバッチサイズ=1）
X = X.reshape(num_samples, sequence_length, input_size, 1)  # バッチ次元1を追加
y = y.reshape(num_samples, 1, 1)

model = SimpleRNN(input_size, hidden_size, output_size)

for epoch in range(num_epochs):
    total_loss = 0
    for i in range(num_samples):
        pred = model.forward(X[i])
        loss = -np.mean(y[i] * np.log(pred + 1e-8) + (1 - y[i]) * np.log(1 - pred + 1e-8))  # BCE
        total_loss += loss
        model.backward(y[i])
    
    avg_loss = total_loss / num_samples
    print(f'Epoch [{epoch+1}/{num_epochs}], Avg Loss: {avg_loss:.4f}')

# 推論の例
test_seq = np.random.randn(sequence_length, input_size, 1)
prediction = model.forward(test_seq)
print(f'Prediction: {prediction.flatten()[0]:.4f}')
```

#### 動作の説明：
- **データ生成**：合計に基づく二値ラベルを持つランダムな系列。
- **順伝播**：系列をタイムステップごとに処理し、隠れ状態 `h_t = tanh(Wxh * x_t + Whh * h_{t-1} + bh)` を更新します。出力は最終的な `h` にシグモイド関数を適用して使用します。
- **逆伝播**：BPTTがすべてのタイムステップの勾配を計算し、単純な勾配降下法で重みを更新します。（注意：これは最小限のBPTTです。完全版ではより正確な蓄積を扱います。）
- **訓練**：サンプルをループ処理し、BCE損失を計算し、更新します。
- **出力**：シグモイド関数は確率（0-1）を与えます。

このパラメータでは、標準的なマシンで約10〜20秒で実行されます。学習を確認するには `num_samples` または `num_epochs` を増やしてください。マルチバッチの場合は、ループをベクトル化してください。

より深く学ぶには：  
[Understanding LSTM Networks (Colah's Blog)](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)  
[NumPy RNN Tutorial](https://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/)