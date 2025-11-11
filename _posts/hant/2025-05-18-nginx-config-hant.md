---
audio: false
generated: true
lang: hant
layout: post
title: Nginx 配置
translated: true
type: note
---

在 Nginx 配置中使用 `server_name 0.0.0.0` 是不正確的做法，因為 `server_name` 用於匹配域名或主機名稱，而非 IP 地址。此外，`0.0.0.0` 是一個特殊地址，表示「監聽所有介面」，這是由 `listen` 指令處理，而非 `server_name`。由於你的筆記型電腦（伺服器）的 IP 地址會動態變化，你需要一個能適應此情況的解決方案。以下是修復 Nginx 配置並有效處理動態 IP 問題的步驟。

### 問題
你的筆記型電腦 IP 地址（例如 `192.168.1.27`）因 DHCP 而變更，但你希望 Nginx 伺服器無論 IP 地址如何變化都能可靠地提供影片檔案。在 `server_name` 指令或客戶端配置中硬編碼 IP 地址，會導致 IP 變更時出現問題。

### 解決方案
為了讓你的 Nginx 伺服器在 IP 變更時仍能無縫運作，你可以使用以下一種或多種方法：

#### 1. 使用動態 DNS（DDNS）或本地主機名稱
不要依賴 IP 地址，而是使用主機名稱來識別你的伺服器。可以透過以下方式實現：
- **使用筆記型電腦的主機名稱**：大多數作業系統會分配預設主機名稱（例如 macOS 上的 `mylaptop.local` 或 Linux/Windows 上的 `mylaptop`）。你可以在 Nginx 的 `server_name` 中使用此主機名稱，並透過主機名稱存取伺服器。
- **設定本地 DNS 或 mDNS**：使用如 Avahi（適用於 Linux）或 Bonjour（適用於 macOS/Windows）的服務，在本地解析筆記型電腦的主機名稱（例如 `mylaptop.local`）。
- **使用 DDNS 服務**：如果你需要從本地網路外部存取，可以使用如 No-IP 或 DynDNS 的服務，分配一個域名（例如 `mymovies.ddns.net`）來追蹤你筆記型電腦的 IP，即使它發生變化。

**Nginx 配置範例**：
```nginx
server {
    listen 80;
    server_name mylaptop.local; # 使用筆記型電腦的主機名稱或 DDNS 名稱
    root /path/to/movies;
    location / {
        try_files $uri $uri/ /index.html; # 根據你的設定進行調整
    }
}
```
- 將 `mylaptop.local` 替換為你筆記型電腦的實際主機名稱或 DDNS 名稱。
- 在客戶端上，透過 `http://mylaptop.local` 而非 IP 地址來存取伺服器。

**如何找到筆記型電腦的主機名稱**：
- Linux/macOS：在終端機中執行 `hostname`。
- Windows：在命令提示字元中執行 `hostname`，或在設定 > 系統 > 關於中查看。
- 確保你的網路支援 mDNS（大多數家用路由器透過 Bonjour/Avahi 支援）。

#### 2. 將 Nginx 綁定到所有介面
如果你希望 Nginx 監聽所有可用的 IP 地址（在 IP 變更時很有用），請將 `listen` 指令配置為使用 `0.0.0.0` 或完全省略地址（Nginx 預設為所有介面）。

**Nginx 配置範例**：
```nginx
server {
    listen 80; # 監聽所有介面（等同於 0.0.0.0:80）
    server_name _; # 匹配任何主機名稱或 IP
    root /path/to/movies;
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```
- `listen 80`：綁定到所有介面，因此伺服器會回應筆記型電腦上任何 IP 的請求。
- `server_name _`：一個萬用字元，匹配用於存取伺服器的任何主機名稱或 IP。
- 客戶端可以使用筆記型電腦當前的任何 IP（例如 `http://192.168.1.27` 或 `http://192.168.1.28`）或主機名稱來存取伺服器。

#### 3. 為筆記型電腦分配靜態 IP
為了避免 IP 地址變更，請將你的筆記型電腦配置為在本地網路中使用靜態 IP 地址（例如 `192.168.1.27`）。可以透過以下方式實現：
- **路由器設定**：在路由器的 DHCP 設定中為你的筆記型電腦的 MAC 地址保留一個 IP（通常稱為「DHCP 保留」）。
- **筆記型電腦網路設定**：在筆記型電腦的網路配置中手動設定一個在 DHCP 範圍之外的靜態 IP（例如 `192.168.1.200`）。

一旦 IP 設為靜態，請更新你的 Nginx 配置：
```nginx
server {
    listen 192.168.1.27:80; # 綁定到靜態 IP
    server_name 192.168.1.27; # 可選，如果客戶端直接使用 IP
    root /path/to/movies;
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```
- 客戶端透過 `http://192.168.1.27` 存取伺服器。

#### 4. 使用反向代理或負載平衡器（進階）
如果你有多個伺服器或想要更穩健的設定，可以在具有靜態 IP 的裝置上設定反向代理（例如另一個 Nginx 實例），將請求轉發到你的筆記型電腦。代理可以使用筆記型電腦的主機名稱或動態解析其 IP。

### 推薦方法
為了簡單起見，我推薦**方法 1（使用筆記型電腦的主機名稱）**或**方法 2（綁定到所有介面）**：
- **方法 1** 適用於你的網路支援 mDNS 且你希望使用易記的 URL（例如 `http://mylaptop.local`）的情況。它需要最少的配置，並在本地網路中運作良好。
- **方法 2** 適用於你不想依賴主機名稱，且可以接受客戶端使用當前 IP（你可以透過在筆記型電腦上執行 `ip addr` 或 `ifconfig` 找到）的情況。

### 實施步驟
1. **編輯 Nginx 配置**：
   - 開啟你的 Nginx 設定檔（例如 `/etc/nginx/sites-available/default` 或 `/etc/nginx/conf.d/movies.conf`）。
   - 應用上述其中一種配置（例如使用 `server_name mylaptop.local` 或 `server_name _` 配合 `listen 80`）。
   - 儲存檔案。

2. **測試配置**：
   ```bash
   sudo nginx -t
   ```
   確保沒有語法錯誤。

3. **重新載入 Nginx**：
   ```bash
   sudo systemctl reload nginx
   ```
   或者，如果 `systemctl` 不可用：
   ```bash
   sudo nginx -s reload
   ```

4. **測試存取**：
   - 從客戶端裝置，使用主機名稱（例如 `http://mylaptop.local`）或筆記型電腦的當前 IP（例如 `http://192.168.1.27`）存取伺服器。
   - 確認影片檔案正確提供。

5. **可選：檢查筆記型電腦的 IP**：
   如果你需要找到筆記型電腦的當前 IP：
   - Linux/macOS：`ip addr show` 或 `ifconfig`。
   - Windows：在命令提示字元中執行 `ipconfig`。

### 額外提示
- **防火牆**：確保筆記型電腦的防火牆允許連接埠 80（或 HTTPS 的 443）上的 HTTP 流量。例如，在 Linux 上使用 `ufw`：
  ```bash
  sudo ufw allow 80/tcp
  ```
- **檔案權限**：確認 Nginx 有權限讀取影片檔案：
  ```bash
  sudo chown -R www-data:www-data /path/to/movies
  sudo chmod -R 755 /path/to/movies
  ```
  （將 `www-data` 調整為 Nginx 運行的使用者，例如在某些系統上為 `nginx`。）
- **HTTPS（可選）**：為了安全起見，考慮設定 HTTPS 並使用自簽憑證或 Let’s Encrypt，特別是如果你需要從本地網路外部存取伺服器。
- **除錯**：如果伺服器無法存取，請檢查 Nginx 日誌：
  ```bash
  sudo tail -f /var/log/nginx/error.log
  sudo tail -f /var/log/nginx/access.log
  ```

### 為什麼 `server_name 0.0.0.0` 無效
- `server_name` 用於匹配 HTTP 請求中的 `Host` 標頭，而非指定監聽介面。設定 `server_name 0.0.0.0` 會期望客戶端發送 `Host: 0.0.0.0` 標頭，但他們不會這樣做。
- 要監聽所有介面，請使用 `listen 0.0.0.0:80`（或僅 `listen 80`），而要匹配任何主機名稱，請使用 `server_name _`。

### 最終配置範例（最簡單）
適用於本地影片伺服器，無論 IP 如何變更都能運作：
```nginx
server {
    listen 80;
    server_name _;
    root /path/to/movies;
    location / {
        autoindex on; # 啟用目錄列表以便瀏覽
        try_files $uri $uri/ /index.html;
    }
}
```
- 按照上述說明儲存、測試並重新載入 Nginx。
- 透過 `http://<筆記型電腦-ip>` 或 `http://<筆記型電腦-主機名稱>` 存取。

此設定確保你的影片伺服器在筆記型電腦 IP 變更時仍可存取，無需在配置中依賴特定 IP。

如果你有更多詳細資訊（例如你當前的 Nginx 配置、作業系統或網路設定），我可以進一步調整解決方案。請告訴我！