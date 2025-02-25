---
audio: false
lang: fr
layout: post
title: Commandes PowerShell
translated: true
---

Pour les scripts PowerShell, l'extension de fichier conventionnelle est `.ps1`. Voici comment vous pourriez lister ces commandes dans un fichier `.ps1` :

**Nom du fichier : `common_commands.ps1`**

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

Ce fichier peut être enregistré avec l'extension `.ps1`, ce qui l'identifie comme un script PowerShell. Pour exécuter ce script, vous utiliseriez :

```powershell
.\common_commands.ps1
```

Veuillez noter que vous pourriez avoir besoin d'ajuster votre politique d'exécution pour exécuter des scripts PowerShell :

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Cette commande permet aux scripts de s'exécuter, mais n'oubliez pas de la réinitialiser ou de l'utiliser prudemment car elle affecte les paramètres de sécurité du système.