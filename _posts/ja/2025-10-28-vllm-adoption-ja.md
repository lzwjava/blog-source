---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: AIプロバイダーによるvLLM導入
translated: true
type: note
---

### AIプロバイダーによるvLLMの使用状況

vLLMは、オープンウェイトモデルを効率的に提供するために一般的に推奨されるオープンソースの推論エンジンです。しかし、本番サービスでの採用状況は様々です。利用可能な情報に基づく内訳は以下の通りです：

| プロバイダー/モデル | 本番環境でvLLMを使用？ | 詳細 |
|---------------|---------------------------|---------|
| **Claude (Anthropic)** | いいえ | AnthropicはClaudeモデルの提供に独自のインフラに依存しています。vLLMはAnthropicのAPIを模倣したローカルまたはサードパーティのデプロイメントとの互換性を提供しますが、内部での使用の証拠はありません。 |
| **OpenAI (GPTモデル)** | いいえ | OpenAIは規模に最適化されたカスタムの社内提供システムを使用しています。vLLMはローカル推論のためのOpenAI互換APIをサポートしますが、OpenAIはその本番環境の基盤としてvLLMを使用していません。 |
| **Minimax AI** | いいえ | MiniMaxはMiniMax-M1/M2のようなモデルをオープンソース化し、そのパフォーマンスからユーザーデプロイメントにvLLMを推奨しています。彼らのコアとなる本番APIでのvLLM使用は確認されておらず、フォークやカスタム設定を使用している可能性があります。 |
| **Kimi (Moonshot AI)** | いいえ | MoonshotはKimi-K2のセルフホスティングにvLLMを推奨しており、彼らのCheckpoint-Engineツールは重み更新のためにvLLMと統合されます。しかし、彼らの本番推論では、SGLangやTensorRT-LLMのようなエンジンと共に、独自の最適化を多用している可能性が高いです。 |
| **DeepSeek AI** | はい | DeepSeekは、彼らの研究からの最適化を組み込んだ、vLLM上に直接構築されたカスタム推論エンジンをオープンソース化しています。これはDeepSeek-V3やR1のようなモデルに使用され、vLLMプロジェクトへの貢献も行っています。 |

### 参考文献
- [DeepSeek、vLLM上に構築されたカスタム推論エンジンをオープンソース化](https://www.ainews.com/p/deepseek-open-sources-custom-inference-engine-built-on-vllm)
- [DeepSeek推論エンジンをオープンソース化するまでの道のり](https://news.ycombinator.com/item?id=43682088)
- [MiniMax-M1ハイブリッドアーキテクチャとvLLMの出会い](https://blog.vllm.ai/2025/06/30/minimax-m1.html)
- [Kimi K2: オープンなエージェント知能](https://moonshotai.github.io/Kimi-K2/)
- [OpenAI互換サーバー - vLLM](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html)
- [Anthropic API `/v1/messages` エンドポイントのサポート · Issue #21313 · vllm-project/vllm](https://github.com/vllm-project/vllm/issues/21313)