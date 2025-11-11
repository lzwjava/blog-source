---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 安全導出 GPG 私密金鑰
translated: true
type: note
---

### 以裝甲格式使用 GPG 匯出私密金鑰

GPG（GNU Privacy Guard）允許以裝甲 ASCII 格式匯出私密金鑰，將其儲存為人類可讀的 `.asc` 檔案（非二進位制）。這對於備份、傳輸或在另一台機器上匯入非常有用。

**重要警告：** 私密金鑰包含敏感資訊。僅在必要時匯出，儲存或傳輸時請加密輸出檔案，使用後請刪除匯出檔案以避免意外洩漏。切勿公開分享私密金鑰。

#### 基本指令結構
要為特定使用者 ID（與金鑰關聯的電郵或名稱）匯出私密金鑰，請使用：

```
gpg --export-secret-keys --armor [金鑰_ID] > 檔案名稱.asc
```

- `金鑰_ID`：金鑰指紋、短 ID、電郵或名稱。您可以使用 `gpg --list-secret-keys` 列出您的金鑰。
- `--armor`：以裝甲（ASCII）格式輸出，而非二進位制。
- `> 檔案名稱.asc`：將輸出重新導向至檔案（例如 `my_secret_key.asc`）。省略此部分則輸出至終端機。

#### 逐步使用範例
1. **列出您的私密金鑰**以找到金鑰_ID：
   ```
   gpg --list-secret-keys
   ```
   範例輸出：
   ```
   sec   rsa3072/ABC12345 2023-01-01 [SC] [expires: 2025-01-01]
         Key fingerprint = 1234 5678 ABCD EF01 2345 6789 ABCD EF01 2345 6789
   uid                 [ultimate] Your Name <your@email.com>
   ```

   此處 `ABC12345` 是短金鑰 ID，或者為了精確起見可使用完整指紋 `ABCDEF0123456789ABCDEF0123456789`。

2. **匯出私密金鑰**：
   ```
   gpg --export-secret-keys --armor ABC12345 > my_secret_key.asc
   ```

3. **驗證匯出**（可選）：
   ```
   cat my_secret_key.asc
   ```
   檔案應以 `-----BEGIN PGP PRIVATE KEY BLOCK-----` 開頭，並以 `-----END PGP PRIVATE KEY BLOCK-----` 結尾。

#### 額外選項
- **匯出所有私密金鑰**：省略金鑰_ID 以匯出全部：
  ```
  gpg --export-secret-keys --armor > all_secret_keys.asc
  ```
- **使用密碼保護**：如果金鑰已加密（預設），GPG 將提示您輸入密碼。
- **若需要公開金鑰**：使用 `--export`（僅用於公開金鑰）。

完整文件請參閱 GPG 手冊頁：`man gpg`。如果您是 GPG 新手，請先使用 `gpg --gen-key` 產生金鑰。