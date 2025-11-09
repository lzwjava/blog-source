---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 神經語言模型的縮放定律
translated: true
type: note
---

### 概述
OpenAI 的 Jared Kaplan 與研究團隊（包括 Sam McCandlish、Tom Henighan、Tom B. Brown、Benjamin Mann、Prafulla Dhariwal、Andrew Radford 及 Ilya Sutskever）於 2020 年發表的論文《Scaling Laws for Neural Language Models》，探討了大型神經語言模型的效能（以交叉熵損失衡量）如何隨關鍵訓練資源擴展。透過對基於 Transformer 的模型進行大量實驗，他們發現了可預測的冪律關係，這些關係在橫跨超過七個數量級的模型規模、數據集和計算預算中均成立。這些「擴展定律」為優化訓練效率及預測效能提供了框架，無需反覆試驗。

### 擴展定律的核心發現
核心洞見是損失函數 \\( L \\) 隨三個變量呈冪律下降：
- **模型規模（\\( N \\)，參數量）**：\\( L(N) \propto N^{-\alpha} \\)，其中 \\( \alpha \approx 0.076 \\)（針對語言建模）。較大模型初期學習更快，但整體訓練速度較慢。
- **數據集規模（\\( D \\)，詞元數量）**：\\( L(D) \propto D^{-\beta} \\)，其中 \\( \beta \approx 0.103 \\)。更多數據持續降低損失，但隨 \\( D \\) 增長，收益遞減。
- **計算量（\\( C \\)，浮點運算次數）**：\\( L(C) \propto C^{-\gamma} \\)，其中 \\( \gamma \approx 0.050 \\)。此定律結合了 \\( N \\) 與 \\( D \\) 的影響，因典型訓練中 \\( C \approx 6ND \\)。

這些定律雖屬經驗性，但在不同架構（例如寬度與深度影響甚微）與任務中表現出驚人一致性。其他觀察包括：
- **樣本效率**：較大模型的數據效率遠更高——例如，規模大 100 倍的模型僅需約 10 倍更少數據即可達到相同損失。
- **過擬合**：可根據 \\( N/D \\) 比率預測；當 \\( N \\) 超過 \\( D \\) 一定倍數時出現，遵循 \\( L_{\text{測試}} - L_{\text{訓練}} \propto (N/D)^\kappa \\)。
- **最優分配**：在固定計算預算下，最佳策略是訓練*極大規模*模型並使用*適量*數據，提前停止（未完全收斂）以避免收益遞減。

### 理論與實踐意義
論文指出這些定律源於神經網絡的基本特性，例如來自噪聲或不可降低困惑度的不可約損失底線。它們挑戰了「數據越大越好」的直覺，轉而主張透過巨型模型從有限計算中榨取更多效能。這深刻影響了現代 AI 發展，透過預測擴展能可靠帶來突破，為如 GPT-3 等巨型模型的投入提供了依據。

總之，論文主張「計算最優」路徑：優先考慮模型規模，使用剛足夠的高質量數據，並高效訓練——為 LLM 的擴展時代鋪平道路。

[Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)