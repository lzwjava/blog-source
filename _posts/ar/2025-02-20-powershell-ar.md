---
audio: false
generated: true
lang: ar
layout: post
title: أوامر PowerShell
translated: true
---

للمسارات PowerShell، الإمتداد التقليدي للملف هو `.ps1`. إليك كيفية سرد هذه الأوامر في ملف `.ps1`:

**اسم الملف: `common_commands.ps1`**

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

يمكن حفظ هذا الملف بامتداد `.ps1`، والذي يحدده كمسار PowerShell. لتشغيل هذا المسار، يمكنك استخدام:

```powershell
.\common_commands.ps1
```

يرجى ملاحظة أنك قد تحتاج إلى تعديل سياستك التنفيذية لتشغيل مسارات PowerShell:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

تسمح هذه الأوامر بالتشغيل، ولكن تذكر أن تعيد تعيينها أو استخدمها بحذر لأنها تؤثر على إعدادات أمن النظام.