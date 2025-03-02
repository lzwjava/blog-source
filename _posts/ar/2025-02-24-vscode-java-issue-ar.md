---
audio: false
generated: false
lang: ar
layout: post
title: مخدم لغة جاڤا ومبني مافن
translated: true
---

يبدو أنك تواجهين مشكلةين متعلقةين في Visual Studio Code (VSCode): شكوى حول الحاجة إلى Java 21 على الأقل، ومشاكل في عدم التعرف على بعض تعريفات الكائنات في كود Java الخاص بك، رغم أن بناء Maven الخاص بك ينجح. دعونا نحل هذه المشكلة خطوة بخطوة.

تحدث المشكلة لأن امتدادات Java في VSCode (خاصة Java Language Server) ومبنيك Maven قد لا يكونا متوافقين في ما يتعلق بنسخة Java Development Kit (JDK) أو تكوين المشروع. VSCode يشير إلى أنه يحتاج إلى JDK 21 للعمل بشكل صحيح، وتشير أخطاء التحليل إلى أنه لا يفهم كودك بنفس الطريقة التي يفهمها Maven. إليك كيفية إصلاح ذلك:

---

### الخطوة 1: تثبيت JDK 21
منذ أن يطلب VSCode Java 21 بشكل صريح، عليك التأكد من تثبيته على نظامك.

- **تحميل JDK 21**: احصل عليه من مصدر موثوق مثل [موقع Oracle](https://www.oracle.com/java/technologies/javase-jdk21-downloads.html) أو [Adoptium](https://adoptium.net/).
- **تثبيته**: اتبع تعليمات التثبيت واكتب مسار التثبيت (مثل `C:\Program Files\Java\jdk-21` في Windows أو `/usr/lib/jvm/java-21-openjdk` في Linux).
- **التحقق**: افتح نافذة الترمينال واكتب `java -version`. يجب أن ترى شيئًا مثل:
  ```
  java version "21.0.1" ...
  ```

---

### الخطوة 2: تكوين VSCode لاستخدام JDK 21
يجب أن تخبر امتدادات Java في VSCode باستخدام JDK 21. إليك كيفية ذلك:

1. **فتح إعدادات VSCode**:
   - اذهب إلى `File > Preferences > Settings` (أو اضغط على `Ctrl + ,`).
2. **تعيين مسار JDK**:
   - ابحث عن `java.jdt.ls.java.home`.
   - أدخل مسار تثبيت JDK 21 الخاص بك (مثل `C:\Program Files\Java\jdk-21`).
   - اختياريًا، ابحث عن `java.home` واكتب نفس المسار للتوافق.
3. **تحرير `settings.json` (بديل)**:
   - افتح لوحة الأوامر (`Ctrl + Shift + P`), اكتب “Preferences: Open Settings (JSON)”, واكتب:
     ```json
     {
         "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-21",
         "java.home": "C:\\Program Files\\Java\\jdk-21"
     }
     ```
   - قم بتعديل المسار بناءً على نظامك (استخدم شريطين مائلين `/` في Linux/Mac).

هذا يضمن أن Java Language Server في VSCode يستخدم JDK 21، مما يفي بالمتطلبات الدنيا.

---

### الخطوة 3: تعيين JDK للمشروع في VSCode
لإصلاح مشاكل التحليل (مثل عدم العثور على تعريفات الكائنات)، تأكد من أن مشروعك في VSCode يستخدم JDK 21 أيضًا:

- في `settings.json`, أضف التالي لتحديد JDK 21 لمشروعك:
  ```json
  "java.configuration.runtimes": [
      {
          "name": "JavaSE-21",
          "path": "C:\\Program Files\\Java\\jdk-21",
          "default": true
      }
  ]
  ```
- هذا يضمن أن زمن تشغيل مشروع VSCode متوافق مع JDK 21، مما يجب أن يساعد في تحليل كودك بشكل صحيح.

---

### الخطوة 4: التحقق من تكوين JDK في Maven
منذ أن يعمل بناء Maven (`mvn compile`) بشكل جيد، فهو يستخدم JDK متوافق. دعونا نؤكد ذلك ونؤكد توافقه مع VSCode:

1. **تحقق من JDK في Maven**:
   - اكتب `mvn -version` في نافذة الترمينال. ابحث عن سطر “Java version” (مثل `Java version: 21.0.1`).
   - إذا لم يكن يستخدم JDK 21، قم بتعيين متغير البيئة `JAVA_HOME` إلى مسار JDK 21 الخاص بك:
     - **Windows**: `set JAVA_HOME=C:\Program Files\Java\jdk-21`
     - **Linux/Mac**: `export JAVA_HOME=/usr/lib/jvm/java-21-openjdk`
   - اكتب `mvn -version` مرة أخرى للتأكيد.
2. **تعيين JDK في `pom.xml`** (اختياري):
   - إذا كنت تريد فرض JDK 21 في مشروع Maven الخاص بك، أضف هذا إلى `pom.xml`:
     ```xml
     <properties>
         <maven.compiler.source>21</maven.compiler.source>
         <maven.compiler.target>21</maven.compiler.target>
     </properties>
     ```

---

### الخطوة 5: تحديث VSCode
بعد إجراء هذه التغييرات، يحتاج VSCode إلى تحديث لتطبيقها:

- اعيد تحميل VSCode:
  - افتح لوحة الأوامر (`Ctrl + Shift + P`) واختر “Developer: Reload Window”.
- أو اغلق وافتح VSCode مرة أخرى.

---

### الخطوة 6: التأكد من تحميل الاعتماديات
إذا لم يستطع VSCode العثور على تعريفات الكائنات، فقد لا يكون قد تحميل الاعتماديات Maven بشكل صحيح:

1. **تنظيف مساحة العمل**:
   - افتح لوحة الأوامر (`Ctrl + Shift + P`).
   - اكتب “Java: Clean Java Language Server Workspace”.
2. **إجبار على التجميع**:
   - اكتب “Java: Force Java Compilation” من لوحة الأوامر.
3. **تحقق من الواردات**:
   - تأكد من أن اعتماديات مشروعك Maven تم استيرادها من خلال النقر باليمين على `pom.xml` في VSCode واختيار “Update Project Configuration”.

---

### حل المشاكل
إذا استمرت المشكلة:
- **تحقق من السجلات**:
  - أضف `"java.trace.server": "verbose"` إلى `settings.json`.
  - افتح لوحة الإخراج (`Ctrl + Shift + U`) واختر “Java Language Server” لمشاهدة السجلات التفصيلية.
- **تحقق من الكود**:
  - تأكد من أن تعريفات الكائنات المفقودة من كودك أو الاعتماديات المدرجة في `pom.xml`، وليس من مشاكل خارجية.

---

### ملخص
من خلال تثبيت JDK 21، تكوين VSCode لاستخدامه، وتوافق إعدادات المشروع ومبني Maven، يجب أن يتوقف VSCode عن الشكوى من Java 21 ويحلل كودك بشكل صحيح، متوافقًا مع بناء Maven الناجح. أخبرني إذا واجهت أي مشاكل!