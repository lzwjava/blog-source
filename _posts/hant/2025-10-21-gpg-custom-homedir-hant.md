---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 使用自訂主目錄的 GPG
translated: true
type: note
---

### 使用 GPG 的 `--homedir` 選項

`--homedir` 標記（注意：是 `--homedir`，不是 `--home-dir`——GPG 使用單詞形式）指示 GPG 使用自訂目錄作為其「主目錄」，用於儲存設定檔、密鑰環、信任資料庫及其他資料。預設情況下，GPG 使用 `~/.gnupg`（例如在 Windows 的 Git Bash 中為 `/c/Users/您的使用者名稱/.gnupg`）。此選項適用於：
- 隔離多個 GPG 設定（例如一個用於個人密鑰，另一個用於工作）。
- 測試或避免與系統全域 GPG 設定衝突。
- 在可攜式或自訂環境中執行 GPG。

#### 基本語法
```
gpg --homedir /自訂目錄的路徑 [其他 gpg 指令]
```
- 將 `/自訂目錄的路徑` 替換為您所需的目錄路徑。
- 在 Windows 的 Git Bash 中，**請始終使用正斜線 (`/`)** 作為路徑分隔符，即使是 Windows 磁碟機代號（例如 `/c/Users/您的使用者名稱/my-gpg-dir`）。
- 目錄必須已存在；GPG 不會自動建立。請先使用 `mkdir -p /自訂目錄的路徑` 建立目錄。

#### 範例：設定及使用自訂主目錄
1. **建立自訂目錄**（在 Git Bash 中）：
   ```
   mkdir -p /c/Users/您的使用者名稱/my-custom-gpg
   ```

2. **使用自訂 homedir 產生密鑰對**：
   ```
   gpg --homedir /c/Users/您的使用者名稱/my-custom-gpg --full-generate-key
   ```
   - 這會將您的密鑰和設定儲存在 `my-custom-gpg` 中，而非預設目錄。

3. **從該目錄列出密鑰**：
   ```
   gpg --homedir /c/Users/您的使用者名稱/my-custom-gpg --list-secret-keys --keyid-format LONG
   ```

4. **使用自訂目錄中的密鑰加密檔案**：
   ```
   gpg --homedir /c/Users/您的使用者名稱/my-custom-gpg --encrypt --recipient 收件人電郵 secret.txt
   ```

5. **解密檔案**：
   ```
   gpg --homedir /c/Users/您的使用者名稱/my-custom-gpg --output decrypted.txt --decrypt secret.txt.gpg
   ```

#### Git Bash on Windows 使用提示
- **路徑：** 堅持使用 `/`——例如避免使用 `\` 或混合斜線，因為它們可能導致指令失效。
- **權限：** 確保自訂目錄具有讀取/寫入權限（為安全起見，可使用 `chmod 700 /自訂目錄的路徑`，類似預設的 `.gnupg` 設定）。
- **環境變數替代方案：** 無需每次使用 `--homedir`，可在 `.bashrc` 中設定 `export GNUPGHOME=/c/Users/您的使用者名稱/my-custom-gpg`（編輯後執行 `source ~/.bashrc`）。之後 GPG 會自動使用該路徑。
- **Git 整合：** 若用於 Git 簽署，請使用以下標記進行設定：
  ```
  git config --global gpg.program "gpg --homedir /c/Users/您的使用者名稱/my-custom-gpg"
  ```
- **常見問題：** 若 GPG 提示缺少檔案，可能需要初始化——請先執行 `gpg --homedir /路徑 --gen-key`。在 Windows 上，除非使用引號，否則請避免包含空格的路徑。

詳細資訊請參閱 GPG 手冊：[GnuPG Documentation](https://www.gnupg.org/documentation/manuals/gnupg/)