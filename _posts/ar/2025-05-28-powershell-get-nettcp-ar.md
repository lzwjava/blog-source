---
audio: false
generated: true
lang: ar
layout: post
title: استخدام PowerShell لـ Get-NetTCPConnection
translated: true
type: note
---

يسترجع cmdlet `Get-NetTCPConnection` في PowerShell معلومات حول اتصالات TCP على نظام Windows. وهو جزء من وحدة `NetTCPIP`، المتوفرة في Windows 8/Windows Server 2012 والإصدارات الأحدث. فيما يلي دليل موجز حول كيفية استخدامه:

### الاستخدام الأساسي
شغِّل `Get-NetTCPConnection` لإدراج جميع اتصالات TCP النشطة:

```powershell
Get-NetTCPConnection
```

هذا يُرجع تفاصيل مثل LocalAddress و LocalPort و RemoteAddress و RemotePort و State و OwningProcess.

### المعلمات الشائعة
- **-State**: فرز حسب حالة الاتصال (مثل Established، Listening، TimeWait).
  ```powershell
  Get-NetTCPConnection -State Established
  ```
- **-LocalPort**: فرز حسب رقم المنفذ المحلي.
  ```powershell
  Get-NetTCPConnection -LocalPort 80
  ```
- **-RemoteAddress**: فرز حسب عنوان IP البعيد.
  ```powershell
  Get-NetTCPConnection -RemoteAddress 192.168.1.1
  ```
- **-RemotePort**: فرز حسب المنفذ البعيد.
  ```powershell
  Get-NetTCPConnection -RemotePort 443
  ```
- **-OwningProcess**: فرز حسب معرّف العملية (PID) التي تمتلك الاتصال.
  ```powershell
  Get-NetTCPConnection -OwningProcess 1234
  ```

### الجمع بين عوامل التصفية
يمكنك الجمع بين المعلمات للحصول على نتائج أكثر تحديدًا:
```powershell
Get-NetTCPConnection -State Established -LocalPort 80
```

### عرض خصائص محددة
استخدم `Select-Object` لعرض الخصائص المطلوبة فقط:
```powershell
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### العثور على تفاصيل العملية
لتحديد العملية وراء الاتصال، اجمعها مع `Get-Process`:
```powershell
Get-NetTCPConnection -LocalPort 80 | ForEach-Object { Get-Process -Id $_.OwningProcess }
```

### فرز وتنسيق المخرجات
رتب النتائج (مثلًا حسب LocalPort) وقم بتنسيقها كجدول:
```powershell
Get-NetTCPConnection | Sort-Object LocalPort | Format-Table LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### أمثلة عملية
1. **إدراج جميع اتصالات الاستماع:**
   ```powershell
   Get-NetTCPConnection -State Listening
   ```
2. **البحث عن اتصالات بخادم بعيد محدد:**
   ```powershell
   Get-NetTCPConnection -RemoteAddress "8.8.8.8"
   ```
3. **التحقق من العملية التي تستخدم منفذًا محددًا:**
   ```powershell
   $connection = Get-NetTCPConnection -LocalPort 8080
   Get-Process -Id $connection.OwningProcess
   ```

### ملاحظات
- **امتيازات المسؤول**: قد تتطلب بعض التفاصيل (مثل OwningProcess للعمليات النظامية) تشغيل PowerShell كمسؤول.
- **IPv4/IPv6**: يقوم الـ cmdlet بالتعامل مع اتصالات IPv4 و IPv6.
- **تصدير النتائج**: احفظ المخرجات إلى ملف باستخدام `Export-Csv`:
  ```powershell
  Get-NetTCPConnection | Export-Csv -Path "tcp_connections.csv" -NoTypeInformation
  ```

لمزيد من التفاصيل، شغِّل:
```powershell
Get-Help Get-NetTCPConnection -Full
```

إذا كنت بحاجة إلى أمثلة محددة أو لديك حالة استخدام معينة، دعني أعلم!