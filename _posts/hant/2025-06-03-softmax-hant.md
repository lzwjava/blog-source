---
audio: false
generated: true
lang: hant
layout: post
title: 深度學習中的 Softmax 函數
translated: true
type: note
---

### 什麼是 Softmax？

**Softmax 函數**是一種在機器學習（尤其是深度學習）中使用的數學函數，用於將原始分數向量（通常稱為 logits）轉換為機率分佈。它確保輸出值為正數且總和為 1，使其可解釋為機率。

Softmax 函數對於向量 \\( z = [z_1, z_2, \dots, z_n] \\) 的定義如下：

\\[
\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^n e^{z_j}}
\\]

其中：
- \\( z_i \\)：第 \\( i \\) 個類別的輸入分數（logit）。
- \\( e^{z_i} \\)：輸入分數的指數，確保正值。
- \\( \sum_{j=1}^n e^{z_j} \\)：所有輸入分數指數的總和，用於歸一化。
- 輸出 \\( \text{Softmax}(z_i) \\) 代表第 \\( i \\) 個類別的機率。

關鍵特性：
- **輸出範圍**：每個輸出值介於 0 和 1 之間。
- **總和為 1**：所有輸出值的總和等於 1，使其成為有效的機率分佈。
- **放大差異**：Softmax 中的指數函數強調較大的輸入值，使得輸出機率對於較大的 logits 更加明確。

### Softmax 在深度學習中的應用

Softmax 函數通常用於神經網絡的**輸出層**，用於**多類別分類**任務。以下是其應用方式：

1. **在神經網絡中的上下文**：
   - 在神經網絡中，最終層通常為每個類別產生原始分數（logits）。例如，在一個有 3 個類別的分類問題中（如貓、狗、鳥），網絡可能輸出像 \\([2.0, 1.0, 0.5]\\) 的 logits。
   - 這些 logits 不能直接解釋為機率，因為它們可以是負數、無界且總和不等於 1。

2. **Softmax 的作用**：
   - Softmax 函數將這些 logits 轉換為機率。對於上面的例子：
     \\[
     \text{Softmax}([2.0, 1.0, 0.5]) = \left[ \frac{e^{2.0}}{e^{2.0} + e^{1.0} + e^{0.5}}, \frac{e^{1.0}}{e^{2.0} + e^{1.0} + e^{0.5}}, \frac{e^{0.5}}{e^{2.0} + e^{1.0} + e^{0.5}} \right]
     \\]
     這可能會得到像 \\([0.665, 0.245, 0.090]\\) 的機率，表示類別 1（貓）的機率為 66.5%，類別 2（狗）為 24.5%，類別 3（鳥）為 9.0%。

3. **應用場景**：
   - **多類別分類**：Softmax 用於像圖像分類（例如識別圖像中的物體）、自然語言處理（例如多類別情感分析）或任何需要將輸入分配給多個類別之一的問題。
   - **損失計算**：Softmax 通常與**交叉熵損失**函數配對使用，該函數衡量預測機率分佈與真實分佈（one-hot 編碼標籤）之間的差異。此損失指導神經網絡的訓練。
   - **決策制定**：輸出機率可用於選擇最可能的類別（例如，取機率最高的類別）。

4. **深度學習中的例子**：
   - **圖像分類**：在卷積神經網絡（CNN）如 ResNet 中，最終的全連接層為每個類別產生 logits（例如 ImageNet 中的 1000 個類別）。Softmax 將這些轉換為機率以預測圖像中的物體。
   - **自然語言處理**：在像 transformers（例如 BERT）的模型中，Softmax 用於輸出層，用於像文本分類或下一個詞預測等任務，其中需要對詞彙或類別集合的機率。
   - **強化學習**：Softmax 可用於將動作分數轉換為機率，以便在基於策略的方法中選擇動作。

5. **在框架中的實現**：
   - 在像 **PyTorch** 或 **TensorFlow** 的框架中，Softmax 通常作為內置函數實現：
     - PyTorch：`torch.nn.Softmax(dim=1)` 或 `torch.nn.functional.softmax()`
     - TensorFlow：`tf.nn.softmax()`
   - 許多框架將 Softmax 與交叉熵損失結合在單一操作中（例如 PyTorch 中的 `torch.nn.CrossEntropyLoss`），以實現數值穩定性，因為單獨計算 Softmax 可能會導致像大 logits 溢位等問題。

### 實際考量
- **數值穩定性**：直接計算 Softmax 可能由於指數函數而導致溢位。常見的技巧是在應用 Softmax 之前從所有 logits 中減去最大 logit 值（\\( z_i - \max(z) \\)），這不會改變輸出但能防止大的指數值。
- **Softmax 與 Sigmoid**：對於**二進制分類**，通常使用 sigmoid 函數而不是 Softmax，因為它更高效地處理兩個類別。Softmax 將 sigmoid 推廣到多個類別。
- **限制**：
  - Softmax 假設互斥性（一個正確類別）。對於多標籤分類（多個類別可以為真），首選 sigmoid。
  - Softmax 可能由於指數函數而對預測過於自信，這可能會放大 logits 中的小差異。

### 計算示例
假設一個神經網絡為一個 3 類別問題輸出 logits \\([1.5, 0.8, -0.2]\\)：
1. 計算指數：\\( e^{1.5} \approx 4.482, e^{0.8} \approx 2.225, e^{-0.2} \approx 0.819 \\)。
2. 指數總和：\\( 4.482 + 2.225 + 0.819 = 7.526 \\)。
3. 計算機率：
   - 類別 1：\\( \frac{4.482}{7.526} \approx 0.596 \\)
   - 類別 2：\\( \frac{2.225}{7.526} \approx 0.296 \\)
   - 類別 3：\\( \frac{0.819}{7.526} \approx 0.109 \\)
4. 輸出：\\([0.596, 0.296, 0.109]\\)，一個有效的機率分佈。

### Softmax 可視化
為了說明 Softmax 如何將 logits 轉換為機率，請考慮以下顯示 logits 及其對應 Softmax 機率的圖表：

```chartjs
{
  "type": "bar",
  "data": {
    "labels": ["Class 1", "Class 2", "Class 3"],
    "datasets": [
      {
        "label": "Logits",
        "data": [1.5, 0.8, -0.2],
        "backgroundColor": "rgba(75, 192, 192, 0.6)",
        "borderColor": "rgba(75, 192, 192, 1)",
        "borderWidth": 1
      },
      {
        "label": "Softmax Probabilities",
        "data": [0.596, 0.296, 0.109],
        "backgroundColor": "rgba(255, 99, 132, 0.6)",
        "borderColor": "rgba(255, 99, 132, 1)",
        "borderWidth": 1
      }
    ]
  },
  "options": {
    "scales": {
      "y": {
        "beginAtZero": true,
        "title": {
          "display": true,
          "text": "Value"
        }
      },
      "x": {
        "title": {
          "display": true,
          "text": "Classes"
        }
      }
    },
    "plugins": {
      "legend": {
        "display": true
      },
      "title": {
        "display": true,
        "text": "Logits vs. Softmax Probabilities"
      }
    }
  }
}
```

此圖表比較了原始 logits 與應用 Softmax 後的機率，突顯了 Softmax 如何將值歸一化為機率分佈。

### 總結
Softmax 函數是深度學習中多類別分類的基石，將原始分數轉換為機率分佈。它廣泛用於神經網絡輸出層，用於像圖像和文本分類等任務，使模型能夠為多個類別分配機率，並通過像交叉熵的損失函數促進訓練。其指數特性使其對 logits 的差異敏感，謹慎的實現確保了數值穩定性。