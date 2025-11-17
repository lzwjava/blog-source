---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GPTモデル訓練における重み減衰
translated: true
type: note
---

Weight decayは、GPTモデル（およびほぼすべての大規模言語モデル）の訓練時に過学習を防ぎ汎化性能を向上させるために使用される一般的な正則化手法です。

### 実際の動作
Weight decayは、モデルの重みを小さな値に向けて押しやるペナルティ項を損失関数に追加します。数学的には、元の損失がℒ（例：交差エントロピー）である場合、weight decayを使用すると以下を最適化します：

ℒ_合計 = ℒ + (λ / 2) × ||w||²

ここで：
- w はモデルパラメータ（重み）
- ||w||² は重みのL2ノルムの二乗
- λ (ラムダ) はweight decay係数（GPTスタイルの訓練では通常 0.01 ~ 0.1）

この追加項により、元の損失を大幅に減少させない限り、モデルが非常に大きな重みを学習することが抑制されます。

### 実際の実装方法 (AdamW)
ほとんどのGPT訓練（OpenAIのGPT-2、GPT-3、LLaMA、Mistralなど）では、標準的なL2正則化を伴う素のAdamは使用されません。代わりにAdamW（分離されたweight decayを備えたAdam）が使用されます。

主な違い：
- Adamにおける標準的なL2正則化は、ペナルティを勾配に直接追加します。
- AdamWはそれを分離します：weight decayを別個の更新ステップとして適用し、Adamのような適応型オプティマイザでより良く機能します。

したがって、訓練設定で以下のような記述を目にした場合：

```python
optimizer = AdamW(model.parameters(), lr=5e-5, weight_decay=0.1)
```

この0.1は上記のλであり、正しく分離されたバージョンが使用されています。

### 実際のGPTスタイルモデルにおける典型的な値

| モデル / 論文           | Weight Decay | 注記                                    |
|-------------------------|--------------|-----------------------------------------|
| GPT-2 (OpenAI)          | 0.01         |                                         |
| GPT-3 (OpenAI)          | 0.1          | Brown et al. 2020                       |
| LLaMA 1 & 2 (Meta)      | 0.1          | ノルム/バイアスへの適用除外と組み合わせることが多い |
| PaLM (Google)           | 0.1          |                                         |
| Grok-1 (xAI)            | 0.1          | 公開リリース設定より                    |
| Mistral / Mixtral       | 0.1          |                                         |

### 重要なニュアンス: どのパラメータにweight decayを適用するか？
現代的な実践（LLaMA以降）では、weight decayを特定の層にのみ適用します：
- 適用する: Linear層（重み行列）、埋め込み行列
- 適用しない: バイアス項、LayerNormの重み、任意の1次元パラメータ

これは通常、PyTorchのパラメータグループを使用して行われます：

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

### GPT規模のモデルにおいて重要な理由
数十億または数百億のパラメータ規模では、モデルは訓練データを容易に記憶してしまいます。Weight decayは、ドロップアウト、確率的深度などと並んで、実効的な容量を抑制し、下流タスクの性能を向上させる最もシンプルで効果的なツールの一つです。

要約すると：weight decay ≈ L2正則化ですが、AdamWを介して適切に実装され、選択的に適用されることで、事実上すべての現代的なGPTスタイルの事前学習レシピにおける標準的な要素となっています。