---
audio: false
generated: true
lang: hant
layout: post
title: 修復 Clash VPN 混合內容錯誤
translated: true
type: note
---

您遇到的錯誤訊息表明 Clash VPN 應用程式存在**混合內容**問題，具體情況是當頁面 `https://clash.razord.top/` 嘗試從不安全的 `http://127.0.0.1:9090/` 端點（例如 `http://127.0.0.1:9090/version`）載入資源時發生。現代瀏覽器會阻止此類請求，因為它們試圖在安全的 HTTPS 頁面上載入不安全的 HTTP 內容，違反了安全政策。此外，由於存取控制限制，還存在 CORS（跨來源資源共用）錯誤。以下是解決此問題的逐步指南。

---

### 問題原因
- **混合內容錯誤**：網頁透過 HTTPS 提供服務，但它試圖從不安全的 `http://127.0.0.1:9090` 獲取資源（例如版本檢查）。瀏覽器會阻止這些請求，以防止潛在的安全漏洞，例如中間人攻擊。
- **CORS 錯誤**：由於 CORS 政策，瀏覽器阻止了對 `http://127.0.0.1:9090` 的請求，該政策限制跨來源請求，除非伺服器明確允許。
- **Clash 背景**：Clash（或 Clash for Windows）是一個代理應用程式，可能使用本地伺服器（`127.0.0.1:9090`）作為其儀表板或 API。如果此本地伺服器不支援 HTTPS 或配置不正確，則在透過 HTTPS 網頁存取時會觸發這些錯誤。

---

### 解決步驟

#### 1. **驗證 Clash Core 配置**
   - **檢查 Clash Core 是否正在執行**：確保 Clash core（後端服務）正在您的機器上執行並監聽 `127.0.0.1:9090`。您可以透過以下方式驗證：
     - 開啟終端機或命令提示字元。
     - 執行 `curl http://127.0.0.1:9090/version` 以檢查端點是否回應 Clash 版本。
     - 如果沒有回應，請確保 Clash 服務處於活動狀態。重新啟動 Clash for Windows 或 Clash core 程序。
   - **為 Clash Core 啟用 HTTPS**（如果可能）：
     - 某些版本的 Clash（例如 Clash Premium 或 Clash Meta）支援為本地 API 使用 HTTPS。請檢查 Clash 文件或配置檔案（通常是 `config.yaml`）中是否有啟用外部控制器（API 端點）HTTPS 的選項。
     - 在配置檔案中尋找如 `external-controller` 或 `external-ui` 的設定。例如：
       ```yaml
       external-controller: 127.0.0.1:9090
       external-ui: <path-to-ui>
       ```
       如果支援 HTTPS，您可能需要為本地伺服器配置憑證。這是進階操作，可能需要產生自簽署憑證（請參閱下面的步驟 4）。

#### 2. **透過 HTTP 存取儀表板（臨時解決方案）**
   - 如果 Clash 儀表板可以透過 HTTP 存取（例如使用 `http://clash.razord.top/` 而不是 HTTPS），請嘗試在不使用 HTTPS 的情況下載入它以避免混合內容問題：
     - 開啟瀏覽器並導航至 `http://clash.razord.top/`。
     - 注意：不建議在生產環境中使用此方法，因為 HTTP 不安全。僅在測試或儀表板僅在本地存取時使用。
   - 如果儀表板需要 HTTPS，請繼續下一步以解決根本原因。

#### 3. **將 URL 更新為 HTTPS**
   - 錯誤表明 Clash 儀表板試圖從 `http://127.0.0.1:9090` 獲取資源。如果您可以存取 Clash 儀表板的原始碼或配置：
     - 檢查前端程式碼（例如 `index-5e90ca00.js` 或 `vendor-827b5617.js`）中是否有硬編碼的 `http://127.0.0.1:9090` 引用。
     - 如果 Clash core 支援 HTTPS，將這些引用更新為 `https://127.0.0.1:9090`，或使用相對 URL（例如 `/version`）讓瀏覽器使用與頁面相同的協定。
     - 如果您無法存取原始碼，則可能需要配置反向代理（請參閱步驟 4）。

#### 4. **設定帶有 HTTPS 的反向代理**
   - 為了解決混合內容問題，您可以設定一個反向代理（例如使用 Nginx 或 Caddy），透過 HTTPS 提供 Clash core API（`http://127.0.0.1:9090`）服務。這允許儀表板安全地與核心通訊。
   - **Nginx 步驟**：
     1. 在您的系統上安裝 Nginx（如果尚未安裝）。
     2. 為 `127.0.0.1` 產生自簽署 SSL 憑證：
        ```bash
        openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout localhost.key -out localhost.crt -subj "/CN=localhost"
        ```
     3. 配置 Nginx 以透過 HTTPS 代理請求到 `http://127.0.0.1:9090`。建立配置檔案（例如 `/etc/nginx/sites-available/clash`）：
        ```nginx
        server {
            listen 443 ssl;
            server_name localhost;

            ssl_certificate /path/to/localhost.crt;
            ssl_certificate_key /path/to/localhost.key;

            location / {
                proxy_pass http://127.0.0.1:9090;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }
        }
        ```
     4. 啟用配置並重新啟動 Nginx：
        ```bash
        sudo ln -s /etc/nginx/sites-available/clash /etc/nginx/sites-enabled/
        sudo nginx -t
        sudo systemctl restart nginx
        ```
     5. 更新 Clash 儀表板，使用 `https://localhost:443` 而不是 `http://127.0.0.1:9090` 進行 API 請求。
     6. 在瀏覽器中出現提示時，接受自簽署憑證。

   - **使用 Caddy 的替代方案**：Caddy 配置更簡單且自動處理 HTTPS：
     1. 安裝 Caddy。
     2. 建立 `Caddyfile`：
        ```caddy
        localhost:443 {
            reverse_proxy http://127.0.0.1:9090
        }
        ```
     3. 執行 Caddy：`caddy run`。
     4. 更新 Clash 儀表板，使用 `https://localhost:443`。

#### 5. **繞過 CORS 限制（進階）**
   - CORS 錯誤（`XMLHttpRequest cannot load http://127.0.0.1:9090/version due to access control checks`）表明 Clash core 伺服器未發送適當的 CORS 標頭。如果您控制 Clash core：
     - 修改 Clash core 配置以包含 CORS 標頭，例如：
       ```yaml
       external-controller: 127.0.0.1:9090
       allow-cors: true
       ```
       （請檢查 Clash 文件以獲取確切語法，因為這取決於 Clash 版本。）
     - 或者，步驟 4 中的反向代理設定可以透過添加如下標頭來處理 CORS：
       ```nginx
       add_header Access-Control-Allow-Origin "https://clash.razord.top";
       add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
       add_header Access-Control-Allow-Headers "*";
       ```
   - 如果您無法控制核心，可以使用瀏覽器擴充功能暫時繞過 CORS（例如 Chrome 的 "CORS Unblock"），但出於安全原因不建議這樣做。

#### 6. **更新 Clash 或切換到相容版本**
   - 確保您使用的是最新版本的 Clash for Windows 或 Clash Verge，因為舊版本可能存在錯誤或缺乏對外部控制器的 HTTPS 支援。
   - 檢查 Clash GitHub 儲存庫（`github.com/Dreamacro/clash` 或 `github.com/Fndroid/clash_for_windows_pkg`）以獲取更新或報告的問題，特別是與混合內容或 CORS 相關的問題。
   - 考慮切換到 **Clash Verge** 或 **Clash Meta**，它們可能對 HTTPS 和現代瀏覽器安全政策有更好的支援。[](https://clashverge.net/en/tutorial-en/)

#### 7. **在瀏覽器中允許不安全內容（不推薦）**
   - 作為最後的手段，您可以在瀏覽器中為 `https://clash.razord.top/` 允許不安全內容：
     - **Chrome**：
       1. 點擊網址列中的鎖定圖示。
       2. 前往「網站設定」>「不安全內容」> 設定為「允許」。
     - **Firefox**：
       1. 點擊鎖定圖示並前往「連線設定」。
       2. 暫時停用「阻止危險和欺騙性內容」。
     - **警告**：這會繞過安全保護，應僅在受信任網路上的本地測試中使用。
   - 或者，使用 `--disable-web-security` 標誌啟動 Chrome（僅用於開發）：
     ```bash
     google-chrome --disable-web-security --user-data-dir="/tmp/chrome_dev"
     ```

#### 8. **檢查衝突的擴充功能或防火牆**
   - 瀏覽器擴充功能（例如廣告攔截器、隱私工具）或防火牆設定可能會干擾 Clash 的本地伺服器。暫時停用擴充功能或檢查防火牆以確保 `127.0.0.1:9090` 可存取。[](https://vpncentral.com/reddit-blocked-by-network-security/)
   - 在 Windows 上，確保 Clash 應用程式具有防火牆權限：
     - 前往「設定」>「網路與網際網路」>「Windows 防火牆」>「允許應用程式透過防火牆」。
     - 添加或啟用 Clash for Windows。

#### 9. **聯絡 Clash 支援或社群**
   - 如果上述步驟無法解決問題，請在 Clash for Windows GitHub 問題頁面（`github.com/Fndroid/clash_for_windows_pkg/issues`）或 Clash 社群論壇上報告問題。提供您的設定詳細資訊，包括：
     - Clash 版本。
     - 作業系統。
     - 配置檔案（遮罩敏感資訊）。
     - 瀏覽器及版本。
   - 在社群中檢查類似問題，因為此錯誤可能特定於某些 Clash 版本或配置。[](https://superuser.com/questions/1769163/could-not-switch-to-this-profile-proxy-0-filed-ws-opts-headershost-invalid-c)

---

### 推薦方法
最安全且穩健的解決方案是**設定帶有 HTTPS 的反向代理**（步驟 4），以確保所有請求都透過 HTTPS 提供服務，從而解決混合內容和 CORS 問題。如果您無法修改 Clash core 或儀表板，使用較新版本的 Clash（例如 Clash Verge）或暫時透過 HTTP 存取儀表板（步驟 2）可能是更快的解決方法。

---

### 補充說明
- 如果您使用自訂 Clash 儀表板或第三方服務（如 `clash.razord.top`），請驗證其與您的 Clash core 版本相容。
- 在進行變更之前，始終備份您的 Clash 配置（`config.yaml`）。
- 如果問題仍然存在，您可以嘗試切換到替代的代理客戶端，如 v2rayN 或 OpenVPN，它們可能對本地 API 有更好的 HTTPS 支援。[](https://stackoverflow.com/questions/67822697/how-to-route-internet-traffic-via-clash-for-windows-ping-from-python-code-is)

如果您在具體步驟（例如設定 Nginx 或除錯 Clash 配置）上需要幫助，請告訴我！