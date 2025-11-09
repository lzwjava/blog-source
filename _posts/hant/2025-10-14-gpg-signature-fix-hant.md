---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 GPG 簽名驗證錯誤
translated: true
type: note
---

### 理解錯誤

您遇到的錯誤是因為 `gpg --verify` 指令在多數情況下需要兩個參數：首先是**簽章檔案**（例如 `zhs.tw.yaml.sig` 或 `zhs.tw.yaml.asc`），接著是要驗證的**實際檔案**（例如 `zhs.tw.yaml`）。

在您的指令中：
```
gpg --verify zhs.tw.yaml
```
GPG 試圖將 `zhs.tw.yaml` 同時解釋為簽章和數據檔案，但它並不包含有效的 OpenPGP 簽章數據（YAML 檔案並非簽章）。因此出現「未找到有效的 OpenPGP 數據」的訊息。

### 如何修正

1. **找到簽章檔案**：您需要與 YAML 檔案對應的獨立簽章檔案。它通常命名為：
   - `zhs.tw.yaml.sig`（二進位格式）
   - `zhs.tw.yaml.asc`（ASCII 編碼格式）

   如果您沒有此檔案，需要從獲取 `zhs.tw.yaml` 的來源處（例如專案儲存庫或網站）下載。

2. **執行正確的指令**：取得簽章後，請使用以下格式：
   ```
   gpg --verify zhs.tw.yaml.sig zhs.tw.yaml
   ```
   - 如果您的檔案是 `.asc` 格式，請將 `.sig` 替換為 `.asc`。
   - 順序很重要：先簽章，後檔案。

3. **成功時的預期輸出**：
   如果簽章有效且您信任該密鑰，您會看到類似：
   ```
   gpg: Signature made [date] using [key type]
   gpg: Good signature from "[signer name/email]"
   ```
   如果簽章無效或密鑰不受信任，您將收到警告/錯誤。

### 額外提示

- **匯入公鑰**：如果 GPG 提示未知密鑰，請獲取並匯入簽署者的公鑰：
  ```
  gpg --keyserver keyserver.ubuntu.com --recv-keys [KEY_ID]
  ```
  （將 `[KEY_ID]` 替換為錯誤輸出或專案文件中提供的實際密鑰指紋。）

- **腳本使用的批次模式**：如果您要自動化此過程，請添加 `--batch` 以抑制提示：
  ```
  gpg --batch --verify zhs.tw.yaml.sig zhs.tw.yaml
  ```

- **內嵌簽章**：如果簽章是*嵌入*在 YAML 檔案中的（對於 `.yaml` 檔案較不可能），您只需在確認檔案以 `-----END PGP SIGNATURE-----` 結尾後執行 `gpg --verify zhs.tw.yaml`。但根據錯誤訊息，這應該是獨立簽章。

如果這未能解決問題，或者您提供更多詳細資訊（例如檔案來源），我可以提供更精確的建議！

[GNU Privacy Guard 手冊](https://www.gnupg.org/documentation/manpage.html)