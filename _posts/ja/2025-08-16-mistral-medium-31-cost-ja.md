---
audio: false
generated: true
image: false
lang: ja
layout: post
title: ミストラル ミディアム 3.1 コスト内訳簡略化
translated: true
type: note
---

Mistral Medium 3.1の「コスト」についてお聞きですね。混乱を避け、明確に説明します。

---

## Mistral Medium 3.1の価格

最新のデータに基づく：

* **入力トークン**は **100万トークンあたり \$0.40**。
* **出力トークン**は **100万トークンあたり \$2.00**。
  ([Mistral AI][1])

一部の情報源では、入力と出力の典型的な比率（例: 3:1、つまり入力3単位に対して出力1単位）を仮定した、**100万トークンあたり約 \$0.80**というブレンド平均価格が示されています。
([Artificial Analysis][2])

---

## それは「高コスト」なのか？

**比較対象によって異なります**：

* GPT‑4のようなハイエンドモデルと比較すると、これは非常に経済的です — Mistral Medium 3（そして3.1も同様）は、最先端に近い性能を**最大8倍低コスト**で提供します。
  ([Mistral AI][3])

* 内部効率指標によると、GPT‑4レベルの推論能力を**コスト約20％**で実現しており、本格的なAIワークロードにおいて予算に優しい選択肢となっています。
  ([Mistral AI][1])

* 純粋なトークンベースの比較：100万トークンを送信すると\$0.40。モデルが100万トークンで応答すると、さらに\$2.00かかります。バランスの取れた3:1のやり取りでは、100万トークンあたり約\$0.80で平均化され — これでも依然として非常に妥当な水準です。
  ([Artificial Analysis][2])

---

### 結論

* **Mistral Medium 3.1は高価なのか？**
  **あまりそうとは言えません。** GPT-4のようなプレミアムモデルの数分の一のコストで、ハイエンドな性能を提供します。

* **トークンコストは控えめ** — 入力が100万トークンあたり\$0.40、出力が\$2.00で、標準的な使用割合を想定すれば約\$0.80で平均化されます。

---

ご自身の想定使用量（例えば、プロンプトあたり10,000トークンを送信する場合や、特定の応答長を予想する場合など）に基づいて計算を実行してみませんか？お申し付けいただければ、推定をお手伝いします！

[1]: https://iamistral.com/pricing/?utm_source=chatgpt.com "Mistral AI Pricing"
[2]: https://artificialanalysis.ai/models/mistral-medium-3-1?utm_source=chatgpt.com "Mistral Medium 3.1 - Intelligence, Performance & Price ..."
[3]: https://mistral.ai/news/mistral-medium-3?utm_source=chatgpt.com "Medium is the new large."