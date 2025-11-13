---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Nginx CORS 與 HTTPS 配置
translated: true
type: note
---

```nginx
# 定義映射以處理允許的來源
map $http_origin $cors_origin {
    default "https://example.com";
    "http://localhost:3000" "http://localhost:3000";
    "https://example.com" "https://example.com";
    "https://www.example.com" "https://www.example.com";
}
```

### 功能說明
- 根據傳入的 `Origin` 標頭值 (`$http_origin`) 建立變數 `$cors_origin`
- 若請求來自 `http://localhost:3000`、`https://example.com` 或 `https://www.example.com`，則回傳相同來源
- 其他來源（或無來源）則預設使用 `https://example.com`
- 此設定後續用於動態設定 `Access-Control-Allow-Origin` 標頭，僅對受信任的前端網域啟用 CORS

---

```nginx
# 將 HTTP 重新導向至 HTTPS
server {
    listen 80;
    server_name example.com api.example.com;
    return 301 https://$host$request_uri;
}
```

### 功能說明
- 監聽 80 端口 (HTTP)
- 匹配發往 `example.com` 或 `api.example.com` 的請求
- 永久重新導向 (301) 所有流量至相同網址的 HTTPS 版本
- 強制使用安全連線，不允許純 HTTP 存取

---

```nginx
# example.com 主要網站配置
server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

    root /home/project/project-web;
    index index.html index.htm index.php default.html default.htm default.php;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$ {
        expires 30d;
    }

    location ~ .*\.(js|css)?$ {
        expires 12h;
    }

    error_page 404 /index.html;
}
```

### 功能說明
- 為 `example.com` 啟用 **HTTPS 伺服器**，監聽 443 端口並啟用 SSL
- 使用 **Let’s Encrypt** 憑證（可自動續期、免費）
- 強制使用現代 TLS 版本 (`TLSv1.2`, `TLSv1.3`) 與高強度加密套件以提升安全性
- 從 `/home/project/project-web` 提供靜態檔案服務
- 嘗試依序提供：請求檔案 → 目錄 → 404 錯誤
- 設定**快取標頭**：
  - 圖片：快取 30 天
  - JS/CSS：快取 12 小時
- 所有 404 錯誤均導向 `index.html` → 支援 **SPA（單頁應用）** 路由（如 React、Vue）

---

```nginx
# api.example.com 的 API 配置
server {
    listen 443 ssl;
    server_name api.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com-0001/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com-0001/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

    location / {
        # 清除任何現有的 Access-Control 標頭
        more_clear_headers 'Access-Control-Allow-Origin';

        # 處理 CORS 預檢請求
        if ($request_method = 'OPTIONS') {
            add_header 'Access-Control-Allow-Origin' $cors_origin;
            add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, DELETE';
            add_header 'Access-Control-Allow-Headers' 'Origin, Content-Type, Accept, Authorization, X-Client-Info, X-Trace-Id, X-Requested-With, X-HTTP-Method-Override, DNT, Keep-Alive, User-Agent, If-Modified-Since, Cache-Control, Content-Range, Range';
            add_header 'Access-Control-Max-Age' 3600;
            return 204;
        }

        add_header 'Access-Control-Allow-Origin' $cors_origin always;
        add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, DELETE' always;
        add_header 'Access-Control-Allow-Headers' '...' always;

        proxy_pass http://127.0.0.1:5000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_connect_timeout 600s;
        proxy_send_timeout 600s;
        proxy_read_timeout 600s;
        send_timeout 600s;
    }
}
```

### 功能說明
- 為 `api.example.com` 啟用 **HTTPS 反向代理**
- 使用**獨立的 Let’s Encrypt 憑證**（可能因多網域/SAN 需求）
- 所有流量均代理至運行於 `localhost:5000` 的**本地後端**（如 Flask、Node.js 等）

#### CORS 處理
- 使用 `$cors_origin` 映射**動態允許**已核准的來源
- **清除任何現有**的 `Access-Control-Allow-Origin` 以避免衝突
- 處理 **OPTIONS 預檢請求**：
  - 立即回傳 `204 No Content`
  - 允許常見方法與標頭
  - 預檢結果快取 1 小時 (`Max-Age: 3600`)
- 對實際請求，使用 `always` 參數添加 CORS 標頭，確保錯誤回應中也包含標頭

#### 代理設定
- 將真實客戶端 IP 與通訊協定資訊轉發至後端
- 高逾時設定（10 分鐘）→ 適用長時間運行的 API 操作（如檔案上傳、複雜運算）

---

### 架構總結

| 組件                | 用途 |
|---------------------|------|
| `example.com`       | 提供靜態 SPA 服務（React/Vue 等） |
| `api.example.com`   | 安全 API 閘道 → 連接 5000 端口後端 |
| HTTP → HTTPS        | 所有流量強制使用 TLS |
| CORS                | 限制僅允許 `example.com`、`www` 及 `localhost:3000` |
| 快取                | 針對效能最佳化 |
| SSL                 | Let’s Encrypt 憑證，現代加密套件 |

### 安全備註
- 強固的 TLS 配置（預期在 SSL Labs 獲評 A+ 等級）
- CORS **非萬用字元** → 防止未授權網站呼叫 API
- 高效處理預檢請求
- 轉發真實 IP → 利於後端的記錄與速率限制

如需圖表或 Docker 化版本，歡迎告知！