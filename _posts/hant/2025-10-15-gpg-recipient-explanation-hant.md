---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GPG 加密收件人說明
translated: true
type: note
---

### 理解 GPG 指令與「收件者」提示

您正在執行的指令是使用 GnuPG (GPG) 加密檔案 (`inputfile.txt`)：

```
gpg --homedir /path/to/custom/dir -e -r recipient@example.com --encrypt inputfile.txt
```

- `--homedir /path/to/custom/dir`：使用自訂目錄作為 GPG 的金鑰環與設定檔存放位置（取代預設的 `~/.gnupg`）。
- `-e`（或 `--encrypt`）：指示 GPG 加密檔案。
- `-r recipient@example.com`：指定**收件者**（您要為其加密的對象）。這應為其公鑰中的電子郵件、姓名或金鑰 ID。
- `--encrypt inputfile.txt`：要加密的檔案（輸出將為 `inputfile.txt.gpg`）。

#### 此處「收件者」的含義是什麼？
在 GPG 加密中：
- **收件者**是將*接收並解密*檔案的人。您使用*他們的公鑰*加密檔案，因此只有他們（使用其私鑰）才能解密。
- 這並非指「寄件者」（您），因為加密是為了保護收件者的資料。您作為寄件者的角色更多涉及簽署（若您添加 `-s` 進行簽署），但此處僅為純加密。

您理解這是為了「傳送」安全資料是正確的，但術語重點在於收件者，因為加密是使用其金鑰進行。可以想像成用別人的鎖頭鎖上盒子——只有他們才能解鎖。

#### 為何出現錯誤：「您未指定使用者 ID。（您可以使用 '-r'）」以及提示？
出現此互動式提示的原因為：
1. GPG 在您的金鑰環（位於自訂 homedir 中）找不到與 `recipient@example.com` 相符的公鑰。
2. 雖然提供了 `-r` 旗標，但無法解析為有效的金鑰，因此 GPG 退回要求您手動輸入使用者 ID。

提示內容為：
```
目前收件者：
輸入使用者 ID。以空行結束：
```

- **使用者 ID** 意指收件者的完整識別資訊，例如 `John Doe <recipient@example.com>` 或其金鑰指紋/ID（例如 `ABCDEF123456`）。
- 如需多行輸入（例如姓名、電子郵件、註解），請以兩次 Enter（空行）結束。

#### 如何解決此問題
1. **先匯入收件者的公鑰**（最常見問題）：
   - 請收件者將其公鑰傳送給您（透過 `gpg --export -a their@email.com` 匯出）。
   - 匯入金鑰：`gpg --homedir /path/to/custom/dir --import their-public-key.asc`。
   - 然後重新執行您的指令。

2. **若金鑰已匯入但無法匹配**：
   - 列出金鑰：`gpg --homedir /path/to/custom/dir --list-keys`。
   - 在 `-r` 中使用其中確切的使用者 ID（例如 `-r "John Doe <recipient@example.com>"`）。

3. **在提示中**（作為快速解決方法）：
   - 輸入完整的使用者 ID，例如：
     ```
     John Doe
     recipient@example.com
     
     ```
     （空行結束輸入。）

#### 為何使用「收件者」而非「寄件者」？
- 加密是*非對稱的*：公鑰（任何人皆可加密）→ 私鑰（僅擁有者可解密）。
- 寄件者（您）使用收件者的**公鑰**加密。
- 若您想證明自己是寄件者，可添加簽署：`gpg ... -e -r recipient@example.com -s --encrypt inputfile.txt`（使用*您的*私鑰進行簽署）。
- 「收件者」是 GPG 的標準術語——重點不在於誰傳送，而在於誰接收/解密。若稱之為「寄件者」會造成混淆，因為寄件者在加密時不需要金鑰（僅在簽署時需要）。

若此說明未能解決問題，請分享 `--list-keys` 的輸出（隱藏敏感資訊），我將協助除錯！

#### 參考資料
- [GPG 加密基礎](https://www.gnupg.org/documentation/manuals/gnupg/Encrypting-and-Decrypting.html)
- [GPG 手冊頁面](https://www.gnupg.org/documentation/manuals/gnupg/gpg.html)