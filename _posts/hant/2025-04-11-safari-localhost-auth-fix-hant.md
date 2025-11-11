---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Safari 本地主機認證修復
translated: true
type: note
---

此問題的出現，是因為 macOS 上的 Safari 對 localhost URL 執行了比 Chrome 更嚴格的資安政策。具體而言，Safari 要求使用安全的 HTTPS 環境，才能允許持續性的 Cookie 和驗證工作階段，以避免像 LibreChat 這類在 HTTP 上運行的應用程式出現潛在的登出循環或每次造訪都需要重新驗證的情況。Chrome 對 localhost 上的 HTTP 較為寬容，因此驗證狀態能在 Chrome 中持續，但在 Safari 中則不行。[1][2][3]

### 影響因素
- **瀏覽器政策**：像 Safari 這類現代瀏覽器要求 localhost 使用 HTTPS，以避免混合內容警告和工作階段不安全問題。
- **LibreChat 行為**：LibreChat 使用安全的 Cookie 或基於 localStorage 的權杖進行驗證，這些在 Safari 中會因為其對非安全來源的嚴格處理而於 HTTP 上失效。

### 解決方案 (按簡易度和有效性排序)
1. **為 Localhost 設定 HTTPS (推薦)**：
   - LibreChat 自身的說明文件和部落格推薦此做法，以防止 HTTP 導致的登出問題。[1]
   - 使用 `mkcert` (一個免費工具) 來為 localhost 產生並信任本機 SSL 憑證：
     - 透過 `brew install mkcert` 安裝 `mkcert` 或從 GitHub 下載。
     - 執行 `mkcert -install` 來安裝根 CA。
     - 建立憑證：`mkcert localhost 127.0.0.1`。
     - 設定 LibreChat (例如透過 Docker 環境變數或設定檔) 使用這些憑證：在你的 `.env` 檔案或環境中新增 `HTTPS=true`、`SSL_CRT_FILE=/path/to/localhost.pem` 和 `SSL_KEY_FILE=/path/to/localhost-key.pem`。
     - 重新啟動 LibreChat 並透過 `https://localhost:3080` 存取。
     - Safari 現在會將其視為安全來源，允許無縫登入。

2. **替代方案：使用 127.0.0.1 代替 localhost**：
   - Safari 有時對 `localhost` 的行為會有所不同 (由於 IPv6 或 DNS 解析問題)。嘗試存取 `http://127.0.0.1:3080` – 這在某些情況下解決了類似的連線問題，但可能無法完全解決驗證持續性的問題。[4][4][5]

3. **清除 Safari 中 localhost 的網站資料**：
   - 前往 Safari > 偏好設定 > 隱私權 > 管理網站資料 > 搜尋 "localhost" > 移除任何項目。
   - 這會強制 Safari 停止強制升級至 HTTPS 或快取不安全的環境。[3][2]
   - 重新啟動 Safari 並測試；如果 LibreChat 支援，驗證狀態應該會保持。

如果以上方法都無效，請檢查 LibreChat 的記錄檔以尋找驗證錯誤，確保你的 `.env` 檔案中沒有衝突的標記 (例如，如果需要，`ALLOW_ANONYMOUS=true` 會完全停用驗證)，並確認你沒有使用 Safari 的私密瀏覽模式，該模式會阻擋持續性儲存。[6][7] 如果問題仍然存在，請提供你的 LibreChat 版本和 .env 設定以進行更深入的疑難排解。

引用文獻：
[1] https://www.librechat.ai/blog/2024-05-16_unsecured_http
[2] https://github.com/danny-avila/LibreChat/discussions/529
[3] https://stackoverflow.com/questions/46394682/safari-keeps-forcing-https-on-localhost
[4] https://superuser.com/questions/30827/safari-is-unable-to-reach-localhost-127-0-0-1
[5] https://apple.stackexchange.com/questions/422556/localhost-has-stopped-working-on-chrome-and-safari-since-upgrading-to-big-sur
[6] https://www.librechat.ai/docs/configuration/authentication
[7] https://discussions.apple.com/thread/255906354