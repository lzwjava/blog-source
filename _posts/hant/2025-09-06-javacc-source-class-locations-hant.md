---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: JavaCC 原始碼與類別位置
translated: true
type: note
---

### JavaCC 概述
JavaCC（Java Compiler Compiler）是一個能從語法定義檔案（.jj 檔案）生成 Java 原始碼（例如解析器類別）的工具。它**不會**直接將程式碼編譯成位元組碼（.class 檔案）——這部分是由標準 Java 編譯器（如 `javac`）處理的。如果您以程式化方式使用 JavaCC（例如在 IDE 或執行環境中）來生成並編譯動態程式碼，輸出位置取決於您的設定方式。我將根據標準 JavaCC 行為和常見使用模式逐步說明。

### JavaCC 生成原始檔的位置
- **預設輸出位置**：JavaCC 會將生成的 `.java` 檔案輸出到**當前工作目錄**（若未指定則輸出至名為 "output" 的子目錄）。您可透過命令列選項（如 `-OUTPUT_DIRECTORY=<路徑>`）或在程式碼中透過 `JavaCCOptions` 類別來覆寫此設定。
- **命令列使用範例**：
  ```
  javacc -OUTPUT_DIRECTORY=/path/to/generated MyGrammar.jj
  ```
  這會在 `/path/to/generated` 目錄中建立 `.java` 檔案（例如 `Token`、`Parser`、`ParseException`）。
- **程式化使用**：若從 Java 應用程式內部呼叫 JavaCC（例如使用 `org.javacc.JavaCC.main()` 或類似 API），可透過設定選項來指定輸出路徑。生成的原始檔僅是純文字 `.java` 檔案，仍需進一步編譯。

這與官方 JavaCC 文件（例如來自 SourceForge 的舊版專案或 Maven 版本）的說明一致，文件指出生成的類別會以原始碼形式輸出至指定目錄，而非位元組碼。

### 編譯生成程式碼後的類別檔案儲存位置
JavaCC 本身不會編譯產生 `.class` 檔案——您必須手動或透過程式碼自動化此流程。後續處理如下：

- **手動編譯**：對生成的 `.java` 檔案使用 `javac`：
  ```
  javac -d /path/to/classes MyGeneratedParser.java
  ```
  - `-d` 參數用於指定 `.class` 檔案的輸出目錄，通常是 `classes/` 資料夾或專案的建置目標目錄（例如 Maven/Gradle 的 `target/classes/`）。
  - 常見位置：依建置系統不同（如 Ant、Maven）可能位於 `bin/`、`build/classes/` 或 `target/classes/`。

- **程式化動態編譯**：若在執行時期使用 JavaCC 為動態程式碼生成解析器（例如用於指令碼解譯或即時解析），通常會：
  1. 以程式化方式生成 `.java` 檔案（例如寫入暫存目錄如 `System.getProperty("java.io.tmpdir")`）。
  2. 使用 Java 編譯器 API（javax.tools.JavaCompiler）或 Janino 等函式庫進行編譯。
     - 範例：將編譯輸出設定至自訂目錄，例如 `new File("generated/classes")`。
     - 編譯後的 `.class` 檔案將儲存於該目錄。執行時期可使用自訂 ClassLoader 從該目錄或記憶體緩衝區載入它們。
  - **JVM 預設行為**：若未設定自訂路徑，類別檔案可能根據建置工具預設輸出至 `target/classes`，或根據編譯任務的設定存放於任意目錄。

- **常見動態情境**：
  - **記憶體內編譯**：編譯器 API 等函式庫允許無需寫入磁碟的編譯，透過 `ClassLoader.defineClass()` 將位元組碼儲存於記憶體中，不會產生實體儲存。
  - **暫存儲存**：若生成的程式碼需編譯並持久化，通常會輸出至 Unix 類系統的 `/tmp/` 或暫存資料夾。生產環境建議使用專案檔案系統中的專用 `generated/` 或 `cache/` 目錄。
  - **框架整合**：ANTLR（JavaCC 的替代方案）或自訂執行器等工具可能自動化此流程，將類別儲存於 RAM 或類別路徑資料夾（例如 `CLASSPATH` 條目）。

### 關鍵注意事項與最佳實踐
- **執行時期安全性**：動態編譯程式碼存在風險（例如安全性問題）。請確保使用者生成的語法經過沙箱防護。
- **建置工具整合**：若使用 Maven 或 Gradle，JavaCC 外掛（例如 `javacc-maven-plugin`）會將原始碼輸出至 `target/generated-sources/javacc/`，編譯後的類別則輸出至 `target/classes/`，這些路徑可在 `pom.xml` 或 `build.gradle` 中設定。
- **除錯技巧**：若編譯失敗，請檢查 JavaCC 的錯誤輸出或記錄檔。生成的檔案通常儲存在應用程式執行位置，而非全域目錄。
- **文件佐證**：根據 JavaCC 官方指南（javacc.github.io 或舊版文件），輸出採用目錄導向模式，後續編譯處理需由使用者自行管理。GitHub 儲存庫中的實際範例（例如搜尋 JavaCC 使用案例）顯示自訂輸出目錄如 `src/main/generated/`。

若以上說明與您的設定不符（例如特定框架或 IDE），請提供更多細節（如程式碼片段或環境資訊），我將進一步完善解答！