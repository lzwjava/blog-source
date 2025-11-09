---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ニューラルネットワークのための最大更新パラメータ化
translated: true
type: note
---

### μP（Maximal Update Parametrization）とは？

μP（Maximal Update Parametrization）は、xAI（以前はMicrosoft Researchに在籍）の数学者兼AI研究者であるGreg Yangによって開発されたニューラルネットワークのパラメータ化技術です。2022年の論文「Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer」で紹介され、深層学習モデルの重みを再パラメータ化することで、トレーニングをよりスケーラブルかつ効率的にするものです。

#### 目的
μPの核心的な目標は、異なるモデルサイズ間でのハイパーパラメータ（HP）チューニングを安定させることです。従来の設定（標準パラメータ化、SP）では、学習率などのハイパーパラメータは、モデルを（例えば数百万パラメータから数十億パラメータへと）スケールアップするたびに再調整が必要でした。なぜなら、勾配と更新が不安定になる（多くの場合、モデルの幅や深さに対して二次関数的にスケールする）ためです。μPは、パラメータを変換することで、「最大更新」（可能な最大の勾配ステップ）がスケールに関わらず一貫して維持されるようにし、これを修正します。これにより、**μTransfer**というワークフローが可能になります。これは、小さな「プロキシ」モデルでHPをチューニングし、それらを追加の調整なしで大規模なターゲットモデルに直接適用するものです。

#### 主な利点
- **コストの大幅な削減**: 小さなモデルでのチューニングは低コストです。例えば、13MパラメータのプロキシからHPを転送することで、公表されているBERT-large（350Mパラメータ）の結果を上回り、総チューニングコストはBERT-largeのプレトレーニング1回分に相当しました。GPT-3（6.7Bパラメータ）では、40Mパラメータのプロキシからの転送がベースラインを上回り、フルプレトレーニングコストのわずか7%でした。
- **大規模モデルへのスケーラビリティ**: TransformerやResNetなどのアーキテクチャでうまく機能し、巨大なニューラルネットワーク（例えばxAIで使用されているもの）のトレーニングに理想的です。これは「スケール不変な最適点」を保証し、モデルが成長しても損失ランドスケープが予測不能に歪むことがありません。
- **使いやすさ**: PyTorchライブラリとして利用可能（`pip install mup`）であり、大規模なAIモデルのための本番トレーニングパイプラインに統合されています。

#### 簡単な数学的直感
SPでは、重みの分散が不安定に増大し、勾配の爆発や消失を引き起こします。μPは重みを再パラメータ化し（例えば、線形層ではファンインでスケーリングする）、Fisher情報行列を正規化して勾配の流れがバランスを保つようにします。これにより、最適なHP（学習率など）がさまざまなスケールでほぼ一定に保たれ、サイズごとの再調整が不要になります。

μPは、ニューラルネットワークの無限幅/深さ限界を理解するためのYangのより広範な「Tensor Programs」フレームワークに基づいており、現在も進化を続けています（2025年現在の最近の研究では、HP転送を超えた最大限の特徴学習におけるその役組が強調されています）。

**参考文献**
- [Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer](https://arxiv.org/abs/2203.03466)
- [The Practitioner's Guide to the Maximal Update Parameterization](https://www.cerebras.ai/blog/the-practitioners-guide-to-the-maximal-update-parameterization)
- [How To Scale (Blog on μP and Scaling)](https://howtoscalenn.github.io/)
- [Greg Yang's Professional Page](https://thegregyang.com/)