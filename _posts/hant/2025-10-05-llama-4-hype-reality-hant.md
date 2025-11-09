---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Llama 4s 熱潮與開發現實
translated: true
type: note
---

### 理解 Llama 4 發展軌跡與朱克伯格的評論

馬克·朱克伯格最初將 Llama 4 宣傳為 Meta 開源 AI 工作的重大飛躍，計劃在 2025 年全年發布多個版本，以推動多模態能力（如原生處理文字和圖像）的進展。在 2024 年 12 月的更新中，他預告這將是 Llama 3 之後的「下一站」；到了 2025 年 4 月，Meta 推出了「Llama 4 系列」的首批模型——包括較小型的模型，如針對單一 GPU 速度優化的 Llama 4 Scout，以及用於處理更長上下文的 Llama 4 Maverick。朱克伯格在一段影片中慶祝這一進展，稱「發展軌跡非常清晰」，並表示更多模型即將發布。

然而，完整的 Llama 4 系列並未如預期順利推進，尤其是旗艦模型「Behemoth」（一個擁有 2 萬億參數的龐然大物）。截至 2025 年 5 月，有報導稱 Meta 因內部疑慮而推遲了 Behemoth 的發布：工程師們難以在性能上實現相較前代版本的顯著提升，且團隊對改進幅度是否足以支撐公開發布存有疑慮。這使得項目偏離了朱克伯格早前制定的激進時間表——他在 2025 年初曾強力推動團隊在約 48 週內達成關鍵里程碑。

時間推進到 2025 年 7 月，情況進一步升級——據報導，Meta 在完成訓練後考慮完全放棄 Behemoth，理由是「內部表現不佳」。他們停止了進一步測試，並將重心轉向新的閉源模型，而非堅持開源路線。這一轉變與朱克伯格在 2025 年 9 月的評論相符，他承認 Llama 4「未處於正確的發展軌道上」，並促使 Meta 大力招聘組建「超智慧實驗室」，以重新整合資源、加速進展，同時避免僵化的自上而下 deadline。

截至 2025 年 10 月，Llama 4 核心版本（Scout 和 Maverick）已發布並可公開使用（甚至在 AWS 等平台上線），但 Behemoth 仍未被發布，實際上已被擱置。核心問題歸結於開發期間的未達預期成果——儘管投入了巨大的計算資源，但未能達到與 OpenAI 或 Google 等競爭對手抗衡所需的性能基準。朱克伯格早期的樂觀與這些現實情況產生衝突，最終導致延遲、資源重新分配，以及策略上轉向更受控的閉源開發。

簡而言之，這是 AI 炒作遇上規模化難題的典型案例：目標遠大，但從日益龐大的模型中榨取最後一點能力時，卻遭遇了技術瓶頸。

### 參考資料
- [馬克·朱克伯格談 Llama 4 訓練進展](https://www.reddit.com/r/LocalLLaMA/comments/1id6gcj/mark_zuckerberg_on_llama_4_training_progress/)
- [Llama 4 正式登場 | 馬克·朱克伯格](https://www.facebook.com/zuck/videos/llama-4-is-here-/1334337587862376/)
- [AI 的未來：基於 Llama 構建](https://ai.meta.com/blog/future-of-ai-built-with-llama/)
- [朱克伯格稱其 AI 實驗室「非常扁平化」且無自上而下的截止期限](https://www.businessinsider.com/mark-zuckerberg-superintelligence-lab-jobs-limited-deadlines-2025-9)
- [據《華爾街日報》報導，Meta 推遲發布「Behemoth」AI 模型](https://www.reuters.com/business/meta-is-delaying-release-its-behemoth-ai-model-wsj-reports-2025-05-15/)
- [Meta 計劃放棄 Llama 4 Behemoth，原因為何？](https://analyticsindiamag.com/global-tech/meta-plans-to-abandon-llama-4-behemoth-but-why/)
- [Llama 4 系列：新時代的開端](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)