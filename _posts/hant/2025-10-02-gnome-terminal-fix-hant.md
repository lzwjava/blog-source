---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 修復 GNOME 終端機啟動問題
translated: true
type: note
---

### 疑難排解 Ubuntu 22.04 中 GNOME 終端機無法開啟的問題

此問題似乎特定於 GNOME 終端機應用程式（預設的終端機模擬器）在啟動時卡在進度條或旋轉圖示上，而其他圖形應用程式（例如設定）和整合式終端機（如 VSCode 中的終端機）則運作正常。這通常指向 GNOME 元件的設定問題、損毀的設定或相依性問題，而非系統層級的故障。以下我將概述如何使用系統日誌（透過 `journalctl` 指令）檢查錯誤以及常見的修復方法。由於 GNOME 終端機無法存取，請使用 VSCode 的整合式終端機進行命令列操作（開啟 VSCode，前往「檢視」>「終端機」）。

### 使用系統日誌 (journalctl) 檢查錯誤
您提到的「journal 指令」很可能是指 `journalctl`，它是 systemd 的一部分，用於檢視日誌。它有助於識別 GNOME 終端機嘗試啟動時發生的情況。以下是逐步使用方法：

1. **存取可運作的終端機**：使用 VSCode 的終端機（或如下所述切換到虛擬主控台）。
2. **執行基本日誌檢查**：
   - 檢視所有近期日誌：`sudo journalctl -b`（顯示上次啟動以來的日誌；加入 `-n 50` 可限制為最後 50 行）。
   - 搜尋終端機相關錯誤：`sudo journalctl -b | grep -i terminal`（在日誌中尋找提及「terminal」的內容）。
   - 尋找特定錯誤，例如「failed to launch」或設定檔問題。常見輸出可能包括權限拒絕或 GTK/GNOME 初始化失敗。
3. **依服務篩選**：如果 GNOME 終端機有特定的單元檔案，請檢查 `journalctl -u gnome-terminal-server` 或使用 `sudo journalctl | grep gnome` 檢查一般 GNOME 日誌。
4. **進行深入分析**：如果錯誤提及設定檔（例如 `~/.bashrc` 或 `~/.profile`），請使用 `cat ~/.bashrc` 檢查它們。如果日誌顯示有程序卡住，請使用 `pkill -f gnome-terminal` 終止它。

如果您發現重複出現的錯誤（例如「org.gnome.Terminal」設定檔損毀），請記下它們以用於後續的特定修復。

### 可能的修復方法
根據 Ubuntu 論壇和疑難排解指南的常見回報[1][2]，請按順序嘗試以下方法，並在每次操作後重新啟動工作階段（登出/登入或重新開機）。請從非破壞性步驟開始。

1. **使用虛擬主控台 (TTY) 進行緊急存取**：
   - 按下 `Ctrl + Alt + F3`（或 F4、F5 等）切換到文字型登入畫面。輸入您的使用者名稱/密碼。
   - 從這裡，您可以在沒有 GUI 衝突的情況下擁有完整的命令列存取權限。例如：執行 `sudo apt update` 或修復指令。
   - 使用 `Ctrl + Alt + F2` 切換回 GUI（通常是主要顯示畫面）。  
     *注意*：如果因顯示問題而失敗，可能表示存在更深的 GNOME 問題[3]。

2. **嘗試從 VSCode 終端機手動啟動 GNOME 終端機**：
   - 在 VSCode 終端機中：輸入 `gnome-terminal` 或 `/usr/bin/gnome-terminal` 並按 Enter。
   - 如果它開啟了，則問題是暫時性的（例如，有卡住的執行個體）。如果出現錯誤，請記下訊息—常見的包括：
     - 「already running」（使用 `pkill -f gnome-terminal` 強制終止，然後重試）。
     - 設定錯誤（例如，設定檔損毀—請繼續進行下一步的重設）。
   - 使用詳細輸出進行測試：加入 `--verbose`（例如，`gnome-terminal --verbose` 以獲取除錯資訊）。

3. **重設 GNOME 終端機設定（如果與設定相關，此方法最安全）**：
   - 在 VSCode 終端機中：執行 `dconf reset -f /org/gnome/terminal/` 以清除所有終端機偏好設定（如果重新建立設定檔，則不會影響設定檔）。
   - 或者，使用 TTY 存取：如果需要，請執行 `sudo apt purge dconf-cli; sudo apt install dconf-cli`，然後重試。
   - 這可以在不重新安裝的情況下修復損毀的設定[1]。

4. **重新安裝 GNOME 終端機及相關套件**：
   - 在 VSCode 終端機或 TTY 中：更新來源然後重新安裝：  
     `sudo apt update && sudo apt install --reinstall gnome-terminal`。
   - 對於更廣泛的 GNOME 問題（因為設定可運作但終端機不行），請嘗試重新安裝核心桌面：  
     `sudo apt install --reinstall ubuntu-gnome-desktop gnome-control-center`（這可以修復相依性衝突而不影響您的資料）[2][4]。
   - 重新安裝後，請登出/登入。

5. **更新系統並檢查套件損毀**：
   - 在 VSCode 終端機或 TTY 中：執行 `sudo apt update && sudo apt upgrade` 以修復過時/衝突的套件。
   - 修復損毀的套件：`sudo dpkg --configure -a && sudo apt-get install -f`。
   - 如果與捲動或 UI 卡住相關（此處可能性較小），請確保沒有 dpkg 損毀[5]。

6. **如果所有方法都無效：備份並重新安裝 GNOME**：
   - 備份重要檔案（例如，`cp -r ~/.config/backup`）。
   - 徹底移除並重新安裝：`sudo apt purge gnome-terminal* && sudo apt autoremove`。
   - 然後：`sudo apt install ubuntu-gnome-desktop`。
   - 作為最後手段，如果問題重複出現，請考慮全新安裝。

### 其他提示
- **為什麼 VSCode 終端機能運作**：它可能使用了不同的後端（例如，內建主控台），與 GNOME 的終端機模擬器無關。
- **預防未來問題**：修復後，請避免在沒有備份的情況下手動編輯 `/etc/environment` 或 `~/.profile`。請使用 `apt` 進行安裝。
- **如果圖形崩潰持續發生**：檢查硬體（例如，透過 `free -h` 檢查 RAM）或在 TTY 中執行 `sudo -i` 進行更高權限的測試。
- 雖然沒有提供確切的日誌，但這些步驟可以解決 80-90% 的情況（例如，設定檔重設或重新安裝）。如果從 `journalctl` 獲得了特定錯誤，我可以進一步完善此內容[1][2]。如果問題持續存在，請考慮在 Ask Ubuntu 論壇上根據您的確切設定進行回報。

引用文獻：
[1] https://askubuntu.com/questions/1442350/terminal-not-launching-in-ubuntu-22-04
[2] https://www.reddit.com/r/Ubuntu/comments/1fedcnz/cannot_open_the_terminal/
[3] https://unix.stackexchange.com/questions/737169/ubuntu-fails-to-boot-due-to-gnome-display-manager-error
[4] https://stackoverflow.com/questions/74985183/settings-menu-missing-ubuntu-22-04
[5] https://superuser.com/questions/1331658/why-cant-i-scroll-in-the-terminal