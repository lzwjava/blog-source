---
audio: false
generated: true
image: false
lang: ja
layout: post
title: ミュオン：構造を考慮した行列オプティマイザー
translated: true
type: note
---

「Kimi」における「Muon」は、高度なオプティマイザー、具体的には**構造を考慮した行列直交化オプティマイザー**を指し、Kimi K2言語モデルのトレーニングに使用されています。

---

### Muonオプティマイザーとは？

1.  **行列を考慮した最適化**
    AdamWやSGDとは異なり、Muonは重み行列を独立したスカラーパラメータではなく、幾何学的な実体として扱います。**Newton–Schulz反復**を適用して運動量平均化された勾配を直交化し、行列の行と列の構造の両方を尊重した、条件の良いバランスの取れた更新を実現します ([Medium][1], [kellerjordan.github.io][2])。

2.  **Newton–Schulzによる直交化**
    計算コストの高い特異値分解 (SVD) を実行する代わりに、Muonは高速な反復法 (Newton–Schulz) を使用して勾配に最も近い直交行列を近似します。これにより、更新が**スペクトルノルム制約**下に保たれ、エネルギーを保存し、学習を全ての方向に均等に広げます ([Medium][1], [kellerjordan.github.io][2])。

3.  **パイプラインの調整**
    標準的な更新フローである**勾配 → 運動量 → パラメータ更新**が、以下のように置き換えられます：
    **勾配 → 運動量 → Newton–Schulz直交化 → パラメータ更新**
    この変更により、2次元パラメータ行列に対するトレーニングの効率と安定性が向上します ([Medium][3], [kellerjordan.github.io][2])。

4.  **実践的な効率性**
    計算上のオーバーヘッドが少し増えるにもかかわらず、Muonは大幅な高速化をもたらします：

    *   NanoGPTスピードランニングで記録を達成し、トレーニング時間を約35%短縮 ([kellerjordan.github.io][2])。
    *   重み減衰とパラメータ単位のRMS調整と組み合わせることで、大規模言語モデルのトレーニングにおいても良好にスケールします ([arXiv][4])。

5.  **強固な理論的基盤**
    最近の研究は、Muonの収束特性、重み減衰の利点、最適なバッチサイズ設定を支持しています。研究は、より厳密な理論的境界と、実用的なシナリオ全体にわたる効率性を確認しています ([arXiv][5])。

---

### **Kimi K2** におけるMuonの役割

Kimi K2は、Moonshot AIの**Mixture-of-Experts (MoE) モデル**であり、**総パラメータ数1兆** (活性化は32B) を誇り、エージェント機能向けに最適化されています。このモデルは、知識、推論、コーディングのベンチマークで卓越したパフォーマンスを達成しましたが、その一部はMuon (および**MuonClip**と呼ばれる派生形) を用いたトレーニングによるものです ([Hugging Face][6], [Poe][7])。

*   **MuonClipオプティマイザー**は、Muonを大規模に適用しつつ、そのような大規模モデルに固有の安定性の課題に対処することを指します ([Hugging Face][6], [Poe][7])。
*   このオプティマイザーは、大規模なトークンデータセット (約15.5兆トークン) において**トレーニングの不安定性をゼロに抑え**、最先端の結果をもたらす上で重要な役割を果たしました ([Hugging Face][6])。

---

### まとめ (表はなし、ご要望通り)

*   **Muon** = 「MomentUm Orthogonalized by Newton–Schulz」— 生の勾配更新を直交化された更新に置き換え、行列パラメータに対する学習ダイナミクスを改善するオプティマイザー。
*   構造を保存し、バランスの取れた更新を保証し、コストの高い分解の代わりに反復的な直交化によって効率性を維持します。
*   **Kimi K2**は、Muon (およびMuonClip) を活用して大規模MoEトレーニングの限界に挑み、安定性と計算効率を兼ね備えた最高のパフォーマンスを実現しています。

---

さらに深く掘り下げたい場合はお知らせください。例えば、トレーニング軌跡におけるMuonとAdamWの比較、MoE向けにMuonClipがアルゴリズムをどのように調整しているか、Newton–Schulz法がコード上でどのように機能するかなどについて説明できます！

[1]: https://medium.com/%40gauritr01/the-truth-about-kimi-k2-pretraining-muon-optimizer-moe-unpacked-43554527d94a?utm_source=chatgpt.com "The Truth About KIMI K2 Pretraining: Muon Optimizer ..."
[2]: https://kellerjordan.github.io/posts/muon/?utm_source=chatgpt.com "Muon: An optimizer for hidden layers in neural networks"
[3]: https://medium.com/%40jenwei0312/going-beyond-adamw-a-practical-guide-to-the-muon-optimizer-93d90e91dbd3?utm_source=chatgpt.com "Going Beyond AdamW: A Practical Guide to the Muon ..."
[4]: https://arxiv.org/html/2502.16982v1?utm_source=chatgpt.com "Muon is Scalable for LLM Training"
[5]: https://arxiv.org/abs/2507.01598?utm_source=chatgpt.com "Convergence Bound and Critical Batch Size of Muon Optimizer"
[6]: https://huggingface.co/moonshotai/Kimi-K2-Base?utm_source=chatgpt.com "moonshotai/Kimi-K2-Base"
[7]: https://poe.com/Kimi-K2?utm_source=chatgpt.com "Kimi-K2"