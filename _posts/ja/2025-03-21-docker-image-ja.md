---
audio: false
generated: true
lang: ja
layout: post
title: Dockerイメージの構築とデプロイ
translated: true
type: note
---

以下は、Spring BootアプリケーションをDockerイメージとしてビルドし、サーバーにデプロイするステップバイステップガイドです：

### 前提条件
1. **Java**（例：JDK 17または互換バージョン）がローカルにインストールされていること
2. **Maven**または**Gradle**（Spring Bootプロジェクトのセットアップに応じて）
3. **Docker**がローカルマシンとサーバーにインストールされていること
4. **コンテナ化する準備が整ったSpring Bootプロジェクト**
5. **サーバーアクセス**（例：SSH経由）とDockerがインストールされていること

---

### ステップ 1: Spring Bootアプリケーションの準備
Spring Bootアプリケーションがローカルで動作することを確認してください。以下でテストします：
```bash
mvn spring-boot:run  # Mavenを使用する場合
# または
gradle bootRun       # Gradleを使用する場合
```

アプリケーションが正常にビルドされることを確認します：
```bash
mvn clean package    # Maven
# または
gradle build         # Gradle
```
これにより、`.jar`ファイル（例：`target/myapp-1.0.0.jar`）が生成されます。

---

### ステップ 2: Dockerfileの作成
プロジェクトのルートディレクトリ（`.jar`ファイルが配置されている場所）に、`Dockerfile`という名前のファイルを作成し、以下の内容を記述します：

```dockerfile
# 公式のOpenJDKランタイムをベースイメージとして使用
FROM openjdk:17-jdk-slim

# コンテナ内の作業ディレクトリを設定
WORKDIR /app

# Spring Boot JARファイルをコンテナにコピー
COPY target/myapp-1.0.0.jar app.jar

# Spring Bootアプリが動作するポートを公開（デフォルトは8080）
EXPOSE 8080

# JARファイルを実行
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**注意点：**
- `myapp-1.0.0.jar`を実際のJARファイル名に置き換えてください
- アプリが別のバージョンを使用する場合は、Javaのバージョン（`openjdk:17-jdk-slim`）を調整してください

---

### ステップ 3: Dockerイメージのビルド
`Dockerfile`を含むディレクトリから、以下を実行します：
```bash
docker build -t myapp:latest .
```
- `-t myapp:latest`は、イメージを`myapp`という名前で`latest`バージョンとしてタグ付けします
- `.`は、Dockerにビルドコンテキストとして現在のディレクトリを使用するように指示します

イメージが作成されたことを確認します：
```bash
docker images
```

---

### ステップ 4: Dockerイメージのローカルテスト
コンテナをローカルで実行して動作を確認します：
```bash
docker run -p 8080:8080 myapp:latest
```
- `-p 8080:8080`は、マシンのポート8080をコンテナのポート8080にマッピングします
- ブラウザを開くか`curl`を使用してテストします（例：`curl http://localhost:8080`）

`Ctrl+C`でコンテナを停止するか、`docker ps`でコンテナIDを確認して停止します：
```bash
docker stop <container-id>
```

---

### ステップ 5: Dockerレジストリへのイメージのプッシュ（オプション）
サーバーにデプロイするには、Docker Hub（またはプライベートレジストリ）にイメージをプッシュする必要があります。これをスキップする場合は、イメージを手動で転送します。

1. Docker Hubにログイン：
   ```bash
   docker login
   ```
2. イメージにタグ付け：
   ```bash
   docker tag myapp:latest yourusername/myapp:latest
   ```
3. イメージをプッシュ：
   ```bash
   docker push yourusername/myapp:latest
   ```

---

### ステップ 6: サーバーへのデプロイ
#### オプション 1: レジストリを使用する場合
1. サーバーにSSH接続：
   ```bash
   ssh user@server-ip
   ```
2. イメージをプル：
   ```bash
   docker pull yourusername/myapp:latest
   ```
3. コンテナを実行：
   ```bash
   docker run -d -p 8080:8080 yourusername/myapp:latest
   ```
   - `-d`はコンテナをデタッチドモード（バックグラウンド）で実行します

#### オプション 2: 手動転送
レジストリを使用しない場合：
1. イメージをローカルで`.tar`ファイルとして保存：
   ```bash
   docker save -o myapp.tar myapp:latest
   ```
2. サーバーに転送（例：SCPを使用）：
   ```bash
   scp myapp.tar user@server-ip:/path/to/destination
   ```
3. サーバーにSSH接続：
   ```bash
   ssh user@server-ip
   ```
4. イメージをロード：
   ```bash
   docker load -i myapp.tar
   ```
5. コンテナを実行：
   ```bash
   docker run -d -p 8080:8080 myapp:latest
   ```

---

### ステップ 7: デプロイの確認
コンテナが実行されているか確認します：
```bash
docker ps
```

サーバー上または外部からアプリをテストします：
- サーバー上の場合：`curl http://localhost:8080`
- 外部からの場合：サーバーのIPを使用（例：`http://server-ip:8080`）。サーバーのファイアウォールでポートが開いていることを確認してください

---

### オプション：機能強化
- **環境変数**: 設定をアプリに渡します：
  ```bash
  docker run -d -p 8080:8080 -e "SPRING_PROFILES_ACTIVE=prod" myapp:latest
  ```
- **Docker Compose**: マルチコンテナ設定の場合は、`docker-compose.yml`ファイルを使用します
- **再起動ポリシー**: `--restart unless-stopped`を追加して、サーバー再起動時にコンテナが再起動するようにします

特定の部分でヘルプが必要な場合はお知らせください！

---

提供されたエラー出力から、`docker build`コマンドが成功するのを妨げているいくつかの問題があります。これらを分解してステップバイステップで解決しましょう。

---

### 特定された問題
1. **`docker-buildx`プラグインの欠落**  
   エラー：`fork/exec /Users/lzwjava/.docker/cli-plugins/docker-buildx: no such file or directory`  
   これは、Dockerがモダンなビルドツールである`buildx`プラグインを使用しようとしているが、正しくインストールまたは設定されていないことを示しています

2. **レガシービルダーの非推奨警告**  
   警告：`DEPRECATED: The legacy builder is deprecated...`  
   DockerはBuildKit（`buildx`）への切り替えを推奨していますが、レガシービルダーにフォールバックして失敗しています

3. **Dockerデーモンが実行されていない**  
   エラー：`Cannot connect to the Docker daemon at unix:///Users/lzwjava/.docker/run/docker.sock. Is the docker daemon running?`  
   Dockerデーモン（コンテナを管理するバックグラウンドサービス）がシステムで実行されていません

4. **ファイルアクセスエラー**  
   エラー：`Can't add file ... to tar: io: read/write on closed pipe`および`Can't close tar writer...`  
   これらは、デーモンが実行されていないためにビルドプロセスが失敗した結果生じる二次的な問題です

5. **プロキシ設定の検出**  
   システムがプロキシ（`HTTP_PROXY`および`HTTPS_PROXY`）を使用しています。これが適切に設定されていない場合、Dockerの動作を妨げる可能性があります

---

### ステップバイステップでの修正

#### 1. Dockerデーモンが実行されていることを確認
核心的な問題は、Dockerデーモンが実行されていないことです。以下で修正します：

- **macOSの場合**（Docker Desktopを使用していると仮定）：
  1. アプリケーションフォルダまたはSpotlightからDocker Desktopを開きます
  2. 実行されていることを確認します（メニューバーのDockerクジラアイコンが緑色になります）
  3. 起動しない場合：
     - Docker Desktopを終了して再起動します
     - アップデートを確認：Docker Desktop > Check for Updates
     - それでも失敗する場合は、[docker.com](https://www.docker.com/products/docker-desktop/)からDocker Desktopを再インストールします

- **ターミナルでの確認**：
  以下を実行：
  ```bash
  docker info
  ```
  デーモンが実行されている場合は、システム情報が表示されます。実行されていない場合は、同じ「Cannot connect」エラーが表示されます

- **手動でデーモンを再起動**（必要な場合）：
  ```bash
  sudo launchctl stop com.docker.docker
  sudo launchctl start com.docker.docker
  ```

デーモンが実行されたら、次のステップに進みます

---

#### 2. `buildx`プラグインのインストール（オプションだが推奨）
レガシービルダーは非推奨であるため、`buildx`を設定しましょう：

1. **`buildx`のインストール**：
   - バイナリを手動でダウンロードするか、Dockerの指示を使用します：
     ```bash
     mkdir -p ~/.docker/cli-plugins
     curl -SL https://github.com/docker/buildx/releases/download/v0.13.0/buildx-v0.13.0.darwin-amd64 -o ~/.docker/cli-plugins/docker-buildx
     chmod +x ~/.docker/cli-plugins/docker-buildx
     ```
     （OS/アーキテクチャに応じて[最新リリース](https://github.com/docker/buildx/releases)を確認してください。例：M1/M2 Macの場合は`darwin-arm64`）

2. **インストールの確認**：
   ```bash
   docker buildx version
   ```

3. **BuildKitをデフォルトとして設定**（オプション）：
   `~/.docker/config.json`に以下を追加：
   ```json
   {
     "features": { "buildkit": true }
   }
   ```

または、これをスキップして今のところレガシービルダーを使用することもできます（ステップ4を参照）

---

#### 3. プロキシ設定の処理
プロキシ設定（`http://127.0.0.1:7890`）が、Dockerのイメージ取得能力を妨げる可能性があります。Dockerがそれらを使用するように設定します：

1. **Docker Desktop経由**：
   - Docker Desktop > Settings > Resources > Proxiesを開きます
   - 「Manual proxy configuration」を有効にして以下を入力：
     - HTTP Proxy: `http://127.0.0.1:7890`
     - HTTPS Proxy: `http://127.0.0.1:7890`
   - 適用して再起動

2. **CLI経由**（Desktopを使用しない場合）：
   `~/.docker/config.json`を作成または編集：
   ```json
   {
     "proxies": {
       "default": {
         "httpProxy": "http://127.0.0.1:7890",
         "httpsProxy": "http://127.0.0.1:7890"
       }
     }
   }
   ```
   編集後、Dockerを再起動します

---

#### 4. ビルドの再試行
デーモンが実行され、プロキシが設定されたので、再度ビルドを試みます：

```bash
docker build -t myapp:latest .
```

- `buildx`をインストールした場合、デフォルトでBuildKitを使用します
- `buildx`をスキップした場合、`--progress=plain`を追加してレガシービルダーを強制します：
  ```bash
  docker build --progress=plain -t myapp:latest .
  ```

---

#### 5. `.git/hooks`エラーのトラブルシューティング（継続する場合）
`.git/hooks/pre-rebase.sample`エラーは、Dockerがビルドコンテキストに不要なファイルを含めようとしていることを示唆します。`.dockerignore`ファイルでこれらを除外します：

1. `Dockerfile`と同じディレクトリに`.dockerignore`を作成：
   ```
   .git
   .gitignore
   *.md
   target/*
   !target/*.jar
   ```
2. これは、Dockerに`.git`フォルダとJARファイルを除く`target/`内のすべてを無視するように指示します

3. ビルドを再試行：
   ```bash
   docker build -t myapp:latest .
   ```

---

### 最終確認
- イメージを確認：
  ```bash
  docker images
  ```
- ローカルで実行：
  ```bash
  docker run -p 8080:8080 myapp:latest
  ```
- `curl http://localhost:8080`でテスト

---

### 次のステップ
イメージが正常にビルドされたら、前回の応答からのデプロイステップ（例：レジストリへのプッシュやサーバーへの転送）に従ってください。さらに問題が発生した場合はお知らせください！