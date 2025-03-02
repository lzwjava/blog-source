---
audio: false
generated: false
lang: hant
layout: post
title: 確定 JVM 是 32 位或 64 位
translated: true
---

要解決錯誤「無法在 32 位 JVM 上加載 64 位 SWT 程式庫」，您需要確保您的 Java 虛擬機 (JVM) 結構與您的 Eclipse 安裝結構相匹配。 此錯誤發生是因為您的 Eclipse 試圖使用 64 位 SWT 程式庫，但您的 JVM 是 32 位，使它們不相容。 以下是檢查您的 Java 結構並修復問題的步驟。

---

### 步驟 1：檢查您的 Java 是 32 位還是 64 位

您可以使用以下方法之一來確定您的 JVM 是 32 位還是 64 位：

#### **方法 1：使用 `java -version`**
1. 打開命令提示字元：
   - **Windows**：按 `Win + R`，輸入 `cmd`，然後按 Enter。
   - **Linux/Mac**：打開您的終端機。
2. 輸入以下命令並按 Enter：
   ```
   java -version
   ```
3. 檢查輸出：
   - **64 位 JVM**：輸出將包括「64-Bit」，例如：
     ```
     java version "1.8.0_311"
     Java(TM) SE Runtime Environment (build 1.8.0_311-b11)
     Java HotSpot(TM) 64-Bit Server VM (build 25.311-b11, mixed mode)
     ```
   - **32 位 JVM**：輸出將不會提及「64-Bit」，例如：
     ```
     java version "1.8.0_311"
     Java(TM) SE Runtime Environment (build 1.8.0_311-b11)
     Java HotSpot(TM) Client VM (build 25.311-b11, mixed mode)
     ```

#### **方法 2：使用 `java -d64 -version`**
1. 在命令提示字元中輸入：
   ```
   java -d64 -version
   ```
2. 解釋結果：
   - **64 位 JVM**：它將顯示與上述相同的版本資訊。
   - **32 位 JVM**：您將看到錯誤，例如：
     ```
     Unrecognized option: -d64
     Error: Could not create the Java Virtual Machine.
     Error: A fatal exception has occurred. Program will exit.
     ```

如果您的 JVM 是 32 位（如錯誤所建議），請繼續進行步驟 2 以修復不匹配。

---

### 步驟 2：解決結構不匹配

您有兩個選項來解決此問題：

#### **選項 1：安裝 64 位 JVM（推薦）**
- **為什麼？** 64 位 JVM 更適合性能並支持更大的記憶體分配，特別是如果您的系統是 64 位。
- **步驟**：
  1. 從可信來源下載 64 位 JDK 或 JRE，例如：
     - [Oracle JDK](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)
     - [OpenJDK](https://adoptopenjdk.net/)
  2. 安裝它並記下安裝路徑（例如 `C:\Program Files\Java\jdk1.8.0_XXX\bin\javaw.exe`）。
  3. 配置 Eclipse 使用 64 位 JVM：
     - 打開 Eclipse 安裝資料夾中的 `eclipse.ini` 文件（例如 `C:\eclipse\eclipse.ini`）。
     - 在 `-vmargs` 部分之前添加這些行：
       ```
       -vm
       C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
       ```
     - 使用正斜線（`/`）並確保路徑與您的安裝相匹配。
  4. 保存文件並重新啟動 Eclipse。

#### **選項 2：切換到 32 位 Eclipse**
- **為什麼？** 如果您想保留 32 位 JVM，您可以使用具有相容 SWT 程式庫的 32 位 Eclipse。
- **步驟**：
  1. 從 [Eclipse 下載頁面](https://www.eclipse.org/downloads/packages/) 下載 32 位版本的 Eclipse。
  2. 安裝它並使用現有的 32 位 JVM 啟動它。

---

### 需要記住的要點
- **匹配結構**：您的 JVM 和 Eclipse 必須具有相同的結構：
  - 64 位 Eclipse 需要 64 位 JVM。
  - 32 位 Eclipse 需要 32 位 JVM。
- **雙重檢查路徑**：如果您編輯 `eclipse.ini`，請確保 `javaw.exe` 的路徑正確。
- **系統相容性**：如果您的作業系統是 64 位，升級到 64 位 JVM 是更好的長期解決方案。

按照這些步驟，您將解決錯誤並讓 Eclipse 順利運行！