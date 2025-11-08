---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GELU 激活函數概述
translated: true
type: note
---

### 什麼是 GELU？

高斯誤差線性單元（GELU）是一種用於神經網路的平滑激活函數，尤其常見於基於 Transformer 的模型，如 BERT 和 GPT 系列。該函數由研究員 Dan Hendrycks 和 Kevin Gimpel 於 2016 年提出，結合了線性轉換的優勢與受高斯（常態）分佈啟發的機率加權。相較於 ReLU（對負輸入輸出零）等簡單激活函數，GELU 允許負值有少量梯度流動，從而透過減少梯度消失等問題並改善收斂性，提升深度網路的效能。

#### 數學定義
GELU 的核心公式為：

\\[
\text{GELU}(x) = x \cdot \Phi(x)
\\]

其中 \\(\Phi(x)\\) 是標準常態分佈的累積分佈函數（CDF）：

\\[
\Phi(x) = \frac{1}{2} \left[ 1 + \erf\left( \frac{x}{\sqrt{2}} \right) \right]
\\]

此處的 \\(\erf\\) 是誤差函數，用於衡量高斯分佈逼近階躍函數的程度。這使得 GELU 具有機率特性：它對負輸入的「抑制」比 ReLU 更溫和，同時保留正輸入的完整性。

為了提升計算效率，通常會使用近似公式，例如基於 sigmoid 的版本：

\\[
\text{GELU}(x) \approx x \cdot \sigma(1.702x)
\\]

其中 \\(\sigma\\) 是 sigmoid 函數。

#### 為何使用 GELU？
- **平滑性**：處處可微，有助於優化過程。
- **非單調性**：輕微抑制負值但不將其歸零，從而保留資訊。
- **實證優勢**：在自然語言處理等任務中表現優於 ReLU 和 ELU，於大型模型中能實現更快的訓練速度與更高的準確度。
- **缺點**：由於需計算 erf 或 sigmoid，運算量略高於 ReLU。

實務上，PyTorch 和 TensorFlow 等程式庫均內建了 GELU 的實現（例如 `torch.nn.GELU()`）。

#### 參考資料
- [Gaussian Error Linear Units (GELUs)](https://arxiv.org/abs/1606.08415)
- [GELU Explained](https://www.baeldung.com/cs/gelu-activation-function)
- [GELU Activation](https://medium.com/@shauryagoel/gelu-gaussian-error-linear-unit-4ec59fb2e47c)