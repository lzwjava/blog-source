---
audio: false
date: 2025-09-14
generated: true
image: false
lang: hant
layout: post
model: mistralai/mistral-medium-3.1
title: 停用 LibreChat 登入驗證
translated: true
type: note
---

要讓 **LibreChat** 無需頻繁登入（或完全停用登入），你可以調整驗證設定。以下是解決問題的步驟：

---

### **1. 停用驗證（無需登入）**
如果你想讓 **LibreChat 完全開放**（無需任何登入），請修改配置：

#### **選項 A：環境變數（建議）**
在 `.env` 檔案（或環境變數）中設定以下內容：
```env
# 完全停用驗證
AUTHENTICATION=false
```
然後重新啟動 LibreChat：
```bash
docker compose down && docker compose up -d  # 如果使用 Docker
# 或
npm run build && npm run start  # 如果在本機運行
```

#### **選項 B：修改 `config.yaml`**
如果你使用 `config.yaml` 檔案，請新增：
```yaml
auth:
  enabled: false
```

---

### **2. 修正常見登出問題（如仍需要登入）**
如果你**想保留驗證**但解決頻繁登出的問題，請嘗試以下解決方案：

#### **A. 增加工作階段/Cookie 有效期**
在 `.env` 中修改工作階段設定：
```env
# 延長工作階段逾時時間（以秒為單位，例如 7 天 = 604800）
SESSION_EXPIRY=604800

# 確保 Cookie 安全（如果使用 HTTPS）
COOKIE_SECURE=true  # 如果在 HTTP 上測試，設為 false
COOKIE_SAME_SITE=lax
```

#### **B. 使用持久化工作階段儲存**
預設情況下，LibreChat 可能使用記憶體工作階段（重啟時會重置）。切換到**資料庫支援的工作階段儲存**（例如 Redis 或 PostgreSQL）：

1. **安裝 Redis**（如果尚未安裝）：
   ```bash
   docker run -d --name redis -p 6379:6379 redis
   ```
2. 更新 `.env`：
   ```env
   SESSION_STORE=redis
   REDIS_URL=redis://localhost:6379
   ```

#### **C. 檢查反向代理設定（如果使用 Nginx/Apache）**
如果你使用代理（例如 Nginx），請確保：
- Cookie 被正確轉發。
- `ProxyPass` 包含 `cookie` 指令。

Nginx 設定範例：
```nginx
location / {
    proxy_pass http://localhost:3080;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_cookie_path / /;  # 確保 Cookie 範圍正確
}
```

#### **D. 清除瀏覽器快取並在無痕模式下測試**
有時瀏覽器快取/損壞的 Cookie 會導致問題。請嘗試：
- 清除 `librechat.example.com` 的 Cookie。
- 在**無痕模式**或不同瀏覽器中測試。

---

### **3. 除錯 Cookie 問題**
如果 Cookie 仍然無法持久化：
1. **檢查瀏覽器開發者工具**（`F12` > **Application** > **Cookies**）查看是否設定了 `connect.sid`（或類似內容）。
2. **驗證 `SameSite` 屬性**（應為 `Lax`，如果是跨網站則為 `None`）。
3. **確保 `Domain` 正確**（例如子網域使用 `.example.com`）。

---

### **4. 更新 LibreChat**
如果你使用的是舊版本，新版本可能已修復錯誤：
```bash
git pull origin main
docker compose down && docker compose up -d --build
```

---

### **最後注意事項**
- **安全警告**：停用驗證（`AUTHENTICATION=false`）會使 LibreChat **公開可存取**。請僅在受信任/內部網路中這樣做。
- **需要 HTTPS**：如果使用 Cookie，請確保你的網站使用 **HTTPS**（或測試時設定 `COOKIE_SECURE=false`）。