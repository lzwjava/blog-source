---
audio: false
generated: true
lang: hant
layout: post
title: 利用線性回歸進行交易
translated: true
type: note
---

很好的問題！你這裡結合了兩個任務：

1. **使用 TigerOpen API 獲取歷史股票數據（例如騰訊）**
2. **將這些數據與你現有的基於 numpy 的線性回歸代碼結合使用**

---

## 現有代碼能直接使用嗎？

**不行，無法直接使用。** 你目前的 ML 代碼期望 `x_train` 和 `y_train` 是代表特徵和標籤（例如人口與利潤）的數值 numpy 陣列。但 TigerOpen API 返回的是**歷史 K 線數據**（OHLCV 數據），這是一個時間序列，每個時間戳包含多個欄位。

你需要：

- 正確提取和預處理股票數據，將其轉換為合適的 `x_train` 和 `y_train` 陣列。
- 調整你的模型和代碼以適應股票數據的上下文（例如根據前幾天的數據預測收盤價）。

---

## 如何調整股票數據以用於你的線性回歸模型？

### 步驟 1：獲取騰訊（代號 `'00700'`）的歷史數據

```python
bars_dict = quote_client.get_bars(
    symbols=['00700'],
    period=BarPeriod.DAY,
    begin_time='2024-01-01',
    end_time=datetime.now().strftime('%Y-%m-%d'),
    limit=100,
    right=QuoteRight.BR
)

bars = bars_dict.get('00700', [])
```

### 步驟 2：提取特徵和標籤

一個簡單的方法是：

- 使用天數索引作為 `x_train`（例如 0, 1, 2, ...）
- 使用收盤價作為 `y_train`

```python
import numpy as np

x_train = np.array([i for i in range(len(bars))])
y_train = np.array([bar.close for bar in bars])
```

或者，你也可以使用前一天的收盤價作為特徵來預測第二天的收盤價，或者使用更複雜的特徵。

### 步驟 3：使用你的線性回歸代碼

現在你的 `x_train` 和 `y_train` 是數字的 numpy 陣列，所以在修復了你的 `compute_cost` 和 `compute_gradient` 函數（目前它們返回零或零梯度）之後，你的代碼應該可以正常運作。

---

## 範例：實現 compute_cost 和 compute_gradient

```python
def compute_cost(x, y, w, b):
    m = x.shape[0]
    total_cost = 0.5 * np.sum((w * x + b - y) ** 2) / m
    return total_cost

def compute_gradient(x, y, w, b):
    m = x.shape[0]
    error = w * x + b - y
    dj_dw = np.sum(error * x) / m
    dj_db = np.sum(error) / m
    return dj_dw, dj_db
```

---

## 總結

- 使用 TigerOpen API 獲取歷史股票數據
- 將時間序列數據轉換為數值陣列（`x_train`, `y_train`）
- 實現或修復你的成本函數和梯度函數
- 然後你的梯度下降和繪圖代碼將能夠運作，以擬合股票價格數據的線性模型

---

## 額外提示：繪製股票價格

你的散點圖將顯示收盤價隨天數的變化，而回歸線將擬合出一個趨勢。

---

如果你需要，我可以幫你編寫一個完整的範例，將 TigerOpen 數據獲取與你的 numpy 線性回歸代碼整合起來！儘管提出。