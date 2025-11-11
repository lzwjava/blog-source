---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: OpenRouter向けCodex CLIの設定
translated: true
type: note
---

### OpenRouter向けCodex CLI設定のセットアップ

Codex CLI（OpenAI製）は、設定ファイルを介してOpenRouterのようなカスタムモデルプロバイダーをサポートするターミナルベースのコーディングエージェントです。OpenRouterはOpenAI互換のAPIを提供しているため、適切なベースURLでプロバイダーを定義することでリクエストを経由させることができます。これにより、Codexを使用しながらより広範なモデル（Anthropic、Google、またはオープンソースプロバイダーなど）にアクセスできます。

設定はTOMLファイル`~/.codex/config.toml`に保存されます（存在しない場合は作成してください）。OpenRouter用の**モデルプロバイダー**セクションを定義し、特定のモデルの**プロファイル**で参照します。

#### ステップ1: OpenRouter APIキーの取得
- まだの場合は[openrouter.ai](https://openrouter.ai)でサインアップしてください
- アカウントダッシュボードからAPIキーを生成してください
- 環境変数として設定します：  
  ```
  export OPENROUTER_API_KEY=your_api_key_here
  ```
  永続化するにはシェルプロファイル（例：`~/.bashrc`または`~/.zshrc`）に追加してください

#### ステップ2: 設定ファイルの編集
エディタで`~/.codex/config.toml`を開き、以下のセクションを追加します。これにより、ベースURLがOpenRouterのエンドポイント（`https://openrouter.ai/api/v1`）に設定されます（これはOpenAI互換で、Codexは自動的に`/chat/completions`を追加します）。

```toml
# OpenRouterプロバイダーの定義
[model_providers.openrouter]
name = "OpenRouter"
base_url = "https://openrouter.ai/api/v1"
env_key = "OPENROUTER_API_KEY"  # 認証用に環境変数から読み取り

# このプロバイダーを使用するプロファイルの定義（例：GPTライクモデルの使用）
[profiles.openrouter-gpt]
model_provider = "openrouter"
model = "openai/gpt-4o-mini"  # OpenRouterのモデルIDで置き換え可能、例："anthropic/claude-3.5-sonnet"
```

- **主要フィールドの説明**：
  - `base_url`: OpenRouterのAPIエンドポイントを指します。これによりデフォルトのOpenAIベースURLが上書きされます
  - `env_key`: Bearerトークン認証ヘッダーのための環境変数を指定します
  - `model`: [OpenRouterのモデル一覧](https://openrouter.ai/models)から正確なモデルIDを使用します。コーディングタスクでは"openai/codex-mini-latest"や"meta-llama/llama-3.1-405b-instruct"を試してみてください
  - 異なるモデル用に複数のプロファイルを追加できます（例：`[profiles.openrouter-claude]`で`model = "anthropic/claude-3.5-sonnet"`）

#### ステップ3: 設定の使用
- 必要に応じてCodex CLIをインストール：`npm install -g @openai/codex`（またはHomebrew経由：`brew install codex`）
- プロファイルを指定してCodexを実行：  
  ```
  codex --profile openrouter-gpt
  ```
  または設定でデフォルトプロファイルを設定：  
  ```toml
  [default_profile]
  name = "openrouter-gpt"
  ```
- テスト：`codex`を実行し、簡単なコーディングプロンプトを与えてください。使用状況はOpenRouterのダッシュボードで確認できます

#### トラブルシューティング
- **認証エラー**: `OPENROUTER_API_KEY`が設定されエクスポートされていることを確認してください
- **モデルが見つからない**: OpenRouterでモデルIDを確認してください - 大文字小文字を区別し、プレフィックスが付きます（例："provider/model-name"）
- **バージョンチェック**: 完全なプロバイダーサポートにはCodex CLI v0.13以上を使用してください。`npm update -g @openai/codex`で更新できます
- **高度なルーティング**: コスト最適化ルーティングのようなOpenRouter固有の機能については、プロファイルの下に`provider = { sort = "price" }`のようなオプションパラメータを追加してください（新しいバージョンでサポート）

このセットアップにより、CodexのOpenAIスタイルAPIとの互換性を保ちながら、OpenRouterのエコシステムを活用できます。詳細については、[Codex CLIのnpmドキュメント](https://www.npmjs.com/package/@openai/codex)またはOpenRouterの[APIガイド](https://openrouter.ai/docs)を参照してください。Open Codexのようなフォークを使用している場合、設定は似ていますがGeminiサポートなどの追加機能がある場合があります。