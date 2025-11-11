---
audio: false
generated: true
lang: hi
layout: post
title: पावरशेल कमांड्स गाइड
translated: true
type: note
---

## PowerShell का परिचय
PowerShell Microsoft द्वारा विकसित एक टास्क ऑटोमेशन और कॉन्फ़िगरेशन प्रबंधन फ्रेमवर्क है, जिसमें एक कमांड-लाइन शेल और एक स्क्रिप्टिंग भाषा शामिल है। यह .NET फ्रेमवर्क (और नए संस्करणों में .NET Core) पर बनाया गया है, जो व्यवस्थापकों को Windows, Linux, और macOS सिस्टम पर जटिल कार्यों को करने में सक्षम बनाता है।

PowerShell कमांड्स, जिन्हें **cmdlets** (उच्चारण "कमांड-लेट्स") कहा जाता है, एक `क्रिया-संज्ञा` नामकरण परंपरा का पालन करते हैं (उदाहरण के लिए, `Get-Process`, `Set-Item`)। यह मार्गदर्शिका आवश्यक cmdlets को उनकी कार्यक्षमता के आधार पर वर्गीकृत करते हुए, उनके उपयोग को प्रदर्शित करने वाले उदाहरणों के साथ कवर करती है।

---

## 1. PowerShell की मूल अवधारणाएँ
कमांड्स में गोता लगाने से पहले, प्रमुख अवधारणाओं को समझना महत्वपूर्ण है:
- **Cmdlets**: हल्के-फुल्के कमांड जो विशिष्ट कार्य करते हैं।
- **Pipelines**: एक cmdlet के आउटपुट को `|` ऑपरेटर का उपयोग करके दूसरे के इनपुट के रूप में पास करने की अनुमति देते हैं।
- **Modules**: Cmdlets, स्क्रिप्ट्स और फ़ंक्शन्स का संग्रह जो PowerShell की कार्यक्षमता का विस्तार करते हैं।
- **Providers**: डेटा स्टोर (जैसे फ़ाइल सिस्टम, रजिस्ट्री) तक पहुँचने के लिए इंटरफेस, मानो वे ड्राइव हों।
- **Objects**: PowerShell प्लेन टेक्स्ट के बजाय ऑब्जेक्ट्स के साथ काम करता है, जो संरचित डेटा मैनिपुलेशन को सक्षम बनाता है।

---

## 2. श्रेणी के अनुसार आवश्यक Cmdlets

### 2.1 सिस्टम सूचना
ये cmdlets सिस्टम, प्रक्रियाओं और सेवाओं के बारे में जानकारी प्राप्त करते हैं।

| Cmdlet | विवरण | उदाहरण |
|--------|-------------|---------|
| `Get-ComputerInfo` | सिस्टम हार्डवेयर और सॉफ्टवेयर विवरण प्राप्त करता है। | `Get-ComputerInfo | Select-Object WindowsProductName, OsVersion` |
| `Get-Process` | चल रही प्रक्रियाओं की सूची बनाता है। | `Get-Process | Where-Object {$_.CPU -gt 1000}` |
| `Get-Service` | सिस्टम पर सेवाएँ प्रदर्शित करता है। | `Get-Service | Where-Object {$_.Status -eq "Running"}` |
| `Get-HotFix` | इंस्टॉल किए गए Windows अपडेट्स की सूची बनाता है। | `Get-HotFix | Sort-Object InstalledOn -Descending` |

**उदाहरण**: CPU उपयोग के आधार पर क्रमबद्ध सभी चल रही प्रक्रियाओं की सूची बनाएं।
```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object Name, CPU, Id -First 5
```

### 2.2 फ़ाइल और निर्देशिका प्रबंधन
PowerShell फ़ाइल सिस्टम को एक प्रदाता के रूप में मानता है, जो एक ड्राइव के समान नेविगेशन की अनुमति देता है।

| Cmdlet | विवरण | उदाहरण |
|--------|-------------|---------|
| `Get-Item` | फ़ाइलें या निर्देशिकाएँ प्राप्त करता है। | `Get-Item C:\Users\*.txt` |
| `Set-Item` | आइटम गुणों (जैसे फ़ाइल विशेषताएँ) को संशोधित करता है। | `Set-Item -Path C:\test.txt -Value "New content"` |
| `New-Item` | एक नई फ़ाइल या निर्देशिका बनाता है। | `New-Item -Path C:\Docs -Name Report.txt -ItemType File` |
| `Remove-Item` | फ़ाइलें या निर्देशिकाएँ हटाता है। | `Remove-Item C:\Docs\OldFile.txt` |
| `Copy-Item` | फ़ाइलें या निर्देशिकाएँ कॉपी करता है। | `Copy-Item C:\Docs\Report.txt D:\Backup` |
| `Move-Item` | फ़ाइलें या निर्देशिकाएँ ले जाता है। | `Move-Item C:\Docs\Report.txt C:\Archive` |

**उदाहरण**: एक निर्देशिका और एक फ़ाइल बनाएं, फिर इसे किसी अन्य स्थान पर कॉपी करें।
```powershell
New-Item -Path C:\Temp -Name MyFolder -ItemType Directory
New-Item -Path C:\Temp\MyFolder -Name Test.txt -ItemType File
Copy-Item C:\Temp\MyFolder\Test.txt C:\Backup
```

### 2.3 सिस्टम प्रबंधन
सिस्टम सेटिंग्स, सेवाओं और उपयोगकर्ताओं के प्रबंधन के लिए Cmdlets.

| Cmdlet | विवरण | उदाहरण |
|--------|-------------|---------|
| `Start-Service` | एक सेवा शुरू करता है। | `Start-Service -Name "wuauserv"` |
| `Stop-Service` | एक सेवा रोकता है। | `Stop-Service -Name "wuauserv"` |
| `Restart-Computer` | सिस्टम को पुनरारंभ करता है। | `Restart-Computer -Force` |
| `Get-EventLog` | इवेंट लॉ एंट्रीज़ प्राप्त करता है। | `Get-EventLog -LogName System -Newest 10` |
| `Set-ExecutionPolicy` | स्क्रिप्ट निष्पादन नीति सेट करता है। | `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |

**उदाहरण**: Windows Update सेवा की स्थिति जांचें और यदि रुकी हुई है तो इसे शुरू करें।
```powershell
$service = Get-Service -Name "wuauserv"
if ($service.Status -eq "Stopped") {
    Start-Service -Name "wuauserv"
}
```

### 2.4 नेटवर्क प्रबंधन
नेटवर्क कॉन्फ़िगरेशन और निदान के लिए Cmdlets.

| Cmdlet | विवरण | उदाहरण |
|--------|-------------|---------|
| `Test-Connection` | एक रिमोट होस्ट को पिंग करता है। | `Test-Connection google.com` |
| `Get-NetAdapter` | नेटवर्क एडाप्टर की सूची बनाता है। | `Get-NetAdapter | Select-Object Name, Status` |
| `Get-NetIPAddress` | IP एड्रेस कॉन्फ़िगरेशन प्राप्त करता है। | `Get-NetIPAddress -AddressFamily IPv4` |
| `Resolve-DnsName` | DNS नामों को रिज़ॉल्व करता है। | `Resolve-DnsName www.google.com` |

**उदाहरण**: एक सर्वर को पिंग करें और उसका DNS रिज़ॉल्यूशन जांचें।
```powershell
Test-Connection -ComputerName google.com -Count 2
Resolve-DnsName google.com
```

### 2.5 उपयोगकर्ता और समूह प्रबंधन
स्थानीय उपयोगकर्ताओं और समूहों के प्रबंधन के लिए Cmdlets.

| Cmdlet | विवरण | उदाहरण |
|--------|-------------|---------|
| `New-LocalUser` | एक स्थानीय उपयोगकर्ता खाता बनाता है। | `New-LocalUser -Name "TestUser" -Password (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force)` |
| `Remove-LocalUser` | एक स्थानीय उपयोगकर्ता खाता हटाता है। | `Remove-LocalUser -Name "TestUser"` |
| `Get-LocalGroup` | स्थानीय समूहों की सूची बनाता है। | `Get-LocalGroup | Select-Object Name` |
| `Add-LocalGroupMember` | एक उपयोगकर्ता को स्थानीय समूह में जोड़ता है। | `Add-LocalGroupMember -Group "Administrators" -Member "TestUser"` |

**उदाहरण**: एक नया स्थानीय उपयोगकर्ता बनाएं और उसे Administrators समूह में जोड़ें।
```powershell
$password = ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force
New-LocalUser -Name "TestUser" -Password $password -FullName "Test User" -Description "Test account"
Add-LocalGroupMember -Group "Administrators" -Member "TestUser"
```

### 2.6 स्क्रिप्टिंग और ऑटोमेशन
PowerShell ऑटोमेशन के लिए स्क्रिप्टिंग में उत्कृष्ट है।

| Cmdlet | विवरण | उदाहरण |
|--------|-------------|---------|
| `Write-Output` | पाइपलाइन में डेटा आउटपुट करता है। | `Write-Output "Hello, World!"` |
| `ForEach-Object` | पाइपलाइन में आइटम्स के माध्यम से लूप करता है। | `Get-Process | ForEach-Object { $_.Name }` |
| `Where-Object` | शर्तों के आधार पर ऑब्जेक्ट्स को फ़िल्टर करता है। | `Get-Service | Where-Object { $_.Status -eq "Running" }` |
| `Invoke-Command` | स्थानीय या रिमोट कंप्यूटरों पर कमांड्स चलाता है। | `Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Process }` |
| `New-ScheduledTask` | एक शेड्यूल्ड टास्क बनाता है। | `New-ScheduledTask -Action (New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File C:\script.ps1") -Trigger (New-ScheduledTaskTrigger -Daily -At "3AM")` |

**उदाहरण**: चल रही प्रक्रियाओं को लॉग करने के लिए एक स्क्रिप्ट बनाएं।
```powershell
$logPath = "C:\Logs\ProcessLog.txt"
Get-Process | Select-Object Name, CPU, StartTime | Export-Csv -Path $logPath -NoTypeInformation
```

### 2.7 मॉड्यूल प्रबंधन
मॉड्यूल PowerShell की कार्यक्षमता का विस्तार करते हैं।

| Cmdlet | विवरण | उदाहरण |
|--------|-------------|---------|
| `Get-Module` | उपलब्ध या आयातित मॉड्यूल की सूची बनाता है। | `Get-Module -ListAvailable` |
| `Import-Module` | एक मॉड्यूल आयात करता है। | `Import-Module ActiveDirectory` |
| `Install-Module` | रिपॉजिटरी से एक मॉड्यूल इंस्टॉल करता है। | `Install-Module -Name PSWindowsUpdate -Force` |
| `Find-Module` | रिपॉजिटरी में मॉड्यूल खोजता है। | `Find-Module -Name *Azure*` |

**उदाहरण**: Windows अपडेट्स को प्रबंधित करने के लिए PSWindowsUpdate मॉड्यूल इंस्टॉल और आयात करें।
```powershell
Install-Module -Name PSWindowsUpdate -Force
Import-Module PSWindowsUpdate
Get-WUList
```

---

## 3. पाइपलाइन के साथ कार्य करना
पाइपलाइन (`|`) डेटा को क्रमिक रूप से प्रोसेस करने के लिए cmdlets को जोड़ने की अनुमति देता है। उदाहरण के लिए:
```powershell
Get-Process | Where-Object { $_.WorkingSet64 -gt 100MB } | Sort-Object WorkingSet64 -Descending | Select-Object Name, WorkingSet64 -First 5
```
यह कमांड:
1. सभी प्रक्रियाओं को प्राप्त करता है।
2. 100MB से अधिक मेमोरी का उपयोग करने वालों को फ़िल्टर करता है।
3. उन्हें मेमोरी उपयोग के आधार पर अवरोही क्रम में क्रमबद्ध करता है।
4. शीर्ष 5 प्रक्रियाओं का चयन करता है, उनका नाम और मेमोरी उपयोग प्रदर्शित करता है।

---

## 4. वेरिएबल्स, लूप्स और कंडीशंस
PowerShell ऑटोमेशन के लिए स्क्रिप्टिंग कंस्ट्रक्ट्स का समर्थन करता है।

### वेरिएबल्स
```powershell
$path = "C:\Logs"
$services = Get-Service
Write-Output "Log path is $path"
```

### लूप्स
- **ForEach-Object**:
```powershell
Get-Service | ForEach-Object { Write-Output $_.Name }
```
- **For लूप**:
```powershell
for ($i = 1; $i -le 5; $i++) { Write-Output "Iteration $i" }
```

### कंडीशंस
```powershell
$service = Get-Service -Name "wuauserv"
if ($service.Status -eq "Running") {
    Write-Output "Windows Update is running."
} else {
    Write-Output "Windows Update is stopped."
}
```

---

## 5. एरर हैंडलिंग
मजबूत स्क्रिप्ट्स के लिए `Try`, `Catch`, और `Finally` का उपयोग करें।
```powershell
Try {
    Get-Item -Path C:\NonExistentFile.txt -ErrorAction Stop
}
Catch {
    Write-Output "Error: $($_.Exception.Message)"
}
Finally {
    Write-Output "Operation completed."
}
```

---

## 6. रिमोट प्रबंधन
PowerShell `Invoke-Command` और `Enter-PSSession` का उपयोग करके रिमोट प्रशासन का समर्थन करता है।

**उदाहरण**: रिमोट कंप्यूटर पर एक कमांड चलाएं।
```powershell
Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Service | Where-Object { $_.Status -eq "Running" } }
```

**उदाहरण**: एक इंटरएक्टिव रिमोट सत्र शुरू करें।
```powershell
Enter-PSSession -ComputerName Server01
```

---

## 7. व्यावहारिक स्क्रिप्ट उदाहरण
नीचे डिस्क स्थान की निगरानी करने और यदि उपयोग 80% से अधिक हो तो अलर्ट करने के लिए एक नमूना स्क्रिप्ट है।

```powershell
$disks = Get-Disk
$threshold = 80

foreach ($disk in $disks) {
    $freeSpacePercent = ($disk.FreeSpace / $disk.Size) * 100
    if ($freeSpacePercent -lt (100 - $threshold)) {
        Write-Output "Warning: Disk $($disk.Number) is at $("{0:N2}" -f (100 - $freeSpacePercent))% capacity."
    }
}
```

---

## 8. प्रभावी PowerShell उपयोग के लिए सुझाव
- **गति के लिए एलियासेस का उपयोग करें**: सामान्य एलियासेस जैसे `dir` (`Get-ChildItem`), `ls` (`Get-ChildItem`), या `gci` (`Get-ChildItem`) इंटरएक्टिव सत्रों में समय बचाते हैं।
- **Get-Help**: विस्तृत दस्तावेज़ीकरण के लिए `Get-Help <cmdlet>` का उपयोग करें (उदाहरण के लिए, `Get-Help Get-Process -Full`)।
- **Update-Help**: `Update-Help` के साथ हेल्प फ़ाइलों को अपडेट रखें।
- **प्रोफाइल्स**: `$PROFILE` को एडिट करके अपने PowerShell वातावरण को कस्टमाइज़ करें (उदाहरण के लिए, `notepad $PROFILE`)।
- **टैब कम्पलीशन**: Cmdlets, पैरामीटर्स और पाथ को ऑटो-कम्पलीट करने के लिए `Tab` दबाएं।
- **वर्बोज़ आउटपुट का उपयोग करें**: विस्तृत निष्पादन जानकारी के लिए cmdlets में `-Verbose` जोड़ें।

---

## 9. अतिरिक्त संसाधन
- **आधिकारिक दस्तावेज़ीकरण**: [Microsoft PowerShell Docs](https://docs.microsoft.com/en-us/powershell/)
- **PowerShell गैलरी**: मॉड्यूल के लिए [PowerShell Gallery](https://www.powershellgallery.com/)।
- **कम्युनिटी**: रीयल-टाइम टिप्स और स्क्रिप्ट्स के लिए X या Stack Overflow जैसे फोरम पर पोस्ट देखें।
- **सीखना**: *PowerShell in Depth* या *Learn PowerShell in a Month of Lunches* जैसी किताबें।

---

PowerShell Microsoft द्वारा विकसित एक शक्तिशाली स्क्रिप्टिंग भाषा और कमांड-लाइन शेल है। इसका व्यापक रूप से टास्क ऑटोमेशन और कॉन्फ़िगरेशन प्रबंधन के लिए उपयोग किया जाता है। यहाँ `Get-NetTCPConnection` के अलावा कुछ सामान्यतः उपयोग किए जाने वाले PowerShell कमांड्स दिए गए हैं:

1.  **Get-Process**: स्थानीय कंप्यूटर या रिमोट कंप्यूटर पर चल रही प्रक्रियाओं के बारे में जानकारी प्राप्त करता है।
2.  **Get-Service**: स्थानीय या रिमोट कंप्यूटर पर सेवाएँ प्राप्त करता है।
3.  **Get-EventLog**: एप्लिकेशन, सुरक्षा और सिस्टम लॉग सहित इवेंट लॉ से इवेंट्स प्राप्त करता है।
4.  **Get-ChildItem**: एक या अधिक निर्दिष्ट स्थानों में आइटम्स और चाइल्ड आइटम्स प्राप्त करता है (कमांड प्रॉम्प्ट में `dir` के समान)।
5.  **Get-Content**: निर्दिष्ट स्थान पर आइटम की सामग्री प्राप्त करता है (कमांड प्रॉम्प्ट में `type` के समान)।
6.  **Set-ExecutionPolicy**: PowerShell निष्पादन नीति के लिए उपयोगकर्ता प्राथमिकता बदलता है।
7.  **Invoke-Command**: स्थानीय और रिमोट कंप्यूटरों पर कमांड्स चलाता है।
8.  **New-Item**: एक नया आइटम बनाता है, जैसे फ़ाइल या निर्देशिका।
9.  **Remove-Item**: निर्दिष्ट आइटम्स को हटाता है।
10. **Copy-Item**: एक आइटम को एक स्थान से दूसरे स्थान पर कॉपी करता है।
11. **Move-Item**: एक आइटम को एक स्थान से दूसरे स्थान पर ले जाता है।
12. **Rename-Item**: PowerShell प्रदाता नेमस्पेस में एक आइटम का नाम बदलता है।
13. **Get-Help**: PowerShell कमांड्स और अवधारणाओं के बारे में जानकारी प्रदर्शित करता है।
14. **Select-Object**: किसी ऑब्जेक्ट या ऑब्जेक्ट्स के सेट की निर्दिष्ट गुणों का चयन करता है।
15. **Where-Object**: उनके गुण मानों के आधार पर किसी संग्रह से ऑब्जेक्ट्स का चयन करता है।
16. **Sort-Object**: गुण मानों द्वारा ऑब्जेक्ट्स को क्रमबद्ध करता है।
17. **Export-Csv**: ऑब्जेक्ट्स को CSV स्ट्रिंग्स की एक श्रृंखला में परिवर्तित करता है और स्ट्रिंग्स को एक फ़ाइल में सहेजता है।
18. **Import-Csv**: एक CSV फ़ाइल आयात करता है और इसे ऑब्जेक्ट्स में परिवर्तित करता है।
19. **Start-Process**: स्थानीय कंप्यूटर पर एक या अधिक प्रक्रियाएँ शुरू करता है।
20. **Stop-Process**: एक या अधिक चल रही प्रक्रियाओं को रोकता है।

ये कमांड्स PowerShell के साथ आप जो कुछ भी कर सकते हैं उसके कुछ उदाहरण मात्र हैं। यह भाषा अत्यधिक विस्तार योग्य है, और आप जटिल कार्यों को स्वचालित करने के लिए कस्टम cmdlets और स्क्रिप्ट्स बना सकते हैं।