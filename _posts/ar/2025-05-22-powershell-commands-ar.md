---
audio: false
generated: true
lang: ar
layout: post
title: دليل أوامر باورشيل
translated: true
type: note
---

## مقدمة إلى PowerShell

PowerShell هو إطار عمل لإدارة التكوين وأتمتة المهام من Microsoft، يتكون من shell سطر الأوامر ولغة برمجة نصية. وهو مبني على .NET Framework (و .NET Core في الإصدارات الأحدث)، مما يمكن المسؤولين من أداء مهام معقدة عبر أنظمة Windows وLinux وmacOS.

أوامر PowerShell، المعروفة باسم **cmdlets** (تُنطق "command-lets")، تتبع اصطلاح تسمية `الفعل-الإسم` (مثال: `Get-Process`، `Set-Item`). يغطي هذا الدليل cmdlets الأساسية، مصنفة حسب الوظيفة، مع أمثلة لتوضيح استخدامها.

---

## 1. المفاهيم الأساسية لـ PowerShell

قبل الخوض في الأوامر، من الضروري فهم المفاهيم الأساسية:
- **Cmdlets**: أوامر خفيفة الوزن تؤدي وظائف محددة.
- **Pipelines**: تسمح بتمرير مخرجات cmdlet واحدة كمدخل لـ cmdlet أخرى باستخدام عامل التشغيل `|`.
- **الوحدات النمطية (Modules)**: مجموعات من cmdlets والنصوص البرمجية والدوال التي توسع وظائف PowerShell.
- **المزودون (Providers)**: واجهات للوصول إلى مخازن البيانات (مثل نظام الملفات، السجل) كما لو كانت محركات أقراص.
- **الكائنات (Objects)**: يعمل PowerShell مع الكائنات، وليس النص العادي، مما يمكن من معالجة البيانات المنظمة.

---

## 2. الـ Cmdlets الأساسية حسب الفئة

### 2.1 معلومات النظام

هذه الـ cmdlets تسترد معلومات حول النظام والعمليات والخدمات.

| الأمر | الوصف | مثال |
|--------|-------------|---------|
| `Get-ComputerInfo` | يسترد تفاصيل أجهزة وبرمجيات النظام. | `Get-ComputerInfo | Select-Object WindowsProductName, OsVersion` |
| `Get-Process` | يسرد العمليات قيد التشغيل. | `Get-Process | Where-Object {$_.CPU -gt 1000}` |
| `Get-Service` | يعرض الخدمات على النظام. | `Get-Service | Where-Object {$_.Status -eq "Running"}` |
| `Get-HotFix` | يسرد تحديثات Windows المثبتة. | `Get-HotFix | Sort-Object InstalledOn -Descending` |

**مثال**: سرد جميع العمليات قيد التشغيل مرتبة حسب استخدام وحدة المعالجة المركزية.
```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object Name, CPU, Id -First 5
```

### 2.2 إدارة الملفات والمجلدات

تعامل PowerShell نظام الملفات كمزود، مما يسمح بالتنقل بشكل مشابه لمحرك الأقراص.

| الأمر | الوصف | مثال |
|--------|-------------|---------|
| `Get-Item` | يسترد الملفات أو المجلدات. | `Get-Item C:\Users\*.txt` |
| `Set-Item` | يعدل خصائص العنصر (مثل سمات الملف). | `Set-Item -Path C:\test.txt -Value "محتوى جديد"` |
| `New-Item` | ينشئ ملفًا أو مجلدًا جديدًا. | `New-Item -Path C:\Docs -Name Report.txt -ItemType File` |
| `Remove-Item` | يحذف الملفات أو المجلدات. | `Remove-Item C:\Docs\OldFile.txt` |
| `Copy-Item` | ينسخ الملفات أو المجلدات. | `Copy-Item C:\Docs\Report.txt D:\Backup` |
| `Move-Item` | ينقل الملفات أو المجلدات. | `Move-Item C:\Docs\Report.txt C:\Archive` |

**مثال**: إنشاء مجلد وملف، ثم نسخه إلى موقع آخر.
```powershell
New-Item -Path C:\Temp -Name MyFolder -ItemType Directory
New-Item -Path C:\Temp\MyFolder -Name Test.txt -ItemType File
Copy-Item C:\Temp\MyFolder\Test.txt C:\Backup
```

### 2.3 إدارة النظام

Cmdlets لإدارة إعدادات النظام والخدمات والمستخدمين.

| الأمر | الوصف | مثال |
|--------|-------------|---------|
| `Start-Service` | يبدأ خدمة. | `Start-Service -Name "wuauserv"` |
| `Stop-Service` | يوقف خدمة. | `Stop-Service -Name "wuauserv"` |
| `Restart-Computer` | يعيد تشغيل النظام. | `Restart-Computer -Force` |
| `Get-EventLog` | يسترد إدخالات سجل الأحداث. | `Get-EventLog -LogName System -Newest 10` |
| `Set-ExecutionPolicy` | يحدد سياسة تنفيذ النصوص البرمجية. | `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |

**مثال**: التحقق من حالة خدمة Windows Update وبدئها إذا كانت متوقفة.
```powershell
$service = Get-Service -Name "wuauserv"
if ($service.Status -eq "Stopped") {
    Start-Service -Name "wuauserv"
}
```

### 2.4 إدارة الشبكة

Cmdlets لتكوين الشبكة والتشخيص.

| الأمر | الوصف | مثال |
|--------|-------------|---------|
| `Test-Connection` | يرسل إشارة ping إلى مضيف بعيد. | `Test-Connection google.com` |
| `Get-NetAdapter` | يسرد محولات الشبكة. | `Get-NetAdapter | Select-Object Name, Status` |
| `Get-NetIPAddress` | يسترد تكوينات عناوين IP. | `Get-NetIPAddress -AddressFamily IPv4` |
| `Resolve-DnsName` | يحل أسماء DNS. | `Resolve-DnsName www.google.com` |

**مثال**: إرسال إشارة ping إلى خادم والتحقق من حله عبر DNS.
```powershell
Test-Connection -ComputerName google.com -Count 2
Resolve-DnsName google.com
```

### 2.5 إدارة المستخدمين والمجموعات

Cmdlets لإدارة المستخدمين والمجموعات المحلية.

| الأمر | الوصف | مثال |
|--------|-------------|---------|
| `New-LocalUser` | ينشئ حساب مستخدم محلي. | `New-LocalUser -Name "TestUser" -Password (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force)` |
| `Remove-LocalUser` | يحذف حساب مستخدم محلي. | `Remove-LocalUser -Name "TestUser"` |
| `Get-LocalGroup` | يسرد المجموعات المحلية. | `Get-LocalGroup | Select-Object Name` |
| `Add-LocalGroupMember` | يضيف مستخدمًا إلى مجموعة محلية. | `Add-LocalGroupMember -Group "Administrators" -Member "TestUser"` |

**مثال**: إنشاء مستخدم محلي جديد وإضافته إلى مجموعة المسؤولين.
```powershell
$password = ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force
New-LocalUser -Name "TestUser" -Password $password -FullName "Test User" -Description "حساب اختبار"
Add-LocalGroupMember -Group "Administrators" -Member "TestUser"
```

### 2.6 البرمجة النصية والأتمتة

يتفوق PowerShell في البرمجة النصية للأتمتة.

| الأمر | الوصف | مثال |
|--------|-------------|---------|
| `Write-Output` | يخرج البيانات إلى خط الأنابيب. | `Write-Output "Hello, World!"` |
| `ForEach-Object` | يحلق عبر العناصر في خط الأنابيب. | `Get-Process | ForEach-Object { $_.Name }` |
| `Where-Object` | يرشح الكائنات بناءً على الشروط. | `Get-Service | Where-Object { $_.Status -eq "Running" }` |
| `Invoke-Command` | يشغل الأوامر على أجهزة الكمبيوتر المحلية أو البعيدة. | `Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Process }` |
| `New-ScheduledTask` | ينشئ مهمة مجدولة. | `New-ScheduledTask -Action (New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File C:\script.ps1") -Trigger (New-ScheduledTaskTrigger -Daily -At "3AM")` |

**مثال**: إنشاء نص برمجي لتسجيل العمليات قيد التشغيل إلى ملف.
```powershell
$logPath = "C:\Logs\ProcessLog.txt"
Get-Process | Select-Object Name, CPU, StartTime | Export-Csv -Path $logPath -NoTypeInformation
```

### 2.7 إدارة الوحدات النمطية

الوحدات النمطية توسع وظائف PowerShell.

| الأمر | الوصف | مثال |
|--------|-------------|---------|
| `Get-Module` | يسرد الوحدات النمطية المتاحة أو المستوردة. | `Get-Module -ListAvailable` |
| `Import-Module` | يستورد وحدة نمطية. | `Import-Module ActiveDirectory` |
| `Install-Module` | يثبت وحدة نمطية من مستودع. | `Install-Module -Name PSWindowsUpdate -Force` |
| `Find-Module` | يبحث عن وحدات نمطية في مستودع. | `Find-Module -Name *Azure*` |

**مثال**: تثبيت واستيراد وحدة PSWindowsUpdate لإدارة تحديثات Windows.
```powershell
Install-Module -Name PSWindowsUpdate -Force
Import-Module PSWindowsUpdate
Get-WUList
```

---

## 3. العمل مع خطوط الأنابيب

خط الأنابيب (`|`) يسمح لسلسلة cmdlets بمعالجة البيانات بشكل تسلسلي. على سبيل المثال:
```powershell
Get-Process | Where-Object { $_.WorkingSet64 -gt 100MB } | Sort-Object WorkingSet64 -Descending | Select-Object Name, WorkingSet64 -First 5
```
هذا الأمر:
1. يسترد جميع العمليات.
2. يرشح تلك التي تستخدم أكثر من 100 ميجابايت من الذاكرة.
3. يرتبها حسب استخدام الذاكرة بترتيب تنازلي.
4. يختار أفضل 5 عمليات، مع عرض اسمها واستخدام الذاكرة.

---

## 4. المتغيرات، الحلقات، والشروط

يدعم PowerShell تراكيب البرمجة النصية للأتمتة.

### المتغيرات
```powershell
$path = "C:\Logs"
$services = Get-Service
Write-Output "مسار السجل هو $path"
```

### الحلقات
- **ForEach-Object**:
```powershell
Get-Service | ForEach-Object { Write-Output $_.Name }
```
- **حلقة For**:
```powershell
for ($i = 1; $i -le 5; $i++) { Write-Output "التكرار $i" }
```

### الشروط
```powershell
$service = Get-Service -Name "wuauserv"
if ($service.Status -eq "Running") {
    Write-Output "Windows Update قيد التشغيل."
} else {
    Write-Output "Windows Update متوقف."
}
```

---

## 5. معالجة الأخطاء

استخدم `Try`، `Catch`، و `Finally` للنصوص البرمجية القوية.
```powershell
Try {
    Get-Item -Path C:\NonExistentFile.txt -ErrorAction Stop
}
Catch {
    Write-Output "خطأ: $($_.Exception.Message)"
}
Finally {
    Write-Output "اكتملت العملية."
}
```

---

## 6. الإدارة عن بُعد

يدعم PowerShell الإدارة عن بُعد باستخدام `Invoke-Command` و `Enter-PSSession`.

**مثال**: تشغيل أمر على كمبيوتر بعيد.
```powershell
Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Service | Where-Object { $_.Status -eq "Running" } }
```

**مثال**: بدء جلسة تفاعلية عن بُعد.
```powershell
Enter-PSSession -ComputerName Server01
```

---

## 7. مثال عملي على نص برمجي

أدناه نموذج نص برمجي لمراقبة مساحة القرص والتنبيه إذا تجاوز الاستخدام 80%.

```powershell
$disks = Get-Disk
$threshold = 80

foreach ($disk in $disks) {
    $freeSpacePercent = ($disk.FreeSpace / $disk.Size) * 100
    if ($freeSpacePercent -lt (100 - $threshold)) {
        Write-Output "تحذير: القرص $($disk.Number) عند $("{0:N2}" -f (100 - $freeSpacePercent))% سعة."
    }
}
```

---

## 8. نصائح للاستخدام الفعال لـ PowerShell

- **استخدم الأسماء المستعارة للسرعة**: الأسماء المستعارة الشائعة مثل `dir` (`Get-ChildItem`)، `ls` (`Get-ChildItem`)، أو `gci` (`Get-ChildItem`) توفر الوقت في الجلسات التفاعلية.
- **Get-Help**: استخدم `Get-Help <cmdlet>` للحصول على وثائق مفصلة (مثال: `Get-Help Get-Process -Full`).
- **Update-Help**: حافظ على تحديث ملفات المساعدة باستخدام `Update-Help`.
- **الملفات الشخصية (Profiles)**: خصص بيئة PowerShell الخاصة بك عن طريق تحرير `$PROFILE` (مثال: `notepad $PROFILE`).
- **الإكمال التلقائي (Tab Completion)**: اضغط `Tab` للإكمال التلقائي لـ cmdlets والمعلمات والمسارات.
- **استخدم المخرجات التفصيلية**: أضف `-Verbose` إلى cmdlets للحصول على معلومات تنفيذ مفصلة.

---

## 9. موارد إضافية

- **التوثيق الرسمي**: [Microsoft PowerShell Docs](https://docs.microsoft.com/en-us/powershell/)
- **معرض PowerShell**: [PowerShell Gallery](https://www.powershellgallery.com/) للوحدات النمطية.
- **المجتمع**: تحقق من المنشورات على X أو المنتديات مثل Stack Overflow للحصول على نصائح ونصوص برمجية فورية.
- **التعلم**: كتب مثل *PowerShell in Depth* أو *Learn PowerShell in a Month of Lunches*.

---

PowerShell هي لغة برمجة نصية و shell سطر أوامر قوية طورتها Microsoft. تُستخدم على نطاق واسع لأتمتة المهام وإدارة التكوين. فيما يلي بعض أوامر PowerShell شائعة الاستخدام بخلاف `Get-NetTCPConnection`:

1.  **Get-Process**: يسترد معلومات حول العمليات التي تعمل على الكمبيوتر المحلي أو الكمبيوتر البعيد.
2.  **Get-Service**: يحصل على الخدمات على كمبيوتر محلي أو بعيد.
3.  **Get-EventLog**: يسترد الأحداث من سجلات الأحداث، بما في ذلك سجلات التطبيقات والأمان والنظام.
4.  **Get-ChildItem**: يحصل على العناصر والعناصر الفرعية في موقع واحد أو أكثر (مشابه لـ `dir` في موجه الأوامر).
5.  **Get-Content**: يحصل على محتوى العنصر في الموقع المحدد (مشابه لـ `type` في موجه الأوامر).
6.  **Set-ExecutionPolicy**: يغير تفضيل المستخدم لسياسة تنفيذ PowerShell.
7.  **Invoke-Command**: يشغل الأوامر على أجهزة الكمبيوتر المحلية والبعيدة.
8.  **New-Item**: ينشئ عنصرًا جديدًا، مثل ملف أو دليل.
9.  **Remove-Item**: يحذف العناصر المحددة.
10. **Copy-Item**: ينسخ عنصرًا من موقع إلى آخر.
11. **Move-Item**: ينقل عنصرًا من موقع إلى آخر.
12. **Rename-Item**: يعيد تسمية عنصر في مساحة اسم موفر PowerShell.
13. **Get-Help**: يعرض معلومات حول أوامر ومفاهيم PowerShell.
14. **Select-Object**: يختار خصائص محددة لكائن أو مجموعة كائنات.
15. **Where-Object**: يختار كائنات من مجموعة بناءً على قيم خصائصها.
16. **Sort-Object**: يرتب الكائنات حسب قيم الخصائص.
17. **Export-Csv**: يحول الكائنات إلى سلسلة من سلاسل CSV ويحفظ السلاسل في ملف.
18. **Import-Csv**: يستورد ملف CSV ويحوله إلى كائنات.
19. **Start-Process**: يبدأ عملية واحدة أو أكثر على الكمبيوتر المحلي.
20. **Stop-Process**: يوقف عملية واحدة أو أكثر قيد التشغيل.

هذه الأوامر ليست سوى أمثلة قليلة لما يمكنك فعله باستخدام PowerShell. اللغة قابلة للتوسيع بشكل كبير، ويمكنك إنشاء cmdlets مخصصة ونصوص برمجية لأتمتة المهام المعقدة.