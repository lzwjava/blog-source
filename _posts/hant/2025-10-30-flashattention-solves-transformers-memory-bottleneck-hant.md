---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: FlashAttention 解決變壓器記憶體瓶頸問題
translated: true
type: note
---

### 背景：標準注意力機制在 Transformer 中的挑戰

Transformer 是 GPT 和 BERT 等模型的骨幹，其運作高度依賴自注意力機制來處理序列。在自注意力機制中，給定輸入序列表示為查詢矩陣 \\(Q\\)、鍵矩陣 \\(K\\) 和值矩陣 \\(V\\)（每個矩陣的形狀為 \\(N \times d\\)，其中 \\(N\\) 是序列長度，\\(d\\) 是頭部維度，通常為 64-128），注意力輸出 \\(O\\) 的計算方式如下：

\\[
S = QK^T \in \mathbb{R}^{N \times N}, \quad P = \softmax(S) \in \mathbb{R}^{N \times N}, \quad O = PV \in \mathbb{R}^{N \times d},
\\]

其中 \\(\softmax\\) 按行應用，且 \\(S\\) 通常會縮放 \\(\tau = 1 / \sqrt{d}\\) 以確保穩定性。此外，常見的附加操作包括因果遮罩（用於自回歸模型）和 dropout。

這種公式雖然優雅，但計算成本高昂。中間矩陣 \\(S\\) 和 \\(P\\) 的大小為 \\(N \times N\\)，導致在序列長度 \\(N\\) 上的**時間和記憶體複雜度為二次方** \\(O(N^2)\\)。對於長上下文（例如 GPT-2 中的 \\(N = 4096\\) 或現代 LLM 中高達 128k 的序列），這成為嚴重的瓶頸：

- **記憶體需求龐大**：在 GPU 上，高頻寬記憶體（HBM）是主要儲存空間，但實體化 \\(S\\) 和 \\(P\\) 可能會超過可用 HBM（例如 A100/H100 上的 40-80 GB）。在 \\(N=4096\\)、\\(d=64\\) 的情況下，僅中間結果就會消耗約 1-2 GB，再加上輸入/輸出/激活值，經常導致記憶體不足（OOM）錯誤。
- **速度限制**：注意力機制受記憶體頻寬限制，而非計算能力限制。現代 GPU（例如 NVIDIA A100）具有約 1.5 TB/s 的 HBM 頻寬，但計算能力約為 19 TFLOPS — 然而像 softmax 這樣的操作需要多次讀寫完整的 \\(N^2\\) 矩陣（例如在前向/反向傳播中每個元素需要 4-6 次 HBM 存取）。這導致實際運行時間呈二次方增長：例如，在 PyTorch 中，當 \\(N=4096\\) 時，前向傳播約為 36 ms，反向傳播約為 88 ms。
- **訓練/生成障礙**：在訓練期間，梯度需要儲存 \\(P\\) 以供反向傳播使用，這使記憶體需求加倍。對於推理，長上下文（例如 64k 個 token）若沒有近似方法（如稀疏注意力或低秩方法，例如 Reformer、Linformer）則無法實現，這些方法以精確度換取效率，但由於忽略 I/O 成本而通常表現不佳。

FlashAttention（由 Tri Dao 等人於 2022 年提出）通過重新設計算法，使其**具備 I/O 感知能力**，並利用 GPU 記憶體層級結構（快速的 SRAM ~20 MB 對比緩慢的 HBM），無需近似即可解決這些問題。

### 核心思想：分塊、核心融合與線上 Softmax

FlashAttention 通過以下方式計算**精確**注意力（無需近似）：

1. **分塊**：不實體化完整的 \\(N \times N\\) 矩陣，而是將 \\(Q, K, V\\) 劃分為可放入 SRAM 的小區塊。將 \\(Q\\) 拆分為 \\(T_r = \lceil N / B_r \rceil\\) 個大小為 \\(B_r \times d\\) 的行區塊（例如 \\(B_r \approx 64-256\\)），並將 \\(K, V\\) 拆分為 \\(T_c = \lceil N / B_c \rceil\\) 個大小為 \\(B_c \times d\\) 的列區塊（例如 \\(B_c \approx 128-1024\\)）。區塊大小根據 SRAM 容量 \\(M\\) 動態選擇（例如 \\(B_c \approx M / (4d)\\)），以最大化重用。

2. **核心融合**：所有操作（用於 \\(S\\) 的矩陣乘法、遮罩、softmax、dropout、用於 \\(O\\) 的矩陣乘法）融合為單一 CUDA 核心。這避免了將中間結果寫入 HBM，減少 I/O 約 50-70%。該核心將區塊從 HBM 加載到 SRAM，在晶片上計算，並僅將部分和寫回 — 例如，每個區塊僅進行一次 HBM 讀取/寫入，而不是每個元素。

3. **帶統計量的線上 Softmax**：Softmax 無法在沒有完整行的情況下部分計算，因此 FlashAttention 使用**關聯分解**進行增量計算。對於拆分為區塊 \\(x = [x^{(1)}; x^{(2)}]\\) 的行，追蹤運行統計量：
   - 行最大值 \\(m_i = \max_j S_{ij}\\)，
   - 指數行和 \\(\ell_i = \sum_j \exp(S_{ij} - m_i)\\)。

   使用局部統計量 \\(\tilde{m}_t, \tilde{\ell}_t\\) 更新新區塊 \\(x^{(t)}\\)：
   \\[
   m_i^{\new} = \max(m_i, \tilde{m}_t), \quad \ell_i^{\new} = e^{m_i - m_i^{\new}} \ell_i + e^{\tilde{m}_t - m_i^{\new}} \tilde{\ell}_t.
   \\]
   部分 softmax 則為 \\(\tilde{P}_{ij} = \exp(S_{ij} - m_i^{\new})\\)，輸出累積為 \\(O_i \leftarrow \frac{\ell_i}{\ell_i^{\new}} e^{m_i - m_i^{\new}} O_i + \frac{\tilde{\ell}_t}{\ell_i^{\new}} e^{\tilde{m}_t - m_i^{\new}} \tilde{P}_{ij} V_j\\)。

   這種方法數值穩定（與融合 softmax 一致）且精確，可通過歸納法證明：在所有區塊處理完畢後，\\(O = \softmax(S) V\\)。

這些思想將**記憶體需求降低至 \\(O(N)\\)**（輸入 + 輸出 + \\(O(N)\\) 統計量如 \\(m, \ell\\)），並將** HBM 存取次數降低至 \\(O(N^2 d / M)\\)** — 次二次方，因為每個 \\(K/V\\) 元素僅讀取一次，而 \\(Q/O\\) 讀取次數為 \\(T_c \approx N d / M\\)。

### 前向傳播：逐區塊計算

前向傳播（論文中的算法 2 偽代碼）遍歷 \\(K, V\\) 的列區塊：

- 在 HBM 中初始化 \\(O = 0^{N \times d}\\)、\\(m = -\infty^N\\)、\\(\ell = 0^N\\)。
- 對於每個列區塊 \\(j = 1\\) 到 \\(T_c\\)：
  - 將 \\(K_j, V_j\\) 加載到 SRAM（在行之間重用）。
  - 對於每個行區塊 \\(i = 1\\) 到 \\(T_r\\)：
    - 將 \\(Q_i, O_i, m_i, \ell_i\\) 加載到 SRAM。
    - 計算局部 \\(S_{ij} = \tau Q_i K_j^T\\)（\\(B_r \times B_c\\)）。
    - 遮罩：\\(S_{ij}^{\masked} = \mask(S_{ij})\\)（例如，因果：下三角區域設為 \\(-\infty\\)）。
    - 局部 softmax 統計量：\\(\tilde{m}_{ij} = \rowmax(S_{ij}^{\masked})\\)、\\(\tilde{P}_{ij} = \exp(S_{ij}^{\masked} - \tilde{m}_{ij})\\)、\\(\tilde{\ell}_{ij} = \rowsum(\tilde{P}_{ij})\\)。
    - 使用上述公式更新全局統計量和輸出，並對 \\(\tilde{P}_{ij}\\) 應用 dropout。
    - 將更新後的 \\(O_i, m_i, \ell_i\\) 寫回 HBM。

這融合了所有操作：總 FLOP 仍為 \\(O(N^2 d)\\)，但 I/O 大幅下降（例如，比標準方法減少 9 倍存取次數）。對於因果注意力，遮罩成本低廉（向量化）。Dropout 使用共享的 RNG 狀態 \\(R\\)，該狀態會保存以供反向傳播使用。

### 反向傳播：通過重計算進行梯度計算

反向傳播（算法 4）較為複雜，因為梯度依賴於 \\(P\\)：

\\[
dP = dO \cdot V^T, \quad dS = P \odot (dP - \rowsum(dO \odot O)), \quad dQ = dS \cdot K, \quad dK = Q^T \cdot dS, \quad dV = P^T \cdot dO.
\\]

儲存 \\(P\\) 需要 \\(O(N^2)\\) 記憶體，因此 FlashAttention **即時重計算區塊**（選擇性重計算，類似於分塊檢查點）：

- 類似地遍歷：對於每個 \\(j\\)，加載 \\(K_j, V_j\\)；初始化局部 \\(dK_j, dV_j = 0\\)。
- 對於每個 \\(i\\)：使用保存的 \\(m_i, \ell_i\\) 重計算 \\(S_{ij}, P_{ij}\\)；從 \\(R\\) 重新生成 dropout 遮罩。
- 計算局部梯度：\\(dV_j += P_{ij}^{dropped^T} dO_i\\)、\\(dP_{ij} = dO_i V_j^T \odot Z_{ij}\\)（dropout 遮罩）、\\(dS_{ij} = P_{ij} \odot (dP_{ij} - D_i)\\)，其中 \\(D_i = \rowsum(dO_i \odot O_i)\\)。
- 累積 \\(dQ_i += \tau dS_{ij} K_j\\)、\\(dK_j += \tau Q_i^T dS_{ij}\\)。

這會使用額外的 \\(O(N^2 d)\\) FLOP，但僅需 \\(O(N)\\) 額外記憶體（無需儲存 \\(P\\)）。總計前向 + 反向：FLOP 約為標準的 2-3 倍，但由於 I/O 節省，速度快 2-4 倍。

### I/O 感知與 GPU 優化

GPU 具有層級結構：暫存器/SRAM（快速，容量小）>> HBM（緩慢，容量大）。標準注意力機制會因每次傳播的 \\(\Theta(N^2)\\) 次存取而導致 HBM 頻繁交換。FlashAttention 的分塊確保：
- \\(K, V\\) 僅加載一次（\\(O(N d)\\)）。
- \\(Q, O\\) 加載次數為 \\(T_c \approx N / B_c \approx N d / M\\)（\\(O(N^2 d / M)\\)）。
- 下限：對於中等範圍的 \\(M\\)，沒有任何精確算法能勝過 \\(\Omega(N^2 d^2 / M)\\)。

實證結果：在 A100 上，HBM 停頓主導運行時間；FlashAttention 將其減少 50-80%，達到計算瓶頸狀態。它支援區塊稀疏性（跳過零遮罩區塊）以獲得更大增益（比密集注意力快 2-4 倍）。

### 優勢：速度、記憶體與下游影響

- **記憶體**：線性 \\(O(N d)\\)，使單個 GPU 能夠處理 64k+ 序列（對比標準的 2k-4k）。例如，在 \\(N=65k\\) 時僅需 13 GB，而標準方法需要 200+ GB。
- **速度**：在 GPT/BERT 訓練中端到端快 2-4 倍；在原始注意力上快達 7 倍。例如，結合前向/反向傳播：在 \\(N=128\\) 時為 0.43 ms，在 \\(N=65k\\) 時為 9s（對比 PyTorch OOM）。
- **品質**：精確計算，因此沒有困惑度下降。支援更長上下文：在 GPT-2 上長度增加 4 倍時，困惑度提升 0.7 點；在長文檔任務上達到最先進水平（例如，在 64k 序列下 Path-256 得分為 63%）。
- **擴展**：FlashAttention-2（2023）增加更好的並行性（快達 2 倍）；FlashAttention-3（2024）使用異步/低精度於 H100（快 50%）。

### PyTorch 整合：無縫使用

PyTorch 2.0+ 通過 `torch.nn.functional.scaled_dot_product_attention(q, k, v)` 原生整合 FlashAttention，該函數在滿足條件時（例如，連續張量、支援的數據類型）自動調度到融合核心。無需自定義 CUDA：

```python
import torch
from torch.nn.functional import scaled_dot_product_attention

q, k, v = torch.randn(1, 8, 1024, 64, device='cuda')  # batch, heads, seq, dim
with torch.backends.cuda.sdp_kernel(enable_flash=True, enable_math=False):
    out = scaled_dot_product_attention(q, k, v, attn_mask=mask, dropout_p=0.1)
```

這處理遮罩/dropout；在不支援時回退到數學核心。對於自定義模型，它是手動注意力循環的即插即用替代方案，可立即獲得 2-3 倍速度提升。

FlashAttention 徹底改變了長上下文訓練，推動了如 Llama-2（4k→70B）等模型的發展。

[FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)  
[PyTorch 2.2: FlashAttention-v2 Integration](https://pytorch.org/blog/pytorch2-2/)  
[GitHub: Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)