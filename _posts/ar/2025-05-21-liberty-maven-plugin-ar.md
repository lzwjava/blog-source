---
audio: false
generated: true
lang: ar
layout: post
title: إضافة موفن للتحرر
translated: true
type: note
---

لتحقيق هدفك المتمثل في تشغيل سكريبت في IntelliJ IDEA على نظام Windows يدير بسرعة خادم Liberty ويبني برنامجك، مع ضمان توقف الخادم قبل استبدال ملف EAR، أوصي باستخدام **Liberty Maven Plugin**. هذا النهج مباشر، ويتكامل جيدًا مع عملية البناء Maven الخاصة بك، ويتجنب المشكلات التي واجهتها مع تنسيق الأوامر وملفات الدُفعة.

إليك كيفية إعداده:

---

### الحل: استخدام Liberty Maven Plugin

#### الخطوة 1: إضافة Liberty Maven Plugin إلى ملف `pom.xml` الخاص بك
يسمح لك Liberty Maven Plugin بالتحكم في خادم Liberty (بدء، إيقاف، نشر، إلخ) مباشرة من Maven، مما يلغي الحاجة إلى سكريبتات معقدة أو ملفات دُفعة.

- افتح ملف `pom.xml` الخاص بمشروعك.
- أضف تكوين الإضافة التالي داخل قسم `<build>`:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>io.openliberty.tools</groupId>
            <artifactId>liberty-maven-plugin</artifactId>
            <version>3.3.4</version>
            <configuration>
                <serverName>default</serverName>
                <installDirectory>C:\path\to\liberty</installDirectory>
            </configuration>
        </plugin>
    </plugins>
</build>
```

- **استبدل** `C:\path\to\liberty` بالمسار الفعلي لدليل تثبيت Liberty الخاص بك (مثال: `C:\Program Files\IBM\WebSphere\Liberty`).
- الـ `<serverName>default</serverName>` يتطابق مع استخدامك لـ `default` في أوامر `server start default` و `server stop default`.

#### الخطوة 2: إنشاء تكوين تشغيل Maven في IntelliJ IDEA
بدلاً من استخدام سكريبت أو ملف دُفعة، يمكنك تكوين IntelliJ IDEA لتشغيل سلسلة من أهداف Maven التي توقف الخادم، تبني مشروعك، ثم تبدأ الخادم مرة أخرى.

- في IntelliJ IDEA، انتقل إلى **Run > Edit Configurations...**.
- انقر على زر **+** واختر **Maven** من القائمة.
- قم بتكوين تشغيل Maven:
  - **Name:** امنحه اسمًا ذو معنى، مثل `Run Liberty`.
  - **Working directory:** تأكد من تعيينه على دليل مشروعك (يتم اكتشافه تلقائيًا عادةً).
  - **Command line:** أدخل سلسلة أهداف Maven التالية:
    ```
    liberty:stop package liberty:start
    ```
- انقر على **Apply** ثم **OK**.

#### الخطوة 3: تشغيل التكوين
- استخدم زر **Run** (المثلث الأخضر) في IntelliJ IDEA لتنفيذ هذا التكوين.
- سيقوم هذا بما يلي:
  1. **إيقاف خادم Liberty** (`liberty:stop`): يضمن عدم تشغيل الخادم عند استبدال ملف EAR.
  2. **بناء مشروعك** (`package`): يشغل `mvn package` لتوليد ملف EAR.
  3. **بدء خادم Liberty** (`liberty:start`): يعيد تشغيل الخادم بملف EAR المحدث.

---

### لماذا هذا الحل يناسبك
- **يصلح مشاكل تنسيق الأوامر:** لقد ذكرت أن استخدام "Script text" في تكوين التشغيل يقسم `server start default` إلى وسيطات منفصلة (`server`, `start`, `default`). نهج Maven يتجنب هذا تمامًا باستخدام أهداف إضافة محددة جيدًا.
- **يتجنب تعقيد ملف الدُفعة:** وجدت صعوبة في جعل ملف `.bat` يعمل بشكل صحيح (مثلًا، بسبب المسارات أو إعدادات البيئة). يقوم Liberty Maven Plugin بإدارة الخادم داخليًا، لذا لا تحتاج إلى تصحيح أخطاء أوامر ملفات الدُفعة أو المسارات.
- **يلبي متطلباتك:** تحتاج إلى توقف الخادم عند استبدال ملف EAR لتجنب مشاكل البدء. هذا الحل يوقف الخادم صراحةً قبل البناء ويبدأه بعده، مما يضمن عملية نظيفة.

---

### بديل: استخدام ملف دُفعة (إذا كنت تفضل ذلك)
إذا كنت تفضل الالتزام بملف دُفعة، إليك مثالاً عمليًا، على الرغم من أنه غير موصى به بشدة بسبب المشكلات التي واجهتها:

1. أنشئ ملفًا باسم `runLiberty.bat` في دليل مشروعك بالمحتوى التالي:

```bat
@echo off
set LIBERTY_BIN=C:\path\to\liberty\bin
set MAVEN_HOME=C:\path\to\maven
set PATH=%PATH%;%LIBERTY_BIN%;%MAVEN_HOME%\bin

"%LIBERTY_BIN%\server" stop default
mvn package
"%LIBERTY_BIN%\server" start default
```

- استبدل `C:\path\to\liberty` و `C:\path\to\maven` بالمسارات الفعلية لتثبيتات Liberty و Maven الخاصة بك.

2. في IntelliJ IDEA:
   - انتقل إلى **Run > Edit Configurations...**.
   - انقر على **+** واختر **Batch file**.
   - عيّن **Path to batch file** على موقع ملف `runLiberty.bat`.
   - عيّن **Working directory** على دليل مشروعك.
   - انقر على **Apply** ثم **OK**.

3. قم بتشغيله باستخدام زر **Run**.

ومع ذلك، تتطلب هذه الطريقة منك التأكد يدويًا من صحة المسارات ومتغيرات البيئة، وهو ما وجدته صعبًا. نهج إضافة Maven أبسط وأكثر موثوقية.

---

### التوصية
استخدم طريقة **Liberty Maven Plugin** الموضحة أعلاه. إنها:
- **مدمجة:** ترتبط بعملية البناء Maven الحالية الخاصة بك.
- **بسيطة:** لا حاجة للتعامل مع صيغة ملفات الدُفعة أو المسارات.
- **موثوقة:** تتعامل مع إيقاف وبدء الخادم بشكل صحيح، مما يتجنب مشاكل استبدال ملف EAR.

هذا الإعداد سيمكنك من تشغيل برنامجك بسرعة وباتساق في IntelliJ IDEA على خادم Liberty الخاص بك!