---
audio: false
generated: true
lang: hant
layout: post
title: PowerShell 對比 命令提示字元
translated: true
type: note
---

PowerShell 與命令提示字元 (cmd.exe) 都是 Windows 環境中使用的命令列介面，但兩者在功能、指令碼處理能力和整體效能方面存在明顯差異。以下為比較說明：

### PowerShell 與命令提示字元比較

1. **語言與語法：**
   - **命令提示字元 (cmd.exe)：** 使用簡單的批次指令碼語言，功能較弱且缺乏物件導向處理方式。指令通常為文字基礎，靈活性較低。
   - **PowerShell：** 採用基於 .NET 的進階指令碼語言，支援物件導向程式設計，可實現更複雜且強大的指令碼功能。

2. **Cmdlet 與指令比較：**
   - **命令提示字元：** 依賴有限的內建指令（如 `dir`、`copy`、`del`）及外部工具。
   - **PowerShell：** 使用稱為 Cmdlet 的專用 .NET 類別來執行特定任務。Cmdlet 採用動詞-名詞命名慣例（如 `Get-ChildItem`、`Copy-Item`），具有更高一致性和強大功能。

3. **指令碼處理能力：**
   - **命令提示字元：** 透過批次檔 (.bat 或 .cmd) 進行指令碼編寫，處理複雜任務時效能較弱且操作繁瑣。
   - **PowerShell：** 透過 PowerShell 指令碼 (.ps1) 執行，支援迴圈、條件判斷、函式與錯誤處理等進階程式設計結構。

4. **輸出處理：**
   - **命令提示字元：** 輸出通常為純文字格式，較難進行操作與解析。
   - **PowerShell：** 輸出為物件基礎，能更輕鬆操作與處理資料，還可透過管線在 Cmdlet 間傳遞物件以執行複雜操作。

5. **整合與擴充性：**
   - **命令提示字元：** 與其他 Windows 功能及外部工具的整合性有限。
   - **PowerShell：** 深度整合 Windows 及其他微軟產品，能充分運用 .NET Framework 的完整功能，並可透過模組與嵌入式管理單元擴充。

6. **錯誤處理：**
   - **命令提示字元：** 僅具備基本錯誤處理能力。
   - **PowerShell：** 提供包含 try-catch 區塊與詳細錯誤訊息的進階錯誤處理機制。

### PowerShell 是否更優越？

對於大多數任務（特別是涉及自動化、系統管理與複雜指令碼處理的工作），PowerShell 通常被認為優於命令提示字元。其進階功能、物件導向處理方式及與 Windows 的深度整合，使其成為更強大且靈活的工具。

### PowerShell 指令碼撰寫

撰寫 PowerShell 指令碼需建立包含 PowerShell 指令與邏輯的 .ps1 檔案。以下為重點說明：

- **語法：** PowerShell 指令碼採用類似其他程式語言的語法，支援變數、迴圈、條件判斷與函式。
- **Cmdlet：** 運用直觀且一致的 Cmdlet 來執行任務。
- **模組：** 透過 PowerShell 模組可匯入額外 Cmdlet 與函式來擴充功能。
- **錯誤處理：** 使用 try-catch 區塊實現優雅的錯誤處理。
- **管線：** 利用管線在 Cmdlet 間傳遞物件，實現複雜資料操作。

### PowerShell 指令碼範例

```powershell
# 列出目錄中檔案並依副檔名篩選的 PowerShell 指令碼範例
$directory = "C:\Example"
$extension = ".txt"

Get-ChildItem -Path $directory -Filter "*$extension" | ForEach-Object {
    Write-Host "檔案：$($_.Name), 大小：$($_.Length) 位元組"
}
```

總而言之，PowerShell 在指令碼處理與自動化任務方面較命令提示字元具有顯著優勢。其進階功能與 Windows 生態系統的整合，使其成為系統管理員與進階使用者的強大工具。