---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast:free
title: Docker Composeを使用しないLibreChatセットアップ
translated: true
type: note
---

はい、Docker Composeを使用せずに、個別の`docker run`コマンドや非Docker方式（Node.js、Yarn、MongoDB、MeiliSearchを使用した手動インストール）でLibreChatをセットアップできます。これにより、`docker-compose`バイナリ自体（これは小さい、〜20-30MBですが、おそらくLibreChatのサービスの合計で〜70MB以上になるイメージのプル全体を指していると推測します）のダウンロードを回避できます。ただし、コアのDockerイメージ（例：アプリ、MongoDB、MeiliSearch用）は、プル時に合計で約500MB-1GBになります。Docker Composeは単にDockerの上で動作するオーケストレーションツールであり、メインの帯域幅の使用者ではありません。遅い4G/5Gでのイメージのプルが依然としてボトルネックになりますが、それを軽減する方法はあります。

以下にオプションを示します。帯域幅節約のヒントを優先して説明します。モバイルデータが非常に限られている場合は、一時的にWiFiネットワークにテザリングするか、別のマシンで事前にダウンロードしたセットアップを使用する（例：`docker save`/`docker load`を介してイメージをエクスポート/インポートする）ことを検討してください。

### Dockerベースのセットアップにおける帯域幅節約のヒント
- **より高速な接続でイメージを事前プル**: インターネットがより良い別のデバイスで、`docker pull node:20-alpine`（アプリ用）、`docker pull mongo:7`（データベース）、`docker pull getmeili/meilisearch:v1.10`（検索）を実行します。次に、それらをファイルに保存します：
  ```
  docker save -o librechat-app.tar node:20-alpine
  docker save -o mongo.tar mongo:7
  docker save -o meili.tar getmeili/meilisearch:v1.10
  ```
  .tarファイルをUSB/ドライブ経由で転送し（圧縮時合計約500-800MB）、Ubuntuマシン上で：`docker load -i librechat-app.tar` などを実行します。オンラインでのプルは必要ありません。
- **より軽量な代替を使用**: テストでは、最初にMeiliSearchをスキップします（検索用でオプションです。設定で無効にします）。MongoDBイメージは約400MBです。代わりにローカルのMongoDBインストールを使用する（以下の非Dockerセクションを参照）ことで、約400MB節約できます。
- **使用量を監視**: `docker pull --quiet`や`watch docker images`などのツールを使用して追跡します。
- **プロキシまたはキャッシュ**: Docker Hubミラーまたはプロキシがある場合は、`/etc/docker/daemon.json`で設定してプルを高速化します。

### オプション1: 純粋なDocker（Composeなし） – Composeセットアップと同等
`docker run`と`docker network`を使用して`docker-compose.yml`の動作を複製できます。これは同じイメージをダウンロードしますが、各ステップを制御できます。合計ダウンロードは依然として約700MB+（アプリビルド + DB）です。

1. **Dockerネットワークを作成**（サービスを分離）:
   ```
   docker network create librechat-network
   ```

2. **MongoDBを実行**（`your_mongo_key`を強力なパスワードに置き換え）:
   ```
   docker run -d --name mongodb --network librechat-network \
     -e MONGO_INITDB_ROOT_USERNAME=librechat \
     -e MONGO_INITDB_ROOT_PASSWORD=your_mongo_key \
     -v $(pwd)/data/mongodb:/data/db \
     mongo:7
   ```
   - 永続性のために `./data/mongodb` を作成します。

3. **MeiliSearchを実行**（`your_meili_key`を置き換え）:
   ```
   docker run -d --name meilisearch --network librechat-network \
     -e MEILI_MASTER_KEY=your_meili_key \
     -p 7700:7700 \
     -v $(pwd)/data/meili:/meili_data \
     getmeili/meilisearch:v1.10
   ```
   - 帯域幅が厳しい場合はスキップします。後でアプリ設定で無効にします。

4. **LibreChatアプリをクローンしてビルド/実行**:
   - まだの場合、リポジトリをクローン: `git clone https://github.com/danny-avila/LibreChat.git && cd LibreChat`（リポジトリのダウンロードは約50MB）。
   - イメージをビルド（これによりNode.jsベース約200MBがプルされ、アプリレイヤーがビルドされます）:
     ```
     docker build -t librechat-app .
     ```
   - 実行（DBにリンクし、環境変数を使用 – 以前の回答のように`.env`ファイルを作成）:
     ```
     docker run -d --name librechat --network librechat-network -p 3080:3080 \
       --env-file .env \
       -v $(pwd):/app \
       librechat-app
     ```
     - `.env`で、`MONGODB_URI=mongodb://librechat:your_mongo_key@mongodb:27017/LibreChat` および `MEILI_HOST=http://meilisearch:7700` などを設定します。

5. **アクセス**: `http://localhost:3080`。ログ: `docker logs -f librechat`。

- **停止/クリーンアップ**: `docker stop mongodb meilisearch librechat && docker rm them`。
- **長所/短所**: Composeと同じですが、より手動です。イメージのプル/ビルドにおけるデータ使用量は依然として多いです。

### オプション2: 非Dockerインストール（手動、イメージプルなし） – 低帯域幅に推奨
Ubuntuに依存関係をネイティブにインストールします。これにより、すべてのDockerオーバーヘッドが回避されます（コンテナ用は約0MB。apt/yarn経由のパッケージダウンロードのみで、合計約200-300MB）。システムのPython/Nodeセットアップを間接的に使用します。

#### 前提条件（一度インストール）
```
sudo apt update
sudo apt install nodejs npm mongodb-org redis meilisearch git curl build-essential python3-pip -y  # MongoDB公式パッケージ; MeiliSearchバイナリ約50MB
sudo systemctl start mongod redis meilisearch
sudo systemctl enable mongod redis meilisearch
```
- Node.js: v20以上でない場合、nvm経由でインストール: `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash`、その後 `nvm install 20`。
- Yarn: `npm install -g yarn`。
- MongoDB設定: `/etc/mongod.conf`を編集してlocalhostにバインドし、再起動。

#### インストール手順
1. **リポジトリをクローン**:
   ```
   cd ~/projects
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   ```

2. **依存関係をインストール**:
   ```
   yarn install  # パッケージ用に約100-200MBダウンロード
   ```

3. **`.env`を設定**（`.env.example`からコピー）:
   - `cp .env.example .env && nano .env`
   - 主な変更点:
     - Mongo: `MONGODB_URI=mongodb://localhost:27017/LibreChat`（必要に応じて`mongo`シェル経由でDBユーザーを作成）。
     - Meili: `MEILI_HOST=http://localhost:7700` および `MEILI_MASTER_KEY=your_key`。
     - Meiliをスキップする場合、検索を無効化: `SEARCH=false`。
     - 必要に応じてAIキーを追加。

4. **ビルドと実行**:
   - 1つのターミナルで: `yarn run backend`（ポート3090でAPIを開始）。
   - 別のターミナルで: `yarn run frontend`（ポート3080でUIを開始）。
   - または、本番用にPM2を使用: `yarn global add pm2 && pm2 start yarn --name backend -- run backend` など。

5. **アクセス**: `http://localhost:3080`。アカウントを作成し、設定します。

- **データ**: MongoDBは`/var/lib/mongodb`に、Meiliは`/var/lib/meilisearch`に保存します。
- **トラブルシューティング**:
  - Mongo認証: `mongo`を実行し、ユーザーを作成: `use LibreChat; db.createUser({user: 'librechat', pwd: 'yourpass', roles: ['readWrite']})`。
  - ポート/ファイアウォール: `sudo ufw allow 3080,3090,7700`。
  - 更新: `git pull && yarn install && サービスを再起動`。
- **長所**: 帯域幅が軽い（コンテナなし）、システムリソースを直接使用。短所: セットアップがより面倒、依存関係の競合の可能性（例：あなたのPython 3.13と、ただしNodeは別）。

モバイルデータが非常に限られている場合は、非Docker方式が最適です。ディレクトリで`du -sh`を使用して監視しながら段階的に行ってください。エラーについては、ログ（例：`yarn run backend`からのログ）を共有してください。公式の非Dockerガイド: https://docs.librechat.ai/install/installation/manual_install.html。ローカルAI用にOllama統合（APIコストを節約）が必要な場合は、それらのスクリプト経由で別途インストールします（約100MB）。調整が必要な場合はお知らせください！