---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 神經網絡如何運作
translated: true
usemathjax: true
---

讓我們直接討論神經網絡工作的核心。也就是說，反向傳播算法：

1. 輸入 x：為輸入層設置相應的激活 $$a^{1}$$。
2. 前向傳播：對於每個 l=2,3,…,L 計算 $$z^{l} = w^l a^{l-1}+b^l$$ 和 $$a^{l} = \sigma(z^{l})$$。
3. 輸出誤差 $$\delta^{L}$$：計算向量 $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$。
4. 反向傳播誤差：對於每個 l=L−1,L−2,…,2，計算 $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$。
5. 輸出：成本函數的梯度由 $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$ 和 $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$ 給出。

這是從 Michael Nelson 的書《神經網絡與深度學習》中複製的。看起來是不是有點讓人不知所措？第一次看到時可能是這樣。但經過一個月的學習後就不會了。讓我來解釋一下。

## 輸入

共有五個階段。第一階段是輸入。這裡我們使用手寫數字作為輸入。我們的任務是識別它們。一個手寫數字有 784 個像素，即 28*28。每個像素中都有一個灰度值，範圍從 0 到 255。所以激活意味著我們使用某個函數來激活它，將其原始值改變為一個新值，以便於處理。

假設我們現在有 1000 張 784 像素的圖片。我們現在訓練它來識別它們顯示的數字。我們有 100 張圖片來測試學習效果。如果程序能識別出 97 張圖片的數字，我們說它的準確率是 97%。

所以我們會遍歷這 1000 張圖片，來訓練出權重和偏差。每次給它一張新圖片學習時，我們都會讓權重和偏差變得更正確。

一個批次的訓練結果會反映在 10 個神經元中。這裡，10 個神經元代表從 0 到 9，其值範圍從 0 到 1，表示它們對其準確性的信心。

輸入是 784 個神經元。我們如何將 784 個神經元減少到 10 個神經元呢？這就是問題所在。假設我們有兩層。層是什麼意思？第一層有 784 個神經元。第二層有 10 個神經元。

我們給 784 個神經元中的每個神經元一個權重，比如：

$$w_1, w_2, w_3, w_4, ... , w_{784}$$

並給第一層一個偏差，即 $$b_1$$。

所以第二層中的第一個神經元的值是：

$$w_1*a_1 + w_2*a_2+...+ w_{784}*a_{784}+b_1$$

但這些權重和偏差是針對 $$neuron^2_{1}$$（第二層中的第一個神經元）的。對於 $$neuron^2_{2}$$，我們需要另一組權重和偏差。

那麼 sigmoid 函數呢？我們使用 sigmoid 函數將上述值映射到 0 到 1 之間。

$$
\begin{eqnarray} 
  \sigma(z) \equiv \frac{1}{1+e^{-z}}
\end{eqnarray}
$$

$$
\begin{eqnarray} 
  \frac{1}{1+\exp(-\sum_j w_j x_j-b)}
\end{eqnarray}
$$

我們還使用 sigmoid 函數來激活第一層。也就是說，我們將灰度值改變為 0 到 1 的範圍。所以現在，每一層中的每個神經元都有一個從 0 到 1 的值。

所以現在對於我們的兩層網絡，第一層有 784 個神經元，第二層有 10 個神經元。我們訓練它以獲得權重和偏差。

我們有 784 * 10 個權重和 10 個偏差。在第二層中，對於每個神經元，我們將使用 784 個權重和 1 個偏差來計算其值。這裡的代碼如下：

```python
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
```

## 前向傳播

> 前向傳播：對於每個 l=2,3,…,L 計算 $$z^{l} = w^l a^{l-1}+b^l$$ 和 $$a^{l} = \sigma(z^{l})$$

注意這裡，我們使用上一層的值，即 $$a^{l-1}$$ 和當前層的權重 $$w^l$$ 及其偏差 $$b^l$$ 來進行 sigmoid 計算，以獲得當前層的值 $$a^{l}$$。

代碼：

```python
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # 前向傳播
        activation = x
        activations = [x] 
        zs = [] 
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
```

## 輸出誤差

> 輸出誤差 $$\delta^{L}$$：計算向量 $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$

讓我們看看 $$\nabla$$ 是什麼意思。

> Del 或 nabla 是數學中（特別是在向量微積分中）用作向量微分算子的運算符，通常由 nabla 符號 ∇ 表示。

$$
\begin{eqnarray}
  w_k & \rightarrow & w_k' = w_k-\eta \frac{\partial C}{\partial w_k} \\
  b_l & \rightarrow & b_l' = b_l-\eta \frac{\partial C}{\partial b_l}
\end{eqnarray}
$$

這裡 $$\eta $$ 是學習率。我們使用 C 對權重和偏差的導數，即它們之間的變化率。這就是下面的 `sigmoid_prime`。

代碼：

```python
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
```

```python
    def cost_derivative(self, output_activations, y):
        return (output_activations-y)
```

## 反向傳播誤差

> 反向傳播誤差：對於每個 l=L−1,L−2,…,2，計算 $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$

```python
     for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)
```

## 輸出

> 輸出：成本函數的梯度由 $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$
和 $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$ 給出。

```python
    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]
```

## 最後

這是一篇短文。在大部分內容中，它只是展示了代碼和數學公式。但對我來說沒問題。在寫這篇文章之前，我並不清楚。在寫完或只是從代碼和書中複製片段後，我理解了大部分內容。在從老師 Yin Wang 那裡獲得信心、閱讀了《神經網絡與深度學習》一書的 30%、聽了 Andrej Karpathy 的斯坦福講座和 Andrew Ng 的課程、與我的朋友 Qi 討論並調整 Anaconda、numpy 和 Theano 庫以使多年前的代碼工作後，我現在理解了它。

其中一個關鍵點是維度。我們應該知道每個符號和變量的維度。它只是進行可微計算。讓我們以 Yin Wang 的引述結束：

> 機器學習真的很有用，甚至可以說是美麗的理論，因為它只是微積分的變身！它是牛頓、萊布尼茨的古老而偉大的理論，以更簡單、優雅和強大的形式呈現。機器學習基本上就是使用微積分來推導和擬合一些函數，而深度學習則是擬合更複雜的函數。

> 人工智能中沒有“智能”，神經網絡中沒有“神經”，機器學習中沒有“學習”，深度學習中沒有“深度”。深度學習中沒有“深度”。在這個領域真正起作用的是“微積分”。所以我更喜歡稱這個領域為“可微計算”，構建模型的過程稱為“可微編程”。