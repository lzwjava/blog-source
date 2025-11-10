---
audio: false
generated: true
image: false
lang: ja
layout: post
title: AIモデルのコストとパフォーマンスガイド
translated: true
type: note
---

各モデル（Claude 4 Opus（Claude Opus 4とも表記）、GPT-5（標準/フル）、GPT-5 Mini、GPT-5 Nano、o3（OpenAI）、Claude 4 Sonnet）の**ベンチマークスコア**と**API価格**を、表を使用せずに明確にまとめました。読みやすさを重視しています。

---

## ベンチマーク性能 (SWE-bench)

ソフトウェアエンジニアリングタスクにおけるモデルの性能を示します：

* **Claude 4 Opus (2025年5月14日)**: 67.60
* **GPT-5 (2025年8月7日, 中程度推論)**: 65.00
* **Claude 4 Sonnet (2025年5月14日)**: 64.93 ([SWE-bench][1])

**要点**: Claude 4 OpusがSWE-benchの性能でわずかにリードしており、GPT-5とClaude Sonnetがそれに続きます。

---

## API価格 (100万トークンあたり)

### **Claude 4 Opus**

* 入力: **\$15**
* 出力: **\$75** ([Anthropic][2], [LaoZhang AI][3], [Simon Willison’s Weblog][4])

### **GPT-5 (標準/フル)**

* 入力: **\$1.25**
* キャッシュ入力 (再利用時): **\$0.125**
* 出力: **\$10** ([OpenAI][5])

### **GPT-5 Mini**

* 入力: **\$0.25**
* 出力: **\$2** ([OpenAI][5], [WIRED][6])

### **GPT-5 Nano**

* 入力: **\$0.05**
* 出力: **\$0.40** ([OpenAI][5], [WIRED][6])

### **o3-mini** (参考)

* o4-mini リファレンスによる価格:
* 入力: **\$1.10**, 出力: **\$4.40** ([Simon Willison’s Weblog][4])

### **Claude 4 Sonnet**

* 入力: **\$3**, 出力: **\$15** ([LaoZhang AI][3])

---

## 簡単な比較のハイライト

* **最高性能**: Claude 4 OpusがコーディングベンチマークでGPT-5およびClaude Sonnetをわずかに上回ります。
* **トークンあたりの最低コスト**:

  * **GPT-5 Nano**が断然最も安価 – 要約などの軽量タスクに最適です。
  * **GPT-5 Mini**は速度と手頃な価格のバランスを提供します。
  * **GPT-5 標準**は、特に安価なキャッシュを考慮すると、非常にコスト効率が良いままです。
* **Claudeモデル**（OpusとSonnetの両方）はトークンあたりのコストが大幅に高いですが、より強力な推論能力とエージェント機能によってその価格を正当化しています。

---

## まとめ (明確かつ簡潔に):

* **Claude 4 Opus**: 最高性能、高コスト (\$15 入力 / \$75 出力)。
* **GPT-5 (フル)**: 優れた性能 (Opusにわずかに次ぐ)、はるかに安価 (\$1.25 入力 / \$10 出力)。
* **GPT-5 Mini**: ミドルティアの予算に優しいオプション (\$0.25 入力 / \$2 出力)。
* **GPT-5 Nano**: 軽量タスクまたは大規模な低コスト利用に理想的 (\$0.05 入力 / \$0.40 出力)。
* **Claude 4 Sonnet**: コストと性能の中間 (\$3 入力 / \$15 出力)、ただしベンチマークは他モデルよりわずかに低め。

---

特定の使用パターンに基づく**月額コスト**の見積もりが必要な場合、またはプロンプトキャッシュとバッチ割引を考慮した比較が必要な場合は、お知らせください！

[1]: https://www.swebench.com/?utm_source=chatgpt.com "SWE-bench Leaderboards"
[2]: https://www.anthropic.com/pricing?utm_source=chatgpt.com "Pricing"
[3]: https://blog.laozhang.ai/ai-tools/claude-4-pricing-guide-2025/?utm_source=chatgpt.com "Claude 4.0 Pricing Guide: Complete Cost Analysis & Best ..."
[4]: https://simonwillison.net/2025/Aug/7/gpt-5/?utm_source=chatgpt.com "GPT-5: Key characteristics, pricing and model card"
[5]: https://openai.com/api/pricing/?utm_source=chatgpt.com "API Pricing"
[6]: https://www.wired.com/story/openais-gpt-5-is-here/?utm_source=chatgpt.com "OpenAI Finally Launched GPT-5. Here's Everything You ..."