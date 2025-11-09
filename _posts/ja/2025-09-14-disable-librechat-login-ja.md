---
audio: false
date: 2025-09-14
generated: true
image: false
lang: ja
layout: post
model: mistralai/mistral-medium-3.1
title: ログイン認証の無効化
translated: true
type: note
---

**LibreChat** で頻繁なログインを必要としないようにする（またはログインを完全に無効にする）には、認証設定を調整します。問題を解決する手順は以下の通りです：

---

### **1. 認証を無効にする（ログイン不要）**
**LibreChat を完全にオープン**（ログインなし）にしたい場合は、設定を変更します：

#### **オプション A: 環境変数（推奨）**
`.env` ファイル（または環境変数）に以下を設定します：
```env
# 認証を完全に無効にする
AUTHENTICATION=false
```
その後、LibreChat を再起動します：
```bash
docker compose down && docker compose up -d  # Docker を使用している場合
# または
npm run build && npm run start  # ローカルで実行している場合
```

#### **オプション B: `config.yaml` を変更する**
`config.yaml` ファイルを使用している場合は、以下を追加します：
```yaml
auth:
  enabled: false
```

---

### **2. 頻繁なログアウトの問題を修正する（ログインを維持したい場合）**
**認証を維持したい**が、頻繁なログアウトの問題を修正したい場合は、以下の解決策を試してください：

#### **A. セッション/Cookie の有効期限を延長する**
`.env` でセッション設定を変更します：
```env
# セッションタイムアウトを延長（秒単位、例：7日 = 604800）
SESSION_EXPIRY=604800

# Cookie がセキュアであることを確認（HTTPS を使用している場合）
COOKIE_SECURE=true  # HTTP でテストする場合は false に設定
COOKIE_SAME_SITE=lax
```

#### **B. 永続的なセッションストアを使用する**
デフォルトでは、LibreChat はメモリ内セッションを使用している可能性があります（再起動時にリセットされます）。**データベースバックアップのセッションストア**（例：Redis または PostgreSQL）に切り替えます：

1. **Redis をインストール**（まだインストールされていない場合）：
   ```bash
   docker run -d --name redis -p 6379:6379 redis
   ```
2. `.env` を更新：
   ```env
   SESSION_STORE=redis
   REDIS_URL=redis://localhost:6379
   ```

#### **C. リバースプロキシ設定を確認する（Nginx/Apache を使用している場合）**
プロキシ（例：Nginx）の背後にある場合は、以下を確認してください：
- Cookie が適切に転送されている。
- `ProxyPass` に `cookie` ディレクティブが含まれている。

Nginx 設定の例：
```nginx
location / {
    proxy_pass http://localhost:3080;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_cookie_path / /;  # Cookie が誤ってスコープされていないことを確認
}
```

#### **D. ブラウザのキャッシュをクリアし、シークレットモードでテストする**
ブラウザのキャッシュや破損した Cookie が原因で問題が発生することがあります。以下を試してください：
- `librechat.example.com` の Cookie をクリアする。
- **シークレットモード**または別のブラウザでテストする。

---

### **3. Cookie の問題をデバッグする**
Cookie がまだ持続しない場合：
1. **ブラウザの DevTools**（`F12` > **Application** > **Cookies**）をチェックし、`connect.sid`（または類似のもの）が設定されているか確認する。
2. **`SameSite` 属性**（クロスサイトの場合は `Lax` または `None` であるべき）を確認する。
3. **`Domain` が正しい**（例：サブドメインの場合は `.example.com`）ことを確認する。

---

### **4. LibreChat を更新する**
古いバージョンを使用している場合、新しいリリースでバグが修正されている可能性があります：
```bash
git pull origin main
docker compose down && docker compose up -d --build
```

---

### **最終的な注意点**
- **セキュリティ警告**: 認証を無効にすると（`AUTHENTICATION=false`）、LibreChat は**公開アクセス可能**になります。信頼できる内部ネットワークでのみこれを行ってください。
- **HTTPS 必須**: Cookie を使用する場合は、サイトが **HTTPS** であることを確認してください（またはテストの場合は `COOKIE_SECURE=false` を設定してください）。