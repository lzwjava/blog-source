---
audio: false
generated: true
lang: hant
layout: post
title: 判斷 JVM 是 32 位元還是 64 位元
translated: true
type: note
---

要解決「無法在 32 位元 JVM 上載入 64 位元 SWT 程式庫」的錯誤，您需要確保 Java 虛擬機 (JVM) 的架構與 Eclipse 安裝版本相符。此錯誤發生原因是您的 Eclipse 嘗試使用 64 位元 SWT 程式庫，但 JVM 卻是 32 位元版本，導致兩者不相容。以下是檢查 Java 架構並解決問題的步驟。

---

### 步驟 1：檢查您的 Java 是 32 位元還是 64 位元

您可透過以下任一種方法確認 JVM 架構：

#### **方法 1：使用 `java -version`**
1. 開啟命令提示字元：
   - **Windows**：按 `Win + R`，輸入 `cmd`，然後按 Enter。
   - **Linux/Mac**：開啟終端機。
2. 輸入以下指令後按 Enter：
   ```
   java -version
   ```
3. 檢查輸出結果：
   - **64 位元 JVM**：輸出內容會包含「64-Bit」，例如：
     ```
     java version "1.8.0_311"
     Java(TM) SE Runtime Environment (build 1.8.0_311-b11)
     Java HotSpot(TM) 64-Bit Server VM (build 25.311-b11, mixed mode)
     ```
   - **32 位元 JVM**：輸出內容不會提及「64-Bit」，例如：
     ```
     java version "1.8.0_311"
     Java(TM) SE Runtime Environment (build 1.8.0_311-b11)
     Java HotSpot(TM) Client VM (build 25.311-b11, mixed mode)
     ```

#### **方法 2：使用 `java -d64 -version`**
1. 在命令提示字元輸入：
   ```
   java -d64 -version
   ```
2. 解讀結果：
   - **64 位元 JVM**：會顯示版本資訊（如上所示）。
   - **32 位元 JVM**：會出現錯誤訊息，例如：
     ```
     Unrecognized option: -d64
     Error: Could not create the Java Virtual Machine.
     Error: A fatal exception has occurred. Program will exit.
     ```

若您的 JVM 為 32 位元（如錯誤訊息所示），請繼續執行步驟 2 來解決架構不符問題。

---

### 步驟 2：解決架構不符問題

您有兩種解決方案：

#### **選項 1：安裝 64 位元 JVM（建議）**
- **原因**：64 位元 JVM 具更佳效能，並支援更大記憶體配置，特別適合 64 位元作業系統。
- **步驟**：
  1. 從可信來源下載 64 位元 JDK 或 JRE，例如：
     - [Oracle JDK](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)
     - [OpenJDK](https://adoptopenjdk.net/)
  2. 安裝後記下安裝路徑（例如 `C:\Program Files\Java\jdk1.8.0_XXX\bin\javaw.exe`）。
  3. 設定 Eclipse 使用 64 位元 JVM：
     - 在 Eclipse 安裝資料夾中開啟 `eclipse.ini` 檔案（例如 `C:\eclipse\eclipse.ini`）。
     - 在 `-vmargs` 段落**之前**加入以下內容：
       ```
       -vm
       C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
       ```
     - 請使用正斜線 (`/`) 並確保路徑與實際安裝位置相符。
  4. 儲存檔案後重新啟動 Eclipse。

#### **選項 2：改用 32 位元 Eclipse**
- **原因**：若想保留 32 位元 JVM，可改用具相容 SWT 程式庫的 32 位元 Eclipse。
- **步驟**：
  1. 從 [Eclipse 下載頁面](https://www.eclipse.org/downloads/packages/) 下載 32 位元版本 Eclipse。
  2. 安裝後使用現有 32 位元 JVM 啟動。

---

### 重要注意事項
- **架構匹配**：JVM 與 Eclipse 必須採用相同架構：
  - 64 位元 Eclipse 需搭配 64 位元 JVM。
  - 32 位元 Eclipse 需搭配 32 位元 JVM。
- **路徑雙重檢查**：若編輯 `eclipse.ini`，請確認 `javaw.exe` 路徑正確無誤。
- **系統相容性**：若您的作業系統為 64 位元，升級至 64 位元 JVM 是較理想的長期方案。

遵循以上步驟即可解決錯誤，讓 Eclipse 順利運作！