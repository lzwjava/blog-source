---
audio: false
generated: true
lang: hant
layout: post
title: 在 iPad 上使用 VLC Mobile 及其他應用程式串流 MKV 檔案
translated: true
type: note
---

要從你的 Nginx 伺服器（例如 `http://192.168.1.27/movies/`）在 iPad 上串流播放 `.mkv` 檔案而不需完整下載，你需要一個支援 HTTP 串流和 `.mkv` 播放的應用程式。iPadOS 在 Safari 或檔案應用程式中無法原生處理 `.mkv` 檔案，因此第三方媒體播放器是解決方案。以下是如何在 iPad 上實現這種「魔法」：

### 推薦用於在 iPad 上串流播放 `.mkv` 的應用程式
#### 1. VLC for Mobile（免費，最佳選擇）
VLC 可在 iPadOS 上使用，功能與 Mac 版本相似，支援帶有範圍請求的 HTTP 串流。
- **安裝**：
  1. 在 iPad 上開啟 **App Store**。
  2. 搜尋 **VLC for Mobile**。
  3. 點擊 **取得**（如果你之前安裝過，則點擊雲端圖示），然後根據提示使用你的 Apple ID 進行驗證。
- **串流**：
  1. 開啟 **VLC** 應用程式。
  2. 點擊底部的 **Network** 標籤（圓錐圖示）。
  3. 選擇 **Open Network Stream**。
  4. 輸入 `http://192.168.1.27/movies/yourfile.mkv`。
  5. 點擊 **Open Network Stream**（或播放按鈕）。
- **為何有效**：VLC 會緩衝串流，讓你可以播放和搜尋而不需下載整個檔案。

#### 2. nPlayer（付費，高級選擇）
nPlayer 是一個功能強大的媒體播放器，具有出色的 `.mkv` 支援和串流能力。
- **安裝**：
  1. 開啟 **App Store**。
  2. 搜尋 **nPlayer**（價格約為 $8.99，但也有帶廣告的免費精簡版）。
  3. 點擊 **取得** 或 **購買**，然後安裝。
- **串流**：
  1. 開啟 **nPlayer**。
  2. 點擊 **+** 圖示或 **Network** 選項。
  3. 選擇 **Add URL** 或 **HTTP/HTTPS**。
  4. 輸入 `http://192.168.1.27/movies/yourfile.mkv`。
  5. 點擊 **Play**。
- **為何有效**：支援高級編解碼器和流暢串流；適合 iPad 的優秀用戶界面。

#### 3. Infuse（免費，含應用程式內購買）
Infuse 是另一個受歡迎的串流和播放 `.mkv` 檔案的選擇，具有時尚的界面。
- **安裝**：
  1. 開啟 **App Store**。
  2. 搜尋 **Infuse**。
  3. 點擊 **取得**（免費版本適用於基本串流；Pro 升級為可選）。
- **串流**：
  1. 開啟 **Infuse**。
  2. 點擊 **Add Files** > **Via URL**。
  3. 輸入 `http://192.168.1.27/movies/yourfile.mkv`。
  4. 點擊 **Add** 或 **Play**。
- **為何有效**：透過 HTTP 串流並能良好處理 `.mkv`；Pro 功能（如 AirPlay）為可選。

### 開始使用的步驟
1. **連接到同一網絡**：
   - 確保你的 iPad 與 Nginx 伺服器處於同一 Wi-Fi 網絡（例如 `192.168.1.x`）。
   - 測試連接：在 iPad 上開啟 Safari 並前往 `http://192.168.1.27/movies/`。你應該能看到檔案列表（即使 Safari 無法播放 `.mkv`）。

2. **選擇一個應用程式**：
   - **VLC** 免費且可靠——從這裡開始。
   - 按照上述說明從 App Store 安裝。

3. **輸入 URL**：
   - 使用你的 `.mkv` 檔案的確切 URL（例如 `http://192.168.1.27/movies/yourfile.mkv`）。
   - 你可以從 Safari 的檔案列表中複製連結並貼到應用程式中。

4. **播放並享受**：
   - 應用程式將串流播放影片。你可以暫停、搜尋或調整播放而不需下載整個檔案。

### 疑難排解
- **連接失敗**：如果 iPad 無法連接到 `192.168.1.27`，請確保伺服器的防火牆允許端口 80（`sudo ufw allow 80`）且 iPad 處於同一區域網絡。
- **緩衝**：Wi-Fi 速度慢可能導致延遲——靠近路由器或檢查網絡速度。
- **編解碼器問題**：如果 `.mkv` 無法播放，可能使用了不支援的編解碼器（例如 VP9）。VLC 能處理大多數編解碼器，但你可以使用 HandBrake 重新編碼為 H.264/AAC 以獲得更好的兼容性。
- **URL 輸入錯誤**：雙重檢查 IP 和路徑——`http://192.168.1.27/movies/yourfile.mkv` 必須與你的設定匹配。

### 額外技巧：瀏覽和選擇
由於 `autoindex on;` 提供了目錄列表：
- 在 iPad 上開啟 Safari，前往 `http://192.168.1.27/movies/`，點擊檔案連結，然後複製 URL。
- 將其貼到 VLC/nPlayer/Infuse 中進行串流。

使用 **VLC for Mobile**，你很快就能在 iPad 上體驗這種「魔法」——輕鬆串流你的 `.mkv` 檔案！如果你需要設定幫助，請告訴我。