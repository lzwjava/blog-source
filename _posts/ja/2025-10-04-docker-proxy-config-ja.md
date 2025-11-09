---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Dockerデーモンプロキシ設定の構成
translated: true
type: note
---

### Docker デーモンのプロキシ設定

Docker デーモンは、企業ファイアウォールの内側からイメージのプルやコンテナのビルドなどの操作を行うために、HTTP/HTTPS プロキシを使用するように設定できます。これは `/etc/docker/daemon.json` ファイルを編集（または作成）することで行います。この設定はデーモン自体（例: `docker pull` や `docker build`）に適用され、個々のコンテナ（これらは環境変数や Docker ビルド引数を使用します）には適用されないことに注意してください。

#### 前提条件
- Linux システムで root または sudo アクセス権が必要です（これは Docker デーモン設定の主要な OS です。Windows/Mac の Docker Desktop では、代わりに GUI 設定を使用してください）。
- Docker がインストールされ、実行されていること。
- プロキシサーバーの詳細（例: HTTP/HTTPS プロキシ用の `http://proxy.company.com:8080`、および no-proxy 例外）を知っていること。

#### ステップバイステップでの設定

1.  **デーモン設定ファイルの場所を確認または作成**:
    - ターミナルを開き、`/etc/docker/` に移動します（ディレクトリが存在しない場合は作成: `sudo mkdir -p /etc/docker`）。
    - テキストエディタ（例: `sudo nano /etc/docker/daemon.json` または `sudo vim /etc/docker/daemon.json`）を使用して `daemon.json` ファイルを編集します。
    - ファイルが存在しない場合は作成します。新しい場合は空の JSON オブジェクト `{}` から始めます。

2.  **プロキシ設定を追加**:
    - JSON ファイルに `"proxies"` セクションを追加します。基本的な例を以下に示します:

      ```json
      {
        "proxies": {
          "http-proxy": "http://proxy.company.com:8080",
          "https-proxy": "http://proxy.company.com:8080",
          "no-proxy": "localhost,127.0.0.1,*.company.com,10.0.0.0/8"
        }
      }
      ```

      - **説明**:
        - `"http-proxy"`: HTTP プロキシの URL（非 HTTPS リクエストに必要）。
        - `"https-proxy"`: HTTPS プロキシの URL（多くの場合、HTTP プロキシと同じ）。
        - `"no-proxy"`: プロキシをバイパスする必要があるホスト/ドメイン/IP 範囲のカンマ区切りリスト（例: ローカルアドレスや内部ドメイン）。これにより無限ループが防止されます。
        - 認証が必要な場合は、`http://username:password@proxy.company.com:8080` の形式を使用します。
        - SOCKS プロキシの場合は、`"http-proxy": "socks5://proxy.company.com:1080"` を使用します。

      - `daemon.json` に既存のコンテンツ（例: `"log-driver": "json-file"` などの他の設定）が既にある場合は、キーを重複させずに `"proxies"` セクションをマージします。有効な JSON 構文であることを確認してください（必要に応じて `jsonlint` のようなツールを使用して検証します）。

3.  **保存して Docker デーモンを再起動**:
    - ファイルを保存します。
    - 変更を適用するために Docker サービスを再起動します:
      ```
      sudo systemctl restart docker
      ```
      - 古いシステムや非 systemd のセットアップでは、`sudo service docker restart` を使用します。
    - デーモンが実行されていることを確認します:
      ```
      sudo systemctl status docker
      ```
      - 問題がある場合はログを確認: `sudo journalctl -u docker.service`.

4.  **設定を検証**:
    - イメージをプルしてテストします（これでプロキシ経由でルーティングされるはずです）:
      ```
      docker pull hello-world
      ```
    - デーモン設定を検査してプロキシ設定が適用されているか確認します:
      ```
      docker info | grep -i proxy
      ```
      - 以下のような出力が表示されるはずです:
        ```
        HTTP Proxy: http://proxy.company.com:8080
        HTTPS Proxy: http://proxy.company.com:8080
        No Proxy: localhost,127.0.0.1,*.company.com,10.0.0.0/8
        ```
    - ビルドコンテキストで Docker を使用している場合は、以下でテストします:
      ```
      docker build -t test-proxy .
      ```
      （ベースイメージをプルする簡単な Dockerfile を想定。）

#### 追加の注意点
- **セキュリティ**: 共有システムでは `daemon.json` に資格情報をハードコーディングするのは避けてください。可能であれば環境変数を使用するか、より高度なセットアップには `docker config` のようなツールを使用します。
- **一般的な問題**:
  - **構文エラー**: 無効な JSON はデーモンの起動を妨げます。`cat /etc/docker/daemon.json` と JSON バリデータでダブルチェックしてください。
  - **ファイアウォール/SELinux**: プロキシに到達可能であり、セキュリティモジュールがそれをブロックしていないことを確認してください。
  - **Docker バージョン**: これは Docker 20.10+ で動作します（以前のバージョンでは `HTTP_PROXY` のような異なる環境変数を使用していました）。`docker --version` でバージョンを確認し、必要に応じてアップグレードしてください。
  - **レジストリ固有のプロキシ**: プライベートレジストリの場合、`"registry-mirrors"` の下または `daemon.json` 内の安全でないレジストリに追加の設定が必要な場合があります。
- **コンテナの場合**: 実行中のコンテナ*内部*（デーモンではない）にプロキシ設定が必要な場合は、Dockerfile 内で環境変数を設定する（例: `ENV http_proxy=http://proxy.company.com:8080`）か、`docker run -e http_proxy=...` 経由で設定します。
- **Docker Desktop (Windows/Mac)**: 設定 > リソース > プロキシ に移動し、そこで有効化/設定します—JSON の編集は必要ありません。

詳細については、公式 Docker ドキュメントを参照してください: [Docker デーモンの設定](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file)。エラーが発生した場合は、正確な出力を共有してトラブルシューティングを行ってください！