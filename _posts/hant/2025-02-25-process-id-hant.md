---
audio: false
generated: false
lang: hant
layout: post
title: 正在運行的伺服器的流程識別碼 (PID)
translated: true
---

由於你正在使用 WebSphere Liberty Profile (WLP) 版本 24.0.0.9，並且需要找到正在運行的伺服器的進程 ID (PID)，但你指出預期的 `.pid` 文件位於 `<WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid` 並不存在，這裡有幾種替代方法可以定位 PID。

標準方法依賴於 Liberty 在伺服器啟動後將 PID 存儲在 `.pid` 文件中。然而，如果這個文件丟失—可能是由於配置問題、啟動失敗或不同的安裝設置—你仍然可以使用系統工具來識別 PID，假設伺服器正在運行。以下是在 Unix 類似系統（例如 Linux）上找到 PID 的可靠步驟。如果你使用的是 Windows，請告訴我，我可以相應地調整指示。

### 步驟 1：確認伺服器正在運行
在搜索 PID 之前，請確保 Liberty 伺服器正在運行。你可以：
- **檢查日誌**：在 `<WLP_HOME>/usr/servers/<serverName>/logs/console.log` 或 `messages.log` 中查找啟動消息，例如 "Server <serverName> started."
- **訪問伺服器**：如果它托管一個 Web 應用程序，嘗試通過瀏覽器訪問它（例如 `http://localhost:<port>`）。

如果伺服器沒有運行，就沒有 PID 可以找到，所以這一步是至關重要的。

### 步驟 2：使用系統命令來找到 PID
由於 `.pid` 文件不可用，你可以使用命令行工具來定位與 Liberty 伺服器相關聯的 Java 進程。Liberty 作為一個 Java 進程運行，因此列出 Java 或網絡進程的工具可以幫助你。以下是兩種有效的方法：

#### 方法 1：使用 `ps` 列出 Java 進程
`ps` 命令顯示正在運行的進程。要過濾 Java 進程，包括 Liberty 伺服器，請運行：
```bash
ps -ef | grep java
```
這將列出命令行中包含 "java" 的所有進程。輸出可能如下：
```
user  12345  1  0  10:00 ?  00:00:00 /path/to/java -jar /path/to/liberty/wlp/bin/tools/ws-server.jar <serverName>
```
- 第二列（例如 `12345`）是 PID。
- 查找提到 "liberty"、"wlp" 或你的 `<serverName>`（例如 `defaultServer`）的行來識別正確的進程。

如果你知道伺服器名稱，可以進一步縮小範圍：
```bash
ps -ef | grep <serverName>
```

#### 方法 2：使用 `jps`（專門的 Java 工具）
如果你安裝了 Java Development Kit (JDK)，`jps` 命令是列出 Java 進程的更簡單的方法。運行：
```bash
jps -l
```
輸出可能如下：
```
12345 com.ibm.ws.kernel.boot.Launcher
```
- 第一列（例如 `12345`）是 PID。
- 查找與 Liberty 相關的類名，例如 `com.ibm.ws.kernel.boot.Launcher`，這通常與 Liberty 的啟動相關聯。

這種方法通常比 `ps` 更乾淨，因為它只顯示 Java 進程。

### 步驟 3：可選 - 使用端口號（如果已知）
如果你知道 Liberty 伺服器正在監聽的端口號（例如從 `server.xml` 或日誌中），你可以使用 `netstat` 來找到 PID：
```bash
netstat -anp | grep <port_number>
```
輸出可能包括：
```
tcp  0  0  0.0.0.0:<port_number>  0.0.0.0:*  LISTEN  12345/java
```
- PID（例如 `12345`）出現在端口詳細信息後。

### 建議
- **首選方法**：如果有 JDK，使用 `jps -l`，因為它針對 Java 進程並且可能清晰地識別 Liberty 伺服器。
- **備用方法**：如果 `jps` 不是選項，使用 `ps -ef | grep java`，並通過檢查命令詳細信息來手動識別 Liberty 進程。

### 疑難排解提示
如果兩個命令都找不到 Liberty 進程：
- 重新檢查伺服器是否正在運行（步驟 1）。
- 驗證你的 `<WLP_HOME>` 和 `<serverName>` 路徑；進程可能引用意外的目錄。
- 使用 `server start <serverName>` 重新啟動伺服器，檢查 `.pid` 文件是否出現，或者查看啟動日誌以獲取為什麼丟失的線索。

使用這些步驟，你應該能夠在缺少 `.pid` 文件的情況下找到運行的 Liberty 24.0.0.9 伺服器的 PID。如果需要進一步的幫助，請告訴我！