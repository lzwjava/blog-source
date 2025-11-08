---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Vision Transformerの著者と貢献
translated: true
type: note
---

### 「An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale」の著者紹介

2020年にAlexey DosovitskiyとGoogleの同僚によって発表された画期的な論文「An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale」は、コンピュータビジョンにおける画期的な転換点となりました。この論文は、Vision Transformer (ViT)を提案し、自然言語処理向けに設計されたトランスフォーマーアーキテクチャを画像パッチに直接適用し、大規模なデータ（例: JFT-300M）で事前学習を行うことで、ImageNetなどの大規模データセットにおいて最先端の性能を達成しました。この研究は、十分な計算資源とデータがあれば、純粋なトランスフォーマーが畳み込みニューラルネットワーク(CNN)を効率性と精度で凌駕できることを実証し、その後のマルチモーダルAIやスケーラブルなビジョンモデルの進歩に影響を与えました。

この論文は、主にGoogle Brainのチューリッヒチームに所属する12名の研究者による共同作業であり、深層学習、シーケンスモデリング、大規模学習に関する専門知識が結集されました。以下は、主要な著者の背景とこの分野への貢献に焦点を当てた概要です。（簡潔さのため、主要な貢献者に焦点を当てています。完全なリストには、Dirk Weissenborn、Thomas Unterthiner、Mostafa Dehghani、Matthias Minderer、Georg Heigold、Sylvain Gelly、Jakob Uszkoreitが含まれます。これらは全員、トランスフォーマー、最適化、視覚言語統合に深い関わりを持つGoogle出身者です。）

#### 主要な著者と背景

- **Alexey Dosovitskiy** (筆頭著者): ViTの背後にある原動力として、Dosovitskiyは画像をパッチのシーケンスとして扱うという核心的なアイデアを概念化しました。ロモノーソフモスクワ国立大学で数学の修士号と博士号を取得し、フライブルク大学で教師なし特徴学習に関する博士研究員を経て、2019年にGoogle Brainに参加しました。2021年にInceptive（ベルリンを拠点とするAI企業）に移る前にViTの開発を主導しました。その研究はコンピュータビジョン、生成モデル、生物学に着想を得た機械学習に及び、引用数は136,000回を超えます。

- **Lucas Beyer**: Beyerは、ViTの実用的な実装、ベンチマークでの評価、効率性の最適化において重要な役割を果たしました。ベルギー出身で、アーヘン工科大学で機械工学を学び、ゲームAIと強化学習に焦点を当てて2018年にロボティクスとAIの博士号を取得しました。博士号取得後にGoogle Brainチューリッヒに参加し、Google DeepMindではスタッフリサーチサイエンティストに昇進しました。2025年にはMetaのトップAI人材の一人として採用され、ビジョントランスフォーマーとデータ中心の機械学習に関する研究を継続しています。

- **Alexander Kolesnikov**: Kolesnikovは、ViTのスケーリング実験と転移学習に関する洞察、特に中規模データセットでの性能に貢献しました。モスクワ国立大学で数学の修士号を取得し、2018年にオーストリア科学技術研究所(ISTA)で機械学習/コンピュータビジョンの博士号を取得しました。2018年にGoogle Brainに入社し、DeepMindでスタッフ職に就いた後、OpenAIを経て2025年にMetaに参加しました。効率的なビジョンモデルに関する専門知識を評価されての引き抜きでした。

- **Xiaohua Zhai**: Zhaiは、表現学習における自身の研究を活かし、ViTの事前学習戦略とマルチモーダル拡張に焦点を当てました。北京大学で電子工学の博士号を取得し、2015年にソフトウェアエンジニアとしてGoogleに入社、2017年にGoogle Brain、2023年にDeepMindで研究に携わりました。現在はMetaの研究者（2025年にはOpenAIチューリッヒを経由）であり、視覚、言語、自己教師あり学習を橋渡しする貢献を行い、引用数は100,000回を超えます。

- **Neil Houlsby** (シニア著者): チームリードとして、HoulsbyはViTのアーキテクチャ設計と、ビジョンにおけるスケーリング則へのより広範な影響を監督しました。2010年頃にGoogle European Doctoral Fellowshipを受け、機械学習で博士号を取得しました。インターン時代から長きにわたるGoogleの研究者であり、Google BrainとDeepMindでニューラルアーキテクチャと視覚言語モデルに関するチームを管理しました。2025年にはAnthropicに参加し、新設されたチューリッヒオフィスの責任者として、安全なAIのスケーリングに焦点を当てています。

このGoogle Brain（主にチューリッヒ拠点）の共同研究は、チームのTPUへの近接性を活かし、25,000 TPU日以上に及ぶ大規模な実験を通じて、トランスフォーマーのテキスト以外での実現可能性を証明しました。多くの著者はその後、Meta、OpenAI、Anthropicなどの主要なAI研究所に移っており、ViTがこの分野に与えた持続的な影響を反映しています。

#### 参考文献
- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (arXiv)](https://arxiv.org/abs/2010.11929)
- [Alexey Dosovitskiy Google Scholar Profile](https://scholar.google.com/citations?user=FXNJRDoAAAAJ)
- [Lucas Beyer Google Scholar Profile](https://scholar.google.com/citations?user=p2gwhK4AAAAJ)
- [Alexander Kolesnikov Google Scholar Profile](https://scholar.google.com/citations?user=H9I0CVwAAAAJ)
- [Xiaohua Zhai Google Scholar Profile](https://scholar.google.com/citations?user=8gruapYAAAAJ)
- [Neil Houlsby Google Scholar Profile](https://scholar.google.com/citations?user=sm1-TZMAAAAJ)
- [From Ph.D. Detour to Meta's Top AI Hire: Lucas Beyer (Times of India)](https://timesofindia.indiatimes.com/education/news/lucas-beyer-educational-qualification-from-ph-d-detour-and-google-rejection-to-becoming-metas-top-ai-hire/articleshow/122158414.cms)
- [Zuckerberg Poaches Alexander Kolesnikov from OpenAI (Times of India)](https://timesofindia.indiatimes.com/education/news/zuckerberg-poached-alexander-kolesnikov-from-sam-altmans-openai-where-did-this-ai-genius-study/articleshow/122158654.cms)
- [Anthropic Poaches Neil Houlsby from Google DeepMind (Euronews)](https://www.euronews.com/next/2025/02/13/anthropic-poaches-google-deepmind-talent-to-lead-new-european-office)