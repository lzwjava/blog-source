---
audio: false
generated: true
image: false
lang: ja
layout: post
title: クラウドAPI料金詳細 2025
translated: true
type: note
---

以下は、Anthropic ClaudeモデルのAPI利用料金をわかりやすくまとめたものです。表形式ではなく、読みやすい文章で説明します。

---

### Claude Sonnet 4

* **入力トークン:** 100万トークンあたり3ドル
* **出力トークン:** 100万トークンあたり15ドル
* **利用可能な割引:** プロンプトキャッシングで最大**90%オフ**、バッチ処理で最大**50%オフ**が適用されます。([custom.typingmind.com][1], [Reddit][2], [Anthropic][3], [Anthropic][4])

---

### Claude 3.5 Sonnet (現在は非推奨)

* **入力トークン:** 100万トークンあたり3ドル
* **出力トークン:** 100万トークンあたり15ドル
* **バッチおよびキャッシュ料金:** 他のSonnetモデルと同じ階層型システムです。バッチ入力は1.50ドル、バッチ出力は7.50ドル、5分間のキャッシュヒットは0.30ドルです。([Anthropic Docs][5])

---

### Claude 3.7 Sonnet

* **基本料金:** 3.5と全く同じです。100万入力トークンあたり3ドル、100万出力トークンあたり15ドルで、ハイブリッドな「思考」モードを使用する場合も同様です。([Reddit][6], [Anthropic Docs][5])

---

### Claude Opus 4

* **入力トークン:** 100万トークンあたり15ドル
* **出力トークン:** 100万トークンあたり75ドル
* **バッチおよびキャッシュ割引:** バッチ入力は7.50ドル、バッチ出力は37.50ドル、キャッシュヒットは1.50ドルです。([Anthropic][7], [Amazon Web Services, Inc.][8], [Anthropic Docs][5], [Wikipedia][9])

---

### 簡単なまとめ

* **すべてのSonnetモデル (3.5, 3.7, 4):** 100万入力トークンあたり3ドル / 100万出力トークンあたり15ドルで、バッチ処理とキャッシングによりさらなる割引があります。
* **Opus 4:** 100万トークンあたり15ドル / 75ドルと大幅に高額ですが、深い推論、長時間のタスク、高いパフォーマンスに最適化されています。

---

### 追加情報

* **モデルの進化:** Claude 3.5 Sonnetは、2024年6月のリリース時にコーディング能力で新たなベンチマークを樹立しましたが、2025年2月の3.7、そして2025年5月のSonnet 4においても、パフォーマンスの向上にもかかわらず料金は変更されていません。([Business Insider][10], [Anthropic][7], [Anthropic Docs][5], [Wikipedia][11])
* **ユースケースに合わせた選択:** ワークロードがチャット中心または高ボリュームである場合、Sonnetモデルは優れたコストパフォーマンスを提供します。非常に複雑なタスクや長時間に及ぶエージェントワークフローの場合は、Opus、または両方を組み合わせたハイブリッド戦略の方が効率的かもしれません。

---

特定のトークン量に基づくコスト例、キャッシングを考慮した比較、あるいはどのモデルを選択すべきかのガイダンスが必要でしたら、お気軽にお知らせください。喜んでご説明いたします。

[1]: https://custom.typingmind.com/tools/estimate-llm-usage-costs/claude-3.5-sonnet?utm_source=chatgpt.com "Anthropic claude-3.5-sonnet API Pricing Calculator"
[2]: https://www.reddit.com/r/ClaudeAI/comments/1jclyjp/can_anthropic_keep_up_with_those_pricing/?utm_source=chatgpt.com "Can Anthropic keep up with those pricing ? : r/ClaudeAI"
[3]: https://www.anthropic.com/news/claude-3-5-sonnet?utm_source=chatgpt.com "Introducing Claude 3.5 Sonnet"
[4]: https://www.anthropic.com/claude/sonnet?utm_source=chatgpt.com "Claude Sonnet 4"
[5]: https://docs.anthropic.com/en/docs/about-claude/pricing?utm_source=chatgpt.com "Pricing"
[6]: https://www.reddit.com/r/ClaudeAI/comments/1ixtyj0/sonnet_37_x_cline_costs_are_skyrocketing/?utm_source=chatgpt.com "Sonnet 3.7 x Cline: Costs are skyrocketing? : r/ClaudeAI"
[7]: https://www.anthropic.com/news/claude-3-7-sonnet?utm_source=chatgpt.com "Claude 3.7 Sonnet and Claude Code"
[8]: https://aws.amazon.com/marketplace/pp/prodview-h2mamlwah46ym?utm_source=chatgpt.com "AWS Marketplace: Claude 3.5 Sonnet (Amazon Bedrock Edition)"
[9]: https://zh.wikipedia.org/wiki/Claude_%28%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%29?utm_source=chatgpt.com "Claude (语言模型)"
[10]: https://www.businessinsider.com/anthropic-ai-breakthrough-vibe-coding-revolution-2025-7?utm_source=chatgpt.com "'The Trillion-Dollar Question': How did Anthropic make AI so good at coding?"
[11]: https://en.wikipedia.org/wiki/Claude_%28language_model%29?utm_source=chatgpt.com "Claude (language model)"