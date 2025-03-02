---
audio: false
generated: true
lang: es
layout: post
title: Comandos de PowerShell
translated: true
---

Para scripts de PowerShell, la extensión de archivo convencional es `.ps1`. Aquí te muestro cómo listar estos comandos en un archivo `.ps1`:

**Nombre del archivo: `common_commands.ps1`**

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

Este archivo se puede guardar con la extensión `.ps1`, lo que lo identifica como un script de PowerShell. Para ejecutar este script, usarías:

```powershell
.\common_commands.ps1
```

Ten en cuenta que es posible que necesites ajustar tu política de ejecución para ejecutar scripts de PowerShell:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Este comando permite que los scripts se ejecuten, pero recuerda restablecerlo o usarlo con precaución, ya que afecta la configuración de seguridad del sistema.