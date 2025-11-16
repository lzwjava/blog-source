---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 優化矩陣乘法以提升大型語言模型效能
translated: true
type: note
---

是的，針對大型語言模型（LLM）訓練中的浮點數矩陣乘法（matmul），確實存在多種優化方法，這與競技程式設計（CP）中的大數乘法技術有某些鬆散的相似之處。我將逐步分解說明，並探討精度問題、dropout，以及為何 dropout 不會在矩陣乘法或單個浮點數乘法「期間」應用。請記住，LLM 訓練專注於大規模效率（例如在 GPU/TPU 上），優先考慮速度和記憶體使用，而非完美的精度，這與 CP 中常要求精確算術的大整數運算不同。

### LLM 訓練中浮點數矩陣乘法的優化
矩陣乘法是 LLM 中的核心瓶頸（例如在注意力層和前饋網路中），通常佔據 80-90% 的計算時間。標準矩陣乘法具有 O(n³) 的複雜度，但優化方法利用了硬體、降低精度和演算法調整：

- **較低精度格式**：為了加速訓練並減少記憶體使用，LLM 通常使用降低的浮點數精度，如 FP16（半精度）、BF16（大腦浮點數）、FP8，甚至 FP4，而不是 FP32/FP64。這減少了資料大小（例如，FP8 每個數字使用 1 位元組，而 FP32 使用 4 個位元組），並通過 NVIDIA GPU 上的張量核心實現更快的硬體加速。例如，FP8 可以通過動態量化以最小的精度損失將矩陣乘法加速 2-4 倍。同樣地，FP4 框架引入了可微分估計器來處理反向傳播期間的量化雜訊。

- **混合精度訓練**：計算以低精度進行（例如 FP16 矩陣乘法），但累加（乘積求和）使用較高精度（例如 FP32）以避免溢位/下溢。這在速度與穩定性之間取得平衡——PyTorch 中的 AMP（自動混合精度）等工具可自動化此過程。在 LLM 預訓練中，這通常能實現 2-3 倍的速度提升，而不降低模型品質。

- **融合核心與硬體優化**：像 cuBLAS 或 TensorRT 這樣的庫將矩陣乘法與其他操作（例如激活函數或歸一化）融合到單個核心中，減少了記憶體存取開銷。對於 LLM，Flash Attention 將注意力矩陣乘法與 softmax 和遮罩融合，將記憶體使用量減少高達 50%。自訂實作（例如使用 C++ 或 Rust）針對特定硬體優化了快取局部性和並行性。

- **演算法替代方案**：受 CP 中快速乘法（例如用於大整數的 Karatsuba 或 FFT，將複雜度降低到 O(n log n)）的啟發，一些 LLM 研究探索了 Strassen 類演算法或矩陣乘法近似。更激進的是，「無矩陣乘法」模型用三元權重（-1, 0, 1）和位元操作（例如 BitNet 或 1-bit LLMs）取代浮點數矩陣乘法，通過完全避免浮點數運算實現 10 倍的效率提升。這與 CP 的精確整數乘法相呼應，但以精度換取速度——在推理中很有用，並在訓練中逐漸興起。

- **稀疏和結構化矩陣乘法**：如果存在稀疏性（例如來自剪枝），使用稀疏矩陣乘法庫來跳過零計算。結構化 dropout 可以在訓練期間誘導稀疏性，並針對其進行優化。

這些優化在 Hugging Face Transformers 或 Lightning AI 等框架中經過實戰測試，通常能將訓練吞吐量提高 2-10 倍。

### 浮點數矩陣乘法中的精度問題
浮點數具有有限的精度（例如 FP16 具有約 11 位尾數，在反向傳播期間的小梯度中存在下溢風險）。在 LLM 中，這在大型矩陣（例如數十億參數）中被放大，導致：
- **累積誤差**：對許多小乘積求和可能會丟失細節或導致溢位。
- **非結合性**：在浮點數中，(a + b) + c ≠ a + (b + c)，導致在不同硬體上產生不可重現的結果。
- **量化雜訊**：低精度格式引入捨入誤差，可能使訓練不穩定。

緩解措施：
- 損失縮放：在反向傳播之前將損失乘以一個因子（例如 2^15），然後再將梯度縮放回來。
- 微縮放格式或模擬高精度累加器。
- 隨機捨入：隨機捨入而不是截斷以減少偏差。

在 CP 中，大數乘法（例如通過 FFT）使用任意精度整數來獲得精確結果，完全避免了浮點數的陷阱。LLM 無法承受這種開銷，因此它們接受帶有安全措施的近似浮點數——精度對於泛化來說「足夠好」，而非精確數學。

### Dropout 及其與矩陣乘法的關係
Dropout 是一種正則化技術，在訓練期間隨機將元素歸零（例如 10-20% 的比率）以防止過擬合——它是在層*之後*應用，而不是在矩陣乘法或單個浮點數乘法*期間*應用。例如：
- 在程式碼中：`output = dropout(matmul(input, weights))`
- 矩陣乘法本身是一個原子操作（例如通過 BLAS 庫），計算完整的點積而不中斷。

你*不會*「在矩陣乘法期間進行 dropout」，因為：
- 矩陣乘法是低階線性代數；在計算過程中注入 dropout 會破壞數學運算和效率。
- Dropout 在矩陣乘法後加入雜訊，這有助於正則化，但與精度修復無關。事實上，通過放大小值，它可能加劇低浮點數精度問題，但我們會單獨處理（例如通過縮放）。
- 在推理期間（非訓練），dropout 被完全禁用——沒有隨機丟棄。

然而，為了優化：
- 融合 dropout（例如在 Flash Attention 中）將其與矩陣乘法結合以隱藏 RNG 開銷，在不改變語義的情況下將性能提高 10-20%。
- 如果 dropout 對精度影響太大，會使用像層歸一化或權重衰減這樣的替代方案，但它在 LLM 訓練中是標準做法。

總之，你是對的——我們不會在矩陣乘法或浮點數乘法期間應用 dropout。它是一個更高層級的操作。

如果你正在實作這個（例如在自訂訓練器中），請從混合精度和融合操作開始。對於 CP 風格的大數啟發，請研究基於整數的 LLM 變體，如 BitNet，以進行精度穩健的訓練。

[FP8 GEMM LLM Training - Emergent Mind](https://www.emergentmind.com/topics/fp8-gemm-llm-training)  
[Floating-Point 8: An Introduction to Efficient, Lower-Precision AI](https://developer.nvidia.com/blog/floating-point-8-an-introduction-to-efficient-lower-precision-ai-training/)  
[Optimizing Large Language Model Training Using FP4 Quantization](https://arxiv.org/html/2501.17116v1)  
[Beyond Matrix Multiplacations: The New Frontier of LLMs with 10x Efficiency](https://machine-learning-made-simple.medium.com/beyond-matmul-the-new-frontier-of-llms-with-10x-efficiency-fef21ee32eb6)  
[4-bit LLM training and Primer on Precision, data types & Quantization](https://vizuara.substack.com/p/4-bit-llm-training-and-primer-on)  
[Accelerating Large Language Models with Mixed-Precision](https://lightning.ai/pages/community/tutorial/accelerating-large-language-models-with-mixed-precision-techniques/)  
[Microscaling Floating Point Formats for Large Language Models](https://arxiv.org/html/2510.01863v1)  
[Understanding Floating Point Numbers and Precision in the Context of LLMs](https://dhnanjay.medium.com/understanding-floating-point-numbers-and-precision-in-the-context-of-large-language-models-llms-3b4d981a8266)  
[MatMul-Free LLMs: Key Concepts Explained](https://www.datacamp.com/blog/matmul-free-language-models)  
[Reducing the Cost of Dropout in Flash-Attention](https://arxiv.org/html/2410.07531)  
[Efficient Sparse Training with Structured Dropout](https://arxiv.org/html/2411.01238v1)  
[Writing an LLM from scratch, part 10 -- dropout](https://www.gilesthomas.com/2025/03/llm-from-scratch-10-dropout)