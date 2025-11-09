---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 使用GPG加密檔案
translated: true
type: note
---

### 使用 GPG 金鑰加密檔案

您的 GPG 金鑰清單顯示一個公開金鑰 (pub)，指紋為 `982740390B5D33E90B6B6133892BC5A4789B71CD`，關聯至您的電子郵件 `lzwjava@gmail.com`。若要使用此金鑰加密檔案（如此僅有您能使用私密金鑰解密），請在終端機中依循以下步驟：

1. **導航至目錄** 包含您欲加密的檔案（例如，若您的檔案為 `secret.txt`）：
   ```
   cd ~/path/to/your/file
   ```

2. **加密檔案** 使用 `--encrypt` 選項並指定收件者（您的電子郵件或金鑰 ID）。此操作將建立加密的 `.gpg` 檔案。
   
   - 使用您的電子郵件（較簡便）：
     ```
     gpg --encrypt --recipient lzwjava@gmail.com secret.txt
     ```
   
   - 使用金鑰 ID（完整指紋）：
     ```
     gpg --encrypt --recipient 982740390B5D33E90B6B6133892BC5A4789B71CD secret.txt
     ```
   
   此操作將輸出 `secret.txt.gpg`，即為加密版本。原始 `secret.txt` 保持不變。

3. **驗證加密**（可選）：
   ```
   gpg --list-packets secret.txt.gpg
   ```
   此指令將顯示加密封包的詳細資訊。

### 解密檔案（供後續參考）

若要將其解密（僅在擁有您的私密金鑰與通行短語時可行）：
```
gpg --decrypt secret.txt.gpg > secret.txt.decrypted
```
在提示時輸入您的通行短語。

### 實用提示
- **對稱加密**（若您不需要收件者金鑰，僅需通行短語）：改用 `gpg -c secret.txt`。
- **加密並簽署**（以證明檔案來源為您）：在加密指令中加入 `--sign`，例如 `gpg --encrypt --sign --recipient lzwjava@gmail.com secret.txt`。
- 若您遇到錯誤（例如金鑰不受信任），請執行 `gpg --edit-key lzwjava@gmail.com` 並使用 `trust` 將其設定為終極信任。
- 請務必備份您的 `~/.gnupg` 目錄以確保金鑰安全。

更多詳細資訊，請查閱 GPG 手冊：[GPG 文件](https://www.gnupg.org/documentation/manpage.html)。