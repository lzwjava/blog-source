---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إنشاء خادم تطبيقات ويب سبير الصحيح
translated: true
type: note
---

لا، الأمر `nodeName -name serverName admin create applciation server` (مع ملاحظة الخطأ المطبعي في "applciation") غير صحيح لإنشاء خادم تطبيقات في IBM WebSphere Application Server (WAS) باستخدام سكريبت wsadmin.

### الصيغة الصحيحة
يستخدم الأمر الصحيح طريقة `AdminTask.createApplicationServer` في Jython (لغة السكريبت الموصى بها لـ wsadmin). وهي تتطلب:
- **اسم العقدة** كوسيطة أولى (سلسلة نصية).
- **قائمة من الخيارات** كوسيطة ثانية، تشمل `-name` لاسم الخادم.

**مثال أساسي:**
```jython
AdminTask.createApplicationServer('YourNodeName', ['-name', 'YourServerName'])
```

- استبدل `'YourNodeName'` باسم العقدة الفعلي (مثال: `ndnode1`).
- استبدل `'YourServerName'` باسم الخادم المطلوب (مثال: `appServer1`).
- يمكن إضافة معلمات اختيارية إلى القائمة، مثل `'-templateName', 'default'` لاستخدام قالب خادم افتراضي.

### خطوات التشغيل
1. ابدأ wsadmin في وضع Jython: `./wsadmin.sh -lang jython -user admin -password pass`.
2. نفذ الأمر أعلاه.
3. احفظ التكوين: `AdminConfig.save()`.
4. اختر الخروج: `quit`.

هذا ينشئ خادم تطبيقات أساسي على العقدة المحددة. للحصول على المزيد من الخيارات (مثال: المنافذ، إعدادات JVM)، راجع وثائق AdminTask الكاملة.

[مجموعة أوامر إدارة الخادم لكائن AdminTask](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-servermanagement-command-group-admintask-object)  
[إنشاء خادم باستخدام السكريبت](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-creating-server-using)