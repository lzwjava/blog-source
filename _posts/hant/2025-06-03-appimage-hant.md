---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 上安裝 AppImage
translated: true
type: note
---

要在 Ubuntu 上安裝並執行 AppImage 檔案，請按照以下步驟操作：

1. **下載 AppImage**：
   - 從應用程式的官方網站或可信來源取得 `.AppImage` 檔案。

2. **設定檔案可執行權限**：
   - 開啟終端機並導覽至包含 AppImage 的目錄：
     ```bash
     cd /path/to/directory
     ```
   - 變更檔案權限使其可執行：
     ```bash
     chmod +x filename.AppImage
     ```
     請將 `filename.AppImage` 替換為您實際的 AppImage 檔案名稱。

3. **執行 AppImage**：
   - 透過以下指令執行 AppImage：
     ```bash
     ./filename.AppImage
     ```
   - 或者，若檔案在檔案管理器中已標記為可執行，您也可以直接雙擊該檔案。

4. **選項：與系統整合**：
   - 部分 AppImage 會自動與系統整合（例如新增桌面項目）。若未整合，您可能需要使用整合選項執行 AppImage（請查閱應用程式文件，有些支援 `./filename.AppImage --install`）。
   - 若要手動建立桌面項目，可使用 `menulibre` 等工具，或在 `~/.local/share/applications/` 目錄中建立 `.desktop` 檔案。

5. **管理 AppImage**：
   - 由於 AppImage 具有可攜性，無需安裝。您可以將檔案移動到偏好的位置（例如 `~/Applications/`）。
   - 更新時，只需下載最新版本的 AppImage 並替換舊檔案。
   - 移除時，直接刪除 `.AppImage` 檔案即可。

**注意事項**：
- 請確保 AppImage 來自可信來源，以避免安全風險。
- 若遇到問題，請檢查是否已安裝依賴項目（如 `libfuse2`）：
  ```bash
  sudo apt install libfuse2
  ```
- 執行 AppImage 通常不需要 root 權限。

如果您有特定的 AppImage 或遇到問題，請告訴我以獲得針對性的協助！