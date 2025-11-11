---
audio: false
generated: true
lang: hant
layout: post
title: PowerShell 指令指南
translated: true
type: note
---

## PowerShell 簡介
PowerShell 是微軟推出的任務自動化與組態管理框架，包含命令列殼層與指令碼語言。它基於 .NET Framework（新版本則基於 .NET Core）建構，讓管理員能夠在 Windows、Linux 和 macOS 系統上執行複雜任務。

PowerShell 命令稱為 **cmdlet**（發音為 "command-lets"），遵循 `動詞-名詞` 的命名慣例（例如 `Get-Process`、`Set-Item`）。本指南將按功能分類介紹重要 cmdlet，並附帶使用範例。

---

## 1. PowerShell 核心概念
在深入學習命令之前，理解關鍵概念至關重要：
- **Cmdlet**：執行特定功能的輕量級命令
- **管線**：透過 `|` 運算子將一個 cmdlet 的輸出傳遞給另一個 cmdlet 作為輸入
- **模組**：包含 cmdlet、指令碼和功能的集合，可擴展 PowerShell 功能
- **提供者**：可將資料存放區（如檔案系統、登錄檔）當作磁碟機存取的介面
- **物件**：PowerShell 以物件而非純文字運作，實現結構化資料處理

---

## 2. 依類別區分的必要 Cmdlet

### 2.1 系統資訊
這些 cmdlet 可擷取系統、處理程序與服務的相關資訊

| Cmdlet | 描述 | 範例 |
|--------|-------------|---------|
| `Get-ComputerInfo` | 擷取系統硬體與軟體詳細資訊 | `Get-ComputerInfo | Select-Object WindowsProductName, OsVersion` |
| `Get-Process` | 列出執行中的處理程序 | `Get-Process | Where-Object {$_.CPU -gt 1000}` |
| `Get-Service` | 顯示系統上的服務 | `Get-Service | Where-Object {$_.Status -eq "Running"}` |
| `Get-HotFix` | 列出已安裝的 Windows 更新 | `Get-HotFix | Sort-Object InstalledOn -Descending` |

**範例**：列出所有執行中的處理程序，並按 CPU 使用率排序
```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object Name, CPU, Id -First 5
```

### 2.2 檔案與目錄管理
PowerShell 將檔案系統視為提供者，允許類似磁碟機的瀏覽方式

| Cmdlet | 描述 | 範例 |
|--------|-------------|---------|
| `Get-Item` | 擷取檔案或目錄 | `Get-Item C:\Users\*.txt` |
| `Set-Item` | 修改項目屬性（例如檔案屬性） | `Set-Item -Path C:\test.txt -Value "New content"` |
| `New-Item` | 建立新檔案或目錄 | `New-Item -Path C:\Docs -Name Report.txt -ItemType File` |
| `Remove-Item` | 刪除檔案或目錄 | `Remove-Item C:\Docs\OldFile.txt` |
| `Copy-Item` | 複製檔案或目錄 | `Copy-Item C:\Docs\Report.txt D:\Backup` |
| `Move-Item` | 移動檔案或目錄 | `Move-Item C:\Docs\Report.txt C:\Archive` |

**範例**：建立目錄與檔案，然後複製到其他位置
```powershell
New-Item -Path C:\Temp -Name MyFolder -ItemType Directory
New-Item -Path C:\Temp\MyFolder -Name Test.txt -ItemType File
Copy-Item C:\Temp\MyFolder\Test.txt C:\Backup
```

### 2.3 系統管理
用於管理系統設定、服務與使用者的 Cmdlet

| Cmdlet | 描述 | 範例 |
|--------|-------------|---------|
| `Start-Service` | 啟動服務 | `Start-Service -Name "wuauserv"` |
| `Stop-Service` | 停止服務 | `Stop-Service -Name "wuauserv"` |
| `Restart-Computer` | 重新啟動系統 | `Restart-Computer -Force` |
| `Get-EventLog` | 擷取事件記錄項目 | `Get-EventLog -LogName System -Newest 10` |
| `Set-ExecutionPolicy` | 設定指令碼執行原則 | `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |

**範例**：檢查 Windows Update 服務狀態，若停止則啟動
```powershell
$service = Get-Service -Name "wuauserv"
if ($service.Status -eq "Stopped") {
    Start-Service -Name "wuauserv"
}
```

### 2.4 網路管理
用於網路組態與診斷的 Cmdlet

| Cmdlet | 描述 | 範例 |
|--------|-------------|---------|
| `Test-Connection` | 對遠端主機執行 ping | `Test-Connection google.com` |
| `Get-NetAdapter` | 列出網路介面卡 | `Get-NetAdapter | Select-Object Name, Status` |
| `Get-NetIPAddress` | 擷取 IP 地址組態 | `Get-NetIPAddress -AddressFamily IPv4` |
| `Resolve-DnsName` | 解析 DNS 名稱 | `Resolve-DnsName www.google.com` |

**範例**：對伺服器執行 ping 並檢查其 DNS 解析
```powershell
Test-Connection -ComputerName google.com -Count 2
Resolve-DnsName google.com
```

### 2.5 使用者與群組管理
用於管理本機使用者與群組的 Cmdlet

| Cmdlet | 描述 | 範例 |
|--------|-------------|---------|
| `New-LocalUser` | 建立本機使用者帳戶 | `New-LocalUser -Name "TestUser" -Password (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force)` |
| `Remove-LocalUser` | 刪除本機使用者帳戶 | `Remove-LocalUser -Name "TestUser"` |
| `Get-LocalGroup` | 列出本機群組 | `Get-LocalGroup | Select-Object Name` |
| `Add-LocalGroupMember` | 將使用者加入本機群組 | `Add-LocalGroupMember -Group "Administrators" -Member "TestUser"` |

**範例**：建立新本機使用者並將其加入 Administrators 群組
```powershell
$password = ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force
New-LocalUser -Name "TestUser" -Password $password -FullName "Test User" -Description "Test account"
Add-LocalGroupMember -Group "Administrators" -Member "TestUser"
```

### 2.6 指令碼編寫與自動化
PowerShell 在自動化指令碼編寫方面表現卓越

| Cmdlet | 描述 | 範例 |
|--------|-------------|---------|
| `Write-Output` | 將資料輸出至管線 | `Write-Output "Hello, World!"` |
| `ForEach-Object` | 循環處理管線中的項目 | `Get-Process | ForEach-Object { $_.Name }` |
| `Where-Object` | 根據條件篩選物件 | `Get-Service | Where-Object { $_.Status -eq "Running" }` |
| `Invoke-Command` | 在本機或遠端電腦上執行命令 | `Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Process }` |
| `New-ScheduledTask` | 建立排程任務 | `New-ScheduledTask -Action (New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File C:\script.ps1") -Trigger (New-ScheduledTaskTrigger -Daily -At "3AM")` |

**範例**：建立指令碼將執行中的處理程序記錄到檔案
```powershell
$logPath = "C:\Logs\ProcessLog.txt"
Get-Process | Select-Object Name, CPU, StartTime | Export-Csv -Path $logPath -NoTypeInformation
```

### 2.7 模組管理
模組可擴展 PowerShell 功能

| Cmdlet | 描述 | 範例 |
|--------|-------------|---------|
| `Get-Module` | 列出可用或已匯入的模組 | `Get-Module -ListAvailable` |
| `Import-Module` | 匯入模組 | `Import-Module ActiveDirectory` |
| `Install-Module` | 從儲存庫安裝模組 | `Install-Module -Name PSWindowsUpdate -Force` |
| `Find-Module` | 在儲存庫中搜尋模組 | `Find-Module -Name *Azure*` |

**範例**：安裝並匯入 PSWindowsUpdate 模組以管理 Windows 更新
```powershell
Install-Module -Name PSWindowsUpdate -Force
Import-Module PSWindowsUpdate
Get-WUList
```

---

## 3. 使用管線
管線（`|`）可讓 cmdlet 鏈結起來依序處理資料。例如：
```powershell
Get-Process | Where-Object { $_.WorkingSet64 -gt 100MB } | Sort-Object WorkingSet64 -Descending | Select-Object Name, WorkingSet64 -First 5
```
此命令：
1. 擷取所有處理程序
2. 篩選記憶體使用量超過 100MB 的處理程序
3. 按記憶體使用量降冪排序
4. 選取前 5 個處理程序，顯示其名稱與記憶體使用量

---

## 4. 變數、循環與條件
PowerShell 支援指令碼建構以實現自動化

### 變數
```powershell
$path = "C:\Logs"
$services = Get-Service
Write-Output "Log path is $path"
```

### 循環
- **ForEach-Object**：
```powershell
Get-Service | ForEach-Object { Write-Output $_.Name }
```
- **For 循環**：
```powershell
for ($i = 1; $i -le 5; $i++) { Write-Output "Iteration $i" }
```

### 條件
```powershell
$service = Get-Service -Name "wuauserv"
if ($service.Status -eq "Running") {
    Write-Output "Windows Update is running."
} else {
    Write-Output "Windows Update is stopped."
}
```

---

## 5. 錯誤處理
使用 `Try`、`Catch` 與 `Finally` 建立穩健的指令碼
```powershell
Try {
    Get-Item -Path C:\NonExistentFile.txt -ErrorAction Stop
}
Catch {
    Write-Output "Error: $($_.Exception.Message)"
}
Finally {
    Write-Output "Operation completed."
}
```

---

## 6. 遠端管理
PowerShell 支援使用 `Invoke-Command` 與 `Enter-PSSession` 進行遠端管理

**範例**：在遠端電腦上執行命令
```powershell
Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Service | Where-Object { $_.Status -eq "Running" } }
```

**範例**：啟動互動式遠端工作階段
```powershell
Enter-PSSession -ComputerName Server01
```

---

## 7. 實用指令碼範例
以下是監控磁碟空間並在使用率超過 80% 時發出警示的範例指令碼

```powershell
$disks = Get-Disk
$threshold = 80

foreach ($disk in $disks) {
    $freeSpacePercent = ($disk.FreeSpace / $disk.Size) * 100
    if ($freeSpacePercent -lt (100 - $threshold)) {
        Write-Output "Warning: Disk $($disk.Number) is at $("{0:N2}" -f (100 - $freeSpacePercent))% capacity."
    }
}
```

---

## 8. 有效使用 PowerShell 的秘訣
- **使用別名提升速度**：常見別名如 `dir`（`Get-ChildItem`）、`ls`（`Get-ChildItem`）或 `gci`（`Get-ChildItem`）可在互動式工作階段中節省時間
- **Get-Help**：使用 `Get-Help <cmdlet>` 取得詳細文件（例如 `Get-Help Get-Process -Full`）
- **Update-Help**：使用 `Update-Help` 保持說明檔案最新
- **設定檔**：透過編輯 `$PROFILE` 自訂 PowerShell 環境（例如 `notepad $PROFILE`）
- **Tab 鍵自動完成**：按 `Tab` 鍵自動完成 cmdlet、參數與路徑
- **使用詳細輸出**：在 cmdlet 中加入 `-Verbose` 以取得詳細執行資訊

---

## 9. 其他資源
- **官方文件**：[Microsoft PowerShell 文件](https://docs.microsoft.com/en-us/powershell/)
- **PowerShell Gallery**：[PowerShell Gallery](https://www.powershellgallery.com/) 提供模組
- **社群**：查看 X 或 Stack Overflow 等論壇上的貼文以取得即時秘訣與指令碼
- **學習資源**：如 *PowerShell in Depth* 或 *Learn PowerShell in a Month of Lunches* 等書籍

---

PowerShell 是微軟開發的強大指令碼語言與命令列殼層，廣泛用於任務自動化與組態管理。以下是除了 `Get-NetTCPConnection` 之外的一些常用 PowerShell 命令：

1. **Get-Process**：擷取在本機電腦或遠端電腦上執行的處理程序相關資訊

2. **Get-Service**：取得本機或遠端電腦上的服務

3. **Get-EventLog**：從事件記錄（包括應用程式、安全性與系統記錄）擷取事件

4. **Get-ChildItem**：取得一個或多個指定位置中的項目與子項目（類似 Command Prompt 中的 `dir`）

5. **Get-Content**：取得指定位置項目的內容（類似 Command Prompt 中的 `type`）

6. **Set-ExecutionPolicy**：變更使用者對 PowerShell 執行原則的偏好設定

7. **Invoke-Command**：在本機與遠端電腦上執行命令

8. **New-Item**：建立新項目，例如檔案或目錄

9. **Remove-Item**：刪除指定項目

10. **Copy-Item**：將項目從一個位置複製到另一個位置

11. **Move-Item**：將項目從一個位置移動到另一個位置

12. **Rename-Item**：在 PowerShell 提供者命名空間中重新命名項目

13. **Get-Help**：顯示關於 PowerShell 命令與概念的資訊

14. **Select-Object**：選取物件或物件集合的指定屬性

15. **Where-Object**：根據屬性值從集合中選取物件

16. **Sort-Object**：按屬性值排序物件

17. **Export-Csv**：將物件轉換為一系列 CSV 字串並將字串儲存到檔案

18. **Import-Csv**：匯入 CSV 檔案並將其轉換為物件

19. **Start-Process**：在本機電腦上啟動一個或多個處理程序

20. **Stop-Process**：停止一個或多個執行中的處理程序

這些命令僅是 PowerShell 功能的少數範例。該語言具有高度擴展性，您可以建立自訂 cmdlet 與指令碼來自動化複雜任務。