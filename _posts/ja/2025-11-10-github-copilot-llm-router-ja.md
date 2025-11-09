---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GitHub Copilot LLMルーターの設定
translated: true
type: note
---

エンタープライズ環境でLLMルーターをGitHub CopilotのLLM APIのみに限定して使用するように設定するには、専用のプロバイダーを追加し、すべてのトラフィックがそのプロバイダーを経由するようにルーター設定を調整します。

- **GitHub Copilotプロバイダーの追加**: "Providers"配列に新しいエントリを追加し、適切なAPIベースURL、APIキーとしてGitHub個人アクセストークン（PAT）、およびサポート対象モデルを指定します。
- **ルーターのデフォルト設定の更新**: すべてのルーターフィールド（例: "default", "think"）を新しいプロバイダー名のみを指すように変更し、他のプロバイダーが呼び出されないようにします。
- **エンタープライズの制限への対応**: 必要なスコープを持つエンタープライズGitHubアカウントのPATを使用し、環境がコンプライアンスのためにプロキシルーティングを要求する場合は、既存の"PROXY_URL"を活用します。
- **テストと検証**: 更新後、すべてのAPI呼び出しがCopilotエンドポイントにのみ向けられ、Copilot APIとのやり取りのみを許可するポリシーに沿っていることを確認します。

### ステップバイステップでの設定
1. **GitHub PATの生成**: GitHubエンタープライズアカウントにログインし、チャットアクセスのための`copilot`スコープや、より広範なモデル推論のための`models:read`スコープなどを持つ個人アクセストークンを作成します。これにより、広範な権限を公開せずに安全な認証が確保されます。
2. **Providers配列の修正**: 設定JSONの"Providers"リストに新しいオブジェクトを追加します。"name"を"github_copilot"など説明的なものに、"api_base_url"を（Copilotエージェントの場合は）"https://api.githubcopilot.com/chat/completions" または（一般的なGitHub Models推論の場合は）"https://models.github.ai/inference/chat/completions"に、"api_key"をあなたのPATに設定し、互換性のあるモデルをリストします。
3. **Routerセクションの調整**: "Router"オブジェクト内のすべての値を新しいプロバイダー名（例: "github_copilot"）に置き換えて、排他的な使用を強制します。これにより、OpenRouterなどの他のプロバイダーへのフォールバックが防止されます。
4. **エンタープライズ環境での考慮事項**: 制限された環境では、ネットワークポリシーがGitHubのドメインへのアウトバウンド呼び出しを許可していることを確認します。必要に応じて、"PROXY_URL"を承認されたエンタープライズプロキシを経由するように更新します。コールを監査しコンプライアンスを確保するためにロギング（"LOG": true）を有効にします。

### 更新後の設定例
以下は変更を加えた後の設定の例です（プレースホルダーを実際のPATと希望のエンドポイントに置き換えてください）:

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
        "deepseek/deepseek-chat-v3.1",
        "deepseek/deepseek-r1",
        "mistralai/mistral-medium-3.1",
        "qwen/qwen3-coder",
        "openai/gpt-oss-120b",
        "openai/gpt-5",
        "z-ai/glm-4.6",
        "x-ai/grok-code-fast-1",
        "x-ai/grok-4-fast",
        "minimax/minimax-m2",
        "moonshotai/kimi-k2-thinking"
      ],
      "transformer": {
        "use": [
          "openrouter"
        ]
      }
    },
    {
      "name": "github_copilot",
      "api_base_url": "https://api.githubcopilot.com/chat/completions",
      "api_key": "ghp_YourPersonalAccessTokenHere",
      "models": [
        "gpt-4o",
        "gpt-4o-mini",
        "claude-3-5-sonnet-20240620"
      ],
      "transformer": {
        "use": [
          "github_copilot"
        ]
      }
    }
  ],
  "Router": {
    "default": "github_copilot",
    "background": "github_copilot",
    "think": "github_copilot",
    "longContext": "github_copilot",
    "longContextThreshold": 30000,
    "webSearch": "github_copilot"
  }
}
```

この設定により、ルーターはCopilot APIとのみやり取りし、承認されたエンドポイントのみへの呼び出しを制限するエンタープライズポリシーに準拠します。

---

エンタープライズ環境では、GitHub CopilotのようなLLM APIを統合するには、セキュリティポリシーに従う注意深い設定が必要であり、多くの場合、アウトバウンド呼び出しを特定の承認済みサービスに制限します。提供されたルーター設定は、OpenRouterやLiteLLMのようなツールと同様に、LLMリクエストをプロバイダー間でルーティングするカスタムセットアップのように見えます。ここでは、"Providers"がAPIエンドポイントとモデルを定義し、"Router"がフォールバックまたはカテゴリ固有のルーティングを指示します。これをGitHub CopilotのLLM APIのみを排他的に使用するように適応させるには（他の外部サービスが呼び出されないことを保証するために）、Copilotをプロバイダーとして組み込み、すべてのルーターパスでそれを強制する必要があります。このアプローチは、エンタープライズのファイアウォールやコンプライアンスルールがGitHubがホストするAPIのみを許可するシナリオをサポートし、チャット補完のためのCopilotのOpenAI互換インターフェースを活用します。

GitHub Copilotは、主に2つの経路でLLMアクセスを提供します：エージェントと拡張機能を構築するための専用のCopilot LLMエンドポイントと、一般的な推論のためのより広範なGitHub Models APIです。`https://api.githubcopilot.com/chat/completions`にあるCopilot専用エンドポイントは、エンタープライズグレードのエージェント開発に合わせて調整されており、OpenAIチャット補完形式でのPOSTリクエストをサポートします。認証には、GitHub個人アクセストークン（PAT）から派生したBearerトークンを使用し、通常は`Authorization`ヘッダーを介して渡されます。例えば、サンプルリクエストには、`Authorization: Bearer <your-pat>`や`Content-Type: application/json`のようなヘッダー、および`messages`（ユーザー/システムプロンプトの配列）とリアルタイム応答のための`stream: true`のようなオプションパラメータを含むボディが含まれる場合があります。モデルはドキュメントに明示的にリストされていませんが、GPT-4バリアントやClaudeモデルなど、Copilotの基盤となるプロバイダーと一致し、悪用を防ぐためにサードパーティ製エージェントに厳格なレート制限が適用されます。

あるいは、`https://models.github.ai/inference/chat/completions`にあるGitHub Models APIは、より多目的な推論サービスを提供し、GitHub資格情報のみを使用してモデルのカタログへのアクセスを可能にします。これはプロトタイピングやGitHub Actionsのようなワークフローへの統合に理想的です。認証には`models:read`スコープを持つPATが必要で、GitHub設定（https://github.com/settings/tokens）から作成できます。エンタープライズ設定では、これは組織レベルのトークンに拡張したり、ワークフローYAMLファイルに`permissions: models: read`を追加することでCI/CDパイプラインで使用したりできます。利用可能なモデルには、`openai/gpt-4o`、`openai/gpt-4o-mini`、`anthropic/claude-3-5-sonnet-20240620`、MetaのLlama 3.1シリーズ、Mistralバリアントなどの業界標準が含まれ、これらはすべて同じOpenAI互換のAPI形式で呼び出すことができます。この互換性により、ダウンストリームコードに大きな変更を加えることなく、ルーター設定に簡単に組み込むことができます。

エンタープライズ固有の設定については、GitHub Copilot Enterpriseは、コードベースに基づいたファインチューニングされたモデルなど、組織全体のコントロールで標準のCopilotを強化しますが、APIアクセスは同じパターンに従います。ネットワーク管理が重要です：Copilotトラフィックが承認されたパスを使用するようにサブスクリプションベースのルーティングを設定でき、ユーザーがこれをサポートする最小バージョンにIDE拡張機能（VS Codeなど）を更新する必要があります。環境がプロキシを義務付けている場合は、設定の"PROXY_URL"をエンタープライズプロキシサーバーを指すように更新し、SSL検査用のカスタム証明書を検討してください。LiteLLMのようなツールは、さらなる制御のための仲介プロキシとして機能します—`pip install litellm[proxy]`でインストールし、YAML設定でモデルを定義し、ローカルポートでサーバーを起動し、ロギング、レート制限、フォールバック処理のためにCopilotリクエストをそこにリダイレクトします。ただし、あなたのケースでは目標が排他性であるため、「Copilotのみ呼び出し可」ポリシーに準拠するために、ルーターでのフォールバックは避けてください。

これを設定に実装するには、まず新しいプロバイダーオブジェクトを追加することから始めます。ユースケースに基づいてエンドポイントを選択します：拡張機能を構築する場合はCopilotエージェントエンドポイントを、一般的なLLMルーティングの場合はGitHub Modelsを使用します。互換性を維持するために、既存のモデル（ClaudeやGPTバリアントなど）と重複するモデルをリストします。次に、すべての"Router"フィールドをこの新しいプロバイダーを参照するように上書きし、",minimax/minimax-m2"のようなカンマやフォールバックを排除します。コンプライアンスを監視するためにロギングを有効にし、リクエストをシミュレートしてテストし、未承認のエンドポイントがヒットしていないことを確認します。VS Codeや他のIDEと統合する場合は、必要に応じて`github.copilot.advanced.debug.overrideProxyUrl`のような設定を調整して、設定されたプロキシを経由するようにルーティングします。

以下は、プロバイダー設定で使用するエンドポイントを決定するのに役立つ、2つの主要なGitHub LLM APIオプションの比較表です：

| 観点                      | GitHub Copilot LLM API (エージェント向け)          | GitHub Models API                                   |
|---------------------------|---------------------------------------------------|-----------------------------------------------------|
| エンドポイント            | https://api.githubcopilot.com/chat/completions    | https://models.github.ai/inference/chat/completions |
| 主な用途                  | Copilot拡張機能とエージェントの構築               | 一般的なプロトタイピング、推論、ワークフロー        |
| 認証                      | Bearer PAT (Authorizationヘッダー経由)            | `models:read`スコープを持つPAT                      |
| サポート対象モデル        | 暗黙的 (例: GPT-4, Claudeバリアント)              | 明示的なカタログ: gpt-4o, claude-3-5-sonnet, Llama 3.1など |
| エンタープライズ機能      | サードパーティ向けの厳格なレート制限; Copilot Enterpriseと統合 | GitHub Actionsで使用可能; 独自APIキーの持込サポート |
| レート制限/クォータ       | 非GitHubエージェントに対して厳格                   | プロトタイピング用の無料ティア; エンタープライズ向けにスケーラブル |
| 互換性                    | OpenAIチャット形式                               | OpenAI互換; ルーター統合が容易                     |

この表は、より明示的なモデル選択とエンタープライズワークフロー統合を提供するため、広範なルーター使用にはGitHub Modelsが望ましいかもしれない理由を強調しています。

潜在的な課題には、トークンの有効期限切れ（PATは通常30-90日間有効）が含まれるため、エンタープライズスクリプトで自動更新を設定してください。環境がGitHub Enterprise Cloudを使用している場合は、シームレスなアクセスのために組織レベルでCopilotを有効にします。高度な設定では、GitHubのエコシステム内に留まりながら希望のプロバイダーを経由するために、GitHub Modelsで独自のAPIキーを持ち込む（BYOK）ことを検討してください。機能は急速に進化するため、最新のスコープとエンドポイントについては常に主要なGitHubドキュメントを優先してください。ネットワーク制限により直接API呼び出しが失敗する場合は、GitHubのプロキシ設定オプションを使用するか、ハイブリッドエンタープライズ導入のためにAzureとの統合を検討してください。

まとめると、この設定はあなたのルーターをCopilot専用システムに変え、コード関連または一般的なLLMタスクの機能を維持しながら、エンタープライズポリシーに沿ったものにします。

**主な引用元:**
- [Using GitHub Copilot's LLM for your agent](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-extensions/build-a-copilot-agent/use-copilots-llm)
- [Quickstart for GitHub Models](https://docs.github.com/en/github-models/quickstart)
- [GitHub Copilot | liteLLM](https://docs.litellm.ai/docs/tutorials/github_copilot_integration)
- [Managing GitHub Copilot access to your enterprise's network](https://docs.github.com/enterprise-cloud%40latest/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-access/manage-network-access)
- [Configuring network settings for GitHub Copilot](https://docs.github.com/copilot/configuring-github-copilot/configuring-network-settings-for-github-copilot)
- [Prototyping with AI models](https://docs.github.com/github-models/prototyping-with-ai-models)
- [Using your own API keys in GitHub Models](https://docs.github.com/en/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)