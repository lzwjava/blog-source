---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 詞彙與位置嵌入詳解
translated: true
type: note
---

### GPT 模型中 `wte` 與 `wpe` 的解釋

在這套 GPT 模型實現（基於 Andrej Karpathy 的 NanoGPT 風格）中，`transformer` 模組包含數個關鍵組件。您詢問的 `wte` 和 `wpe` 都是 `nn.Embedding` 層的實例，用於將離散輸入（如詞元與位置）轉換為稱為**嵌入向量**的稠密向量表示。嵌入向量是 transformer 模型的核心部分，讓神經網絡能夠為分類數據學習具意義的數值表示。

#### 什麼是 `wte`？
- **全稱**：詞元嵌入（有時稱為「詞語詞元嵌入」）
- **用途**：將詞彙表中的每個獨特**詞元**（例如單詞、子詞或字符）映射到固定大小的向量，維度為 `config.n_embd`（模型的嵌入大小，通常為 768 或類似值）
  - 詞彙表大小為 `config.vocab_size`（例如典型 GPT 分詞器的 50,000）
  - 輸入：整數詞元 ID（0 到 vocab_size-1）
  - 輸出：代表該詞元「語義」的學習向量
- **必要性**：原始詞元 ID 只是不帶語義資訊的整數。嵌入將其轉化為能捕捉關聯性的向量（例如經過訓練後，「king」與「queen」可能會獲得相似向量）

#### 什麼是 `wpe`？
- **全稱**：位置嵌入
- **用途**：將輸入序列中的每個**位置**（從 0 到 `config.block_size - 1`，其中 block_size 是最大序列長度，例如 1024）映射到相同維度 `config.n_embd` 的固定大小向量
  - 輸入：整數位置索引（0 到 block_size-1）
  - 輸出：編碼序列中位置資訊的學習向量
- **必要性**：Transformer 並行處理序列且沒有內建順序感知能力（不同於 RNN）。位置嵌入注入關於詞元相對或絕對位置的信息，讓模型能區分位置 1 的「cat」與位置 10 的「cat」

#### 嵌入在訓練中的運作原理
您說得完全正確——這些是神經網絡中的**可學習參數**：
- **初始化**：PyTorch 的 `nn.Embedding` 會隨機初始化嵌入矩陣（默認使用 -√(1/dim) 到 +√(1/dim) 之間的均勻分佈，其中 dim 為 `n_embd`）。這賦予它們非零且非隨機噪聲的初始值
- **訓練過程**：在模型訓練期間（例如通過語言建模損失的反向傳播），梯度會像更新其他參數（如 transformer 區塊中的參數）一樣更新這些嵌入權重。隨著時間推移，它們會學習以最小化損失的方式表示詞元與位置——捕捉語義、句法和位置依賴關係
- **前向傳播中的應用**：（雖然您的程式碼片段未顯示，但典型做法）對於詞元 ID 序列 `x`，模型會計算：
  ```
  token_emb = wte(x)  # 形狀：(batch_size, seq_len, n_embd)
  pos_emb = wpe(torch.arange(seq_len))  # 廣播以匹配 token_emb
  input_emb = token_emb + pos_emb  # 逐元素相加
  ```
  接著 `input_emb`（經過 dropout 後）會輸入到 transformer 區塊（`h`）中

這樣的配置對於 GPT 類模型既高效又標準。如果您有完整的前向傳播過程或更多程式碼，我可以進行更深入的解析！