---
audio: false
generated: true
lang: ja
layout: post
title: OpenRouter経由のClaudeアクセス
translated: true
type: note
---

### OpenRouter経由でClaudeモデルを使用する方法（中国ユーザー向け、Anthropic APIアクセスなし）

中国ユーザーは、地域制限によりAnthropicのClaude APIに直接アクセスできない場合があります。しかし、OpenRouterは信頼性の高い代替手段で、AnthropicのClaudeモデルを含む複数のAIプロバイダーへの統一APIゲートウェイとして機能します。OpenRouterは中国でアクセス可能（ウェブサイトもAPIエンドポイントもブロックされていません）で、直接AnthropicアカウントやAPIキーがなくてもClaudeにリクエストをルーティングできます。従量課金制（支払い方法の追加が必要）ですが、登録は無料で、限定使用の無料ティアもサポートしています。

OpenRouterのAPIはOpenAIの形式と互換性があるため、OpenAI Python SDKのような使い慣れたライブラリを使用できます。以下では、ClaudeをPythonで使用するための開始手順とコード例を説明します。

#### ステップ1: OpenRouterにサインアップ
1. OpenRouterウェブサイトにアクセス: https://openrouter.ai
2. 「Sign Up」または「Get Started」をクリック（通常は右上）
3. メールアドレス（またはGitHub/Googleログインが利用可能な場合）を使用してアカウントを作成。サイトは中国で動作するためVPNは不要
4. サインアップ後、必要に応じてメールを確認
5. ダッシュボードに移動し、支払い方法（クレジットカードなど）を追加してアカウントに資金を入金。OpenRouterはトークン使用量に基づいて課金しますが、少額の入金から始められます。Claudeモデルの詳細は価格ページで確認

#### ステップ2: APIキーの生成
1. OpenRouterダッシュボードで「API Keys」または「Keys」セクションに移動
2. 新しいAPIキーを作成（長い文字列、例: `sk-or-v1...`）
3. コピーして安全に保存 - パスワードのように扱ってください。Anthropicキーの代わりにコードで使用します

#### ステップ3: Claudeモデルの選択
OpenRouterで利用可能なAnthropicのClaudeモデルID:
- `anthropic/claude-3.5-sonnet`（ほとんどのタスクに推奨、バランスが取れて高性能）
- `anthropic/claude-3-opus`（より強力だが高価）
- 新しいバージョン（例: 2025年時点でClaude 3.7が利用可能な場合）は https://openrouter.ai/models?providers=anthropic で確認

モデルページでコスト、コンテキスト制限、利用可能性を確認できます

#### ステップ4: 環境のセットアップ
- Pythonをインストール（バージョン3.8以上推奨）
- OpenAIライブラリをインストール: ターミナルで `pip install openai` を実行

#### ステップ5: コードでClaudeを使用
OpenAI SDKをOpenRouterのベースURL（`https://openrouter.ai/api/v1`）で使用。リクエストでClaudeモデルIDを指定します。

Claude 3.5 Sonnetとチャットする簡単なPython例:

```python
from openai import OpenAI

# OpenRouterのエンドポイントとAPIキーでクライアントを初期化
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_API_KEY_HERE",  # 実際のキーに置き換え
)

# Claudeにリクエストを送信
completion = client.chat.completions.create(
    model="anthropic/claude-3.5-sonnet",  # ClaudeモデルIDを使用
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, what is the capital of China?"}
    ],
    temperature=0.7,  # オプション: 創造性を調整（0-1）
    max_tokens=150    # オプション: 応答長を制限
)

# 応答を表示
print(completion.choices[0].message.content)
```

- **説明**: システムプロンプトとユーザーメッセージをClaudeに送信し、応答を取得して表示します。APIキーを置き換え、必要に応じてパラメータを調整
- **OpenAIライブラリを使用しない生のHTTPリクエストを希望する場合**:

```python
import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer YOUR_OPENROUTER_API_KEY_HERE",
        "Content-Type": "application/json"
    },
    data=json.dumps({
        "model": "anthropic/claude-3.5-sonnet",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, what is the capital of China?"}
        ]
    })
)

# 応答を解析して表示
data = response.json()
print(data['choices'][0]['message']['content'])
```

- **ヒント**:
  - `"HTTP-Referer": "your-site-url"` や `"X-Title": "Your App Name"` のようなオプションヘッダーを追加して使用を属性付与（リーダーボードや潜在的な無料クレジットに役立つ）
  - 予期しないコストを避けるため、OpenRouterダッシュボードで使用状況を監視
  - ストリーミング応答や高度な機能（ツールなど）については、OpenRouterの完全なドキュメントを参照
  - レート制限やエラーが発生した場合、残高を確認するか別のモデルを試す

#### トラブルシューティング
- **APIエラー**: キーが正しく資金が十分にあることを確認。まず安価なモデルでテスト
- **地域の問題**: ブロックが発生した場合（可能性は低い）、VPNを使用するが、OpenRouterはサポートモデルに対してそのような制限を回避するように設計されている
- **無料の代替手段**: 限定された無料アクセスの場合、Puter.jsのようなプロキシを探索（ただし制限がある可能性）

このセットアップにより、直接AnthropicアクセスなしでClaudeをプログラムで使用できます。特定のツール（Cursor IDEやMake.comなど）との統合が必要な場合は、それらに関するチュートリアルを検索

参考文献:  
[OpenRouter Documentation](https://openrouter.ai/docs)  
[Anthropic Claude on OpenRouter](https://openrouter.ai/anthropic/claude-3.5-sonnet)  
[Using OpenRouter in China](https://medium.com/ai-simplified-in-plain-english/not-re-inventing-the-wheel-in-ai-2ec3e76ae2bd)  
[How to Use Claude in China](https://www.comparitech.com/blog/vpn-privacy/how-to-use-claude-in-china/)