---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 回転ResNetに過ぎなかったLSTM
translated: true
type: note
---

NeurIPS 2024のTest of Time賞を受賞した2014年の論文「Sequence to Sequence Learning with Neural Networks」に関する講演で、Ilya Sutskeverは当時の重要な洞察と誤りを振り返りました。彼が「我々が間違っていた点」として取り上げた主要な問題の一つは、機械翻訳のような初期の系列モデリングのブレークスルーを支えたLSTM（Long Short-Term Memory networks）の過剰な複雑化とその限界でした。

### LSTMに関する核心的な誤解
我々はLSTMを、系列データに特化して設計された根本的に新しく複雑なアーキテクチャ——時間依存性、勾配消失、再帰性を扱うために深層学習研究者が苦心して設計しなければならない「特別な」もの——として扱っていました。しかしSutskeverが説明したように、現実にはLSTMはそれよりもはるかに単純なものでした：**それらは本質的に90度回転させたResNet（Residual Network）に過ぎない**のです。

- **ResNet**（2015年に導入）は、情報が層を直接跨いで流れることを可能にするスキップ接続（残差）を追加することで、訓練の不安定性なしに遥かに深いネットワークを可能にし、画像処理に革命をもたらしました。
- LSTM（1997年から）は、*時間次元*で同様のことを行っていました：そのゲートとセル状態は残差のように機能し、勾配と情報が消失することなく長い系列にわたって伝播することを可能にします。それは同じ原理——単に空間的な積み重ね（例：画像内のピクセル）から時間的な積み重ね（例：文の中の単語）へと「回転」させただけなのです。

Sutskeverは冗談交じりにこう述べています：「よく知らない人にとって、LSTMとはTransformer以前の貧しい深層学習研究者が使っていたものです。それは基本的にはResNetですが90度回転させたようなもの…。そしてそれは以前に登場しました。少し複雑な、積分器といくつかの乗算を持つResNetのようなものです。」このアナロジーは、LSTMが根本的な方向転換ではなく、再帰性への残差の考え方の初期のエレガントな応用であったことを強調しています。

### これが重要だった理由（そして何がうまくいかなかったか）
- **見事に機能した点**：LSTMは当時としては驚くほどスケールし、seq2seqモデルが翻訳タスクで従来の統計的手法を凌駕することを可能にしました。この残差接続は、後にフィードフォワードネットワークで実現したのと同様に、深い再帰ネットワークの学習を可能にしました。
- **我々が間違っていた点（そしてLSTMが衰退した理由）**：我々はLSTMの逐次的な性質がスケーリングのボトルネックとなることを過小評価していました。並列化可能なResNetやTransformerとは異なり、LSTMはデータをステップバイステップで処理するため、大規模データセットや長い文脈に対して非効率です。また、LSTMはTransformerの注意機構によって単純化される不必要な複雑さ（例：複数のゲート）を追加していました。2017年までにTransformerはこれらの限界を明らかにし、より優れた並列性と長距離依存性を実現するためのself-attentionへと焦点を移行させました。

後知恵では、LSTMを発明したこと自体が「間違い」だったのではありません——それらは過渡期における画期的な解決策でした——しかし、系列モデルの最終形としてLSTMに固執し、残差接続を一般的なツールとして認識し、より並列的なアーキテクチャへと早期に推進しなかったことが「間違い」だったのです。

この視点は、LSTMを過去の遺物ではなく、スキップ接続が如何に次元を超えて深度を解放するかを理解するための基礎的な一歩として再定義します。

[Sequence to Sequence Learning with Neural Networks: What a Decade – Transcript & Video](https://kingy.ai/news/sequence-to-sequence-learning-with-neural-networks-what-a-decade-transcript-video/)  
[Ilya Sutskever NeurIPS 2024 full talk](https://www.youtube.com/watch?v=1yvBqasHLZs)  
[Reflections from Ilya's Full Talk at NeurIPS 2024](https://dlyog.com/papers/one_internet_v1)