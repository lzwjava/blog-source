---
audio: true
lang: hant
layout: post
title: JVM 選項在 WebSphere Liberty Server
translated: true
---

要檢查 WebSphere Liberty Profile (WLP) 伺服器的 `jvm.options` 文件中設定的 JVM 選項，可以使用 Java Development Kit (JDK) 提供的 `jinfo` 命令。這種方法可以有效地驗證應用於運行中的伺服器的選項。以下是完成此操作的分步指南：

### 檢查 JVM 選項的步驟

1. **了解上下文**
   伺服器目錄中的 `jvm.options` 文件（通常位於 `<WLP_HOME>/usr/servers/<serverName>/jvm.options`）用於指定 JVM 參數，例如堆大小（例如 `-Xmx`）、垃圾回收設置（例如 `-XX:+UseG1GC`）或系統屬性（例如 `-Dmy.property=value`），這些參數在 Liberty 伺服器啟動時應用。

2. **啟動伺服器**
   使用以下命令在後台啟動您的 Liberty 伺服器：
   ```
   <WLP_HOME>/bin/server start <serverName>
   ```
   將 `<WLP_HOME>` 替換為 WebSphere Liberty 安裝的路徑，將 `<serverName>` 替換為您的伺服器名稱。此命令以後台進程啟動伺服器。

3. **定位進程 ID (PID)**
   啟動伺服器後，您需要運行 Java 進程的進程 ID。Liberty 方便地將其存儲在 `.pid` 文件中，位於：
   ```
   <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
   ```
   打開此文件（例如在 Unix 類系統上使用 `cat` 或文本編輯器）以檢索 PID，這是一個表示伺服器進程的數值。

4. **驗證 JVM 旗標**
   使用 `jinfo` 命令檢查應用於運行伺服器的 JVM 旗標。運行：
   ```
   jinfo -flags <pid>
   ```
   將 `<pid>` 替換為從 `.pid` 文件中獲取的進程 ID。此命令輸出傳遞給 JVM 的命令行旗標，例如 `-Xmx1024m` 或 `-XX:+PrintGCDetails`。查看輸出以確認您在 `jvm.options` 中設置的旗標是否存在。

5. **驗證系統屬性**
   如果您的 `jvm.options` 文件包括系統屬性（例如 `-Dmy.property=value`），請單獨檢查：
   ```
   jinfo -sysprops <pid>
   ```
   這將顯示為 JVM 設置的所有系統屬性。在輸出中搜索您定義的特定屬性，以確保它們已正確應用。

### 預先條件
- **已安裝 JDK**：`jinfo` 命令是 JDK 的一部分，而不是 JRE。請確保已安裝 JDK，並且 `jinfo` 可執行文件在系統的 PATH 中。
- **權限**：使用與啟動伺服器相同的用戶運行 `jinfo`，或者具有足夠的權限來附加到進程。

### 替代方法
如果 `jinfo` 無法使用或您更喜歡另一種方法，這裡有兩種附加選項：

- **使用 `server dump`**：
  1. 使用 `server start <serverName>` 啟動伺服器。
  2. 使用以下命令生成伺服器轉储：
     ```
     <WLP_HOME>/bin/server dump <serverName>
     ```
  3. 在 `<WLP_HOME>/usr/servers/<serverName>/` 中定位生成的 `.zip` 文件，將其提取並打開 `javacore.<timestamp>.txt` 文件。
  4. 搜索 "CMDLINE" 部分以查看完整的 Java 命令行，包括 JVM 旗標，以及 "System Properties" 部分以查看系統屬性。

- **追蹤啟動腳本**（Unix 類系統）：
  1. 使用啟用追蹤的伺服器腳本運行：
     ```
     sh -x <WLP_HOME>/bin/server start <serverName>
     ```
  2. 查看輸出以查找腳本執行的 Java 命令，其中包括 `jvm.options` 中的所有選項。

### 注意事項
- **伺服器未運行**：如果伺服器因無效選項而無法啟動，請使用 `server run <serverName>` 在前台運行它，並檢查控制台輸出以查找錯誤，或者使用腳本追蹤方法以查看命令。
- **日誌文件**：`<WLP_HOME>/usr/servers/<serverName>/logs/` 中的 `console.log` 文件可能包含一些啟動信息，但除非啟用了詳細日誌記錄（例如 `-XX:+PrintFlagsFinal`），否則它不會可靠地列出所有 JVM 選項。

### 結論
`jinfo` 方法是驗證 `jvm.options` 中為運行的 Liberty 伺服器設置的 JVM 選項的最直接方法。通過遵循上述步驟，您可以確認 JVM 旗標和系統屬性已按預期應用。