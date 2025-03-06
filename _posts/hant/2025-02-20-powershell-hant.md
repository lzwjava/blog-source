---
audio: false
generated: false
lang: hant
layout: post
title: PowerShell 指令
translated: true
---

對於 PowerShell 腳本，傳統的文件擴展名是 `.ps1`。以下是如何在 `.ps1` 文件中列出這些命令：

**文件名：`common_commands.ps1`**

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

這個文件可以保存為 `.ps1` 擴展名，這樣就能識別它是一個 PowerShell 腳本。要運行這個腳本，可以使用：

```powershell
.\common_commands.ps1
```

請注意，您可能需要調整執行策略來運行 PowerShell 腳本：

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

這個命令允許腳本運行，但請記住要將其設置回來或謹慎使用，因為它會影響系統安全設置。