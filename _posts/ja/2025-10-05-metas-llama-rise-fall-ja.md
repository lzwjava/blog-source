---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: メタのリャマの台頭と凋落
translated: true
type: note
---

### MetaのLlamaの旅：2023年の躍進から2025年の苦闘へ

2023年、MetaはLlama 1と2でAIシーンに登場し、これらはフロンティアモデルとして称られました。オープンソースの代替手段でありながら、GPT-3.5のようなクローズドシステムと同等の能力を持ち、大規模な開発者コミュニティを育成しました。この動きにより、MetaはAIの民主化をリードする存在としての地位を確立し、人材と投資を集めました。しかし、2025年までに、LlamaはGoogle（Gemini）、OpenAI（GPTシリーズ）、さらにはMistralやDeepSeekのようなより機敏なオープンソースのプレイヤーにも後れを取るようになりました。この遅れは、内部の失敗、外部からの圧力、そして初期の勢いを損なった戦略的転換が混在した結果です。

#### 1. **大規模な人材流出**
2023年の研究論文にクレジットされたMetaのオリジナルのLlamaチームは、壊滅的な打撃を受けました。14人の主要な著者のうち、2025年半ばまでに残っていたのは3人だけで、11人が2年間で離脱しました。その多くは、Mistral AI（元Meta研究者のGuillaume LampleとTimothée Lacroixが共同設立）のような競合他社を設立したり、参加したりしました。この流出（離脱者1人あたり平均5年以上在籍）により、スケーリングとイノベーションのための専門知識に空白が生じました。内部関係者は、攻撃的な締め切り、内部政治、そしてより多くの自律性とリソースを提供するスタートアップや大手テクノロジー企業でのより良い機会を理由に、バーンアウトを指摘しています。

#### 2. **開発障害と拙速なリリース**
初期のLlamaの生誕地であるMetaのFundamental AI Research（FAIR）ラボから、製品中心のGenAIチームへの移行は、ワークフローを混乱させました。FAIRは計算リソースにおける優先順位を失い、探索的な作業が遅くなり、一方で製品チームは短期的な成果を求めました。これにより、内部ベンチマークが期待外れだったために巨大な「Behemoth」モデルの開発が中止されたり、タイミングの悪いLlama 4のローンチ（専用の推論モデルを含む完全なバリアントなしで週末にリリース）などの遅延が発生しました。批評家は、不完全なテストと体系的な反復の欠如を指摘し、競合他社の洗練されたローンチと対比させています。

#### 3. **パフォーマンス格差とコミュニティの反発**
Llama 4は、マルチモーダル機能と1,000万トークンという巨大なコンテキストウィンドウにもかかわらず、長いコンテキストでの情報検索や多段階推論といった主要なベンチマークで期待外れの結果に終わりました。これらの分野では、DeepSeek R1（低コストの中国製モデル）やMistralのアップデートが大きく躍進しました。Hugging Faceのようなプラットフォーム上の開発者たちは、より急速に進化する代替手段にダウンロードをシフトし、Llamaの採用率を低下させました。指標の水増し（ランキング用にカスタマイズされたバージョンの使用）と不透明性に対する非難は信頼をさらに損ない、ChatGPTやGeminiと比較したMetaのユーザーエンゲージメントの遅れは、1日あたりの低いトラフィックと定着率の統計によって浮き彫りになりました。

#### 4. **戦略的な不一致**
Metaは「前進への道」としてオープンソースに注力を続けましたが、クローズドモデルのリーダーや機敏なオープンソースの競合他社のペースには追いつけませんでした。Zuckerbergによる急速なスケーリングへの圧力は、AI開発の現実と衝突し、「ブルースカイ」研究よりも商業製品へのリソースの再配分を招きました。2025年までに、これはFAIRの「緩やかな死」（内部関係者談）、Joelle Pineauの退任などのリーダーシップの刷新、そして不名誉を避けるためのクローズドソースモデルへの転換の噂として現れました。その間、Googleのような競合他社は、ベンチマークを圧倒するリリースとより良い価格設定でMetaの失策を利用しました。

要するに、Metaの2023年の成功は、大胆な開放性とスターチームによって支えられていましたが、2025年はそのリスクを露呈しました：超競争環境における人材の流出、縦割り化された優先順位、そしてイノベーション疲労です。同社は現在、「超知能研究所」のために積極的に採用を行い、巻き返しを図っていますが、追いつくためには失われた魔法を再構築する必要があります。

### 参考文献
- [Meta’s Llama Troubles](https://medium.com/predict/metas-llama-troubles-f637f21a82dd)
- [Meta's Llama AI team has been bleeding talent](https://www.businessinsider.com/meta-llama-ai-talent-mistral-2025-5)
- [Google Leads With LLMs, Meta and OpenAI Struggle](https://spectrum.ieee.org/large-language-models-2025)
- [Meta’s AI research lab is ‘dying a slow death’](https://fortune.com/2025/04/10/meta-ai-research-lab-fair-questions-departures-future-yann-lecun-new-beginning/)
- [Meta Is Delaying the Rollout of Its 'Behemoth' AI Model](https://www.wsj.com/tech/ai/meta-is-delaying-the-rollout-of-its-flagship-ai-model-f4b105f7)
- [Statistics Reveal How Far Behind Meta Is Against Top AI Competitors](https://seekingalpha.com/article/4774647-statistics-reveal-how-far-behind-meta-is-against-top-ai-competitors-its-not-even-close)