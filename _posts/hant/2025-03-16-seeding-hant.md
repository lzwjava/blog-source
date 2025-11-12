---
audio: false
generated: true
lang: hant
layout: post
title: 配置 qBittorrent 進行做種與自動檔案管理
translated: true
type: note
---

看來您想設定 qBittorrent 在持續做種的同時，自動將已完成的 `.mkv` 檔案移至 `/var/www/movies` 目錄以供伺服器使用。以下將逐步指導您完成設定，假設您是在 `/var/www/movies` 為有效目錄的系統上使用 qBittorrent（例如使用 Apache 或 Nginx 網頁伺服器的 Linux 伺服器）。設定方式如下：

---

### 逐步設定指南

#### 1. **了解 qBittorrent 的檔案管理機制**
   - qBittorrent 可在下載完成後自動移動檔案並持續做種，前提是您需正確使用內建的「設定位置」或「移動」功能。若在 qBittorrent 外部手動移動檔案（例如透過檔案總管），將會中斷做種，除非您重新指向新位置。

#### 2. **設定 qBittorrent 選項**
   - 開啟 qBittorrent。
   - 前往 **工具 > 選項**（或按下 `Alt + O`）。

   ##### a) **設定預設下載位置**
   - 在 **下載** 分頁下：
     - 將 **預設儲存路徑** 設為暫存目錄，用於初始下載（例如 `/home/user/downloads` 或任何有空間的位置）。此處將作為檔案下載及做種時的暫存位置，直到檔案被移動。
     - 可選設定：如需將未完成檔案存放在不同位置，可設定 **將未完成檔案儲存於** 選項。

   ##### b) **啟用自動移動檔案功能**
   - 向下滾動至 **當 Torrent 完成時**：
     - 勾選 **自動將已完成下載移至**。
     - 將路徑設為 `/var/www/movies`，這會指示 qBittorrent 在下載完成後將 `.mkv` 檔案移至 `/var/www/movies`。
   - 重要提示：qBittorrent 在移動後會從新位置 (`/var/www/movies`) 繼續做種，無需擔心影響做種能力。

   ##### c) **可選：僅篩選 .mkv 檔案**
   - 若您只想移動 `.mkv` 檔案至 `/var/www/movies`（而不移動其他檔案類型如 `.txt` 或 `.nfo`），可改用 qBittorrent 的 **執行外部程式** 功能（見下方步驟 3）。

   ##### d) **設定做種限制**
   - 在 **BitTorrent** 或 **下載** 分頁下：
     - 依需要設定做種限制（例如達到特定分享率或時間後停止）。若需無限做種，將 **分享率** 與 **時間** 設為 `0` 或取消勾選限制。
     - 這能確保 qBittorrent 從 `/var/www/movies` 持續上傳做種。

   - 點擊 **套用** 與 **確定** 儲存設定。

#### 3. **替代方案：使用「執行外部程式」以獲得更多控制**
   - 若需更高自訂性（例如僅移動 `.mkv` 檔案，其餘檔案保留在原位置做種）：
     - 在 **選項 > 下載** 中，滾動至 **執行外部程式**。
     - 勾選 **當 Torrent 完成時執行外部程式**。
     - 輸入如下指令：
       ```
       mv "%F"/*.mkv /var/www/movies/
       ```
       - `%F` 是 qBittorrent 的佔位符，代表內容資料夾路徑。此指令僅移動 `.mkv` 檔案至 `/var/www/movies`。
     - 注意：qBittorrent 在移動後仍會從 `/var/www/movies` 為 `.mkv` 檔案做種，但其他檔案（如 `.torrent`、`.nfo`）將保留在原位置並繼續做種，除非您進一步調整。

#### 4. **確認權限設定**
   - 確保 qBittorrent 對 `/var/www/movies` 具寫入權限：
     - 在 Linux 上執行：
       ```
       sudo chown -R <qbittorrent-user>:<qbittorrent-group> /var/www/movies
       sudo chmod -R 775 /var/www/movies
       ```
       將 `<qbittorrent-user>` 與 `<qbittorrent-group>` 替換為執行 qBittorrent 的使用者及群組（例如您的使用者名稱或服務帳號 `qbittorrent`）。
   - 若權限不足，qBittorrent 將無法移動檔案至此目錄。

#### 5. **測試設定**
   - 在 qBittorrent 中加入包含 `.mkv` 檔案的 torrent。
   - 等待下載完成。
   - 確認：
     - `.mkv` 檔案已移至 `/var/www/movies`。
     - qBittorrent 中的 torrent 狀態轉為 **做種**，且上傳速度顯示仍在分享檔案。
   - 檢查 `/var/www/movies` 確認檔案存在且可存取（例如透過網頁伺服器網址 `http://<伺服器-ip>/movies`）。

#### 6. **手動移動現有檔案（如需）**
   - 若您已下載的 torrent 需移至 `/var/www/movies` 且不中斷做種：
     - 在 qBittorrent 中，右鍵點擊 torrent。
     - 選擇 **設定位置**。
     - 選擇 `/var/www/movies` 並讓 qBittorrent 移動檔案。
     - 移動後，qBittorrent 將從新位置繼續做種。

#### 7. **最佳化上傳設定**
   - 為最大化做種效率：
     - 前往 **選項 > 速度**：
       - 將 **上傳** 設為 `0`（無限制）或較高值（例如最高上傳速度的 80%）。
     - 前往 **選項 > 連線**：
       - 確保勾選 **啟用 UPnP / NAT-PMP 通訊埠轉送**（若路由器支援），或手動轉送通訊埠以改善連線能力。
       - 增加 **全域最大上傳槽數**（例如設為 50 或 100），允許更多節點連線。

---

### 關鍵注意事項
- **做種連續性**：只要您讓 qBittorrent 處理檔案移動（透過自動移動或「設定位置」），它將更新內部追蹤並從 `/var/www/movies` 繼續做種。
- **網頁伺服器存取**：請確保您的網頁伺服器（如 Apache/Nginx）已設定為從 `/var/www/movies` 提供檔案。此部分雖超出 qBittorrent 範圍，但對實現伺服器目標至關重要。
- **儲存空間**：確認 `/var/www/movies` 有足夠空間容納檔案。

若遇到問題（例如檔案未移動或做種中斷），請提供您的設定詳情（作業系統、qBittorrent 版本等），我將協助進一步調整解決方案！