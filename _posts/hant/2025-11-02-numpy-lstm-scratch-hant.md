---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: NumPy LSTM 從零開始實現
translated: true
type: note
---

這是一個僅使用 NumPy 實現的長短期記憶（LSTM）網絡基礎版本，靈感來自 Christopher Olah 關於理解 LSTM 網絡的部落格文章中所闡述的概念。它包含了核心閘門（遺忘閘、輸入閘、候選細胞閘和輸出閘），並專注於前向傳播過程。該類別透過 `forward()` 方法處理單個時間步，並透過 `forward_sequence()` 方法處理整個序列。

權重採用隨機初始化（實際應用中建議使用 Xavier/Glorot 等更好的初始化方法）。此實現未包含反向傳播或訓練功能——需透過時間反向傳播（BPTT）進行擴展。

```python
import numpy as np

class LSTM:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        # 初始化遺忘閘、輸入閘、細胞閘和輸出閘的權重與偏置
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
        # x: (input_size, 1), h_prev 和 C_prev: (hidden_size, 1)
        # 串接隱藏狀態與輸入
        concat = np.vstack((h_prev, x))
        # 遺忘閘
        f_t = self.sigmoid(np.dot(self.Wf, concat) + self.bf)
        # 輸入閘
        i_t = self.sigmoid(np.dot(self.Wi, concat) + self.bi)
        C_tilda = self.tanh(np.dot(self.WC, concat) + self.bC)
        # 細胞狀態更新
        C_t = f_t * C_prev + i_t * C_tilda
        # 輸出閘
        o_t = self.sigmoid(np.dot(self.Wo, concat) + self.bo)
        # 隱藏狀態更新
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
        return np.hstack(outputs).T  # 回傳 (seq_len, hidden_size)

# 使用範例
input_size = 3
hidden_size = 5
lstm = LSTM(input_size, hidden_size)

# 單步處理
x_t = np.random.randn(input_size, 1)
h_prev = np.zeros((hidden_size, 1))
C_prev = np.zeros((hidden_size, 1))
h_t, C_t = lstm.forward(x_t, h_prev, C_prev)
print("單步處理 - 隱藏狀態維度:", h_t.shape)

# 序列處理
X = np.random.randn(4, input_size)  # seq_len=4
outputs = lstm.forward_sequence(X)
print("序列輸出維度:", outputs.shape)
```

### 簡要說明
- **初始化**：權重連接串接後的輸入（前一隱藏狀態 + 當前輸入）至各個閘門。偏置採用零初始化。
- **閘門機制**：
  - **遺忘閘** (`f_t`)：決定從先前細胞狀態中遺忘哪些資訊（sigmoid：0-1）。
  - **輸入閘** (`i_t`) 與 **候選細胞** (`C_tilda`)：決定加入哪些新資訊（sigmoid + tanh）。
  - **輸出閘** (`o_t`)：過濾細胞狀態以產生隱藏狀態（sigmoid + tanh 作用於細胞狀態）。
- **細胞狀態** (`C_t`)：具有加法更新的線性流動，用於長期記憶。
- **使用方式**：處理序列時，需逐步遍歷時間步，持續更新隱藏狀態與細胞狀態。

此實現與 Colah 部落格中描述的 LSTM 架構相符：細胞狀態作為由閘門控制的「高速公路」。

[理解 LSTM：從零開始實現](https://medium.com/@samina.amin/understanding-lstms-lstm-implementation-from-scratch-18965a150eca)