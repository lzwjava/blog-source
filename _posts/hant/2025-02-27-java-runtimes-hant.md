---
audio: false
generated: true
lang: hant
layout: post
title: Visual Studio Code 中的 Java 運行環境
translated: true
type: note
---

要在 Visual Studio Code（VS Code）設定中使用 `java.configuration.runtimes`，你需要在 `settings.json` 檔案中進行配置。此設定允許你指定多個 Java 開發工具包（JDK）版本供 VS Code 在 Java 專案中使用。當處理需要特定 Java 版本的不同專案時，這尤其有用。以下是設定步驟：

### 配置 `java.configuration.runtimes` 的步驟

1. **開啟 VS Code 設定**：
   - Windows/Linux：前往 `檔案 > 偏好設定 > 設定` 或按下 `Ctrl + ,`。
   - macOS：前往 `Code > Preferences > Settings` 或按下 `Cmd + ,`。

2. **存取 JSON 設定檔案**：
   - 在設定介面中，搜尋 `java.configuration.runtimes`。
   - 你會看到類似「Java: Configuration: Runtimes」的選項。點擊「Edit in settings.json」（通常是設定描述下方的連結）以開啟 `settings.json` 檔案。

3. **編輯 `settings.json`**：
   - 在 `settings.json` 檔案中，新增或修改 `java.configuration.runtimes` 陣列。此陣列包含物件，每個物件代表一個你希望 VS Code 識別的 JDK 版本。
   - 每個物件通常包括：
     - `name`：Java 版本識別符（例如 `JavaSE-1.8`、`JavaSE-11`、`JavaSE-17`）。
     - `path`：JDK 安裝目錄在你系統中的絕對路徑。
     - `default`（可選）：設為 `true` 可將此 JDK 設為非託管資料夾（沒有建置工具如 Maven 或 Gradle 的專案）的預設 JDK。

   以下是一個配置範例：

   ```json
   {
       "java.configuration.runtimes": [
           {
               "name": "JavaSE-1.8",
               "path": "C:/Program Files/Java/jdk1.8.0_351",
               "default": true
           },
           {
               "name": "JavaSE-11",
               "path": "C:/Program Files/Java/jdk-11.0.15"
           },
           {
               "name": "JavaSE-17",
               "path": "C:/Program Files/Java/jdk-17.0.6"
           }
       ]
   }
   ```

4. **驗證 JDK 路徑**：
   - 確保 `path` 指向你的 JDK 安裝根目錄（例如包含 `java.exe` 或 `java` 的 `bin` 資料夾所在位置）。
   - 在 Windows 上，路徑使用正斜線 (`/`) 或轉義反斜線 (`\\`)。
   - 在 macOS/Linux 上，使用適當的檔案系統路徑（例如 `/usr/lib/jvm/java-17-openjdk`）。

5. **儲存並重新載入**：
   - 儲存 `settings.json` 檔案。
   - 重新啟動 VS Code 或重新載入視窗（`Ctrl + R` 或 `Cmd + R`）以套用變更。

6. **檢查配置**：
   - 開啟命令選擇區（`Ctrl + Shift + P` 或 `Cmd + Shift + P`）並執行命令 `Java: Configure Java Runtime`。
   - 這會開啟一個顯示專案可用 JDK 的檢視畫面。請確認你配置的執行環境出現在「Project JDKs」標籤下。

### 運作原理
- **非託管資料夾**：對於沒有建置工具的專案（例如純 Java 檔案），VS Code 使用 `java.configuration.runtimes` 中指定的 `default` JDK。
- **託管專案（Maven/Gradle）**：對於有建置工具的專案，JDK 版本由建置配置（例如 `pom.xml` 或 `build.gradle`）決定，但 VS Code 仍會識別此處列出的執行環境以確保相容性。
- **語言伺服器**：Java Language Server（Java 擴充功能的一部分）需要 JDK 17+ 才能執行。如有需要，你可以透過 `java.jdt.ls.java.home` 單獨指定（例如 `"java.jdt.ls.java.home": "C:/Program Files/Java/jdk-17.0.6"`）。

### 多個 JDK 範例
如果你在 Mac 上透過 Homebrew 安裝了 JDK 8 和 17，你的配置可能如下：

```json
{
    "java.configuration.runtimes": [
        {
            "name": "JavaSE-1.8",
            "path": "/Library/Java/JavaVirtualMachines/jdk1.8.0_351.jdk/Contents/Home",
            "default": true
        },
        {
            "name": "JavaSE-17",
            "path": "/Library/Java/JavaVirtualMachines/jdk-17.0.6.jdk/Contents/Home"
        }
    ]
}
```

### 提示
- 使用正確的 `name` 格式（`JavaSE-<version>`），與 Java 版本匹配（例如 Java 11 對應 `JavaSE-11`）。
- 即使你只有一個 JDK，仍可將其列出以確保 VS Code 明確使用它。
- 要尋找你的 JDK 路徑，可在終端機中執行 `java -version`，並檢查安裝目錄（例如在 Windows 上使用 `where java`，或在 Unix-like 系統上使用 `which java`，然後追溯至 JDK 根目錄）。

此設定讓你能靈活地在 VS Code 中無縫使用多個 Java 版本！如果你需要協助尋找 JDK 路徑或疑難排解，請告訴我。