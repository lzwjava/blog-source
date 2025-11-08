---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: RMSProp 及類似優化器詳解
translated: true
type: note
---

### 什麼是 RMSProp？

RMSProp（均方根傳播）是一種用於機器學習的自適應優化算法，通過梯度下降來訓練神經網絡。它通過維護平方梯度的移動平均值來標準化每個參數的學習率，從而解決梯度消失或爆炸的挑戰。這使其對於非平穩目標（如循環神經網絡 RNN 中的目標）特別有效。該算法由 Geoffrey Hinton 提出，是 Adagrad 的一種變體，使用指數衰減平均值而非累積所有過往梯度，防止學習率隨時間過度縮減。

### 與 RMSProp 相似的優化器

與 RMSProp「相似」的優化器通常是那些根據梯度歷史動態調整學習率的自適應方法。它們基於帶動量的梯度下降思想，但專注於每個參數的適應性，以處理稀疏或噪聲數據。以下是主要相似優化器的比較：

| 優化器 | 主要特點 | 與 RMSProp 的相似之處 | 與 RMSProp 的差異 |
|--------|----------|------------------------|-------------------|
| **Adagrad** | 累積平方梯度的總和以調整學習率；適合稀疏數據。 | 兩者都使用梯度幅度來調整每個參數的學習率。 | Adagrad 累積*所有*過往梯度，導致學習率單調遞減（通常過快）；RMSProp 使用移動平均值實現更穩定的適應。 |
| **Adadelta** | Adagrad 的擴展，使用梯度更新的移動窗口；無需手動調整學習率。 | 共享均方根（RMS）梯度標準化以實現自適應學習率。 | 引入了參數更新的單獨移動平均值（不僅僅是梯度），使其對初始化更穩健並降低超參數敏感性。 |
| **Adam**（自適應矩估計） | 結合動量（梯度的一階矩）與類似 RMSProp 的自適應（二階矩）；經過偏差校正以改善早期訓練。 | 與 RMSProp 一樣，使用平方梯度的指數衰減平均值進行每個參數的縮放。 | 添加動量項以加速收斂；包含偏差校正，在大型數據集上通常優於 RMSProp，但在某些情況下泛化能力稍差。 |
| **AdamW** | Adam 的變體，具有解耦權重衰減以進行正則化。 | 繼承 RMSProp 通過二階矩估計進行自適應縮放。 | 將權重衰減與自適應學習率分開，在微調 transformer 等任務中比標準 Adam（因此也比 RMSProp）具有更好的泛化能力。 |
| **SGD with Nesterov Momentum** | 基本隨機梯度下降，帶有「前瞻」動量以預測梯度。 | 在實踐中可以模擬自適應行為以實現更平滑的更新。 | 並非真正的自適應（固定學習率）；依賴動量進行加速而非每個參數的縮放，但通常比純自適應方法（如 RMSProp）泛化能力更好。 |

這些優化器通常在 PyTorch 或 TensorFlow 等框架中實現（例如 `torch.optim.RMSprop`）。對於大多數深度學習任務，可以從 RMSProp 或 Adam 開始，因為它們能很好地處理各種問題。對於稀疏數據，可以嘗試 Adagrad；對於 RNN/LSTM，RMSProp 或 Adam 表現出色。

### 參考資料
- [Understanding Deep Learning Optimizers: Momentum, AdaGrad, RMSProp & Adam](https://towardsdatascience.com/understanding-deep-learning-optimizers-momentum-adagrad-rmsprop-adam-e311e377e9c2)
- [Which Optimizer should I use for my ML Project?](https://www.lightly.ai/blog/which-optimizer-should-i-use-for-my-machine-learning-project)
- [A Comprehensive Guide on Deep Learning Optimizers](https://www.analyticsvidhya.com/blog/2021/10/a-comprehensive-guide-on-deep-learning-optimizers/)