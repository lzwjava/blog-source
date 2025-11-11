---
audio: false
generated: true
lang: hant
layout: post
title: 編寫 Windows 批次檔案
translated: true
type: note
---

Windows 批次檔案（.bat 或 .cmd）是一種包含一系列由 Windows 命令提示字元（cmd.exe）執行指令的腳本檔案。批次檔案能自動化重複性任務、管理系統操作或執行程式。以下是撰寫 Windows 批次檔案的完整介紹，涵蓋其用途、語法、常用指令與最佳實踐。

### 什麼是批次檔案？
批次檔案是副檔名為 `.bat` 或 `.cmd` 的純文字檔案，內含由 Windows 命令提示字元解譯的指令。執行時，指令會依序運行，可實現檔案管理、系統設定或軟體安裝等任務的自動化。

### 為何使用批次檔案？
- **自動化**：透過單一腳本執行多個指令
- **簡易性**：無需進階程式設計知識
- **系統管理**：執行備份、用戶管理或環境設定等任務
- **相容性**：適用所有具備命令提示字元的 Windows 版本

### 建立批次檔案
1. **撰寫腳本**：使用文字編輯器（如 Notepad、VS Code）編寫指令
2. **正確儲存副檔名**：將檔案儲存為 `.bat` 或 `.cmd` 副檔名（例如 `script.bat`）
3. **執行**：雙擊檔案或透過命令提示字元運行

### 基礎語法與結構
- **指令**：批次檔案使用命令提示字元指令（如 `dir`、`copy`、`del`）與批次專用指令（如 `echo`、`set`、`goto`）
- **註解**：使用 `REM` 或 `::` 添加說明註解
- **大小寫不敏感**：指令與變數不區分大小寫
- **逐行執行**：除非透過流程控制指令（如 `if`、`for` 或 `goto`），否則指令會逐行執行

### 常用指令與功能
#### 1. **基礎指令**
- `ECHO`：控制指令顯示或輸出文字
  - 範例：`ECHO Hello, World!` 顯示 "Hello, World!"
  - `ECHO OFF`：隱藏執行過程中的指令顯示
- `CLS`：清除命令提示字元畫面
- `PAUSE`：暫停執行，等待用戶輸入
- `EXIT`：終止腳本或命令提示字元工作階段

#### 2. **變數**
- **設定變數**：使用 `SET` 建立或修改變數
  - 範例：`SET MY_VAR=Hello` 建立變數 `MY_VAR`
- **使用變數**：以 `%變數名稱%` 格式引用
  - 範例：`ECHO %MY_VAR%` 顯示 "Hello"
- **環境變數**：內建變數如 `%PATH%`、`%USERNAME%` 或 `%DATE%`

#### 3. **輸入與輸出**
- **用戶輸入**：使用 `SET /P` 提示輸入
  - 範例：`SET /P NAME=請輸入姓名：` 將輸入儲存至 `NAME`
- **重新導向輸出**：使用 `>` 寫入檔案，`>>` 附加內容
  - 範例：`DIR > filelist.txt` 將目錄列表存入 `filelist.txt`

#### 4. **條件語句**
- 使用 `IF` 根據條件執行指令
  - 語法：`IF 條件 指令 [ELSE 指令]`
  - 範例：`IF "%NAME%"=="Admin" ECHO Welcome, Admin! ELSE ECHO Access denied.`

#### 5. **迴圈**
- **FOR 迴圈**：遍歷檔案、目錄或數值
  - 範例：`FOR %i IN (*.txt) DO ECHO %i` 列出所有 `.txt` 檔案
  - 注意：在批次檔案中需使用 `%%i` 代替 `%i`
- **WHILE 式迴圈**：透過 `GOTO` 與 `IF` 模擬實現

#### 6. **副程式與標籤**
- **標籤**：使用 `:label` 標記程式碼區段
- **GOTO**：跳轉至標記區段
  - 範例：`GOTO :EOF` 跳至檔案結尾
- **CALL**：呼叫其他批次檔案或副程式
  - 範例：`CALL :mySubroutine` 執行標記副程式

#### 7. **錯誤處理**
- 透過 `%ERRORLEVEL%` 檢查指令執行狀態
  - 範例：`IF %ERRORLEVEL% NEQ 0 ECHO 指令執行失敗`

### 最佳實踐
- **使用 `ECHO OFF`**：隱藏指令輸出以減少雜訊
- **添加註解**：使用 `REM` 或 `::` 記錄程式碼
- **增量測試**：分段執行小範圍程式碼進行除錯
- **錯誤處理**：檢查 `%ERRORLEVEL%` 確認執行狀態
- **路徑引號**：用引號包覆含空格的路徑（如 `"C:\Program Files\"`）
- **避免保留名稱**：勿使用 `CON`、`NUL` 或 `PRN` 作為檔案或變數名稱
- **使用 `@` 靜默執行**：在指令前添加 `@` 隱藏單行指令顯示（如 `@ECHO OFF`）

### 批次檔案範例
以下示範常用功能的範例批次檔案：提示用戶輸入、建立目錄與記錄輸出內容


@echo off
REM 範例批次檔案：建立目錄並記錄操作
ECHO 開始執行腳本...

:: 提示輸入目錄名稱
SET /P DIRNAME=請輸入目錄名稱：

:: 檢查是否輸入內容
IF "%DIRNAME%"=="" (
    ECHO 錯誤：未提供目錄名稱
    PAUSE
    EXIT /B 1
)

:: 建立目錄並記錄結果
MKDIR "%DIRNAME%"
IF %ERRORLEVEL%==0 (
    ECHO 目錄 "%DIRNAME%" 建立成功
    ECHO %DATE% %TIME%：建立目錄 "%DIRNAME%" >> log.txt
) ELSE (
    ECHO 建立目錄 "%DIRNAME%" 失敗
    ECHO %DATE% %TIME%：建立目錄 "%DIRNAME%" 失敗 >> log.txt
)

::mettere:PAUSE
ECHO 執行完畢
EXIT /B


### 執行批次檔案
- 將上述程式碼儲存為 `sample.bat`
- 雙擊執行或透過命令提示字元運行（`cmd.exe /c sample.bat`）

### 進階技巧
- **延遲擴充**：在迴圈中使用 `SETLOCAL EnableDelayedExpansion` 處理更新變數（改用 `!變數!` 格式）
- **錯誤等級**：使用 `IF ERRORLEVEL n` 檢測特定結束代碼
- **外部工具**：整合 `PowerShell` 或 `curl` 等工具實現進階功能
- **安全性**：避免執行來源不明的批次檔案以防惡意程式碼

### 限制
- **複雜度**：處理複雜任務時效能不如 PowerShell 或 Python
- **錯誤處理**：相較現代腳本語言功能有限
- **跨平台**：批次檔案僅適用 Windows 系統

### 資源
- **官方文件**：Microsoft 命令提示字元參考（cmd.exe 中的 `help` 指令）
- **教學資源**：SS64.com 等網站提供詳細指令參考
- **社群資源**：可在 X 或 Stack Overflow 等論壇搜尋批次檔案範例

本介紹提供撰寫批次檔案的基礎知識。透過簡單腳本實際練習，並利用命令提示字元的 `help` 指令探索更多指令，將能逐步提升您的技能。