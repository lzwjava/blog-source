---
audio: false
generated: true
lang: ar
layout: post
title: دمج مُحلل YourKit مع WebSphere Liberty على Windows
translated: true
type: note
---

يتضمن استخدام YourKit Java Profiler مع خادم WebSphere Liberty على Windows دمج وكيل YourKit في JVM الخاص بـ WebSphere Liberty وتكوينه لإجراء التحليل الأدائي. فيما يلي الخطوات اللازمة لإعداد ذلك، بناءً على المعلومات المتاحة وأفضل الممارسات للتكامل بين YourKit و WebSphere Liberty:

### المتطلبات الأساسية
- **YourKit Java Profiler**: مثبت على جهاز Windows الخاص بك. قم بتنزيله من [الموقع الرسمي لـ YourKit](https://www.yourkit.com/) وتأكد من أن لديك ترخيصًا صالحًا أو مفتاح تجربة.
- **WebSphere Liberty**: مثبت ويعمل على نظام Windows الخاص بك. تأكد من أن لديك حق الوصول الإداري إلى ملفات تكوين الخادم.
- **Java JDK**: يستخدم WebSphere Liberty وقت تشغيل Java (IBM JDK أو OpenJDK). تأكد من أن إصدار JDK متوافق مع YourKit (يدعم YourKit Java 5 والإصدارات الأحدث، ولكن تحقق من التوافق مع إصدارك المحدد).
- **الصلاحيات الإدارية**: مطلوبة لتعديل ملفات تكوين WebSphere Liberty.

### دليل خطوة بخطوة

1. **تثبيت YourKit Java Profiler**
   - قم بتنزيل وتثبيت YourKit Java Profiler لنظام Windows من [موقع YourKit](https://www.yourkit.com/download).
   - لاحظ دليل التثبيت، حيث ستحتاج إلى المسار إلى مكتبة وكيل YourKit (`yjpagent.dll`).

2. **تحديد موقع وكيل YourKit**
   - عادةً ما يوجد وكيل YourKit لنظام Windows في:
     ```
     C:\Program Files\YourKit-Java-Profiler-<version>\bin\win64\yjpagent.dll
     ```
     (استخدم `win32` بدلاً من `win64` إذا كنت تستخدم JVM 32-bit.)
   - تأكد من أن الوكيل يتطابق مع بنية JVM (32-bit أو 64-bit) التي يستخدمها WebSphere Liberty.

3. **تكوين WebSphere Liberty لاستخدام وكيل YourKit**
   - **حدد موقع ملف `jvm.options`**:
     - انتقل إلى دليل تكوين خادم WebSphere Liberty الخاص بك، عادةً:
       ```
       <LIBERTY_INSTALL_DIR>\usr\servers\<server_name>\jvm.options
       ```
       استبدل `<LIBERTY_INSTALL_DIR>` بالمسار إلى تثبيت WebSphere Liberty (مثل `C:\wlp`)، و `<server_name>` باسم خادمك (مثل `defaultServer`).
     - إذا كان ملف `jvm.options` غير موجود، فقم بإنشائه في دليل الخادم.
   - **أضف مسار وكيل YourKit**:
     - افتح `jvm.options` في محرر نصوص بصلاحيات إدارية.
     - أضف السطر التالي لتضمين وكيل YourKit:
       ```
       -agentpath:C:\Program Files\YourKit-Java-Profiler-<version>\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
       ```
       - استبدل `<version>` بإصدار YourKit الخاص بك (مثل `2023.9`).
       - تقلل الخيارات (`disablestacktelemetry`, `disableexceptiontelemetry`, `probe_disable=*`) من الحمل عن طريق تعطيل القياس عن بُعد غير الضروري. يضمن `delay=10000` بدء الوكيل بعد تهيئة الخادم، ويحدد `sessionname=WebSphereLiberty` جلسة التحليل الأدائي.
       - مثال:
         ```
         -agentpath:C:\Program Files\YourKit-Java-Profiler-2023.9\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
         ```
   - **احفظ الملف**: تأكد من أن لديك أذونات الكتابة لملف `jvm.options`.

4. **التحقق من توافق JVM**
   - غالبًا ما يستخدم WebSphere Liberty IBM JDK أو OpenJDK. YourKit متوافق مع كليهما، ولكن إذا واجهت مشكلات (مثل `NoSuchMethodError` كما هو مذكور في بعض حالات IBM JDK)، أضف `probe_disable=*` إلى مسار الوكيل لتعطيل المسابر التي قد تسبب تعارضات مع IBM JDK.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=8042)
   - تحقق من إصدار Java المستخدم بواسطة Liberty:
     ```
     <LIBERTY_INSTALL_DIR>\java\bin\java -version
     ```
     تأكد من أنه مدعوم من قبل YourKit (Java 5 أو إصدار أحدث للإصدارات القديمة؛ تدعم الإصدارات الحديثة Java 8+).

5. **بدء تشغيل WebSphere Liberty**
   - ابدأ تشغيل خادم WebSphere Liberty الخاص بك كالمعتاد:
     ```
     <LIBERTY_INSTALL_DIR>\bin\server start <server_name>
     ```
     مثال:
     ```
     C:\wlp\bin\server start defaultServer
     ```
   - تحقق من سجلات الخادم (`<LIBERTY_INSTALL_DIR>\usr\servers\<server_name>\logs\console.log` أو `messages.log`) للبحث عن أي أخطاء متعلقة بوكيل YourKit.
   - ابحث عن سجل وكيل YourKit في:
     ```
     %USERPROFILE%\.yjp\log\<session_name>-<pid>.log
     ```
     مثال:
     ```
     C:\Users\<YourUsername>\.yjp\log\WebSphereLiberty-<pid>.log
     ```
     يجب أن يشير السجل إلى أن الوكيل محمل ويستمع على منفذ (افتراضي: 10001):
     ```
     Profiler agent is listening on port 10001
     ```

6. **الاتصال بواجهة مستخدم YourKit Profiler**
   - شغّل واجهة مستخدم YourKit Java Profiler على جهاز Windows الخاص بك.
   - في واجهة مستخدم YourKit، حدد **Profile | Profile Local Java Server or Application** أو **Profile | Profile Remote Java Server or Application**.
     - للتحليل الأدائي المحلي (نظرًا لأن YourKit و Liberty على نفس الجهاز)، اختر **Profile Local Java Server or Application**.
     - يجب أن تكتشف واجهة المستخدم عملية WebSphere Liberty (المعرفة بواسطة `sessionname=WebSphereLiberty`).
   - إذا لم يتم الكشف عنها تلقائيًا، استخدم **Profile Remote Java Server or Application**، وحدد **Direct Connect**، وأدخل:
     - **Host**: `localhost`
     - **Port**: `10001` (أو المنفذ المحدد في سجل الوكيل).
   - اتصل بالخادم. ستعرض واجهة المستخدم قياسات أداء المعالج والذاكرة والخيوط.

7. **تحليل التطبيق أدائيًا**
   - استخدم واجهة مستخدم YourKit للقيام بما يلي:
     - **تحليل أداء المعالج (CPU Profiling)**: قم بتمكين أخذ عينات أو تتبع المعالج لتحديد الاختناقات في الأداء. تجنب تمكين "Profile J2EE" لأنظمة الحمل العالي لتقليل الحمل.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)
     - **تحليل أداء الذاكرة (Memory Profiling)**: حلل استخدام الكومة واكتشف تسريبات الذاكرة عن طريق تجميع الكائنات حسب التطبيق الويب (مفيد للتطبيقات المستضافة على Liberty).[](https://www.yourkit.com/docs/java-profiler/latest/help/webapps.jsp)
     - **تحليل الخيوط (Thread Analysis)**: تحقق من وجود حالات توقف (deadlocks) أو خيوط مجمدة في علامة التبويب Threads.[](https://www.yourkit.com/changes/)
   - خذ لقطات (snapshots) للتحليل في وضع عدم الاتصال إذا لزم الأمر (File | Save Snapshot).
   - راقب استخدام الذاكرة، حيث يمكن أن يزيد التحليل الأدائي من استهلاك الذاكرة. تجنب جلسات التحليل الطويلة بدون مراقبة.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

8. **استكشاف الأخطاء وإصلاحها**
   - **فشل الخادم في البدء أو يصبح غير قابل للوصول**:
     - تحقق من السجلات (`console.log`, `messages.log`, وسجل وكيل YourKit) للبحث عن أخطاء مثل `OutOfMemoryError` أو `NoSuchMethodError`.[](https://www.yourkit.com/forum/viewtopic.php?t=328)[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
     - تأكد من إضافة `-agentpath` إلى ملف `jvm.options` الصحيح وأنه يتطابق مع البرنامج النصي المستخدم لبدء تشغيل Liberty.[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
     - إذا كنت تستخدم IBM JDK، حاول إضافة `probe_disable=*` إلى مسار الوكيل لتجنب التعارضات.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=8042)
   - **ClassNotFoundException**:
     - إذا رأيت أخطاء مثل `java.lang.ClassNotFoundException` (مثل `java.util.ServiceLoader`)، فتأكد من أن إصدار وكيل YourKit متوافق مع JDK الخاص بك. بالنسبة لإصدارات IBM JDK القديمة (مثل Java 5)، استخدم YourKit 8.0 أو إصدار أقدم.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=7149)
   - **لا توجد بيانات تحليل أدائي**:
     - تحقق من تطابق إصدارات وكيل YourKit وواجهة المستخدم. يمكن أن تسبب الإصدارات غير المتطابقة مشكلات في الاتصال.[](https://www.yourkit.com/forum/viewtopic.php?t=328)
     - تأكد من إمكانية الوصول إلى الخادم عبر المتصفح (مثل `https://localhost:9443` إذا كنت تستخدم SSL). إذا لم يكن كذلك، فتحقق من إعدادات الجدار الناري أو تكوين SSL.[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
   - **مشكلات ملف السجل**:
     - إذا لم يتم إنشاء سجل YourKit في `~/.yjp/log/`، فتأكد من أن العملية لها أذونات الكتابة إلى الدليل الرئيسي للمستخدم.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=3219)
   - **تأثير على الأداء**:
     - يمكن أن يؤثر التحليل الأدائي على الأداء. استخدم الحد الأدنى من الإعدادات (مثل تعطيل قياس مكدس الاستدعاءات) للبيئات الشبيهة بالإنتاج.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

9. **اختياري: استخدام معالج تكامل YourKit**
   - يوفر YourKit معالج تكامل خادم Java لتبسيط التكوين:
     - شغّل واجهة مستخدم YourKit وحدد **Profile | Profile Local Java Server or Application**.
     - اختر **WebSphere Liberty** من قائمة الخوادم المدعومة (أو "Other Java application" إذا لم يكن Liberty مدرجًا).
     - اتبع المعالج لتوليد إعدادات `-agentpath` اللازمة وتحديث `jvm.options`. تأكد من أن لديك أذونات الكتابة لملفات التكوين.[](https://www.yourkit.com/docs/java-profiler/latest/help/java-server-integration-wizard.jsp)
   - هذا مفيد بشكل خاص لضمان المسارات والإعدادات الصحيحة.

10. **إيقاف التحليل الأدائي**
    - لتعطيل التحليل الأدائي، قم بإزالة أو تعليق سطر `-agentpath` في `jvm.options` وأعد تشغيل الخادم.
    - بدلاً من ذلك، أوقف الخادم:
      ```
      <LIBERTY_INSTALL_DIR>\bin\server stop <server_name>
      ```

### ملاحظات إضافية
- **الترخيص**: لا يلزم مفتاح ترخيص لوكيل YourKit على الخادم؛ يتم تطبيق الترخيص في واجهة مستخدم YourKit. للتحليل الأدائي عن بُعد من جهاز Windows آخر، تأكد من أن واجهة المستخدم لديها ترخيص صالح.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=11385)[](https://www.yourkit.com/forum/viewtopic.php?t=11385)
- **التحليل الأدائي عن بُعد**: إذا كنت تقوم بالتحليل الأدائي من جهاز مختلف، فتأكد من إمكانية الاتصال بالشبكة إلى منفذ الوكيل (افتراضي: 10001) واستخدم خيار **Profile Remote Java Server or Application** مع اسم المضيف / IP الخاص بالخادم.
- **اعتبارات الأداء**: يمكن أن يزيد التحليل الأدائي من استخدام الذاكرة والمعالج. بالنسبة لأنظمة الإنتاج، ابدأ بأقل خيارات تحليل أدائي (مثل أخذ عينات المعالج) وراقب صحة الخادم.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)
- **التوافق**: إذا كنت تستخدم إصدارًا قديمًا من WebSphere Liberty مع IBM JDK 1.4.2 أو 1.5، فقد تحتاج إلى إصدار أقدم من YourKit (مثل 8.0 لـ Java 5).[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=7149)[](https://stackoverflow.com/questions/61795/java-profiler-for-ibm-jvm-1-4-2-websphere-6-0-2)
- **التوثيق**: راجع التوثيق الرسمي لـ YourKit للحصول على خيارات التحليل الأدائي التفصيلية: [YourKit Java Profiler Help](https://www.yourkit.com/docs/java/help/).[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

### مثال على التكوين
إليك نموذج لملف `jvm.options`:
```
-Xmx4G
-Xms4G
-agentpath:C:\Program Files\YourKit-Java-Profiler-2023.9\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
```

### اختبار الإعداد
- بعد بدء تشغيل الخادم، قم بالوصول إلى تطبيقك (مثل `https://localhost:9443`) للتأكد من أنه يعمل.
- في واجهة مستخدم YourKit، تحقق من عرض بيانات القياس عن بُعد (المعالج، الذاكرة، الخيوط).
- إذا ظهرت مشكلات، فتحقق من سجل وكيل YourKit وسجلات Liberty للبحث عن الأخطاء.

إذا واجهت أخطاء محددة أو تحتاج إلى مساعدة في خطوة معينة، فأخبرني، ويمكنني تقديم مزيد من المساعدة!