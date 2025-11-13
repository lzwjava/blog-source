---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Gunicorn 生產環境部署指南
translated: true
type: note
---

Gunicorn (Green Unicorn) 是一個專為 Python 網路應用程式設計的熱門 WSGI HTTP 伺服器。它被廣泛應用於生產環境中，用於運行基於 Flask、Django、FastAPI 等框架建構的應用程式，或任何符合 WSGI 標準的應用。與開發伺服器（例如 Flask 內建伺服器）不同，Gunicorn 更加穩定、高效，且專為實際部署環境設計。

---

## 什麼是 WSGI？

**WSGI** (Web Server Gateway Interface) 是 Python 的標準規範 (PEP 333)，定義了網頁伺服器如何與 Python 網路應用程式進行通訊。Gunicorn 作為 WSGI 伺服器，負責接收來自客戶端的 HTTP 請求（通常透過反向代理如 Nginx），並將這些請求傳遞給你的 Python 應用程式。

```
客戶端 → Nginx (反向代理) → Gunicorn → 你的 WSGI 應用程式 (例如 Flask/Django)
```

---

## 為什麼要使用 Gunicorn？

| 功能 | 優勢 |
|-------|--------|
| **生產環境就緒** | 能高效處理多個並行請求 |
| **工作者模式** | 支援同步、非同步、執行緒和 gevent 工作者 |
| **預先分支模型** | 產生多個工作者程序來並行處理請求 |
| **零停機重載** | 透過 `SIGHUP` 實現平順重啟 |
| **整合性** | 可與 Nginx、systemd、Docker 無縫協作 |

> **注意**：Gunicorn **無法**高效提供靜態檔案服務——請使用 Nginx 或 CDN 處理此類需求。

---

## 安裝

```bash
pip install gunicorn
```

如需非同步支援：
```bash
pip install gunicorn[gevent]    # 或 [eventlet], [tornado]
```

---

## 基本使用方式

### 命令列

```bash
gunicorn [選項] 模組名稱:變數名稱
```

Flask 應用範例：
```bash
gunicorn --workers 3 --bind 0.0.0.0:8000 run:app
```

- `run:app` → `run.py` 檔案，`app` 是 Flask/FastAPI 實例
- `--workers 3` → 3 個工作者程序
- `--bind 0.0.0.0:8000` → 監聽所有介面，埠號 8000

---

## 工作者類型

Gunicorn 支援不同的工作者類別，以因應各種應用程式需求：

| 工作者類型 | 指令 | 適用場景 |
|-----------|--------|---------|
| **sync** (預設) | `gunicorn -k sync` | CPU 密集型或簡單應用 |
| **gevent** | `gunicorn -k gevent` | 高並行、I/O 密集型 (例如 API、websockets) |
| **eventlet** | `gunicorn -k eventlet` | 類似 gevent，適合非同步處理 |
| **tornado** | `gunicorn -k tornado` | 即時應用程式 |
| **threads** | `gunicorn -k sync --threads 4` | 混合 I/O + CPU，但需注意 GIL 限制 |

> **建議**：對於大多數網路 API，使用 `gevent` 或 `eventlet`。

---

## 關鍵配置選項

| 選項 | 說明 | 範例 |
|------|-------------|--------|
| `--bind` | 主機和埠號 | `--bind 0.0.0.0:8000` |
| `--workers` | 工作者程序數量 | `--workers 4` |
| `--worker-class` | 工作者類型 | `-k gevent` |
| `--threads` | 每個同步工作者的執行緒數 | `--threads 2` |
| `--timeout` | 工作者逾時時間 (秒) | `--timeout 30` |
| `--keep-alive` | Keep-alive 逾時時間 | `--keep-alive 2` |
| `--max-requests` | 在處理 N 個請求後重啟工作者 | `--max-requests 1000` |
| `--max-requests-jitter` | 隨機化重啟時機 | `--max-requests-jitter 100` |
| `--preload` | 在分支前載入應用程式 | `--preload` (啟動更快，共享記憶體) |
| `--log-level` | 記錄等級 | `--log-level debug` |

---

## 該配置多少工作者？

一般經驗法則：

```text
工作者數量 = (2 × CPU 核心數) + 1
```

對於 gevent/eventlet (非同步)：
```text
工作者數量 = CPU 核心數
執行緒數 = 100–1000 (依並行需求調整)
```

範例：
```bash
gunicorn -k gevent --workers 2 --threads 200 run:app
```

> 使用 `nproc` 或 `htop` 檢查 CPU 核心數。

---

## 配置檔案 (`gunicorn-cfg.py`)

與其使用冗長的命令列參數，不如使用配置檔案（如你的 Dockerfile 所示）：

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

然後執行：
```bash
gunicorn --config gunicorn-cfg.py run:app
```

> 你的 Dockerfile 正是採用此模式——**絕佳實踐**。

---

## 記錄設定

Gunicorn 記錄存取和錯誤日誌：

```python
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "warning"
```

或記錄到 stdout (適合 Docker)：
```python
accesslog = "-"
errorlog = "-"
```

記錄格式：
```python
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
```

---

## 平順重載與零停機

1. **重載工作者** (新程式碼)：
   ```bash
   kill -HUP <gunicorn_pid>
   ```

2. **平順重啟**：
   ```bash
   kill -TERM <gunicorn_pid>
   ```

3. **使用 systemd**：
   ```ini
   [Service]
   ExecReload=/bin/kill -HUP $MAINPID
   ```

---

## 在 Nginx 後運行 (推薦)

### Nginx 配置片段

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

## Docker 最佳實踐 (你的 Dockerfile 很完善！)

```dockerfile
FROM python:3.9
COPY . .
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
```

**優點分析**：
- `PYTHONUNBUFFERED=1` → 即時記錄
- `PYTHONDONTWRITEBYTECODE=1` → 不產生 `.pyc` 檔案
- `--no-cache-dir` → 更小的映像檔
- 配置檔案 → 簡潔的 CMD 指令

**可選改進**：
```dockerfile
# 使用非 root 使用者
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# 健康檢查
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1
```

---

## Systemd 服務範例

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

啟用服務：
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now gunicorn
```

---

## 常見問題與除錯

| 問題 | 解決方案 |
|------|----------|
| **工作者逾時** | 增加 `--timeout` 或優化程式碼 |
| **開啟檔案過多** | 增加 `ulimit -n` 或使用非同步工作者 |
| **記憶體洩漏** | 使用 `--max-requests` 定期重啟工作者 |
| **502 Bad Gateway** | 檢查 Gunicorn 是否運行，埠號綁定是否正確 |
| **啟動緩慢** | 若記憶體允許，使用 `--preload` |

---

## 監控

- **記錄**：即時查看存取/錯誤記錄
- **指標**：使用 `prometheus-client` + Gunicorn exporter
- **健康檢查端點**：
  ```python
  @app.route("/health")
  def health():
      return "OK", 200
  ```

---

## 進階：非同步視圖 (FastAPI 範例)

```python
# run.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}
```

執行指令：
```bash
gunicorn -k uvicorn.workers.UvicornWorker run:app
```

安裝：
```bash
pip install "uvicorn[standard]"
```

---

## 總結檢查清單

| 任務 | 完成？ |
|------|-------|
| 使用配置檔案 (`gunicorn-cfg.py`) | 是 |
| 根據 CPU 設定 `workers` | 是 |
| 對 I/O 密集型應用使用非同步工作者 | 是 |
| 在 Nginx 後運行 | 是 |
| 在 Docker 中記錄到 stdout | 是 |
| 設定逾時和 max-requests | 是 |
| 使用 `HUP` 實現平順重載 | 是 |

---

## 參考資料

- [Gunicorn 官方文件](https://docs.gunicorn.org/)
- [Gunicorn 設定參考](https://docs.gunicorn.org/en/stable/settings.html)
- [DigitalOcean Gunicorn 教學](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu)
- [Uvicorn + Gunicorn 用於 FastAPI](https://fastapi.tiangolo.com/deployment/server-workers/)