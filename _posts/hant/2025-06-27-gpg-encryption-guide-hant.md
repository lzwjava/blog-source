---
audio: false
generated: true
lang: hant
layout: post
title: 認識 GPG：安全通訊工具
translated: true
type: note
---

## 什麼是 GPG？
GPG，全名為 GNU Privacy Guard，是 OpenPGP 標準（Pretty Good Privacy）的開源實作。它是一種安全通訊工具，提供加密、解密、數位簽章和密鑰管理功能。GPG 廣泛用於保護電子郵件、檔案及其他資料，確保機密性、完整性和真實性。

GPG 可在大多數作業系統上使用，包括 Linux、macOS 和 Windows。它基於命令列操作，但可與圖形介面工具或電子郵件客戶端（如 Thunderbird）整合。

---

## GPG 運作原理
GPG 結合**對稱金鑰加密**和**公開金鑰加密**來保護資料安全：

1. **對稱金鑰加密**：
   - 使用單一金鑰進行加密和解密。
   - GPG 採用對稱金鑰演算法（例如 AES）來加密實際資料，因為這類演算法處理大型資料集時速度較快。
   - 每次加密操作都會產生一個隨機的工作階段金鑰。

2. **公開金鑰加密**：
   - 使用一對金鑰：**公開金鑰**用於加密，**私密金鑰**用於解密。
   - GPG 支援如 RSA 或 ECDSA 等演算法來產生金鑰對。
   - 公開金鑰用於加密工作階段金鑰，該工作階段金鑰隨後用於加密資料。接收者使用其私密金鑰解密工作階段金鑰，再使用該金鑰解密資料。

3. **數位簽章**：
   - GPG 允許使用者使用其私密金鑰對資料進行簽章，以證明真實性和完整性。
   - 接收者使用寄件者的公開金鑰驗證簽章。

4. **金鑰管理**：
   - GPG 在密鑰環中管理金鑰，該密鑰環儲存公開和私密金鑰。
   - 金鑰可被產生、匯入、匯出及發佈到金鑰伺服器。

### GPG 加密流程
加密檔案或訊息時：
1. GPG 為對稱加密產生一個隨機的**工作階段金鑰**。
2. 使用對稱演算法（例如 AES-256）以工作階段金鑰加密資料。
3. 使用非對稱演算法（例如 RSA）以接收者的**公開金鑰**加密工作階段金鑰。
4. 將加密的工作階段金鑰和加密的資料合併為單一的輸出檔案或訊息。

解密時：
1. 接收者使用其**私密金鑰**解密工作階段金鑰。
2. 使用工作階段金鑰透過對稱演算法解密資料。

這種混合方法結合了對稱加密的速度和非對稱加密的安全性。

---

## 安裝 GPG
GPG 已預先安裝在許多 Linux 發行版上。對於其他系統：
- **Linux**：透過套件管理員安裝：
  ```bash
  sudo apt install gnupg  # Debian/Ubuntu
  sudo yum install gnupg  # CentOS/RHEL
  ```
- **macOS**：透過 Homebrew 安裝：
  ```bash
  brew install gnupg
  ```
- **Windows**：從 [gpg4win.org](https://gpg4win.org/) 下載 Gpg4win。

驗證安裝：
```bash
gpg --version
```

---

## 產生 GPG 金鑰
使用 GPG 前，您需要一對金鑰（公開金鑰和私密金鑰）。

### 逐步金鑰產生
執行以下命令來產生金鑰對：
```bash
gpg --full-generate-key
```

1. **選擇金鑰類型**：
   - 預設為 RSA 和 RSA（選項 1）。
   - RSA 廣泛使用且對大多數用途來說是安全的。

2. **金鑰大小**：
   - 建議：2048 或 4096 位元（4096 更安全但速度較慢）。
   - 範例：選擇 4096。

3. **金鑰過期時間**：
   - 選擇過期日期（例如 1 年）或選擇 0 表示永不過期。
   - 設定過期金鑰可限制金鑰的生命週期，從而增強安全性。

4. **使用者 ID**：
   - 輸入您的姓名、電子郵件及可選的註解。
   - 範例：`John Doe <john.doe@example.com>`。

5. **通行密碼**：
   - 設定一個強通行密碼來保護私密金鑰。
   - 解密和簽章時需要此通行密碼。

執行命令後的範例輸出：
```
gpg: key 0x1234567890ABCDEF marked as ultimately trusted
gpg: generated key pair
```

### 匯出金鑰
- **匯出公開金鑰**：
  ```bash
  gpg --armor --output public-key.asc --export john.doe@example.com
  ```
  這會建立一個包含您公開金鑰的 ASCII 格式檔案（`public-key.asc`）。

- **匯出私密金鑰**（請謹慎操作，確保其安全）：
  ```bash
  gpg --armor --output private-key.asc --export-secret-keys john.doe@example.com
  ```

---

## 加密與解密檔案
### 加密檔案
為接收者加密檔案：
1. 確保接收者的公開金鑰在您的密鑰環中：
   ```bash
   gpg --import recipient-public-key.asc
   ```
2. 加密檔案：
   ```bash
   gpg --encrypt --recipient john.doe@example.com --output encrypted-file.gpg input-file.txt
   ```
   - `--recipient`：指定接收者的電子郵件或金鑰 ID。
   - `--output`：指定輸出檔案。
   - 結果為 `encrypted-file.gpg`，只有接收者可以解密。

### 解密檔案
解密為您加密的檔案：
```bash
gpg --decrypt --output decrypted-file.txt encrypted-file.gpg
```
- 在提示時輸入您的通行密碼。
- 解密後的內容將儲存到 `decrypted-file.txt`。

---

## 簽章與驗證資料
### 簽章檔案
簽章可證明資料的真實性和完整性。
- **明文簽章**（包含人類可讀的簽章）：
  ```bash
  gpg --clearsign input-file.txt
  ```
  輸出：`input-file.txt.asc`，包含檔案內容和簽章。

- **分離簽章**（獨立的簽章檔案）：
  ```bash
  gpg --detach-sign input-file.txt
  ```
  輸出：`input-file.txt.sig`。

### 驗證簽章
驗證已簽章的檔案：
```bash
gpg --verify input-file.txt.asc
```
對於分離簽章：
```bash
gpg --verify input-file.txt.sig input-file.txt
```
您需要簽章者的公開金鑰在您的密鑰環中。

---

## 使用 GPG 產生密碼
GPG 可以產生隨機資料，用於建立安全密碼。雖然 GPG 主要不是密碼產生器，但其隨機數生成是密碼學安全的。

### 產生密碼的命令
```bash
gpg --gen-random --armor 1 32
```
- `--gen-random`：產生隨機位元組。
- `--armor`：以 ASCII 格式輸出。
- `1`：品質等級（1 適用於密碼學用途）。
- `32`：位元組數（根據所需密碼長度調整）。

範例輸出：
```
4eX9j2kPqW8mZ3rT5vY7nL9xF2bC6dA8
```
若要使其更像密碼，可透過 base64 或十六進制轉換器進行處理，或修剪至所需長度。

### 範例：產生 20 字元密碼
```bash
gpg --gen-random --armor 1 15 | head -c 20
```
這會產生一個 20 字元的隨機字串。

---

## 金鑰管理
### 列出金鑰
- 列出公開金鑰：
  ```bash
  gpg --list-keys
  ```
- 列出私密金鑰：
  ```bash
  gpg --list-secret-keys
  ```

### 發佈公開金鑰
透過金鑰伺服器分享您的公開金鑰：
```bash
gpg --keyserver hkps://keys.openpgp.org --send-keys 0x1234567890ABCDEF
```
將 `0x1234567890ABCDEF` 替換為您的金鑰 ID。

### 匯入金鑰
從檔案匯入公開金鑰：
```bash
gpg --import public-key.asc
```
或從金鑰伺服器匯入：
```bash
gpg --keyserver hkps://keys.openpgp.org --recv-keys 0x1234567890ABCDEF
```

### 撤銷金鑰
若金鑰遭洩露或過期：
1. 產生撤銷憑證（在建立金鑰時進行此操作）：
   ```bash
   gpg --output revoke.asc --gen-revoke john.doe@example.com
   ```
2. 匯入並發佈撤銷：
   ```bash
   gpg --import revoke.asc
   gpg --keyserver hkps://keys.openpgp.org --send-keys john.doe@example.com
   ```

---

## 最佳實踐
1. **備份金鑰**：
   - 安全地儲存私密金鑰和撤銷憑證（例如加密的 USB 隨身碟）。
   - 切勿分享私密金鑰。

2. **使用強通行密碼**：
   - 為您的私密金鑰使用長且獨特的通行密碼。

3. **定期更新金鑰**：
   - 設定過期日期並定期輪換金鑰。

4. **驗證金鑰指紋**：
   - 在信任公開金鑰前，與擁有者驗證其指紋：
     ```bash
     gpg --fingerprint john.doe@example.com
     ```

5. **安全使用金鑰伺服器**：
   - 使用受信任的金鑰伺服器，如 `hkps://keys.openpgp.org`。

6. **僅簽章受信任的金鑰**：
   - 當簽署他人的金鑰時，請親自或透過可信管道驗證其身分。

---

## 常用 GPG 命令摘要
以下是常用 GPG 命令的快速參考：
- 產生金鑰對：`gpg --full-generate-key`
- 加密檔案：`gpg --encrypt --recipient <email> --output <output.gpg> <input.txt>`
- 解密檔案：`gpg --decrypt --output <output.txt> <input.gpg>`
- 簽章檔案：`gpg --clearsign <input.txt>` 或 `gpg --detach-sign <input.txt>`
- 驗證簽章：`gpg --verify <file.asc>` 或 `gpg --verify <file.sig> <file>`
- 匯出公開金鑰：`gpg --armor --output public-key.asc --export <email>`
- 匯入金鑰：`gpg --import <key.asc>`
- 產生隨機密碼：`gpg --gen-random --armor 1 <bytes>`

---

## 疑難排解
- **「沒有私密金鑰」錯誤**：確保私密金鑰在您的密鑰環中（`gpg --list-secret-keys`）且與接收者的公開金鑰匹配。
- **忘記通行密碼**：若遺失通行密碼，您必須撤銷金鑰並產生新金鑰。
- **找不到金鑰**：匯入接收者的公開金鑰或檢查金鑰伺服器。
- **GPG 版本問題**：確保所有方使用相容的 GPG 版本（透過 `gpg --version` 檢查）。

---

## 進階功能
1. **電子郵件整合**：
   - 透過外掛程式（例如 Enigmail 或內建的 OpenPGP 功能）在電子郵件客戶端如 Thunderbird 中使用 GPG。