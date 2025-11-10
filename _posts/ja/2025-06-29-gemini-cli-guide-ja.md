---
audio: false
generated: true
lang: ja
layout: post
title: Gemini CLIのインストールと使用方法
translated: true
type: note
---

**Google Gemini CLI ガイド**

以下は、**Google Gemini CLI**（Geminiの機能をターミナルに統合し、コーディング、タスク自動化などを可能にするオープンソースのAIエージェント）のインストール、セットアップ、使用方法に関する簡潔なガイドです。このガイドは、2025年6月29日時点で利用可能な最新情報に基づいています。

---

## **Google Gemini CLI ガイド**

### **Gemini CLI とは？**
Gemini CLI は、Googleによって開発されたオープンソースのコマンドラインツールで、Gemini 2.5 Proモデル（100万トークンのコンテキストウィンドウ）のパワーをターミナルにもたらします。コーディング、デバッグ、コンテンツ生成、タスク自動化、画像や動画生成などのマルチモーダルタスクをサポートします。Googleアカウントで無料で利用でき、Google SearchやModel Context Protocol (MCP) サーバーなどのツールと統合できます。

---

### **前提条件**
- **Node.js**: バージョン18以上。`node -v`で確認。必要に応じて [nodejs.org](https://nodejs.org) からインストール。
- **Googleアカウント**: Gemini 2.5 Proへの無料アクセスに必要（60リクエスト/分、1,000リクエスト/日）。
- (オプション) **APIキー**: より高い制限や特定のモデルを使用する場合、[Google AI Studio](https://aistudio.google.com) から生成。
- (オプション) **Docker**: MCPサーバー統合（例：GitHubツール）に必要。

---

### **インストール**
Gemini CLIを始めるには2つの方法があります：

1. **グローバルインストール**:
   ```bash
   npm install -g @google/gemini-cli
   gemini
   ```
   これによりCLIがグローバルにインストールされ、`gemini`コマンドで実行されます。

2. **インストールなしで実行**:
   ```bash
   npx https://github.com/google-gemini/gemini-cli
   ```
   これはインストールせずに直接CLIを実行する方法で、テストに最適です。

---

### **セットアップ**
1. **CLIの起動**:
   - ターミナルで `gemini` を実行。
   - 初回起動時、テーマ（例：ASCII、dark、light）を選択しEnterを押す。

2. **認証**:
   - 無料アクセスのためには **Login with Google** を選択（ほとんどのユーザーに推奨）。
   - ブラウザウィンドウが開くので、Googleアカウントでサインイン。
   - あるいは、APIキーを使用：
     - [Google AI Studio](https://aistudio.google.com) からキーを生成。
     - 環境変数として設定：
       ```bash
       export GEMINI_API_KEY=YOUR_API_KEY
       ```
     - これはより高い制限やエンタープライズ用途に有用。

3. **プロジェクトへの移動**:
   - コード関連タスクのコンテキストを提供するため、プロジェクトのルートディレクトリで `gemini` を実行。

---

### **基本的な使用方法**
Gemini CLIは対話型のRead-Eval-Print Loop (REPL) 環境で動作します。コマンドや自然言語のプロンプトを入力してGeminiモデルと対話します。以下は一般的なタスクの例です：

1. **コードの説明**:
   - プロジェクトフォルダに移動して実行：
     ```bash
     gemini
     ```
   - プロンプト: `このプロジェクトのアーキテクチャを説明して` または `main.pyのmain関数について説明して`。
   - CLIはファイルを読み、構造化された説明を提供します。

2. **コード生成**:
   - プロンプト: `HTML、CSS、JavaScriptでシンプルなToDoアプリを作成して`。
   - CLIはコードを生成し、要求に応じてファイルに保存できます。

3. **デバッグ**:
   - エラーメッセージやスタックトレースを貼り付け、`このエラーの原因は何？`と質問。
   - CLIはエラーを分析し、修正を提案します。追加のコンテキストのためにGoogle Searchを使用する可能性があります。

4. **ファイル管理**:
   - プロンプト: `PDFの請求書を支出月ごとに整理して`。
   - CLIはファイルを操作したり、形式を変換（例：画像をPNGに）できます。

5. **GitHub連携**:
   - GitHubタスク（例：Issueの一覧表示）にMCPサーバーを使用：
     - Personal Access Token (PAT) を使用して、`.gemini/settings.json`でGitHub MCPサーバーを設定。
     - プロンプト: `foo/barリポジトリで自分にアサインされている全てのオープンなIssueを取得して`。
   - `/mcp`を実行して設定済みのMCPサーバーとツールを一覧表示。

6. **マルチモーダルタスク**:
   - ImagenやVeoなどのツールでメディアを生成：
     - プロンプト: `Veoを使用して、オーストラリアでの猫の冒険の短い動画を作成して`。

---

### **主な機能**
- **コンテキストファイル (GEMINI.md)**: プロジェクトのルートに`GEMINI.md`ファイルを追加して、コーディングスタイル、プロジェクトルール、または設定（例：「JavaScriptではasync/awaitを使用する」）を定義。CLIはこれを使用して調整された応答を提供します。
- **組み込みツール**:
   - `/tools`: 利用可能なツール（例：Google Search、ファイル操作）を一覧表示。
   - `/compress`: チャットのコンテキストを要約してトークンを節約。
   - `/bug`: Gemini CLI GitHubリポジトリに直接Issueを登録。
- **非対話型モード**: スクリプト用に、コマンドをパイプ：
   ```bash
   echo "Pythonスクリプトを書いて" | gemini
   ```
- **会話メモリ**: `/save <tag>`でセッション履歴を保存し、`/restore <tag>`で再開。
- **カスタム設定**:
   - グローバル設定には`~/.gemini/settings.json`を、プロジェクト固有の設定には`.gemini/settings.json`を編集。
   - 例：MCPサーバーやカスタムテーマの設定。

---

### **ヒントとテクニック**
- **計画から始める**: 複雑なタスクでは、まず計画を要求：`ログインシステムの詳細な実装計画を作成して`。これにより構造化された出力が保証されます。
- **ローカルコンテキストを使用**: より高速で信頼性の高い応答のために、MCPサーバーに依存する代わりに、プロジェクト固有の詳細を`GEMINI.md`にエンコード。
- **デバッグ**: `DEBUG=true gemini`で詳細なログを有効化し、リクエスト/レスポンス情報を確認。
- **変更の確認**: ファイル変更やコマンド実行前には常にレビュー（確認には`y`と入力）。
- **ツールの探索**: `/tools`を実行して、ウェブ検索やメモリ保存などの組み込み機能を発見。

---

### **トラブルシューティング**
- **認証の問題**: GoogleアカウントまたはAPIキーが有効であることを確認。`/auth`で方法を切り替え。
- **レート制限**: 無料ティアでは60リクエスト/分、1,000回/日が許可されます。より高い制限には、APIキーまたはVertex AIを使用。
- **エラー**: GitHubの [トラブルシューティングガイド](https://github.com/google-gemini/gemini-cli/docs/troubleshooting.md) を確認。
- **応答が遅い**: CLIはプレビュー段階であり、API呼び出しで遅くなる可能性があります。GitHubでフィードバックを提出。

---

### **高度な使用方法**
- **MCPサーバー統合**:
  - リポジトリ操作のためにGitHub MCPサーバーを設定：
    - 必要なスコープを持つGitHub PATを作成。
    - `.gemini/settings.json`に追加：
      ```json
      {
        "mcpServers": [
          {
            "name": "github",
            "url": "http://localhost:8080",
            "type": "github"
          }
        ]
      }
      ```
    - MCPサーバーのためにDockerコンテナを実行（GitHubドキュメント参照）。
- **スクリプティング**: Gemini CLIをスクリプトに統合してタスクを自動化：
  ```bash
  gemini --non-interactive "ファイルをバックアップするbashスクリプトを生成して"
  ```
- **マルチモーダルプロンプト**:
  - 例: `この画像を説明して: path/to/image.jpg` (`gemini-pro-vision`などの画像認識対応モデルが必要)。

---

### **制限事項**
- **プレビュー段階**: Gemini CLIは一般提供前の段階であり、サポートが限定的であったりバグが発生する可能性があります。
- **完全なオープンソースではない**: CLI UIのみがApache 2.0ライセンスであり、Geminiモデルはプロプライエタリです。
- **クォータ共有**: 制限はGemini Code Assistを使用している場合、それと共有されます。
- **将来の価格設定**: プレビュー後の価格は不明確であり、高度な機能には支払いが必要になる可能性があります。

---

### **リソース**
- **公式GitHub**: [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- **ドキュメント**: [gemini-cli.click](https://gemini-cli.click) または GitHub docs
- **ブログ発表**: [blog.google](https://blog.google)
- **フィードバック**: GitHubでバグや提案を提出。

---

### **使用例ワークフロー**
1. インストール: `npm install -g @google/gemini-cli`
2. 実行: `cd my-project && gemini`
3. 認証: Googleでログイン。
4. プロンプト: `FastAPIを使用したREST APIのPythonスクリプトを書いて`。
5. 生成されたコードをレビューして保存。
6. `/tools`を使用してGitHub連携などの追加機能を探索。

---

Gemini CLIは、ターミナルでのシームレスなAI統合を提供する、開発者向けの強力なツールです。シンプルに始め、コンテキストのために`GEMINI.md`を活用し、生産性を高めるためにそのマルチモーダル機能を探索してください。より多くの例については、[GitHubチュートリアル](https://github.com/google-gemini/gemini-cli/docs/cli/tutorials.md)を確認してください。

特定の例が必要な場合や、特定の機能について質問がある場合は、お知らせください！