---
audio: false
generated: true
image: false
lang: ja
layout: post
title: DeepSeekツール呼び出し競合の修正
translated: true
type: note
---

**ツール呼び出しの検証エラー**が発生しています。DeepSeek（OpenAI形式）が、Anthropic形式のツールメッセージを期待するClaude Codeフローで使用されています。安全な修正方法は2つあります：

* **Claude Code関連の作業をすべてAnthropicにルーティングする**（プロキシ経由）
* **DeepSeekを使用する際はツールをオフにし**（プレーンテキストのみを返すように）、推論ストリームを抑制する

以下は両方を行う更新された単一ファイル設定です。そのまま貼り付けてください：

```json
{
  "PROXY_URL": "http://127.0.0.1:7890",
  "LOG": true,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "",
      "models": [
        "moonshotai/kimi-k2",
        "anthropic/claude-sonnet-4",
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.7-sonnet:thinking",
        "anthropic/claude-opus-4",
        "google/gemini-2.5-flash",
        "google/gemini-2.5-pro",
        "deepseek/deepseek-chat-v3-0324",
        "deepseek/deepseek-chat-v3.1",
        "deepseek/deepseek-r1",
        "mistralai/mistral-medium-3.1",
        "qwen/qwen3-coder",
        "openai/gpt-oss-120b",
        "openai/gpt-5",
        "openai/gpt-5-mini",
        "x-ai/grok-3-mini"
      ],
      "transformer": {
        "use": ["openrouter"]
      },
      "params": {
        "deepseek/deepseek-chat-v3.1": {
          "tool_choice": "none",
          "reasoning": { "exclude": true }
        },
        "deepseek/deepseek-r1": {
          "tool_choice": "none",
          "reasoning": { "exclude": true }
        }
      }
    },
    {
      "name": "anthropic-proxy",
      "api_base_url": "http://127.0.0.1:3000/v1/messages",
      "api_key": "",
      "models": [
        "anthropic/claude-sonnet-4",
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.7-sonnet:thinking",
        "anthropic/claude-opus-4"
      ]
    }
  ],
  "Router": {
    "default": "anthropic-proxy,anthropic/claude-sonnet-4",
    "background": "anthropic-proxy,anthropic/claude-sonnet-4",
    "think": "anthropic-proxy,anthropic/claude-sonnet-4",
    "longContext": "openrouter,moonshotai/kimi-k2",
    "longContextThreshold": 2000,
    "webSearch": "openrouter,mistralai/mistral-medium-3.1",
    "overrides": {
      "deepseek/deepseek-chat-v3.1": "openrouter,deepseek/deepseek-chat-v3.1",
      "deepseek/deepseek-r1": "openrouter,deepseek/deepseek-r1",
      "google/gemini-2.5-flash": "openrouter,google/gemini-2.5-flash",
      "google/gemini-2.5-pro": "openrouter,google/gemini-2.5-pro",
      "qwen/qwen3-coder": "openrouter,qwen/qwen3-coder",
      "openai/gpt-5-mini": "openrouter,openai/gpt-5-mini"
    }
  }
}
```

この設定の動作：

* Claude Codeパス（`default/background/think`）は **`anthropic-proxy`経由でAnthropic** に送られるため、ツール使用が機能します
* DeepSeekは利用可能ですが、`"tool_choice":"none"`と`"reasoning.exclude": true`が設定されているため、IDEエージェントを壊すツール呼び出しや思考チャンクを出力しません
* 明示的にDeepSeekを選択した場合（例：プレーンなチャットやドラフト作成用）、OpenRouter経由でクリーンにルーティングされます

「無効なツールパラメータ」がまだ表示される場合は、何らかのレイヤーが*まだ*DeepSeekにツール呼び出しを出力させていることを意味します。その場合、ランナーがモデルごとの`params`を実際に尊重していることを確認してください。尊重しない場合は、DeepSeekの使用をツールが無効化されているコンテキストでのみに設定するか、`default`を`openai/gpt-5-mini`に戻し、DeepSeekを手動の「ツールなし」プロファイル用に予約してください。