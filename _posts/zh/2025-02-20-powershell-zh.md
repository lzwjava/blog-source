---
audio: false
generated: true
lang: zh
layout: post
title: PowerShell 命令
translated: true
---

对于 PowerShell 脚本，常用的文件扩展名是 `.ps1`。以下是如何在 `.ps1` 文件中列出这些命令：

**文件名: `common_commands.ps1`**

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

这个文件可以保存为 `.ps1` 扩展名，以标识它为 PowerShell 脚本。要运行这个脚本，可以使用：

```powershell
.\common_commands.ps1
```

请注意，您可能需要调整执行策略以运行 PowerShell 脚本：

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

这个命令允许脚本运行，但请记住要将其设置回原位或谨慎使用，因为它会影响系统的安全设置。