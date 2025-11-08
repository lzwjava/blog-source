---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 翻訳API認証エラー修正
translated: true
type: note
---

### ワークフローとエラー原因の分析

「Translate Recent Notes」のGitHub Actionsワークフローは全体的に適切に構成されています。リポジトリのチェックアウト、Pythonのセットアップ、依存関係のインストール、最新N件の投稿に対する翻訳スクリプトの実行、`_notes/`への変更のコミットという流れです。しかし、先ほど共有いただいたログ（ar、de、frなどの言語への翻訳中の401エラー）に基づくと、問題は`scripts/translation/update_lang_notes.py`内の翻訳API呼び出しにおける認証にあります。

#### 根本原因
- エラー「"No cookie auth credentials found"」（HTTP 401）は、**OpenRouter API**（またはLiteLLMや非公式SDKなどのPythonクライアント/ライブラリ）に特有のものです。これはAPIリクエストに適切な認証ヘッダーが含まれていない場合に発生します。
- OpenRouterはリクエストに`Authorization: Bearer <your_openrouter_api_key>`を期待しています。キーが正しく渡されない場合、一部のクライアントは（クッキーベースのセッション認証が必要であると誤解して）フォールバックし、この正確なエラーを引き起こします。
- あなたのワークフローでは：
  - `OPENROUTER_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}`を設定しており、シークレット値をスクリプトの環境に渡しています。
  - しかし、スクリプトはこの環境変数を正しく読み取っていない、または使用していない可能性が高いです。一般的な不一致：
    - スクリプトは`OPENAI_API_KEY`を期待している（OpenRouterのようなOpenAI互換エンドポイント用）。
    - または、ベースURLを`https://openrouter.ai/api/v1`に設定せずにライブラリ（例：`openai` Python SDK）を使用している。
    - シークレット`DEEPSEEK_API_KEY`が実際にはあなたの**OpenRouter APIキー**（DeepSeek/Grokモデルにルーティング用）を保持している可能性がありますが、もし直接のDeepSeekキーである場合、OpenRouterでは動作しません。
- ログから、スクリプトはモデル`'x-ai/grok-4-fast'`（OpenRouter経由のGrok 4）を使用しており、フロントマター/タイトルは正常に処理していますが、言語ごとのコンテンツ翻訳で失敗しています。
- これはGitHub Actionsの問題ではなく、PythonスクリプトのAPIクライアント設定にあります。ワークフローはコミットステップまで継続します（したがって`git config user.name "github-actions[bot]"`ログが表示されます）が、翻訳がないため、英語ファイルのみが追加されます。

#### 推奨される修正
1. **ワークフロー内の環境変数の更新**:
   - 一般的なOpenRouter設定（OpenAI互換）に合わせます。「Translate posts」ステップの`env`ブロックを以下に変更：
     ```
     env:
       GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
       OPENAI_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}  # スクリプトが期待する変数名に変更
       OPENAI_BASE_URL: https://openrouter.ai/api/v1   # OpenRouterへのルーティングに必須
     ```
   - `DEEPSEEK_API_KEY`があなたのOpenRouterキーであれば問題ありません。もし直接のDeepSeekキーである場合は、リポジトリ設定で新しいシークレット`OPENROUTER_API_KEY`を作成し、実際のOpenRouterキーを設定してください（[openrouter.ai/keys](https://openrouter.ai/keys)で取得）。
   - テスト：ログ内のデバッグ用に`echo $OPENAI_API_KEY`（秘匿化）を実行ステップに追加。

2. **Pythonスクリプト（`update_lang_notes.py`）の修正**:
   - 以下のようにOpenAIクライアントを初期化することを確認（`openai`ライブラリを想定）：
     ```python
     import os
     from openai import OpenAI

     client = OpenAI(
         api_key=os.getenv("OPENAI_API_KEY"),
         base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")  # 未設定時はOpenAIにデフォルト
     )

     # その後、client.chat.completions.create(..., model="x-ai/grok-4-fast")を使用
     ```
   - LiteLLMを使用している場合（マルチプロバイダーで一般的）：`requirements.txt`にない場合はインストールし、`completion(model="openrouter/x-ai/grok-4-fast", api_key=os.getenv("OPENAI_API_KEY"), api_base="https://openrouter.ai/api/v1", ...)`を呼び出し。
   - 翻訳ループについて：言語ごとにエラーハンドリングを追加（例：API呼び出しを`try/except`で囲み、失敗をログに記録、401の場合はスキップ）。
   - クッキーを明示的に処理？おそらく不要です。APIキーに固執してください。スクリプトにブラウザ/Seleniumコードが含まれている場合は、CIの信頼性のために削除。

3. **ワークフローの改善**:
   - **入力検証**: N=0または無効な`--n`をチェックする処理を追加し、何も処理しないことを回避。
   - **条件付きコミット**: `git diff --cached --quiet || git commit`は良いですが、メッセージをすべての言語を反映するように更新：`-m "Add translated posts (ar, de, es, fr, hi, ja, zh, hant)"`。
   - **キャッシング**: `pip`用に`actions/cache`を追加してインストールを高速化。
   - **デバッグモード**: オプションの入力`debug: true`とスクリプトへの`--debug`フラグを追加して詳細なログを出力。
   - **権限**: `github-pages`環境が必要な読み取り/書き込み権限を持っていることを確認。
   - 「Translate posts」ステップの完全な更新済みYAMLスニペット：
     ```
     - name: Translate posts
       run: |
         python scripts/translation/update_lang_notes.py --n ${{ inputs.n }}
       env:
         GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         OPENAI_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
         OPENAI_BASE_URL: https://openrouter.ai/api/v1
     ```

4. **テスト手順**:
   - **ローカルテスト**: 環境変数をエクスポートして（例：`export OPENAI_API_KEY=your_key`）、`python scripts/translation/update_lang_notes.py --n 1`をローカルで実行。
   - **ワークフローテスト**: `workflow_dispatch`でN=1を指定してトリガーし、ログでAPI呼び出しを確認。
   - **シークレットの確認**: リポジトリ設定 > Secretsで、`DEEPSEEK_API_KEY`に有効なOpenRouterキー（`sk-or-...`で始まる）が設定されていることを確認。
   - それでも失敗する場合は、スクリプトに`--verbose`を追加し、リクエストヘッダーを検査（例：`print(client.api_key)`経由）。

これにより401エラーが解決し、翻訳が流れるはずです。`update_lang_notes.py`からのスニペット（例：APIクライアントの初期化部分）を共有いただければ、より正確に特定できます。

#### 参考資料
- [OpenRouterクイックスタート（API認証設定）](https://openrouter.ai/docs/quickstart)
- [LiteLLM OpenRouter統合](https://docs.litellm.ai/docs/providers/openrouter)（使用している場合）
- [類似のOpenRouter認証エラーに関するGitHub Issue](https://github.com/mendableai/firecrawl/issues/1352)
- [OpenRouter 401エラーに関するRedditスレッド](https://www.reddit.com/r/openrouter/comments/1oqiaol/error_401_no_cookie_auth_credentials_found/)