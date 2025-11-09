---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: SenseTimeのAIモデルは競合に遅れ
translated: true
type: note
---

### SenseTimeのDayDayNewとRiri Xinモデルの理解

SenseTimeは、中国の「AIドラゴン」の一つとして、2014年以降コンピュータビジョンと顔認識のリーダーとなってきました。生成AIの時代において、同社はSenseNovaの傘下で大規模言語モデル（LLM）に軸足を移しています。「DayDayNew」（中国語では「日日新」と表記されることが多い）は、対話型AIプラットフォームとモデルシリーズを指し、最新のDayDayNew 6.5は2025年10月末の世界人工知能会議（WAIC）で発表されました。これは、テキスト、画像、動画の処理などのマルチモーダルタスク向けに設計されており、企業向けアプリケーション、API統合、およびハードウェア連携（例：Xiaomi AI glasses）を強く重視しています。「Riri Xin」（日日新統合モデル）は、2025年初頭にローンチされた関連する軽量マルチモーダルLLMであり、深い推論、クロスモーダル生成、およびコンシューマーデバイス向けの効率性に焦点を当てています。

これらのモデルは、中国の超競争的なAI環境で競争することを目指していますが、DeepSeek (DeepSeek-V3)、Kimi (Moonshot AIのKimiシリーズ)、MiniMax (ABABシリーズ) のようなフロンティアプレイヤーと比較して、生の性能ベンチマークでは確かに遅れを取っています。参考までに、2025年半ばのSuperCLUEベンチマーク（推論、数学、一般能力に関する主要な中国LLM評価）では、DeepSeek-V3が総合スコア（～85/100）でトップとなり、Kimi K2が～82、MiniMax ABABが～80でしたが、SenseNovaの各種モデル（Riri Xin統合モデルを含む）は70～75前後で、推論とコーディングタスクではMiniMaxに敗れることが多かったです。同様の差は、MMLUやHumanEvalなどのグローバル評価にも見られ、SenseTimeは純粋なテキスト推論よりもマルチモーダルを優先していることがわかります。

### DeepSeek、Kimi、MiniMaxに遅れを取る理由

この遅れは、SenseTimeのレガシー、市場動態、および外部圧力に根ざすいくつかの要因によって説明できます：

1.  **コンピュータビジョンからLLMへの遅れた転換**: SenseTimeは、知覚AI（例：監視技術）でその帝国を築き、生成LLMには2023年にSenseNovaで本格参入しました。これは、LLMネイティブのスタートアップと比較して、彼らのスケーリングを遅らせました。DeepSeek（2023年設立）とMoonshot AI（Kimi、2023年）は、効率的でオープンウェイトのモデルにレーザーフォーカスで開始し、コスト効率の高いトレーニングのためのスパースアテンションのようなアーキテクチャを迅速に反復しました。MiniMaxは、より若い（2021年）にもかかわらず、初日からビデオ生成（Hailuo）のようなコンシューマーアプリ向けに最適化していました。

2.  **米国エンティティリスト制裁**: 2019年に人権問題の疑いで米国にブラックリストに登録されたSenseTimeは、高度なチップ（例：NVIDIA GPU）や米国技術へのアクセスが制限されています。これは、競合他社の規模でのトレーニングを妨げています — DeepSeekは国産のHuawei Ascendチップを革新的に使用し、KimiとMiniMaxは同じ輸出規制のないハイブリッド設定を活用しています。結果：モデル更新の遅延とコスト上昇により、性能差は拡大しています。

3.  **機敏なスタートアップ対確立された巨人**: SenseTimeは上場企業（香港取引所上場）で～10億ドル以上の収益を持ち、企業顧客（例：銀行、政府）にサービスを提供しています。これにより、官僚主義と、最先端のベンチマークよりも準拠したマルチモーダルソリューションへの焦点がもたらされます。対照的に：
    - DeepSeekは「高速、安価、オープン」なモデルを重視し、低い推論コストでオープンソースリーダーボードを席巻しています。
    - Kimiは長文コンテキスト推論（最大200Kトークン）に優れ、OpenAIのo1に対抗します。
    - MiniMaxはマルチモーダル（テキストからビデオへ）と効率性で光り、しばしばSenseTimeと直接対決して勝利します。

    皮肉なことに、MiniMaxの創業者（Yan JunjieとZhou Yucong）は元SenseTimeエンジニアで、同社でディープラーニングツールチェーンを率いていました。彼らはより機敏なスタートアップを構築するために去り、その専門知識を持って旧雇主を追い抜きました — これは人材の流動性が中国のAI軍拡競争を促進する方法を浮き彫りにしています。

4.  **ベンチマークと誇大宣伝の力学**: SuperCLUEのような中国の評価は、推論/数学を重視し、スタートアップはこれに過度に注力します。SenseTimeの強みは統合（例：ファインチューニングのためのSenseCoreクラウド）にありますが、「フロンティア」テストではパフォーマンスが低下します。誇大宣伝が少ないことは、反復のためのユーザー/データが少ないことを意味し、フィードバックループを生み出します。2025年10月現在、SenseTimeはAIGC市場シェアの約14％（トップ3）を保持していますが、それは収益ベースであり、能力ベースではありません。

### 最近のニュースとSenseTimeの取り組み

SenseTimeに関するニュースはスタートアップの熱狂（例：DeepSeekのバイラルなR1リリース）に比べて静かですが、同社は企業向け/生成AIの成長において活動的です：

-   **2025年4月**: SenseNova V6 Omniをローンチ。自社主張では中国で「最も先進的」なマルチモーダルモデルで、モデル理解を向上させるSenseCore 2.0インフラストラクチャへのアップグレードを伴います。
-   **2025年6月**: AI競争の中でByteDance/Alibabaとともにモデル更新に参加し、コスト効率の良いAPIを強調。
-   **2025年8月**: DayDayNewプラットフォームがXiaomi AI glassesと統合；生成AI需要（トレーニング/推論サービス）により収益が前年比21％急増。
-   **2025年9月**: 非中核部門を切り離し、生成AIへの焦点を合理化して収益性に向けて推進。
-   **2025年10月**: WAICでDayDayNew 6.5とMynieプラットフォームを発表、マルチモーダルインタラクション（例：動画理解力30％向上）を後押し。

彼らはコンシューマーチャットボットではなくB2B（例：クラウドサービス、デバイス組み込み）に注力しており、これが「ニュースがない」感覚 — バイラルなデモが少なく、地味な企業での勝利 — を説明しています。それでも、制裁緩和の話し合いと国産チップの進歩により、2026年までに差を縮める可能性があります。

要するに、SenseTimeのレガシーはスタートアップとの短距離走において足かせとなりますが、彼らのマルチモーダルへの賭けは、純粋なベンチマーク追跡よりも実用的な勝利に向けたポジショニングを可能にしています。

[ChinAI #324: SuperCLUE Benchmarks —2025 Midyear Check-in](https://chinai.substack.com/p/chinai-324-superclue-large-model)  
[SenseTime's SenseNova Foundation Models Among Top Three](https://www.sensetime.com/en/news-detail/51169429?categoryId=1072)  
[An Overview of Chinese AI Tigers](https://www.topbots.com/chinese-ai-tigers-overview/)  
[China's SenseTime Reshapes to Focus on Generative AI Growth](https://www.reuters.com/technology/artificial-intelligence/chinas-sensetime-reshapes-focus-generative-ai-growth-2024-12-04/)  
[SenseTime Unveils DayDayNew 6.5 AI Model](https://forntend-test-5sqwmq-3a22a9-107-172-80-230.traefik.me/sensetime-unveils-daydaynew-6-5-ai-model-and-mynie-platform-1753705726167)