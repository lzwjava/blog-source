---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 神經網絡的最大更新參數化
translated: true
type: note
---

### 什麼是 μP（最大更新參數化）？

μP，全稱為「最大更新參數化」，是由數學家兼 AI 研究員 Greg Yang（現任職於 xAI，先前在微軟研究院）開發的一種神經網絡參數化技術。該技術於其 2022 年發表的論文《Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer》中提出，它對深度學習模型的權重進行重新參數化，使其在訓練時更具可擴展性和效率。

#### 目的
μP 的核心目標是穩定不同模型規模下的超參數調校。在傳統設定（例如標準參數化，或稱 SP）中，每當你擴大模型規模（例如從數百萬參數擴展到數十億參數）時，由於梯度與更新變得不穩定（通常隨模型寬度或深度呈二次方縮放），學習率等超參數需要重新調整。μP 通過轉換參數來解決此問題，使得「最大更新」（即可能的最大梯度步長）在不同規模下保持一致。這實現了 **μTransfer**——一種工作流程，讓你能在微小的「代理」模型上調校超參數，並直接將其應用於龐大的目標模型，無需任何進一步調整。

#### 主要優勢
- **大幅節省成本**：在小型模型上進行調校成本低廉。例如，從一個 1300 萬參數的代理模型轉移超參數，其表現超越了已發表的 BERT-large（3.5 億參數）結果，且總調校成本僅相當於一次 BERT-large 的預訓練。對於 GPT-3（67 億參數），使用 4000 萬參數的代理模型進行轉移，僅以完整預訓練成本的 7% 就超越了基準結果。
- **大型模型的可擴展性**：適用於 Transformer 和 ResNet 等架構，非常適合訓練巨型神經網絡（例如 xAI 所使用的模型）。它確保了「規模不變的最優點」，意味著損失函數的景觀不會隨著模型增長而不可預測地扭曲。
- **易於使用**：可透過 PyTorch 函式庫使用（`pip install mup`），並已整合於大型 AI 模型的生產訓練流程中。

#### 簡要數學直觀
在 SP 中，權重的方差會不穩定地增長，導致梯度爆炸或消失。μP 對權重進行重新參數化（例如，對線性層按扇入進行縮放），以標準化 Fisher 信息矩陣，確保梯度流動保持平衡。這使得最佳超參數（如學習率）在不同規模下大致保持不變，避免了針對不同規模重新調校的需要。

μP 建立在 Yang 更廣泛的「Tensor Programs」框架之上，該框架用於理解神經網絡中的無限寬度/深度極限，並且它仍在持續發展——截至 2025 年的最新研究強調了其在超越單純超參數轉移的最大化特徵學習中的作用。

**參考文獻**  
- [Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer](https://arxiv.org/abs/2203.03466)  
- [The Practitioner's Guide to the Maximal Update Parameterization](https://www.cerebras.ai/blog/the-practitioners-guide-to-the-maximal-update-parameterization)  
- [How To Scale (Blog on μP and Scaling)](https://howtoscalenn.github.io/)  
- [Greg Yang's Professional Page](https://thegregyang.com/)