---
audio: false
generated: true
image: false
lang: hant
layout: post
title: macOS 上變更 Nginx 連接埠指南
translated: true
type: note
---

你想讓 macOS 上的 Nginx 在**不同端口**上監聽，而非使用預設端口（HTTP 為 80，HTTPS 為 443）。以下是清晰的逐步指南：

---

### 1. 找到你的 Nginx 設定檔

* 如果是透過 **Homebrew** 安裝，預設設定檔通常位於：

  ```
  /usr/local/etc/nginx/nginx.conf
  ```

  或在 Apple Silicon 架構上：

  ```
  /opt/homebrew/etc/nginx/nginx.conf
  ```
* 如果是手動安裝，可能位於 `/usr/local/nginx/conf/nginx.conf`。

---

### 2. 編輯 `listen` 指令

1. 在文字編輯器中開啟設定檔：

   ```bash
   nano /opt/homebrew/etc/nginx/nginx.conf
   ```
2. 找到 `server` 區塊：

   ```nginx
   server {
       listen 80;
       server_name localhost;

       location / {
           root   html;
           index  index.html index.htm;
       }
   }
   ```
3. 將 `listen 80;` 更改為你想要的端口，例如 8080：

   ```nginx
   listen 8080;
   ```

---

### 3. 測試設定

執行：

```bash
nginx -t
```

* 如果顯示 `syntax is ok` 和 `test is successful`，表示你的設定有效。
* 如果有錯誤，請檢查報告的行號。

---

### 4. 重新啟動 Nginx

* 如果是透過 Homebrew 安裝：

```bash
brew services restart nginx
```

* 或手動執行：

```bash
sudo nginx -s reload
```

---

### 5. 透過新端口存取

* 在瀏覽器或 curl 中輸入：

```
http://localhost:8080
```

---

**補充說明：**

* **<1024** 的端口在 macOS 上需要 `sudo` 權限。因此使用像 80 這樣的端口需要 root 權限，但 8080 或 3000 則不需要。
* 如果你想同時運行多個 Nginx 伺服器，每個伺服器**必須使用唯一的端口**。

---

我也可以提供一個**快速技巧，無需編輯 nginx.conf 即可暫時在任何端口上運行 Nginx**，使用命令列參數即可。這對測試很方便。需要我示範嗎？