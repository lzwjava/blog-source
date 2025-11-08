---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: スクラッチからのNumPy LSTM実装
translated: true
type: note
---

これは、Christopher Olahのブログ記事「Understanding LSTM Networks」の概念に触発され、NumPyのみを使用したLong Short-Term Memory（LSTM）ネットワークの基本的な実装です。コアゲート（忘却、入力、候補セル、出力）を含み、フォワードパスに焦点を当てています。このクラスは、単一のタイムステップを`forward()`で、シーケンス全体を`forward_sequence()`で処理します。

重みはランダムに初期化されています（実際には、Xavier/Glorotなどのより良い初期化方法を使用してください）。ここにはバックワードパスやトレーニングは含まれていません。それらを実装するには、時間方向への誤差逆伝播法（BPTT）で拡張してください。

```python
import numpy as np

class LSTM:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        # 忘却、入力、セル、出力ゲートの重みとバイアスを初期化
        self.Wf = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wi = np.random.randn(hidden_size, hidden_size + input_size)
        self.WC = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wo = np.random.randn(hidden_size, hidden_size + input_size)
        self.bf = np.zeros((hidden_size, 1))
        self.bi = np.zeros((hidden_size, 1))
        self.bC = np.zeros((hidden_size, 1))
        self.bo = np.zeros((hidden_size, 1))

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def tanh(self, z):
        return np.tanh(z)

    def forward(self, x, h_prev, C_prev):
        # x: (input_size, 1), h_prev と C_prev: (hidden_size, 1)
        # 隠れ状態と入力を連結
        concat = np.vstack((h_prev, x))
        # 忘却ゲート
        f_t = self.sigmoid(np.dot(self.Wf, concat) + self.bf)
        # 入力ゲート
        i_t = self.sigmoid(np.dot(self.Wi, concat) + self.bi)
        C_tilda = self.tanh(np.dot(self.WC, concat) + self.bC)
        # セル状態の更新
        C_t = f_t * C_prev + i_t * C_tilda
        # 出力ゲート
        o_t = self.sigmoid(np.dot(self.Wo, concat) + self.bo)
        # 隠れ状態の更新
        h_t = o_t * self.tanh(C_t)
        return h_t, C_t

    def forward_sequence(self, X):
        # X: (seq_len, input_size)
        h = np.zeros((self.hidden_size, 1))
        C = np.zeros((self.hidden_size, 1))
        outputs = []
        for x in X:
            h, C = self.forward(x.reshape(-1, 1), h, C)
            outputs.append(h)
        return np.hstack(outputs).T  # (seq_len, hidden_size) を返す

# 使用例
input_size = 3
hidden_size = 5
lstm = LSTM(input_size, hidden_size)

# 単一ステップ
x_t = np.random.randn(input_size, 1)
h_prev = np.zeros((hidden_size, 1))
C_prev = np.zeros((hidden_size, 1))
h_t, C_t = lstm.forward(x_t, h_prev, C_prev)
print("単一ステップ - 隠れ状態の形状:", h_t.shape)

# シーケンス
X = np.random.randn(4, input_size)  # seq_len=4
outputs = lstm.forward_sequence(X)
print("シーケンス出力の形状:", outputs.shape)
```

### 簡単な説明
- **初期化**: 重みは連結された入力（前の隠れ状態＋現在の入力）を各ゲートに接続します。バイアスはゼロ初期化されています。
- **ゲート**:
  - **忘却ゲート** (`f_t`): 前のセル状態から何を忘れるかを決定します（シグモイド: 0-1）。
  - **入力ゲート** (`i_t`) と **候補セル** (`C_tilda`): どの新しい情報を追加するかを決定します（シグモイド + tanh）。
  - **出力ゲート** (`o_t`): 隠れ状態を生成するためにセル状態をフィルタリングします（シグモイド + セルへのtanh）。
- **セル状態** (`C_t`): 長期記憶のための加算的更新を持つ線形の流れ。
- **使用法**: シーケンスの場合、タイムステップをループ処理し、隠れ状態とセル状態を段階的に更新します。

これはColahのブログにあるLSTMアーキテクチャに一致します: ゲートによって制御される「ハイウェイ」としてのセル状態。

[Understanding LSTMs: Implementation from Scratch](https://medium.com/@samina.amin/understanding-lstms-lstm-implementation-from-scratch-18965a150eca)