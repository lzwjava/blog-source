---
audio: false
generated: true
lang: hant
layout: post
title: 使用 VLC 從 Nginx 串流 MKV 檔案
translated: true
type: note
---

既然你有一台提供 `.mkv` 檔案服務的 Nginx 伺服器（例如在 `http://192.168.1.27/movies/`），並且你想在 Mac 上觀看這些檔案而不需要下載整個檔案，那麼你正在尋找**串流**播放影片的方法。Nginx 預設支援 HTTP 範圍請求（range requests），這使得媒體播放器能夠進行串流播放而非完整下載。以下是具體操作方法，以及適用於 macOS 的合適工具。

### 先決條件
- 你的 Nginx 配置（例如 `alias /var/www/movies/; autoindex on;`）正常運作，並且 `http://192.168.1.27/movies/` 能列出檔案。
- `.mkv` 檔案可透過網路存取（已從其他機器測試過）。

### 在 macOS 上串流播放 `.mkv` 檔案的工具
你需要一個支援透過 HTTP 串流播放並能良好處理 `.mkv` 檔案的媒體播放器。以下是最佳選擇：

#### 1. VLC Media Player（免費，推薦）
VLC 是一款多功能、開源的播放器，支援透過 HTTP 串流播放 `.mkv` 檔案而無需下載整個檔案（它使用範圍請求）。
- **安裝**：
  - 從 [videolan.org](https://www.videolan.org/vlc/) 下載。
  - 在你的 Mac 上安裝。
- **串流播放**：
  1. 開啟 VLC。
  2. 按下 `Cmd + N`（或前往 `檔案 > 開啟網路串流`）。
  3. 輸入 URL，例如 `http://192.168.1.27/movies/yourfile.mkv`。
  4. 點擊 `開啟`。
- **為何可行**：VLC 僅緩衝所需部分，讓你可以跳轉和播放，而無需下載整個檔案。

#### 2. IINA（免費，macOS 原生風格）
IINA 是一款現代化、專為 macOS 設計的播放器，具有出色的 `.mkv` 支援和串流功能。
- **安裝**：
  - 從 [iina.io](https://iina.io/) 下載，或使用 `brew install iina`（透過 Homebrew）。
- **串流播放**：
  1. 開啟 IINA。
  2. 按下 `Cmd + U`（或 `檔案 > 開啟 URL`）。
  3. 輸入 `http://192.168.1.27/movies/yourfile.mkv`。
  4. 點擊 `確定`。
- **為何可行**：輕量、支援 HTTP 串流，並與 macOS 良好整合。

#### 3. QuickTime Player（內建，功能有限）
macOS 預設的 QuickTime Player 可以串流播放某些格式，但對 `.mkv` 的支援不穩定，需要額外的編解碼器。
- **試用**：
  1. 開啟 QuickTime Player。
  2. 按下 `Cmd + U`（或 `檔案 > 開啟位置`）。
  3. 輸入 `http://192.168.1.27/movies/yourfile.mkv`。
  4. 點擊 `開啟`。
- **注意事項**：如果無法播放，請安裝 Perian（舊版編解碼器包）或改用 VLC/IINA。

#### 4. 瀏覽器（Safari/Chrome，最簡單）
現代瀏覽器可以直接串流播放 `.mkv` 檔案，前提是這些檔案使用支援的編解碼器編碼（例如 H.264 影片、AAC 音訊）。
- **方法**：
  1. 在 Mac 上開啟 Safari 或 Chrome。
  2. 前往 `http://192.168.1.27/movies/`。
  3. 點擊 `yourfile.mkv`。
- **為何可行**：瀏覽器使用 HTML5 影片標籤和範圍請求進行串流播放。
- **限制**：如果 `.mkv` 使用不支援的編解碼器（例如 VP9、Opus），則無法播放——請改用 VLC 或 IINA。

### 確保 Nginx 支援串流播放
Nginx 預設處理範圍請求，這正是實現串流播放的關鍵。請確認：
- 檢查你的配置未禁用此功能（例如沒有 `limit_rate` 或自訂標頭阻擋範圍請求）。
- 使用 VLC 或 IINA 進行測試——如果你可以跳轉（例如跳到 5 分鐘處），則表示串流播放正常運作。

### 推薦工作流程
1. **使用 VLC**（最可靠）：
   - 安裝 VLC。
   - 透過 `Cmd + N` 開啟 `http://192.168.1.27/movies/yourfile.mkv`。
   - 根據需要播放、暫停或跳轉。
2. **目錄瀏覽**：
   - 在 Safari/Chrome 中訪問 `http://192.168.1.27/movies/` 以查看檔案列表（感謝 `autoindex on;`）。
   - 複製 `yourfile.mkv` 的 URL 並貼上到 VLC 或 IINA 中。

### 疑難排解
- **緩衝問題**：網路速度慢或大型 `.mkv` 檔案可能導致延遲——請確保你的區域網路穩定（例如 Wi-Fi 沒有斷線）。
- **編解碼器錯誤**：如果 VLC 顯示「不支援的格式」，該 `.mkv` 可能使用罕見的編解碼器——嘗試使用 HandBrake 重新編碼為 H.264/AAC。
- **連線被拒絕**：請重新檢查伺服器上的防火牆設定（`sudo ufw allow 80` 或等效指令）。

使用 VLC 或 IINA，你很快就能在 Mac 上串流播放你的 `.mkv` 檔案，而無需完整下載。如果你遇到任何問題，請告訴我！

---

在 Mac 上安裝 VLC 非常簡單。以下是一個快速指南，幫助你設定好 VLC，以便從你的 Nginx 伺服器串流播放 `.mkv` 檔案：

### 方法 1：從官方網站下載
1. **訪問 VLC 網站**：
   - 開啟你的瀏覽器（例如 Safari 或 Chrome）。
   - 前往 [https://www.videolan.org/vlc/](https://www.videolan.org/vlc/)。

2. **下載 VLC**：
   - 點擊 **Download VLC** 按鈕。它應該會自動偵測你的 macOS 並提供正確的版本（例如目前是 VLC 3.0.20）。
   - 你將獲得一個 `.dmg` 檔案（例如 `vlc-3.0.20.dmg`）。

3. **安裝 VLC**：
   - 開啟下載的 `.dmg` 檔案（通常在 `下載` 資料夾中）。
   - 按照視窗中的提示，將 VLC 圖示拖曳到 **應用程式** 資料夾。
   - 關閉 `.dmg` 視窗並退出它（在桌面或 Finder 中右鍵點擊磁碟圖示並選擇「退出」）。

4. **執行 VLC**：
   - 前往你的 **應用程式** 資料夾（例如透過 Finder 或使用 `Cmd + Space` 開啟 Spotlight，然後輸入「Applications」）。
   - 雙擊 **VLC**。
   - 如果 macOS 阻擋它（「未識別的開發者」），請右鍵點擊 VLC，選擇 **開啟**，然後在對話框中點擊 **開啟**。

5. **串流播放你的檔案**：
   - 開啟 VLC。
   - 按下 `Cmd + N`（或 `檔案 > 開啟網路串流`）。
   - 輸入 `http://192.168.1.27/movies/yourfile.mkv`。
   - 點擊 **開啟**。

### 方法 2：透過 Homebrew 安裝（終端機）
如果你偏好命令列且已安裝 Homebrew：
1. **安裝 Homebrew**（如果尚未安裝）：
   - 開啟 Terminal。
   - 執行：
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - 按照提示操作。

2. **安裝 VLC**：
   - 在 Terminal 中：
     ```bash
     brew install vlc
     ```

3. **執行 VLC**：
   - 從 Terminal 啟動：
     ```bash
     open -a VLC
     ```
   - 或在 **應用程式** 中找到 `VLC.app`。

4. **串流播放**：
   - 同上：`Cmd + N`，輸入你的 URL，然後播放。

### 驗證安裝
- 安裝完成後，VLC 應該會出現在你的 **應用程式** 資料夾中。
- 首先使用本地檔案測試（將一個 `.mkv` 檔案拖曳到 VLC 中）以確保其運作正常，然後嘗試串流播放 `http://192.168.1.27/movies/yourfile.mkv`。

### 疑難排解
- **下載失敗**：如果主要下載速度慢，請使用 VLC 網站上的鏡像連結。
- **安全性提示**：如果 macOS 阻擋它，請前往 `系統設定 > 安全性與隱私權 > 一般` 並點擊 **強制開啟**。
- **無法播放**：請確保 URL 正確且你的伺服器可連線（從 Terminal 執行 `ping 192.168.1.27`）。

就是這樣！VLC 現在應該已經在你的 Mac 上準備好串流播放你的 `.mkv` 檔案了。如果你需要下一步的幫助，請告訴我！