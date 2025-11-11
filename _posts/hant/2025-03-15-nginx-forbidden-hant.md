---
audio: false
generated: true
lang: hant
layout: post
title: 修復 Nginx 403 禁止錯誤
translated: true
type: note
---

要修正您遇到的 Nginx「403 Forbidden」錯誤，需要解決兩個主要問題：在 `location` 區塊中錯誤使用了 `root` 指令，以及潛在的檔案系統權限問題。以下是根據您提供的配置來解決問題的逐步指南：

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies {
        root /path/to/your/movie/folder;
        autoindex on; # 啟用目錄列表
    }
}
```

當您訪問 `http://localhost/movies` 時，出現 403 Forbidden 錯誤，這通常表示 Nginx 無法存取或提供目標目錄的內容。以下是修正方法：

---

### 1. 修正 Nginx 配置
當前的 `location /movies` 區塊使用了 `root /path/to/your/movie/folder;`。在 Nginx 中，`root` 指令會將請求的 URI（例如 `/movies`）附加到指定路徑之後，這意味著 Nginx 會嘗試從 `/path/to/your/movie/folder/movies` 提供檔案。如果此目錄不存在，Nginx 就會傳回 403 錯誤。

要修正此問題，您應該使用 `alias` 指令來替代 `root`。`alias` 指令會將 `/movies/` URI 直接映射到 `/path/to/your/movie/folder/`，而不會附加 URI，這很可能是您預期的行為。

請按以下方式更新您的配置：

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies/ {
        alias /path/to/your/movie/folder/;
        autoindex on; # 啟用目錄列表
    }
}
```

- **主要變更：**
  - 將 `root` 改為 `alias`。
  - 在 `location /movies/` 和 `alias /path/to/your/movie/folder/` 的結尾加上斜線，以確保在使用 `autoindex` 時能正確處理目錄。

- **套用變更：**
  更新配置檔案（例如 `/etc/nginx/nginx.conf` 或 `/etc/nginx/sites-enabled/` 中的檔案）後，重新啟動 Nginx 以套用變更：
  - 在 Linux 上：`sudo systemctl restart nginx`
  - 在 Windows 上：手動停止並啟動 Nginx 服務。

- **測試 URL：**
  訪問 `http://localhost/movies/`（請注意結尾的斜線），查看目錄列表是否出現。

---

### 2. 檢查檔案系統權限
如果僅更改配置無法解決 403 錯誤，問題可能與檔案系統權限有關。Nginx 需要讀取 `/path/to/your/movie/folder/` 及其內容的權限，而此存取權限取決於 Nginx 運作時所使用的使用者（通常是 `nginx` 或 `www-data`）。

- **識別 Nginx 使用者：**
  檢查您的主要 Nginx 配置檔案（例如 `/etc/nginx/nginx.conf`）中的 `user` 指令。它可能看起來像：
  ```nginx
  user nginx;
  ```
  如果未指定，則可能根據您的系統預設為 `www-data` 或其他使用者。

- **驗證權限：**
  執行以下命令來檢查您的電影資料夾的權限：
  ```bash
  ls -l /path/to/your/movie/folder
  ```
  這將顯示擁有者、群組和權限（例如 `drwxr-xr-x`）。

- **如果需要，調整權限：**
  確保 Nginx 使用者具有讀取（以及對於目錄的執行）權限。這裡有兩個選項：
  - **選項 1：變更擁有者（建議）：**
    將資料夾的擁有者設為 Nginx 使用者（例如 `nginx`）：
    ```bash
    sudo chown -R nginx:nginx /path/to/your/movie/folder
    ```
    如果實際使用者不同（例如 `www-data`），請替換 `nginx`。

  - **選項 2：設為所有人可讀（安全性較低）：**
    如果您不想變更擁有者，可以讓其他人也能讀取該資料夾：
    ```bash
    sudo chmod -R o+r /path/to/your/movie/folder
    ```

- **確保目錄存取權：**
  目錄本身需要執行權限（`x`），Nginx 才能存取其內容：
  ```bash
  sudo chmod o+x /path/to/your/movie/folder
  ```

- **檢查上層目錄：**
  如果 `/path/to/your/movie/folder` 位於受限制的上層目錄內（例如 `/home/user/`），請確保所有上層目錄直到根目錄都對 Nginx 使用者具有執行權限：
  ```bash
  sudo chmod o+x /path /path/to /path/to/your /path/to/your/movie
  ```

---

### 3. 驗證並疑難排解
進行這些變更後，再次訪問 `http://localhost/movies/` 進行測試。如果 403 錯誤仍然存在：

- **檢查 Nginx 錯誤日誌：**
  查看錯誤日誌以獲取具體細節（通常位於 `/var/log/nginx/error.log`）：
  ```bash
  sudo tail -f /var/log/nginx/error.log
  ```
  尋找如「permission denied」或「directory index is forbidden」等訊息以找出問題所在。

- **其他注意事項：**
  - **SELinux（如果適用）：** 在啟用了 SELinux 的系統（如 CentOS）上，它可能會阻止存取。暫時將 SELinux 設為寬容模式以進行測試：
    ```bash
    sudo setenforce 0
    ```
    如果這樣能解決問題，您需要調整 SELinux 策略（例如使用 `chcon` 或 `audit2allow`）。
  - **防火牆：** 如果從另一台機器存取，請確保連接埠 80 是開放的（儘管在本地透過 `localhost` 測試時不太可能發生）。

---

### 最終配置
以下是修正後的完整配置：

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies/ {
        alias /path/to/your/movie/folder/;
        autoindex on; # 啟用目錄列表
    }
}
```

- 將 `/path/to/your/movie/folder/` 替換為您電影目錄的實際絕對路徑。
- 重新啟動 Nginx：`sudo systemctl restart nginx`。
- 訪問 `http://localhost/movies/` 以確認目錄列表正常運作。

透過修正 `alias` 指令並確保正確的檔案權限，應該能解決 403 Forbidden 錯誤，讓您能透過 Nginx 成功存取您的電影資料夾。

---

要修正您的 Nginx 403 Forbidden 錯誤並確保您的單一 `.mkv` 檔案可被存取，讓我們根據您的情況來調整設定。您有一個 `.mkv` 檔案，並且想知道該將其儲存在哪裡，以便 Nginx 使用者能夠存取它。下面，我將逐步指導您完成整個過程，包括選擇合適的目錄和配置 Nginx。

### 步驟 1：為您的 `.mkv` 檔案選擇一個目錄
在決定將 `.mkv` 檔案儲存在哪裡以供 Nginx 提供服務時，請考慮以下因素：
- **可存取性**：Nginx 使用者（例如 `nginx` 或 `www-data`）需要讀取權限。
- **慣例**：網頁伺服器通常從標準目錄（如 `/var/www/` 或 `/srv/www/`）提供檔案。
- **安全性**：避免將檔案放在權限過大或敏感的目錄中（例如，除非必要，否則避免使用 `/home/user/`）。

就您的情況而言，由於只有一個 `.mkv` 檔案，並且您是在本地（`localhost`）進行測試，我建議使用 `/var/www/html/movies/` 作為一個簡單、標準的位置。原因如下：
- `/var/www/html/` 是 Nginx 和 Apache 常見的預設網站根目錄。
- 它通常由網頁伺服器使用者或群組擁有，便於權限管理。
- 新增一個 `/movies/` 子目錄有助於保持條理。

如果 `/var/www/html/` 在您的系統上不存在或不適用，替代方案包括：
- `/srv/www/movies/`（另一個標準的網站目錄）。
- `/usr/share/nginx/html/movies/`（有時是 Nginx 的預設文件根目錄）。

在此範例中，我們使用 `/var/www/html/movies/`。

### 步驟 2：設定目錄和檔案
假設您在 Linux 系統上，請遵循以下步驟：

1. **建立目錄**：
   ```bash
   sudo mkdir -p /var/www/html/movies
   ```

2. **移動您的 `.mkv` 檔案**：
   將 `yourfile.mkv` 替換為您的實際檔案名稱，並將其移動到該目錄：
   ```bash
   sudo mv /path/to/yourfile.mkv /var/www/html/movies/yourfile.mkv
   ```

3. **設定權限**：
   Nginx 使用者（通常是 `nginx` 或 `www-data`）需要對檔案具有讀取權限，並對目錄具有執行權限。首先，透過檢查 `/etc/nginx/nginx.conf` 來識別 Nginx 使用者：
   ```bash
   grep user /etc/nginx/nginx.conf
   ```
   尋找類似 `user nginx;` 或 `user www-data;` 的行。如果未指定，則可能預設為 `www-data`（Ubuntu/Debian）或 `nginx`（CentOS/RHEL）。

   然後，調整擁有者：
   ```bash
   sudo chown -R nginx:nginx /var/www/html/movies
   ```
   如果使用者不同，請將 `nginx` 替換為 `www-data` 或實際使用者。

   確保正確的權限：
   ```bash
   sudo chmod -R 755 /var/www/html/movies
   ```
   - `755` 表示擁有者（Nginx）具有完整存取權，而其他人（包括網頁伺服器程序）可以讀取和執行（瀏覽）該目錄。

### 步驟 3：配置 Nginx
更新您的 Nginx 配置，以從 `/var/www/html/movies/` 提供 `.mkv` 檔案。以下是一個最小可運作的配置：

```nginx
server {
    listen 80;
    server_name localhost;

    location /movies/ {
        alias /var/www/html/movies/;
        autoindex on; # 如果您想瀏覽檔案，請啟用目錄列表
    }
}
```

- **注意事項**：
  - 使用 `alias` 而不是 `root`，將 `/movies/` 直接映射到 `/var/www/html/movies/`。
  - `autoindex on;` 是可選的。如果您禁用它（`autoindex off;`），則需要指定確切的檔案 URL（例如 `http://localhost/movies/yourfile.mkv`）來存取它。

將此配置儲存（例如在 `/etc/nginx/sites-enabled/default` 或自訂檔案如 `/etc/nginx/conf.d/movies.conf` 中），然後測試並重新啟動 Nginx：
```bash
sudo nginx -t  # 測試配置是否有語法錯誤
sudo systemctl restart nginx  # 套用變更
```

### 步驟 4：測試存取
- 開啟您的瀏覽器並訪問：
  - `http://localhost/movies/`（如果 `autoindex` 是開啟的，您會看到包含 `yourfile.mkv` 的目錄列表）。
  - `http://localhost/movies/yourfile.mkv`（直接存取檔案）。
- 如果運作正常，檔案應該會顯示在瀏覽器中（如果支援）或提示下載。

### 步驟 5：如有需要，進行疑難排解
如果您仍然遇到 403 錯誤：
1. **檢查權限**：
   ```bash
   ls -l /var/www/html/movies/
   ```
   確保 `yourfile.mkv` 是可讀的（例如 `-rwxr-xr-x` 或至少 `-rw-r--r--`）。

2. **檢查 Nginx 日誌**：
   ```bash
   sudo tail -f /var/log/nginx/error.log
   ```
   尋找如「permission denied」等線索。

3. **SELinux（如果適用）**：
   如果在啟用 SELinux 的系統上（例如 CentOS），請執行：
   ```bash
   sudo setenforce 0  # 暫時停用
   ```
   再次測試。如果運作正常，您需要調整 SELinux 上下文：
   ```bash
   sudo chcon -R -t httpd_sys_content_t /var/www/html/movies/
   sudo setenforce 1  # 重新啟用 SELinux
   ```

### 最後總結
透過將您的 `.mkv` 檔案儲存在 `/var/www/html/movies/`、設定正確的權限，並在 Nginx 中使用 `alias` 指令，您應該能解決 403 錯誤。此設定簡單且遵循網頁伺服器慣例，使 Nginx 使用者易於存取檔案。如果您遇到任何問題，請告訴我！

---

如果您在使用 `sudo chown -R nginx:nginx /var/www/movies` 時遇到「invalid user」錯誤，這表示 `nginx` 使用者在您的系統上不存在。這是因為 Nginx 程序可能以不同的使用者身分執行，例如 `www-data`（在 Debian/Ubuntu 上常見），或者根據您的作業系統預設為其他使用者。

### 修正：識別並使用正確的使用者
1. **檢查 Nginx 使用者**：
   查看您的 Nginx 配置檔案（通常是 `/etc/nginx/nginx.conf`）：
   ```bash
   grep user /etc/nginx/nginx.conf
   ```
   - 如果顯示 `user www-data;`，請使用 `www-data`。
   - 如果顯示 `user nginx;`，則 `nginx` 使用者應該存在（可能表示配置錯誤）。
   - 如果找不到 `user` 指令，則預設使用者取決於您的系統：
     - Ubuntu/Debian: `www-data`
     - CentOS/RHEL: `nginx`
     - 其他：可能是 `http`、`apache` 或類似使用者。

2. **替代方法：檢查執行中的程序**：
   如果配置不清楚，請查看 Nginx 以什麼使用者身分執行：
   ```bash
   ps aux | grep nginx
   ```
   查看第一列（例如 `www-data` 或 `nginx`）中的 worker 程序。

3. **套用正確的使用者**：
   假設是 `www-data`（在 Ubuntu/Debian 上常見），更新指令：
   ```bash
   sudo chown -R www-data:www-data /var/www/movies
   ```
   如果是不同的使用者（例如 `http`），請使用：
   ```bash
   sudo chown -R http:http /var/www/movies
   ```

4. **設定權限**：
   修正擁有者後，確保正確的權限：
   ```bash
   sudo chmod -R 755 /var/www/movies
   ```

5. **重新啟動並測試**：
   ```bash
   sudo systemctl restart nginx
   ```
   訪問 `http://localhost/movies/yourfile.mkv`。

### 如果仍然卡住
如果 `nginx` 和 `www-data` 都不起作用，並且程序檢查也無助於事，請告訴我您的作業系統（例如 Ubuntu、CentOS）或 `ps aux | grep nginx` 的輸出，我將為您找出確切的使用者！

---

如果設定了 `autoindex on;` 但 `http://localhost/movies/` 仍然沒有列出檔案，讓我們逐步進行疑難排解並修正它。由於您沒有看到目錄列表，可能是配置問題、權限問題或其他因素阻擋了它。以下是解決方法：

### 1. 驗證您的配置
確保您的 Nginx 配置正確且已套用。它應該看起來像這樣：

```nginx
server {
    listen 80;
    server_name localhost;

    location /movies/ {
        alias /var/www/movies/;
        autoindex on;
    }
}
```

- **常見錯誤**：
  - `alias` 路徑拼寫錯誤（例如，使用 `/var/www/movie/` 而不是 `/var/www/movies/`）。
  - `autoindex on;` 位於錯誤的區塊或被註解掉。
  - 配置檔案未載入（例如，儲存在錯誤的位置）。

檢查您的配置位於何處：
- 如果在 `/etc/nginx/sites-enabled/` 中，請確保它連結正確（例如 `ls -l /etc/nginx/sites-enabled/`）。
- 如果在 `/etc/nginx/conf.d/` 中，請確保它以 `.conf` 結尾（例如 `movies.conf`）。

測試並重新載入：
```bash
sudo nginx -t
sudo systemctl reload nginx  # 重新載入而非重新啟動，以避免停機
```

### 2. 確認檔案存在
檢查 `/var/www/movies/` 中是否有您的 `.mkv` 檔案：
```bash
ls -l /var/www/movies/
```
- 如果是空的，請將您的檔案移動到那裡：
  ```bash
  sudo mv /path/to/yourfile.mkv /var/www/movies/
  ```
- 如果不是空的，請記下檔案名稱以供測試。

### 3. 檢查權限
Nginx 需要對目錄和檔案具有讀取（`r`）和執行（`x`）權限。請驗證：
```bash
ls -ld /var/www/movies/
ls -l /var/www/movies/
```
- 輸出應該類似：
  ```
  drwxr-xr-x 2 www-data www-data 4096 Mar 15 14:00 /var/www/movies/
  -rw-r--r-- 1 www-data www-data 123456 Mar 15 14:00 yourfile.mkv
  ```
- 如果需要，請修正（將 `www-data` 替換為您的 Nginx 使用者）：
  ```bash
  sudo chown -R www-data:www-data /var/www/movies/
  sudo chmod -R 755 /var/www/movies/
  ```

### 4. 檢查日誌
查看 Nginx 錯誤日誌以獲取線索：
```bash
sudo tail -n 20 /var/log/nginx/error.log
```
- **「permission denied」**：表示權限問題——請重新檢查步驟 3。
- **「directory index forbidden」**：表示 `autoindex` 未運作——請再次檢查配置。
- 沒有相關錯誤：可能意味著 Nginx 沒有命中正確的 location 區塊。

### 5. 測試直接存取
嘗試存取特定檔案：
- 訪問 `http://localhost/movies/yourfile.mkv`。
- 如果它運作但 `/movies/` 不運作，那麼問題出在 `autoindex` 或目錄設定上。

### 6. 常見修正
- **結尾斜線**：確保 `alias` 以 `/` 結尾（`/var/www/movies/`），並測試 `http://localhost/movies` 和 `http://localhost/movies/`。
- **SELinux（如果在 CentOS/RHEL 上）**：
  ```bash
  sudo setenforce 0  # 暫時停用
  ```
  再次測試。如果運作正常，請套用：
  ```bash
  sudo chcon -R -t httpd_sys_content_t /var/www/movies/
  sudo setenforce 1
  ```
- **衝突的 Location 區塊**：如果另一個 `location` 區塊（例如 `location /`）覆蓋了 `/movies/`，請將此區塊在配置中移得更高或使其更具體。

### 7. 最小測試配置
如果仍然無法運作，請簡化配置以隔離問題。將您的配置替換為：

```nginx
server {
    listen 80;
    server_name localhost;

    location /movies/ {
        alias /var/www/movies/;
        autoindex on;
    }
}
```

儲存、測試並重新載入：
```bash
sudo nginx -t
sudo systemctl reload nginx
```

### 目前情況如何？
請告訴我：
- 您在 `http://localhost/movies/` 看到了什麼（例如 403、404、空白頁面）？
- `sudo tail -n 20 /var/log/nginx/error.log` 中有任何錯誤嗎？
- `ls -l /var/www/movies/` 的輸出是什麼？

有了這些資訊，我就能準確找出問題所在，讓您的目錄列表正常運作！