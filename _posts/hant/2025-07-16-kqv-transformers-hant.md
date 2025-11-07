---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 神經網路、Transformer 與 GPT
translated: true
type: post
---

### 目錄

1. [我如何學習 Transformers 中的 KQV 機制](#how-i-learned-the-kqv-mechanism-in-transformers)
   - Query、Key、Value 矩陣代表 token 互動
   - 理解需要了解維度和形狀
   - 初始概念隨時間變得更清晰
   - AI 時代提供豐富的學習資源
   - 勵志故事激勵持續學習

2. [從神經網絡到 GPT](#from-neural-network-to-gpt)
   - 從頭開始複製神經網絡以加深理解
   - Transformers 透過 embedding 和 encoding 處理文本
   - Self-attention 計算詞語之間的相似性
   - 觀看基礎講座並閱讀程式碼
   - 透過專案和論文追隨好奇心

3. [神經網絡的運作原理](#how-neural-network-works)
   - Backpropagation 演算法更新權重和偏差
   - 輸入資料通過網絡層激活
   - Feedforward 透過 sigmoid 計算層輸出
   - 錯誤計算指導學習調整
   - 維度理解對於掌握至關重要


## 我如何學習 Transformers 中的 KQV 機制

*2025.07.16*

閱讀完 [K, Q, V Mechanism in Transformers](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en) 後，我終於某程度理解了 K、Q 和 V 的運作方式。

Q 代表 Query，K 代表 Key，V 代表 Value。對於一個句子，Query 是一個矩陣，儲存一個 token 需要向其他 token 詢問的值。Key 代表 token 的描述，而 Value 代表 token 的實際意義矩陣。

它們具有特定的形狀，因此需要了解它們的維度和細節。

我大約在 2025 年 6 月初理解了這一點。我最早在 2023 年底左右學習到它。那時候，我閱讀了像 [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) 這樣的文章，但沒有理解很多。

大約兩年後，我發現現在更容易理解了。在這兩年裡，我專注於 backend 工作和準備副學士學位考試，並沒有太多閱讀或學習關於 machine learning 的內容。然而，我也會在我開車或做其他事情時，不時思考這些概念。

這讓我想到時間的影響。我們可能乍看之下學到很多東西，即使我們沒有理解太多。但不知何故，它觸發了我們思維的起點。

隨著時間的推移，我發現對於知識和發現，第一次很難思考或理解事物。但後來，學習和了解似乎更容易了。

其中一個原因是，在 AI 時代，學習更容易，因為你可以深入任何細節或方面來解決你的疑問。還有更多相關的 AI 影片可供觀看。更重要的是，你看到很多人正在學習並在此基礎上建構專案，像是 [llama.cpp](https://github.com/ggml-org/llama.cpp)。

Georgi Gerganov 的故事令人鼓舞。作為一個大約在 2021 年開始學習 machine learning 的新人，他在 AI 社群中產生了強大的影響。

這種事情會一再發生。因此，對於 reinforcement learning 和最新的 AI 知識，即使我仍然無法投入大量時間，但我認為我可以找出一些時間快速學習並努力思考它們。大腦會完成它的工作。


---

## 從神經網絡到 GPT

*2023.09.28*

### YouTube 影片

Andrej Karpathy - Let's build GPT: from scratch, in code, spelled out.

Umar Jamil - Attention is all you need (Transformer) - Model explanation (including math), Inference and Training

StatQuest with Josh Starmer - Transformer Neural Networks, ChatGPT's foundation, Clearly Explained!!!

Pascal Poupart - CS480/680 Lecture 19: Attention and Transformer Networks

The A.I. Hacker - Michael Phi - Illustrated Guide to Transformers Neural Network: A step-by-step explanation

### 我如何學習

讀完半本 "Neural Networks and Deep Learning" 後，我開始從頭實作辨識手寫數字的神經網絡範例。我在 GitHub 上建立了一個儲存庫：https://github.com/lzwjava/neural-networks-and-zhiwei-learning。

這才是真正的難點。如果一個人能從頭開始編寫程式碼而不複製任何內容，那麼他就理解得非常透徹。

我複製的程式碼仍然缺乏 `update_mini_batch` 和 `backprop` 的實作。然而，通過仔細觀察在載入資料、feed forwarding 和評估階段的變數，我對向量、維度、矩陣和物件的形狀有了更好的理解。

我開始學習 GPT 和 Transformer 的實作。通過 word embedding 和 positional encoding，文本變成了數字。那麼，從本質上講，它與辨識手寫數字的簡單神經網絡沒有區別。

Andrej Karpathy 的「Let's build GPT」講座非常好。他解釋得很清楚。

第一個原因是，它真的是從頭開始。我們首先看到如何生成文本。它有點模糊和隨機。第二個原因是，Andrej 能夠非常直觀地表達事物。Andrej 花了數個月時間在 nanoGPT 專案上。

我剛想到一個衡量講座品質的新方法。作者真的能寫出這些程式碼嗎？為什麼我不理解，作者又遺漏了哪些主題？除了這些優雅的圖表和動畫，它們的缺點和不足是什麼？

回到 machine learning 本身的主題。正如 Andrej 提到的，dropout、residual connection、Self-Attention、Multi-Head Attention、Masked Attention。

通過觀看更多上述影片，我開始有所理解。

通過使用 sin 和 cos 函數進行 positional encoding，我們得到一些權重。通過 word embedding，我們將單詞轉換為數字。

$$
    PE_{(pos,2i)} = sin(pos/10000^{2i/d_{model}}) \\
    PE_{(pos,2i+1)} = cos(pos/10000^{2i/d_{model}}) 
$$

> The pizza came out of the oven and it tasted good.

在這個句子中，演算法如何知道 it 指的是 pizza 還是 oven？我們如何計算句子中每個詞語的相似性？

我們想要一組權重。如果我們使用 Transformer 網絡來執行翻譯任務，每次我們輸入一個句子，它就可以輸出另一種語言的相應句子。

關於這裡的點積。我們在這裡使用點積的一個原因是，點積會考慮向量中的每個數字。如果我們使用平方點積呢？我們首先計算數字的平方，然後讓它們進行點積。如果我們做一些反向點積呢？

關於這裡的 masked，我們將矩陣一半的數字更改為負無窮大。然後我們使用 softmax 使值範圍從 0 到 1。如果我們將左下方的數字更改為負無窮大呢？

### 計劃

繼續閱讀程式碼、論文和觀看影片。享受其中，跟隨我的好奇心。

https://github.com/karpathy/nanoGPT

https://github.com/jadore801120/attention-is-all-you-need-pytorch

---

## 神經網絡的運作原理

*2023.05.30*

讓我們直接討論神經網絡的核心。也就是 backpropagation 演算法：

1. 輸入 x：為輸入層設定對應的激活 $$a^{1}$$。
2. Feedforward：對於每個 l=2,3,…,L 計算 $$z^{l} = w^l a^{l-1}+b^l$$ 和 $$a^{l} = \sigma(z^{l})$$
3. 輸出誤差 $$\delta^{L}$$：計算向量 $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$
4. 反向傳播誤差：對於每個 l=L−1,L−2,…,2，計算 $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$
5. 輸出：成本函數的梯度由 $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$ 和 $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$ 給出

這段話摘自 Michael Nelson 的著作 *Neural Networks and Deep Learning*。是不是很難懂？第一次看到可能如此。但經過一個月的學習後，就不是了。我來解釋一下。

### 輸入

共有 5 個階段。第一階段是輸入。這裡我們將手寫數字作為輸入。我們的任務是辨識它們。一個手寫數字有 784 個像素，即 28*28。每個像素都有一個灰度值，範圍從 0 到 255。所以激活意味著我們使用一些函數來激活它，將其原始值更改為一個新值以方便處理。

假設我們現在有 1000 張 784 像素的圖片。我們現在訓練它來辨識它們顯示的數字。我們現在有 100 張圖片來測試學習效果。如果程式能辨識 97 張圖片的數字，我們說它的準確率是 97%。

所以我們將循環遍歷這 1000 張圖片，訓練出權重和偏差。每次我們給它一張新的圖片學習時，我們都會使權重和偏差更正確。

一個批次訓練結果將反映在 10 個神經元中。這裡，10 個神經元代表從 0 到 9，其值範圍從 0 到 1，以表示它們對其準確度的信心。

輸入是 784 個神經元。我們如何將 784 個神經元減少到 10 個神經元？這就是問題所在。假設我們有兩層。層是什麼意思？就是第一層，我們有 784 個神經元。在第二層，我們有 10 個神經元。

我們給 784 個神經元中的每個神經元一個權重，比如，

$$w_1, w_2, w_3, w_4, ... , w_{784}$$

並給第一層一個偏差，即 $$b_1$$。

所以對於第二層的第一個神經元，其值是：

$$w_1*a_1 + w_2*a_2+...+ w_{784}*a_{784}+b_1$$

但是這些權重和偏差是針對 $$neuron^2_{1}$$（第二層的第一個神經元）的。對於 $$neuron^2_{2}$$，我們需要另一組權重和偏差。

Sigmoid 函數如何？我們使用 sigmoid 函數將上述值映射到 0 到 1 的範圍。

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

我們也使用 sigmoid 函數來激活第一層。也就是說，我們將那個灰度值更改為 0 到 1 的範圍。所以現在，每一層的每個神經元的值都在 0 到 1 之間。

所以現在對於我們的兩層網絡，第一層有 784 個神經元，第二層有 10 個神經元。我們訓練它以獲得權重和偏差。

我們有 784 * 10 個權重和 10 個偏差。在第二層，對於每個神經元，我們將使用 784 個權重和 1 個偏差來計算其值。程式碼如下：

```python
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
```

### Feedforward

> Feedforward: 對於每個 l=2,3,…,L 計算 $$z^{l} = w^l a^{l-1}+b^l$$ 和 $$a^{l} = \sigma(z^{l})$$

請注意，這裡我們使用上一層的值，即 $$a^{l-1}$$ 和當前層的權重 $$w^l$$ 及其偏差 $$b^l$$ 進行 sigmoid 運算，以獲得當前層的值 $$a^{l}$$。

程式碼：

```python
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x] 
        zs = [] 
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
```
### 輸出誤差

> 輸出誤差 $$\delta^{L}$$：計算向量 $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$

讓我們看看 $$\nabla$$ 是什麼意思。

> Del，或 nabla，是數學中（特別是向量微積分中）使用的一種運算符，作為向量微分運算符，通常以 nabla 符號 ∇ 表示。

$$
\begin{eqnarray}
  w_k & \rightarrow & w_k' = w_k-\eta \frac{\partial C}{\partial w_k} \\
  b_l & \rightarrow & b_l' = b_l-\eta \frac{\partial C}{\partial b_l}
\end{eqnarray}
$$

這裡的 $$\eta $$ 是學習率。我們使用 C 相對於權重和偏差的導數，即它們之間的變化率。這就是下面的 `sigmoid_prime`。

程式碼：

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

### 反向傳播誤差

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

### 輸出

> 輸出：成本函數的梯度由 $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$
和 $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$ 給出

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

### 總結

這是一篇短文章。大部分內容只是展示了程式碼和數學公式。但對我來說沒問題。在撰寫之前，我並不完全理解。在撰寫或只是從程式碼和書中複製片段之後，我理解了大部分內容。在獲得 Yin Wang 老師的信心、閱讀了約 30% 的 *Neural Networks and Deep Learning* 一書、聽了 Andrej Karpathy 的史丹福講座和 Andrew Ng 的課程、與朋友 Qi 討論，並調整了 Anaconda、numpy 和 Theano 函式庫以使多年前的程式碼能夠運作之後，我現在理解了它。

其中一個關鍵點是維度。我們應該知道每個符號和變數的維度。它只是進行可微分運算。讓我們以 Yin Wang 的名言結束：

> Machine learning 確實非常有用，甚至可以說是一種美麗的理論，因為它只是微積分經過一番改造！它是牛頓、萊布尼茨古老而偉大的理論，以一種更簡單、優雅而強大的形式呈現。Machine learning 本質上是利用微積分來推導和擬合一些函數，而 deep learning 則是擬合更複雜的函數。

> 在 artificial intelligence 中沒有「intelligence」，在 neural network 中沒有「neural」，在 machine learning 中沒有「learning」，在 deep learning 中也沒有「depth」。真正起作用的是「calculus」。所以我更喜歡將這個領域稱為「differentiable computing」，而建構模型的過程稱為「differentiable programming」。