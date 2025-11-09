---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Docker GHCR TLS タイムアウトエラーの修正
translated: true
type: note
---

発生しているエラー `Get "https://ghcr.io/v2/": net/http: TLS handshake timeout` は、Docker が GitHub Container Registry (GHCR) からイメージをプルしようとする際にネットワークの問題が発生していることを示す典型的な例です。この問題をトラブルシューティングして解決するための手順を以下に示します：

---

### 1. **インターネット接続を確認する**
- マシンが安定したインターネット接続を確立していることを確認してください。
- ブラウザで `https://ghcr.io` にアクセスしてみて、サイトに到達できるか確認してください。

---

### 2. **Docker デーモンのステータスを確認する**
- Docker デーモンを再起動します：
  ```bash
  sudo systemctl restart docker
  ```
- Docker が実行中であることを確認します：
  ```bash
  sudo systemctl status docker
  ```

---

### 3. **Docker DNS を設定する**
- 企業ネットワークやプロキシの内側にいる場合、Docker はカスタム DNS 設定を必要とする可能性があります。
- `/etc/docker/daemon.json` を編集または作成します：
  ```json
  {
    "dns": ["8.8.8.8", "1.1.1.1"]
  }
  ```
- Docker を再起動します：
  ```bash
  sudo systemctl restart docker
  ```

---

### 4. **プロキシ設定を確認する**
- プロキシの内側にいる場合、Docker がそれを使用するように設定します：
  ```bash
  mkdir -p ~/.docker
  echo '{
    "proxies": {
      "default": {
        "httpProxy": "http://your-proxy-address:port",
        "httpsProxy": "http://your-proxy-address:port",
        "noProxy": "localhost,127.0.0.1"
      }
    }
  }' > ~/.docker/config.json
  ```
- `your-proxy-address:port` を実際のプロキシの詳細に置き換えてください。

---

### 5. **イメージの手動プルを再試行する**
- イメージを手動でプルして、問題が持続するか確認してみてください：
  ```bash
  docker pull ghcr.io/librechat/librechat:latest
  ```
- これが動作する場合は、`docker-compose up -d` を再試行してください。

---

### 6. **ファイアウォール/ネットワーク制限を確認する**
- ファイアウォールやネットワークが `ghcr.io` へのアクセスをブロックしていないことを確認してください。
- テストのために一時的にファイアウォールを無効にします：
  ```bash
  sudo ufw disable
  ```
  (必要に応じて、テスト後に再有効化してください。)

---

### 7. **Docker と Docker-Compose を更新する**
- 最新バージョンを使用していることを確認してください：
  ```bash
  sudo apt update && sudo apt upgrade docker-ce docker-compose-plugin
  ```

---

### 8. **UID/GID 環境変数を設定する**
- `UID` と `GID` に関する警告は致命的なものではありませんが、`.env` ファイルまたは `docker-compose.yml` でこれらを設定することで警告を抑制できます：
  ```bash
  echo "UID=$(id -u)" >> .env
  echo "GID=$(id -g)" >> .env
  ```

---

### 9. **別のレジストリミラーを使用する (オプション)**
- GHCR に一貫して到達できない場合、ミラーの使用を試すことができます (ただし、本番環境では推奨されません)：
  ```json
  {
    "registry-mirrors": ["https://mirror.example.com"]
  }
  ```
  これを `/etc/docker/daemon.json` に追加し、Docker を再起動します。

---

### 10. **時刻同期を確認する**
- システムの時刻が同期されていることを確認してください：
  ```bash
  sudo apt install ntp
  sudo systemctl restart ntp
  ```

---

### コマンドまとめ表



| 手順 | コマンド/アクション |
|------|----------------|
| Docker の再起動 | `sudo systemctl restart docker` |
| Docker ステータスの確認 | `sudo systemctl status docker` |
| DNS の設定 | `/etc/docker/daemon.json` を編集 |
| イメージの手動プル | `docker pull ghcr.io/librechat/librechat:latest` |
| UID/GID の設定 | `echo "UID=$(id -u)" >> .env` |

---

これらの手順を試した後も問題が解決しない場合は、以下のコマンドの出力を教えてください：
```bash
docker info
```
また、上記のコマンドを実行した際に表示されるエラーメッセージも併せてお知らせください。これらはさらなる診断に役立ちます！