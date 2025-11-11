---
audio: false
generated: true
lang: ar
layout: post
title: حل مشاكل إكليبس لجافا
translated: true
type: note
---

عند بدء تشغيل Eclipse 4.6.3 بالنقر على `eclipse.exe` ومواجهة الخطأ "Java was started but returned exit code" مع الإشارة إلى `Oracle\Java\javapath\javaw.exe`، فهذا يعني أن Eclipse يحاول استخدام آلة Java الافتراضية (JVM) غير متوافقة أو غير مهيأة بشكل صحيح. يشير المسار `Oracle\Java\javapath\javaw.exe` إلى أن Eclipse يستخدم افتراضيًا JVM مُعرَّفًا في متغير بيئة PATH في نظامك، والذي قد لا يكون مناسبًا لـ Eclipse 4.6.3. لحل هذه المشكلة، تحتاج إلى تحديد Java home الصحيح لـ Eclipse عن طريق تكوينه لاستخدام JVM متوافق. إليك الطريقة:

### الحل خطوة بخطوة

1. **فهم المتطلبات**  
   يتطلب Eclipse 4.6.3 (Neon) على الأقل Java 8 لتشغيله بشكل صحيح. يشير الخطأ إلى أن JVM الحالي (من `Oracle\Java\javapath`) قد لا يستوفي هذا المتطلب أو لديه مشاكل في التهيئة. ستحتاج إلى توجيه Eclipse إلى تثبيت Java متوافق، مثل Java 8 JDK.

2. **تحديد موقع تثبيت Java**  
   حدد مكان وجود إصدار Java متوافق (مثل JDK 1.8.0) على نظامك. المواقع الشائعة على نظام Windows تشمل:  
   - `C:\Program Files\Java\jdk1.8.0_XXX` (لـ Java 64-bit)  
   - `C:\Program Files (x86)\Java\jdk1.8.0_XXX` (لـ Java 32-bit)  
   استبدل `XXX` بإصدار التحديث المحدد (مثل `231` لـ JDK 1.8.0_231). داخل هذا الدليل، يوجد ملف `javaw.exe` في المجلد الفرعي `bin` (مثال: `C:\Program Files\Java\jdk1.8.0_XXX\bin\javaw.exe`).

   **نصيحة**: للتأكد من الإصدار والهيكل، افتح موجه الأوامر، انتقل إلى دليل `bin` (مثال: `cd C:\Program Files\Java\jdk1.8.0_XXX\bin`)، وقم بتشغيل:
   ```
   java -version
   ```
   ابحث عن "64-Bit" أو "32-Bit" في الناتج للتحقق من الهيكل. تأكد من أنه يطابق إصدار Eclipse الخاص بك (على الأرجح 64-bit إذا تم تنزيله مؤخرًا).

3. **ابحث عن ملف `eclipse.ini`**  
   ملف `eclipse.ini` هو ملف تهيئة موجود في نفس دليل `eclipse.exe`. على سبيل المثال، إذا كان Eclipse مثبتًا في `C:\eclipse`، سيكون الملف في `C:\eclipse\eclipse.ini`. يسمح لك هذا الملف بتحديد JVM الذي يجب أن يستخدمه Eclipse.

4. **تحرير ملف `eclipse.ini`**  
   افتح `eclipse.ini` في محرر نصوص (مثل Notepad) بصلاحيات المسؤول. ستقوم بتعديله لتضمين وسيط `-vm`، الذي يخبر Eclipse بأي JVM يستخدم. اتبع هذه الخطوات:

   - **تحقق من المحتوى الحالي**: ابحث عن وسيط `-vm`. إذا كان موجودًا بالفعل، سيكون متبوعًا بمسار في السطر التالي (مثال: `-vm` متبوعًا بـ `C:/some/path/bin/javaw.exe`). إذا كان يشير إلى المسار Problematic `Oracle\Java\javapath\javaw.exe`، فستستبدله. إذا لم يكن وسيط `-vm` موجودًا، فستضيفه.
   - **أضف أو عدل وسيط `-vm`**: أدخل السطرين التاليين قبل قسم `-vmargs` (إذا كان موجودًا) أو بالقرب من أعلى الملف بعد معلمات بدء التشغيل الأولية:
     ```
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     ```
     - استخدم الشرطات المائلة للأمام (`/`) بدلاً من الشرطات المائلة للخلف (`\`) لتجنب مشاكل التحليل.
     - استبدل `C:/Program Files/Java/jdk1.8.0_XXX` بالمسار الفعلي لتثبيت Java الخاص بك.
   - **تأكد من الموضع الصحيح**: يجب أن يظهر وسيط `-vm` قبل قسم `-vmargs`، والذي يبدأ عادةً بـ `-vmargs` متبوعًا بخيارات JVM مثل `-Xms256m` أو `-Xmx1024m`. على سبيل المثال، قد يبدو ملف `eclipse.ini` الخاص بك هكذا بعد التحرير:
     ```
     -startup
     plugins/org.eclipse.equinox.launcher_1.3.201.v20161025-1711.jar
     --launcher.library
     plugins/org.eclipse.equinox.launcher.win32.win32.x86_64_1.1.401.v20161122-1740
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     -vmargs
     -Dosgi.requiredJavaVersion=1.8
     -Xms256m
     -Xmx1024m
     ```
   - **تجنب المسافات الإضافية أو الأسطر الفارغة**: تأكد من عدم وجود مسافات غير ضرورية أو أسطر فارغة مباشرة بعد أسطر `-vm` أو المسار، لأن هذا قد يتسبب في سوء تفسير Eclipse للتكوين.

5. **احفظ واختبر**  
   احفظ ملف `eclipse.ini`، ثم انقر نقرًا مزدوجًا فوق `eclipse.exe` لبدء تشغيل Eclipse. إذا تم التكوين بشكل صحيح، يجب أن يبدأ Eclipse دون ظهور خطأ "Java was started but returned exit code".

### ملاحظات إضافية
- **مطابقة الهيكل**: تأكد من أن هيكل JVM (32-bit أو 64-bit) يطابق تثبيت Eclipse الخاص بك. يتطلب Eclipse 64-bit JVM 64-bit، والذي يوجد عادةً في `C:\Program Files\Java`، بينما يحتاج Eclipse 32-bit إلى JVM 32-bit من `C:\Program Files (x86)\Java`.
- **تحقق من المسار**: راجع مرة أخرى أن `javaw.exe` موجود في الموقع المحدد. إذا كان المسار غير صحيح، فسيفشل Eclipse في البدء.
- **خيار بديل**: إذا لم ينجح هذا، ففكر في تعيين متغير بيئة `JAVA_HOME` (مثال: `C:\Program Files\Java\jdk1.8.0_XXX`) وتحديث نظام PATH لتضمين `%JAVA_HOME%\bin`. ومع ذلك، يعد تعديل `eclipse.ini` هو الطريقة المفضلة والأكثر موثوقية لـ Eclipse.

من خلال تحرير ملف `eclipse.ini` لتضمين وسيط `-vm` مع المسار إلى `javaw.exe` متوافق، فإنك تحدد بشكل فعال Java home لـ Eclipse، مما يضمن استخدامه لـ JVM الصحيح للبدء.