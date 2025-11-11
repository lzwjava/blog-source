---
audio: false
generated: true
lang: hant
layout: post
title: PowerShell：Get-NetTCPConnection 用法
translated: true
type: note
---

PowerShell 中的 `Get-NetTCPConnection` cmdlet 用於擷取 Windows 系統上的 TCP 連線資訊。它屬於 `NetTCPIP` 模組，可在 Windows 8/Windows Server 2012 及更新版本中使用。以下是使用指南：

### 基本用法
執行 `Get-NetTCPConnection` 以列出所有活躍的 TCP 連線：

```powershell
Get-NetTCPConnection
```

這會傳回詳細資訊，包括 LocalAddress、LocalPort、RemoteAddress、RemotePort、State 及 OwningProcess。

### 常用參數
- **-State**：依連線狀態篩選（例如 Established、Listening、TimeWait）。
  ```powershell
  Get-NetTCPConnection -State Established
  ```
- **-LocalPort**：依本機端口號碼篩選。
  ```powershell
  Get-NetTCPConnection -LocalPort 80
  ```
- **-RemoteAddress**：依遠端 IP 位址篩選。
  ```powershell
  Get-NetTCPConnection -RemoteAddress 192.168.1.1
  ```
- **-RemotePort**：依遠端端口篩選。
  ```powershell
  Get-NetTCPConnection -RemotePort 443
  ```
- **-OwningProcess**：依擁有連線的行程 ID (PID) 篩選。
  ```powershell
  Get-NetTCPConnection -OwningProcess 1234
  ```

### 合併篩選條件
可合併參數以獲得更精確的結果：
```powershell
Get-NetTCPConnection -State Established -LocalPort 80
```

### 顯示特定屬性
使用 `Select-Object` 僅顯示所需屬性：
```powershell
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### 查詢行程詳細資訊
結合 `Get-Process` 識別連線對應的行程：
```powershell
Get-NetTCPConnection -LocalPort 80 | ForEach-Object { Get-Process -Id $_.OwningProcess }
```

### 排序與格式化輸出
將結果排序（例如依 LocalPort）並以表格格式顯示：
```powershell
Get-NetTCPConnection | Sort-Object LocalPort | Format-Table LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### 實用範例
1. **列出所有監聽中的連線：**
   ```powershell
   Get-NetTCPConnection -State Listening
   ```
2. **尋找連線至特定遠端伺服器的連線：**
   ```powershell
   Get-NetTCPConnection -RemoteAddress "8.8.8.8"
   ```
3. **檢查特定端口正在被哪個行程使用：**
   ```powershell
   $connection = Get-NetTCPConnection -LocalPort 8080
   Get-Process -Id $connection.OwningProcess
   ```

### 注意事項
- **管理員權限**：部分詳細資訊（例如系統行程的 OwningProcess）可能需要以管理員身分執行 PowerShell。
- **IPv4/IPv6**：此 cmdlet 同時處理 IPv4 與 IPv6 連線。
- **匯出結果**：使用 `Export-Csv` 將輸出儲存至檔案：
  ```powershell
  Get-NetTCPConnection | Export-Csv -Path "tcp_connections.csv" -NoTypeInformation
  ```

如需更多詳細資訊，請執行：
```powershell
Get-Help Get-NetTCPConnection -Full
```

如果您需要特定範例或有特殊使用情境，請告訴我！