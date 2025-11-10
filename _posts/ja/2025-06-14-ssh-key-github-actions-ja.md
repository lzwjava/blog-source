---
audio: false
generated: true
lang: ja
layout: post
title: GitHub Actions JARデプロイのためのSSH鍵設定
translated: true
type: note
---

GitHub Actions で JAR ファイルをデプロイするための SSH キーを生成するには、以下の手順に従ってください。

1. **SSH キーペアの生成**:
   - ローカルマシンまたは安全な環境で以下を実行します:
     ```bash
     ssh-keygen -t ed25519 -C "your_email@example.com" -f github-actions-deploy
     ```
   - システムが Ed25519 をサポートしていない場合は、以下を使用します:
     ```bash
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f github-actions-deploy
     ```
   - デフォルトのファイル保存場所を受け入れるために Enter キーを押し、必要に応じてパスフレーズを設定します（セキュリティ上、推奨）。これにより、以下の 2 つのファイルが作成されます:
     - `github-actions-deploy` (秘密鍵)
     - `github-actions-deploy.pub` (公開鍵)

2. **公開鍵をターゲットサーバーに追加**:
   - 公開鍵をコピーします:
     ```bash
     cat github-actions-deploy.pub
     ```
   - JAR ファイルをデプロイするサーバーにログインします。
   - 公開鍵をサーバーの `~/.ssh/authorized_keys` に追記します:
     ```bash
     echo "your-public-key-content" >> ~/.ssh/authorized_keys
     ```
   - `authorized_keys` ファイルに正しいパーミッションが設定されていることを確認します:
     ```bash
     chmod 600 ~/.ssh/authorized_keys
     ```

3. **秘密鍵を GitHub Secrets に保存**:
   - GitHub リポジトリの `Settings > Secrets and variables > Actions > Secrets` に移動します。
   - **New repository secret** をクリックします。
   - シークレットに名前を付けます（例: `SSH_PRIVATE_KEY`）。
   - 秘密鍵 (`github-actions-deploy`) の内容を貼り付けます:
     ```bash
     cat github-actions-deploy
     ```
   - シークレットを保存します。

4. **GitHub Actions ワークフローの設定**:
   - ワークフローファイル（例: `.github/workflows/deploy.yml`）を作成または編集します。
   - JAR のデプロイに SSH キーを使用するステップを追加します。以下はワークフローの例です:

     ```yaml
     name: Deploy JAR

     on:
       push:
         branches:
           - main

     jobs:
       deploy:
         runs-on: ubuntu-latest

         steps:
         - name: Checkout code
           uses: actions/checkout@v4

         - name: Set up Java
           uses: actions/setup-java@v4
           with:
             java-version: '17' # 使用する Java バージョンに調整
             distribution: 'temurin'

         - name: Build JAR
           run: mvn clean package # 使用するビルドツールに合わせて調整（例: Gradle）

         - name: Install SSH Key
           uses: shimataro/ssh-key-action@v2
           with:
             key: ${{ secrets.SSH_PRIVATE_KEY }}
             known_hosts: 'optional-known-hosts' # 以下の注記を参照

         - name: Add Known Hosts
           run: |
             ssh-keyscan -H <server-ip-or-hostname> >> ~/.ssh/known_hosts
           # <server-ip-or-hostname> をサーバーの IP またはホスト名に置き換え

         - name: Deploy JAR to Server
           run: |
             scp target/your-app.jar user@<server-ip-or-hostname>:/path/to/deploy/
             ssh user@<server-ip-or-hostname> "sudo systemctl restart your-service" # デプロイプロセスに合わせて調整
     ```

   - **注記**:
     - `target/your-app.jar` を JAR ファイルへのパスに置き換えてください。
     - `user@<server-ip-or-hostname>` をサーバーの SSH ユーザーとアドレスに置き換えてください。
     - デプロイコマンド（例: `sudo systemctl restart your-service`）を、サーバー上で JAR を起動またはデプロイする方法に合わせて調整してください。
     - `known_hosts` ステップは、SSH ホスト検証の問題を回避するために重要です。サーバーのホストキーがわかっている場合は、`shimataro/ssh-key-action` ステップで事前に設定するか、例のように `ssh-keyscan` を使用できます。

5. **ワークフローのセキュリティ確保**:
   - 秘密鍵がログや出力に公開されないようにします。
   - シークレットへの不正アクセスを防ぐために、リポジトリの権限を制限します。
   - SSH キーにパスフレーズを使用している場合は、別のシークレットとして追加し、`shimataro/ssh-key-action` ステップに含めます:
     ```yaml
     with:
       key: ${{ secrets.SSH_PRIVATE_KEY }}
       passphrase: ${{ secrets.SSH_KEY_PASSPHRASE }}
       known_hosts: 'optional-known-hosts'
     ```

6. **ワークフローのテスト**:
   - `main` ブランチ（またはワークフローで指定したブランチ）に変更をプッシュします。
   - GitHub リポジトリの **Actions** タブでワークフローを監視し、JAR が正しくビルドおよびデプロイされることを確認します。

7. **トラブルシューティング**:
   - **Permission denied**: SSH キーがサーバーの `authorized_keys` に正しく追加されていること、およびユーザーがターゲットディレクトリにアクセスする権限を持っていることを確認してください。
   - **Host verification failed**: `known_hosts` ステップがサーバーの IP またはホスト名で正しく設定されていることを確認してください。
   - **Build issues**: Java バージョンとビルドコマンドがプロジェクトの設定と一致していることを確認してください。

この設定により、JAR ファイルをデプロイするための SSH ベースのデプロイメントが GitHub Actions ワークフローに安全に統合されます。特定の調整（例: 特定のサーバー設定やビルドツール用）が必要な場合は、お知らせください。