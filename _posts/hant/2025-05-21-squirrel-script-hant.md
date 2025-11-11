---
audio: false
generated: true
lang: hant
layout: post
title: SQuirreL 啟動指令碼
translated: true
type: note
---

這個批次腳本用於啟動 SQuirreL SQL Client，這是一個基於 Java 的資料庫管理工具。以下是對腳本的詳細解釋，逐步分析其用途、結構和功能。

---

### **概述**
該腳本設計用於：
1. 配置 Java 環境以運行 SQuirreL SQL Client。
2. 驗證 Java 版本兼容性（需要 Java 1.6 或 1.7）。
3. 檢查軟體更新並在可用時應用。
4. 為 SQuirreL 及其函式庫建置 classpath。
5. 使用適當參數啟動 SQuirreL SQL Client 應用程式。

該腳本為 Windows 編寫（使用 `.bat` 副檔名），並使用 Windows 命令提示字的批次腳本語言。

---

### **逐行解釋**

#### **1. `@echo off`**
- **用途**：停用向控制台顯示指令，使腳本輸出更清晰，僅顯示預期輸出（例如錯誤訊息或特定的 `echo` 語句）。
- **效果**：除非使用 `echo` 明確列印，否則腳本中執行的指令不會顯示。

---

#### **2. `@rem IZPACK_JAVA is filtered in by the IzPack installer when this script is installed`**
- **用途**：註解（`@rem`）表示 `IZPACK_JAVA` 變數由 IzPack 安裝程式在安裝過程中設定。
- **上下文**：IzPack 是用於建立 Java 應用程式安裝程式的工具。它會在腳本中動態設定 `JAVA_HOME` 環境變數，指向安裝過程中使用的 Java 安裝路徑。

#### **3. `set IZPACK_JAVA=%JAVA_HOME`**
- **用途**：將 `JAVA_HOME` 環境變數（由 IzPack 設定）的值賦予 `IZPACK_JAVA` 變數。
- **解釋**：這確保腳本知道 Java 安裝的位置。`JAVA_HOME` 通常指向 Java Development Kit (JDK) 或 Java Runtime Environment (JRE) 的根目錄。

---

#### **4. Java 偵測邏輯**
```bat
@rem We detect the java executable to use according to the following algorithm:
@rem 1. If the one used by the IzPack installer is available then use that; otherwise
@rem 2. Use the java that is in the command path.
if exist "%IZPACK_JAVA%\bin\javaw.exe" (
  set LOCAL_JAVA=%IZPACK_JAVA%\bin\javaw.exe
) else (
  set LOCAL_JAVA=javaw.exe
)
```
- **用途**：決定使用哪個 Java 可執行檔來運行 SQuirreL SQL。
- **邏輯**：
  1. **檢查 IzPack Java**：腳本檢查 `javaw.exe` 是否存在於 `IZPACK_JAVA` 指定的 Java 安裝的 `bin` 目錄中（即 `%IZPACK_JAVA%\bin\javaw.exe`）。
     - `javaw.exe` 是 Windows 特定的 Java 可執行檔，運行 Java 應用程式時不會開啟控制台視窗（與 `java.exe` 不同）。
     - 如果找到，`LOCAL_JAVA` 將設定為 `javaw.exe` 的完整路徑。
  2. **回退到 PATH**：如果在 `IZPACK_JAVA` 目錄中找不到 `javaw.exe`，腳本將回退到使用系統 `PATH` 環境變數中的 `javaw.exe`。
- **為何使用 `javaw.exe`？**：使用 `javaw.exe` 確保應用程式運行時不會有持續存在的命令視窗，提供更整潔的使用者體驗。

#### **5. `echo Using java: %LOCAL_JAVA%`**
- **用途**：將正在使用的 Java 可執行檔路徑列印到控制台，用於除錯或資訊目的。
- **範例輸出**：如果 `LOCAL_JAVA` 是 `C:\Program Files\Java\jre1.6.0_45\bin\javaw.exe`，它將顯示：
  ```
  Using java: C:\Program Files\Java\jre1.6.0_45\bin\javaw.exe
  ```

---

#### **6. 確定 SQuirreL SQL 主目錄**
```bat
set basedir=%~f0
:strip
set removed=%basedir:~-1%
set basedir=%basedir:~0,-1%
if NOT "%removed%"=="\" goto strip
set SQUIRREL_SQL_HOME=%basedir%
```
- **用途**：確定 SQuirreL SQL 的安裝目錄（`SQUIRREL_SQL_HOME`）。
- **解釋**：
  - `%~f0`：這會展開為批次腳本本身的完整路徑（例如 `C:\Program Files\SQuirreL\squirrel-sql.bat`）。
  - **`:strip` 循環**：腳本迭代地從 `basedir` 中移除最後一個字元，直到遇到反斜線（`\`），從而有效地去除腳本檔案名稱以取得目錄路徑。
  - **結果**：`SQUIRREL_SQL_HOME` 設定為包含腳本的目錄（例如 `C:\Program Files\SQuirreL`）。
- **為何採用這種方法？**：這確保腳本能夠動態確定自身的安裝目錄，使其在不同系統間具有可攜性。

---

#### **7. Java 版本檢查**
```bat
"%LOCAL_JAVA%" -cp "%SQUIRREL_SQL_HOME%\lib\versioncheck.jar" JavaVersionChecker 1.6 1.7
if ErrorLevel 1 goto ExitForWrongJavaVersion
```
- **用途**：驗證 Java 版本與 SQuirreL SQL 兼容（需要 Java 1.6 或 1.7）。
- **解釋**：
  - 腳本運行 `JavaVersionChecker` 類別，該類別位於 SQuirreL SQL 的 `lib` 目錄中的 `versioncheck.jar`。
  - **`-cp`**：指定 classpath，指向 `versioncheck.jar`。
  - **參數**：`1.6 1.7` 表示 Java 版本必須是 1.6 或 1.7。
  - **注意**：`versioncheck.jar` 是使用 Java 1.2.2 兼容性編譯的，確保它可以在較舊的 JVM 上運行以執行版本檢查。
  - **錯誤處理**：如果 Java 版本不兼容，`ErrorLevel` 將設定為 1，腳本跳轉到 `:ExitForWrongJavaVersion` 標籤，終止執行。
- **為何進行此檢查？**：SQuirreL SQL 需要特定的 Java 版本才能正常運作，這防止應用程式在不支援的 JVM 上運行。

---

#### **8. 軟體更新檢查**
```bat
if not exist "%SQUIRREL_SQL_HOME%\update\changeList.xml" goto launchsquirrel
SET TMP_CP="%SQUIRREL_SQL_HOME%\update\downloads\core\squirrel-sql.jar"
if not exist %TMP_CP% goto launchsquirrel
dir /b "%SQUIRREL_SQL_HOME%\update\downloads\core\*.*" > %TEMP%\update-lib.tmp
FOR /F %%I IN (%TEMP%\update-lib.tmp) DO CALL "%SQUIRREL_SQL_HOME%\addpath.bat" "%SQUIRREL_SQL_HOME%\update\downloads\core\%%I"
SET UPDATE_CP=%TMP_CP%
SET UPDATE_PARMS=--log-config-file "%SQUIRREL_SQL_HOME%\update-log4j.properties" --squirrel-home "%SQUIRREL_SQL_HOME%" %1 %2 %3 %4 %5 %6 %7 %8 %9
"%LOCAL_JAVA%" -cp %UPDATE_CP% -Dlog4j.defaultInitOverride=true -Dprompt=true net.sourceforge.squirrel_sql.client.update.gui.installer.PreLaunchUpdateApplication %UPDATE_PARAMS%
```
- **用途**：在啟動主應用程式之前檢查並應用軟體更新。
- **解釋**：
  1. **檢查更新檔案**：
     - 腳本檢查 `update` 目錄中是否存在 `changeList.xml`。該檔案由 SQuirreL 的軟體更新功能建立，用於追蹤更新。
     - 如果 `changeList.xml` 不存在，腳本跳過更新過程並跳轉到 `:launchsquirrel`。
     - 它還檢查 `update\downloads\core` 目錄中是否存在更新的 `squirrel-sql.jar`。如果不存在，腳本跳轉到 `:launchsquirrel`。
  2. **建置更新 Classpath**：
     - `dir /b` 指令列出 `update\downloads\core` 目錄中的所有檔案，並將其寫入暫存檔案（`%TEMP%\update-lib.tmp`）。
     - `FOR /F` 循環遍歷 `update-lib.tmp` 中的檔案，並呼叫 `addpath.bat` 將每個檔案附加到儲存在 `TMP_CP` 中的 classpath。
     - `UPDATE_CP` 設定為 classpath，從更新目錄中的 `squirrel-sql.jar` 開始。
  3. **設定更新參數**：
     - `UPDATE_PARMS` 包括：
       - `--log-config-file`：指定更新過程中用於記錄的 Log4j 設定檔。
       - `--squirrel-home`：傳遞 SQuirreL 安裝目錄。
       - `%1 %2 %3 ... %9`：傳遞提供給腳本的任何命令列參數。
  4. **運行更新應用程式**：
     - 腳本啟動 `PreLaunchUpdateApplication`（`squirrel-sql.jar` 中的 Java 類別）以應用更新。
     - **`-Dlog4j.defaultInitOverride=true`**：覆寫預設的 Log4j 設定。
     - **`-Dprompt=true`**：可能在更新過程中啟用互動式提示。
- **為何有此步驟？**：SQuirreL SQL 支援自動更新，此部分確保在啟動主應用程式之前應用任何下載的更新。

---

#### **9. 啟動 SQuirreL SQL**
```bat
:launchsquirrel
@rem build SQuirreL's classpath
set TMP_CP="%SQUIRREL_SQL_HOME%\squirrel-sql.jar"
dir /b "%SQUIRREL_SQL_HOME%\lib\*.*" > %TEMP%\squirrel-lib.tmp
FOR /F %%I IN (%TEMP%\squirrel-lib.tmp) DO CALL "%SQUIRREL_SQL_HOME%\addpath.bat" "%SQUIRREL_SQL_HOME%\lib\%%I"
SET SQUIRREL_CP=%TMP_CP%
echo "SQUIRREL_CP=%SQUIRREL_CP%"
```
- **用途**：為主要的 SQuirreL SQL 應用程式建置 classpath 並準備啟動。
- **解釋**：
  1. **初始化 Classpath**：
     - `TMP_CP` 使用 SQuirreL 安裝目錄中的 `squirrel-sql.jar` 路徑進行初始化。
  2. **新增函式庫 Jars**：
     - `dir /b` 指令列出 `lib` 目錄中的所有檔案，並將其寫入 `squirrel-lib.tmp`。
     - `FOR /F` 循環遍歷檔案並呼叫 `addpath.bat`，將每個函式庫檔案（例如 `.jar` 檔案）附加到 `TMP_CP` classpath。
  3. **設定最終 Classpath**：
     - `SQUIRREL_CP` 設定為完成的 classpath。
  4. **除錯輸出**：
     - 腳本列印最終的 classpath（`SQUIRREL_CP`）用於除錯目的。

---

#### **10. 設定啟動參數**
```bat
SET TMP_PARMS=--log-config-file "%SQUIRREL_SQL_HOME%\log4j.properties" --squirrel-home "%SQUIRREL_SQL_HOME%" %1 %2 %3 %4 %5 %6 %7 %8 %9
```
- **用途**：定義要傳遞給 SQuirreL SQL 應用程式的參數。
- **解釋**：
  - `--log-config-file`：指定主應用程式的 Log4j 設定檔。
  - `--squirrel-home`：傳遞 SQuirreL 安裝目錄。
  - `%1 %2 ... %9`：傳遞提供給腳本的任何命令列參數。

---

#### **11. 啟動應用程式**
```bat
@rem -Dsun.java2d.noddraw=true prevents performance problems on Win32 systems.
start "SQuirreL SQL Client" /B "%LOCAL_JAVA%" -Xmx256m -Dsun.java2d.noddraw=true -cp %SQUIRREL_CP% -splash:"%SQUIRREL_SQL_HOME%/icons/splash.jpg" net.sourceforge.squirrel_sql.client.Main %TMP_PARMS%
```
- **用途**：啟動 SQuirreL SQL Client 應用程式。
- **解釋**：
  - **`start "SQuirreL SQL Client" /B`**：在不開啟新控制台視窗的情況下，於新進程中運行指令（`/B` 抑制視窗）。
  - **`%LOCAL_JAVA%`**：指定要使用的 Java 可執行檔。
  - **`-Xmx256m`**：將 Java 堆積大小上限設定為 256 MB，以限制記憶體使用。
  - **`-Dsun.java2d.noddraw=true`**：停用 Java 2D 圖形的 DirectDraw，以避免在 Windows 系統上出現效能問題。
  - **`-cp %SQUIRREL_CP%`**：指定應用程式的 classpath。
  - **`-splash:"%SQUIRREL_SQL_HOME%/icons/splash.jpg"`**：在應用程式啟動時顯示啟動畫面（圖像）。
  - **`net.sourceforge.squirrel_sql.client.Main`**：要執行的主要 Java 類別。
  - **`%TMP_PARMS%`**：傳遞先前定義的參數。

---

#### **12. 錯誤 Java 版本退出**
```bat
:ExitForWrongJavaVersion
```
- **用途**：如果 Java 版本檢查失敗，用作退出點的標籤。
- **解釋**：如果 Java 版本不是 1.6 或 1.7，腳本將跳轉到此處並在不啟動應用程式的情況下終止。

---

### **關鍵組件和概念**
1. **Classpath 建構**：
   - 腳本通過包含 `squirrel-sql.jar` 和 `lib` 或 `update\downloads\core` 目錄中的所有 `.jar` 檔案，動態建置更新過程（`UPDATE_CP`）和主應用程式（`SQUIRREL_CP`）的 classpath。
   - 假設 `addpath.bat` 腳本（未顯示）會將每個檔案附加到 classpath 變數。

2. **Log4j 設定**：
   - Log4j 是 SQuirreL SQL 使用的記錄框架。腳本為更新過程（`update-log4j.properties`）和主應用程式（`log4j.properties`）指定了單獨的 Log4j 設定檔。

3. **軟體更新機制**：
   - SQuirreL SQL 支援自動更新，由 `PreLaunchUpdateApplication` 類別管理。腳本檢查更新檔案並在必要時運行更新過程。

4. **Java 版本兼容性**：
   - 腳本強制要求與 Java 1.6 或 1.7 嚴格兼容，這可能是由於這些版本特定的依賴關係或功能。

5. **可攜性**：
   - 腳本通過動態確定安裝目錄和 Java 可執行檔位置來設計為可攜式。

---

### **潛在問題和注意事項**
1. **Java 版本限制**：
   - 腳本僅允許 Java 1.6 或 1.7，這些版本已經過時（分別於 2006 年和 2011 年發布）。現代系統可能具有較新的 Java 版本，導致腳本失敗，除非安裝了較舊的 JRE。
   - **解決方法**：使用者可能需要安裝兼容的 JRE，或修改腳本以支援較新版本（如果 SQuirreL SQL 兼容）。

2. **硬編碼路徑**：
   - 腳本假設某些檔案（例如 `squirrel-sql.jar`、`versioncheck.jar`、`addpath.bat`）存在於相對於 `SQUIRREL_SQL_HOME` 的特定目錄中。如果這些檔案遺失或移動，腳本將失敗。

3. **Windows 特定**：
   - 腳本使用 Windows 特定指令（`dir /b`、`FOR /F`、`start /B`）和 `javaw.exe`，使其在未經修改的情況下與非 Windows 系統不兼容。

4. **錯誤處理**：
   - 腳本處理 Java 版本錯誤，但未為其他故障（例如遺失 `squirrel-sql.jar` 或無效的 classpath）提供詳細的錯誤訊息。

5. **記憶體限制**：
   - `-Xmx256m` 標誌將 JVM 記憶體限制為 256 MB，對於大型資料庫或複雜查詢可能不足，可能導致 `OutOfMemoryError`。

---

### **總結**
此批次腳本是 SQuirreL SQL Client 的啟動器，執行以下任務：
- 偵測並配置 Java 可執行檔。
- 驗證 Java 版本兼容性（1.6 或 1.7）。
- 檢查並在可用時應用軟體更新。
- 為應用程式建置 classpath。
- 使用適當參數啟動 SQuirreL SQL，包括啟動畫面和記憶體設定。

該腳本結構良好，適合其用途，但針對特定環境（Windows、Java 1.6/1.7）定制，可能需要更新以支援現代系統或較新的 Java 版本。

如果您有進一步的問題或需要協助修改腳本（例如以支援較新的 Java 版本），請告訴我！