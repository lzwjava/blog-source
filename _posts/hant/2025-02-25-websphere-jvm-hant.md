---
audio: true
generated: true
lang: hant
layout: post
title: JVM 選項在 WebSphere Liberty Server
translated: true
---

檢查 WebSphere Liberty Profile (WLP) 伺服器的 `jvm.options` 文件中設置的 JVM 選項，可以使用 Java Development Kit (JDK) 提供的 `jinfo` 命令。這種方法可以有效地驗證應用於運行伺服器的選項。以下是完成此操作的分步指南：

### 檢查 JVM 選項的步驟

1. **了解上下文**
   伺服器目錄中的 `jvm.options` 文件（通常位於 `<WLP_HOME>/usr/servers/<serverName>/jvm.options`）用於指定 JVM 參數，例如堆大小（例如 `-Xmx`）、垃圾收集設置（例如 `-XX:+UseG1GC`）或系統屬性（例如 `-Dmy.property=value`），這些參數在 Liberty 伺服器啟動時應用。

2. **啟動伺服器**
   使用以下命令在後台啟動您的 Liberty 伺服器：
   ```
   <WLP_HOME>/bin/server start <serverName>
   ```
   將 `<WLP_HOME>` 替換為 WebSphere Liberty 安裝的路徑，將 `<serverName>` 替換為您的伺服器名稱。此命令以後台進程啟動伺服器。

3. **定位進程 ID (PID)**
   啟動伺服器後，您需要運行 Java 進程的進程 ID。Liberty 方便地將其存儲在以下位置的 `.pid` 文件中：
   ```
   <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
   ```
   打開此文件（例如，在類 Unix 系統上使用 `cat` 或文本編輯器）以檢索 PID，這是一個表示伺服器進程的數值。

4. **驗證 JVM 旗標**
   使用 `jinfo` 命令檢查應用於運行伺服器的 JVM 旗標。運行：
   ```
   jinfo -flags <pid>
   ```
   將 `<pid>` 替換為從 `.pid` 文件中獲取的進程 ID。此命令輸出傳遞給 JVM 的命令行旗標，例如 `-Xmx1024m` 或 `-XX:+PrintGCDetails`。查看輸出以確認您在 `jvm.options` 中設置的旗標是否存在。

5. **驗證系統屬性**
   如果您的 `jvm.options` 文件包含系統屬性（例如 `-Dmy.property=value`），請使用以下命令單獨檢查它們：
   ```
   jinfo -sysprops <pid>
   ```
   這將顯示為 JVM 設置的所有系統屬性。在輸出中搜索您定義的特定屬性，以確保它們已正確應用。

### 前提條件
- **安裝 JDK**：`jinfo` 命令是 JDK 的一部分，而不是 JRE。請確保已安裝 JDK，並且 `jinfo` 可執行文件在系統的 PATH 中。
- **權限**：以啟動伺服器的相同用戶身份運行 `jinfo`，或者具有足夠的權限附加到進程。

### 替代方法
如果 `jinfo` 無法使用或您偏好其他方法，以下是兩種附加選項：

- **使用 `server dump`**：
  1. 使用 `server start <serverName>` 啟動伺服器。
  2. 使用以下命令生成伺服器轉傳：
     ```
     <WLP_HOME>/bin/server dump <serverName>
     ```
  3. 在 `<WLP_HOME>/usr/servers/<serverName>/` 中定位生成的 `.zip` 文件，將其提取並打開 `javacore.<timestamp>.txt` 文件。
  4. 搜索 "CMDLINE" 部分以查看完整的 Java 命令行，包括 JVM 旗標，以及 "System Properties" 部分以查看系統屬性。

- **追蹤啟動腳本**（類 Unix 系統）：
  1. 使用啟用追蹤的伺服器腳本運行：
     ```
     sh -x <WLP_HOME>/bin/server start <serverName>
     ```
  2. 審查輸出以查找腳本執行的 Java 命令，其中包括 `jvm.options` 中的所有選項。

### 注意事項
- **伺服器未運行**：如果伺服器因無效選項而無法啟動，請使用 `server run <serverName>` 在前台運行它，並在控制台輸出中檢查錯誤，或者使用腳本追蹤方法查看命令。
- **日誌文件**：`<WLP_HOME>/usr/servers/<serverName>/logs/` 中的 `console.log` 文件可能包含一些啟動信息，但除非啟用了詳細日誌記錄（例如 `-XX:+PrintFlagsFinal`），否則它不會可靠地列出所有 JVM 選項。

### 結論
`jinfo` 方法是驗證 `jvm.options` 中設置的 JVM 選項的最直接方法。通過遵循上述步驟，您可以確認 JVM 旗標和系統屬性已按預期應用。

---

`jinfo` 命令報告說無法附加到進程。

此外，使用轉傳命令後無法在預期位置（`<WLP_HOME>/usr/servers/<serverName>/`）中找到 `javacore.<timestamp>.txt` 文件。

WebSphere Liberty 伺服器的版本是 24.0.0.9。

---

### 解決 WebSphere Liberty 24.0.0.9 中檢查 JVM 選項的問題

您在 WebSphere Liberty Profile (WLP) 伺服器版本 24.0.0.9 中使用 `jinfo` 命令檢查 JVM 選項時遇到問題，錯誤報告說 "無法附加到進程"。此外，在生成伺服器轉傳後，您無法在預期位置（`<WLP_HOME>/usr/servers/<serverName>/`）中找到 `javacore.<timestamp>.txt` 文件。以下是詳細指南，幫助您排查並解決這些問題，確保您可以驗證 `jvm.options` 文件中設置的 JVM 選項。

---

### 了解問題

- **`jinfo` 失敗**："無法附加到進程" 錯誤通常意味著 `jinfo` 無法連接到運行的 Java 虛擬機（JVM）。這通常是由於權限問題（例如，以不同於啟動伺服器的用戶身份運行命令）或對 JVM 進程的限制。
- **缺少 `javacore.<timestamp>.txt`**：伺服器轉傳過程應該生成一個包含診斷文件（包括 `javacore.<timestamp>.txt`）的 `.zip` 文件，但其缺失表明轉傳失敗、文件在意外位置或預期內容未生成。

由於您使用的是 WebSphere Liberty 24.0.0.9，並且根據典型的文件路徑，我們將根據 Unix 類系統進行解決方案。

---

### 分步解決方案

以下是多種方法來檢索您的 JVM 選項，從最簡單的 `jinfo` 替代方案開始，並解決伺服器轉傳問題。

#### 1. 驗證伺服器正在運行
在繼續之前，請確保您的 Liberty 伺服器正在運行：

- **命令**：
  ```bash
  <WLP_HOME>/bin/server status <serverName>
  ```
- **預期輸出**：
  如果正在運行，您將看到類似於 "伺服器 <serverName> 正在運行，進程 ID 為 <pid>" 的消息。如果沒有，請啟動它：
  ```bash
  <WLP_HOME>/bin/server start <serverName>
  ```

- **定位 PID**：
  使用以下命令在 `<WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid` 中找到進程 ID：
  ```bash
  cat <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
  ```
  記下此 PID 以供後續步驟使用。

#### 2. 使用 `jps -v` 作為 `jinfo` 的替代方案
`jps` 命令（JDK 的一部分）列出 Java 進程及其選項，通常可以避免 `jinfo` 遇到的附加問題。

- **命令**：
  ```bash
  jps -v
  ```
- **輸出**：
  Java 進程列表，例如：
  ```
  12345 Liberty -Xmx1024m -XX:+UseG1GC -Dmy.property=value
  ```
- **操作**：
  通過匹配 `.pid` 文件中的 PID 或在命令行中查找 "Liberty" 或您的 `<serverName>` 來識別您的 Liberty 伺服器進程。列出的選項（例如 `-Xmx1024m`，`-Dmy.property=value`）包括來自 `jvm.options` 的選項。

- **權限檢查**：
  如果 `jps -v` 失敗或顯示無輸出，請以啟動伺服器的相同用戶身份運行它（例如 `sudo -u <serverUser> jps -v`）或使用 `sudo`：
  ```bash
  sudo jps -v
  ```

#### 3. 使用 `jcmd` 获取詳細 JVM 信息
如果 `jps -v` 不夠，`jcmd`（另一個 JDK 工具）可以在不受 `jinfo` 附加限制的情況下查詢運行的 JVM。

- **命令**：
  - 針對 JVM 選項：
    ```bash
    jcmd <pid> VM.command_line
    ```
    輸出：完整命令行，例如 `java -Xmx1024m -XX:+UseG1GC -Dmy.property=value ...`
  - 針對系統屬性：
    ```bash
    jcmd <pid> VM.system_properties
    ```
    輸出：屬性列表，例如 `my.property=value`。

- **操作**：
  將 `<pid>` 替換為您的伺服器的 PID。請確保您以適當的權限運行這些命令（例如，如果需要，使用 `sudo jcmd <pid> ...`）。

#### 4. 生成並檢查 Javacore 文件
由於伺服器轉傳未生成預期的 `javacore.<timestamp>.txt`，請嘗試生成獨立的 javacore 文件：

- **命令**：
  ```bash
  <WLP_HOME>/bin/server javadump <serverName>
  ```
- **預期輸出**：
  顯示 javacore 文件位置的消息，通常是 `<WLP_HOME>/usr/servers/<serverName>/javacore.<timestamp>.txt`。

- **操作**：
  - 檢查目錄：
    ```bash
    ls <WLP_HOME>/usr/servers/<serverName>/javacore.*.txt
    ```
  - 打開文件並搜索：
    - **CMDLINE**：列出 JVM 選項（例如 `-Xmx1024m`）。
    - **系統屬性**：列出 `-D` 屬性。

- **故障排除**：
  如果沒有文件出現，請檢查伺服器的 `console.log` 或 `messages.log`，位於 `<WLP_HOME>/usr/servers/<serverName>/logs/` 中，以查找命令執行過程中的錯誤。

#### 5. 重新檢查伺服器轉傳方法
讓我們確保完整的伺服器轉傳正確運行：

- **命令**：
  ```bash
  <WLP_HOME>/bin/server dump <serverName>
  ```
- **預期輸出**：
  在 `<WLP_HOME>/usr/servers/<serverName>/` 中生成的 `.zip` 文件，例如 `<serverName>.dump-<timestamp>.zip`。

- **操作**：
  - 驗證文件是否存在：
    ```bash
    ls <WLP_HOME>/usr/servers/<serverName>/*.zip
    ```
  - 提取它：
    ```bash
    unzip <serverName>.dump-<timestamp>.zip -d temp_dir
    ```
  - 搜索 `javacore.<timestamp>.txt`：
    ```bash
    find temp_dir -name "javacore.*.txt"
    ```
  - 打開文件並檢查 "CMDLINE" 和 "System Properties" 部分。

- **故障排除**：
  - 檢查命令的控制台輸出以查找錯誤。
  - 確保伺服器在轉傳期間運行（儘管 `server dump` 可以在停止的伺服器上運行，但 javacore 需要運行的 JVM）。
  - 如果 `.zip` 文件丟失，請檢查 `<WLP_HOME>/usr/servers/<serverName>/logs/` 中的日誌以獲取線索。

#### 6. 啟用詳細 JVM 輸出（最後手段）
如果所有方法都失敗，請修改 `jvm.options` 以記錄所有 JVM 旗標：

- **編輯 `<WLP_HOME>/usr/servers/<serverName>/jvm.options`**：
  添加：
  ```
  -XX:+PrintFlagsFinal
  ```
- **重新啟動伺服器**：
  ```bash
  <WLP_HOME>/bin/server stop <serverName>
  <WLP_HOME>/bin/server start <serverName>
  ```
- **檢查日誌**：
  打開 `<WLP_HOME>/usr/servers/<serverName>/logs/console.log` 並搜索 JVM 旗標表，例如：
  ```
  [uintx] MaxHeapSize = 1073741824 {product}
  ```

---

### 附加說明

- **權限**：
  `jinfo` 失敗表明權限不匹配。始終以啟動伺服器的相同用戶身份（例如，使用 `sudo -u <serverUser>` 或以該用戶身份登錄）運行所有命令。
- **WebSphere Liberty 24.0.0.9**：
  轉傳行為應該與文檔過程一致（`.zip` 在 `<WLP_HOME>/usr/servers/<serverName>/` 中包含 `javacore.<timestamp>.txt`）。如果不同，請檢查 IBM 的文檔以獲取版本特定的更改，儘管 `server javadump` 方法仍然可靠。
- **JDK 要求**：
  確保已安裝 JDK（而不僅僅是 JRE），因為 `jps`、`jcmd` 和 `jinfo` 是 JDK 工具。

---

### 推薦方法

1. **首先嘗試 `jps -v`**：它快速且可能避免附加問題。
2. **回退到 `jcmd`**：提供詳細輸出，如果 `jps` 不夠。
3. **使用 `server javadump`**：直接生成 javacore，繞過完整轉傳的複雜性。
4. **調試轉傳**：重新運行 `server dump` 並驗證 `.zip` 文件的內容（如果需要）。

通過遵循這些步驟，您應該能夠成功檢索 JVM 選項並解決 `jinfo` 和缺失 javacore 文件的問題。如果遇到具體錯誤，請告訴我！