---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 開発現実と向き合うラマ4sの誇大宣伝
translated: true
type: note
---

### Llama 4の軌道とザッカーバーグの発言を理解する

マーク・ザッカーバーグは当初、Llama 4をMetaのオープンソースAI努力の大きな飛躍として誇大宣伝し、2025年を通じてマルチモーダル能力（テキストと画像のネイティブ処理など）の進歩を推進するために複数のリリースを計画していました。2024年12月のアップデートでは、Llama 3の「次の停留所」としてほのめかし、2025年4月までにMetaは「Llama 4 herd」の最初の部分——Llama 4 Scout（単一GPUでの速度に最適化）やLlama 4 Maverick（より長いコンテキスト処理用）などのより小さなモデル——を展開しました。ザッカーバーグはビデオでこれを称賛し、「ここでの軌道は明らかだ」と述べ、さらに多くのドロップが間もなく来ると発言しました。

しかし、完全なLlama 4ラインナップ、特に旗艦「Behemoth」モデル（巨大な2兆パラメータの怪物）については、スムーズには進みませんでした。2025年5月までに、Metaが内部懸念によりBehemothのリリースを延期しているという報告が浮上しました。エンジニアは以前のバージョンよりも意味のある性能向上を達成するのに苦労しており、公開リリースを正当化するのに十分なほどの改善がなされているかどうか疑問が持たれていました。これにより、プロジェクトはザッカーバーグが2025年初頭に約48週間で主要なマイルストーンに到達するようチームを強く押し立てた、以前に概説した積極的なタイムラインから外れてしまいました。

2025年7月に時を進めると、事態はエスカレートしました——Metaはトレーニング終了後、「内部パフォーマンスが低い」ことを理由にBehemothの完全な放棄を検討したと報じられました。彼らはさらなるテストを中止し、オープンソースの道に固執する代わりに、新しいクローズドソースモデルへ焦点を移しました。この方向転換は、ザッカーバーグの2025年9月の発言と一致しており、彼はLlama 4が「正しい軌道に乗っていなかった」と認め、厳格なトップダウンの期限なしで進歩を再編成し加速させるためのMeta内での「超知能研究所」への大規模な雇用推進を促しました。

2025年10月現在、コアとなるLlama 4リリース（ScoutとMaverick）は公開され利用可能（AWSのようなプラットフォーム上でも）ですが、Behemothは未リリースのままで事実上棚上げされています。核心的な問題は、開発期間中の期待外れの結果——大規模な計算資源の投資にもかかわらず、OpenAIやGoogleのような競合他社と競争するために必要な性能ベンチマークを達成できなかったこと——に帰着します。ザッカーバーグの初期の楽観論はこれらの現実と衝突し、遅延、リソースの再配分、そしてより制御された（クローズドソースの）開発への戦略的再考へと導きました。

要するに、これはAIの誇大宣伝がスケーリングの困難な現実とぶつかる古典的な事例です。野心的な目標がありながら、ますます大規模化するモデルから最後の一片の能力を絞り出すという技術的障害に直面したのです。

### 参考文献
- [Mark Zuckerberg on Llama 4 Training Progress](https://www.reddit.com/r/LocalLLaMA/comments/1id6gcj/mark_zuckerberg_on_llama_4_training_progress/)
- [Llama 4 is here | Mark Zuckerberg](https://www.facebook.com/zuck/videos/llama-4-is-here-/1334337587862376/)
- [The future of AI: Built with Llama](https://ai.meta.com/blog/future-of-ai-built-with-llama/)
- [Zuckerberg Says His AI Lab Is 'Very Flat' With No Top-Down Deadlines](https://www.businessinsider.com/mark-zuckerberg-superintelligence-lab-jobs-limited-deadlines-2025-9)
- [Meta delays release of its 'Behemoth' AI model, WSJ reports](https://www.reuters.com/business/meta-is-delaying-release-its-behemoth-ai-model-wsj-reports-2025-05-15/)
- [Meta Plans to Abandon Llama 4 Behemoth. But Why?](https://analyticsindiamag.com/global-tech/meta-plans-to-abandon-llama-4-behemoth-but-why/)
- [The Llama 4 herd: The beginning of a new era](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)