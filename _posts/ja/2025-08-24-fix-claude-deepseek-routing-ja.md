---
audio: false
generated: true
image: false
lang: ja
layout: post
title: クロードコードディープシーク設定ルーティング修正
translated: true
type: note
---

了解しました。あなたの設定では、**Claude CodeのAnthropic形式のトラフィック**が**OpenRouterのOpenAI形式エンドポイント**にDeepSeek V3.1用に送信されています。Claude Code（IDEエージェント）がtools/plan/streamを実行しようとすると、メッセージスキーマが一致せず→エラーが発生します。

以下は、**Anthropicモデル**がAnthropic形式のゲートウェイを使用し、**DeepSeek V3.1**（OpenAI形式）が`/chat/completions`に残るように配線するクリーンな方法です。貼り付け可能な正確な編集内容を示します。

---

### 1) DeepSeek V3.1のslugを確認

OpenRouterのチャットモデルslugは以下です：

```
deepseek/deepseek-chat-v3.1
```

（これはinstruct/chatモデルであり、「base」モデルとは異なります。）([OpenRouter][1])

---

### 2) Claude Code用にAnthropic形式のプロキシを追加

Claude Codeは**Anthropic Messages**（`/messages`、`tool_use`ブロック）を期待します。最も簡単な修正方法は、Anthropic→OpenAI（OpenRouter）およびその逆の変換を行う小さなプロキシを実行することです。既製のものがあります：**maxnowack/anthropic-proxy**。以下のように起動します（環境変数はあなたのOpenRouterキーです）：

```bash
OPENROUTER_API_KEY=YOUR_KEY npx anthropic-proxy
```

これはローカルでリッスンし、スキーマを変換します。([GitHub][2])

次に、Claude Codeのトラフィックをそのプロキシに向ける**2番目のプロバイダー**を追加します。

#### 🔧 あなたのJSONを以下の焦点を絞った変更に置き換え

**このプロバイダーを追加（現在の`openrouter`プロバイダーはそのまま保持）：**

```json
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
```

**既存のOpenRouterプロバイダーを保持（DeepSeekや他のOpenAIスキーマモデルには`/chat/completions`を使用するのは正しいです）。** OpenRouterはOpenAI互換スキーマに正規化し、推論トークン、ツールなどの追加機能をサポートします。([OpenRouter][3])

---

### 3) モデルを適切なプロバイダーにルーティング

Anthropicモデルは**anthropic-proxy**を指すように；DeepSeek/GPT/Gemini/Qwenは**openrouter**を指すようにします。

挿入可能なRouterブロックの例：

```json
"Router": {
  "default": "openrouter,openai/gpt-5-mini",

  "background": "openrouter,google/gemini-2.5-flash",
  "think": "openrouter,qwen/qwen3-coder",
  "longContext": "openrouter,moonshotai/kimi-k2",
  "longContextThreshold": 2000,
  "webSearch": "openrouter,mistralai/mistral-medium-3.1",

  "overrides": {
    "anthropic/claude-sonnet-4": "anthropic-proxy,anthropic/claude-sonnet-4",
    "anthropic/claude-3.5-sonnet": "anthropic-proxy,anthropic/claude-3.5-sonnet",
    "anthropic/claude-3.7-sonnet:thinking": "anthropic-proxy,anthropic/claude-3.7-sonnet:thinking",
    "anthropic/claude-opus-4": "anthropic-proxy,anthropic/claude-opus-4",

    "deepseek/deepseek-chat-v3.1": "openrouter,deepseek/deepseek-chat-v3.1"
  }
}
```

> あなたのルーターが`overrides`マップをサポートしていない場合、同等の方法は：アプリ内で別々の「プロファイル」（例：「anthropic-proxy経由のClaude Code」と「openrouter経由の一般チャット」）を作成し、アクションごとにプロファイルを選択することです。

---

### 4) DeepSeekでの推論ストリーム衝突を回避（オプションだが安全）

DeepSeek V3.1は**「thinking」トークン**をサポートします。多くのラッパーは、それらがストリームの途中で出現すると混乱します。OpenRouterでは、リクエストフラグで**推論を除外**できます。あなたのルーターがモデルごとのパラメータ設定を許可する場合、以下を添付します：

```json
"params": {
  "reasoning": { "exclude": true }
}
```

（または、あなたのルーターのパラメータ名に応じて`include_reasoning: false`）。これにより、あなたのClaude Code UIがプレーンテキストを期待する場所に`