---
audio: false
lang: ar
layout: post
title: حل مشاكل JDK في Eclipse
translated: true
---

عندما تبدأ Eclipse 4.6.3 عن طريق النقر على `eclipse.exe` وتواجه الخطأ "Java was started but returned exit code" مع مرجع إلى `Oracle\Java\javapath\javaw.exe`، فهذا يعني أن Eclipse تحاول استخدام آلة افتراضية Java (JVM) إما غير متوافقة أو غير مهيئة بشكل صحيح. يشير المسار `Oracle\Java\javapath\javaw.exe` إلى أن Eclipse تستخدم JVM محدد في متغير المسار (PATH) للنظام، والذي قد لا يكون مناسبًا لـ Eclipse 4.6.3. لتحل هذا المشكلة، عليك تحديد المنزل Java الصحيح لـ Eclipse عن طريق تكوينه لاستخدام JVM متوافقة. إليك كيفية القيام بذلك:

### حل خطوة بخطوة

1. **فهم المتطلبات**
   Eclipse 4.6.3 (Neon) يتطلب على الأقل Java 8 للعمل بشكل صحيح. يشير الخطأ إلى أن JVM الحالية (من `Oracle\Java\javapath`) قد لا تتوافق مع هذا المتطلب أو لديها مشاكل في التكوين. عليك توجيه Eclipse إلى تثبيت Java متوافق، مثل JDK 8.

2. **تحديد تثبيت Java**
   حدد مكان تثبيت نسخة متوافقة من Java (مثل JDK 1.8.0) على نظامك. المواقع الشائعة على Windows تشمل:
   - `C:\Program Files\Java\jdk1.8.0_XXX` (لJava 64-bit)
   - `C:\Program Files (x86)\Java\jdk1.8.0_XXX` (لJava 32-bit)
   استبدل `XXX` بالنسخة التحديثية المحددة (مثل `231` لـ JDK 1.8.0_231). داخل هذا المجلد، يوجد ملف `javaw.exe` في المجلد الفرعي `bin` (مثل `C:\Program Files\Java\jdk1.8.0_XXX\bin\javaw.exe`).

   **نصائح**: لتأكيد الإصدار والعمارة، افتح نافذة الأوامر، انتقل إلى المجلد `bin` (مثل `cd C:\Program Files\Java\jdk1.8.0_XXX\bin`), واكتب:
   ```
   java -version
   ```
   ابحث عن "64-Bit" أو "32-Bit" في الإخراج لتأكيد العمارة. تأكد من تطابقها مع إصدار Eclipse (likely 64-bit إذا تم تنزيله مؤخرًا).

3. **إيجاد ملف `eclipse.ini`**
   ملف `eclipse.ini` هو ملف تهيئة موجود في نفس المجلد الذي يحتوي على `eclipse.exe`. على سبيل المثال، إذا كان Eclipse مثبتًا في `C:\eclipse`، فسيكون الملف في `C:\eclipse\eclipse.ini`. هذا الملف يسمح لك بتحديد JVM التي يجب أن تستخدمها Eclipse.

4. **تحرير ملف `eclipse.ini`**
   افتح `eclipse.ini` في محرر نص (مثل Notepad) مع صلاحيات إدارية. ستعدل الملف لتضمن حجة `-vm` التي تحدد JVM التي يجب أن تستخدمها Eclipse. اتبع هذه الخطوات:

   - **تحقق من المحتوى الحالي**: ابحث عن حجة `-vm`. إذا كانت موجودة بالفعل، فستكون متبوعة بمسار في السطر التالي (مثل `-vm` متبوعًا بـ `C:/some/path/bin/javaw.exe`). إذا كانت تشير إلى `Oracle\Java\javapath\javaw.exe` المشكل، فستبدلها. إذا لم توجد حجة `-vm`، فستضيفها.
   - **إضافة أو تعديل حجة `-vm`**: أضف السطرين التاليين قبل قسم `-vmargs` (إذا كان موجودًا) أو بالقرب من أعلى الملف بعد متغيرات التشغيل الأولية:
     ```
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     ```
     - استخدم فاصلًا (`/`) بدلاً من فاصل (`\`) لتجنب مشاكل في التحليل.
     - استبدل `C:/Program Files/Java/jdk1.8.0_XXX` بالمسار الفعلي لتثبيت Java.
   - **تأكد من وضع صحيح**: يجب أن تظهر حجة `-vm` قبل قسم `-vmargs`، الذي يبدأ عادةً بـ `-vmargs` متبوعًا بأوامر JVM مثل `-Xms256m` أو `-Xmx1024m`. على سبيل المثال، قد يبدو ملف `eclipse.ini` بعد التعديل كالتالي:
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
   - **تجنب المسافات أو السطور الفارغة الزائدة**: تأكد من عدم وجود مسافات أو سطور فارغة غير ضرورية مباشرة بعد `-vm` أو سطور المسار، لأن هذا قد يسبب Eclipse في تفسير التهيئة بشكل خاطئ.

5. **حفظ وتجربة**
   احفظ ملف `eclipse.ini`، ثم انقر على `eclipse.exe` لبدء Eclipse. إذا تم التهيئة بشكل صحيح، فسيبدأ Eclipse بدون الخطأ "Java was started but returned exit code".

### ملاحظات إضافية
- **تطابق العمارة**: تأكد من تطابق عمارة JVM (32-bit أو 64-bit) مع تثبيت Eclipse. يتطلب Eclipse 64-bit JVM 64-bit، عادةً ما يتم العثور عليه في `C:\Program Files\Java`، بينما يتطلب Eclipse 32-bit JVM 32-bit من `C:\Program Files (x86)\Java`.
- **تحقق من المسار**: تأكد من وجود `javaw.exe` في الموقع المحدد. إذا كان المسار غير صحيح، فلن يبدأ Eclipse.
- **خيار احتياطي**: إذا لم يعمل هذا، فاعتبر تعيين متغير `JAVA_HOME` (مثل `C:\Program Files\Java\jdk1.8.0_XXX`) وتحديث المسار النظامي لتضمين `%JAVA_HOME%\bin`. ومع ذلك، تعد تعديل `eclipse.ini` هو الطريقة المفضل والموثوق بها لـ Eclipse.

بتعديل ملف `eclipse.ini` لتضمن حجة `-vm` مع مسار `javaw.exe` متوافق، فإنك تحدد المنزل Java لـ Eclipse بشكل فعال، مما يضمن استخدام JVM الصحيح للبدء.