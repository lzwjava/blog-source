---
audio: false
generated: true
image: false
lang: ja
layout: post
title: トランスクリプトクリーンアップガイドのベストモデル
translated: true
type: note
---

優れたユースケースです。**厳格なフォーマットと「余計な発言なし」が求められる長文トランスクリプトのクリーンアップ**について、OpenRouterで現在最も効果的な方法をシナリオ別に紹介します。

**高速＋低コストなワークホース（英語/中国語、長文ファイル）：DeepSeek-V3.1**
指示への追従性が高く、128kのコンテキストを処理可能。速度が必要な場合は「推論」をオフに、テキストが乱れている場合はオンに切り替えられます。フィラー語の削除や一貫した話者タグ付けにおいて、二言語で良好なパフォーマンスを発揮します。（[DeepSeek API Docs][1], [OpenRouter][2]）

**中国語が多いインタビューと口語表現：Kimi K2 Instruct**
MoonshotのK2（MoE）は中国語のスラングやスタイルに特に流暢。技術用語をそのまま保持しつつ、中国語メインのトランスクリプトに最適です。（[OpenRouter][3]）

**編集指示への最高の準拠：Claude Sonnet (3.7/4)**
AnthropicのSonnetシリーズは「メタ発言なしで洗練されたテキストのみを出力」することに優れており、意味の変更に関して控えめな傾向があります—ステップリストの制約に理想的です。利用可能ならSonnet 4を、3.7も良好に動作します。（[OpenRouter][4]）

**超長セッションまたは一発でのプロジェクト全体処理：GPT-5**
非常に大きなコンテキストを処理し、虚構発生成を低く抑えたい場合、OpenRouter上のフロンティアモデルではGPT-5が最も安全な選択です（非常に大きなコンテキストでリストされ、強力な推論と編集能力を備える）。マラソン的なトランスクリプトや最終的な「仕上げ」処理に使用します。（[OpenRouter][5]）

**同樣に強力だがコストプロファイルに注意：Gemini 2.5 Pro**
推論と長文コンテキスト編集において非常に有能です。洗練には優れていますが、プロバイダ経路に応じた価格/クォータに注意してください。（[OpenRouter][6]）

---

### 実用的なルーティングレシピ（表なし）

* **≤128k トークン、英語/中国語混合、速度重視:** DeepSeek-V3.1 (非推論モード)。段落が混沌としている場合のみ推論モードに切り替え。（[DeepSeek API Docs][1]）
* **主に中国語のトランスクリプト:** Kimi K2 Instruct。（[OpenRouter][3]）
* **厳格な「編集者」動作（コメントなし）、法務/金融トーン:** Claude Sonnet。（[OpenRouter][4]）
* **巨大ファイルまたは最終的な単一パス仕上げ:** GPT-5。（[OpenRouter][5]）

---

### これを堅牢にするためのクイックコード調整

* **モデル選択可能化**: `--model` CLIフラグを追加。デフォルトは `deepseek-v3.1`。
* **サイズ/言語による自動ルーティング**: トークン数と中国語比率を検出。中国語が多い場合はK2、巨大入力の場合はGPT-5、「厳格編集」モードの場合はClaudeを選択。
* **推論トグル（DeepSeek）**: 難しい箇所に対して、OpenRouterコール内で `reasoning.enabled` を設定するパラメータを追加。（[DeepSeek API Docs][1]）
* **小さなバグの修正**: 迷子の `print(".1f")` を修正。話者ラベルの正規表現を拡張し、`A：`（全角コロン）やスペースなしのバリアントを許可。
* **ガードレール**: 長さの差分が10%を超える場合、「コンテンツを削除しない」リマインダーで自動リトライ。`A:`/`B:` が見つからない場合、「話者にラベルを付ける」促しで自動リトライ。

必要であれば、`--model` フラグとスマートルーティングロジックを追加するために、あなたのスクリプトを今すぐ書き直すことができます。

[1]: https://api-docs.deepseek.com/quick_start/pricing?utm_source=chatgpt.com "Models & Pricing"
[2]: https://openrouter.ai/deepseek/deepseek-chat-v3.1?utm_source=chatgpt.com "DeepSeek V3.1 - API, Providers, Stats"
[3]: https://openrouter.ai/moonshotai/kimi-k2?utm_source=chatgpt.com "Kimi K2 - API, Providers, Stats"
[4]: https://openrouter.ai/anthropic/claude-3.7-sonnet?utm_source=chatgpt.com "Claude 3.7 Sonnet - API, Providers, Stats"
[5]: https://openrouter.ai/openai/gpt-5?utm_source=chatgpt.com "GPT-5 - API, Providers, Stats"
[6]: https://openrouter.ai/google/gemini-2.5-pro?utm_source=chatgpt.com "Gemini 2.5 Pro - API, Providers, Stats"