---
audio: false
generated: true
lang: hant
layout: post
title: 在 Visual Studio Code 中配置 Java 編譯器
translated: true
type: note
---

你好！要在 Windows 系統上的 Visual Studio Code (VSCode) 1.96.4 版本中配置 Java 編譯器，特別是當你已經安裝了 Java Extension Pack 後，你需要設定 Java Development Kit (JDK) 的路徑。Java 編譯器是 JDK 的一部分，VSCode 需要知道其位置才能編譯你的 Java 程式碼。以下是詳細的設定步驟：

---

### 步驟 1：確保已安裝 JDK
在 VSCode 中進行任何配置之前，請先確認你的 Windows 電腦已安裝 JDK（而不僅僅是 JRE）。JDK 包含了 Java 編譯器 (`javac`)。如果尚未安裝，你可以從 Oracle、OpenJDK 或 Adoptium 等供應商下載（例如 JDK 17 或與你的專案相容的其他版本）。安裝完成後，請記下安裝路徑（例如 `C:\Program Files\Java\jdk-17.0.1`）。

---

### 步驟 2：開啟 VSCode 設定
要告訴 VSCode 你的 JDK 位置，你需要調整其設定：

- **透過設定介面：**
  - 按下 `Ctrl + ,` 開啟設定面板。
  - 或者，前往 `檔案 > 偏好設定 > 設定`。
- **透過 settings.json（可選）：**
  - 按下 `Ctrl + Shift + P` 開啟命令選擇區。
  - 輸入 **"Open Settings (JSON)"** 並選擇它，以直接編輯 `settings.json` 檔案。

---

### 步驟 3：使用 `java.home` 設定 JDK 路徑
Java Extension Pack 依賴 `java.home` 設定來定位你的 JDK，以進行編譯和語言功能（如 IntelliSense）。配置方法如下：

- **在設定介面中：**
  - 在設定面板中，搜尋 **"java.home"**。
  - 在 "Java: Home" 欄位中，輸入你的 JDK 完整安裝路徑。例如：
    ```
    C:\Program Files\Java\jdk-17.0.1
    ```
  - 由於你在 Windows 上，請使用反斜線 (`\`)，並確保路徑指向 JDK 的根目錄（其中應包含帶有 `javac.exe` 的 `bin` 資料夾）。

- **在 settings.json 中：**
  - 如果你正在編輯 `settings.json`，請加入這一行（將路徑替換為你的實際 JDK 位置）：
    ```json
    "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    ```
  - 完整的 `settings.json` 範例：
    ```json
    {
        "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    }
    ```
  - 編輯後儲存檔案。

---

### 步驟 4：驗證路徑
請仔細檢查：
- 路徑指向的是 JDK（而非 JRE）。JDK 的 `bin` 資料夾應包含 `javac.exe`。
- 路徑中沒有拼寫錯誤，且與你的 JDK 安裝位置相符（例如 `C:\Program Files\Java\jdk-17.0.1`）。

如果不確定 JDK 的安裝位置，你可以在 `C:\Program Files\Java` 或安裝時選擇的路徑中找到。

---

### 步驟 5：可選 - 配置多個 JDK
如果你安裝了多個 JDK 版本並希望在不同版本間切換（例如，某個專案使用 JDK 8，另一個使用 JDK 17），你可以使用 `java.configuration.runtimes` 設定：

- 將以下內容加入你的 `settings.json`：
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
- `default: true` 選項會設定為執行程式碼的預設運行環境。然而，對於編譯，Java 擴充功能主要使用 `java.home` 中指定的 JDK。

---

### 步驟 6：重新載入或重啟 VSCode
設定 `java.home` 後，你可能需要：
- 重新載入 VSCode 視窗（按下 `Ctrl + Shift + P`，輸入 **"Reload Window"** 並選擇它）。
- 或者完全重啟 VSCode 以使變更生效。

---

### 關於編譯的注意事項
- **單一 Java 檔案：** 如果你正在處理獨立的 `.java` 檔案（未使用建置工具），Java Extension Pack 的 "Language Support for Java(TM) by Red Hat" 會使用 `java.home` 中的 JDK 來編譯和執行你的程式碼。你可以使用 "Run" 按鈕或 **"Java: Run"** 命令。
- **使用建置工具的專案：** 如果你使用 Maven、Gradle 或其他建置工具，編譯器將由建置工具的配置管理（例如 `JAVA_HOME` 環境變數、Maven 的 `pom.xml` 或 Gradle 的 `build.gradle`）。然而，設定 `java.home` 仍能確保 VSCode 的語言功能正常運作。

---

### 疑難排解
- **路徑問題：** 如果 VSCode 無法找到 JDK，請仔細檢查 `java.home` 中的路徑。避免不必要的空格或引號。
- **未安裝 JDK：** 如果出現關於缺少 `javac` 的錯誤，請確保已安裝 JDK。
- **版本相容性：** 請確保你的 JDK 版本符合專案要求（例如 JDK 8、11、17）。

---

就是這樣！你現在應該已經在 VSCode 中配置好了 Java 編譯器。如果你遇到任何問題或有更多疑問——例如使用特定的建置工具——請隨時告訴我，我很樂意進一步協助！😊

---

將 `maven.terminal.userJavaHome` 設定為 true。你可以在終端機中檢查 Java 版本。