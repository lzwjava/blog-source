---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 使用 jstack 診斷 Java 程式停滯問題
translated: true
type: note
---

### 使用 jstack 診斷 Java 應用程式停頓或卡住問題

jstack 是 JDK 內建的命令列工具，可為運作中的 Java 虛擬機（JVM）生成執行緒傾印。執行緒傾印能捕捉特定時刻所有執行緒的狀態，對於識別停頓原因至關重要，例如死結、無窮迴圈、阻塞的 I/O 或 CPU 密集型操作。它在 Linux/Unix 系統或跨平台環境中尤其有用。

#### 使用 jstack 的步驟：
1. **識別 Java 程序 ID (PID)：**
   - 執行 `jps`（同樣是 JDK 的一部分）以列出所有 Java 程序：  
     ```
     jps -l
     ```
     這會輸出類似 `12345 MyApp.jar` 的內容。請記下 PID（例如 12345）。

   - 或者，在 Linux/macOS 上使用作業系統命令如 `ps aux | grep java`。

2. **生成執行緒傾印：**
   - 執行 jstack 並將 PID 作為參數，將傾印輸出至檔案：  
     ```
     jstack <PID> > thread-dump.txt
     ```
     - 將 `<PID>` 替換為你的程序 ID。
     - 如需更詳細的傾印（包含鎖定資訊），請使用 `jstack -l <PID> > thread-dump.txt`。
     - 如果 JVM 對信號無回應，請使用 `jhsdb jstack --pid <PID>`（適用於 JDK 8 及以上版本）。

3. **擷取多個傾印以供分析：**
   - 停頓問題通常需要隨時間進行比較。請以 10-30 秒的間隔擷取 3-5 個傾印：  
     ```
     jstack <PID> > dump1.txt
     sleep 10
     jstack <PID> > dump2.txt
     sleep 10
     jstack <PID> > dump3.txt
     ```
     - 如有需要，可使用腳本循環執行（例如使用 bash 腳本）。

4. **分析傾印檔案：**
   - 在編輯器或 IDE 中開啟文字檔案。
   - 尋找：
     - **執行緒狀態：** 專注於處於 `RUNNABLE`（活動中）、`BLOCKED`（等待鎖定，可能死結）、`WAITING`（空閒等待）或 `TIMED_WAITING` 狀態的執行緒。
     - **死結：** 搜尋 "deadlock" 或使用如 `jstack -l` 等會標記死結的工具。
     - **堆疊追蹤：** 識別重複模式或卡在特定方法中的情況（例如在迴圈中的無窮迴圈）。
     - **原生框架：** 如果執行緒卡在原生存碼中，可能表示 JNI 問題或作業系統層級的阻塞。
   - 用於深入分析的工具：VisualVM、Eclipse MAT 或線上解析器如 fastThread.io。例如，在 VisualVM 中，於 "Thread" 標籤下載入傾印檔案以視覺化鎖定和狀態。

如果 JVM 沒有回應（例如在 Unix 上使用 `kill -3 <PID>` 沒有輸出），停頓可能發生在作業系統層級——請考慮透過 `gcore <PID>` 進行完整核心傾印。

### 使用 ProcDump 診斷程序停頓或卡住問題

ProcDump 是適用於 Windows 的免費 Sysinternals 工具，可建立程序的記憶體或 CPU 傾印。它非常適合擷取任何應用程式（包括 Java）停頓時的快照，尤其是在程序無回應時。使用它來擷取完整記憶體傾印，並使用 WinDbg 或 Visual Studio 等工具進行分析。

#### 使用 ProcDump 的步驟：
1. **下載與設定：**
   - 從 Microsoft Sysinternals 網站取得 ProcDump（procdump.exe）。
   - 以管理員身分執行命令提示字元。
   - 導航至包含 procdump.exe 的資料夾。

2. **識別程序：**
   - 使用工作管理員或 `tasklist | findstr <process-name>` 來取得 PID 或映像名稱（例如 `java.exe`）。

3. **擷取停頓傾印：**
   - 用於立即擷取完整記憶體傾印（對於卡住的程序非常有用）：  
     ```
     procdump -ma <process-name-or-PID>
     ```
     - `-ma`：完整記憶體傾印（包含所有執行緒和堆積）。
     - 範例：`procdump -ma java.exe` 或 `procdump -ma 12345`。

   - 用於自動停頓偵測（在無回應時觸發）：  
     ```
     procdump -h <process-name-or-PID> -o
     ```
     - `-h`：監控停頓情況（程序對視窗訊息無回應超過 5 秒；對於沒有視窗的服務，請使用 CPU 閾值如 `-h 80` 代表 80% CPU）。
     - `-o`：覆蓋現有的傾印檔案。
     - 對於服務：結合 `-e` 用於例外情況或監控 CPU：`procdump -c 80 -h <service-exe>`。

   - 擷取多個傾印：加入 `-n 3` 以在間隔時間內擷取 3 個傾印（例如 `-t 10` 代表 10 秒延遲）：  
     ```
     procdump -ma -n 3 -t 10 <PID>
     ```

4. **分析傾印檔案：**
   - 傾印檔案會以 `.dmp` 格式儲存在目前目錄中。
   - 在 WinDbg（Microsoft 免費提供）或 Visual Studio Debugger 中開啟。
   - WinDbg 中的關鍵命令：
     - `!threads`：列出執行緒及其狀態（尋找阻塞/等待中的執行緒）。
     - `~<thread-id>s`：切換到特定執行緒並使用 `k` 查看堆疊追蹤。
     - `!analyze -v`：自動分析停頓/死結。
   - 對於 Java 特定分析，請將傾印載入 Eclipse MAT 或對堆積傾印使用 `jhat`（如果使用 `-mh` 旗標擷取）。

ProcDump 對於非互動式程序（如服務）效果良好；如果停頓是 CPU 密集型，請使用 `-c` 在高 CPU 使用率時觸發。

### 兩種工具的通用提示
- **安全性：** 傾印檔案可能很大（完整記憶體傾印可達 GB 級）；請確保有足夠的磁碟空間。
- **結合使用工具：** 對於 Windows 上的 Java，先使用 jstack（較輕量），然後使用 ProcDump 進行更深入的作業系統層級分析。
- **預防措施：** 啟用 JVM 旗標如 `-XX:+PrintGCDetails` 用於記錄，或使用如 JFR 等代理程式進行性能分析。
- 如果傾印沒有顯示明確問題，請使用如 `top` 或 Performance Monitor 等工具檢查系統資源（CPU、記憶體、I/O）。

[Oracle Java 疑難排解指南](https://docs.oracle.com/en/java/javase/17/troubleshoot/troubleshoot-process-hangs-and-loops.html)  
[使用 ProcDump 擷取停頓傾印](https://www.poppastring.com/blog/taking-a-hang-dump-or-crash-dump-with-procdump)  
[Java 執行緒傾印分析](https://www.baeldung.com/java-analyze-thread-dumps)  
[ProcDump 用於停頓的用法](https://learn.microsoft.com/en-us/sysinternals/downloads/procdump)