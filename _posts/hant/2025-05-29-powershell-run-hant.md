---
audio: false
generated: true
lang: hant
layout: post
title: PowerShell：在當前終端中執行命令
translated: true
type: note
---

若要在目前的 PowerShell 終端機中直接執行 `mvn` 或 WebSphere 伺服器指令，而無需開啟新的命令提示字元視窗，您可以使用呼叫運算子 (`&`) 或直接呼叫指令。這種方法能確保指令在現有的 PowerShell 工作階段中執行，讓輸出和錯誤訊息都顯示在同一個終端機內。

具體操作方式如下：

1. **直接執行指令**：
   若指令（例如 `mvn`）已存在於系統 PATH 或當前目錄中，只需像在終端機中一樣輸入指令：

   ```powershell
   mvn clean install
   ```

   這會直接在 PowerShell 工作階段中執行 `mvn`，輸出內容將保留在當前終端機。

2. **使用呼叫運算子 (`&`)**：
   若需指定執行檔路徑或指令儲存於變數中，請使用呼叫運算子：

   ```powershell
   & "C:\path\to\maven\bin\mvn.cmd" clean install
   ```

   對於 WebSphere 伺服器指令（如 `wsadmin` 或 `startServer`），可這樣操作：

   ```powershell
   & "C:\path\to\WebSphere\AppServer\bin\startServer.bat" server1
   ```

   `&` 運算子能確保指令在當前 PowerShell 工作階段中執行。

3. **處理含空格或變數的指令**：
   若指令路徑包含空格或儲存於變數中，請使用 `&` 並以引號包覆路徑：

   ```powershell
   $mvnPath = "C:\Program Files\Apache Maven\bin\mvn.cmd"
   & $mvnPath clean install
   ```

4. **設定環境變數（如需要）**：
   某些指令（如 `mvn` 或 WebSphere 指令碼）可能需要環境變數（例如 `JAVA_HOME` 或 `WAS_HOME`），請在執行指令前於指令碼中設定：

   ```powershell
   $env:JAVA_HOME = "C:\path\to\jdk"
   $env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
   mvn --version
   ```

   針對 WebSphere：

   ```powershell
   $env:WAS_HOME = "C:\path\to\WebSphere\AppServer"
   & "$env:WAS_HOME\bin\startServer.bat" server1
   ```

5. **擷取輸出或處理錯誤**：
   要擷取指令輸出或處理錯誤，請使用 PowerShell 的標準機制：

   ```powershell
   try {
       $output = & mvn clean install 2>&1
       Write-Output $output
   } catch {
       Write-Error "Failed to run Maven: $_"
   }
   ```

6. **避免使用 `Start-Process`**：
   與 `Start-Process`（會在新視窗中啟動程序）不同，上述方法能維持在當前工作階段中執行。請避免這樣使用 `Start-Process`：

   ```powershell
   # 這會開啟新的命令提示字元視窗
   Start-Process -FilePath "mvn" -ArgumentList "clean install"
   ```

   請改用直接執行或 `&` 運算子。

### 範例指令碼
以下是在當前終端機中執行 `mvn` 與 WebSphere 指令的 PowerShell 範例指令碼：

```powershell
# 如需要則設定環境變數
$env:JAVA_HOME = "C:\Program Files\Java\jdk-11"
$env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
$env:WAS_HOME = "C:\IBM\WebSphere\AppServer"

# 執行 Maven 指令
Write-Output "Running Maven..."
& mvn clean install

# 執行 WebSphere 伺服器指令
Write-Output "Starting WebSphere server..."
& "$env:WAS_HOME\bin\startServer.bat" server1
```

### 注意事項
- 請確保命令列工具（`mvn`、`startServer.bat` 等）已加入 PATH 或提供完整執行檔路徑
- 若指令需特定工作目錄，請在執行前使用 `Set-Location`（或 `cd`）：

   ```powershell
   Set-Location "C:\path\to\project"
   & mvn clean install
   ```

- 對於依賴 `.bat` 或 `.cmd` 檔案的指令（常見於 WebSphere），`&` 運算子能正常運作，但請確保指令碼在 PowerShell 而非 `cmd.exe` 中執行
- 若遇到環境變數或 PATH 問題，可用 `Get-ChildItem Env:` 進行驗證

此方法能讓所有操作集中在當前 PowerShell 終端機，避免開啟新視窗並維持流暢的工作流程。若您遇到特定指令或設定問題，請提供詳細資訊以便進一步定制解決方案。