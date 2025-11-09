---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: 修復 GNOME 終端機 Python 導入錯誤
translated: true
type: note
---

### 問題診斷
您的 GNOME 終端機因 GObject Introspection (GI) 函式庫中的 Python 導入錯誤而無法啟動。追蹤資訊顯示問題出在 `from gi.repository import GLib, Gio` 這行，具體是在 `/usr/lib/python3/dist-packages/gi/__init__.py` 的第 40 行。完整的錯誤（根據常見報告）很可能是：

```
ImportError: cannot import name '_gi' from partially initialized module 'gi' (most likely due to a circular import)
```

這通常是由於系統的 Python 版本與 GI 綁定（python3-gi 套件）不匹配所致，常見於手動升級 Python、使用虛擬環境或套件損毀後。您在 journalctl 輸出中看到的 UFW BLOCK 記錄與此無關——它們只是防火牆在丟棄無害的多播流量（例如來自 192.168.1.x 網段其他設備的 mDNS/UPnP 探索）。請暫時忽略這些記錄。

### 可嘗試的快速修復
由於您目前已有可用的 shell 提示字元（看起來您在 `~/projects` 目錄中），可以直接執行以下指令。從最簡單的開始：

1. **重新安裝 GI 套件與 GNOME 終端機**（最常見的修復方法）：
   ```
   sudo apt update
   sudo apt install --reinstall python3-gi gir1.2-glib-2.0 gnome-terminal
   ```
   然後在當前 shell 中執行 `gnome-terminal` 進行測試。

2. **若上述方法無效，請檢查/修復 Python 符號連結**（如果您最近曾調整 Python 版本）：
   - 驗證系統 Python：`ls -l /usr/bin/python3`（應指向類似 python3.10 或 3.12 的版本，具體取決於您的發行版版本）。
   - 若連結損毀，請重新安裝預設 Python：
     ```
     sudo apt install --reinstall python3-minimal
     ```
   - 或手動設定符號連結（將 `3.10` 替換為您發行版的預設版本）：
     ```
     sudo ln -sf /usr/bin/python3.10 /usr/bin/python3
     ```

3. **完整重置 GNOME**（若以上方法均失敗——會重置終端機偏好設定但不影響資料）：
   ```
   dconf reset -f /org/gnome/terminal/
   gnome-terminal --reset-config
   ```

4. **終極方案：徹底移除並重新安裝 GNOME 終端機**：
   ```
   sudo apt purge gnome-terminal
   sudo apt install gnome-terminal
   ```

完成任一修復後，請登出/登入或重新啟動系統，以確保桌面環境能正確載入變更。如果您使用的是 Ubuntu/Debian 系發行版（從路徑判斷），這些指令應能生效。若為其他發行版（如 Fedora），請將 `apt` 替換為 `dnf`。

如果以上方法均無法解決問題，請在當前 shell 中執行 `python3 -c "from gi.repository import GLib; print('OK')"` 並分享輸出結果以供進一步分析。

### 參考資料
- [Gnome terminal will not start after trying to install newer version of Python](https://askubuntu.com/questions/880188/gnome-terminal-will-not-start-after-trying-to-install-newer-version-of-python-3)
- [Why won't terminal open?](https://www.reddit.com/r/Ubuntu/comments/1f9qh0a/why_wont_terminal_open/)
- [ImportError: cannot import name '_gi' from partially initialized module](https://stackoverflow.com/questions/59838238/importerror-cannot-import-name-gi-from-partially-initialized-module-gi-mo)
- [Some applications not working on Zorin 17 Core](https://forum.zorin.com/t/some-applications-not-working-on-zorin-17-core/43391)