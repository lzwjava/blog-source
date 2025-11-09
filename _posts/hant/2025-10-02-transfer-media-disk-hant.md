---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 將媒體傳輸至外置硬碟
translated: true
type: note
---

### 在 macOS 上將相片和影片移至便攜磁碟

根據你的系統資訊，你使用的是 macOS 15.6.1 系統，並有一個便攜磁碟掛載在 `/Volumes/Untitled`（總容量 2.0 TB，可用空間 1.5 TB）。移動相片和影片涉及將檔案從 Mac 儲存空間（例如相片位於 `~/Pictures`，影片位於 `~/Movies`）傳輸到外接磁碟。這可以透過圖形介面（Finder）或命令列工具（如 Terminal）完成，取決於你的偏好。以下我將介紹兩種方法，假設你是移動檔案而非整個 Photos 應用程式資料庫（如需移動資料庫，請先從 Photos 應用程式匯出）。

**重要注意事項：**
- **先備份：** 確保已備份檔案，以免發生錯誤時遺失資料。
- **權限：** 某些操作可能需要管理員權限。如出現提示，請以管理員身份執行 Terminal 指令。
- **空間檢查：** 確認檔案大小未超過便攜磁碟的可用空間（你的情況為 1.5 TB）。
- **檔案位置：** 預設路徑為相片 `~/Pictures` 和影片 `~/Movies`。如果檔案位於其他目錄（例如 Downloads），請相應調整。
- **安全卸載：** 移動完成後，透過 Finder > 退出或 `diskutil unmount /Volumes/Untitled` 卸載磁碟，以防損壞。

#### 1. 使用 Finder（圖形化方法 - 適合初學者）
這是對大多數用戶最簡單的方式，透過 macOS 的檔案管理器進行拖放操作。

1. **定位便攜磁碟和檔案：**
   - 開啟 Finder（點擊 Dock 中的笑臉圖示）。
   - 在側邊欄的「位置」下，你會看到「Untitled」（你的便攜磁碟）。點擊以瀏覽其內容。
   - 開啟另一個 Finder 視窗（Command + N）並導航至相片/影片的儲存位置（例如你的 Pictures 或 Movies 資料夾）。

2. **移動檔案：**
   - 選擇要移動的相片/影片（按住 Command 可多選）。
   - 將它們從目前位置拖曳至便攜磁碟的視窗中（例如，可先在磁碟上建立「PhotosBackup」資料夾以便整理）。
   - 若要移動（永久重新定位，釋放 Mac 空間），拖曳時按住 Option 鍵。若要複製（建立副本），直接拖曳即可。
     - 或者，在複製後右鍵點選選取的檔案 >「移到垃圾桶」，以透過刪除原始檔案來實現「移動」效果。
   - 如需整理，可在磁碟上建立資料夾（右鍵 > 新增資料夾），例如「Photos」和「Videos」。

3. **驗證和退出：**
   - 在 Finder 中開啟便攜磁碟，確認檔案已存在。
   - 將磁碟圖示拖曳至垃圾桶（或右鍵 > 退出）以安全卸載，然後斷開連接。

此方法可保留元數據（例如建立日期）並能高效處理大型檔案。

#### 2. 使用 Terminal（命令列方法 - 適合批量操作）
如果你偏好使用指令或腳本處理（如你的 Python 腳本所示），可使用 Terminal 進行精確操作。這對自動化或遞歸移動非常有用。

1. **導航至檔案和磁碟位置：**
   - 開啟 Terminal（應用程式 > 工具程式 > Terminal）。
   - 檢查目前目錄：執行 `pwd` 並根據需要導航（例如 `cd ~/Pictures` 以存取相片）。
   - 確認磁碟已掛載：執行 `ls /Volumes` 以查看「Untitled」。根據提供的輸出，你的磁碟已掛載。

2. **移動檔案：**
   - 若要**移動**檔案（永久重新定位，從原始位置刪除）：
     - 單一檔案：`mv /path/to/photo.jpg /Volumes/Untitled/Photos/`
     - 整個目錄（例如整個 Photos 資料夾）：`mv ~/Pictures/PhotosLibrary /Volumes/Untitled/`
     - 完整移動範例：`mv ~/Pictures/* /Volumes/Untitled/Photos/`（將 Pictures 中的所有內容移動到磁碟上的新資料夾；可添加選項如 `-v` 以顯示詳細輸出）。
   - 若要**複製**（建立副本而不刪除原始檔案）：使用 `cp` 並加上 `-r` 以處理遞歸目錄。
     - 範例：`cp -r ~/Pictures/PhotosLibrary /Volumes/Untitled/Photos/`（遞歸複製；適合需保留原始檔案的備份）。
   - 對於 Movies 中的影片：`cp -r ~/Movies/Videos/ /Volumes/Untitled/Videos/`
   - 處理隱藏檔案或權限問題：如需可添加 `sudo`（例如 `sudo mv ~/Pictures/photo.jpg /Volumes/Untitled/`）。
   - 為安全起見，可預覽將移動的檔案：`ls -la ~/Pictures` 以列出檔案。

3. **驗證和卸載：**
   - 檢查磁碟：`ls /Volumes/Untitled` 以確認傳輸完成。
   - 安全卸載：`diskutil unmount /Volumes/Untitled`，然後實體斷開磁碟連接。

**進階提示：**
- **使用 Rsync 進行同步：** 對於增量備份（僅新檔案/變更的檔案），可使用 `rsync -av ~/Pictures /Volumes/Untitled/Photos`（如果未安裝 rsync 請先安裝，但 macOS 內建已有）。
- **自動化：** 將此改編至你的 Python 腳本中（例如使用 `subprocess` 執行 `cp` 或 `mv` 指令，基於 `list_portable_disks.py` 的輸出）。
- **MacBook 特定提示：** 在你的 M2 MacBook Air（型號 Mac14,2）上，透過 USB-C 傳輸應非常快速。如有需要，可監控電池溫度（例如透過 Activity Monitor）。

如果遇到問題（例如權限錯誤），請提供更多詳細資訊（如確切檔案路徑或錯誤訊息）以獲得針對性建議。此流程在你的設定中應能可靠運作。