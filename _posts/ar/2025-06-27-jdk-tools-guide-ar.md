---
audio: false
generated: true
lang: ar
layout: post
title: نظرة عامة على أدوات OpenJDK 21
translated: true
type: note
---

يحتوي الدليل `/usr/lib/jvm/java-21-openjdk-amd64/bin/` على أدوات مقدمة من OpenJDK 21 Java Development Kit (JDK). تُستخدم هذه الأدوات لمهام متنوعة متعلقة بتطوير Java، وتصحيح الأخطاء، والمراقبة، والتعبئة. فيما يلي شرح موجز لكل أداة واستخدامها الشائع. للحصول على تفاصيل الاستخدام، يمكنك تشغيل `tool_name --help` أو `man tool_name` في الطرفية لمعظم هذه الأدوات.

---

### 1. **jar** - إنشاء وإدارة ملفات Java ARchive (JAR)
- **الغرض**: حزم فئات Java والموارد في ملف JAR أو استخراج المحتويات من ملف JAR.
- **الاستخدام الشائع**:
  ```bash
  jar cf myapp.jar *.class  # إنشاء ملف JAR
  jar xf myapp.jar          # استخراج محتويات ملف JAR
  jar tf myapp.jar          # إدراج محتويات ملف JAR
  ```
- **مثال**: `jar cvfm myapp.jar manifest.txt *.class` (ينشئ ملف JAR مع ملف manifest).

---

### 2. **java** - تشغيل تطبيق Java
- **الغرض**: تشغيل برنامج Java من خلال تنفيذ ملف فئة أو ملف JAR.
- **الاستخدام الشائع**:
  ```bash
  java MyClass              # تشغيل ملف فئة
  java -jar myapp.jar       # تشغيل ملف JAR
  java -cp . MyClass        # التشغيل مع classpath محدد
  ```
- **مثال**: `java -Xmx512m -jar myapp.jar` (يشغّل ملف JAR بحد أقصى للذاكرة المؤقتة يبلغ 512 ميجابايت).

---

### 3. **javadoc** - إنشاء توثيق API
- **الغرض**: إنشاء توثيق HTML من تعليقات شفرة مصدر Java.
- **الاستخدام الشائع**:
  ```bash
  javadoc -d docs MyClass.java  # إنشاء التوثيق في مجلد 'docs'
  ```
- **مثال**: `javadoc -d docs -sourcepath src -subpackages com.example` (إنشاء توثيق لحزمة).

---

### 4. **jcmd** - إرسال أوامر تشخيصية إلى JVM قيد التشغيل
- **الغرض**: التفاعل مع عملية Java قيد التشغيل للتشخيص (مثل: تفريغ البيانات threads، معلومات heap).
- **الاستخدام الشائع**:
  ```bash
  jcmd <pid> help           # إدراج الأوامر المتاحة لعملية JVM
  jcmd <pid> Thread.print   # طباعة تفريغ البيانات threads
  ```
- **مثال**: `jcmd 1234 GC.run` (تشغيل garbage collection لعملية ذات المعرف 1234).

---

### 5. **jdb** - مصحح أخطاء Java
- **الغرض**: تصحيح تطبيقات Java بشكل تفاعلي.
- **الاستخدام الشائع**:
  ```bash
  jdb MyClass               # بدء تصحيح الأخطاء لفئة
  java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 MyClass  # التشغيل مع وكيل التصحيح
  jdb -attach localhost:5005  # الربط بـ JVM قيد التشغيل
  ```
- **مثال**: `jdb -sourcepath src MyClass` (تصحيح الأخطاء مع شفرة المصدر).

---

### 6. **jdeps** - تحليل تبعيات الفئات وملفات JAR
- **الغرض**: تحديد تبعيات تطبيق أو مكتبة Java.
- **الاستخدام الشائع**:
  ```bash
  jdeps myapp.jar           # تحليل التبعيات في ملف JAR
  jdeps -s MyClass.class    # ملخص للتبعيات
  ```
- **مثال**: `jdeps -v myapp.jar` (تحليل مفصل للتبعيات).

---

### 7. **jhsdb** - مصحح أخطاء Java HotSpot
- **الغرض**: تصحيح وتحليل متقدم لعمليات JVM (مثل: core dumps).
- **الاستخدام الشائع**:
  ```bash
  jhsdb jmap --heap --pid <pid>  # تحليل heap لعملية قيد التشغيل
  jhsdb hsdb                     # تشغيل واجهة المستخدم الرسومية لمصحح أخطاء HotSpot
  ```
- **مثال**: `jhsdb jmap --heap --pid 1234` (تفريغ معلومات heap للعملية 1234).

---

### 8. **jinfo** - عرض أو تعديل تكوين JVM
- **الغرض**: فحص أو تغيير خيارات JVM لعملية قيد التشغيل.
- **الاستخدام الشائع**:
  ```bash
  jinfo <pid>               # عرض إشارات وخصائص JVM
  jinfo -flag +PrintGC <pid>  # تمكين إشارة JVM
  ```
- **مثال**: `jinfo -sysprops 1234` (عرض خصائص النظام للعملية 1234).

---

### 9. **jmap** - تفريغ ذاكرة JVM أو معلومات heap
- **الغرض**: إنشاء heap dumps أو إحصائيات الذاكرة.
- **الاستخدام الشائع**:
  ```bash
  jmap -heap <pid>          # طباعة ملخص heap
  jmap -dump:file=dump.hprof <pid>  # إنشاء heap dump
  ```
- **مثال**: `jmap -dump:live,format=b,file=dump.hprof 1234` (تفريغ الكائنات النشطة).

---

### 10. **jpackage** - حزم تطبيقات Java
- **الغرض**: إنشاء مثبتات أو ملفات تنفيذية أصلية لتطبيقات Java (مثل: .deb, .rpm, .exe).
- **الاستخدام الشائع**:
  ```bash
  jpackage --input target --name MyApp --main-jar myapp.jar --main-class MyClass
  ```
- **مثال**: `jpackage --type deb --input target --name MyApp --main-jar myapp.jar` (إنشاء حزمة Debian).

---

### 11. **jps** - إدراج عمليات JVM قيد التشغيل
- **الغرض**: عرض عمليات Java مع معرفات العمليات (PIDs) الخاصة بها.
- **الاستخدام الشائع**:
  ```bash
  jps                       # إدراج جميع عمليات Java
  jps -l                    # تضمين أسماء الفئات الكاملة
  ```
- **مثال**: `jps -m` (عرض الفئة الرئيسية والوسائط).

---

### 12. **jrunscript** - تشغيل نصوص برمجية في Java
- **الغرض**: تنفيذ نصوص برمجية (مثل: JavaScript) باستخدام محرك النصوص البرمجية في Java.
- **الاستخدام الشائع**:
  ```bash
  jrunscript -e "print('Hello')"  # تشغيل أمر نص برمجي مفرد
  jrunscript script.js            # تشغيل ملف نص برمجي
  ```
- **مثال**: `jrunscript -l js -e "print(2+2)"` (تشغيل شفرة JavaScript).

---

### 13. **jshell** - Java REPL تفاعلي
- **الغرض**: تشغيل مقاطع شفرة Java بشكل تفاعلي للاختبار أو التعلم.
- **الاستخدام الشائع**:
  ```bash
  jshell                    # بدء الطرفية التفاعلية
  jshell script.jsh         # تشغيل نص JShell
  ```
- **مثال**: `jshell -q` (بدء JShell في الوضع الهادئ).

---

### 14. **jstack** - إنشاء تفريغ البيانات threads
- **الغرض**: التقاط أثر المكدس للـ threads في JVM قيد التشغيل.
- **الاستخدام الشائع**:
  ```bash
  jstack <pid>              # طباعة تفريغ البيانات threads
  jstack -l <pid>           # تضمين معلومات القفل
  ```
- **مثال**: `jstack 1234 > threads.txt` (حفظ تفريغ البيانات threads في ملف).

---

### 15. **jstat** - مراقبة إحصائيات JVM
- **الغرض**: عرض إحصائيات الأداء (مثل: garbage collection، استخدام الذاكرة).
- **الاستخدام الشائع**:
  ```bash
  jstat -gc <pid>           # عرض إحصائيات garbage collection
  jstat -class <pid> 1000   # عرض إحصائيات تحميل الفئات كل ثانية
  ```
- **مثال**: `jstat -gcutil 1234 1000 5` (عرض إحصائيات GC 5 مرات، كل ثانية).

---

### 16. **jstatd** - خادم مراقبة JVM
- **الغرض**: تشغيل خادم مراقبة عن بُعد للسماح لأدوات مثل `jstat` بالاتصال عن بُعد.
- **الاستخدام الشائع**:
  ```bash
  jstatd -J-Djava.security.policy=jstatd.policy
  ```
- **مثال**: `jstatd -p 1099` (بدء الخادم على المنفذ 1099).

---

### 17. **keytool** - إدارة المفاتيح المشفرة والشهادات
- **الغرض**: إنشاء وإدارة مخازن المفاتيح لتطبيقات Java الآمنة.
- **الاستخدام الشائع**:
  ```bash
  keytool -genkeypair -alias mykey -keystore keystore.jks  # إنشاء زوج مفاتيح
  keytool -list -keystore keystore.jks                     # إدراج محتويات مخزن المفاتيح
  ```
- **مثال**: `keytool -importcert -file cert.pem -keystore keystore.jks` (استيراد شهادة).

---

### 18. **rmiregistry** - بدء سجل RMI
- **الغرض**: تشغيل سجل لكائنات Java Remote Method Invocation (RMI).
- **الاستخدام الشائع**:
  ```bash
  rmiregistry               # بدء سجل RMI على المنفذ الافتراضي (1099)
  rmiregistry 1234          # البدء على منفذ محدد
  ```
- **مثال**: `rmiregistry -J-Djava.rmi.server.codebase=file:./classes/` (البدء مع codebase).

---

### 19. **serialver** - إنشاء serialVersionUID للفئات
- **الغرض**: حساب `serialVersionUID` لفئات Java التي تنفذ `Serializable`.
- **الاستخدام الشائع**:
  ```bash
  serialver MyClass         # طباعة serialVersionUID لفئة
  ```
- **مثال**: `serialver -classpath . com.example.MyClass` (الحساب لفئة محددة).

---

### 20. **javac** - مترجم Java
- **الغرض**: ترجمة ملفات مصدر Java إلى bytecode.
- **الاستخدام الشائع**:
  ```bash
  javac MyClass.java        # ترجمة ملف مفرد
  javac -d bin *.java       # الترجمة إلى دليل محدد
  ```
- **مثال**: `javac -cp lib/* -sourcepath src -d bin src/MyClass.java` (الترجمة مع التبعيات).

---

### 21. **javap** - تفكيك ملفات الفئات
- **الغرض**: عرض bytecode أو توقيعات الطرق لفئة مترجمة.
- **الاستخدام الشائع**:
  ```bash
  javap -c MyClass          # تفكيك bytecode
  javap -s MyClass          # عرض توقيعات الطرق
  ```
- **مثال**: `javap -c -private MyClass` (عرض الطرق الخاصة وـ bytecode).

---

### 22. **jconsole** - أداة مراقبة JVM رسومية
- **الغرض**: مراقبة أداء JVM (الذاكرة، threads، وحدة المعالجة المركزية) عبر واجهة مستخدم رسومية.
- **الاستخدام الشائع**:
  ```bash
  jconsole                  # بدء JConsole والاتصال بـ JVM محلي
  jconsole <pid>            # الاتصال بعملية محددة
  ```
- **مثال**: `jconsole localhost:1234` (الاتصال بـ JVM عن بُعد).

---

### 23. **jdeprscan** - فحص واجهات برمجة التطبيقات المهملة
- **الغرض**: تحديد استخدام واجهات برمجة التطبيقات المهملة في ملف JAR أو ملف فئة.
- **الاستخدام الشائع**:
  ```bash
  jdeprscan myapp.jar       # فحص ملف JAR للبحث عن واجهات برمجة التطبيقات المهملة
  ```
- **مثال**: `jdeprscan --release 11 myapp.jar` (التحقق مقابل واجهات برمجة تطبيقات Java 11).

---

### 24. **jfr** - Java Flight Recorder
- **الغرض**: إدارة وتحليل بيانات التنميط من Java Flight Recorder.
- **الاستخدام الشائع**:
  ```bash
  jfr print recording.jfr   # طباعة محتويات ملف JFR
  jfr summary recording.jfr # تلخيص ملف JFR
  ```
- **مثال**: `jfr print --events GC recording.jfr` (عرض أحداث GC).

---

### 25. **jimage** - فحص أو استخراج ملفات JIMAGE
- **الغرض**: العمل مع ملفات JIMAGE (المستخدمة في وحدات JDK).
- **الاستخدام الشائع**:
  ```bash
  jimage extract image.jimage  # استخراج محتويات ملف JIMAGE
  ```
- **مثال**: `jimage list image.jimage` (إدراج محتويات ملف JIMAGE).

---

### 26. **jlink** - إنشاء صور وقت تشغيل Java مخصصة
- **الغرض**: بناء JRE أدنى مع الوحدات المطلوبة فقط.
- **الاستخدام الشائع**:
  ```bash
  jlink --module-path mods --add-modules java.base --output myjre
  ```
- **مثال**: `jlink --add-modules java.base,java.sql --output custom-jre` (إنشاء JRE مع وحدات محددة).

---

### 27. **jmod** - إدارة ملفات JMOD
- **الغرض**: إنشاء أو إدارة ملفات JMOD (المستخدمة لوحدات JDK).
- **الاستخدام الشائع**:
  ```bash
  jmod create --class-path classes mymod.jmod  # إنشاء ملف JMOD
  jmod list mymod.jmod                        # إدراج المحتويات
  ```
- **مثال**: `jmod extract mymod.jmod` (استخراج محتويات JMOD).

---

### 28. **jwebserver** - خادم HTTP بسيط
- **الغرض**: تشغيل خادم ويب أساسي لخدمة الملفات الثابتة.
- **الاستخدام الشائع**:
  ```bash
  jwebserver -d /path/to/dir  # بدء الخادم لدليل
  jwebserver -p 8080          # البدء على منفذ محدد
  ```
- **مثال**: `jwebserver -d ./html -p 8000` (خدمة الملفات من ./html على المنفذ 8000).

---

### نصائح لمزيد من التعلم
- **التوثيق**: شغّل `tool_name --help` أو راجع توثيق Oracle لـ JDK (مثال: https://docs.oracle.com/en/java/javase/21/docs/specs/man/).
- **صفحات الدليل**: استخدم `man tool_name` للأدوات التي تحتوي على صفحات دليل.
- **الممارسة**: جرب في مشروع اختبار لفهم سلوك الأداة.
- **أدوات المراقبة**: بالنسبة لـ `jcmd`، `jmap`، `jstack`، إلخ، استخدم `jps` للعثور على PID لعملية Java الخاصة بك.
- **تصحيح الأخطاء**: اجمع بين `jdb`، `jhsdb`، أو `jconsole` لتصحيح الأخطاء المتقدم.

إذا كنت تعمل على مشروع تداول (كما يُقترح من دليلك)، فمن المرجح أن تكون الأدوات مثل `javac`، `java`، `jar`، و `jpackage` هي الأكثر صلة بترجمة وتشغيل وتعبئة تطبيقك. لضبط الأداء، استخدم `jstat`، `jmap`، أو `jfr`. دعني أعلم إذا كنت بحاجة إلى غوص أعمق في أي أداة محددة أو مساعدة في مشروع التداول الخاص بك!