---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 釋放 macOS 系統儲存空間
translated: true
type: note
---

### macOS 系統儲存空間清理概覽

根據 Apple 官方指引與專家建議，釋放 macOS（如您使用的 15.6.1 版本）儲存空間可透過內建工具優化儲存、安全清除可移除快取及刪除不必要的檔案。系統資料通常包含快取、暫存檔與日誌檔——多數內容可手動或自動清除而不損害 Mac。請避免刪除關鍵系統檔案，以免導致系統不穩定。您的系統顯示約 13 GiB 可用空間（總容量 460 GiB），使用率達 45%，建議優先處理快取、下載項目與附件以快速釋放空間。[1][2][3]

### 使用 macOS 內建儲存管理工具
Apple 提供整合式空間分析與釋放功能，無需第三方應用程式。
1. **檢查儲存使用量**：前往 Apple 選單 > 系統設定 > 一般 > 儲存空間。此處會顯示顏色分類的空間分佈（如應用程式、文件、系統資料），點擊任一類別可查看建議。[1]
2. **自動優化儲存空間**：在儲存空間設定中啟用「最佳化儲存空間」，自動卸載未使用的應用程式資料並管理附件。同時開啟「自動清倒垃圾桶」功能（設定為 30 天後執行）。[1]
3. **清空垃圾桶與下載項目**：系統資料包含垃圾桶內容——請從 Finder 手動清空。檢查 ~/Downloads 資料夾中的舊檔案並刪除。[1][2]
4. **管理大型附件**：前往儲存空間設定 > 應用程式 > 管理 > Mail >「最佳化儲存空間」，設定僅在需要時下載大型電郵附件。[1]

如需深度清理，可在儲存空間設定的「先前項目」分頁檢視近期備份（如 Time Machine 備份），並在不需要時移除。[2]

### 識別與清除可移除快取檔案
快取是加速應用程式運作的暫存檔，但可能累積達數 GB。可透過 Finder 安全清除使用者層級快取；除非依 Apple 支援指引，否則請避免清理系統層級快取以防問題發生。您的 Mac 快取存放於資源庫資料夾——可使用 Finder 的「取得資訊」檢查大小。

1. **使用者快取目錄（最安全清理範圍）**：
   - 開啟 Finder > 前往 > 前往檔案夾，輸入 `~/Library/Caches` 後按 Enter。
   - 此資料夾包含應用程式快取（如瀏覽器、Office 應用程式）。選取內部所有資料夾並刪除，這些檔案多數可安全清除且會自動重新生成。
   - 提示：可檢查 `com.apple.* 等子資料夾中的 Apple 應用程式快取，但不確定時請跳過。完成後請清空垃圾桶。[4][2]

2. **應用程式特定快取**：
   - 瀏覽器：在 Safari 中透過 Safari 選單 > 清除歷史紀錄來清理快取。Chrome/Google 應用程式：前往 Chrome > 設定 > 隱私權 > 清除瀏覽資料。
   - Xcode/開發者工具：若您進行編程，可在 Xcode > 偏好設定 > Locations > Derived Data 清除衍生資料。
   - 其他應用程式：檢查應用程式偏好設定中的快取清理選項，或透過 Finder 檢視 `~/Library/Caches` 子資料夾。[2][3]

3. **系統與資源庫快取（請謹慎操作）**：
   - `/Library/Caches` 可能包含系統快取——僅可刪除特定資料夾（如過時應用程式快取），避免清除核心系統檔案（例如請勿刪除 `com.apple.coreservices`）。
   - 若要安全分析大小，可透過 Terminal 列出大型快取：開啟 Terminal 執行 `du -sh /Library/Caches/* | sort -h`。
   - 深度系統快取的最終處理方式：重啟至恢復模式（開機時按 Command+R），執行磁碟工具程式 > 修理工具，之後重啟並使用儲存空間管理工具。[2]

### 手動安全清理的補充技巧
- **移除暫存與日誌檔案**：系統資料包含 `/private/var/log` 中的日誌檔。可使用 Terminal 指令如 `sudo rm -rf /private/var/log/asl/*.asl` 清理舊版 Apple 日誌（請先登出並重新登入）。對於暫存檔，可在檢查後透過 `sudo rm -rf /tmp/*` 刪除 `/tmp` 內容。[2]
- **移轉至外部儲存**：透過儲存空間設定 >「儲存在 iCloud」將照片/影片移至 iCloud 或外接硬碟。[1]
- **安全分析工具**：第三方工具如 CleanMyMac（來自 MacPaw）或 OmniDiskSweeper 可掃描大型快取/檔案——使用這些工具作為指引，但務必先進行備份（例如透過 Time Machine）。[3]
- **清理後監控**：執行大量刪除後請重新開機重整系統。再次檢查儲存空間使用狀況；可重新生成的快取刪除不應影響效能。[2]

若系統資料仍佔用過高空間（如部分案例中的 218 GB），可能是隱藏備份或損毀檔案——Apple 支援建議在 Terminal 執行 `tmutil thinlocalsnapshots / 10000000000 4` 進行 Time Machine 清理。[5] 進行操作前請確保已備份資料。這些方法應能在如您使用的 M2 等 Apple Silicon Mac 上安全回收顯著空間。[1][2][4]

參考文獻：
[1] https://support.apple.com/en-us/102624
[2] https://macpaw.com/how-to/clear-system-storage-mac
[3] https://nektony.com/how-to/clean-up-system-storage-on-mac?srsltid=AfmBOorJjQPPX59Jw3MM47n0NZ8DQlerYQAbkZdymj0rUZM0rtLZlw1s
[4] https://www.reddit.com/r/MacOS/comments/154rp99/how_to_do_i_clear_system_data_on_mac_os/
[5] https://discussions.apple.com/thread/255084458