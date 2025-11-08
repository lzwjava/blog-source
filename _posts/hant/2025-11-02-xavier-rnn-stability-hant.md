---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Xavier初始化對循環神經網絡穩定性的影響
translated: true
type: note
---

### 為什麼 RNN 需要 Xavier 初始化？

RNN（循環神經網絡）依賴 Xavier（亦稱 Glorot）初始化來設置其權重矩陣——例如 `Wxh`（輸入到隱藏層）、`Whh`（隱藏層到隱藏層，即循環權重）和 `Why`（隱藏層到輸出層）——以維持穩定的訓練動態。您程式碼中的具體形式使用高斯（常態）分佈，並以 `sqrt(1 / fan_in)` 進行縮放，其中 `fan_in` 是該層的輸入神經元數量。這能將權重的變異數維持在 `1 / fan_in` 左右，確保輸入訊號不會被過度放大或壓縮。

以下是這對 RNN 至關重要的原因，以及為何簡單地從 [0, 1] 均勻隨機抽取會導致問題：

#### 1. **跨層與時間步保留訊號變異數**
   - 在前饋網絡中，Xavier 有助於在訊號向前傳播（及梯度向後傳播）時，保持*激活值的變異數*大致穩定。若無此機制，深層網絡可能出現激活值爆炸（變得極大）或消失（降至接近零），導致訓練無法進行。
   - RNN 如同在時間維度上*展開的「深層」網絡*：循環權重 `Whh` 在每個時間步與隱藏狀態相乘，形成一連串的乘法鏈（例如，對於序列長度 *T*，就如同 *T* 層深度）。若 `Whh` 中的權重變異數 >1，梯度在反向傳播時會呈指數級爆炸（對長序列尤其不利）。若 <1，梯度則會消失。
   - Xavier 的縮放（例如對 `Whh` 使用 `* sqrt(1. / hidden_size)`）能確保隱藏狀態的期望變異數維持在 ~1，避免此問題。若使用 [0,1] 均勻初始化：
     - 平均值 ~0.5（偏向正值，導致偏移）。
     - 變異數 ~1/12 ≈ 0.083——對於較大的 `hidden_size`（例如 512）而言過小，會導致訊號迅速消失。

#### 2. **適應層的維度**
   - Xavier 考慮了 *fan_in*（層的輸入數）有時也考慮 *fan_out*（輸出數）。對於 `Wxh`，以 `sqrt(1 / input_size)` 縮放能根據詞彙量或嵌入維度進行標準化。對於 `Whh`，則基於 `hidden_size` 以匹配循環迴路。
   - [0,1] 初始化忽略維度：在大型隱藏層（例如 1000 個單元）中，對大量 [0,1] 輸入進行未經縮放的加總會淹沒下一層。而在小型層中，則會導致下溢。

#### 3. **透過時間反向傳播中的梯度流動**
   - RNN 訓練使用 BPTT，梯度會向後傳播 *T* 個時間步。不良的初始化會導致「梯度消失問題」（在普通 RNN 中常見，這也是 LSTM/GRU 出現的原因）。Xavier 透過以平衡的幅度開始來緩解此問題。
   - 實證研究（例如 Glorot 和 Bengio 的原始論文）顯示，在深度/循環網絡中，Xavier 能將收斂所需週期減少 2-10 倍。

#### 替代方案與何時 [0,1] 初始化可能「有效」
- [0,1] 初始化可能在極小的玩具模型（例如單層、短序列）中「有效」，但在規模擴大時會失敗——例如出現梯度爆炸或 NaN 損失。
- 現代調整：He 初始化（適用於 ReLU，縮放係數為 `sqrt(2 / fan_in)`）或正交初始化（適用於 RNN，能精確保持範數）。但 Xavier 對於 RNN 中常見的 sigmoid/tanh 激活函數而言，仍是安全的預設選擇。

總之，Xavier 的核心在於*穩定性優先*：它將權重設置得小而不過小，並考慮維度，讓梯度能自由流動。隨機的 [0,1] 初始化過於粗糙——就像未平衡輪胎就猛踩油門。

深入閱讀：  
[Understanding the Difficulty of Training Deep Feedforward Neural Networks](http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf) (Glorot & Bengio, 2010)  
[Recurrent Neural Network Regularization](https://arxiv.org/abs/1409.2329) (Zaremba et al., 關於 RNN 初始化問題)