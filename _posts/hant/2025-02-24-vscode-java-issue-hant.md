---
audio: false
generated: true
lang: hant
layout: post
title: Java 語言伺服器與 Maven 建置工具
translated: true
type: note
---

聽起來你在 Visual Studio Code (VSCode) 中遇到了兩個相關問題：一個是系統提示需要至少 Java 21，另一個是 VSCode 無法識別你 Java 程式碼中的某些物件定義，即使你的 Maven 建置能夠成功編譯。讓我們逐步解決這些問題。

這個問題的根源在於 VSCode 的 Java 擴充功能（特別是 Java Language Server）和你的 Maven 建置可能在 Java 開發套件 (JDK) 版本或專案配置上不一致。VSCode 提示需要 JDK 21 才能正常運作，而解析錯誤表明它解析程式碼的方式與 Maven 不同。以下是解決方法：

---

### 步驟 1：安裝 JDK 21
由於 VSCode 明確要求 Java 21，你需要確保系統中已安裝該版本。

- **下載 JDK 21**：從可靠來源獲取，例如 [Oracle 官網](https://www.oracle.com/java/technologies/javase-jdk21-downloads.html) 或 [Adoptium](https://adoptium.net/)。
- **安裝**：按照安裝說明操作，並記下安裝路徑（例如 Windows 上的 `C:\Program Files\Java\jdk-21` 或 Linux 上的 `/usr/lib/jvm/java-21-openjdk`）。
- **驗證**：開啟終端機並執行 `java -version`。你應該會看到類似以下的輸出：
  ```
  java version "21.0.1" ...
  ```

---

### 步驟 2：配置 VSCode 使用 JDK 21
你需要告訴 VSCode 的 Java 擴充功能使用 JDK 21。方法如下：

1. **開啟 VSCode 設定**：
   - 前往 `檔案 > 偏好設定 > 設定`（或按下 `Ctrl + ,`）。
2. **設定 JDK 路徑**：
   - 搜尋 `java.jdt.ls.java.home`。
   - 輸入你的 JDK 21 安裝路徑（例如 `C:\Program Files\Java\jdk-21`）。
   - 可選：搜尋 `java.home` 並設定為相同的路徑以保持一致性。
3. **編輯 `settings.json`（替代方法）**：
   - 開啟命令選擇區 (`Ctrl + Shift + P`)，輸入「Preferences: Open Settings (JSON)」，然後新增：
     ```json
     {
         "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-21",
         "java.home": "C:\\Program Files\\Java\\jdk-21"
     }
     ```
   - 根據你的系統調整路徑（Linux/Mac 使用正斜線 `/`）。

這將確保 VSCode 中的 Java Language Server 使用 JDK 21，滿足最低要求。

---

### 步驟 3：在 VSCode 中設定專案的 JDK
為了解決解析問題（例如找不到物件定義），請確保你的 VSCode 專案也使用 JDK 21：

- 在 `settings.json` 中，新增以下內容以指定專案使用 JDK 21：
  ```json
  "java.configuration.runtimes": [
      {
          "name": "JavaSE-21",
          "path": "C:\\Program Files\\Java\\jdk-21",
          "default": true
      }
  ]
  ```
- 這將使 VSCode 的專案執行環境與 JDK 21 對齊，有助於正確解析你的程式碼。

---

### 步驟 4：驗證 Maven 的 JDK 配置
由於你的 Maven 建置 (`mvn compile`) 運作正常，它很可能使用了相容的 JDK。讓我們確認並使其與 VSCode 對齊：

1. **檢查 Maven 的 JDK**：
   - 在終端機中執行 `mvn -version`。查看「Java version」這一行（例如 `Java version: 21.0.1`）。
   - 如果它沒有使用 JDK 21，請將 `JAVA_HOME` 環境變數設定為你的 JDK 21 路徑：
     - **Windows**：`set JAVA_HOME=C:\Program Files\Java\jdk-21`
     - **Linux/Mac**：`export JAVA_HOME=/usr/lib/jvm/java-21-openjdk`
   - 再次執行 `mvn -version` 以確認。
2. **在 `pom.xml` 中指定 JDK**（可選）：
   - 如果你想在 Maven 專案中強制使用 JDK 21，請在 `pom.xml` 中新增以下內容：
     ```xml
     <properties>
         <maven.compiler.source>21</maven.compiler.source>
         <maven.compiler.target>21</maven.compiler.target>
     </properties>
     ```

---

### 步驟 5：重新整理 VSCode
進行這些更改後，需要重新整理 VSCode 以應用它們：

- 重新載入 VSCode：
  - 開啟命令選擇區 (`Ctrl + Shift + P`) 並選擇「Developer: Reload Window」。
- 或者，關閉並重新開啟 VSCode。

---

### 步驟 6：確保依賴項已載入
如果 VSCode 仍然找不到物件定義，可能是因為它沒有正確載入你的 Maven 依賴項：

1. **清理工作區**：
   - 開啟命令選擇區 (`Ctrl + Shift + P`)。
   - 執行「Java: Clean Java Language Server Workspace」。
2. **強制編譯**：
   - 在命令選擇區中執行「Java: Force Java Compilation」。
3. **檢查匯入**：
   - 確保你的專案 Maven 依賴項已匯入，方法是右鍵點擊 VSCode 中的 `pom.xml` 並選擇「Update Project Configuration」。

---

### 疑難排解
如果問題仍然存在：
- **檢查日誌**：
  - 在 `settings.json` 中新增 `"java.trace.server": "verbose"`。
  - 開啟輸出面板 (`Ctrl + Shift + U`) 並選擇「Java Language Server」以查看詳細日誌。
- **驗證程式碼**：
  - 再次檢查缺失的物件定義是來自你的程式碼還是 `pom.xml` 中列出的依賴項，而非外部問題。

---

### 總結
通過安裝 JDK 21、配置 VSCode 使用它、對齊你的專案和 Maven 設定，並重新整理環境，VSCode 應該會停止對 Java 21 的抱怨，並正確解析你的程式碼，與 Maven 的成功編譯保持一致。如果你遇到任何困難，請告訴我！