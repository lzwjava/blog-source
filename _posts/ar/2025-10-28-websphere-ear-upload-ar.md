---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح أخطاء تحميل ملفات EAR الكبيرة في WebSphere
translated: true
type: note
---

### فهم المشكلة
خطأ "تحميل ملف متعدد الأجزاء" (غالبًا ما يظهر كـ `org.apache.commons.fileupload.FileUploadException: Processing of multipart/form-data request failed. File too large (errno:27)`) يحدث عادة عند تحديث ملف EAR في IBM WebSphere Application Server (WAS) عبر وحدة التحكم الإدارية. هذا شائع مع ملفات EAR الكبيرة (مثلاً >20 ميجابايت) بسبب حدود تحميل الملفات، أو التخزين المؤقت، أو ذاكرة الكومة (Heap)، أو قيود موارد نظام التشغيل. المشكلة ليست في ملف EAR نفسه، ولكن في كيفية تعامل وحدة التحكم مع تحميل HTTP متعدد الأجزاء.

### إصلاحات سريعة لتجربتها أولاً
1. **انسخ ملف EAR إلى الخادم ونشره محلياً**:
   - استخدم FTP/SCP لنقل ملف EAR الجديد إلى مجلد على خادم WAS (مثلاً `/opt/IBM/WebSphere/AppServer/installableApps/`).
   - في وحدة التحكم الإدارية: انتقل إلى **التطبيقات > أنواع التطبيقات > تطبيقات مؤسسة WebSphere**.
   - اختر تطبيقك الموجود > **تحديث**.
   - اختر **استبدال أو إضافة وحدة مفردة** أو **استبدال التطبيق بالكامل**، ثم اختر **نظام الملفات المحلي** واشِر إلى مسار ملف EAR المنسوخ.
   - يتجاوز هذا طريقة التحميل متعدد الأجزاء عبر HTTP.

2. **زيادة حدود حجم الملف في نظام التشغيل (خوادم UNIX/Linux)**:
   - الخطأ `errno:27` يعني غالبًا أن الملف تجاوز حد ulimit للعملية.
   - نفّذ `ulimit -f` كمستخدم WAS (مثلاً `webadmin`) للتحقق من الحد الحالي.
   - عيّنه إلى "غير محدود": أضف `ulimit -f unlimited` إلى ملف تعريف shell للمستخدم (مثلاً `~/.bash_profile`) أو إلى سكريبت بدء تشغيل الخادم.
   - أعد تشغيل مدير النشر (dmgr) وحاول التحميل مرة أخرى.

### تغييرات التكوين في WAS
1. **زيادة حجم ذاكرة الكومة (Heap) لمدير النشر**:
   - ملفات EAR الكبيرة قد تسبب خطأ OutOfMemory أثناء المعالجة.
   - في وحدة التحكم الإدارية: **الخوادم > أنواع الخوادم > الخوادم الإدارية > مدير النشر**.
   - تحت **إدارة Java وعملية التشغيل > تعريف العملية > آلة Java الافتراضية**:
     - عيّن **حجم ذاكرة الكومة الابتدائية** إلى 1024 (أو أعلى، مثلاً 2048 لملفات EAR كبيرة جداً).
     - عيّن **أقصى حجم لذكرة الكومة** إلى 2048 (أو أعلى).
   - احفظ، أعد تشغيل dmgr، وحاول مرة أخرى.

2. **ضبط حدود جلسة HTTP أو حجم البيانات المرسلة (Post Size) (إذا كان ذلك ينطبق)**:
   - لحدود حاوية الويب: **الخوادم > أنواع الخوادم > خوادم تطبيقات WebSphere > [خادمك] > حاوية الويب > نُقَل HTTP**.
   - زِد **أقصى حجم للبيانات المرسلة** (بالبايت) إذا كان مضبوطاً على قيمة منخفضة.
   - ملاحظة: هذا يؤثر بشكل غير مباشر على تطبيق الويب لوحدة التحكم الإدارية.

### الحل الموصى به على المدى الطويل: استخدام wsadmin للتحديثات
للتحديثات الكبيرة أو المتكررة، تجنب استخدام وحدة التحكم تماماً – فهي غير موثوقة للملفات الكبيرة. استخدم أداة السكريبت wsadmin (Jython أو JACL) لتحديث التطبيق.

#### الخطوات:
1. انسخ ملف EAR الجديد إلى مسار يمكن للخادم الوصول إليه (مثلاً `/tmp/myapp.ear`).
2. شغّل wsadmin:  
   ```
   /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh -lang jython -user admin -password pass
   ```
3. نفّذ سكريبت Jython هذا للتحديث:  
   ```python
   AdminApp.update('MyAppName', 'app', [-Map ModulesToApps, '[-MapWebModToVH [[default_host MyContext virtual_host]] ]'], [-Operation update], [-appname MyAppName], [-MapModulesToServers [[MyModule MyServer]]], [-nodefaultoptions], [-preCompileJSPs false], [-contextroot MyContext], [-noTxImport], [-connType SERVER], [ -contenturi /tmp/myapp.ear ])
   AdminConfig.save()
   ```
   - استبدل `MyAppName` باسم تطبيقك، و`MyContext` بجذر السياق (context root)، و`MyServer` بالخادم/المجموعة المستهدفة (cluster)، و`/tmp/myapp.ear` بمسار ملف EAR.
4. زامِن العُقَد (Sync nodes) إذا كنت في بيئة مجمعة: `AdminControl.invoke(AdminControl.completeServers(), 'sync')`.
5. أعد تشغيل التطبيق: **التطبيقات > [التطبيق] > إعادة تشغيل**.

هذه الطريقة أسرع، وتتجنب حدود التحميل، ويمكن كتابتها سكريبتياً للأتمتة (مثلاً عبر Jenkins).

### نصائح إضافية
- **افحص السجلات**: راجع `SystemOut.log` و `SystemErr.log` في ملف تعريف dmgr للحصول على التفاصيل (مثلاً `/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/logs/dmgr/`).
- **اختبر باستخدام ملف EAR أصغر**: تحقق مما إذا كانت المشكلة متعلقة بالحجم عن طريق ضغط نسخة مصغرة.
- **إصدار WAS**: تأكد من أنك تستخدم إصداراً مدعوماً (مثلاً 8.5، 9.0). طَبِّق أحدث التحديثات إذا لزم الأمر.
- إذا استمر الخطأ (مثلاً، انتهت المهلة)، فزِد مهلة HTTP في **البيئة > خوادم تطبيقات الويب > [الخادم] > إعدادات الحاوية > إعدادات حاوية الويب > حاوية الويب > إدارة الجلسة > التكوين > انتهاء المهلة**.

إذا لم يحل أي من هذه الحلول المشكلة، شارك رسالة الخطأ الدقيقة وإصدار WAS للحصول على نصائح أكثر تخصيصاً.

### المراجع
- [Error during deploy of war file on Websphere Application Server 7.0](https://coderanch.com/t/459530/application-servers/Error-deploy-war-file-Websphere)
- [OutOfMemory errors while deploying applications in WebSphere Application Server](https://www.ibm.com/support/pages/outofmemory-errors-while-deploying-applications-websphere-application-server)
- [Maximum size limit of an Ear that can be deployed in WAS](https://stackoverflow.com/questions/58748076/maximum-size-limit-of-an-ear-that-can-be-deployed-in-was)
- [Deploying the enterprise archive (EAR) using the WebSphere Administrative Console](https://www.ibm.com/docs/en/configurepricequote/9.5.0?topic=cwaso-deploying-enterprise-archive-ear-using-websphere-admin-console)