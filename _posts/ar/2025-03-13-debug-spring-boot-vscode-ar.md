---
audio: false
generated: true
lang: ar
layout: post
title: تصحيح أخطاء تطبيقات Spring Boot في Visual Studio Code
translated: true
type: note
---

لتصحيح مشروع Maven Spring Boot في Visual Studio Code (VSCode)، يمكنك اتباع هذه الخطوات البسيطة لإعداد وتشغيل تطبيقك في وضع التصحيح. يفترض هذا الدليل أن لديك مشروع Maven Spring Boot أساسي يحتوي على ملف `pom.xml` وفئة رئيسية مشروحة بـ `@SpringBootApplication`. إليك الطريقة:

### الخطوة 1: تثبيت الامتدادات اللازمة
قبل أن تبدأ، تأكد من أن VSCode مجهز بالامتدادات المطلوبة لتطوير Java و Spring Boot:
- **Java Extension Pack**: يتضمن هذا الحزمة أدوات أساسية مثل Language Support for Java من Red Hat، والتي توفر إمكانيات التصحيح، إلى جانب أدوات أخرى لتطوير Java.
- **Spring Boot Extension Pack**: تعزز هذه الحزمة تطوير Spring Boot بميزات مثل Spring Boot Dashboard، وSpring Boot Tools، والمزيد.

لتثبيت هذه الحزمة:
1. افتح VSCode.
2. انتقل إلى عرض الامتدادات (`Ctrl+Shift+X` أو `Cmd+Shift+X` على نظام macOS).
3. ابحث عن "Java Extension Pack" و "Spring Boot Extension Pack"، ثم انقر فوق **تثبيت** لكل منهما.

### الخطوة 2: افتح مشروع Maven Spring Boot الخاص بك
- شغّل VSCode وافتح مجلد مشروعك عن طريق تحديد **File > Open Folder** واختيار الدليل الذي يحتوي على ملف `pom.xml` الخاص بك.
- سيكتشف VSCode ملف `pom.xml`، وستقوم حزمة Java Extension Pack تلقائيًا بفهرسة المشروع وحل التبعيات. قد يستغرق هذا بعض الوقت، لذا انتظر حتى تكتمل العملية (سترى التقدم في شريط الحالة في الأسفل يمين).

### الخطوة 3: إنشاء أو تحرير ملف `launch.json`
لتكوين التصحيح، تحتاج إلى إعداد ملف `launch.json` في VSCode:
1. افتح عرض **Run and Debug** بالنقر على أيقونة الخلل والتشغيل في الشريط الجانبي أو بالضغط على `Ctrl+Shift+D`.
2. إذا لم يكن هناك تكوين تصحيح موجود، انقر فوق **"create a launch.json file"**. إذا كان هناك تكوين موجود بالفعل، انقر على أيقونة الترس لتحريره.
3. عند المطالبة، اختر **Java** كبيئة التشغيل. سينشئ VSCode ملف `launch.json` افتراضيًا في مجلد `.vscode` داخل مشروعك.
4. أضف أو عدّل تكوين التصحيح لتطبيق Spring Boot الخاص بك. إليك مثال على التكوين:

    ```json
    {
        "type": "java",
        "name": "Debug Spring Boot",
        "request": "launch",
        "mainClass": "com.example.demo.DemoApplication",
        "projectName": "demo"
    }
    ```

    - استبدل `"com.example.demo.DemoApplication"` بالاسم المؤهل الكامل للفئة الرئيسية الخاصة بك (على سبيل المثال، `com.yourcompany.yourapp.YourApplication`).
    - استبدل `"demo"` باسم مشروعك، وهو عادةً `<artifactId>` من ملف `pom.xml` الخاص بك.

5. احفظ ملف `launch.json`.

#### اختياري: إضافة وسائط
إذا كان تطبيقك يتطلب وسائط محددة (مثل ملفات تعريف Spring)، يمكنك تضمينها:
```json
{
    "type": "java",
    "name": "Debug Spring Boot",
    "request": "launch",
    "mainClass": "com.example.demo.DemoApplication",
    "projectName": "demo",
    "args": "--spring.profiles.active=dev"
}
```

### الخطوة 4: بدء التصحيح
- في عرض **Run and Debug**، اختر **"Debug Spring Boot"** من القائمة المنسدلة في الأعلى.
- انقر فوق زر التشغيل الأخضر (أو اضغط `F5`) لإطلاق التطبيق في وضع التصحيح.
- سيقوم VSCode بتجميع المشروع باستخدام Maven، وتشغيل تطبيق Spring Boot، وإرفاق أداة التصحيح تلقائيًا.

### الخطوة 5: تعيين نقاط التوقف والتصحيح
- افتح ملف Java في مشروعك (على سبيل المثال، فئة متحكم أو خدمة).
- عيّن نقاط التوقف بالنقر في الهامش إلى يسار أرقام الأسطر، حيث ستظهر نقطة حمراء.
- تفاعل مع تطبيقك (على سبيل المثال، عبر متصفح أو عميل API). عندما يصل التنفيذ إلى نقطة توقف، سيوقف VSCode التنفيذ، مما يسمح لك بما يلي:
  - فحص المتغيرات في لوحة **Variables**.
  - التحرّق خلال الكود باستخدام عناصر التحكم مثل **Step Over** (`F10`)، أو **Step Into** (`F11`)، أو **Continue** (`F5`).
  - عرض مكدس الاستدعاءات والمزيد في الشريط الجانبي للتصحيح.

### طرق بديلة
بينما تُوصى طريقة `launch.json` لمرونتها، يمكنك أيضًا التصحيح باستخدام:
- **Maven View**:
  1. افتح عرض Maven في الشريط الجانبي (ابحث عن أيقونة "M" أو قم بتمكينه عبر الامتدادات).
  2. وسّع مشروعك، وانتقل إلى `spring-boot` تحت Plugins، انقر بزر الماوس الأيمن فوق `spring-boot:run`، وحدد **Debug**.
  3. سيبدأ التطبيق، وسيتم إرفاق أداة التصحيح.
- **Spring Boot Dashboard**:
  1. افتح Spring Boot Dashboard (عادة في عرض Explorer أو عبر命令 Palette: `Spring Boot Dashboard`).
  2. حدد موقع تطبيقك، انقر عليه بزر الماوس الأيمن، وحدد **Debug** (إذا كان متاحًا).

### المتطلبات الأساسية والملاحظات
- تأكد من تثبيت **Maven** على نظامك وأنه يمكن الوصول إليه عبر سطر الأوامر، أو اعتمد على Membedded Maven في VSCode (تم تكوينه عبر الإعدادات إذا لزم الأمر).
- تحقق من أن مشروعك يُبنى بنجاح (`mvn clean install`) لتجنب أخطاء وقت التشغيل أثناء التصحيح.
- استخدم إصدار Java متوافقًا كما هو محدد في ملف `pom.xml` الخاص بك (على سبيل المثال، عبر `<java.version>`).

باتباع هذه الخطوات، يمكنك تصحيح مشروع Maven Spring Boot الخاص بك بشكل فعال في VSCode، والاستفادة من أدوات التصحيح القوية لتحديد المشكلات في الكود الخاص بك وحلها.