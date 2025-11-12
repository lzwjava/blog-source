---
audio: false
generated: false
lang: ja
layout: post
title: PowerShellコマンド
translated: true
type: note
---

PowerShellスクリプトの場合、従来のファイル拡張子は`.ps1`です。以下はこれらのコマンドを`.ps1`ファイルに記述する方法です：

**ファイル名：`common_commands.ps1`**

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

このファイルは`.ps1`拡張子で保存でき、PowerShellスクリプトとして識別されます。このスクリプトを実行するには、以下を使用します：

```powershell
.\common_commands.ps1
```

PowerShellスクリプトを実行するには、実行ポリシーを調整する必要がある場合があります：

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

このコマンドはスクリプトの実行を許可しますが、システムのセキュリティ設定に影響するため、注意して使用し、元に戻すか慎重に使用することを忘れないでください。