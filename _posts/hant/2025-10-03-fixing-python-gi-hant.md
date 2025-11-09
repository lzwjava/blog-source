---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: 修復損壞的 Python GI 綁定
translated: true
type: note
---

### 更新診斷
根據最新細節，您的 Python 3.13.7 安裝（可能是手動安裝或透過 PPA/原始碼安裝）已損壞系統的 GObject Introspection (GI) 綁定。`gi` 模組的 `_gi` C 擴展是為您發行版預設的 Python（可能是 3.10 或 3.11，依據 `/usr/lib/python` 中的目錄判斷）編譯的，而不是為 3.13 編譯。這導致 `gnome-terminal`（一個 Python 腳本）嘗試載入時出現循環導入錯誤。`/usr/lib/python` 中的多版本設定確認了此不匹配——系統套件如 `python3-gi` 尚未為 3.13 構建（截至 2025 年，對大多數發行版來說它太新了）。

UFW 日誌仍然是無關的雜訊。

### 建議修復：還原至系統預設 Python
最乾淨的解決方案是將 `/usr/bin/python3` 切換回您發行版的預設版本（例如 3.10），然後重新安裝 GI 綁定。這避免了像複製 .so 檔案這樣的駭客方法，後者可能導致不一致。

1. **識別並切換至預設 Python 版本**（如果配置了 `update-alternatives` 則使用它；否則手動建立符號連結）：
   ```
   # 檢查是否設定了 alternatives
   sudo update-alternatives --config python3
   ```
   - 如果它列出選項，請選擇優先級最低的選項（通常是發行版預設，如 3.10）。
   - 如果沒有 alternatives（在標準 Ubuntu 上常見），手動還原：
     ```
     # 假設預設是 3.10（Ubuntu 22.04 常見；如果您的基礎是 3.11，則替換為 3.11）
     sudo rm /usr/bin/python3
     sudo ln -s /usr/bin/python3.10 /usr/bin/python3
     ```
   - 驗證：`python3 --version` 現在應顯示 3.10.x（或您的預設版本）。

2. **重新安裝 GI 和 GNOME Terminal 套件**：
   ```
   sudo apt update
   sudo apt install --reinstall python3-gi gir1.2-glib-2.0 gnome-terminal
   ```

3. **測試**：
   ```
   python3 -c "from gi.repository import GLib, Gio; print('GI OK')"
   gnome-terminal
   ```
   - 如果 Python 測試通過但終端機仍然失敗，請重設其配置：`dconf reset -f /org/gnome/terminal/`。

### 如果您想保留 Python 3.13
- 這會比較棘手，因為官方 `python3-gi` 尚未為 3.13 提供。您需要從原始碼編譯 PyGObject：
  1. 安裝建置依賴：`sudo apt install libgirepository1.0-dev libcairo2-dev pkg-config python3.13-dev`。
  2. 下載並建置 PyGObject：遵循[官方指南](https://pygobject.gnome.org/install.html)，使用 `--prefix=/usr/local`。
  3. 但這有損壞其他系統工具的風險——如果出現問題，請還原。
- 或者，以駭客方式複製 `_gi` 擴展（不建議長期使用）：
  ```
  cd /usr/lib/python3/dist-packages/gi/
  sudo cp _gi.cpython-3[01]m*.so _gi.cpython-313m-x86_64-linux-gnu.so  # 將 '3[01]' 調整為您的預設版本（3.10 或 3.11）
  ```
  然後如上所述重新安裝 `python3-gi`。

### 預防措施
- 不要手動覆蓋 `/usr/bin/python3`——對於需要 3.13 的專案，請使用虛擬環境（`python3 -m venv myenv`）。
- 如果您透過 deadsnakes PPA 安裝了 3.13，請移除它並堅持使用發行版的 Python。

如果這無法修復問題，請執行 `ls -l /usr/bin/python*` 和 `dpkg -l | grep python3 | grep -E 'gi|default'` 並分享輸出。

[gnome-terminal will not start after trying to install newer version of Python 3](https://askubuntu.com/questions/880188/gnome-terminal-will-not-start-after-trying-to-install-newer-version-of-python-3)  
[ImportError: cannot import name '_gi' from partially initialized module 'gi'](https://stackoverflow.com/questions/59838238/importerror-cannot-import-name-gi-from-partially-initialized-module-gi-mo)  
[Why won't terminal open?](https://www.reddit.com/r/Ubuntu/comments/1f9qh0a/why_wont_terminal_open/)