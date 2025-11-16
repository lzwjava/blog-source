---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 比較浮點數精度格式
translated: true
type: note
---

### float32、float16 與 bfloat16 的差異

這些是計算中使用的浮點數資料類型，特別是在機器學習框架中（例如您分享的 PyTorch 程式碼片段）。它們在位元寬度上有所不同，這會影響精度（數字表示的準確程度）、動態範圍（可處理的數值範圍）、記憶體使用量以及計算速度。以下為詳細說明：

- **float32（單精度）**：
  - 總共 32 位元：1 個符號位元、8 個指數位元、23 個尾數（小數）位元。
  - 高精度和寬動態範圍（指數允許數值範圍約從 1e-38 到 1e+38）。
  - 優點：對大多數計算準確，在許多情境下避免溢位/下溢位。
  - 缺點：記憶體使用量較高（每個數字 4 位元組），在 GPU 上計算速度較慢，因為需要更多頻寬和處理能力。
  - 常見於傳統的 CPU 基礎計算或需要完全準確度的情況。

- **float16（半精度）**：
  - 總共 16 位元：1 個符號位元、5 個指數位元、10 個尾數位元。
  - 較低精度和較窄動態範圍（指數限制數值範圍約從 1e-7 到 65504）。
  - 優點：記憶體使用量減半（每個數字 2 位元組），並在支援的硬體（例如現代 GPU）上加速計算，對於像 LLM 這樣記憶體是瓶頸的大型模型非常有用。
  - 缺點：容易發生溢位（大數）或下溢位（小數/梯度），這可能導致訓練期間出現 NaN（非數字）等問題。同時在表示中會損失更多細節。

- **bfloat16（大腦浮點數）**：
  - 總共 16 位元：1 個符號位元、8 個指數位元、7 個尾數位元。
  - 與 float32 的動態範圍匹配（相同的指數位元，因此數值範圍相似），但精度降低（較少的尾數位元）。
  - 優點：與 float16 相同的記憶體節省（2 位元組），但由於範圍更廣，在深度學習中穩定性更好——較不容易發生溢位/下溢位。它專為神經網路設計，在訓練中表現良好，無需太多縮放或正規化。
  - 缺點：精度甚至比 float16 更低，可能導致稍微更多的近似誤差，但在實踐中，對於 LLM 來說通常可以忽略不計。

在您展示的程式碼中（`dtype = 'bfloat16' if torch.cuda.is_available() and torch.cuda.is_bf16_supported() else 'float16'`），它選擇 bfloat16（如果 GPU 支援，常見於較新的 NVIDIA/AMD 硬體），否則回退到 float16。這用於混合精度設定，其中計算使用較低精度以獲得速度，同時將某些部分（例如累加器）保持在較高精度以維持準確性。在許多現代設定中（例如 Google 用於 TPU），bfloat16 是首選，因為它在範圍上更像 float32，減少了訓練不穩定性。

### 量化方法及其關聯性

量化是一種減少模型權重、激活值（有時包括梯度）位元寬度的技術，進一步壓縮模型，不僅僅是使用 float16/bfloat16。它與您程式碼中切換資料類型（這更多是關於運行時的浮點精度）不同，但相關，因為兩者都旨在優化 LLM 的效率。

- **什麼是量化？**
  - 它將高精度值（例如 float32）映射到較低位元的表示（例如 int8、int4，甚至自定義浮點數）。這減少了記憶體佔用和推理時間，對於在邊緣設備上或大規模部署 LLM 至關重要。
  - 例如：一個 float32 權重（32 位元）可能被量化為 int8（8 位元），大小減少 4 倍。

- **常見的量化方法**：
  - **訓練後量化（PTQ）**：在訓練後應用。簡單但如果未校準（例如使用小數據集調整尺度）可能會降低準確性。方法如最小-最大縮放或基於直方圖的（例如在 TensorRT 或 ONNX 中）。
  - **量化感知訓練（QAT）**：在訓練期間模擬量化（例如 PyTorch 中的偽量化操作），因此模型學會處理降低的精度。更準確但需要重新訓練。
  - **進階變體**：
    - **僅權重量化**：僅量化權重（例如到 int4），保持激活值在 float16/bfloat16。
    - **分組量化**：分組量化（例如 GPTQ 方法分組權重以獲得更好的準確性）。
    - **AWQ（激活感知權重量化）**：考慮激活分佈以獲得更好的裁剪。
    - **INT4/INT8 與反量化**：在推理期間，反量化回 float16 進行計算。

- **與 float16/bfloat16/float32 的關係**：
  - 您的資料類型選擇是*混合精度*的一種形式（例如 PyTorch 中的 AMP），它使用 float16/bfloat16 進行大多數操作，但縮放到 float32 以防止下溢位。量化通過使用整數或甚至更低位的浮點數更進一步。
  - 它們在優化流程中相關：從 float32 訓練開始，切換到 bfloat16 以加快訓練，然後量化到 int8 以進行部署。例如，像 Hugging Face Transformers 這樣的庫在加載時使用 `torch_dtype=bfloat16`，然後應用量化（例如通過 BitsAndBytes）減少到 4 位元。
  - 權衡：較低的精度/量化加速了過程，但存在準確性損失的風險（例如 LLM 中的困惑度增加）。bfloat16 通常在完全量化之前是一個理想的折衷點。

### 與 Flash Attention 的關係

Flash Attention 是一種用於在 transformer 中計算注意力（LLM 如 GPT 的關鍵部分）的優化算法。它通過即時重新計算中間值而不是存儲它們來減少記憶體使用並加速，特別適用於長序列。

- **精度如何相關**：
  - Flash Attention（例如通過 `torch.nn.functional.scaled_dot_product_attention` 或 flash-attn 庫）原生支援較低精度如 float16/bfloat16。事實上，在這些資料類型中通常更快，因為 GPU（例如 NVIDIA Ampere+）對它們有硬體加速（例如 Tensor Cores）。
  - 您的程式碼的資料類型選擇直接影響它：使用 bfloat16 或 float16 啟用 Flash Attention 的高性能模式，因為它可以融合操作並避免記憶體瓶頸。在 float32 中，它可能回退到較慢的實現。
  - 量化也與之相關——量化模型如果在計算期間反量化到 float16，則可以使用 Flash Attention。像 vLLM 或 ExLlama 這樣的庫將 Flash Attention 與量化集成，實現超快推理。

在 PyTorch 中，如果您設置 `torch.backends.cuda.enable_flash_sdp(True)`，當資料類型是 float16/bfloat16 且硬體支援時，它會優先使用 Flash Attention。

### 浮點精度在 LLM 模型中的一般使用

在大型語言模型（LLM）如 GPT、Llama 或 Grok 中：

- **訓練**：通常從 float32 開始以獲得穩定性，但轉向 bfloat16（例如在 Google 的模型中）或混合精度（float16 帶有 float32 縮放）以更快處理大規模數據集。bfloat16 越來越受歡迎（例如在 PyTorch 2.0+ 中），因為它比 float16 需要更少的超參數調整。
- **推理/部署**：float16 或 bfloat16 在 GPU 上為速度而常見。為了更高的效率（例如在消費級硬體上），模型被量化到 8 位元或 4 位元（例如 llama.cpp 中的 GGUF 格式）。這允許在 <24GB VRAM 上運行 700 億參數模型。
- **權衡**：
  - 較高精度（float32）：更好的準確性，但更慢且更耗記憶體。
  - 較低精度：更快、更輕量，但可能導致輸出質量下降（例如在極端量化中幻覺稍微增加）。
- **趨勢**：隨著像 NVIDIA H100（強大的 bfloat16 支援）這樣的硬體，bfloat16 正在成為標準。像 PEFT（參數高效微調）這樣的工具將其與量化結合以進行微調。在開源中，像 Transformers 或 Optimum 這樣的庫處理自動資料類型轉換和量化。

如果您在程式碼中實現這一點，請在您的硬體上測試——bfloat16 在較新的 GPU 上表現出色，而 float16 更通用但在梯度處理上更棘手。

參考資料：  
[理解深度學習中的浮點精度](https://towardsdatascience.com/understanding-fp32-fp16-bf16-in-neural-networks-27075c96b4d3)  
[LLM 的量化技術](https://huggingface.co/docs/transformers/quantization)  
[Flash Attention 解釋](https://arxiv.org/abs/2205.14135)  
[PyTorch 中的混合精度訓練](https://pytorch.org/docs/stable/amp.html)