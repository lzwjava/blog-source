---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GraalVM 安裝與使用指南
translated: true
type: note
---

## 什麼是 GraalVM？

GraalVM 是一個開源的高效能運行時環境（JDK 發行版），支援多種程式語言，如 Java、JavaScript、Python 等。它具備先進的 JIT 編譯器，可實現更快的執行速度，並能透過 Native Image 將 Java 應用程式編譯為原生可執行檔，從而減少啟動時間和記憶體佔用。

## 安裝步驟

1. **下載 GraalVM**：
   - 前往 GraalVM 官方下載頁面。
   - 選擇 Community Edition（免費版）或 Oracle GraalVM（具備額外功能）。
   - 根據您的平台（例如 Linux、macOS、Windows）和架構（x64 或 ARM）選擇相應版本。
   - 截至 2025 年，最新穩定版本為 GraalVM for JDK 22 或 23——請查閱官網以獲取最新資訊。

2. **解壓縮並安裝**：
   - 將下載的壓縮檔解壓至目錄，例如在 Linux/macOS 上解壓至 `/opt/graalvm`，或在 Windows 上解壓至 `C:\Program Files\GraalVM`。
   - 無需安裝程式，這是一個可攜式發行版。

3. **設定環境變數**：
   - 將 `JAVA_HOME` 設定為 GraalVM 目錄（例如在 Linux/macOS 上使用 `export JAVA_HOME=/opt/graalvm`）。
   - 將 `bin` 目錄加入 `PATH`（例如 `export PATH=$JAVA_HOME/bin:$PATH`）。
   - 使用 `java -version` 驗證；應顯示 GraalVM 的詳細資訊。

4. **安裝額外元件（可選）**：
   - 使用 `gu`（GraalVM 更新工具）安裝語言運行時或 Native Image：`gu install native-image`（在 Linux 上需要建置工具如 `build-essential`）。

## 建置 Hello World 程式

我們將以 Java 為例，因為它是 GraalVM 的主要語言。建立一個簡單的 "Hello World" 應用程式，編譯並執行它。

### 步驟 1：編寫程式碼
建立一個名為 `HelloWorld.java` 的檔案：

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World from GraalVM!");
    }
}
```

### 步驟 2：編譯
在包含該檔案的目錄中開啟終端機，並執行：
```
javac HelloWorld.java
```
這將產生 `HelloWorld.class`。

### 步驟 3：執行
```
java HelloWorld
```
輸出：
```
Hello, World from GraalVM!
```

### 進階：編譯為原生可執行檔
GraalVM 的 Native Image 功能可讓您建置獨立的二進位檔。

1. 確保已安裝 Native Image：`gu install native-image`。
2. 產生配置（首次執行可能需要此步驟）：
   ```
   native-image --no-fallback -H:+ReportExceptionStackTraces HelloWorld
   ```
   - 這將建立 `HelloWorld`（或在 Windows 上為 `helloworld.exe`），即原生二進位檔。
   - 首次建置時，它會分析應用程式，可能需要幾分鐘時間。

3. 執行原生二進位檔：
   ```
   ./HelloWorld
   ```
   輸出相同，但啟動瞬間完成且記憶體使用量低。

## 使用 GraalVM 的提示
- **切換 JDK**：使用 SDKMAN!（`sdk install java 22.0.2-graal`）方便管理。
- **多語言支援**：使用 GraalVM 的 `node` 執行 Node.js 程式碼，或使用 `python` 執行 Python 程式碼。
- **效能優化**：使用 `-XX:+UnlockExperimentalVMOptions -XX:+UseJVMCICompiler` 啟用 GraalVM 的 JIT。
- **疑難排解**：檢查 `~/.gu/` 中的日誌以解決問題；確保系統已安裝 C 編譯器以使用 Native Image。

更多詳細資訊，請參閱官方文件。

[GraalVM 下載](https://www.graalvm.org/downloads/)  
[GraalVM 使用指南](https://www.graalvm.org/latest/reference-manual/)  
[Native Image 教學](https://www.graalvm.org/latest/reference-manual/native-image/)