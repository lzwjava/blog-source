---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 Firefox APT 儲存庫錯誤
translated: true
type: note
---

您遇到的錯誤是針對 Mozilla Firefox APT 儲存庫（`https://packages.mozilla.org/apt`）的特定問題，在獲取 `binary-all/Packages` 索引檔案時失敗，並出現 400 Bad Request 錯誤。這是其他 Ubuntu/Debian 用戶回報的一個已知的間歇性問題，通常與代理設定有關（您本地的代理 `127.0.0.1:7890` 暗示您可能正在使用 Clash、V2Ray 或類似工具，這些工具可能會干擾 APT 的 HTTPS 請求）。好消息是 APT 會忽略此失敗並使用快取/舊的索引，因此系統更新不會被阻擋——但這可能會妨礙您獲取最新的 Firefox deb 套件。

### 可嘗試的快速解決方法（按順序）
1. **清除 APT 快取**（這可以解決損壞或過時的索引檔案，對許多用戶有效）：
   ```
   sudo apt clean
   sudo apt update
   ```

2. **暫時讓 APT 繞過您的代理**（因為 400 錯誤通常源於代理對該儲存庫 HTTPS 的干擾）：
   ```
   unset http_proxy https_proxy all_proxy
   sudo -E apt update
   ```
   - 請在同一個終端機工作階段中執行此指令。如果有效，您可以將 `unset` 這幾行加入到您的 `~/.bashrc` 中（或僅在 APT 指令前執行），或者暫時停用代理應用程式。
   - 如果您的代理是系統全域設定的（例如在 `/etc/environment` 中），請編輯該檔案以排除 APT，或暫時將相關行註解掉。

3. **全域停用 APT 的代理**（如果上述方法有效，但您想要一個一勞永逸的選項）：
   ```
   echo 'Acquire::http::Proxy "";
   Acquire::https::Proxy "";' | sudo tee /etc/apt/apt.conf.d/99no-proxy
   sudo apt update
   ```
   - 這會告訴 APT 完全忽略代理。如果需要復原，請刪除 `/etc/apt/apt.conf.d/99no-proxy` 檔案。

### 如果您需要最新版 Firefox 但不想使用該儲存庫
如果儲存庫持續失敗，而您只想要更新 Firefox：
- **切換到 Snap**（Ubuntu 的預設選項，更新容易，無需處理儲存庫問題）：
  ```
  sudo snap install firefox
  ```
- **或使用 Flatpak**（如果您偏好）：
  ```
  sudo apt install flatpak
  flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
  flatpak install flathub org.mozilla.firefox
  ```

### 預防措施/注意事項
- Mozilla 儲存庫是非官方的，用於獲取最新版的 Firefox deb 套件——除非您特別需要 deb 套件，否則請考慮堅持使用 Ubuntu 的 snap 版本。
- 如果以上方法都無效，請檢查您的代理日誌（例如 Clash 儀表板）中是否有被拒絕的發往 `packages.mozilla.org` 的請求，或者完全在不使用代理的情況下進行測試。
- 修復後，再次執行 `sudo apt update` 以驗證。

如果這些方法無法解決問題，請分享更多詳細資訊，例如您的代理設定或完整的 `/etc/apt/sources.list.d/mozilla.list` 檔案內容，以便進行更深入的疑難排解。

[Ubuntu 23.10 - 更新問題](https://askubuntu.com/questions/1507571/ubuntu-23-10-update-problems-some-index-files-failed-to-download)  
[Firefox apt 儲存庫錯誤](https://www.reddit.com/r/firefox/comments/1ois308/firefox_apt_repository_error/)