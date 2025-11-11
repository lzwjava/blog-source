---
audio: false
generated: true
lang: ar
layout: post
title: خادم لغة جافا وبناء مافن
translated: true
type: note
---

يبدو أنك تواجه مشكلتين مرتبطتين في Visual Studio Code (VSCode): شكوى حول الحاجة إلى Java 21 على الأقل، ومشاكل في عدم تعرف VSCode على بعض تعريفات الكائنات في كود Java الخاص بك، على الرغم من أن بناء Maven الخاص بك يتم بنجاح. دعنا نحل هذه المشكلة خطوة بخطوة.

تنشأ المشكلة لأن امتدادات Java في VSCode (على وجه التحديد Java Language Server) وبناء Maven قد لا يكونان متوافقين من حيث إصدار Java Development Kit (JDK) أو تكوين المشروع. يشير VSCode إلى أنه يحتاج إلى JDK 21 ليعمل بشكل صحيح، وتشير أخطاء التحليل إلى أنه لا يفسر الكود الخاص بنفس الطريقة التي يفعلها Maven. إليك كيفية الإصلاح:

---

### الخطوة 1: تثبيت JDK 21
بما أن VSCode يطلب صراحة Java 21، ستحتاج إلى التأكد من تثبيتها على نظامك.

- **تحميل JDK 21**: احصل عليه من مصدر موثوق مثل [موقع Oracle](https://www.oracle.com/java/technologies/javase-jdk21-downloads.html) أو [Adoptium](https://adoptium.net/).
- **ثبته**: اتبع تعليمات التثبيت ولاحظ مسار التثبيت (مثال: `C:\Program Files\Java\jdk-21` على Windows أو `/usr/lib/jvm/java-21-openjdk` على Linux).
- **تحقق**: افتح طرفية وقم بتشغيل `java -version`. يجب أن ترى شيئًا مثل:
  ```
  java version "21.0.1" ...
  ```

---

### الخطوة 2: تكوين VSCode لاستخدام JDK 21
تحتاج إلى إخبار امتدادات Java في VSCode باستخدام JDK 21. إليك الطريقة:

1. **افتح إعدادات VSCode**:
   - اذهب إلى `File > Preferences > Settings` (أو اضغط `Ctrl + ,`).
2. **عيّن مسار JDK**:
   - ابحث عن `java.jdt.ls.java.home`.
   - أدخل المسار إلى تثبيت JDK 21 الخاص بك (مثال: `C:\Program Files\Java\jdk-21`).
   - اختياريًا، ابحث عن `java.home` وعيّنه لنفس المسار من أجل التناسق.
3. **عدّل `settings.json` (بديل)**:
   - افتح Command Palette (`Ctrl + Shift + P`)، اكتب "Preferences: Open Settings (JSON)"، وأضف:
     ```json
     {
         "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-21",
         "java.home": "C:\\Program Files\\Java\\jdk-21"
     }
     ```
   - اضبط المسار بناءً على نظامك (استخدم الشرطة المائلة `/` لنظام Linux/Mac).

هذا يضمن أن Java Language Server في VSCode يستخدم JDK 21، مما يحقق الحد الأدنى من المتطلبات.

---

### الخطوة 3: عيّن JDK المشروع في VSCode
لإصلاح مشاكل التحليل (مثال: عدم العثور على تعريفات الكائنات)، تأكد من أن مشروعك في VSCode يستخدم JDK 21 أيضًا:

- في `settings.json`، أضف ما يلي لتحديد JDK 21 لمشروعك:
  ```json
  "java.configuration.runtimes": [
      {
          "name": "JavaSE-21",
          "path": "C:\\Program Files\\Java\\jdk-21",
          "default": true
      }
  ]
  ```
- هذا يُحاذي وقت تشغيل المشروع في VSCode مع JDK 21، مما ينبغي أن يساعده في تحليل الكود الخاص بك بشكل صحيح.

---

### الخطوة 4: التحقق من تكوين JDK لـ Maven
بما أن بناء Maven (`mvn compile`) يعمل بشكل جيد، فمن المرجح أنه يستخدم JDK متوافق. دعنا نؤكد ذلك ونوافقه مع VSCode:

1. **تحقق من JDK الخاص بـ Maven**:
   - شغّل `mvn -version` في طرفيتك. ابحث عن سطر "Java version" (مثال: `Java version: 21.0.1`).
   - إذا لم يكن يستخدم JDK 21، عيّن متغير البيئة `JAVA_HOME` ليشير إلى مسار JDK 21 الخاص بك:
     - **Windows**: `set JAVA_HOME=C:\Program Files\Java\jdk-21`
     - **Linux/Mac**: `export JAVA_HOME=/usr/lib/jvm/java-21-openjdk`
   - شغّل `mvn -version` مرة أخرى للتأكد.
2. **حدد JDK في `pom.xml`** (اختياري):
   - إذا كنت تريد فرض استخدام JDK 21 في مشروع Maven الخاص بك، أضف هذا إلى `pom.xml`:
     ```xml
     <properties>
         <maven.compiler.source>21</maven.compiler.source>
         <maven.compiler.target>21</maven.compiler.target>
     </properties>
     ```

---

### الخطوة 5: تحديث VSCode
بعد إجراء هذه التغييرات، يحتاج VSCode إلى تحديث لتطبيقها:

- أعِد تحميل VSCode:
  - افتح Command Palette (`Ctrl + Shift + P`) واختر "Developer: Reload Window".
- بديلًا عن ذلك، أغلق VSCode وأعِد فتحه.

---

### الخطوة 6: تأكد من تحميل التبعيات
إذا كان VSCode لا يزال غير قادر على العثور على تعريفات الكائنات، فقد لا يكون قد حمّل تبعيات Maven بشكل صحيح:

1. **نظّف مساحة العمل**:
   - افتح Command Palette (`Ctrl + Shift + P`).
   - شغّل "Java: Clean Java Language Server Workspace".
2. **فرض الترجمة**:
   - شغّل "Java: Force Java Compilation" من Command Palette.
3. **تحقق من الاستيرادات**:
   - تأكد من استيراد تبعيات Maven الخاصة بمشروعك عن طريق النقر بزر الماوس الأيمن على `pom.xml` في VSCode واختيار "Update Project Configuration".

---

### استكشاف الأخطاء وإصلاحها
إذا استمرت المشكلة:
- **تحقق من السجلات**:
  - أضف `"java.trace.server": "verbose"` إلى `settings.json`.
  - افتح لوحة Output (`Ctrl + Shift + U`) واختر "Java Language Server" لعرض السجلات التفصيلية.
- **تحقق من الكود**:
  - تأكد مرة أخرى من أن تعريفات الكائنات المفقودة هي من الكود الخاص بك أو من التبعيات المدرجة في `pom.xml`، وليست مشاكل خارجية.

---

### الملخص
من خلال تثبيت JDK 21، وتكوين VSCode لاستخدامه، ومحاذاة إعدادات مشروعك وMaven، وتحديث البيئة، يجب أن يتوقف VSCode عن الشكوى بشأن Java 21 ويقوم بتحليل الكود الخاص بك بشكل صحيح، بما يتطابق مع نجاح ترجمة Maven. أعلمني إذا واجهت أي عقبات!