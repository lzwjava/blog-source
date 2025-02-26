---
audio: false
lang: hant
layout: post
title: 解決 Eclipse JDK 問題
translated: true
---

當你點擊 `eclipse.exe` 啟動 Eclipse 4.6.3 時，如果遇到錯誤 "Java was started but returned exit code" 並提到 `Oracle\Java\javapath\javaw.exe`，這意味著 Eclipse 正嘗試使用一個不相容或配置不當的 Java 虛擬機 (JVM)。路徑 `Oracle\Java\javapath\javaw.exe` 表示 Eclipse 默認使用系統 PATH 環境變量中定義的 JVM，這可能不適合 Eclipse 4.6.3。要解決這個問題，你需要通過配置 Eclipse 使用相容的 JVM 來指定正確的 Java 家目錄。以下是如何做到的：

### 分步解決方案

1. **了解需求**
   Eclipse 4.6.3 (Neon) 需要至少 Java 8 才能正常運行。錯誤建議當前 JVM（來自 `Oracle\Java\javapath`）可能不符合這個要求或有配置問題。你需要將 Eclipse 指向一個相容的 Java 安裝，例如 Java 8 JDK。

2. **定位你的 Java 安裝**
   確定系統上安裝了相容的 Java 版本（例如 JDK 1.8.0）。Windows 上的常見位置包括：
   - `C:\Program Files\Java\jdk1.8.0_XXX`（適用於 64 位 Java）
   - `C:\Program Files (x86)\Java\jdk1.8.0_XXX`（適用於 32 位 Java）
   將 `XXX` 替換為具體的更新版本（例如 `231` 適用於 JDK 1.8.0_231）。在這個目錄中，`javaw.exe` 文件位於 `bin` 子目錄中（例如 `C:\Program Files\Java\jdk1.8.0_XXX\bin\javaw.exe`）。

   **提示**：要確認版本和架構，打開命令提示符，導航到 `bin` 目錄（例如 `cd C:\Program Files\Java\jdk1.8.0_XXX\bin`），然後運行：
   ```
   java -version
   ```
   在輸出中查找 "64-Bit" 或 "32-Bit" 以驗證架構。確保它與你的 Eclipse 版本匹配（如果最近下載，很可能是 64 位）。

3. **找到 `eclipse.ini` 文件**
   `eclipse.ini` 文件是一個配置文件，位於與 `eclipse.exe` 相同的目錄中。例如，如果 Eclipse 安裝在 `C:\eclipse`，文件將位於 `C:\eclipse\eclipse.ini`。這個文件允許你指定 Eclipse 應該使用的 JVM。

4. **編輯 `eclipse.ini` 文件**
   使用文本編輯器（例如記事本）以管理員權限打開 `eclipse.ini`。你將修改它以包含 `-vm` 參數，告訴 Eclipse 使用哪個 JVM。按照以下步驟進行：

   - **檢查現有內容**：查找 `-vm` 參數。如果已經存在，它將在下一行後跟隨一個路徑（例如 `-vm` 後跟 `C:/some/path/bin/javaw.exe`）。如果它指向問題的 `Oracle\Java\javapath\javaw.exe`，你將替換它。如果不存在 `-vm` 參數，你將添加它。
   - **添加或修改 `-vm` 參數**：在 `-vmargs` 部分（如果存在）之前插入以下兩行，或者在文件頂部的初始啟動參數後面：
     ```
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     ```
     - 使用正斜杠（`/`）而不是反斜杠（`\`）以避免解析問題。
     - 將 `C:/Program Files/Java/jdk1.8.0_XXX` 替換為你的 Java 安裝的實際路徑。
   - **確保正確位置**：`-vm` 參數必須出現在 `-vmargs` 部分之前，這部分通常以 `-vmargs` 開頭，後跟 JVM 選項如 `-Xms256m` 或 `-Xmx1024m`。例如，編輯後的 `eclipse.ini` 可能如下所示：
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
   - **避免額外空格或空行**：確保 `-vm` 或路徑行後面沒有不必要的空格或空行，否則 Eclipse 可能會誤解配置。

5. **保存並測試**
   保存 `eclipse.ini` 文件，然後雙擊 `eclipse.exe` 以啟動 Eclipse。如果配置正確，Eclipse 應該能夠在沒有 "Java was started but returned exit code" 錯誤的情況下啟動。

### 額外說明
- **架構匹配**：確保 JVM 架構（32 位或 64 位）與你的 Eclipse 安裝匹配。64 位 Eclipse 需要 64 位 JVM，通常在 `C:\Program Files\Java` 中找到，而 32 位 Eclipse 需要 32 位 JVM 來自 `C:\Program Files (x86)\Java`。
- **驗證路徑**：雙重檢查 `javaw.exe` 是否存在於指定位置。如果路徑不正確，Eclipse 將無法啟動。
- **備用選項**：如果這個方法不起作用，考慮設置 `JAVA_HOME` 環境變量（例如 `C:\Program Files\Java\jdk1.8.0_XXX`）並更新系統 PATH 以包含 `%JAVA_HOME%\bin`。然而，修改 `eclipse.ini` 是 Eclipse 的首選和更可靠的方法。

通過編輯 `eclipse.ini` 文件以包含 `-vm` 參數和指向相容 `javaw.exe` 的路徑，你有效地為 Eclipse 指定了 Java 家目錄，確保它使用正確的 JVM 來啟動。