---
audio: false
generated: true
lang: ja
layout: post
title: プロキシ環境でのVSCode拡張機能インストールのトラブルシューティング
translated: true
type: note
---

Visual Studio Code（VSCode）で拡張機能のインストールログを確認する、またはコマンドラインで `code --install-extension` を使用して拡張機能をインストールし、ログを表示する方法（特にプロキシの問題が疑われる場合）は以下の通りです。

---

### コマンドラインで `code --install-extension` を使用する
拡張機能をコマンドライン経由でインストールし、プロセスを可視化することで、プロキシの問題の診断に役立つ場合があります。

1. **詳細出力を有効にしてインストール**  
   以下のコマンドを実行して、拡張機能をインストールし、より詳細な出力を確認します：
   ```bash
   code --install-extension <extension-id> --verbose
   ```
   - `<extension-id>` は拡張機能のID（例: `vscodevim.vim`）に置き換えてください。
   - `--verbose` フラグは出力の詳細度を増し、プロキシやネットワークの問題などの進捗状況や潜在的なエラーを表示します。

2. **プロキシの問題への対応**  
   プロキシの内側にいる場合、インストールを妨げる可能性があります。以下の方法を試してください：
   - **プロキシ環境変数の設定**:  
     コマンドを実行する前に、プロキシ設定を構成します：
     ```bash
     export HTTP_PROXY=http://your-proxy-server:port
     export HTTPS_PROXY=http://your-proxy-server:port
     code --install-extension <extension-id>
     ```
     - Windowsでは、`export` の代わりに `set` を使用します：
       ```cmd
       set HTTP_PROXY=http://your-proxy-server:port
       set HTTPS_PROXY=http://your-proxy-server:port
       code --install-extension <extension-id>
       ```
   - **プロキシを直接指定**:  
     `--proxy-server` フラグを使用します：
     ```bash
     code --install-extension <extension-id> --proxy-server=http://your-proxy-server:port
     ```

3. **出力の確認**  
   - `--verbose` フラグからのコンソール出力には、インストールの進捗状況やエラー（接続タイムアウトやプロキシ認証失敗など）が表示されます。
   - 注意: コマンドラインインターフェース（`code`）のプロキシサポートはVSCode GUIと比較して限られているため、ログは期待したほど詳細ではない可能性があります。

---

### VSCodeでログを確認する
より詳細なログ（特にインストール試行後）については、VSCodeの組み込みログ機能を使用します：

1. **ログフォルダを開く**  
   - VSCodeを開き、コマンドパレットにアクセスします：
     - `Ctrl+Shift+P`（macOSでは `Cmd+Shift+P`）を押します。
     - **Developer: Open Logs Folder** と入力して選択します。
   - これにより、さまざまなログファイルを含むフォルダが開きます。以下を探してください：
     - **`exthost.log`**: 拡張機能ホストプロセスに関連するログ（インストール試行を含む）。
     - **`sharedprocess.log`**: 拡張機能関連のイベントを含む可能性のある共有プロセスのログ。
   - これらのファイルをテキストエディタで開き、拡張機能ID、ネットワーク問題、またはプロキシ問題に言及するエラーを検索してください。

2. **出力パネルを表示**  
   - VSCodeで、`表示 > 出力` に移動して **出力** パネルを開きます。
   - 右側のドロップダウンメニューで **Extensions** を選択します。
   - これは、VSCode内からのインストール時の拡張機能アクティビティのリアルタイムログを表示します（CLI経由では直接表示されません）。VSCode UIを通じてインストールを再試行すると、ここにプロキシ関連のエラーが表示される可能性があります。

---

### プロキシのトラブルシューティングの追加手順
プロキシの問題が疑われる場合、適切な構成を確保するための追加のヒントを以下に示します：

- **VSCodeでプロキシを構成**  
  - VSCode設定を開きます（`ファイル > 基本設定 > 設定` または `Ctrl+,`）。
  - `proxy` を検索し、設定します：
    ```json
    "http.proxy": "http://your-proxy-server:port"
    ```
  - 必要に応じて、`"http.proxyStrictSSL"`（必要に応じて `false` に設定）または `"http.proxyAuthorization"`（認証プロキシ用）を調整します。
  - これらの設定は、CLIではなくVSCode内でのインストールに適用されます。

- **ネットワークアクセスのテスト**  
  - プロキシがVSCode Marketplaceへのアクセスを許可しているか手動でテストします：
    - 拡張機能のVSIXファイルのURLを探します（例: Marketplace Webサイトから）。
    - `curl` などのツールを使用します：
      ```bash
      curl -x http://your-proxy-server:port <vsix-url>
      ```
    - これが失敗した場合、プロキシが接続をブロックしている可能性があります。

---

### 推奨アプローチ
- **CLIインストールの場合**: `code --install-extension <extension-id> --verbose` をプロキシ環境変数または `--proxy-server` と共に使用し、即時の出力を確認します。ターミナルでのエラーをチェックします。
- **詳細なログの場合**: 拡張機能をVSCode UI（Marketplace）経由でインストールし、**出力 > Extensions** パネルまたはログフォルダ（`exthost.log`）を確認します。
- **プロキシチェック**: システムとVSCodeの両方でプロキシ設定が正しいことを確認します。

この組み合わせにより、進捗状況を監視し、プロキシの問題を効果的に診断できます。CLI出力が不十分な場合、VSCodeログは問題の原因についてより深い洞察を提供します。