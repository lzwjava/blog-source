---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 視覺變換器作者與貢獻
translated: true
type: note
---

### 《一張影像價值 16x16 個詞語：大規模影像識別的 Transformer 模型》作者簡介

2020 年由 Alexey Dosovitskiy 與 Google 團隊發表的開創性論文《一張影像價值 16x16 個詞語：大規模影像識別的 Transformer 模型》，標誌著電腦視覺領域的關鍵轉折。該論文提出了 Vision Transformer（ViT）模型，將原本為自然語言處理設計的 transformer 架構直接應用於影像區塊，在大型數據集（如 JFT-300M）上進行預訓練後，於 ImageNet 等大規模數據集實現了最先進的性能。這項工作證明在足夠的運算資源與數據支持下，純 transformer 模型能在效率與準確度上超越卷積神經網絡（CNN），對後續多模態 AI 與可擴展視覺模型的發展產生深遠影響。

本論文由 12 位研究人員共同完成，主要來自 Google Brain 蘇黎世團隊，融合了深度學習、序列建模與大規模訓練的專業知識。以下概述主要作者背景及其對領域的貢獻。（為簡潔起見，僅聚焦核心貢獻者；完整作者名單包含 Dirk Weissenborn、Thomas Unterthiner、Mostafa Dehghani、Matthias Minderer、Georg Heigold、Sylvain Gelly 與 Jakob Uszkoreit——均為 Google 校友，在 transformer、優化與視覺語言整合領域有深厚根基。）

#### 核心作者與背景

- **Alexey Dosovitskiy**（主要作者）：作為 ViT 的推動者，Dosovitskiy 提出了將影像視為區塊序列的核心概念。他擁有莫斯科國立大學數學碩士與博士學位，並於弗萊堡大學從事博士後研究，專注無監督特徵學習。2019 年加入 Google Brain 後主導 ViT 開發，於 2021 年轉赴柏林 AI 新創公司 Inceptive。其研究涵蓋電腦視覺、生成模型與生物啟發機器學習，論文引用數超過 136,000 次。

- **Lucas Beyer**：Beyer 在 ViT 的實作、基準評估與效率優化方面扮演關鍵角色。這位比利時籍研究者於亞琛工業大學攻讀機械工程，2018 年獲機器人學與 AI 博士學位，專注遊戲 AI 與強化學習。博士畢業後加入 Google Brain 蘇黎世團隊，晉升為 Google DeepMind 主任研究科學家。2025 年獲 Meta 延攬為頂尖 AI 人才，持續投入視覺 transformer 與數據中心機器學習研究。

- **Alexander Kolesnikov**：Kolesnikov 貢獻於 ViT 的擴展實驗與遷移學習分析，著重其中型數據集的表現。他取得莫斯科國立大學數學碩士學位，並於奧地利科學技術研究所（ISTA）獲機器學習與電腦視覺博士學位。2018 年加入 Google Brain，晉升 DeepMind 資深研究員後轉赴 OpenAI，於 2025 年受 Meta 挖角，憑藉其高效視覺模型專業獲得重用。

- **Xiaohua Zhai**：Zhai 聚焦 ViT 的預訓練策略與多模態擴展，運用其表徵學習領域的深厚積累。他擁有北京大學電子工程博士學位，2015 年以軟體工程師身份加入 Google，2017 年轉任 Google Brain 研究員，2023 年進入 DeepMind。現為 Meta 研究員（經 2025 年 OpenAI 蘇黎世分部轉職），其研究成果串聯視覺、語言與自監督學習，論文引用數逾 100,000 次。

- **Neil Houlsby**（資深作者）：作為團隊領導，Houlsby 統籌 ViT 的架構設計與視覺擴展律的影響。他曾獲 Google 歐洲博士獎學金，完成機器學習博士學位。自實習期便長期任職 Google，於 Google Brain 與 DeepMind 領導神經架構與視覺語言模型團隊。2025 年加入 Anthropic 主持新設蘇黎世辦公室，專注 AI 安全擴展研究。

這支以蘇黎世為基地的 Google Brain 團隊，運用鄰近 TPU 資源進行大規模實驗——累計超過 25,000 TPU-日——證實 transformer 在文字領域外的應用潛力。多位作者其後轉赴 Meta、OpenAI 與 Anthropic 等頂尖 AI 實驗室，彰顯 ViT 對領域的持續影響力。

#### 參考資料
- [《一張影像價值 16x16 個詞語：大規模影像識別的 Transformer 模型》（arXiv）](https://arxiv.org/abs/2010.11929)
- [Alexey Dosovitskiy Google Scholar 檔案](https://scholar.google.com/citations?user=FXNJRDoAAAAJ)
- [Lucas Beyer Google Scholar 檔案](https://scholar.google.com/citations?user=p2gwhK4AAAAJ)
- [Alexander Kolesnikov Google Scholar 檔案](https://scholar.google.com/citations?user=H9I0CVwAAAAJ)
- [Xiaohua Zhai Google Scholar 檔案](https://scholar.google.com/citations?user=8gruapYAAAAJ)
- [Neil Houlsby Google Scholar 檔案](https://scholar.google.com/citations?user=sm1-TZMAAAAJ)
- [從博士繞道到 Meta 頂尖 AI 人才：Lucas Beyer（印度時報）](https://timesofindia.indiatimes.com/education/news/lucas-beyer-educational-qualification-from-ph-d-detour-and-google-rejection-to-becoming-metas-top-ai-hire/articleshow/122158414.cms)
- [祖克柏從 OpenAI 挖角 Alexander Kolesnikov（印度時報）](https://timesofindia.indiatimes.com/education/news/zuckerberg-poached-alexander-kolesnikov-from-sam-altmans-openai-where-did-this-ai-genius-study/articleshow/122158654.cms)
- [Anthropic 從 Google DeepMind 挖角 Neil Houlsby（歐洲新聞）](https://www.euronews.com/next/2025/02/13/anthropic-poaches-google-deepmind-talent-to-lead-new-european-office)