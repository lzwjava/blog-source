---
audio: false
generated: true
lang: ja
layout: post
title: VS Code で GitHub Copilot を使い始める
translated: true
type: note
---

Visual Studio Code（VS Code）でGitHub Copilotを使用するのは、一度セットアップしてしまえば簡単です。以下は、2025年3月20日現在の開始手順です：

---

### ステップ 1: VS Codeのインストール
- Visual Studio Codeがインストールされていることを確認してください。まだの場合は、[code.visualstudio.com](https://code.visualstudio.com/)からダウンロードしてください。
- 最適な互換性のために、VS Codeを最新バージョンに更新してください（`ヘルプ > 更新プログラムを確認` に移動）。

---

### ステップ 2: GitHub Copilot拡張機能のインストール
1.  **VS Codeを開きます**。
2.  **拡張機能マーケットプレイスに移動します**：
    - 左側のアクティビティバーにある拡張機能アイコンをクリックするか（Macでは `Ctrl+Shift+X` / `Cmd+Shift+X` を押します）。
3.  **"GitHub Copilot"を検索します**：
    - 検索バーに「GitHub Copilot」と入力します。
    - GitHubによる公式拡張機能（確認済みバッジが付いています）を探します。
4.  **拡張機能をインストールします**：
    - 「GitHub Copilot」の横にある`インストール`ボタンをクリックします。
5.  **オプション: Copilot Chatをインストール（推奨）**：
    - 「GitHub Copilot Chat」を検索してインストールします。これにより、チャットで質問したりコードを生成したりする会話型AI機能が追加されます。

---

### ステップ 3: GitHub Copilotにサインイン
1.  **GitHubで認証します**：
    - インストール後、サインインを求めるプロンプトが表示されます。
    - ポップアップで`Sign in to GitHub`をクリックするか、VS Codeの右下隅にあるCopilotステータスアイコンに移動して「Sign in」を選択します。
2.  **ブラウザで承認します**：
    - GitHubアカウントへのログインを求めるブラウザウィンドウが開きます。
    - `Authorize Git hypoxia`をクリックして承認リクエストを承認します。
3.  **コードをコピーします**：
    - GitHubはワンタイムコードを提供します。それをコピーし、VS Codeで要求されたときに貼り付けます。
4.  **アクティベーションを確認します**：
    - サインインすると、ステータスバーのCopilotアイコンが緑色に変わり、アクティブであることを示します。アクセスが確認されたことを示す通知も表示されます。

---

### ステップ 4: Copilotの設定（オプション）
- **提案の有効/無効**：
  - `ファイル > 基本設定 > 設定`（または `Ctrl+,` / `Cmd+,`）に移動します。
  - 「Copilot」を検索して、インライン提案の有効化や特定の言語での無効化などの設定を調整します。
- **サブスクリプションを確認**：
  - Copilotは30日間の無料トライアル後、サブスクリプション（月額10ドルまたは年間100ドル）が必要です。学生、教師、オープンソースメンテナは、[GitHub Education](https://education.github.com/)またはCopilot設定から無料アクセスを申請できます。

---

### ステップ 5: Copilotの使用開始
コーディングワークフローでCopilotを活用する方法は以下の通りです：

#### 1. **コード提案**
- **インラインオートコンプリート**：
  - ファイルで入力を開始すると（例: Pythonで `def calculate_sum(`）、Copilotは灰色のテキストで補完を提案します。
  - 提案を受け入れるには`Tab`を押し、無視するには入力を続けます。
- **複数行の提案**：
  - `// Function to sort an array`のようなコメントを書いてEnterキーを押します。Copilotは実装全体（ソートアルゴリズムなど）を提案する場合があります。
  - `Alt+]`（Macでは`Option+]`）を使用して、複数の提案を循環表示します。

#### 2. **コメントからのコード生成**
- 以下のような説明的なコメントを入力します：
  ```javascript
  // Fetch data from an API and handle errors
  ```
  Enterキーを押すと、Copilotは以下を生成する場合があります：
  ```javascript
  async function fetchData(url) {
    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error('Network response was not ok');
      return await response.json();
    } catch (error) {
      console.error('Fetch error:', error);
    }
  }
  ```
- `Tab`で受け入れるか、必要に応じて調整します。

#### 3. **Copilot Chat（インストール済みの場合）**
- **チャットを開く**：
  - サイドバーのチャットアイコンをクリックするか、`Ctrl+Alt+C`（カスタマイズ可能）を使用します。
- **質問する**：
  - 「JavaScriptでのPromiseの仕組みを説明してください」や「CSVファイルを読み取るPythonスクリプトを書いてください」などと入力します。
  - Copilotはチャットパネルで応答し、コードを直接エディタに挿入できます。
- **コンテキストヘルプ**：
  - コードをハイライトし、右クリックして「Ask Copilot」を選択すると、説明やリファクタリングを行います。

#### 4. **デバッグとテスト**
- `// Write unit tests for this function`のようなコメントを書くと、CopilotはJestやPyTestなどのフレームワークを使用してテストケースを生成できます。

---

### 効果的な使用のためのヒント
- **具体的に記述する**：提供するコンテキスト（コメント、変数名など）が多ければ多いほど、Copilotの提案は向上します。
- **提案を確認する**：Copilotは完璧ではありません。正確性とセキュリティのために、そのコードを常に確認してください。
- **言語サポート**：人気のある言語（Python、JavaScript、Javaなど）で最も効果的に機能しますが、数十の言語をサポートしています。
- **キーボードショートカット**：
  - `Alt+\`（Macでは`Option+\`）：すべての提案を手動で表示します。
  - `Ctrl+Enter`：提案パネルを開きます。

---

### トラブルシューティング
- **動作しない？**：
  - サインインしていることを確認してください（ステータスバーを確認）。
  - GitHubアカウント設定でサブスクリプションがアクティブであることを確認してください。
  - 問題が解決しない場合は、VS Codeを再起動するか、拡張機能を再インストールしてください。
- **提案が表示されない？**：
  - 現在の言語でCopilotが有効になっているか確認してください（設定で`editor.inlineSuggest.enabled`がtrueである必要があります）。

---

以上です！これでVS CodeでGitHub Copilotを使用する準備が整いました。ファイルを開き、コードやコメントを入力して、Copilotに支援してもらいましょう。スマートなコーディングをお楽しみください！