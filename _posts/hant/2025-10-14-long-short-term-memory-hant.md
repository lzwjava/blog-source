---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 長短期記憶入門
translated: true
type: note
---

## 什麼是 LSTM？

長短期記憶（LSTM）是一種特殊類型的循環神經網絡（RNN）架構，專為處理和學習序列數據（如時間序列、自然語言或語音）而設計。由 Sepp Hochreiter 和 Jürgen Schmidhuber 於 1997 年提出，LSTM 解決了傳統 RNN 的關鍵限制，特別是它們在處理數據中長距離依賴關係時的困難。

LSTM 的核心是一個神經網絡單元，它逐步處理輸入序列，同時保持對先前輸入的「記憶」。這種記憶使其能夠捕捉長時間的模式，對於序列中遠端上下文重要的任務非常強大。LSTM 廣泛應用於 TensorFlow 和 PyTorch 等深度學習框架中，構成了許多人工智慧尖端模型的基礎。

## 背景：為何需要 LSTM

傳統 RNN 通過隱藏狀態將信息從一個時間步傳遞到下一個來處理序列。然而，它們存在兩個主要問題：

- **梯度消失問題**：在通過時間的反向傳播（BPTT）過程中，梯度可能指數級縮小，導致難以學習長期依賴關係。如果相關事件發生在 50 步之前，網絡可能會「忘記」它。
- **梯度爆炸問題**：相反，梯度可能變得過大，導致訓練不穩定。

這些問題限制了普通 RNN 只能處理短序列。LSTM 通過引入**細胞狀態**來解決這個問題——這是一種類似傳送帶的結構，貫穿整個序列，通過最小的線性交互來長距離保存信息。

## LSTM 的工作原理：核心組件

LSTM 單元在時間步 \\( t \\) 處理輸入序列 \\( x_t \\)，根據先前的隱藏狀態 \\( h_{t-1} \\) 和細胞狀態 \\( c_{t-1} \\) 更新其內部狀態。其關鍵創新在於使用**門控**——經過 sigmoid 激活的神經網絡，用於決定保留、添加或輸出哪些信息。這些門控充當信息流動的「調節器」。

### 三個主要門控

1. **遺忘門 (\\( f_t \\))**：
   - 決定從細胞狀態中丟棄哪些信息。
   - 公式：\\( f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f) \\)
   - 輸出：一個介於 0（完全遺忘）和 1（完全保留）之間的數值向量。
   - 其中，\\( \sigma \\) 是 sigmoid 函數，\\( W_f \\) 和 \\( b_f \\) 是可學習的權重和偏置。

2. **輸入門 (\\( i_t \\)) 和候選值 (\\( \tilde{c}_t \\))**：
   - 決定將哪些新信息存儲到細胞狀態中。
   - 輸入門：\\( i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i) \\)
   - 候選值：\\( \tilde{c}_t = \tanh(W_c \cdot [h_{t-1}, x_t] + b_c) \\)（使用雙曲正切函數，數值範圍在 -1 到 1 之間）。
   - 這些共同創建對細胞狀態的潛在更新。

3. **輸出門 (\\( o_t \\))**：
   - 決定將細胞狀態的哪些部分輸出為隱藏狀態。
   - 公式：\\( o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o) \\)
   - 隱藏狀態則為：\\( h_t = o_t \odot \tanh(c_t) \\)（其中 \\( \odot \\) 表示逐元素乘法）。

### 更新細胞狀態

細胞狀態 \\( c_t \\) 的更新方式為：
\\[ c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t \\]
- 第一項：遺忘過去不相關的信息。
- 第二項：添加新的相關信息。

這種加法更新（而非 RNN 中的乘法更新）有助於梯度更好地流動，緩解梯度消失問題。

### 視覺化表示

將細胞狀態想像成一條高速公路：遺忘門是交通燈，決定讓哪些來自前一路段的車輛（信息）通過；輸入門從側路匯入新車輛；輸出門則過濾哪些車輛駛出到下一條高速公路（隱藏狀態）。

## 數學概述

以下是基本 LSTM 單元的完整方程式組：

\\[
\begin{align*}
f_t &= \sigma(W_f x_t + U_f h_{t-1} + b_f) \\
i_t &= \sigma(W_i x_t + U_i h_{t-1} + b_i) \\
\tilde{c}_t &= \tanh(W_c x_t + U_c h_{t-1} + b_c) \\
o_t &= \sigma(W_o x_t + U_o h_{t-1} + b_o) \\
c_t &= f_t \odot c_{t-1} + i_t \odot \tilde{c}_t \\
h_t &= o_t \odot \tanh(c_t)
\end{align*}
\\]

- \\( W \\) 矩陣連接輸入到門控；\\( U \\) 連接隱藏狀態。
- 訓練涉及通過梯度下降優化這些參數。

## LSTM 的優勢

- **長期記憶**：擅長處理長達數千步的序列，優於標準 RNN。
- **靈活性**：處理可變長度輸入和雙向處理（向前和向後處理序列）。
- **可解釋性**：門控提供了模型「記住」或「忘記」內容的洞察。
- **魯棒性**：與更簡單的模型相比，對噪聲序列數據的過擬合風險較低。

缺點包括更高的計算成本（更多參數）和調參複雜度。

## 變體與演進

- **門控循環單元（GRU）**：一種更輕量的替代方案（2014年），將遺忘門和輸入門合併為更新門，在保留大部分 LSTM 性能的同時減少參數。
- **窺視孔連接**：早期變體，門控可以窺視細胞狀態。
- **雙向 LSTM（BiLSTM）**：兩個 LSTM（向前和向後）用於在機器翻譯等任務中提供更好的上下文。
- 現代整合：Transformer 中的 LSTM（例如混合模型）或注意力增強型 LSTM。

## 應用領域

LSTM 在具有時間或序列結構的領域中表現卓越：

- **自然語言處理（NLP）**：情感分析、機器翻譯（例如早期的 Google Translate）、文本生成。
- **時間序列預測**：股價預測、天氣預報、傳感器數據中的異常檢測。
- **語音識別**：將音頻轉換為文本（例如 Siri 或 Alexa）。
- **視頻分析**：通過處理幀序列進行動作識別。
- **醫療保健**：根據順序醫療記錄預測患者結果。
- **音樂生成**：通過建模音符序列創作旋律。

近年來（截至 2025 年），LSTM 常與 Transformer 結合以實現混合效率，但它們在計算資源有限的邊緣設備上仍然具有基礎性作用。

## 開始使用 LSTM

可以使用 Python 配合 Keras/TensorFlow 進行實驗：

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

model = Sequential()
model.add(LSTM(50, input_shape=(timesteps, features)))  # 50 個單元
model.add(Dense(1))  # 輸出層
model.compile(optimizer='adam', loss='mse')
# 在您的序列數據上進行訓練
```

實踐資源：官方 TensorFlow 教程或原始論文。

LSTM 革命性地推進了序列建模，為當今的人工智慧發展鋪平了道路。如果您想深入學習，請專注於通過 LSTM 流程圖等視覺化工具理解門控機制。

## 參考文獻
- [原始 LSTM 論文：Long Short-Term Memory](https://www.bioinf.jku.at/publications/older/2604.pdf)
- [Colah's Blog: Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [Towards Data Science: A Gentle Introduction to LSTMs](https://towardsdatascience.com/understanding-lstm-and-its-diagrams-37e2f46f1714)