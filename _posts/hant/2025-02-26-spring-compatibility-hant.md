---
audio: false
generated: true
lang: hant
layout: post
title: Java 版本與 Spring Boot 的兼容性
translated: true
type: note
---

### 理解錯誤原因

當你使用 Spring Boot 3.4.3 執行 `mvn spring-boot:run` 並遇到錯誤「class file has wrong version 61.0, should be 52.0」時，這表示存在 Java 版本相容性問題。在 Java 中，類別檔案具有對應編譯時所用 Java 版本的版本號：

- **版本 52.0** 對應 Java 8
- **版本 61.0** 對應 Java 17

此錯誤表明你的 Spring Boot 應用程式類別檔案是用 Java 17（版本 61.0）編譯的，但嘗試執行它們的 Java 虛擬機（JVM）預期的是與 Java 8（版本 52.0）相容的類別檔案。由於 Java 8 的 JVM 無法執行用 Java 17 編譯的類別檔案（因為 Java 在此情境下是向後相容而非向前相容），因此會出現此錯誤。

### 問題發生原因

Spring Boot 3.4.3 要求最低支援版本為 **Java 17 或更新版本**。這意味著你的專案應該使用至少 Java 17 進行編譯和執行。出現版本不符的情況可能是因為：

1. **編譯環境**：你的專案設定為使用 Java 17 編譯，產生了版本 61.0 的類別檔案。這通常透過 `pom.xml` 中的 `maven-compiler-plugin` 或 `<java.version>` 屬性設定
2. **執行環境**：當你執行 `mvn spring-boot:run` 時，Spring Boot Maven 插件會啟動新的 Java 程序來運行應用程式。然而它使用的 `java` 執行檔來自 Java 8 安裝（版本 52.0），無法處理 Java 17 編譯的類別檔案

### 解決步驟

要解決此問題，你需要確保編譯和執行環境都使用 Java 17。以下是修復方法：

#### 1. 確認專案的 Java 版本
首先確認你的專案設定為使用 Java 17。在 `pom.xml` 中檢查以下內容：

```xml
<properties>
    <java.version>17</java.version>
</properties>
```

此屬性告訴 `maven-compiler-plugin` 使用 Java 17 編譯你的程式碼。Spring Boot 3.4.3 預設會設定此值，但最好確認一下。如果缺少此設定或設為其他版本（例如 8），請更新為 17。

#### 2. 安裝 Java 17
確保系統已安裝 Java 17。你可以從以下位置下載：

- [Adoptium (Eclipse Temurin)](https://adoptium.net/)
- [Oracle JDK](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)（若你接受授權條款）

要檢查是否已安裝 Java 17，請開啟終端機並執行：

```bash
java -version
```

如果未顯示 Java 17（例如 `openjdk 17.x.x` 或類似內容），請安裝後繼續。

#### 3. 更新環境以使用 Java 17
Spring Boot Maven 插件使用來自環境的 `java` 執行檔，通常由 `JAVA_HOME` 環境變數或系統 PATH 中的 `java` 命令決定。如果你當前的 `java` 命令指向 Java 8，則需要更新它。

##### 選項 A：設定 JAVA_HOME 和 PATH
將 `JAVA_HOME` 環境變數指向 Java 17 安裝目錄，並確保 PATH 中的 `java` 命令使用它。

- **在 Linux/Mac 上**：
  1. 找到你的 Java 17 安裝目錄（例如 `/usr/lib/jvm/java-17-openjdk` 或你的安裝位置）
  2. 在終端機中設定 `JAVA_HOME` 並更新 `PATH`：
     ```bash
     export JAVA_HOME=/path/to/java-17
     export PATH=$JAVA_HOME/bin:$PATH
     ```
  3. 驗證：
     ```bash
     java -version
     ```
     現在應該顯示 Java 17

  要永久設定，請將 `export` 行加入你的 shell 設定檔（例如 `~/.bashrc`、`~/.zshrc`）

- **在 Windows 上**：
  1. 找到 Java 17 安裝目錄（例如 `C:\Program Files\Java\jdk-17`）
  2. 設定 `JAVA_HOME`：
     - 開啟系統屬性視窗（在開始功能表中搜尋「環境變數」）
     - 在「系統變數」下，新增或更新 `JAVA_HOME` 為 `C:\Program Files\Java\jdk-17`
  3. 更新 `Path`：
     - 在「系統變數」中，編輯 `Path` 並新增 `%JAVA_HOME%\bin`（確保它在最前面或移除舊的 Java 路徑如 Java 8）
  4. 開啟新的命令提示字元並驗證：
     ```cmd
     java -version
     ```
     應該顯示 Java 17

##### 選項 B：為 Maven 使用特定 Java 版本
如果你安裝了多個 Java 版本且不想變更系統全域的 `JAVA_HOME`，可以讓 Maven 使用特定的 Java 版本：

- 在執行 `mvn spring-boot:run` 前，僅為該命令設定 `JAVA_HOME`：
  ```bash
  JAVA_HOME=/path/to/java-17 mvn spring-boot:run
  ```
  這可確保 Spring Boot Maven 插件使用 Java 17，而不改變你的系統設定

#### 4. 再次執行應用程式
正確設定 Java 17 後，執行：

```bash
mvn spring-boot:run
```

插件現在將使用 Java 17 來執行你的應用程式，與編譯的類別檔案版本（61.0）相符，錯誤應該會消失。

### 額外檢查
- **Maven 的 Java 版本**：執行 `mvn -version` 查看 Maven 使用的 Java 版本。它應該與你的 `JAVA_HOME` 相符。如果不符合，請確保 PATH 和 `JAVA_HOME` 設定正確
- **相依性**：如果錯誤仍然存在，可能是某個相依性使用 Java 17 編譯，而你的執行環境仍設定錯誤。由於 Spring Boot 3.4.3 強制要求 Java 17，確保執行環境為 Java 17 應該能解決此問題

### 為何不能使用 Java 8？
Spring Boot 3.4.3 不支援 Java 8。如果你需要使用 Java 8，必須降級到舊版 Spring Boot（例如 2.x），但除非有特定限制，否則不建議這樣做。由於你的類別檔案是版本 61.0，堅持使用 Java 17 符合 Spring Boot 3.4.3 的要求。

### 最終解決方案總結
要修復在 Spring Boot 3.4.3 中執行 `mvn spring-boot:run` 時出現的「class file has wrong version 61.0, should be 52.0」錯誤：

1. 確保 `pom.xml` 中有 `<java.version>17</java.version>`
2. 如果尚未安裝，請安裝 Java 17
3. 將 `JAVA_HOME` 設定為你的 Java 17 安裝目錄
4. 更新 PATH，使 `java -version` 顯示 Java 17
5. 再次執行 `mvn spring-boot:run`

這可確保你的執行環境與編譯的 Java 17 類別檔案相符，解決相容性問題。