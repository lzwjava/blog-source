---
audio: false
generated: false
lang: hant
layout: post
title: PowerShell 指令
translated: true
type: note
---

對於 PowerShell 腳本，慣用的檔案副檔名是 `.ps1`。以下是如何在 `.ps1` 檔案中列出這些指令：

**檔案名稱：`common_commands.ps1`**

```powershell
Get-Command -Verb Get
Get-Help Get-Process -Full
Get-Process java
Stop-Process -Name java -Force
Start-Process -FilePath "java" -ArgumentList "-jar", "app.jar"
Get-Service -Name mysql
Start-Service -Name mysql
Stop-Service -Name mysql
Get-ChildItem -Path "C:\Projects\MySpringApp"
Remove-Item -Path "C:\Logs\*.log"
Copy-Item -Path "C:\Source\config.properties" -Destination "C:\Destination"
New-Item -Path "C:\Projects\NewSpringProject" -ItemType Directory
Set-Location -Path "C:\Projects\MySpringApp"
Invoke-WebRequest -Uri "http://localhost:8080/api/v1/resource" -Method Get
Test-NetConnection -ComputerName "localhost" -Port 8080
Get-Content -Path "C:\Logs\app.log" -Tail 100
Set-Content -Path "C:\Config\db.properties" -Value "db.url=jdbc:mysql://localhost:3306/mydb"
Add-Content -Path "C:\Logs\app.log" -Value "Application started at $(Get-Date)"
Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Get-Content -Path "C:\Logs\app.log" | Measure-Object -Line
@{Name="John"; Age=30} | ConvertTo-Json
```

此檔案可儲存為 `.ps1` 副檔名，以識別為 PowerShell 腳本。要執行此腳本，您需要使用：

```powershell
.\common_commands.ps1
```

請注意，您可能需要調整執行原則才能執行 PowerShell 腳本：

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

此指令允許腳本執行，但請記住謹慎使用或將其設回原值，因為它會影響系統安全性設定。