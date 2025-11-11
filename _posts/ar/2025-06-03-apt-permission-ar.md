---
audio: false
generated: true
lang: ar
layout: post
title: تثبيت الحزم في لينكس
translated: true
type: note
---

تشير رسالة الخطأ التي تراها إلى أن مدير الحزم (`apt`) واجه مشكلة في الأذونات أثناء محاولته الوصول إلى ملف الحزمة الذي تم تنزيله. على وجه التحديد، يحاول الوصول إلى الحزمة كمسؤول (root)، لكنه لا يستطيع لأن الأمر يعمل بأذونات مرتفعة بطريقة تقيد الوصول إلى الملف.

لحل هذه المشكلة، لديك خياران:

### الخيار 1: استخدام دليل مختلف
انقل حزمة `.deb` إلى دليل مختلف وحاول تثبيتها من هناك. على سبيل المثال:

```bash
sudo mv /home/lzw/Downloads/TencentMeeting_0300000000_3.19.2.400_x86_64_default.publish.officialwebsite.deb /tmp/
sudo apt install /tmp/TencentMeeting_0300000000_3.19.2.400_x86_64_default.publish.officialwebsite.deb
```

### الخيار 2: تعديل الأذونات مؤقتًا
غيّر ملكية ملف حزمة `.deb` مؤقتًا للسماح لأمر `apt` بالوصول إليه:

```bash
sudo chown root:root /home/lzw/Downloads/TencentMeeting_0300000000_3.19.2.400_x86_64_default.publish.officialwebsite.deb
sudo apt install /home/lzw/Downloads/TencentMeeting_0300000000_3.19.2.400_x86_64_default.publish.officialwebsite.deb
```

### الخيار 3: إعادة تنزيل الحزمة مرة أخرى
إذا كنت تفضل، يمكنك أيضًا محاولة إعادة تنزيل الحزمة والتأكد من أن لديك الأذونات الصحيحة:

1. احذف حزمة `.deb` الموجودة إذا كانت موجودة:
   ```bash
   rm /home/lzw/Downloads/TencentMeeting_0300000000_3.19.2.400_x86_64_default.publish.officialwebsite.deb
   ```

2. أعد تنزيل الحزمة من الموقع الرسمي أو المصدر وحاول التثبيت مرة أخرى.

### مثال:
```bash
sudo apt install /path/to/downloaded/package.deb
```

### نصائح إضافية:
- تأكد من أن دليل العمل الحالي لديه الأذونات اللازمة للوصول إلى الحزمة التي تم تنزيلها.
- تحقق من أن الحزمة التي قمت بتنزيلها هي بالفعل حزمة `.deb` صالحة وغير تالفة.

اتباع هذه الخطوات يجب أن يسمح لـ `apt` بفك حزمة Tencent Meeting وتثبيتها بنجاح.