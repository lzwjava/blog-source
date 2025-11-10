---
audio: false
generated: true
image: false
lang: ja
layout: post
title: SSHを使用したGitHubへの接続
translated: true
type: note
---

SSHを使用してGitHubに接続するには、以下の手順に従ってください。このガイドはGitHubの公式ドキュメントに基づいており、既存の鍵の確認、新しい鍵の生成、GitHubへの追加、接続テストを含みます。

### 1. 既存のSSH鍵の確認
新しいSSH鍵を作成する前に、既存の鍵があるか確認します：
- ターミナル（macOS/Linux）またはGit Bash（Windows）を開きます
- 以下のコマンドを実行：
  ```bash
  ls -al ~/.ssh
  ```
- `id_rsa`や`id_rsa.pub`（または`id_ed25519`、`id_ed25519.pub`など）のようなファイルを探します。既存の鍵がある場合は、ステップ3に進んでください。ない場合は新しい鍵を生成します

### 2. 新しいSSH鍵の生成
SSH鍵がない場合、または新しい鍵が必要な場合：
- ターミナルで新しいSSH鍵を生成：
  ```bash
  ssh-keygen -t ed25519 -C "your_email@example.com"
  ```
  - `your_email@example.com`をGitHubアカウントに関連付けられたメールアドレスに置き換えてください
  - `ed25519`をサポートしていないシステムの場合：
    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```
- プロンプトが表示されたら、Enterを押してデフォルトの場所（`~/.ssh/id_ed25519`または`~/.ssh/id_rsa`）に保存します
- オプションでパスフレーズを入力（不要な場合はEnterを押す）

### 3. SSH鍵をSSHエージェントに追加
SSHエージェントは認証用の鍵を管理します：
- SSHエージェントを起動：
  ```bash
  eval "$(ssh-agent -s)"
  ```
- 秘密鍵をエージェントに追加：
  ```bash
  ssh-add ~/.ssh/id_ed25519
  ```
  - RSAを使用した場合は`id_ed25519`を`id_rsa`に置き換えてください
- パスフレーズを設定した場合は、入力するようプロンプトが表示されます

### 4. SSH鍵をGitHubアカウントに追加
- 公開鍵をクリップボードにコピー：
  - macOSの場合：
    ```bash
    pbcopy < ~/.ssh/id_ed25519.pub
    ```
  - Linuxの場合：
    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```
    出力を手動でコピーします
  - Windows（Git Bash）の場合：
    ```bash
    cat ~/.ssh/id_ed25519.pub | clip
    ```
  - RSAを使用した場合は`id_ed25519.pub`を`id_rsa.pub`に置き換えてください
- GitHubにアクセス：
  - [GitHub](https://github.com)にログイン
  - プロフィール画像（右上）→ **Settings** → **SSH and GPG keys** → **New SSH key**または**Add SSH key**
  - 公開鍵を「Key」フィールドに貼り付け、タイトル（例：「My Laptop」）を入力し、**Add SSH key**をクリック

### 5. SSH接続のテスト
SSH鍵がGitHubで機能するか確認：
- 実行：
  ```bash
  ssh -T git@github.com
  ```
- プロンプトが表示されたら`yes`と入力して確認
- 以下のようなメッセージが表示されます：
  ```
  Hi username! You've successfully authenticated, but GitHub does not provide shell access.
  ```
  これでSSH接続が正常に機能していることが確認できます

### 6. GitでSSHを使用するように設定
Gitリポジトリが認証にSSHを使用するようにします：
- リポジトリのリモートURLを確認：
  ```bash
  git remote -v
  ```
- URLが`https://`で始まる場合は、SSHに変更：
  ```bash
  git remote set-url origin git@github.com:username/repository.git
  ```
  - `username/repository`をGitHubのユーザー名とリポジトリ名に置き換えてください

### 7. オプション：SSH鍵パスフレーズの管理
パスフレーズを設定した場合、再入力を避けるためにSSHエージェントを設定できます：
- macOSの場合、鍵をキーチェーンに追加：
  ```bash
  ssh-add --apple-use-keychain ~/.ssh/id_ed25519
  ```
- Linux/Windowsの場合、SSHエージェントは通常セッションごとに1回のみパスフレーズを要求します

### 8. オプション：SSHエージェント転送またはデプロイ鍵の使用
- **SSHエージェント転送**：サーバーにデプロイする場合、エージェント転送を有効にしてローカルのSSH鍵を安全に使用できます。`~/.ssh/config`に追加：
  ```bash
  Host example.com
      ForwardAgent yes
  ```
  `example.com`をサーバーのホスト名に置き換えてください
- **デプロイ鍵**：自動化スクリプトの場合、サーバーごとに個別のSSH鍵を生成し、GitHubリポジトリ設定でデプロイ鍵として追加します

### トラブルシューティング
- `ssh -T git@github.com`が失敗する場合：
  - 公開鍵が正しくGitHubに追加されているか確認
  - SSHエージェントが実行中で鍵が追加されているか確認（`ssh-add -l`でロードされた鍵を表示）
  - ファイルの権限が正しいか確認：
    ```bash
    chmod 600 ~/.ssh/id_ed25519
    chmod 644 ~/.ssh/id_ed25519.pub
    ```
- その他の問題については、GitHubのトラブルシューティングガイドを確認してください

これで、認証情報を繰り返し入力することなく、SSHを使用してGitHubと安全にやり取りできます。

[Connecting to GitHub with SSH - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)