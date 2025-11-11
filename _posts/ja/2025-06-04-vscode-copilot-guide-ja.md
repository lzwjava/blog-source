---
audio: false
generated: true
lang: ja
layout: post
title: Visual Studio CodeでのGitHub Copilotの使い方
translated: true
type: note
---

GitHub Copilotは、GitHubとOpenAIが共同開発したAI搭載のコーディングアシスタントで、Visual Studio Code（VS Code）における開発者の生産性向上を目的としています。コンテキストを考慮したコード補完、自然言語チャット、高度な編集機能を提供します。このガイドでは、Copilotのセットアップ、機能の探索、そしてヒントとベストプラクティスを用いたワークフローの最適化について説明します。

## 1. GitHub Copilotの紹介
GitHub Copilotは、AIを活用したペアプログラマーとして機能し、リアルタイムのコード提案、コーディングに関する質問への回答、反復的なタスクの自動化を提供します。公開された膨大なコードデータセットでトレーニングされた大規模言語モデルによって駆動されており、Python、JavaScript、TypeScript、Ruby、Go、C#、C++など、多数のプログラミング言語とフレームワークをサポートします。

主な機能:
- **コード補完**: 入力中に、単一行から関数全体までのコードスニペットを提案します。
- **Copilot チャット**: 自然言語クエリを使用して、コードの説明、スニペットの生成、デバッグを行うことができます。
- **エージェントモード**: リファクタリングやアプリ作成など、複数ステップのコーディングタスクを自動化します。
- **カスタム指示**: 提案をあなたのコーディングスタイルやプロジェクト要件に合わせて調整します。

## 2. VS CodeでのGitHub Copilotセットアップ

### 前提条件
- **VS Code**: [公式ウェブサイト](https://code.visualstudio.com/)からVisual Studio Codeをダウンロードしてインストールします。互換性のあるバージョン（Copilotをサポートする最近のバージョン）であることを確認してください。
- **GitHub アカウント**: CopilotにアクセスできるGitHubアカウントが必要です。オプションは以下の通りです:
  - **Copilot Free**: 月間の補完とチャットのやり取りが制限されます。
  - **Copilot Pro/Pro+**: 制限が緩和され、高度な機能を利用できる有料プラン。
  - **組織でのアクセス**: 組織から提供されている場合は、管理者に詳細を確認してください。
- **インターネット接続**: Copilotは提案を提供するためにアクティブな接続を必要とします。

### インストール手順
1. **VS Codeを開く**:
   お使いのマシンでVisual Studio Codeを起動します。

2. **GitHub Copilot拡張機能をインストール**:
   - **拡張機能**ビュー（Ctrl+Shift+X または macOSでは Cmd+Shift+X）に移動します。
   - 拡張機能マーケットプレイスで "GitHub Copilot" を検索します。
   - 公式のGitHub Copilot拡張機能の**インストール**をクリックします。これによりCopilot Chat拡張機能も自動的にインストールされます。

3. **GitHubにサインイン**:
   - インストール後、VS Codeのステータスバー（右下隅）にCopilotのセットアップを促すプロンプトが表示される場合があります。
   - Copilotアイコンをクリックし、**Sign in**を選択してGitHubアカウントで認証します。
   - プロンプトが表示されない場合は、コマンドパレット（Ctrl+Shift+P または Cmd+Shift+P）を開き、`GitHub Copilot: Sign in` コマンドを実行します。
   - ブラウザベースの認証フローに従い、VS Codeから提供されたコードをGitHubにコピーします。

4. **アクティベーションを確認**:
   - サインイン後、ステータスバーのCopilotアイコンが緑色に変わり、アクティブ状態であることを示します。
   - Copilotサブスクリプションをお持ちでない場合、月間使用量が制限されたCopilot Freeプランに登録されます。

5. **オプション: テレメトリを無効にする**:
   - デフォルトでは、Copilotはテレメトリデータを収集します。無効にするには、**設定**（Ctrl+, または Cmd+,）に移動し、`telemetry.telemetryLevel`を検索して`off`に設定します。または、`GitHub Copilot Settings`でCopilot固有の設定を調整します。

> **注意**: 組織でCopilot Chatが無効化されている、または機能が制限されている場合は、管理者に連絡してください。トラブルシューティングについては、[GitHub Copilotトラブルシューティングガイド](https://docs.github.com/ja/copilot/troubleshooting)を参照してください。[](https://code.visualstudio.com/docs/copilot/setup)

## 3. VS CodeでのGitHub Copilotのコア機能

### 3.1 コード補完
Copilotは、コードのコンテキストとファイル構造に基づいて、入力中に単一行から関数やクラス全体までのコードを提案します。
- **仕組み**:
  - サポートされている言語（例: JavaScript、Python、C#）で入力を開始します。
  - Copilotは提案を灰色の「ゴーストテキスト」で表示します。
  - 提案を受け入れるには**Tab**を押すか、入力を続けて無視します。
  - 複数の提案がある場合は、**Alt+]**（次）または**Alt+[**（前）を使用して切り替えます。
- **例**:
  ```javascript
  // 数値の階乗を計算する
  function factorial(n) {
  ```
  Copilotは以下を提案するかもしれません:
  ```javascript
  if (n === 0) return 1;
  return n * factorial(n - 1);
  }
  ```
  **Tab**を押して提案を受け入れます。

- **ヒント**:
  - Copilotを導くために説明的な関数名やコメントを使用します（例: `// 配列を昇順でソートする`）。
  - 複数の提案がある場合は、提案にマウスを合わせて補完パネル（Ctrl+Enter）を開き、すべてのオプションを表示します。

### 3.2 Copilot チャット
Copilot Chatを使用すると、自然言語でCopilotと対話し、質問をしたり、コードを生成したり、デバッグを行ったりできます。
- **チャットへのアクセス**:
  - アクティビティバーから**チャットビュー**を開くか、**Ctrl+Alt+I**（Windows/Linux）または**Cmd+Ctrl+I**（macOS）を使用します。
  - または、エディター内で直接**インラインチャット**（Ctrl+I または Cmd+I）を使用して、コンテキスト固有のクエリを実行します。
- **使用例**:
  - **コードの説明**: コードブロックを選択し、インラインチャットを開き、`explain this code`と入力します。
  - **コード生成**: チャットビューで`write a Python function to reverse a string`と入力します。
  - **デバッグ**: エラーメッセージをチャットに貼り付け、修正を依頼します。
- **例**:
  チャットビューで、以下を入力します:
  ```
  What is recursion?
  ```
  Copilotは、多くの場合Markdownでコード例を含む詳細な説明で応答します。

- **スラッシュコマンド**:
  `/explain`、`/doc`、`/fix`、`/tests`、`/optimize`などのコマンドを使用してタスクを指定します。例:
  ```
  /explain this function
  ```
  関数が選択されている状態で実行すると、詳細な説明が生成されます。

### 3.3 エージェントモード (プレビュー)
エージェントモードでは、Copilotがアプリの作成、コードのリファクタリング、テストの記述など、複数ステップのコーディングタスクを自律的に処理できます。
- **使用方法**:
  - VS Code InsidersまたはStable（利用可能な場合）で**Copilot Edits View**を開きます。
  - モードドロップダウンから**Agent**を選択します。
  - プロンプトを入力します（例: `Create a React form component with name and email fields`）。
  - Copilotはコードベースを分析し、編集を提案し、ターミナルコマンドやテストを実行できます。
- **能力**:
  - 複数ファイルにわたるコードの生成。
  - エラーの監視と問題修正のための反復。
  - 新しいライブラリの統合やモダンフレームワークへのコード移行。

> **注意**: エージェントモードは実験的であり、小規模なリポジトリで最高のパフォーマンスを発揮します。フィードバックはVS CodeのGitHubリポジトリ経由で共有してください。[](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)

### 3.4 カスタム指示
Copilotをカスタマイズして、コーディングスタイルやプロジェクト要件に合わせます。
- **セットアップ**:
  - ワークスペースに`.github/copilot-instructions.md`ファイルを作成します。
  - Markdown形式で指示を追加します（例: `Use snake_case for Python variable names`）。
  - **設定** > **GitHub** > **Copilot** > **Enable custom instructions**（VS Code 17.12以降）でカスタム指示を有効にします。
- **例**:
  ```markdown
  # Copilotカスタム指示
  - JavaScript変数にはキャメルケースを使用する。
  - プロミスには.then()よりもasync/awaitを優先する。
  ```
  Copilotはこれらの設定に合わせて提案を調整します。

### 3.5 @workspaceによるワークスペースコンテキスト
`@workspace`コマンドを使用して、コードベース全体に対してクエリを実行します。
- **例**:
  チャットビューで、以下を入力します:
  ```
  @workspace Where is the database connection string configured?
  ```
  Copilotはワークスペースを検索し、関連するファイルを参照します。

### 3.6 次の編集提案 (プレビュー)
Copilotは、最近の変更に基づいて、次に行う論理的な編集を予測し提案します。
- **仕組み**:
  - コードを編集すると、Copilotは潜在的な次の編集をハイライト表示します。
  - **Tab**で提案を受け入れるか、インラインチャットで修正します。
- **使用例**: 反復的なリファクタリングや関連するコード変更の完了に最適です。

## 4. Copilot使用を最適化するためのヒントとコツ

### 4.1 効果的なプロンプトの書き方
- 具体的に: `write a function`ではなく、`write a Python function to sort a list of dictionaries by the 'age' key`のように試してみてください。
- コンテキストを提供: フレームワークやライブラリの詳細を含めます（例: `use React hooks`）。
- コメントを使用: `// Generate a REST API endpoint in Express`と書いて補完を導きます。

### 4.2 コンテキストの活用
- **ファイル/シンボルの参照**: チャットプロンプトで`#filename`、`#folder`、`#symbol`を使用してコンテキストの範囲を限定します。
  ```
  /explain #src/utils.js
  ```
- **ドラッグ＆ドロップ**: ファイルやエディタタブをチャットプロンプトにドラッグしてコンテキストを追加します。
- **画像の添付**: VS Code 17.14 Preview 1以降では、スクリーンショットを添付して問題（例: UIバグ）を説明できます。

### 4.3 スラッシュコマンドの使用
- `/doc`: 関数のドキュメントを生成します。
- `/fix`: エラーに対する修正を提案します。
- `/tests**: 選択したコードの単体テストを作成します。
- 例:
  ```
  /tests Generate Jest tests for this function
  ```

### 4.4 プロンプトの保存と再利用
- `.github/prompts/`ディレクトリに`.prompt.md`ファイルを作成して、再利用可能なプロンプトを保存します。
- 例:
  ```markdown
  # Reactコンポーネントプロンプト
  Tailwind CSSスタイリングを施したReact関数コンポーネントを生成します。コンポーネント名とpropsが提供されていない場合は尋ねてください。
  ```
  - チャットでプロンプトを添付して、プロジェクト間で再利用します。

### 4.5 適切なモデルの選択
- Copilotは複数の言語モデル（例: GPT-4o、Claude Sonnet）をサポートしています。
  - チャットビューのドロップダウンでモデルを選択し、コーディング速度や深い推論を行います。
  - 複雑なタスクでは、Claude Sonnetがエージェントモードでより優れたパフォーマンスを発揮する場合があります。[](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)

### 4.6 ワークスペースのインデックス作成
- ワークスペースのインデックス作成を有効にして、コード検索をより速く、正確にします。
- GitHubリポジトリにはリモートインデックスを、大規模なコードベースにはローカルインデックスを使用します。

## 5. ベストプラクティス
- **提案の確認**: Copilotの提案が正確でプロジェクトの標準に沿っているか常に確認してください。
- **IntelliCodeとの併用**: Visual Studioでは、CopilotはIntelliCodeを補完し、強化された補完を実現します。[](https://devblogs.microsoft.com/visualstudio/github-copilot-in-visual-studio-2022/)
- **セキュリティの確認**: Copilotは脆弱性を含むコードを提案する可能性があります。特に機密性の高いプロジェクトでは提案を確認し、組織のポリシーをチェックしてください。[](https://medium.com/%40codebob75/how-to-use-copilot-in-visual-studio-a-step-by-step-guide-b2a5db3b54ba)
- **意味のある名前の使用**: 説明的な変数名と関数名は、提案の品質を向上させます。
- **チャットでの反復**: 最初の提案が的外れな場合は、プロンプトを洗練させてください。
- **使用制限の監視**: Copilot Freeでは、GitHubアカウント設定またはVS CodeのCopilotバッジを通じて、月間の補完とチャットのやり取りを追跡してください。[](https://learn.microsoft.com/ja-jp/visualstudio/ide/copilot-free-plan?view=vs-2022)

## 6. 一般的な問題のトラブルシューティング
- **Copilotが非アクティブ**: CopilotにアクセスできるGitHubアカウントでサインインしていることを確認してください。Copilotステータスバードロップダウンから資格情報を更新します。
- **提案がない**: インターネット接続を確認するか、サポートされている言語に切り替えてください。**ツール** > **オプション** > **GitHub Copilot**で設定を調整します。
- **機能制限**: Copilot Freeの使用制限に達した場合、IntelliCodeの提案に戻ります。有料プランにアップグレードするか、ステータスを確認してください。[](https://learn.microsoft.com/ja-jp/visualstudio/ide/copilot-free-plan?view=vs-2022)
- **ネットワーク問題**: [GitHub Copilotトラブルシューティングガイド](https://docs.github.com/ja/copilot/troubleshooting)を参照してください。

## 7. 高度な使用例
- **データベースクエリ**: CopilotにSQLクエリの生成を依頼します（例: `Write a SQL query to join two tables`）。
- **API開発**: APIエンドポイントコードのリクエスト（例: `Create a Flask route to handle POST requests`）。
- **単体テスト**: `/tests`を使用して、JestやPytestなどのフレームワーク向けのテストを生成します。
- **リファクタリング**: エージェントモードを使用して、ファイル間でコードをリファクタリングします（例: `Migrate this jQuery code to React`）。

## 8. プライバシーとセキュリティの考慮事項
- **データ使用**: Copilotは提案を生成するためにコードスニペットをGitHubサーバーにリアルタイムで送信しますが、保持しません（Copilot for Businessはスニペットを即座に破棄します）。[](https://medium.com/%40codebob75/how-to-use-copilot-in-visual-studio-a-step-by-step-guide-b2a5db3b54ba)
- **公開コードの一致**: Copilotは公開GitHubリポジトリと一致するコードを提案する可能性があります。コード参照を有効にしてライセンスの詳細を表示します。[](https://learn.microsoft.com/ja-jp/visualstudio/ide/visual-studio-github-copilot-extension?view=vs-2022)
- **組織のポリシー**: 組織によってはCopilotの使用を許可していない場合があり、チャットが無効化されていたり、提案が制限されていたりする可能性があるため、確認してください。[](https://docs.github.com/ja/copilot/quickstart)
- **テレメトリ**: 必要に応じてVS Code設定でテレメトリを無効にします。[](https://code.visualstudio.com/docs/copilot/setup)

## 9. さらなる学習のためのリソース
- [GitHub Copilot ドキュメント](https://docs.github.com/ja/copilot)
- [VS Code Copilot クイックスタート](https://code.visualstudio.com/docs/copilot/copilot-quickstart)
- [Copilot Chat チュートリアル](https://code.visualstudio.com/docs/copilot/copilot-chat)
- [VS Code Copilot シリーズ on YouTube](https://www.youtube.com/playlist?list=PLj6YeMhvp2S6X0vF4TrRkpZ7GIqM3oPWp)
- [GitHub Copilot FAQ](https://docs.github.com/ja/copilot/faq)

## 10. 結論
VS CodeにおけるGitHub Copilotは、インテリジェントな提案の提供、質問への回答、複雑なタスクの自動化を通じて、コーディングを効率化する強力なツールです。正しくセットアップし、その機能を活用し、ベストプラクティスに従うことで、生産性を大幅に向上させ、創造的なコーディングタスクに集中できます。Copilotの能力を試し、ワークフローに合わせてカスタマイズし、セキュリティと使用制限に注意を払うことで、このAIペアプログラマーを最大限に活用してください。