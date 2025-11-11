---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Keytool 導入證書
translated: true
type: note
---

針對您關於使用 `keytool -importcert` 指令將憑證匯入 `jre/lib/security/cacerts` 檔案時遇到「password verification failed」錯誤並伴隨 `java.security.UnrecoverableException` 的問題，讓我們逐步分析問題成因、解決方法以及可能的密碼選項。

### 問題理解

`keytool` 工具是 Java Development Kit (JDK) 內建的命令列工具，用於管理密鑰庫。密鑰庫是儲存加密金鑰和憑證的檔案，常用於保護如 SSL/TLS 等網路通訊安全。位於 `jre/lib/security` 的 `cacerts` 檔案是 Java Runtime Environment (JRE) 自帶的特定密鑰庫，其中包含來自知名憑證機構 (CA) 的可信任根憑證集合，Java 應用程式預設使用這些憑證來驗證安全連線。

當您執行 `keytool -importcert` 指令將新憑證加入 `cacerts` 檔案時，需要提供正確的密鑰庫密碼。您遇到的錯誤訊息——「password verification failed」後接 `java.security.UnrecoverableException」——表示您輸入的密碼（或未正確輸入）與密鑰庫密碼不符。此異常通常發生在提供的密碼錯誤，導致 `keytool` 無法存取或修改密鑰庫時出現。

### 相關指令說明

您可能使用的指令類似以下格式：

```
keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias
```

- `-file mycert.crt`：指定要匯入的憑證檔案
- `-keystore /path/to/jre/lib/security/cacerts`：指向 `cacerts` 密鑰庫
- `-alias myalias`：為密鑰庫中的憑證指定唯一別名

執行此指令時，`keytool` 會提示您輸入密鑰庫密碼。若輸入的密碼不正確，就會出現您描述的錯誤。

### 識別可能密碼

在標準 JRE 安裝環境（如 Oracle 或 OpenJDK 版本）中，`cacerts` 檔案的**預設密碼**是 **"changeit"**。這是跨 Java 版本和發行版的通用預設值。名稱 "changeit" 旨在提醒系統管理員可基於安全理由變更密碼，但在大多數標準未修改的安裝環境中，此密碼通常保持不變。

由於您的指令因密碼驗證失敗而報錯，最可能的原因是：
1. 您未正確輸入 "changeit"（例如拼寫錯誤或大小寫問題——密碼區分大小寫）
2. 密碼提示處理不當
3. 在您的特定環境中，預設密碼已被修改（不過對於 `cacerts` 來說這種情況較少見，除非系統管理員明確變更）

考慮到您的查詢未提及自訂設定，我們假設這是標準 JRE 安裝環境，理應適用 "changeit" 密碼。

### 問題解決方法

以下是解決問題的步驟：

1. **確保在提示時正確輸入密碼**
   重新執行指令：

   ```
   keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias
   ```

   當出現密碼提示時，請仔細輸入 **"changeit"**（全部小寫，無空格）後按 Enter。請仔細檢查拼寫錯誤或鍵盤配置問題。

2. **在指令列直接指定密碼**
   為避免互動式提示的問題（例如指令碼或終端機行為異常），您可以使用 `-storepass` 選項直接包含密碼：

   ```
   keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias -storepass changeit
   ```

   這會明確將 "changeit" 作為密碼傳遞，繞過提示步驟。若此操作成功且無錯誤，則問題很可能源自先前密碼輸入方式。

3. **檢查權限設定**
   由於 `cacerts` 位於 JRE 目錄中（例如 Linux 上的 `/usr/lib/jvm/java-11-openjdk/lib/security/cacerts` 或 Windows 上的類似路徑），請確保您具有寫入權限。必要時請使用管理員權限執行指令：
   - Linux/Mac：`sudo keytool ...`
   - Windows：以系統管理員身分執行命令提示字元

   不過由於您的錯誤是關於密碼驗證而非檔案存取，這可能不是核心問題——但仍建議確認。

4. **驗證密碼正確性**
   如果 "changeit" 仍然失敗，可能是您的環境中密碼已被變更。若要測試密碼而不修改密鑰庫，請嘗試列出其內容：

   ```
   keytool -list -keystore /path/to/jre/lib/security/cacerts
   ```

   在提示時輸入 "changeit"。若成功顯示憑證列表，則表示密碼正確。若出現相同錯誤，則代表密碼與預設值不同。

### 若 "changeit" 非正確密碼的處理方式

如果 "changeit" 無效，請考慮以下可能性：
- **自訂密碼**：在極少數情況下，系統管理員可能已變更 `cacerts` 密碼。您需要查閱系統文件或諮詢系統管理員以取得正確密碼。若密碼遺失將無法直接復原；若確實無法得知密碼，您可能需要使用新 JRE 安裝中的全新 `cacerts` 檔案替換現有檔案（這會將密碼重設為 "changeit"）。
- **環境特定預設值**：某些非標準 Java 發行版（例如 IBM JDK）可能使用不同的預設密碼，但這種情況並不常見，且您的查詢表明這是典型設定環境。

在缺乏額外背景資訊的情況下，"changeit" 仍是標準 JRE 環境中最可能的密碼選項。

### 最終解決方案

要解決您的問題：
- 假設為標準 JRE 環境，請使用此指令：

  ```
  keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias -storepass changeit
  ```

- 若仍失敗，請透過 `-list` 指令驗證密碼，或向系統管理員確認。

根據標準 Java 慣例，此情境中的**可能密碼**就是 **"changeit"**。只要正確輸入且 `cacerts` 檔案未被自訂修改，這應能解決 `java.security.UnrecoverableException` 問題。