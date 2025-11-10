---
audio: false
generated: true
lang: ja
layout: post
title: GitHub CLIのインストール
translated: true
type: note
---

Ubuntu で GitHub CLI (`gh`) をインストールし、`gh workflow run` コマンドを使用して GitHub Actions ワークフローをトリガーするには、以下の手順に従ってください。

### Ubuntu での GitHub CLI (`gh`) インストール手順

1. **GitHub CLI リポジトリと GPG キーを追加**:
   以下のコマンドをターミナルで実行し、公式 GitHub CLI パッケージリポジトリをセットアップします：

   ```bash
   (type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
   && sudo mkdir -p -m 755 /etc/apt/keyrings \
   && wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
   && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
   && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
   ```

   このスクリプトは以下を行います：
   - `wget` がまだインストールされていない場合、インストールします。
   - APT キーリング用のディレクトリを作成します。
   - GitHub CLI GPG キーをダウンロードして追加します。
   - システムに GitHub CLI リポジトリを設定します。

2. **パッケージインデックスを更新し `gh` をインストール**:
   パッケージリストを更新し、`gh` コマンドラインツールをインストールします：

   ```bash
   sudo apt update
   sudo apt install gh -y
   ```

3. **インストールを確認**:
   以下のコマンドを実行して `gh` が正しくインストールされたことを確認します：

   ```bash
   gh --version
   ```

   `gh version X.Y.Z (YYYY-MM-DD)` のような出力が表示され、インストールが確認されます。

4. **GitHub で認証**:
   `gh` を使用する前に、GitHub アカウントで認証します：

   ```bash
   gh auth login
   ```

   プロンプトに従います：
   - `GitHub.com`（または該当する場合はエンタープライズサーバー）を選択します。
   - 優先するプロトコル（`HTTPS` または `SSH`；SSH キーが設定されている場合は `SSH` が推奨）を選択します。
   - 認証方法を選択します（ブラウザが最も簡単です。ログインするためのウェブページが開きます）。
   - 提供されたワンタイムコードをコピーし、ブラウザに貼り付けて `gh` を承認します。
   - デフォルト設定を確認するか、必要に応じて調整します。

   認証が成功すると、確認メッセージが表示されます。

### GitHub Actions での `gh workflow run` の使用方法

`gh workflow run` コマンドは GitHub Actions ワークフローをトリガーします。使用方法は以下の通りです：

1. **リポジトリに移動**（オプション）:
   ローカルの Git リポジトリ（GitHub にリンクされている）内にいる場合、`gh` は自動的にそれを検出します。それ以外の場合は、`--repo` フラグでリポジトリを指定します。

2. **利用可能なワークフローをリスト表示**（オプション）:
   ワークフロー ID またはファイル名を見つけるには、以下を実行します：

   ```bash
   gh workflow list
   ```

   これにより、リポジトリ内のすべてのワークフローが表示され、名前、ID、ステータス（例：`active`）が示されます。

3. **ワークフローを実行**:
   ワークフローのファイル名または ID を指定して `gh workflow run` コマンドを使用します。例：

   ```bash
   gh workflow run workflow.yml
   ```

   または、ワークフロー ID（例：`123456`）を使用します：

   ```bash
   gh workflow run 123456
   ```

   ワークフローが入力を接受する場合、`--field` フラグで指定します：

   ```bash
   gh workflow run workflow.yml --field key=value
   ```

   ブランチまたは ref を指定するには、`--ref` フラグを使用します：

   ```bash
   gh workflow run workflow.yml --ref branch-name
   ```

4. **ワークフローを監視**:
   トリガー後、実行ステータスを確認します：

   ```bash
   gh run list
   ```

   特定の実行をリアルタイムで監視するには、以下を使用します：

   ```bash
   gh run watch <run-id>
   ```

   `<run-id>` は `gh run list` からの実行 ID に置き換えます。

### トラブルシューティングのヒント

- **GPG 署名エラー**: `apt update` 中に GPG 関連の問題が発生した場合、GitHub のイシュートラッカーで修正を参照する（例：`cli/cli#9569`）か、キーインポートステップを再試行してください。[](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- **ファイアウォールの問題**: `keyserver.ubuntu.com` が失敗する場合、以下を試してください：

   ```bash
   sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key C99B11DEB97541F0
   ```

   または、必要に応じて `dirmngr` をインストールします：

   ```bash
   sudo apt-get install dirmngr
   ```

  [](https://gist.github.com/Manoj-Paramsetti/dc957bdd6a4430275d0fc28a0dc43ae9)
- **Snap インストールの警告**: GitHub はランタイムの問題により、`gh` の Snap パッケージの使用を推奨していません。上記の APT メソッドに従ってください。[](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- **認証スコープ**: `gh workflow run` が権限のために失敗する場合、トークンに `workflow` スコープがあることを確認してください。以下で再認証します：

   ```bash
   gh auth refresh -s workflow
   ```

### 追加の注意点

- **GitHub CLI マニュアル**: `gh` コマンドの詳細については、`gh help` を実行するか、公式マニュアル [cli.github.com](https://cli.github.com) を参照してください。[](https://cli.github.com/manual/)
- **ワークフローの要件**: ワークフローファイル（例：`workflow.yml`）がリポジトリの `.github/workflows/` ディレクトリに存在し、手動トリガー（例：`workflow_dispatch` イベント）用に設定されていることを確認してください。
- **代替インストール方法**: Homebrew（`brew install gh`）を使用するか、[リリースページ](https://github.com/cli/cli/releases) からバイナリをダウンロードして `gh` をインストールすることもできますが、Ubuntu では APT メソッドが推奨されます。[](https://github.com/cli/cli)

このセットアップにより、Ubuntu のコマンドラインから GitHub Actions ワークフローを効率的に管理できます。特定の `gh` コマンドやワークフロー設定についてヘルプが必要な場合はお知らせください！