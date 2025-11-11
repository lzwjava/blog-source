---
audio: false
generated: true
lang: hant
layout: post
title: Visual Studio Code 中的 Java 語言伺服器
translated: true
type: note
---

嘿！Visual Studio Code（VSCode）中的 `java.jdt.ls.java.home` 設定是一個特定配置選項，由 Java Language Server（隸屬於「Language Support for Java(TM) by Red Hat」擴充功能，包含在 Java Extension Pack 中）使用。讓我們來詳細解析：

---

### 它的含義
- **JDT**：代表「Java Development Tools」，最初是 Eclipse IDE 的一部分。VSCode 中的 Java Language Server 基於 Eclipse 的 JDT，提供代碼補全、調試和編譯等功能。
- **LS**：代表「Language Server」，是一個後台進程，為 VSCode 的 Java 支援（例如 IntelliSense、錯誤檢查）提供動力。
- **`java.jdt.ls.java.home`**：此設定告訴 Java Language Server 具體使用哪個 Java Development Kit（JDK）來進行其操作。它與更廣泛的 `java.home` 設定不同，儘管它們相關。

簡而言之，`java.jdt.ls.java.home` 指定了 Java Language Server 使用的 JDK 路徑，用於：
- 解析你的 Java 代碼。
- 提供語言功能（例如自動補全、跳轉到定義）。
- 在某些情況下編譯和運行代碼（儘管編譯通常依賴於其他設定或構建工具）。

---

### 與 `java.home` 的區別
- **`java.home`**：一個通用的 VSCode 設定，指向所有 Java 相關擴充功能和任務的 JDK。除非被更特定的設定覆蓋，否則會使用此設定。
- **`java.jdt.ls.java.home`**：一個更特定的設定，僅針對 Java Language Server 覆蓋 `java.home`。如果未設定此項，Language Server 將回退到使用 `java.home`。

因此，如果你設定了 `java.jdt.ls.java.home`，它將優先於 Language Server 的操作，讓你可以為語言功能使用不同的 JDK，而不是用於運行或調試任務。

---

### 如何配置
由於你使用的是 Windows 和 VSCode 1.96.4 以及 Java Extension Pack，以下是設定方法：

1. **開啟設定：**
   - 按下 `Ctrl + ,` 開啟設定 UI，或使用 `Ctrl + Shift + P` 並輸入 **「Open Settings (JSON)」** 來編輯 `settings.json`。

2. **設定路徑：**
   - **在設定 UI 中：**
     - 搜尋 **「java.jdt.ls.java.home」**。
     - 輸入你的 JDK 完整路徑（例如 `C:\Program Files\Java\jdk-17.0.1`）。
   - **在 settings.json 中：**
     - 添加這一行（替換為你的 JDK 路徑）：
       ```json
       "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
       ```
     - 示例 `settings.json`：
       ```json
       {
           "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
       }
       ```

3. **驗證 JDK 路徑：**
   - 確保路徑指向一個包含 `bin` 目錄的 JDK 資料夾，其中包含 `javac.exe` 和 `java.exe`。

4. **重新載入 VSCode：**
   - 重新載入視窗（`Ctrl + Shift + P` > 「Reload Window」）或重新啟動 VSCode 以應用更改。

---

### 何時使用
你通常會在以下情況設定 `java.jdt.ls.java.home`：
- 你安裝了多個 JDK，並希望 Language Server 使用特定的 JDK（例如 JDK 17），而其他 Java 任務（如運行代碼）可能通過 `java.home` 使用不同的 JDK。
- 你在排查 Language Server 問題（例如它沒有自動選擇正確的 JDK）。
- 你的項目對語言功能有特定的 JDK 版本要求。

如果你不設定它，Language Server 將使用 `java.home` 中的 JDK（或作為最後手段，使用系統的 `JAVA_HOME` 環境變數）。

---

### 實際示例
假設你安裝了 JDK 8 和 JDK 17：
- 設定 `"java.home": "C:\\Program Files\\Java\\jdk1.8.0_291"` 用於一般用途。
- 設定 `"java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"` 以確保 Language Server 使用 JDK 17 來支援現代 Java 語法。

這樣，你可以使用 JDK 8 進行調試/運行，同時獲得對 JDK 17 功能的語言支援。

---

這樣清楚了嗎？如果你想知道這如何適應你的設定，或需要進一步調整幫助，請隨時告訴我！😊