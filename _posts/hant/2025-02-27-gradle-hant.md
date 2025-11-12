---
audio: false
generated: true
lang: hant
layout: post
title: Gradle：建構自動化工具
translated: true
type: note
---

Gradle 是一款強大的建構自動化工具，常用於 Java、Kotlin 和 Android 專案，但其靈活性也足以應對其他語言。以下是一份適合新手的入門指南，幫助你有效使用 Gradle：

---

### 1. **安裝 Gradle**
使用 Gradle 前需先安裝：
- **Mac/Linux (使用 Homebrew)**：
  - 在終端機執行 `brew install gradle`。
- **Windows (或手動安裝)**：
  - 從 [gradle.org](https://gradle.org/install/) 下載 Gradle 二進位檔。
  - 解壓縮至資料夾（例如 `C:\Gradle` 或 `/opt/gradle`）。
  - 將 Gradle 的 `bin` 目錄（例如 `C:\Gradle\gradle-8.x\bin`）新增至系統的 PATH 環境變數。
- **驗證安裝**：
  - 開啟終端機並執行 `gradle -v`，你應看到 Gradle 版本與詳細資訊。

若專案已包含 **Gradle Wrapper**（常見於共享專案），則無需全域安裝 Gradle——只需在專案目錄中使用 `./gradlew` (Linux/Mac) 或 `gradlew.bat` (Windows)。

---

### 2. **理解 Gradle 基礎**
Gradle 使用 **Groovy** 或 **Kotlin** 腳本（通常是 `build.gradle` 或 `build.gradle.kts`）定義專案建置方式。關鍵概念如下：
- **專案**：Gradle 建置可包含一個或多個專案（例如單一應用程式或多模組設定）。
- **任務**：Gradle 執行的動作，例如 `compileJava`、`test` 或 `build`。
- **相依性**：Gradle 管理專案所需的函式庫（例如從 Maven Central 或 Google 儲存庫取得）。

---

### 3. **建立簡單的 Gradle 專案**
讓我們建立基礎 Java 專案來體驗 Gradle：
1. **建立專案資料夾**：
   - 建立目錄（例如 `my-gradle-project`）並在終端機中導航至該目錄。
2. **初始化 Gradle**：
   - 執行 `gradle init`。
   - 依提示選擇「application」、「Java」及建置腳本的「Groovy」（或 Kotlin）。
   - 此操作會建立包含 `build.gradle` 檔案與範例程式碼的基礎結構。
3. **檢視生成的 `build.gradle`**：
   ```groovy
   plugins {
       id 'java'
       id 'application'
   }

   repositories {
       mavenCentral()
   }

   dependencies {
       implementation 'org.slf4j:slf4j-api:1.7.36'
   }

   application {
       mainClass = 'com.example.App'  // 請根據你的套件名稱調整
   }
   ```
   - `plugins`：新增 Java 支援與應用程式執行功能。
   - `repositories`：Gradle 搜尋相依性的來源（例如 Maven Central）。
   - `dependencies`：專案使用的函式庫。
   - `application`：指定執行的主類別。

4. **執行任務**：
   - 建置專案：`gradle build`。
   - 執行應用程式：`gradle run`。
   - 列出可用任務：`gradle tasks`。

---

### 4. **常用 Gradle 指令**
以下是你會頻繁使用的指令：
- `gradle build`：編譯並打包專案。
- `gradle clean`：刪除 `build` 目錄以重新開始。
- `gradle test`：執行專案測試。
- `gradle dependencies`：顯示相依性樹狀圖。
- `./gradlew <task>`：使用專案的 Gradle Wrapper 而非全域安裝版本。

---

### 5. **新增相依性**
要使用外部函式庫，請編輯 `build.gradle`。例如新增 Gson（JSON 解析庫）：
```groovy
dependencies {
    implementation 'com.google.code.gson:gson:2.10.1'
}
```
接著執行 `gradle build` 以下載該函式庫。

---

### 6. **自訂建置設定**
你可以在 `build.gradle` 中新增自訂任務或調整設定。自訂任務範例：
```groovy
task hello {
    doLast {
        println 'Hello, Gradle!'
    }
}
```
使用 `gradle hello` 執行此任務。

---

### 7. **使用 Gradle Wrapper（團隊協作推薦）**
Gradle Wrapper 能確保所有人使用相同版本的 Gradle：
- 生成 Wrapper：`gradle wrapper`。
- 使用方式：`./gradlew build`（Windows 則為 `gradlew.bat build`）。

---

### 8. **成功使用技巧**
- **文件參考**：查閱 [Gradle 官方文件](https://docs.gradle.org/current/userguide/userguide.html) 以深入學習。
- **快取機制**：Gradle 會快取相依性與任務輸出，因此建置速度會隨時間提升。
- **外掛擴充**：探索各類外掛（例如 Spring Boot、Android 或程式碼品質檢測）以擴充功能。

---

### 範例：建置並執行 Java 應用程式
若你的 `src/main/java/com/example/App.java` 內容如下：
```java
package com.example;
public class App {
    public static void main(String[] args) {
        System.out.println("Hello from Gradle!");
    }
}
```
執行 `gradle run`，你將看到輸出結果。

---

如需特定 Gradle 任務、專案設定或疑難排解協助，歡迎隨時提問！你正在進行什麼類型的專案呢？