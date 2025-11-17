---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: NanoGPT 初始化與啟動詳情
translated: true
type: note
---

在 Andrej Karpathy 的 **NanoGPT**（2022 年底至 2025 年間流行的極簡 GPT 實現）中，模型**並未**使用 ReLU。它採用 **GELU**（高斯誤差線性單元）作為激活函數，這是現代 GPT 風格模型（與 GPT-2、GPT-3、Llama 等相同）的標準選擇。

### NanoGPT 關鍵參數初始化範圍（截至 2025 年最新版本）

| 參數 / 組件          | 初始化方法                          | 典型尺度 / 範圍                               | 備註 |
|--------------------------------|------------------------------------------------|-----------------------------------------------------|-------|
| 嵌入層（詞符 + 位置） | `nn.Embedding` → 正態分佈         | 標準差 = 0.02                                          | 極小值以保持初始 logits 較小 |
| FFN 中的線性層（投影）    | `nn.Linear` → 默認 PyTorch 初始化 → 然後縮放 | 權重：縮放後標準差 ≈ 0.02–0.03               | Karpathy 在某些配置中應用 `0.02 / sqrt(n_embd)` 或類似的縮放因子 |
| 最終 LM 頭部（輸出投影） | 與嵌入層相同（權重綁定）             | 標準差 = 0.02                                          | 與詞符嵌入權重綁定 |
| LayerNorm 偏置                  | 零值                                          | 0                                                   | 標準做法 |
| LayerNorm 權重                | 單位值                                           | 1.0                                                 | 標準做法 |
| 殘差縮放（初始化後）    | 權重乘以小因子           | 通常為 `權重 *= 0.02` 或 `權重 *= sqrt(2/n_layers)` | 在初始化時穩定訓練的關鍵技巧 |
| 注意力 QKV 投影        | 按上述方式縮放                                | 有效標準差 ≈ 0.02                                | 與其他線性層縮放相同 |
| 注意力輸出投影    | 額外縮放：`cproj.weight *= 0.02` 或類似 | 更小（以補償殘差路徑）     | 對深層模型非常重要 |

### NanoGPT 中的特殊初始化技巧
在 `model.py` 中，創建每個 `nn.Linear` 層後，Karpathy 會執行類似這樣的操作（具體值取決於配置）：

```python
if isinstance(m, nn.Linear):
    torch.nn.init.normal_(m.weight, mean=0.0, std=0.02)
    if m.bias is not None:
        torch.nn.init.zeros_(m.bias)
    # 對深層網絡重要的殘差縮放
    if "cproj" in name:          # 注意力或 FFN 的輸出投影
        m.weight.data *= 0.02    # 或有時 *= 1/sqrt(n_layer)
```

或在較新版本（2024–2025 年）中，他使用配置驅動的縮放：

```python
std = 0.02 / math.sqrt(2 * n_layer)   # 有助於深層模型
```

這確保了殘差流的方差不會隨著深度增加而爆炸或消失。

### 總結：NanoGPT 未使用 ReLU
- 激活函數：**GELU**（非 ReLU）
- 主要初始化標準差：**~0.02**
- 輸出投影的額外縮放：**0.02 或更小**（尤其重要）
- 除 LayerNorm 外，大多數線性層無偏置

這種極小的初始化 + 殘差縮放是 NanoGPT 即使在最小配置中無需學習率熱身也能穩定訓練的原因。

如果您從頭開始訓練自己的 NanoGPT，請複製這些確切的初始化技巧 — 它們的重要性超乎許多人的想像！