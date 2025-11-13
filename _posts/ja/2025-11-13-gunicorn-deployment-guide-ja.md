---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Gunicorn本番環境デプロイガイド
translated: true
type: note
---

Gunicorn (Green Unicorn) は、Python Webアプリケーション向けの人気のあるWSGI HTTPサーバーです。Flask、Django、FastAPIなどのフレームワークで構築されたアプリケーション、あるいはWSGIに準拠したあらゆるアプリケーションを本番環境で提供するために広く使用されています。開発サーバー（例：Flaskの組み込みサーバー）とは異なり、Gunicornは堅牢で効率的であり、実際のデプロイメント向けに設計されています。

---

## WSGIとは？

**WSGI** (Web Server Gateway Interface) は、WebサーバーがPython Webアプリケーションとどのように通信するかを定義するPython標準 (PEP 333) です。GunicornはWSGIサーバーとして機能します。クライアントからのHTTPリクエストを（Nginxのようなリバースプロキシ経由で）受け取り、それをあなたのPythonアプリに渡します。

```
クライアント → Nginx (リバースプロキシ) → Gunicorn → あなたのWSGIアプリ (例: Flask/Django)
```

---

## Gunicornを使用する理由

| 機能 | 利点 |
|-------|--------|
| **本番環境対応** | 複数の同時リクエストを効率的に処理 |
| **ワーカーモデル** | 同期、非同期、スレッド、geventワーカーをサポート |
| **プリフォークモデル** | リクエストを並列処理するためにワーカープロセスを生成 |
| **ゼロダウンタイムリロード** | `SIGHUP`によるグレースフルリスタート |
| **統合性** | Nginx、systemd、Dockerとシームレスに連携 |

> **注意**: Gunicornは静的ファイルを効率的に提供**しません**。静的ファイルにはNginxやCDNを使用してください。

---

## インストール

```bash
pip install gunicorn
```

非同期サポートの場合:
```bash
pip install gunicorn[gevent]    # または [eventlet], [tornado]
```

---

## 基本的な使用方法

### コマンドライン

```bash
gunicorn [OPTIONS] MODULE_NAME:VARIABLE_NAME
```

Flaskでの例:
```bash
gunicorn --workers 3 --bind 0.0.0.0:8000 run:app
```

- `run:app` → `run.py` ファイル、`app` は Flask/FastAPI インスタンス
- `--workers 3` → 3つのワーカープロセス
- `--bind 0.0.0.0:8000` → 全てのインターフェース、ポート8000でリッスン

---

## ワーカーの種類

アプリケーションのニーズに応じて、Gunicornは異なるワーカークラスをサポートしています:

| ワーカーの種類 | コマンド | ユースケース |
|-----------|--------|---------|
| **sync** (デフォルト) | `gunicorn -k sync` | CPUバウンドまたはシンプルなアプリ |
| **gevent** | `gunicorn -k gevent` | 高同時接続性、I/O負荷の高いアプリ (例: API, WebSocket) |
| **eventlet** | `gunicorn -k eventlet` | geventと同様、非同期に適している |
| **tornado** | `gunicorn -k tornado` | リアルタイムアプリ |
| **threads** | `gunicorn -k sync --threads 4` | 混合I/O + CPU、ただしGILに注意 |

> **推奨**: ほとんどのWeb APIには `gevent` または `eventlet` を使用してください。

---

## 主な設定オプション

| オプション | 説明 | 例 |
|------|-------------|--------|
| `--bind` | ホストとポート | `--bind 0.0.0.0:8000` |
| `--workers` | ワーカープロセス数 | `--workers 4` |
| `--worker-class` | ワーカーの種類 | `-k gevent` |
| `--threads` | 同期ワーカーあたりのスレッド数 | `--threads 2` |
| `--timeout` | ワーカータイムアウト (秒) | `--timeout 30` |
| `--keep-alive` | キープアライブタイムアウト | `--keep-alive 2` |
| `--max-requests` | Nリクエスト後にワーカーを再起動 | `--max-requests 1000` |
| `--max-requests-jitter` | 再起動をランダム化 | `--max-requests-jitter 100` |
| `--preload` | フォーク前にアプリをロード | `--preload` (起動が高速、メモリ共有) |
| `--log-level` | ログレベル | `--log-level debug` |

---

## ワーカー数はいくつが適切か？

一般的な経験則:

```text
workers = (2 × CPUコア数) + 1
```

gevent/eventlet (非同期) の場合:
```text
workers = CPUコア数
threads = 100–1000 (同時接続数に依存)
```

例:
```bash
gunicorn -k gevent --workers 2 --threads 200 run:app
```

> CPUコア数を確認するには `nproc` または `htop` を使用してください。

---

## 設定ファイル (`gunicorn-cfg.py`)

長いCLI引数の代わりに、設定ファイルを使用します（あなたのDockerfileのように）:

```python
# gunicorn-cfg.py
bind = "0.0.0.0:8000"
workers = 3
worker_class = "gevent"
worker_connections = 1000
timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 100
loglevel = "info"
accesslog = "-"
errorlog = "-"
preload_app = False
```

実行:
```bash
gunicorn --config gunicorn-cfg.py run:app
```

> あなたのDockerfileはこの正確なパターンを使用しています — **優れたプラクティスです**。

---

## ロギング

Gunicornはアクセスログとエラーログを記録します:

```python
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "warning"
```

または標準出力にログ出力 (Dockerに優しい):
```python
accesslog = "-"
errorlog = "-"
```

ログフォーマット:
```python
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
```

---

## グレースフルリロードとゼロダウンタイム

1. **ワーカーのリロード** (新しいコード):
   ```bash
   kill -HUP <gunicorn_pid>
   ```

2. **グレースフルな再起動**:
   ```bash
   kill -TERM <gunicorn_pid>
   ```

3. **systemdを使用する場合**:
   ```ini
   [Service]
   ExecReload=/bin/kill -HUP $MAINPID
   ```

---

## Nginxの背後での実行 (推奨)

### Nginx設定スニペット

```nginx
upstream app_server {
    server 127.0.0.1:8000 fail_timeout=0;
}

server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://app_server;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /path/to/static/;
    }
}
```

---

## Dockerのベストプラクティス (あなたのDockerfileは素晴らしい!)

```dockerfile
FROM python:3.9
COPY . .
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
```

**これが優れている理由**:
- `PYTHONUNBUFFERED=1` → リアルタイムログ
- `PYTHONDONTWRITEBYTECODE=1` → `.pyc` ファイルを作成しない
- `--no-cache-dir` → イメージサイズが小さくなる
- 設定ファイル → クリーンなCMD

**オプションの改善点**:
```dockerfile
# 非rootユーザーを使用
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# ヘルスチェック
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1
```

---

## Systemdサービス例

```ini
# /etc/systemd/system/gunicorn.service
[Unit]
Description=Gunicorn instance
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/project
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/gunicorn \
          --config gunicorn-cfg.py \
          run:app
ExecReload=/bin/kill -HUP $MAINPID
Restart=always

[Install]
WantedBy=multi-user.target
```

有効化:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now gunicorn
```

---

## 一般的な問題とデバッグ

| 問題 | 解決策 |
|------|----------|
| **ワーカーがタイムアウト** | `--timeout` を増やすかコードを最適化 |
| **開いているファイルが多すぎる** | `ulimit -n` を増やすか非同期ワーカーを使用 |
| **メモリリーク** | `--max-requests` を使用してワーカーを再起動 |
| **502 Bad Gateway** | Gunicornが実行中か、ポートバインドを確認 |
| **起動が遅い** | メモリが許せば `--preload` を使用 |

---

## モニタリング

- **ログ**: アクセス/エラーログを監視
- **メトリクス**: `prometheus-client` + Gunicorn exporterを使用
- **ヘルスエンドポイント**:
  ```python
  @app.route("/health")
  def health():
      return "OK", 200
  ```

---

## 上級編: 非同期ビュー (FastAPIの例)

```python
# run.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}
```

実行:
```bash
gunicorn -k uvicorn.workers.UvicornWorker run:app
```

インストール:
```bash
pip install "uvicorn[standard]"
```

---

## サマリーチェックリスト

| タスク | 完了? |
|------|-------|
| 設定ファイル (`gunicorn-cfg.py`) を使用 | Yes |
| CPUに基づいて `workers` を設定 | Yes |
| I/Oには非同期ワーカーを使用 | Yes |
| Nginxの背後で実行 | Yes |
| Dockerでは標準出力にログ | Yes |
| タイムアウトとmax-requestsを設定 | Yes |
| `HUP`によるグレースフルリロード | Yes |

---

## 参考文献

- [Gunicorn 公式ドキュメント](https://docs.gunicorn.org/)
- [Gunicorn 設定リファレンス](https://docs.gunicorn.org/en/stable/settings.html)
- [DigitalOcean Gunicorn チュートリアル](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu)
- [FastAPI向け Uvicorn + Gunicorn](https://fastapi.tiangolo.com/deployment/server-workers/)