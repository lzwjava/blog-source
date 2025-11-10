---
audio: false
generated: true
lang: ja
layout: post
title: ミストラルAIの2025年モデルコンテキスト長
translated: true
type: note
---

2025年6月現在、Mistral AIは様々なコンテキスト長を持つ複数のモデルをリリースしています。主要なモデルとそのコンテキストウィンドウの概要は以下の通りです：

* **Magistral Small (magistral-small-2506):** このオープンウェイトモデルは128kのコンテキストウィンドウを持ちますが、40kを超えるとパフォーマンスが低下する可能性があるため、推奨最大長は40kトークンです。
* **Magistral Medium (magistral-medium-2506):** このAPI専用の推論モデルも、推奨コンテキストウィンドウは40kです。
* **Mistral Small 3.1 (mistral-small-2503) / Mistral Small 3.2 (mistral-small-2506):** これらのモデルは最大128,000トークンのコンテキストウィンドウを特徴とします。
* **Codestral (codestral-2501):** このコード特化型モデルは、256,000トークンという大幅なコンテキストウィンドウを誇ります。
* **Mistral Large 2 (mistral-large-2407 / mistral-large-2411):** Mistralのフラッグシップ大規模モデルは128kのコンテキストウィンドウを持ちます。
* **Mistral NeMo (open-mistral-nemo-2407):** NVIDIAとの協業で開発されたこの12Bモデルは、最大128,000トークンの大規模なコンテキストウィンドウを提供します。
* **Mistral Medium 3 (mistral-medium-2505):** このマルチモーダルモデルも128kのコンテキストウィンドウをサポートします。

一部のモデルは非常に大きなコンテキストウィンドウ（例：128k）を宣伝していますが、実用的なパフォーマンスはやや小さい範囲（例：Magistralモデルの場合は40k）で最適化されている可能性があることに注意することが重要です。