---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 為何大型語言模型避免使用S型函數
translated: true
type: note
---

### 為何 GPT/LLM 模型不使用 Sigmoid 函數

大型語言模型（LLM）如 GPT 依賴 Transformer 架構，其中激活函數在前饋網絡（FFN）層中引入非線性及處理注意力輸出方面扮演關鍵角色。雖然 Sigmoid 函數——定義為 \\(\sigma(x) = \frac{1}{1 + e^{-x}}\\)，可將輸入壓縮至 (0, 1) 範圍——在早期神經網絡（例如用於二元分類）中頗受歡迎，但在現代 LLM 的內部激活中已基本避免使用。以下按關鍵問題逐一說明原因：

#### 1. **梯度消失問題**
   - Sigmoid 在極端值處飽和：對於極大的正數 \\(x\\)，\\(\sigma(x) \approx 1\\)；對於極大的負數 \\(x\\)，\\(\sigma(x) \approx 0\\)。
   - 其導數為 \\(\sigma'(x) = \sigma(x)(1 - \sigma(x))\\)，在這些區域會趨近於 0。在反向傳播過程中，這會導致梯度「消失」（變得極小），使深層網絡的學習停滯。
   - LLM 中的 Transformer 架構極深（例如 GPT-4 有 100 多層），因此此問題會影響訓練效率。替代方案如 ReLU（\\(f(x) = \max(0, x)\\)）或 GELU（我們之前討論過）能避免對負輸入完全飽和，從而實現更好的梯度流動。

#### 2. **非零中心輸出**
   - Sigmoid 總是輸出正值（0 到 1），這在優化過程中會對權重更新產生偏差，導致梯度下降路徑呈「之字形」，減慢收斂速度，相比之下，如 tanh 或 GELU 等零中心函數表現更佳。
   - 在 Transformer 中，FFN 層處理高維度嵌入，零中心激活有助於在殘差連接中保持穩定的信號傳播。

#### 3. **實證表現不佳**
   - 大量實驗顯示，Sigmoid 在自然語言處理任務中的表現落後於現代激活函數。早期 Transformer（例如原始 GPT）使用 ReLU 以追求速度和簡潔性。後來的模型如 GPT-2/3 轉向 GELU，因其平滑的概率特性在實證上能提升準確度和收斂速度，且無 Sigmoid 的缺點。
   - 某些 LLM（例如 InstructGPT）中出現了如 SiLU（Sigmoid 線性單元，\\(f(x) = x \cdot \sigma(x)\\)）的變體，但這並非單純的 Sigmoid——它乘以 \\(x\\) 以修正零中心問題並減少飽和。

#### 4. **輸出層考量**
   - 在 LLM 的下一個詞預測任務中，最終層使用 **softmax** 對 logits 進行處理（一種歸一化的多 Sigmoid 函數），而非 Sigmoid。Sigmoid 適用於二元決策，但對於多類別詞彙（例如 5 萬多個詞元）則不適用，因為其輸出總和不等於 1，會導致概率不穩定。
   - Softmax 確保了有效的概率分佈，這對於交叉熵損失函數至關重要。

#### 何時仍會使用 Sigmoid？
- 在 LLM 的隱藏層中極少使用，但偶爾會出現在特殊位置，如二元門控或較舊的 RNN/LSTM（Transformer 時代之前）。
- 在視覺模型（例如某些 CNN）中，有時會用於像素歸一化，但不用於專注於文本的 LLM。

總而言之，Sigmoid 在 1980 年代的優雅特性無法擴展至 LLM 的深度和規模。ReLU/GELU/Swish 等函數能提供更快、更可靠的訓練，且陷阱更少。若您正在調整模型，建議從 GELU 開始以確保與 Transformer 的兼容性。

#### 參考資料
- [Transformer 模型中的線性層與激活函數](https://machinelearningmastery.com/linear-layers-and-activation-functions-in-transformer-models/)
- [深度學習 101：Transformer 激活函數詳解](https://www.saltdatalabs.com/blog/deep-learning-101-transformer-activation-functions-explainer-relu-leaky-relu-gelu-elu-selu-softmax-and-more)
- [常見激活函數](https://www.aussieai.com/book/ch21-common-activation-functions)
- [理解 Logits、Sigmoid、Softmax 與交叉熵損失](https://wandb.ai/amanarora/Written-Reports/reports/Understanding-Logits-Sigmoid-Softmax-and-Cross-Entropy-Loss-in-Deep-Learning--Vmlldzo0NDMzNTU3)