---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Nginx CORSとHTTPS設定
translated: true
type: note
---

```nginx
# 許可されたオリジンを処理するマップを定義
map $http_origin $cors_origin {
    default "https://example.com";
    "http://localhost:3000" "http://localhost:3000";
    "https://example.com" "https://example.com";
    "https://www.example.com" "https://www.example.com";
}
```

### 機能
- 受信した`Origin`ヘッダー（`$http_origin`）の値に基づいて、変数`$cors_origin`を作成します。
- リクエストが`http://localhost:3000`、`https://example.com`、または`https://www.example.com`からの場合、そのオリジンをそのまま返します。
- 他のオリジン（またはオリジンなし）の場合、デフォルトで`https://example.com`を使用します。
- これは後で`Access-Control-Allow-Origin`ヘッダーを動的に設定し、信頼されたフロントエンドドメインのみにCORSを有効にするために使用されます。

---

```nginx
# HTTPをHTTPSにリダイレクト
server {
    listen 80;
    server_name example.com api.example.com;
    return 301 https://$host$request_uri;
}
```

### 機能
- ポート80（HTTP）で待ち受けます。
- `example.com`または`api.example.com`へのリクエストに一致します。
- すべてのトラフィックを同じURLのHTTPSバージョンに恒久的にリダイレクト（301）します。
- 安全な接続を強制し、平文のHTTPアクセスを許可しません。

---

```nginx
# example.comのメインサイト設定
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

### 機能
- ポート443でSSLを有効にした`example.com`の**HTTPSサーバー**です。
- **Let's Encrypt**証明書（自動更新可能、無料）を使用します。
- セキュリティのために最新のTLSバージョン（`TLSv1.2`、`TLSv1.3`）と強力な暗号を適用します。
- `/home/project/project-web`から静的ファイルを提供します。
- 要求されたファイル→ディレクトリ→404の順に提供を試みます。
- **キャッシュヘッダー**を設定：
  - 画像：30日間キャッシュ。
  - JS/CSS：12時間キャッシュ。
- すべての404エラーは`index.html`にルーティング→**SPA（シングルページアプリ）**ルーティング（例：React、Vue）を有効にします。

---

```nginx
# api.example.comのAPI設定
server {
    listen 443 ssl;
    server_name api.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com-0001/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com-0001/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

    location / {
        # 既存のAccess-Controlヘッダーをクリア
        more_clear_headers 'Access-Control-Allow-Origin';

        # CORSプリフライトリクエストを処理
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

### 機能
- `api.example.com`の**HTTPSリバースプロキシ**です。
- **別のLet's Encrypt証明書**（おそらく複数ドメイン/SANのため）を使用します。
- すべてのトラフィックは`localhost:5000`で実行されている**ローカルバックエンド**（例：Flask、Node.jsなど）にプロキシされます。

#### CORS処理
- `$cors_origin`マップを使用して、承認されたオリジンのみを**動的に許可**します。
- 競合を防ぐために既存の`Access-Control-Allow-Origin`を**クリア**します。
- **OPTIONSプリフライト**を処理：
  - 直ちに`204 No Content`を返します。
  - 一般的なメソッドとヘッダーを許可します。
  - プリフライトを1時間キャッシュ（`Max-Age: 3600`）。
- 実際のリクエストでは、エラーレスポンスでもCORSヘッダーが表示されるように`always`でCORSヘッダーを追加します。

#### プロキシ設定
- 実際のクライアントIPとプロトコル情報をバックエンドに転送します。
- 高いタイムアウト（10分）→長時間実行されるAPI操作（例：ファイルアップロード、重い計算）に適しています。

---

### アーキテクチャの概要

| コンポーネント           | 目的 |
|---------------------|--------|
| `example.com`       | 静的SPA（React/Vueなど）を提供 |
| `api.example.com`   | 安全なAPIゲートウェイ→ポート5000のバックエンド |
| HTTP → HTTPS        | すべてのトラフィックをTLS経由に強制 |
| CORS                | `example.com`、`www`、`localhost:3000`に制限 |
| キャッシュ             | パフォーマンス最適化 |
| SSL                 | Let's Encrypt、最新の暗号 |

### セキュリティノート
- 強力なTLS設定（SSL LabsでA+の可能性）。
- CORSは**ワイルドカードではない**→不正なサイトからのAPI呼び出しを防止。
- プリフライトが効率的に処理。
- 実際のIPが転送→バックエンドでのロギング/レート制限に有用。

図やDocker化バージョンが必要な場合はお知らせください！