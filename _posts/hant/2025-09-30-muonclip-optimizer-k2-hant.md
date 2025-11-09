---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: MuonClip 優化器 for Kimi K2
translated: true
type: note
---

### Muon Optimizer 概述

Muon Optimizer 是一種尖端優化算法，由 Moonshot AI 創始人兼 CEO 楊植麟在開發其大型語言模型 Kimi K2 的背景下提及[1][2][3]。它是一種受二階方法啟發的優化器，在模型訓練期間使用高秩更新來更好地適應損失曲面的幾何形狀[2]。然而，它存在訓練不穩定的問題，Moonshot AI 為此創建了名為 MuonClip 的增強版本來解決[1][4]。

### 主要特點
- **效率與設計**：Muon 旨在實現 Token 效率，這意味著它比傳統優化器（如 AdamW）處理更少的 Token，同時實現相當或更好的性能。它從二階方法（例如牛頓法）中汲取靈感，但適應了大規模深度學習場景[2][3]。
- **穩定性問題**：基礎 Muon 優化器在長時間訓練運行中可能導致不穩定，例如損失峰值，因為它在某些條件下容易發散[2][1]。
- **MuonClip 增強功能**：Moonshot AI 通過將 Muon 與「QK-Clip」技術相結合，引入了 MuonClip，該技術對注意力機制中的查詢-鍵交互進行裁剪以防止不穩定。這使得 Kimi K2 能夠在 15.5 萬億 Token 上進行穩定、無峰值的訓練[1][4][5]。

### 在 Kimi K2 中的應用
MuonClip 在預訓練 Kimi K2（一個總參數達 1 萬億的專家混合模型，激活參數為 320 億）中起到了關鍵作用。該優化器使 Moonshot AI 能夠在 Tau2-Bench (66.1)、ACEBench (76.5) 和 SWE-Bench Verified (65.8) 等基準測試中取得最先進的結果，而無需延長思考時間[4][6]。楊植麟強調這是開源 AI 發展的一個突破，強調了其在使大規模訓練更高效和穩定方面的作用[7][8]。

有關技術細節，請參閱 arXiv 上的 Kimi K2 論文[1][4]。楊植麟在 2025 年 7 月模型發布的訪談和公告中討論了這一點[2][7]。

引用文獻：
[1] https://arxiv.org/pdf/2507.20534?
[2] https://artificialintelligencemadesimple.substack.com/p/kimi-k2-is-the-most-important-model?utm_source=post-email-title&publication_id=1315074&post_id=169438943&utm_campaign=email-post-title&isFreemail=true&r=36rt3&triedRedirect=true&utm_medium=email
[3] https://composio.dev/blog/notes-on-kimi-k2
[4] https://arxiv.org/abs/2507.20534
[5] https://www.hpcwire.com/2025/07/16/chinas-moonshot-ai-releases-trillion-parameter-model-kimi-k2/
[6] https://intuitionlabs.ai/pdfs/analysis-of-the-kimi-k2-open-weight-language-model.pdf
[7] https://www.chinatalk.media/p/kimi-k2-the-open-source-way
[8] https://github.com/MoonshotAI/Kimi-K2