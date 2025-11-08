---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: نظرة عامة على أداة IBM WebSphere wsadmin
translated: true
type: note
---

### نظرة عامة على wsadmin في IBM WebSphere Application Server (WAS)

أداة `wsadmin` هي واجهة سكريبت سطر أوامر لإدارة خادم تطبيقات WebSphere. تتيح لك أتمتة المهام مثل إدارة الخوادم، ونشر التطبيقات، وتهيئة الموارد، ومراقبة عمليات وقت التشغيل. يمكن كتابة السكريبتات بلغة Jython (المبنية على Python) أو JACL (المبنية على Tcl)، حيث تُستخدم Jython بشكل أكثر شيوعًا بسبب سهولة قراءتها.

- **`wsadmin.bat`**: تُستخدم في أنظمة Windows.
- **`wsadmin.sh`**: تُستخدم في أنظمة Unix/Linux/AIX.

توجد كلتا الأداتين في دليل `bin` لملف تعريف WebSphere (مثال: `<WAS_HOME>/profiles/<ProfileName>/bin/`) أو في دليل التثبيت الأساسي (`<WAS_HOME>/bin/`). يُوصى بتشغيلهما من دليل `bin` لملف التعريف لضمان بيئة التشغيل الصحيحة.

#### بدء wsadmin بشكل تفاعلي
يؤدي هذا إلى تشغيل shell حيث يمكنك إدخال الأوامر مباشرة.

**الصيغة:**
```
wsadmin[.bat|.sh] [options]
```

**مثال أساسي (Windows):**
```
cd C:\IBM\WebSphere\AppServer\profiles\AppSrv01\bin
wsadmin.bat -lang jython -user admin -password mypass
```

**مثال أساسي (Unix/Linux):**
```
cd /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin
./wsadmin.sh -lang jython -user admin -password mypass
```

- `-lang jython`: يحدد لغة Jython (استخدم `-lang jacl` لـ JACL).
- `-user` و `-password`: مطلوبان إذا كان الأمان الشامل مفعلًا (احذفهما إذا كان معطلًا).
- إذا تم حذفهما، فإنه يتصل بالخادم المحلي باستخدام موصل SOAP الافتراضي على المنفذ 8879 (أو RMI على المنفذ 2809).

بمجرد دخولك إلى موجه wsadmin (مثال: `wsadmin>`)، يمكنك تشغيل الأوامر باستخدام كائنات السكريبت:
- **AdminConfig**: لإجراء تغييرات على التهيئة (مثال: إنشاء موارد).
- **AdminControl**: لعمليات وقت التشغيل (مثال: بدء/إيقاف الخوادم).
- **AdminApp**: لنشر/تحديث التطبيقات.
- **AdminTask**: للمهام عالية المستوى (مثال: مزامنة العُقد).
- **Help**: للحصول على المساعدة المدمجة (مثال: `Help.help()`).

**أمثلة على الأوامر في الـ Shell:**
- سرد جميع الخوادم: `print AdminConfig.list('Server')`
- بدء تشغيل خادم: `AdminControl.invoke(AdminControl.completeObjectName('type=ServerIndex,process=server1,*'), 'start')`
- حفظ التغييرات: `AdminConfig.save()`
- خروج: `quit`

#### تشغيل ملف سكريبت
استخدم الخيار `-f` لتنفيذ سكريبت Jython (.py أو .jy) أو JACL (.jacl) بشكل غير تفاعلي.

**مثال على سكريبت (deployApp.py):**
```python
# الاتصال ونشر تطبيق
appName = 'MyApp'
AdminApp.install('/path/to/MyApp.ear', '[-appname ' + appName + ']')
AdminConfig.save()
print 'Application ' + appName + ' deployed successfully.'
```

**التشغيل على Windows:**
```
wsadmin.bat -lang jython -f /path/to/deployApp.py -user admin -password mypass
```

**التشغيل على Unix/Linux:**
```
./wsadmin.sh -lang jython -f /path/to/deployApp.py -user admin -password mypass
```

#### تشغيل أمر واحد
استخدم الخيار `-c` للأوامر المنفردة (مفيد في ملفات الدُفعات أو الأتمتة).

**مثال (مقتطف من ملف دُفعة Windows):**
```batch
@echo off
call "C:\IBM\WebSphere\AppServer\profiles\AppSrv01\bin\wsadmin.bat" -lang jython -c "print AdminConfig.list('Server')" -user admin -password mypass
```

**مثال (مقتطف من سكريبت shell لنظام Unix):**
```bash
#!/bin/bash
./wsadmin.sh -lang jython -c "print AdminConfig.list('Server')" -user admin -password mypass
```

#### الخيارات الرئيسية

| الخيار | الوصف | مثال |
|--------|-------------|---------|
| `-conntype` | نوع الموصل: `SOAP` (افتراضي، المنفذ 8879) أو `RMI` (المنفذ 2809). | `-conntype RMI` |
| `-host` | الخادم البعيد للاتصال به. | `-host myhost.example.com` |
| `-port` | منفذ الموصل. | `-port 8879` |
| `-tracefile` | تسجيل الناتج في ملف. | `-tracefile wsadmin.log` |
| `-profile` | تشغيل سكريبت ملف تعريف قبل السكريبت الرئيسي. | `-profile init.py` |
| `-c` | تنفيذ أمر واحد (غير تفاعلي). | `-c "AdminConfig.save()"` |
| `-f` | تنفيذ ملف سكريبت. | `-f myscript.py` |
| `-job` | تشغيل أمر مدير المهام. | `-job deploy.xml` |

#### نصائح وأفضل الممارسات
- **الأمان**: إذا كان الأمان الشامل معطلًا، احذف `-user` و `-password`. للإعدادات الآمنة، استخدم بيانات اعتماد مشفرة أو ملفات مفتاح.
- **وضع العميل الخفيف**: للإدارة عن بُعد بدون تثبيت كامل لـ WAS، استخدم `wsadmin -conntype NONE` مع ملفات JAR الخاصة بالعميل الخفيف (مثال: `com.ibm.ws.admin.client_*.jar`).
- **الأداء**: للأوامر المتعددة، استخدم سكريبت واحد بـ `-f` بدلاً من استدعاءات `-c` متكررة لتجنب حمل JVM.
- **معالجة الأخطاء**: اطلب دائمًا `AdminConfig.save()` بعد تغييرات التهيئة. استخدم try-except في Jython لزيادة المتانة.
- **إنشاء الأوامر**: في وحدة تحكم إدارة WAS، نفّذ إجراءً وانقر على "View administrative scripting command for last action" للحصول على أمر wsadmin المكافئ.
- **ملاحظات الإصدار**: السلوك متسق عبر إصدارات WAS 8.5+ و 9.0+، ولكن تحقق من وثائق IBM للحصول على تفاصيل خاصة بالإصدار (مثال: Jython 2.7 في الإصدارات الأحدث).

للحصول على استخدامات متقدمة، استكشف كائن AdminTask للحصول على أوامر مبسطة مثل `AdminTask.importFile('path/to/file')`.

### المراجع
- [wsadmin scripting tool - IBM Docs](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-wsadmin-tool)
- [Getting started with wsadmin scripting - IBM Docs](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.doc/ae/txml_script.html)
- [WAS - wsadmin (Jython) Tutorial](http://www.mtitek.com/tutorials/websphere/wsadmin_jython.php)
- [IBM WebSphere - Getting Started with wsadmin](https://www.freekb.net/Article?id=1563)
- [WSADMIN Tutorial – Part1](https://websphereapplicationservernotes.wordpress.com/2012/12/25/wsadmin-tutorial-part1/)