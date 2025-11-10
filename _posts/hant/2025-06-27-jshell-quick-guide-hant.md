---
audio: false
generated: true
lang: hant
layout: post
title: JShell 快速入門指南
translated: true
type: note
---

JShell 是一款互動式 REPL（讀取-執行-輸出循環）工具，自 JDK 9 起隨 Java 開發工具包（JDK）提供。它讓你能直接執行 Java 程式碼片段，無需編寫完整程式。以下是使用 JShell 的簡明指南：

### 1. **啟動 JShell**
- **確認 JDK 已安裝**：確保你已安裝 JDK 9 或更新版本。可在終端機或命令提示字元中執行 `java -version` 來檢查。
- **啟動 JShell**：
  - 開啟終端機或命令提示字元。
  - 輸入 `jshell` 後按 Enter。
  - 看到 `jshell>` 提示符號即表示 JShell 已就緒。

### 2. **基礎用法**
- **執行 Java 程式碼**：
  - 直接在提示符號後輸入 Java 表達式、陳述式或宣告。
  - 範例：
    ```java
    jshell> System.out.println("Hello, JShell!")
    Hello, JShell!
    ```
  - JShell 會立即評估輸入內容並顯示結果。

- **變數與表達式**：
  - 宣告變數或評估表達式：
    ```java
    jshell> int x = 10
    x ==> 10
    jshell> x * 2
    $2 ==> 20
    ```
  - JShell 會自動為表達式結果分配暫存名稱（例如 `$2`）。

- **定義方法與類別**：
  - 可定義方法或類別：
    ```java
    jshell> void sayHello() { System.out.println("Hello!"); }
    |  created method sayHello()
    jshell> sayHello()
    Hello!
    ```
    ```java
    jshell> class Test { int x = 5; }
    |  created class Test
    jshell> Test t = new Test()
    t ==> Test@7c417213
    jshell> t.x
    $5 ==> 5
    ```

### 3. **關鍵指令**
JShell 提供以 `/` 開頭的內建指令，以下為常用指令：
- **列出所有程式碼**：`/list` – 顯示工作階段中輸入的所有程式碼片段。
  ```java
  jshell> /list
  ```
- **編輯程式碼**：`/edit <id>` – 為指定 ID 的程式碼片段開啟圖形編輯介面（ID 來自 `/list`）。
- **儲存工作階段**：`/save myfile.java` – 將所有程式碼片段儲存至檔案。
- **載入檔案**：`/open myfile.java` – 從檔案載入並執行程式碼。
- **檢視變數**：`/vars` – 列出所有已宣告變數。
  ```java
  jshell> /vars
  |    int x = 10
  ```
- **檢視方法**：`/methods` – 列出所有已定義方法。
- **結束 JShell**：`/exit` – 關閉 JShell 工作階段。
- **協助說明**：`/help` – 顯示所有可用指令。

### 4. **匯入套件**
- JShell 會自動匯入常用套件（如 `java.util`、`java.io`）。如需使用其他套件，可手動匯入：
  ```java
  jshell> import java.time.LocalDate
  jshell> LocalDate.now()
  $3 ==> 2025-06-27
  ```

### 5. **編輯與修正程式碼**
- **修改現有程式碼**：
  - 使用 `/list` 查詢程式碼片段 ID。
  - 直接輸入新版本即可重新定義，JShell 會覆寫舊定義：
    ```java
    jshell> int x = 5
    x ==> 5
    jshell> int x = 10
    x ==> 10
    ```
- **刪除片段**：`/drop <id>` – 依 ID 移除特定程式碼片段。

### 6. **Tab 鍵自動完成**
- 按 `Tab` 鍵可自動完成類別名稱、方法或指令。
- 範例：
  ```java
  jshell> System.out.pr<tab>
  ```
  系統會建議 `println`、`print` 等選項。

### 7. **執行外部指令稿**
- 載入並執行 Java 檔案：
  ```java
  jshell> /open MyScript.java
  ```
- 亦可透過指令稿啟動 JShell：
  ```bash
  jshell MyScript.java
  ```

### 8. **自訂 JShell**
- **啟動指令稿**：建立包含匯入指令或常用程式碼的檔案（如 `startup.jsh`），透過 `/open startup.jsh` 載入，或設為預設啟動指令稿：
  ```bash
  jshell --start startup.jsh
  ```
- **回饋模式**：使用 `/set feedback <mode>` 調整輸出詳細程度（如 `normal`、`concise`、`verbose`）。

### 9. **實用技巧**
- **快速原型設計**：使用 JShell 測試小型程式碼片段、實驗 API 或學習 Java 語法。
- **錯誤處理**：JShell 提供清晰的錯誤訊息，並可即時修正錯誤。
- **多行輸入**：針對複雜程式碼，JShell 支援多行編輯。在行尾加上反斜線（`\`）即可續行：
  ```java
  jshell> int sum(int a, int b) { \
      ...> return a + b; \
      ...> }
  ```

### 10. **疑難排解**
- **找不到 JShell**：請確認 JDK 的 `bin` 目錄已加入系統 PATH 環境變數。
- **啟動緩慢**：部分系統中 JShell 可能需要較長時間初始化，請確保 JDK 為最新版本。
- **重設工作階段**：使用 `/reset` 可清除所有程式碼片段並重新開始。

如需詳細資訊，請查閱官方 JDK 文件或在 JShell 中執行 `/help`。如果你有特定任務或想嘗試的程式碼，歡迎告訴我，我會進一步為你指引！