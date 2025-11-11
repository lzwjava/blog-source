---
audio: false
generated: true
lang: hant
layout: post
title: 解決 Eclipse JDK 問題
translated: true
type: note
---

當你點擊 `eclipse.exe` 啟動 Eclipse 4.6.3 並遇到錯誤「Java was started but returned exit code」且提及 `Oracle\Java\javapath\javaw.exe` 時，這表示 Eclipse 正嘗試使用不相容或配置錯誤的 Java Virtual Machine (JVM)。路徑 `Oracle\Java\javapath\javaw.exe` 顯示 Eclipse 預設使用了系統 PATH 環境變數中定義的 JVM，而該 JVM 可能不適用於 Eclipse 4.6.3。為解決此問題，你需要透過配置讓 Eclipse 使用相容的 JVM 來指定正確的 Java home。具體操作如下：

### 逐步解決方案

1. **了解需求**  
   Eclipse 4.6.3 (Neon) 需要至少 Java 8 才能正常運作。此錯誤表明目前的 JVM（來自 `Oracle\Java\javapath`）可能不符合此要求或存在配置問題。你需要將 Eclipse 指向相容的 Java 安裝，例如 Java 8 JDK。

2. **尋找你的 Java 安裝位置**  
   確認系統上相容 Java 版本（例如 JDK 1.8.0）的安裝位置。Windows 上常見的位置包括：  
   - `C:\Program Files\Java\jdk1.8.0_XXX`（適用於 64 位元 Java）  
   - `C:\Program Files (x86)\Java\jdk1.8.0_XXX`（適用於 32 位元 Java）  
   請將 `XXX` 替換為具體的更新版本（例如 `231` 對應 JDK 1.8.0_231）。在此目錄內，`javaw.exe` 檔案位於 `bin` 子目錄中（例如 `C:\Program Files\Java\jdk1.8.0_XXX\bin\javaw.exe`）。

   **提示**：要確認版本與架構，請開啟命令提示字元，導航至 `bin` 目錄（例如 `cd C:\Program Files\Java\jdk1.8.0_XXX\bin`），並執行：
   ```
   java -version
   ```
   在輸出中尋找「64-Bit」或「32-Bit」以驗證架構。確保其與你的 Eclipse 版本相符（若為近期下載，很可能為 64 位元）。

3. **尋找 `eclipse.ini` 檔案**  
   `eclipse.ini` 是一個配置檔案，位於與 `eclipse.exe` 相同的目錄中。例如，若 Eclipse 安裝在 `C:\eclipse`，則該檔案位於 `C:\eclipse\eclipse.ini`。此檔案允許你指定 Eclipse 應使用的 JVM。

4. **編輯 `eclipse.ini` 檔案**  
   使用文字編輯器（例如 Notepad）以管理員權限開啟 `eclipse.ini`。你將修改此檔案以加入 `-vm` 參數，該參數會告知 Eclipse 使用哪個 JVM。請遵循以下步驟：

   - **檢查現有內容**：尋找 `-vm` 參數。若已存在，其下一行會跟隨一個路徑（例如 `-vm` 後接 `C:/some/path/bin/javaw.exe`）。若其指向有問題的 `Oracle\Java\javapath\javaw.exe`，則需替換它。若無 `-vm` 參數，則需新增。
   - **新增或修改 `-vm` 參數**：在 `-vmargs` 段落之前（若存在）或檔案頂部初始啟動參數後插入以下兩行：
     ```
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     ```
     - 使用正斜線 (`/`) 而非反斜線 (`\`) 以避免解析問題。
     - 將 `C:/Program Files/Java/jdk1.8.0_XXX` 替換為你的 Java 安裝實際路徑。
   - **確保正確放置**：`-vm` 參數必須出現在 `-vmargs` 段落之前，該段落通常以 `-vmargs` 開頭，後接 JVM 選項如 `-Xms256m` 或 `-Xmx1024m`。例如，編輯後你的 `eclipse.ini` 可能如下所示：
     ```
     -startup
     plugins/org.eclipse.equinox.launcher_1.3.201.v20161025-1711.jar
     --launcher.library
     plugins/org.eclipse.equinox.launcher.win32.win32.x86_64_1.1.401.v20161122-1740
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     -vmargs
     -Dosgi.requiredJavaVersion=1.8
     -Xms256m
     -Xmx1024m
     ```
   - **避免多餘空格或空行**：確保在 `-vm` 或路徑行之後沒有不必要的空格或空行，否則可能導致 Eclipse 錯誤解讀配置。

5. **儲存並測試**  
   儲存 `eclipse.ini` 檔案，然後雙擊 `eclipse.exe` 啟動 Eclipse。若配置正確，Eclipse 應能正常啟動，不再出現「Java was started but returned exit code」錯誤。

### 補充說明
- **架構匹配**：確保 JVM 架構（32 位元或 64 位元）與你的 Eclipse 安裝相符。64 位元 Eclipse 需要 64 位元 JVM，通常位於 `C:\Program Files\Java`；而 32 位元 Eclipse 則需要來自 `C:\Program Files (x86)\Java` 的 32 位元 JVM。
- **驗證路徑**：雙重確認 `javaw.exe` 存在於指定位置。若路徑不正確，Eclipse 將無法啟動。
- **備用方案**：若此方法無效，可考慮設定 `JAVA_HOME` 環境變數（例如 `C:\Program Files\Java\jdk1.8.0_XXX`）並更新系統 PATH 以包含 `%JAVA_HOME%\bin`。然而，修改 `eclipse.ini` 是 Eclipse 更推薦且可靠的方法。

透過編輯 `eclipse.ini` 檔案以包含帶有相容 `javaw.exe` 路徑的 `-vm` 參數，你就能有效為 Eclipse 指定 Java home，確保其使用正確的 JVM 啟動。