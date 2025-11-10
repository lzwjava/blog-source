---
audio: false
generated: true
image: false
lang: ja
layout: post
title: OpenRouterと直接APIコストの比較
translated: true
type: note
---

はい、OpenRouter APIを使用して同じモデルにアクセスすることは、DeepSeek、Mistral、Google（Gemini）、xAI（Grok）などのプロバイダーから直接公式APIを使用する場合と比較して、一般的にコストが高くなります。OpenRouterは推論コスト自体にマークアップを加えず、基盤となるプロバイダーの価格をそのまま通過させると主張していますが、全体の費用を増加させる追加料金を請求します：

- 標準的な支払い方法でクレジットを購入する場合、5.5%の手数料（最低$0.80）、暗号通貨での支払いの場合はさらに5%追加。
- サポートされているプロバイダー向けに独自のAPIキー（BYOK）を持ち込む場合でも、OpenRouterはOpenRouterクレジットから（彼らの見積もるモデルコストに基づいて）5%の手数料を差し引きます。

これらの手数料により、OpenRouterは使用量と支払い方法に応じて、直接利用する場合よりも実質的に5〜5.5%高くなり、固定の最低料金も加算されます。直接アクセスではこれらの追加料金は発生せず、プロバイダーのトークン料金のみを支払います。

### コスト比較例
以下は、利用可能な価格データに基づく大まかな比較です（100万トークンあたりのUSD。レートはモデルバージョン、時間帯、キャッシュ、地域によって変動する可能性があるため、最新の詳細は常に公式サイトで確認してください）。OpenRouterの基本トークンレートはプロバイダーと一致しますが、上記の手数料が追加されます。

- **DeepSeek**:
  - 直接: 入力 ~$0.14–$0.55（キャッシュヒット/ミス）、出力 ~$1.10–$2.19（モデルと割引期間によって変動）。
  - OpenRouter: 同じ基本レート + 5–5.5%の手数料。

- **Mistral**:
  - 直接: 入力 ~$2.00 (Large 2の場合)、出力 ~$6.00（混合レートに基づく推定。Smallなどの旧モデルは入力~$0.15/出力~$0.50）。
  - OpenRouter: 同じ基本レート + 5–5.5%の手数料。

- **Gemini (Google)**:
  - 直接: モデルによって大きく異なる（例: Gemini 1.5 Pro: 入力 $1.25–$2.50、出力 $5.00–$10.00; Gemini 1.5 Flash: 入力 $0.075–$0.15、出力 $0.30–$0.60）。
  - OpenRouter: 同じ基本レート + 5–5.5%の手数料（Google向けBYOKはサポートされている可能性あり）。

- **Grok (xAI)**:
  - Grok APIの価格とアクセスの詳細については、https://x.ai/api を参照。公開情報に基づくと、Grok-3/Grok-4のレートは入力$3.00/出力$15.00程度、Grok-3-miniは入力$0.30/出力$0.50程度。
  - OpenRouter: 同じ基本レート + 5–5.5%の手数料（xAI向けBYOKは通常言及されていない）。

使用量が多額の場合、パーセンテージの手数料は急速に増加します。使用量が少ない場合やテスト目的では、その差は最小限かもしれませんが、直接アクセスの方が依然として安価です。OpenRouterの価値は、統一されたAPIとルーティング機能にあり、利便性のために追加コストを正当化する可能性があります。

[OpenRouter FAQ](https://openrouter.ai/docs/faq)  
[DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing)  
[Mistral AI Pricing](https://mistral.ai/pricing)  
[Google Gemini API Pricing](https://ai.google.dev/pricing)  
[xAI API](https://x.ai/api)  
[Mistral Large 2 Analysis](https://artificialanalysis.ai/models/mistral-large-2)  
[DeepSeek Pricing Guide](https://team-gpt.com/blog/deepseek-pricing/)