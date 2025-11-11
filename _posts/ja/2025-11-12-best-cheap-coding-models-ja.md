---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: OpenRouterで選ぶ最高のコーディングモデル
translated: true
type: note
---

### Codex CLI via OpenRouterでコーディングに最適な低コストモデル

2025年現在の最近のベンチマーク、ユーザーディスカッション、モデルランキングに基づき、Codex CLIでのコーディングタスクにおいてGPT-5-Codexの代替として最適で手頃な価格のモデルをいくつか紹介します。GPT-5-Codexは確かに高価（プロバイダーによって異なりますが、多くの場合100万トークンあたり入力$20-50 / 出力$60-150の範囲）であるため、ここでは強力なコーディング性能を持ちながらコスト効率の良いオプションに焦点を当てます。OpenRouterの従量課金制では処理されたトークンのみを支払うため、多くのモデルが無料枠を持っていたり、非常に低いレート（100万トークンあたり入出力合計$1未満）であったりします。

SWE-Bench、HumanEval、Aiderなどのコーディングベンチマークで高スコアを獲得しながら、安価または無料のモデルを優先して紹介します。モデルIDは`config.toml`での使用を容易にするためにフォーマットされています（例: `model = "provider/model-name"`）。正確な最新の価格は、レートが変動する可能性があるため、OpenRouterのモデルページで確認してください。

#### おすすめトップ:
- **Grok Code Fast (xAI)**  
  モデルID: `xai/grok-code-fast`  
  理由: コーディングにおけるOpenRouterのLLMランキングでトップ。速度とエージェントタスク（例: 国際情報オリンピックで#1）に優れる。基本的な使用では無料であることが多く、プラットフォームで最も使用されているモデル。反復的なコーディングワークフローに最適。  
  価格: 無料 または ~$0.50/$2.00 per 1M トークン (入力/出力)。コンテキスト: 128K トークン。

- **Kat Coder Pro (KwaiPilot)**  
  モデルID: `kwaipilot/kat-coder-pro:free`  
  理由: SWE-Bench Verifiedで73.4%を達成した専門的なコーディングモデルで、トップのプロプライエタリモデルに匹敵。期間限定無料であり、複雑な推論とコード生成に理想的。  
  価格: 無料 (プロモーション)。コンテキスト: 256K トークン、出力は最大 32K。

- **DeepSeek Coder V3 (DeepSeek)**  
  モデルID: `deepseek/deepseek-coder-v3`  
  理由: Aiderコーディングスコアで約71%と優れた価値を提供し、実装とデバッグに強い。フォーラムで予算重視のコーディングによく推薦される。  
  価格: 非常に安価 (~$0.14/$0.28 per 1M)。コンテキスト: 128K トークン。

- **Llama 4 Maverick (Meta)**  
  モデルID: `meta/llama-4-maverick`  
  理由: コーディング品質とVS Code統合（例: RooCodeのようなツールと）において無料ティアで最高。実世界のコードタスクで良好なパフォーマンスを発揮。  
  価格: 無料ティア利用可能、または低コスト (~$0.20/$0.80 per 1M)。コンテキスト: 128K トークン。

- **Mistral Devstral Small (Mistral)**  
  モデルID: `mistral/devstral-small`  
  理由: 価格、高速なスループット、コード実装において優れるように最適化されている。大規模モデルと組み合わせたハイブリッドワークフローでよく使用される。  
  価格: 安価 (~$0.25/$1.00 per 1M)。コンテキスト: 128K トークン。

- **Qwen3 235B (Qwen)**  
  モデルID: `qwen/qwen3-235b`  
  理由: コーディングベンチマークで高いパフォーマンスを発揮し、コスト最適化されたセットアップに推薦される。大規模なコードプロジェクトをうまく処理する。  
  価格: 手頃 (~$0.50/$2.00 per 1M)。コンテキスト: 128K トークン。

- **Gemini 2.5 Flash (Google)**  
  モデルID: `google/gemini-2.5-flash`  
  理由: ランキングで#3、反復的なコーディングにおいて高速かつ低コスト。コードがデータ可視化を含む場合、マルチモーダルタスクにも強い。  
  価格: 安価 (~$0.35/$1.05 per 1M)。コンテキスト: 1M トークン。

これらのモデルはOpenAI互換であるため、プロバイダーを"openrouter"に設定し、APIキーを設定すれば、Codex CLIでシームレスに動作します。Grok Code FastやKat Coderのような無料のものからテストを始めてみてください。コーディング特有の用途では、SWE-Benchスコアを確認してください — スコアが高いほど実際のGitHubイシューを解決する能力が優れていることを意味します。より多くのコンテキストや速度が必要な場合は、OpenRouterのルーティングを利用して安価なモデルへの自動フォールバックを組み合わせてください。

統合方法: `config.toml`に、`[profiles cheap-coder]`のようなプロファイルを追加し、`model_provider = "openrouter"`および`model = "上記のIDのいずれか"`を設定します。

[Top AI Models on OpenRouter 2025: Performance vs Cost Guide](https://www.teamday.ai/blog/top-ai-models-openrouter-2025)  
[Best Budget Coding LLMs 2025: DeepSeek R1 vs Gemini vs GPT](https://llmx.de/blog/budget-coding-llms-2025/)  
[What are the best LLMs available on OpenRouter to use for coding](https://medium.com/@okreitz/what-are-the-best-llms-available-on-openrouter-to-use-for-coding-with-kilo-ca04e75a84ee)  
[Best Free AI Models You Can Use on OpenRouter](https://apidog.com/blog/free-ai-models/)  
[Top AI Coding Models in 2025](https://www.veerotech.net/blog/top-ai-coding-models-in-2025-boost-your-development-workflow-with-these-game-changers/)  
[LLM Rankings - OpenRouter](https://openrouter.ai/rankings)  
[Top 5 AI Coding Models of March 2025](https://dev.to/apipie-ai/top-5-ai-coding-models-of-march-2025-5f04)  
[Models - OpenRouter](https://openrouter.ai/models)  
[whats the best coding model on openrouter? - Reddit](https://www.reddit.com/r/RooCode/comments/1kdu7we/whats_the_best_coding_model_on_openrouter/)