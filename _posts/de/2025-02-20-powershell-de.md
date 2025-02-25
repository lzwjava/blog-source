---
audio: false
lang: de
layout: post
title: PowerShell-Befehle
translated: true
---

Für PowerShell-Skripte ist die übliche Dateierweiterung `.ps1`. Hier ist, wie Sie diese Befehle in einer `.ps1`-Datei auflisten:

**Dateiname: `common_commands.ps1`**

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

Diese Datei kann mit der Erweiterung `.ps1` gespeichert werden, was sie als PowerShell-Skript kennzeichnet. Um dieses Skript auszuführen, verwenden Sie:

```powershell
.\common_commands.ps1
```

Bitte beachten Sie, dass Sie möglicherweise Ihre Ausführungsrichtlinie anpassen müssen, um PowerShell-Skripte auszuführen:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Dieser Befehl ermöglicht das Ausführen von Skripten, aber denken Sie daran, ihn zurückzusetzen oder vorsichtig zu verwenden, da er die System-Sicherheitseinstellungen beeinflusst.