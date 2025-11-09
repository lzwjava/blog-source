---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 導出 GPG 私密金鑰
translated: true
type: note
---

### 從伺服器匯出 GPG 私鑰

要匯出你的私鑰，你需要透過 SSH 或終端機存取伺服器。GPG 私鑰非常敏感——請安全處理並在傳輸後刪除匯出的檔案。

1. **列出你的私密金鑰**（用以透過電郵或金鑰 ID 識別金鑰）：  
   ```
   gpg --list-secret-keys
   ```  
   尋找類似 `sec   rsa4096/ABC123DEF456 2023-01-01 [SC]` 的條目。記下電郵或金鑰 ID（例如 `user@example.com` 或 `ABC123DEF456`）。

2. **匯出私鑰**（使用 `--armor` 取得 ASCII 格式，便於傳輸）：  
   ```
   gpg --export-secret-keys --armor user@example.com > private-key.asc
   ```  
   - 將 `user@example.com` 替換為你的實際電郵或金鑰 ID。  
   - 這會在當前目錄建立 `private-key.asc` 檔案。  
   - 如果你有多把金鑰，請指定金鑰 ID 以確保準確：`gpg --export-secret-keys --armor ABC123DEF456 > private-key.asc`。  
   - **安全注意**：此操作匯出的金鑰*不包含*密碼。在匯入時若系統提示，你需要輸入密碼。

3. **安全地將檔案傳輸**到本地筆記型電腦：  
   - 使用 `scp`（從你的本地機器執行）：  
     ```
     scp user@server-ip:/path/to/private-key.asc ./
     ```  
     將 `user@server-ip` 替換為你的伺服器詳情，並將 `/path/to/` 替換為實際路徑。  
   - 其他選擇：較大檔案可使用 `rsync`，或需要圖形介面時使用 SFTP。避免透過電郵或不安全渠道傳輸。

4. **在伺服器上清理**：  
   ```
   rm private-key.asc
   ```  
   使用 `ls` 確認檔案已刪除。

### 在本地筆記型電腦上匯入 GPG 私鑰

假設你已安裝 GPG（例如在 Linux 上透過 `apt install gnupg`、在 macOS 上透過 `brew install gnupg`，或在 Windows 上使用 Chocolatey）。

1. **匯入金鑰**：  
   ```
   gpg --import private-key.asc
   ```  
   - 你將看到類似 "gpg: key ABC123DEF456: secret key imported" 的輸出。  
   - 如果在匯入過程中提示輸入密碼，請輸入原始密碼。

2. **驗證匯入**：  
   ```
   gpg --list-secret-keys
   ```  
   你的金鑰現在應該出現在 "sec" 下方。

3. **可選：設定信任等級**（如果用於簽署/電郵）：  
   ```
   gpg --edit-key user@example.com
   ```  
   - 在提示中，輸入 `trust`，選擇 "ultimate"（選項 5），然後 `save` 並 `quit`。  
   - 這會將金鑰標記為在你的本地機器上完全受信任。

### 提示與警告
- **密碼**：務必使用高強度密碼。如果忘記密碼，金鑰將無法使用。
- **子金鑰**：如果你的金鑰包含子金鑰（例如用於加密），請使用 `--export-secret-subkeys` 一併匯出。
- **備份**：將匯出的金鑰儲存在安全的保險庫中（例如加密驅動器）。
- **版本**：此操作在 GPG 2.x 版本測試通過；在 1.x 版本上操作類似。
- 更多詳情，請參閱官方 GPG 文件：[GnuPG Manual](https://www.gnupg.org/documentation/manuals/gnupg/)。