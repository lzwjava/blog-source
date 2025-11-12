---
audio: false
generated: true
lang: hant
layout: post
title: 注入問題
translated: true
type: note
---

Infuse 中出現「在解複用串流時無法開啟輸入串流」錯誤，通常表示應用程式無法正常存取或處理您嘗試串流的影片檔案。既然您是從 Nginx 伺服器串流 `.mkv` 檔案（例如 `http://192.168.1.27/movies/yourfile.mkv`），且 VLC 可正常播放但 Infuse 不行，問題可能源自網路問題、檔案相容性或 Infuse 的特殊限制。以下是疑難排解與修復方法：

### 1. 驗證網路連線能力
Infuse 常因網路中斷或設定錯誤而觸發此錯誤。
- **測試可存取性**：從您的 iPad（或執行 Infuse 的裝置）確認網址可連：
  - 開啟 Safari 並前往 `http://192.168.1.27/movies/`，應能看到檔案列表。
  - 點擊 `yourfile.mkv` — 可能無法播放，但請確認連結可連通。
- **對伺服器執行 Ping**：在 iPad 上使用 **Network Ping Lite**（App Store 免費軟體）對 `192.168.1.27` 執行 ping。若失敗，請檢查 Wi-Fi 或伺服器防火牆。
- **防火牆檢查**：在 Ubuntu 伺服器上：
  ```bash
  sudo ufw status
  ```
  確認連接埠 80 已開啟（`80/tcp ALLOW`）。若未開啟：
  ```bash
  sudo ufw allow 80
  sudo systemctl restart nginx
  ```

### 2. 重新啟動 Infuse 與裝置
暫時性故障可能引發此錯誤。
- **關閉 Infuse**：雙擊 Home 鍵（或在新款 iPad 上向上滑動）並滑掉 Infuse。
- **重新開啟**：啟動 Infuse 並重試串流。
- **重新啟動 iPad**：長按電源鍵，滑動關機，然後重新啟動。再次測試。

### 3. 檢查檔案相容性
雖然 Infuse 支援 `.mkv`，但錯誤可能與檔案的編解碼器或結構有關。
- **測試其他檔案**：上傳一個小型、確認可運作的 `.mkv`（例如使用 H.264 影片與 AAC 音訊編碼）至 `/var/www/movies/`：
  ```bash
  sudo mv /path/to/testfile.mkv /var/www/movies/
  sudo chown www-data:www-data /var/www/movies/testfile.mkv
  sudo chmod 644 /var/www/movies/testfile.mkv
  ```
  嘗試在 Infuse 中串流 `http://192.168.1.27/movies/testfile.mkv`。
- **編解碼器檢查**：既然 VLC 可播放，檔案應可串流，但 Infuse 可能對冷門編解碼器（如 VP9、Opus）相容性較差。使用 Mac 上的 VLC 檢查：
  - 開啟 `.mkv`，按下 `Cmd + I`（工具 > 編解碼器資訊），記下影片/音訊編解碼器。
  - 若非 H.264/AAC，請使用 HandBrake（免費，handbrake.fr）重新編碼：
    - 載入 `.mkv`，選擇「H.264 (x264)」影片與「AAC」音訊，然後轉換。

### 4. 調整 Nginx 設定
Infuse 可能需要特定標頭或設定以實現順暢串流。
- **更新設定**：編輯 Nginx 檔案（例如 `/etc/nginx/sites-enabled/default`）：
  ```nginx
  server {
      listen 80;
      server_name 192.168.1.27 localhost;

      location /movies/ {
          alias /var/www/movies/;
          autoindex on;
          add_header Accept-Ranges bytes;  # 確保範圍請求運作
          add_header Content-Disposition "inline";  # 輔助串流
      }
  }
  ```
- **重新載入**：
  ```bash
  sudo nginx -t
  sudo systemctl reload nginx
  ```
- **原因**：`Accept-Ranges` 確保 Infuse 可請求檔案部分內容（對串流至關重要）。

### 5. 提交診斷報告
Infuse 開發者建議對持續性問題執行此操作。
- **步驟**：
  1. 在 Infuse 中，前往 **設定 > 一般**。
  2. 點擊 **提交診斷報告**。
  3. 記下提供的代碼。
  4. 造訪 [Firecore 社群論壇](https://community.firecore.com/)，貼出代碼並描述您的設定（Nginx、`.mkv`、HTTP 串流）。
- **原因**：他們可精確判斷是否為錯誤或設定問題。

### 6. 替代解決方案
若 Infuse 持續失敗：
- **使用 VLC**：在 iPad 上持續使用 VLC for Mobile（因其運作可靠）。
- **切換應用程式**：嘗試使用 **nPlayer** 或 **PlayerXtreme**（App Store）開啟相同網址。

### 可能原因
既然 VLC 可正常串流，很可能為網路瞬斷或 Infuse 對 HTTP 串流的處理較嚴格。Nginx 調整（步驟 4）與測試檔案（步驟 3）通常可解決此問題。若仍無效，診斷報告將提供進一步說明。

請告知嘗試這些步驟後的結果 — 特別是任何記錄錯誤或診斷代碼！