---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast:free
title: UbuntuへのLibreChatインストール
translated: true
type: note
---

### Ubuntu 24.04 LTS への LibreChat インストール

LibreChat は、Web インターフェースを通じて複数の AI モデル（例: OpenAI、Gemini、Ollama）をサポートするオープンソースの AI チャットプラットフォームです。推奨されるインストール方法は Docker Compose を使用することです。この方法はシンプルで、MongoDB や MeiliSearch のような依存関係を自動的に処理し、Ubuntu 上で確実に動作します。お使いのシステム (Ubuntu 24.04.2 LTS with Python 3.13.4) は要件を満たしていますが、まず Docker と Git をインストールする必要があります。

#### 前提条件
1. **システムの更新**:
   ```
   sudo apt update && sudo apt upgrade -y
   ```

2. **Git のインストール** (未インストールの場合):
   ```
   sudo apt install git -y
   ```

3. **Docker と Docker Compose のインストール**:
   - Docker のインストール:
     ```
     sudo apt install docker.io -y
     sudo systemctl start docker
     sudo systemctl enable docker
     sudo usermod -aG docker $USER
     ```
     グループ変更を反映させるため、ログアウトして再度ログインするか（または `newgrp docker` を実行してください）。
   - Docker Compose のインストール (最新バージョン):
     ```
     sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
     sudo chmod +x /usr/local/bin/docker-compose
     ```
     `docker-compose --version` で確認してください。

#### インストール手順
1. **LibreChat リポジトリのクローン**:
   ```
   cd ~/projects  # または任意のディレクトリ
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   ```

2. **環境設定ファイルのコピーと設定**:
   - サンプルファイルをコピー:
     ```
     cp .env.example .env
     ```
   - テキストエディタ (例: `nano .env`) で `.env` を編集します。更新する主な設定:
     - MongoDB マスターキーを設定: 強力なパスワードを生成し、`MONGODB_URI=mongodb://mongodb:27017/LibreChat?authSource=admin` と `MONGODB_MASTER_KEY=your_generated_key_here` を設定します。
     - MeiliSearch の場合: `MEILI_MASTER_KEY=your_generated_key_here` を設定します (強力なキーを生成してください)。
     - 必要に応じて AI API キーを追加します (例: `OPENAI_API_KEY=your_openai_key`)。Ollama のようなローカルモデルの場合、最初はキーは不要です。
     - 保存して終了します。全ての設定オプションについては、ドキュメントを参照してください。

3. **Docker Compose で LibreChat を起動**:
   ```
   docker-compose up -d
   ```
   - これにより、イメージの取得、サービスの起動 (LibreChat アプリ、MongoDB、MeiliSearch)、そしてデタッチドモードでの実行が行われます。
   - 完全に起動するまで待機します (`docker-compose logs -f` で確認できます)。

4. **LibreChat へのアクセス**:
   - ブラウザを開き、`http://localhost:3080` にアクセスします。
   - ログインページでアカウントを作成します。
   - AI モデルを選択し (設定でエンドポイントを構成)、チャットを開始します。

#### インストール後のヒント
- **停止/更新**: 停止するには `docker-compose down` を実行し、更新するには `git pull` してから `docker-compose up -d --build` を実行します。
- **データ永続化**: MongoDB データ用のボリュームが自動的に作成されます (`./data/mongodb` 内)。
- **トラブルシューティング**:
  - ポートが競合する場合は、`docker-compose.yml` を編集して `3080:3080` を変更してください。
  - ヘッドレス/サーバーアクセスの場合、サーバーの IP アドレスを使用し (例: `http://your-server-ip:3080`)、ファイアウォールがポート 3080 を許可していることを確認します (`sudo ufw allow 3080`)。
  - ローカル LLM を使用する場合、Ollama を別途インストールし、`.env` でエンドポイントとして追加してください。
- **代替方法: NPM メソッド** (Docker なし): もし希望する場合は、Node.js 18+、Yarn、MongoDB、MeiliSearch を手動でインストールし、その後 `yarn install` と `yarn run frontend` + `yarn run backend` を実行します。ただし、シンプルさの点では Docker が強く推奨されます。

これで素早くセットアップできるはずです。エラーが発生した場合は、出力内容を共有してください。

[LibreChat 公式ドキュメント](https://docs.librechat.ai/install/installation/docker_compose.html)  
[Ubuntu Docker ガイド](https://docs.librechat.ai/install/installation/docker_ubuntu.html)  
[It's FOSS チュートリアル](https://itsfoss.com/librechat-linux/)