---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GPG Pinentry 回環模式詳解
translated: true
type: note
---

### 什麼是 GPG 中的 `--pinentry-mode loopback`？

在 GNU Privacy Guard (GPG) 中，`--pinentry-mode loopback` 選項用於控制工具在加密、解密或簽署操作期間處理密碼短語提示的方式。Pinentry 是 GPG 用於安全輸入密碼短語（例如私鑰密碼）的機制，通常透過圖形對話框、控制台提示或其他介面實現。

#### 主要含義與用途
- **Loopback 模式**：此設定將 pinentry 設為「loopback」行為，GPG 不會啟動外部的 pinentry 程式（例如 GUI 彈出視窗）。相反，它會將查詢直接發送回呼叫程序（如腳本或應用程式），從而模擬 pinentry。這允許以程式化方式提供密碼短語，例如透過標準輸入 (STDIN)、環境變數或檔案，而無需互動式用戶提示。

- **為何使用它？**
  - 適用於**自動化**：在 bash 腳本、CI/CD 流水線（如 GitHub Actions）或無頭環境（如 SSH 會話）中，圖形對話框無法顯示時特別有用。
  - 避免在非互動式設定中卡住或失敗。
  - 自 GnuPG 2.1.12 起，loopback 通常預設允許使用 `--allow-loopback-pinentry`，但明確設定 `--pinentry-mode loopback` 可確保其被使用。

- **常見用法示例**：
  在腳本中解密檔案，同時透過 STDIN 提供密碼短語：
  ```
  echo "your-passphrase" | gpg --pinentry-mode loopback --passphrase-fd 0 --decrypt encrypted-file.gpg > decrypted-file.txt
  ```
  - `--passphrase-fd 0`：從檔案描述符 0 (STDIN) 讀取密碼短語。
  - 這會提示一次（或使用快取，如果已配置），並在非互動式環境中工作。

#### 潛在問題
- **安全性注意**：如果未謹慎處理，Loopback 可能會在程序列表或日誌中暴露密碼短語——僅在受信任的環境中使用。
- **配置**：要全域啟用，請將 `allow-loopback-pinentry` 添加到 `~/.gnupg/gpg-agent.conf`，並使用 `gpgconf --reload gpg-agent` 重新載入。
- 如果重複提示，請檢查 `gpg-agent.conf` 中的快取超時設定（例如 `default-cache-ttl 3600` 為 1 小時）。

此模式對於將 GPG 整合到 Git 簽署或 Emacs 工作流程等工具中的開發者特別方便。

#### 參考資料
- [How do I use gpg --pinentry-mode loopback in a bash script?](https://stackoverflow.com/questions/77231645/how-do-i-use-gpg-pinentry-mode-loopback-in-a-bash-script)
- [Agent OPTION (GnuPG Manual)](https://www.gnupg.org/documentation/manuals/gnupg/Agent-OPTION.html)
- [GnuPG - ArchWiki](https://wiki.archlinux.org/title/GnuPG)