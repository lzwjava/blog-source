---
audio: false
generated: false
lang: hant
layout: post
title: 配置 Java 編譯器於 Visual Studio Code
translated: true
---

哈囉！要在 Windows 上配置 Visual Studio Code (VSCode) 版本 1.96.4 的 Java 編譯器，特別是你已經安裝了 Java Extension Pack，你需要設置 Java Development Kit (JDK) 路徑。Java 編譯器是 JDK 的一部分，VSCode 需要知道它的位置來編譯你的 Java 代碼。以下是逐步指南來幫助你設置：

---

### 第 1 步：確保已安裝 JDK
在 VSCode 中配置任何設定之前，請確保你已在 Windows 計算機上安裝了 JDK（而不是 JRE）。JDK 包含 Java 編譯器 (`javac`)。如果你還沒有安裝，可以從 Oracle、OpenJDK 或 Adoptium（例如 JDK 17 或與你的項目兼容的其他版本）下載。安裝後，記下安裝路徑（例如 `C:\Program Files\Java\jdk-17.0.1`）。

---

### 第 2 步：打開 VSCode 設定
要告訴 VSCode 你的 JDK 位置，你需要調整其設定：

- **通過設定 UI：**
  - 按 `Ctrl + ,` 打開設定面板。
  - 或者，前往 `File > Preferences > Settings`。
- **通過 settings.json（可選）：**
  - 按 `Ctrl + Shift + P` 打開命令面板。
  - 输入 **"Open Settings (JSON)"** 並選擇它來直接編輯 `settings.json` 文件。

---

### 第 3 步：使用 `java.home` 設置 JDK 路徑
Java Extension Pack 依賴於 `java.home` 設定來定位 JDK 進行編譯和語言功能（如 IntelliSense）。以下是如何配置它：

- **在設定 UI 中：**
  - 在設定面板中，搜索 **"java.home"**。
  - 在 "Java: Home" 字段中，輸入 JDK 安裝的完整路徑。例如：
    ```
    C:\Program Files\Java\jdk-17.0.1
    ```
  - 使用反斜杠 (`\`) 因為你在 Windows 上，並確保路徑指向 JDK 根目錄（它應該包含一個包含 `javac.exe` 的 `bin` 文件夾）。

- **在 settings.json 中：**
  - 如果你正在編輯 `settings.json`，添加這一行（用你的實際 JDK 位置替換路徑）：
    ```json
    "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    ```
  - 完整的 `settings.json` 示例：
    ```json
    {
        "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    }
    ```
  - 編輯後保存文件。

---

### 第 4 步：驗證路徑
雙重檢查：
- 路徑指向 JDK（而不是 JRE）。JDK 的 `bin` 文件夾應該包含 `javac.exe`。
- 路徑中沒有拼寫錯誤，並與你的 JDK 安裝位置匹配（例如 `C:\Program Files\Java\jdk-17.0.1`）。

如果你不確定 JDK 安裝在哪裡，可以在 `C:\Program Files\Java` 或你在安裝過程中選擇的位置找到它。

---

### 第 5 步：可選 - 配置多個 JDK
如果你安裝了多個 JDK 版本並希望在它們之間切換（例如，一個項目使用 JDK 8，另一個項目使用 JDK 17），你可以使用 `java.configuration.runtimes` 設定：

- 將以下內容添加到你的 `settings.json`：
  ```json
  "java.configuration.runtimes": [
      {
          "name": "JavaSE-1.8",
          "path": "C:\\Program Files\\Java\\jdk1.8.0_291"
      },
      {
          "name": "JavaSE-17",
          "path": "C:\\Program Files\\Java\\jdk-17.0.1",
          "default": true
      }
  ]
  ```
- `default: true` 選項設置默認運行時來運行你的代碼。然而，對於編譯，Java 扩展主要使用 `java.home` 中指定的 JDK。

---

### 第 6 步：重新加載或重啟 VSCode
設置 `java.home` 後，你可能需要：
- 重新加載 VSCode 窗口（按 `Ctrl + Shift + P`，輸入 **"Reload Window"**，然後選擇它）。
- 或完全重啟 VSCode 以使更改生效。

---

### 編譯說明
- **單個 Java 文件：** 如果你正在處理單個 `.java` 文件（沒有構建工具），Java Extension Pack 的 "Language Support for Java(TM) by Red Hat" 使用 `java.home` 中的 JDK 來編譯和運行你的代碼。你可以使用 "Run" 按鈕或 **"Java: Run"** 命令。
- **使用構建工具的項目：** 如果你使用 Maven、Gradle 或其他構建工具，編譯器由構建工具的配置管理（例如 `JAVA_HOME` 環境變量、Maven 的 `pom.xml` 或 Gradle 的 `build.gradle`）。然而，設置 `java.home` 仍然確保 VSCode 的語言功能正常工作。

---

### 錯誤排除
- **路徑問題：** 如果 VSCode 無法找到 JDK，請重新檢查 `java.home` 中的路徑。避免不必要的空格或引號，除非必要。
- **未安裝 JDK：** 如果你收到關於缺少 `javac` 的錯誤，請確保已安裝 JDK。
- **版本兼容性：** 確保你的 JDK 版本與項目的要求匹配（例如 JDK 8、11、17）。

---

這就是了！你現在應該已經在 VSCode 中配置了 Java 編譯器。如果你遇到任何問題或有更多問題——例如使用特定的構建工具——請隨時告訴我，我會很高興進一步幫助你！ 😊

---

設置 `maven.terminal.userJavaHome` 為 true。你可以在終端中檢查 Java 版本。