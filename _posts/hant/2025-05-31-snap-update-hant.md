---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 上透過 Snap 更新 VSCode
translated: true
type: note
---

若要更新透過 Snap 在 Ubuntu 上安裝的 Visual Studio Code (VSCode)，請遵循以下步驟：

1. **開啟終端機**：您可以按 `Ctrl + Alt + T` 來開啟。

2. **檢查更新**：Snap 會自動在背景檢查更新，但您也可以手動觸發更新檢查，執行：
   ```bash
   sudo snap refresh
   ```

3. **更新 VSCode**：如果有新版本的 VSCode 可用，`snap refresh` 指令將會下載並安裝它。您會看到顯示進度的輸出，例如：
   ```
   code 1.85.2 from Visual Studio Code (code✓) refreshed
   ```
   如果沒有可用更新，則會顯示：
   ```
   所有 snap 套件均已是最新版本。
   ```

4. **驗證更新**：要確認 VSCode 的安裝版本，請執行：
   ```bash
   code --version
   ```
   這將顯示 VSCode 的目前版本。

### 注意事項：
- **自動更新**：Snap 套件（包括 VSCode）通常會在背景自動更新。除非您想強制更新，否則通常無需手動介入。
- **root 權限**：系統範圍的 Snap 操作需要 `sudo` 指令。
- **檢查 Snap 狀態**：如果想查看已安裝的 Snap 套件及其版本，請使用：
   ```bash
   snap list
   ```
- **疑難排解**：如果更新失敗，請確保您的網路連線穩定，且 Snap 常駐程式正在執行（`sudo systemctl status snapd`）。您也可以嘗試重新整理 Snap 元數據：
   ```bash
   sudo snap refresh --list
   ```

此流程可確保 VSCode 持續更新至 Snap Store 中可用的最新版本。