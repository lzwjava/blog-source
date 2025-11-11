---
audio: false
generated: true
lang: ar
layout: post
title: تهيئة ملف launch.json لـ Spring Boot في VSCode
translated: true
type: note
---

لتكوين ملف `launch.json` لمشروع Maven Spring Boot في Visual Studio Code (VSCode)، تحتاج إلى إعداد تكوين تشغيل يسمح لـ VSCode بتشغيل وتصحيح تطبيقك باستخدام إضافات Java الخاصة به. فيما يلي دليل خطوة بخطوة لمساعدتك في تحقيق هذا.

### المتطلبات الأساسية
قبل المتابعة، تأكد من الآتي:
- لديك **Java Extension Pack** مثبتًا في VSCode. تتضمن هذه الحزمة إضافات أساسية مثل "Debugger for Java" و "Language Support for Java" من Red Hat، والتي توفر الدعم لتشغيل وتصحيح تطبيقات Java، بما في ذلك مشاريع Spring Boot.
- مشروع Spring Boot الخاص بك هو مشروع Maven يحتوي على ملف `pom.xml` صالح.
- يحتوي المشروع على فئة رئيسية مشروحة بـ `@SpringBootApplication`، والتي تحتوي على طريقة `main` لبدء التطبيق.

### خطوات تكوين `launch.json`
1. **تحديد موقع الفئة الرئيسية**
   - في مشروع Spring Boot نموذجي، توجد الفئة الرئيسية في دليل `src/main/java` ومشروحة بـ `@SpringBootApplication`. على سبيل المثال، قد تُسمى `com.example.demo.DemoApplication`.
   - افتح مشروعك في VSCode وتعرف على الاسم المؤهل بالكامل لهذه الفئة (مثال: `com.example.demo.DemoApplication`).

2. **تحديد اسم المشروع**
   - اسم المشروع في مشروع Maven يتوافق مع `artifactId` المحدد في ملف `pom.xml` الخاص بك.
   - افتح ملف `pom.xml` الخاص بك وابحث عن وسم `<artifactId>`. على سبيل المثال:
     ```xml
     <artifactId>demo</artifactId>
     ```
     هنا، سيكون اسم المشروع هو `demo`.

3. **افتح نافذة التصحيح**
   - في VSCode، انقر على أيقونة **Debug** في الشريط الجانبي الأيسر (أو اضغط `Ctrl+Shift+D` / `Cmd+Shift+D` على جهاز Mac).
   - انقر على أيقونة الترس ⚙️ بجوار القائمة المنسدلة "Run and Debug" لتكوين إعدادات التشغيل. إذا لم يكن `launch.json` موجودًا، سيطالبك VSCode بإنشاء واحد.

4. **إنشاء أو تعديل `launch.json`**
   - إذا طُلب منك اختيار بيئة، اختر **Java**. سيؤدي هذا إلى إنشاء ملف `launch.json` أساسي في مجلد `.vscode` الخاص بمشروعك.
   - افتح ملف `launch.json`. إذا كان موجودًا بالفعل، يمكنك تعديله مباشرة.

5. **إضافة تكوين تشغيل**
   - أضف التكوين التالي داخل المصفوفة `"configurations"` في `launch.json`. استبدل العناصر النائبة بتفاصيل مشروعك:
     ```json
     {
         "type": "java",
         "name": "Launch Spring Boot App",
         "request": "launch",
         "mainClass": "com.example.demo.DemoApplication",
         "projectName": "demo"
     }
     ```
     - **شرح الحقول:**
       - `"type": "java"`: يحدد أن هذا تكوين تشغيل Java.
       - `"name": "Launch Spring Boot App"`: اسم وصفي لهذا التكوين، سيظهر في القائمة المنسدلة للتصحيح.
       - `"request": "launch"`: يشير إلى أن VSCode يجب أن يشغل التطبيق (على عكس الالتحاق بعملية موجودة مسبقًا).
       - `"mainClass"`: الاسم المؤهل بالكامل لفئة Spring Boot الرئيسية الخاصة بك (مثال: `com.example.demo.DemoApplication`).
       - `"projectName"`: `artifactId` من ملف `pom.xml` الخاص بك (مثال: `demo`)، مما يساعد VSCode على تحديد موقع المشروع في الإعداد متعدد الوحدات.

   - إليك مثال لملف `launch.json` كامل بهذا التكوين:
     ```json
     {
         "version": "0.2.0",
         "configurations": [
             {
                 "type": "java",
                 "name": "Launch Spring Boot App",
                 "request": "launch",
                 "mainClass": "com.example.demo.DemoApplication",
                 "projectName": "demo"
             }
         ]
     }
     ```

6. **اختياري: إضافة وسيطات VM أو وسيطات البرنامج**
   - إذا كان تطبيقك يتطلب إعدادات إضافية (مثال: تفعيل ملف تعريف Spring)، يمكنك إضافتها باستخدام `"vmArgs"` أو `"args"`:
     - مثال مع ملف تعريف Spring:
       ```json
       {
           "type": "java",
           "name": "Launch Spring Boot App with Profile",
           "request": "launch",
           "mainClass": "com.example.demo.DemoApplication",
           "projectName": "demo",
           "vmArgs": "-Dspring.profiles.active=dev"
       }
       ```
       هذا يضبط خاصية `spring.profiles.active` على `dev`.
     - مثال مع وسيطات البرنامج:
       ```json
       "args": ["arg1", "arg2"]
       ```

7. **حفظ وتشغيل**
   - احفظ ملف `launch.json`.
   - ارجع إلى نافذة التصحيح، واختر **"Launch Spring Boot App"** من القائمة المنسدلة، وانقر على زر التشغيل الأخضر (أو اضغط `F5`).
   - سيقوم VSCode ببناء وتشغيل تطبيق Spring Boot الخاص بك باستخدام Maven وإضافة Java. يجب أن ترى سجلات بدء تشغيل Spring Boot في وحدة تحكم التصحيح.

### التحقق من التكوين
- إذا كان تطبيق Spring Boot الخاص بك هو تطبيق ويب، افتح متصفحًا وانتقل إلى `http://localhost:8080` (أو المنفذ المحدد في ملف `application.properties` أو `application.yml` الخاص بك) للتأكد من أنه يعمل.
- يمكنك أيضًا تعيين نقاط التوقف في الكود الخاص بك واستخدام أدوات التحكم في التصحيح (إيقاف مؤقت، التخطي، إلخ) لتصحيح تطبيقك.

### ملاحظات
- تقوم إضافات Java في VSCode تلقائيًا بإدارة classpath وعملية البناء بناءً على ملف `pom.xml` الخاص بك، لذلك لا تحتاج عادةً إلى تشغيل `mvn clean install` يدويًا مسبقًا.
- إذا كان مشروعك جزءًا من إعداد Maven متعدد الوحدات، فتأكد من تطابق `projectName` مع `artifactId` للوحدة الصحيحة.
- للتكوينات المتقدمة (مثال: أدوات العمل المخصصة أو مهام ما قبل التشغيل)، راجع [توثيق تصحيح Java في VSCode](https://code.visualstudio.com/docs/java/java-debugging).

مع هذا الإعداد، يجب أن يكون `launch.json` الخاص بك مُكونًا بشكل صحيح لتشغيل وتصحيح مشروع Maven Spring Boot الخاص بك في VSCode!