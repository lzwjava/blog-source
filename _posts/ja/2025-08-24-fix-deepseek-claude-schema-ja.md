---
audio: false
generated: true
image: false
lang: ja
layout: post
title: DeepSeek Claudeコードスキーマ不一致の修正
translated: true
type: note
---

短い答え：スキーマの不一致です。

Claude Codeは「Anthropic仕様」（`tool_use`/`tool_result`ブロックのようなAnthropic-Messages形式のツール使用を期待）で動作します。一方、OpenRouter上のDeepSeek V3.1は「OpenAI仕様」（OpenAI形式の`tool_calls`/関数呼び出しを出力）で動作します。Claude Codeルーターがリクエスト/レスポンスを変換せずにDeepSeek V3.1にタスクを転送すると、アシスタントのツール呼び出しメッセージが解析できず、エージェントがツールの計画/実行や出力ストリーミングを試みた瞬間にエラーが発生します。（[Anthropic][1], [OpenRouter][2], [DeepSeek API Docs][3]）

対処法（クイックフィックス）：

1. ルーターのトランスフォーマーを使用する
   Claude CodeルーターでOpenRouter↔︎Anthropicリクエスト/レスポンストランスフォーマーを有効にし、`tool_calls` ⇄ `tool_use`を双方向にマッピングします。人気のコミュニティルーターはこれを明示的にサポートしています。「Request/Response Transformation」セクションと設定例を確認してください。（[GitHub][4], [ClaudeLog][5]）

2. 正しいモデルスラッグを選択する
   DeepSeek V3.1には特定のOpenRouterスラッグ（例：V3.1/V3ファミリーエントリ）があります。誤ったまたは古いスラッグを使用すると、ストリーミングやツール実行フェーズでエラーが発生する可能性があります。OpenRouterのDeepSeekページに表示されている正確なモデルIDを確認し、ルーターマッピングで使用してください。（[OpenRouter][6]）

3. フィールドマッピングが完了するまで「chat」モデルを使用する（「reasoner」ではない）
   特別な推論フィールドをストリーミングする推論バリアントを試す場合、ルーターがそれらを翻訳する必要があります。さもなければClaude Codeが処理できません。標準的なチャットモデルを優先するか、トランスフォーマーが対応するまで追加の「思考」出力を無効にしてください。（DeepSeekのドキュメントはOpenAI形式の関数呼び出しを強調しています。マッピングすべきはそれです。）（[DeepSeek API Docs][3]）

4. 最新のルータービルドに更新する
   最近のコミュニティビルドでは、非Anthropicプロバイダー向けの互換性調整が追加されています。テスト前にアップグレードしてください。（[GitHub][4]）

これがV3.1でのみ発生する理由
V3.1はデフォルトで強力なエージェント/ツール呼び出し機能を追加しました。これにより、Claude Codeフローが変換されていないツールメッセージに遭遇する可能性が高まり、まさにその場所でスキーマの不一致が問題を引き起こします。（[DeepSeek API Docs][7]）

正確なエラーテキストを共有していただければ、設定に追加すべき具体的なトランスフォーマースニペットを指摘できます。

[1]: https://www.anthropic.com/engineering/claude-code-best-practices?utm_source=chatgpt.com "Claude Code: エージェント型コーディングのベストプラクティス"
[2]: https://openrouter.ai/docs/features/tool-calling?utm_source=chatgpt.com "ツール & 関数呼び出し"
[3]: https://api-docs.deepseek.com/guides/function_calling?utm_source=chatgpt.com "関数呼び出し"
[4]: https://github.com/musistudio/claude-code-router?utm_source=chatgpt.com "musistudio/claude-code-router"
[5]: https://claudelog.com/claude-code-mcps/claude-code-router/?utm_source=chatgpt.com "Claude Code ルーター"
[6]: https://openrouter.ai/models?q=deepseek&utm_source=chatgpt.com "モデル: 'deepseek'"
[7]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 リリース"