---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 驗證 GPG 數碼簽署
translated: true
type: note
---

### 驗證 GPG 簽名

GnuPG（GPG）可讓您驗證數位簽名，以確保檔案或訊息未被篡改且確實來自聲稱的發送者。驗證需要您的密鑰環中包含簽署者的公鑰。以下是常見情境的步驟與指令。

#### 前置準備
1. **安裝 GPG**：確保系統已安裝 GnuPG（例如在 Debian 系統上使用 `apt install gnupg`，或在 macOS 上使用 `brew install gnupg`）。
2. **匯入簽署者的公鑰**：您需要簽署檔案者或實體的公鑰。從密鑰伺服器或檔案下載後進行匯入：
   ```
   gpg --import public-key.asc
   ```
   （將 `public-key.asc` 替換為實際密鑰檔案。若從密鑰伺服器取得，請使用 `gpg --keyserver keyserver.ubuntu.com --recv-keys KEYID`，其中 `KEYID` 為密鑰指紋或 ID。）

#### 驗證步驟
具體指令取決於簽名的建立方式（例如內嵌於檔案中或分離式簽名）。

1. **驗證分離式簽名**（常見於軟體發佈檔案；簽名位於獨立的 `.sig` 檔案）：
   ```
   gpg --verify signature.sig original-file
   ```
   - 有效簽名的輸出範例：
     ```
     gpg: Signature made [日期] using [密鑰類型] key ID [密鑰ID]
     gpg: Good signature from "[名稱] <email@example.com>"
     ```
   - 若密鑰未受信任，可能顯示警告如「此密鑰未獲受信任簽名認證！」您可透過 `gpg --edit-key KEYID` 後輸入 `trust` 調整信任等級。

2. **驗證內嵌簽名檔案**（簽名嵌入檔案中，通常為二進位格式）：
   - 僅檢查簽名：
     ```
     gpg --verify signed-file
     ```
   - 驗證並提取原始內容：
     ```
     gpg --output original-file --decrypt signed-file
     ```
     若經加密會提示輸入密碼，但僅驗證簽名時則直接進行檢查。

3. **驗證明文簽名訊息**（含 ASCII 封裝簽名的可讀文字，常見於電子郵件或 README 文件）：
   ```
   gpg --verify clearsigned-file.txt
   ```
   輸出將顯示簽名狀態而不更動檔案內容。

#### 疑難排解
- **「找不到公鑰」錯誤**：請依前述方式匯入密鑰。
- **簽名無效**：檔案可能遭篡改——請重新下載。
- **密鑰有效性**：使用 `gpg --list-keys` 檢查密鑰詳細資訊，或驗證指紋是否與官方來源相符。
- 需批次驗證或腳本處理時，請添加 `--batch --exit-on-status-write-error` 參數。

關於簽署或進階選項的詳細說明，請參閱官方手冊。

[製作與驗證簽名 - GnuPG 手冊](https://www.gnupg.org/gph/en/manual/x135.html)