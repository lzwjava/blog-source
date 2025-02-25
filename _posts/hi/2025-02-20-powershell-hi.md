---
audio: false
lang: hi
layout: post
title: PowerShell Commands का उपयोग
translated: true
---

PowerShell स्क्रिप्टों के लिए पारंपरिक फ़ाइल एक्सटेंशन `.ps1` है। यहाँ एक `.ps1` फ़ाइल में इन कमांडों को सूचीबद्ध करने का तरीका है:

**फ़ाइल नाम: `common_commands.ps1`**

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

इस फ़ाइल को `.ps1` एक्सटेंशन के साथ सेंड कर सकते हैं, जो इसे एक PowerShell स्क्रिप्ट के रूप में पहचानता है। इस स्क्रिप्ट को चलाने के लिए आप उपयोग करेंगे:

```powershell
.\common_commands.ps1
```

कृपया ध्यान दें कि आप PowerShell स्क्रिप्ट चलाने के लिए अपने एक्सिक्यूशन पॉलिसी को सेट करने की जरूरत हो सकती है:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

यह कमांड स्क्रिप्ट को चलने देता है, लेकिन इसे वापस सेट करने या सावधानी से उपयोग करने की याद रखें क्योंकि यह सिस्टम सुरक्षा सेटिंग्स को प्रभावित करता है।