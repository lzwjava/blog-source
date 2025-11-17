---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GPT 模型訓練中的權重衰減
translated: true
type: note
---

權重衰減是一種常用的正則化技術，在訓練 GPT 模型（以及幾乎所有大型語言模型）時使用，以防止過度擬合並提升泛化能力。

### 實際作用原理
權重衰減在損失函數中加入懲罰項，迫使模型權重趨向較小值。數學上，若原始損失為 ℒ（例如交叉熵），加入權重衰減後將優化：

ℒ_總和 = ℒ + (λ / 2) × ||w||²

其中：
- w 代表模型參數（權重）
- ||w||² 是權重的平方 L2 範數
- λ (lambda) 是權重衰減係數（在 GPT 風格訓練中通常為 0.01 ~ 0.1）

這項附加條款會抑制模型學習過大的權重，除非這些權重能顯著降低原始損失。

### 實際實現方式 (AdamW)
在多數 GPT 訓練過程（如 OpenAI 的 GPT-2、GPT-3、LLaMA、Mistral 等）中，人們並不使用標準 L2 正則化的普通 Adam，而是採用 AdamW（具解耦權重衰減的 Adam）。

關鍵差異：
- 標準 Adam 中的 L2 正則化會直接將懲罰項加入梯度
- AdamW 將其解耦：以獨立更新步驟應用權重衰減，這能與 Adam 等自適應優化器更好地配合

當在訓練配置中看到如下代碼時：

```python
optimizer = AdamW(model.parameters(), lr=5e-5, weight_decay=0.1)
```

其中的 0.1 即為前述的 λ 值，且採用的是正確的解耦版本。

### 真實 GPT 風格模型中的典型數值

| 模型 / 論文           | 權重衰減值 | 備註說明                                |
|----------------------|------------|----------------------------------------|
| GPT-2 (OpenAI)       | 0.01       |                                        |
| GPT-3 (OpenAI)       | 0.1        | Brown 等人 2020 年論文                 |
| LLaMA 1 & 2 (Meta)   | 0.1        | 常與規範化層/偏置項無衰減結合使用       |
| PaLM (Google)        | 0.1        |                                        |
| Grok-1 (xAI)         | 0.1        | 根據公開版本配置                        |
| Mistral / Mixtral    | 0.1        |                                        |

### 重要細節：哪些參數需應用權重衰減？
現代實踐（自 LLaMA 起）僅對特定層應用權重衰減：
- 需應用：線性層（權重矩陣）、嵌入矩陣
- 不應用：偏置項、LayerNorm 權重、所有一維參數

通常透過 PyTorch 參數分組實現：

```python
decay = set()
no_decay = set()
for name, param in model.named_parameters():
    if "bias" in name or "layer_norm" in name or param.ndim == 1:
        no_decay.add(param)
    else:
        decay.add(param)

optimizer = AdamW([
    {"params": list(decay),   "weight_decay": 0.1},
    {"params": list(no_decay), "weight_decay": 0.0}
], lr=...)
```

### 對 GPT 級別模型的重要性
當參數規模達數十億甚至數千億時，模型極易記憶訓練數據。權重衰減是最簡潔有效的工具之一（與 dropout、隨機深度等技術並列），能有效控制模型實際容量並提升下游任務表現。

簡而言之：權重衰減 ≈ L2 正則化，但透過 AdamW 正確實現並選擇性應用，已成為所有現代 GPT 風格預訓練方案中的標準組件。