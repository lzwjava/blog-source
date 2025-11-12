---
audio: false
generated: false
lang: hi
layout: post
title: पावरशेल कमांड्स
translated: true
type: note
---

PowerShell स्क्रिप्ट्स के लिए, पारंपरिक फ़ाइल एक्सटेंशन `.ps1` है। यहां बताया गया है कि आप इन कमांड्स को एक `.ps1` फ़ाइल में कैसे सूचीबद्ध करेंगे:

**फ़ाइल का नाम: `common_commands.ps1`**

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

इस फ़ाइल को `.ps1` एक्सटेंशन के साथ सेव किया जा सकता है, जो इसे एक PowerShell स्क्रिप्ट के रूप में पहचानता है। इस स्क्रिप्ट को रन करने के लिए, आप इसका उपयोग करेंगे:

```powershell
.\common_commands.ps1
```

कृपया ध्यान दें कि PowerShell स्क्रिप्ट्स को रन करने के लिए आपको अपनी एक्ज़िक्यूशन पॉलिसी को एडजस्ट करने की आवश्यकता हो सकती है:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

यह कमांड स्क्रिप्ट्स को रन होने की अनुमति देती है, लेकिन याद रखें कि इसे वापस सेट कर दें या सावधानी से उपयोग करें क्योंकि यह सिस्टम सुरक्षा सेटिंग्स को प्रभावित करती है।