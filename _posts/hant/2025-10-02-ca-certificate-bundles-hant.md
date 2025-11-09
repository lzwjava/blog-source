---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 認識 CA 證書捆綁包
translated: true
type: note
---

### 什麼是 cacert.pem？

`cacert.pem`（或類似名稱的檔案，如 `ca-bundle.crt`、`ca-bundle.pem` 或 `ca-certificates.pem`）指的是包含一個或多個憑證授權機構（CA）根憑證的檔案，採用 PEM 格式。PEM 全稱為 Privacy Enhanced Mail，是一種基於文字的編碼標準（使用 Base64），將憑證數據包裹在 `-----BEGIN CERTIFICATE-----` 和 `-----END CERTIFICATE-----` 等標頭之間。

- **用途**：這些檔案是來自主要憑證授權機構（例如 Let's Encrypt、DigiCert、GlobalSign）的可信任根憑證集合。它們讓軟體（如網頁瀏覽器、伺服器或工具）能夠在安全連線（HTTPS）期間，驗證網站或伺服器提供的 SSL/TLS 憑證的真實性。
- **在你的範例中**：貼上的內容是一個過時的 `ca-bundle.crt` 檔案（來自 2012 年 10 月），從 Mozilla 的 Firefox 瀏覽器提取。它包含如「GTE CyberTrust Global Root」和「Thawte Server CA」等根憑證，這些在當時是可信任的，但現已過期或被取代。現代的 CA 憑證集合會定期更新（例如透過作業系統更新或軟體包）。

許多系統和工具使用類似的檔案：
- 在 Linux 上：通常位於 `/etc/ssl/certs/ca-certificates.crt`（Debian/Ubuntu）或 `/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem`（Red Hat）。
- 在 macOS 上：作為系統鑰匙圈的一部分。
- 在 Windows 上：儲存在憑證存放區中。

這些憑證被信任的證據：CA 憑證由可信任的實體簽署，而這樣的憑證集合確保了安全的網頁瀏覽。若沒有它們，SSL 驗證將會失敗，從而存在中間人攻擊的風險。關於更新，Mozilla 在 https://wiki.mozilla.org/CA 發布最新資料。

### 為什麼我們需要它？

CA 憑證集合對於 SSL/TLS 加密（用於 HTTPS、安全電郵等）至關重要，因為它們：
- **驗證真實性**：當你連線到像 https://example.com 這樣的網站時，伺服器會發送其憑證。你的客戶端（瀏覽器、curl 等）使用 CA 憑證集合來檢查該憑證是否由可信任的根憑證簽署。如果不是，它會發出警告或阻止連線。
- **防止攻擊**：若沒有驗證，任何人都可以偽造憑證，導致如網路釣魚或資料攔截等漏洞。
- **實現安全通訊**：它們確保端對端加密和對數位憑證的信任，這對於電子商務、銀行業務和任何線上服務至關重要。
- **歷史背景**：在 1990 年代初期，SSL 被開發出來，而 CA 憑證集合成為標準（例如，受到如 RFC 5280 用於 X.509 憑證的 IETF 標準信任）。

如果你的系統缺乏最新的憑證集合，安全網站可能會顯示錯誤（例如「憑證不受信任」）。大多數作業系統會自動維護和更新這些憑證。

### 如何使用它？

使用方法取決於工具或軟體。以下是一些常見範例：

#### 1. **在 Curl（命令列工具）中**
   - Curl 預設使用 CA 憑證集合（來自你系統的儲存庫），但你可以指定自訂檔案進行驗證。
   - 範例：下載自訂的憑證集並用於 HTTPS 請求。
     ```
     wget https://curl.se/ca/cacert.pem  # 從 curl 網站取得更新的 CA 憑證集
     curl --cacert cacert.pem https://api.github.com  # 針對此憑證集進行驗證
     ```
     - 若沒有 `--cacert`，curl 可能會從 Linux 上的 `/etc/ssl/certs/ca-certificates.crt` 載入。

#### 2. **在 Apache/Nginx（網頁伺服器）中**
   - 設定用於客戶端憑證驗證或 SSL 驗證。
   - 在 Apache 的 `httpd.conf` 或虛擬主機中：
     ```
     SSLCACertificateFile /path/to/ca-bundle.crt
     ```
     - 這告訴 Apache 使用該憑證集來信任客戶端憑證或驗證上游連線。

#### 3. **在 PHP 或其他語言中**
   - 對於 PHP 中的 cURL：
     ```
     $ch = curl_init();
     curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);  // 啟用驗證
     curl_setopt($ch, CURLOPT_CAINFO, '/path/to/cacert.pem');  // 指定憑證集
     // 發出請求...
     ```
   - Node.js 或 Python（requests 函式庫）有類似的選項來設定自訂 CA 路徑。

#### 4. **瀏覽器使用**
   - 瀏覽器（Chrome、Firefox）包含內建的 CA 憑證集，通常不需要手動設定。如果需要，你可以透過設定添加自訂 CA（例如，用於自簽署的開發站點）。

#### 5. **一般提示**
   - **保持更新**：CA 憑證會過期或被撤銷。從如 https://mkcert.dev（用於開發）或你的作業系統套件管理器（例如在 Ubuntu 上使用 `sudo apt-get update ca-certificates`）等來源下載最新的憑證集。
   - **安全性注意**：僅使用可信任的憑證集，以避免接受無效的憑證。對於測試，你可以使用 OpenSSL 建立自簽署的憑證（例如 `openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365`）。
   - **檢查有效性**：使用 `openssl x509 -in cacert.pem -text -noout` 來檢查憑證的詳細資料。

如果這是用於特定應用程式，請提供更多詳細資料以獲得量身定制的建議！如果你看到錯誤（例如「SSL 憑證驗證失敗」），可能意味著你的憑證集已過時或遺失。