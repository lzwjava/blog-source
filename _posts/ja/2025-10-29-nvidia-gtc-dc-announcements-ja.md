---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: NVIDIA GTC ワシントンD.C. 発表
translated: true
type: note
---

### 2025年10月29日 NVIDIA発表まとめ

NVIDIAはGTCワシントンD.C.カンファレンス（10月27日～29日）の最終日を迎え、本日はAIインフラストラクチャ、通信分野の進展、次世代ハードウェアに焦点を当てたいくつかの主要発表がありました。主な内容を以下にまとめます：

#### アメリカのAIインフラストラクチャ構築
NVIDIAは、米国エネルギー省の国立研究所（アルゴンヌ、ロスアラモス）および主要企業との協業を発表し、大規模なAIスーパーコンピュータの導入と、ギガワット規模の「AIファクトリー」の青写真作成を進めます。
- **主要システム**: アルゴンヌ研究所に設置されるSolstice（NVIDIA Blackwell GPU 10万基、エネルギー省最大のAIスーパーコンピュータ、Oracleと共同構築）およびEquinox（Blackwell GPU 1万基、2026年稼働開始、最大2,200エクサフロップス性能）。その他、アルゴンヌ研究所のTara、Minerva、Janusや、ロスアラモス国立研究所のMission/Visionなど、今後登場するVera Rubinプラットフォームを採用したシステム。
- **パートナー**: SolsticeにはOracle、ハードウェアにHPE、デジタルツインにベクテル/ジェイコブズ、電力/冷却にイートン、GE ヴェルノヴァ、テスラなど。Google Cloud、Microsoft Azure、xAIといったクラウドプロバイダーは、BlackwellおよびGB300ラックを用いたAIファクトリーを拡大中。
- **目標**: アメリカ主導のAIイノベーションにより、科学の発見、経済成長、「次の産業革命」を加速すること。NVIDIAはバージニア州にVera Rubinを搭載したAIファクトリー研究センターを開設します。

これにより、リリー（創薬）やメイヨークリニック（医療）などの企業による投資と相まって、米国はAIにおけるリーダーシップを確立する立場にあります。

#### ノキアとのAIネイティブ6Gネットワークに関する提携
NVIDIAとノキアは、5G-Advancedおよび6G向けのAI無線アクセスネットワーク（AI-RAN）の先駆けとなる戦略的提携を発表し、米国の通信分野におけるリーダーシップ奪還を目指します。
- **投資**: NVIDIAがノキアに対し10億ドル（1株6.01ドル）を投資し、イノベーションの加速を図ります。
- **新技術**: NVIDIA Aerial ARC-Proプラットフォーム（接続性、コンピューティング、センシングを統合した6G対応RANコンピュータ）。ノキアは自社のAirScale基地局装置にこれを統合し、アップグレードを提供します。
- **協力企業**: T-Mobile（2026年に性能/効率性に関する実証試験を実施）、デル（PowerEdgeサーバーを提供）。
- **影響**: 2030年までに2000億ドル規模に達すると見込まれるAI-RAN市場をターゲットとし、AIトラフィックの急増（例：モバイルでのChatGPT利用）への対応や、ドローン、AR/VR、エージェント型AI向けの新サービスを可能にします。また、NVIDIAのAIデータセンター向けにノキアの光技術の活用も検討中です。

#### 次世代Vera Rubinスーパーチップの公開
主要なハードウェア発表として、NVIDIAはBlackwellの後継となる、極大規模AI向けのVera Rubinプラットフォームを披露しました。
- **仕様**: Vera CPU（88 ARMコア、176スレッド）と2基のRubin GPU（各GPUは2つのレティクルサイズダイを搭載、FP4性能最大50ペタフロップス、288 GB HBM4メモリ）をペアリング。1.8 TB/sのNVLinkおよび最大1.8 TBのシステムメモリをサポート。
- **システム**:
  - Rubin NVL144（2026年後半）: 3.6エクサフロップスのFP4推論性能（GB300比3.3倍）、13 TB/sのHBM4帯域幅。
  - Rubin Ultra NVL576（2027年後半）: 15エクサフロップスのFP4推論性能（GB300比14倍）、4.6 PB/sのHBM4帯域幅。
- **タイムライン**: GPUは現在TSMCにて試験中。量産は2026年第3四半期/第4四半期、またはそれ以前を予定。

これは前述のAIファクトリーやスーパーコンピュータを駆動し、推論、学習、帯域幅において2～12倍の性能向上をもたらします。

その他の注記：昨日発表されたPalantirとの統合（CUDA-XおよびNemotronをAIPに組み込み、エンタープライズAIを強化）は、本日のインフラストラクチャ推進策と連動しており、またNVIDIAは本日終了するROSConにおいてオープンロボティクスフレームワークへの貢献も行いました。

[ NVIDIA and Partners Build America’s AI Infrastructure](https://nvidianews.nvidia.com/news/nvidia-partners-ai-infrastructure-america)  
[ NVIDIA and Nokia to Pioneer the AI Platform for 6G](https://nvidianews.nvidia.com/news/nvidia-nokia-ai-telecommunications)  
[ NVIDIA Shows Next-Gen Vera Rubin Superchip](https://wccftech.com/nvidia-shows-next-gen-vera-rubin-superchip-two-massive-gpus-production-next-year/)  
[ GTC Washington D.C. Event Page](https://www.nvidia.com/gtc/dc/)