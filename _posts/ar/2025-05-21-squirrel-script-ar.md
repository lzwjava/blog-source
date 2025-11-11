---
audio: false
generated: true
lang: ar
layout: post
title: نص تشغيل سكويرل
translated: true
type: note
---

يُستخدم هذا النصيقة الدفعية (batch script) لتشغيل عميل SQuirreL SQL، وهو أداة إدارة قواعد بيانات مبنية بلغة Java. فيما يلي شرح شامل للنصيقة، موضحًا الغرض منها وبنائها ووظيفتها خطوة بخطوة.

---

### **نظرة عامة**
صُممت النصيقة لتحقيق ما يلي:
1.  تكوين بيئة Java لتشغيل عميل SQuirreL SQL.
2.  التحقق من توافق إصدار Java (يتطلب الإصدار 1.6 أو 1.7).
3.  التحقق من وجود تحديثات للبرنامج وتطبيقها إذا كانت متاحة.
4.  بناء classpath لـ SQuirreL ومكتباته.
5.  تشغيل تطبيق عميل SQuirreL SQL مع المعلمات المناسبة.

كُتبت النصيقة لنظام Windows (باستخدام امتداد `.bat`) وتستخدم لغة النصيقة الدفعية لموجه أوامر Windows.

---

### **شرح سطرًا بسطر**

#### **1. `@echo off`**
- **الغرض**: يعطى عرض الأوامر في وحدة التحكم، مما يجعل ناتج النصيقة أنظف من خلال عرض الناتج المقصود فقط (مثل رسائل الخطأ أو عبارات `echo` محددة).
- **التأثير**: لا يتم عرض الأوامر المنفذة في النصيقة ما لم تتم طباعتها صراحةً باستخدام `echo`.

---

#### **2. `@rem IZPACK_JAVA is filtered in by the IzPack installer when this script is installed`**
- **الغرض**: تعليق (`@rem`) يشير إلى أن المتغير `IZPACK_JAVA` يتم تعيينه بواسطة مثبت IzPack أثناء عملية التثبيت.
- **السياق**: IzPack هو أداة تُستخدم لإنشاء مثبتات لتطبيقات Java. يقوم بتعيين متغير بيئة `JAVA_HOME` ديناميكيًا في النصيقة للإشارة إلى تثبيت Java المستخدم أثناء الإعداد.

#### **3. `set IZPACK_JAVA=%JAVA_HOME`**
- **الغرض**: يعين قيمة متغير البيئة `JAVA_HOME` (المعين بواسطة IzPack) إلى المتغير `IZPACK_JAVA`.
- **الشرح**: يضمن هذا أن النصيقة تعرف مكان تثبيت Java. يشير `JAVA_HOME` عادةً إلى الدليل الجذري لـ Java Development Kit (JDK) أو Java Runtime Environment (JRE).

---

#### **4. منطق اكتشاف Java**
```bat
@rem We detect the java executable to use according to the following algorithm:
@rem 1. If the one used by the IzPack installer is available then use that; otherwise
@rem 2. Use the java that is in the command path.
if exist "%IZPACK_JAVA%\bin\javaw.exe" (
  set LOCAL_JAVA=%IZPACK_JAVA%\bin\javaw.exe
) else (
  set LOCAL_JAVA=javaw.exe
)
```
- **الغرض**: يحدد أي ملف تنفيذي لـ Java سيتم استخدامه لتشغيل SQuirreL SQL.
- **المنطق**:
  1.  **التحقق من IzPack Java**: تتحقق النصيقة مما إذا كان `javaw.exe` موجودًا في الدليل `bin` الخاص بتثبيت Java المحدد بواسطة `IZPACK_JAVA` (أي `%IZPACK_JAVA%\bin\javaw.exe`).
     - `javaw.exe` هو ملف تنفيذي خاص بـ Windows يعمل بتطبيقات Java دون فتح نافذة وحدة تحكم (على عكس `java.exe`).
     - إذا وُجد، يتم تعيين `LOCAL_JAVA` إلى المسار الكامل لـ `javaw.exe`.
  2.  **الرجوع إلى PATH**: إذا لم يتم العثور على `javaw.exe` في الدليل `IZPACK_JAVA`، ترجع النصيقة إلى استخدام `javaw.exe` من متغير البيئة `PATH` في النظام.
- **لماذا `javaw.exe`؟**: يضمن استخدام `javaw.exe` تشغيل التطبيق دون نافذة أوامر مستمرة، مما يوفر تجربة مستخدم أكثر سلاسة.

#### **5. `echo Using java: %LOCAL_JAVA%`**
- **الغرض**: يطبع مسار الملف التنفيذي لـ Java المستخدم في وحدة التحكم لأغراض التصحيح أو المعلومات.
- **مثال على الناتج**: إذا كانت `LOCAL_JAVA` هي `C:\Program Files\Java\jre1.6.0_45\bin\javaw.exe`، فستعرض:
  ```
  Using java: C:\Program Files\Java\jre1.6.0_45\bin\javaw.exe
  ```

---

#### **6. تحديد دليل الصفحة الرئيسي لـ SQuirreL SQL**
```bat
set basedir=%~f0
:strip
set removed=%basedir:~-1%
set basedir=%basedir:~0,-1%
if NOT "%removed%"=="\" goto strip
set SQUIRREL_SQL_HOME=%basedir%
```
- **الغرض**: يحدد الدليل الذي تم تثبيت SQuirreL SQL فيه (`SQUIRREL_SQL_HOME`).
- **الشرح**:
  - `%~f0`: يتم توسيع هذا إلى المسار الكامل للنصيقة الدفعية نفسها (مثل `C:\Program Files\SQuirreL\squirrel-sql.bat`).
  - **حلقة `:strip`**: تقوم النصيقة بإزالة الحرف الأخير من `basedir` بشكل متكرر حتى تصادف شرطة مائلة للخلف (`\`)، مما يؤدي فعليًا إلى تجريد اسم ملف النصيقة للحصول على مسار الدليل.
  - **النتيجة**: يتم تعيين `SQUIRREL_SQL_HOME` على الدليل الذي يحتوي على النصيقة (مثل `C:\Program Files\SQuirreL`).
- **لماذا هذا الأسلوب؟**: يضمن هذا أن النصيقة يمكنها تحديد دليل التثبيت الخاص بها ديناميكيًا، مما يجعلها قابلة للنقل عبر أنظمة مختلفة.

---

#### **7. فحص إصدار Java**
```bat
"%LOCAL_JAVA%" -cp "%SQUIRREL_SQL_HOME%\lib\versioncheck.jar" JavaVersionChecker 1.6 1.7
if ErrorLevel 1 goto ExitForWrongJavaVersion
```
- **الغرض**: يتحقق من توافق إصدار Java مع SQuirreL SQL (يتطلب الإصدار 1.6 أو 1.7).
- **الشرح**:
  - تشغل النصيقة فئة `JavaVersionChecker` من `versioncheck.jar`، الموجود في الدليل `lib` لـ SQuirreL SQL.
  - **`-cp`**: يحدد classpath، مشيرًا إلى `versioncheck.jar`.
  - **الوسائط**: `1.6 1.7` تشير إلى أن إصدار Java يجب أن يكون 1.6 أو 1.7.
  - **ملاحظة**: تم تجميع `versioncheck.jar` مع توافق Java 1.2.2، مما يضمن إمكانية تشغيله على JVMs أقدم لإجراء فحص الإصدار.
  - **معالجة الأخطاء**: إذا كان إصدار Java غير متوافق، يتم تعيين `ErrorLevel` على 1، وتقفز النصيقة إلى التسمية `:ExitForWrongJavaVersion`، مما ينهي التنفيذ.
- **لماذا هذا الفحص؟**: يتطلب SQuirreL SQL إصدارات محددة من Java ليعمل بشكل صحيح، وهذا يمنع التطبيق من التشغيل على JVMs غير مدعومة.

---

#### **8. فحص تحديث البرنامج**
```bat
if not exist "%SQUIRREL_SQL_HOME%\update\changeList.xml" goto launchsquirrel
SET TMP_CP="%SQUIRREL_SQL_HOME%\update\downloads\core\squirrel-sql.jar"
if not exist %TMP_CP% goto launchsquirrel
dir /b "%SQUIRREL_SQL_HOME%\update\downloads\core\*.*" > %TEMP%\update-lib.tmp
FOR /F %%I IN (%TEMP%\update-lib.tmp) DO CALL "%SQUIRREL_SQL_HOME%\addpath.bat" "%SQUIRREL_SQL_HOME%\update\downloads\core\%%I"
SET UPDATE_CP=%TMP_CP%
SET UPDATE_PARMS=--log-config-file "%SQUIRREL_SQL_HOME%\update-log4j.properties" --squirrel-home "%SQUIRREL_SQL_HOME%" %1 %2 %3 %4 %5 %6 %7 %8 %9
"%LOCAL_JAVA%" -cp %UPDATE_CP% -Dlog4j.defaultInitOverride=true -Dprompt=true net.sourceforge.squirrel_sql.client.update.gui.installer.PreLaunchUpdateApplication %UPDATE_PARAMS%
```
- **الغرض**: يتحقق عن تحديثات البرنامج ويطبقها قبل تشغيل التطبيق الرئيسي.
- **الشرح**:
  1.  **التحقق من ملفات التحديث**:
     - تتحقق النصيقة مما إذا كان `changeList.xml` موجودًا في الدليل `update`. يتم إنشاء هذا الملف بواسطة ميزة تحديث برنامج SQuirreL لتتبع التحديثات.
     - إذا لم يكن `changeList.xml` موجودًا، تتخطى النصيقة عملية التحديث وتقفز إلى `:launchsquirrel`.
     - تتحقق أيضًا من وجود `squirrel-sql.jar` المحدث في الدليل `update\downloads\core`. إذا لم يكن موجودًا، تتخطى النصيقة إلى `:launchsquirrel`.
  2.  **بناء classpath للتحديث**:
     - ي列出 الأمر `dir /b` جميع الملفات في الدليل `update\downloads\core` ويكتبها في ملف مؤقت (`%TEMP%\update-lib.tmp`).
     - تقوم حلقة `FOR /F` بالتكرار على الملفات في `update-lib.tmp` وتستدعي `addpath.bat` لإلحاق كل ملف بـ classpath المخزن في `TMP_CP`.
     - يتم تعيين `UPDATE_CP` على classpath، بدءًا من `squirrel-sql.jar` من دليل التحديث.
  3.  **تعيين معلمات التحديث**:
     - يتضمن `UPDATE_PARMS`:
       - `--log-config-file`: يحدد ملف تكوين Log4j للتسجيل أثناء عملية التحديث.
       - `--squirrel-home`: يمرر دليل تثبيت SQuirreL.
       - `%1 %2 %3 ... %9`: يمرر أي وسائط سطر أوامر مقدمة للنصيقة.
  4.  **تشغيل تطبيق التحديث**:
     - تشغل النصيقة `PreLaunchUpdateApplication` (فئة Java في `squirrel-sql.jar`) لتطبيق التحديثات.
     - **`-Dlog4j.defaultInitOverride=true`**: يتجاوز تكوين Log4j الافتراضي.
     - **`-Dprompt=true`**: يُفترض أنه يُمكن المطالبات التفاعلية أثناء عملية التحديث.
- **لماذا هذه الخطوة؟**: يدعم SQuirreL SQL التحديثات التلقائية، ويضمن هذا القسم تطبيق أي تحديثات تم تنزيلها قبل تشغيل التطبيق الرئيسي.

---

#### **9. تشغيل SQuirreL SQL**
```bat
:launchsquirrel
@rem build SQuirreL's classpath
set TMP_CP="%SQUIRREL_SQL_HOME%\squirrel-sql.jar"
dir /b "%SQUIRREL_SQL_HOME%\lib\*.*" > %TEMP%\squirrel-lib.tmp
FOR /F %%I IN (%TEMP%\squirrel-lib.tmp) DO CALL "%SQUIRREL_SQL_HOME%\addpath.bat" "%SQUIRREL_SQL_HOME%\lib\%%I"
SET SQUIRREL_CP=%TMP_CP%
echo "SQUIRREL_CP=%SQUIRREL_CP%"
```
- **الغرض**: يبني classpath لتطبيق SQuirreL SQL الرئيسي ويستعد لتشغيله.
- **الشرح**:
  1.  **تهيئة Classpath**:
     - يتم تهيئة `TMP_CP` بالمسار إلى `squirrel-sql.jar` في دليل تثبيت SQuirreL.
  2.  **إضافة ملفات Jars للمكتبات**:
     - ي列出 الأمر `dir /b` جميع الملفات في الدليل `lib` ويكتبها في `squirrel-lib.tmp`.
     - تقوم حلقة `FOR /F` بالتكرار على الملفات وتستدعي `addpath.bat` لإلحاق كل ملف مكتبة (مثل ملفات `.jar`) بـ classpath `TMP_CP`.
  3.  **تعيين Classpath النهائي**:
     - يتم تعيين `SQUIRREL_CP` على classpath المكتمل.
  4.  **ناتج التصحيح**:
     - تطبع النصيقة classpath النهائي (`SQUIRREL_CP`) لأغراض التصحيح.

---

#### **10. تعيين معلمات التشغيل**
```bat
SET TMP_PARMS=--log-config-file "%SQUIRREL_SQL_HOME%\log4j.properties" --squirrel-home "%SQUIRREL_SQL_HOME%" %1 %2 %3 %4 %5 %6 %7 %8 %9
```
- **الغرض**: يحدد المعلمات التي سيتم تمريرها إلى تطبيق SQuirreL SQL.
- **الشرح**:
  - `--log-config-file`: يحدد ملف تكوين Log4j للتطبيق الرئيسي.
  - `--squirrel-home`: يمرر دليل تثبيت SQuirreL.
  - `%1 %2 ... %9`: يمرر أي وسائط سطر أوامر مقدمة للنصيقة.

---

#### **11. تشغيل التطبيق**
```bat
@rem -Dsun.java2d.noddraw=true prevents performance problems on Win32 systems.
start "SQuirreL SQL Client" /B "%LOCAL_JAVA%" -Xmx256m -Dsun.java2d.noddraw=true -cp %SQUIRREL_CP% -splash:"%SQUIRREL_SQL_HOME%/icons/splash.jpg" net.sourceforge.squirrel_sql.client.Main %TMP_PARMS%
```
- **الغرض**: يشغل تطبيق عميل SQuirreL SQL.
- **الشرح**:
  - **`start "SQuirreL SQL Client" /B`**: يشغل الأمر في عملية جديدة دون فتح نافذة وحدة تحكم جديدة (`/B` يمنع ظهور النافذة).
  - **`%LOCAL_JAVA%`**: يحدد الملف التنفيذي لـ Java المراد استخدامه.
  - **`-Xmx256m`**: يحدد الحد الأقصى لحجم ذاكرة Java heap إلى 256 ميغابايت للحد من استخدام الذاكرة.
  - **`-Dsun.java2d.noddraw=true`**: يعطل DirectDraw لرسومات Java 2D لتجنب مشاكل الأداء على أنظمة Windows.
  - **`-cp %SQUIRREL_CP%`**: يحدد classpath للتطبيق.
  - **`-splash:"%SQUIRREL_SQL_HOME%/icons/splash.jpg"`**: يعرض شاشة ترحيب (صورة) عند بدء تشغيل التطبيق.
  - **`net.sourceforge.squirrel_sql.client.Main`**: فئة Java الرئيسية التي سيتم تنفيذها.
  - **`%TMP_PARMS%`**: يمرر المعلمات المحددة مسبقًا.

---

#### **12. الخروج لإصدار Java غير الصحيح**
```bat
:ExitForWrongJavaVersion
```
- **الغرض**: تسمية تُستخدم كنقطة خروج إذا فشل فحص إصدار Java.
- **الشرح**: إذا لم يكن إصدار Java هو 1.6 أو 1.7، تقفز النصيقة إلى هنا وتنتهي دون تشغيل التطبيق.

---

### **المكونات والمفاهيم الرئيسية**
1.  **بناء Classpath**:
    - تبني النصيقة classpath ديناميكيًا لكل من عملية التحديث (`UPDATE_CP`) والتطبيق الرئيسي (`SQUIRREL_CP`) من خلال تضمين `squirrel-sql.jar` وجميع ملفات `.jar` في الدلائل `lib` أو `update\downloads\core`.
    - يُفترض أن نصيقة `addpath.bat` (غير معروضة) تقوم بإلحاق كل ملف بمتغير classpath.

2.  **تكوين Log4j**:
    - Log4j هو إطار عمل للتسجيل تستخدمه SQuirreL SQL. تحدد النصيقة ملفات تكوين Log4j منفصلة لعملية التحديث (`update-log4j.properties`) وللتطبيق الرئيسي (`log4j.properties`).

3.  **آلية تحديث البرنامج**:
    - يدعم SQuirreL SQL التحديثات التلقائية، والتي تديرها فئة `PreLaunchUpdateApplication`. تتحقق النصيقة من ملفات التحديث وتشغل عملية التحديث إذا لزم الأمر.

4.  **توافق إصدار Java**:
    - تفرض النصيقة التوافق الصارم مع إصدار Java 1.6 أو 1.7، ويرجع ذلك على الأرجح إلى تبعيات أو ميزات محددة لهذه الإصدارات.

5.  **القابلية للنقل**:
    - صُممت النصيقة لتكون قابلة للنقل من خلال تحديد دليل التثبيت وموقع الملف التنفيذي لـ Java ديناميكيًا.

---

### **المشكلات والاعتبارات المحتملة**
1.  **تقييد إصدار Java**:
    - تسمح النصيقة فقط بإصدار Java 1.6 أو 1.7، وهما إصداران قديمان (تم إصدارهما في 2006 و 2011 على التوالي). قد تحتوي الأنظمة الحديثة على إصدارات أحدث من Java، مما يتسبب في فشل النصيقة ما لم يتم تثبيت JRE أقدم.
    - **الحل البديل**: قد يحتاج المستخدمون إلى تثبيت JRE متوافق أو تعديل النصيقة لدعم الإصدارات الأحدث (إذا كان SQuirreL SQL متوافقًا).

2.  **المسارات الثابتة**:
    - تفترض النصيقة وجود ملفات معينة (مثل `squirrel-sql.jar`، `versioncheck.jar`، `addpath.bat`) في دلائل محددة بالنسبة إلى `SQUIRREL_SQL_HOME`. إذا كانت هذه الملفات مفقودة أو مُنقلة، فستفشل النصيقة.

3.  **خاص بنظام Windows**:
    - تستخدم النصيقة أوامر خاصة بـ Windows (`dir /b`، `FOR /F`، `start /B`) و `javaw.exe`، مما يجعلها غير متوافقة مع أنظمة غير Windows دون تعديل.

4.  **معالجة الأخطاء**:
    - تتعامل النصيقة مع أخطاء إصدار Java ولكنها لا توفر رسائل خطأ مفصلة لفشل آخر (مثل فقدان `squirrel-sql.jar` أو classpath غير صالح).

5.  **حد الذاكرة**:
    - يقتصر العلم `-Xmx256m` على JVM بذاكرة مقدارها 256 ميغابايت، وهو ما قد يكون غير كافٍ لقواعد البيانات الكبيرة أو الاستعلامات المعقدة، مما قد يتسبب في `OutOfMemoryError`.

---

### **ملخص**
هذه النصيقة الدفعية هي مُشغل لعميل SQuirreL SQL، وتقوم بالمهام التالية:
- تكتشف وتكون الملف التنفيذي لـ Java.
- تتحقق من توافق إصدار Java (1.6 أو 1.7).
- تتحقق من تحديثات البرنامج وتطبقها إذا كانت متاحة.
- تبني classpath للتطبيق.
- تشغل SQuirreL SQL بالمعلمات المناسبة، بما في ذلك شاشة الترحيب وإعدادات الذاكرة.

هيكل النصيقة جيد لغرضها ولكنها مصممة خصيصًا لبيئة معينة (Windows، Java 1.6/1.7) وقد تحتاج إلى تحديثات لدعم الأنظمة الحديثة أو إصدارات Java الأحدث.

إذا كان لديك المزيد من الأسئلة أو تحتاج إلى مساعدة في تعديل النصيقة (مثلًا، لدعم إصدارات Java أحدث)، فأخبرني!