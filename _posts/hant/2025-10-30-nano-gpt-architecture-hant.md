---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: NanoGPT 模型架構概要
translated: true
type: note
---

### NanoGPT 模型架構概覽

NanoGPT 在 PyTorch 中實現了一個類似 GPT-2 的僅解碼器 Transformer 模型。其架構定義於 `model.py` 檔案中，並透過可配置的 `GPTConfig` 來設定超參數。預設配置（例如對應 "gpt2" 變體）使用：

- **Transformer 區塊數量**：12 (`n_layer = 12`)
- **嵌入維度（層大小）**：768 (`n_embd = 768`)
- **注意力頭數量**：12 (`n_head = 12`)
- **MLP 中間層大小**：3072 (`n_embd * 4`，擴展因子為 4)

每個 Transformer 區塊（類別 `Block`）是一個標準的解碼器區塊，包含殘差連接與層標準化。它包含：
- **LayerNorm 1** (`ln1`)：應用於自注意力機制之前。
- **多頭自注意力機制** (`attn`)：因果（遮罩）注意力，防止查看未來資訊。
- 注意力機制後的殘差加法。
- **LayerNorm 2** (`ln2`)：應用於 MLP 之前。
- **MLP** (`mlp`)：一個簡單的前饋神經網路。
- MLP 後的殘差加法。

整體模型（類別 `GPT`）在詞彙標記嵌入與位置嵌入之後堆疊了這 12 個區塊，最後接一個 LayerNorm (`ln_f`) 以及一個線性投影層以輸出詞彙表大小的維度。

#### MLP 結構
MLP（`Block` 內的類別 `MLP`）是一個兩層的前饋神經網路：
- 第一層線性層 (`c_fc`)：從 `n_embd` (768) 投影至中間層大小 (3072)。
- GELU 激活函數：在第一層投影後進行元素級別的應用。
- 第二層線性層 (`c_proj`)：從 3072 投影回 `n_embd` (768)。

這遵循您提到的 "全連接層 -> gelu -> 投影層" 模式。

#### 前向傳播流程
前向傳播採用殘差風格，並使用前置層標準化（在子層之前進行 LayerNorm）。以下是高層次的流程分解：

1. **主要前向傳播 (GPT.forward)**：
   - 詞彙標記嵌入：輸入標記（形狀 `[B, T]`）→ 嵌入向量（形狀 `[B, T, n_embd]`）。
   - 位置嵌入：與詞彙標記嵌入相加。
   - 通過堆疊的 `n_layer` (12) 個 Transformer 區塊：對每個區塊執行 `x = block(x)`。
   - 最終 LayerNorm：`x = self.ln_f(x)`。
   - 線性投影：`logits = self.lm_head(x)` → 輸出形狀 `[B, T, vocab_size]`。

   程式碼片段（簡化）：
   ```python
   def forward(self, idx, targets=None):
       # ... 嵌入 + 位置
       for block in self.blocks:
           x = block(x)
       x = self.ln_head(x)
       logits = self.head(x)
       # ... 若有目標則計算損失
       return logits
   ```

2. **Transformer 區塊內的前向傳播 (Block.forward)**：
   - 對輸入 `x` 應用 `ln1`。
   - 自注意力機制：`x = x + attn(ln1(x))`（殘差連接）。
   - 對結果應用 `ln2`。
   - MLP：`x = x + mlp(ln2(x))`（殘差連接）。

   程式碼片段（簡化）：
   ```python
   def forward(self, x):
       x = x + self.attn(self.ln1(x))
       x = x + self.mlp(self.ln2(x))
       return x
   ```

3. **自注意力機制內的前向傳播 (MultiheadAttention.forward)**：
   - 對 LayerNorm 後的輸入 → 計算 Q、K、V 投影（線性層 `c_attn`）。
   - 分割成多個頭，應用因果遮罩，進行縮放點積注意力運算。
   - 合併多個頭，透過 `c_proj` 投影回來。
   - 殘差加法（在區塊外部進行）。

   關鍵點：因果遮罩確保忽略未來標記。輸出形狀保持為 `[B, T, n_embd]`。

   程式碼片段（核心注意力計算，簡化）：
   ```python
   def forward(self, x):
       B, T, C = x.shape
       qkv = self.c_attn(x).split(self.n_embd, dim=2)  # Q,K,V
       # ... 重塑為多頭，應用遮罩，attn = q @ k.transpose / sqrt
       # attn = attn.masked_fill(mask == 0, -1e9)
       # y = attn @ v
       # ... 合併並投影
       return self.c_proj(y.reshape(B, T, C))
   ```

4. **MLP 內的前向傳播 (MLP.forward)**：
   - 第一層投影：`x = self.c_fc(x)` → 轉換至中間層大小。
   - GELU：`x = F.gelu(x)`。
   - 第二層投影：`x = self.c_proj(x)` → 轉換回 `n_embd`。

   程式碼片段：
   ```python
   def forward(self, x):
       x = self.c_fc(x)
       x = F.gelu(x)
       x = self.c_proj(x)
       return x
   ```

此設定緊密遵循 GPT-2 的架構，在預設配置下約有 1.24 億個參數。如需確切程式碼，請查閱程式庫。

[model.py 原始碼](https://github.com/karpathy/nanoGPT/blob/master/model.py)