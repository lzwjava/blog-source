---
audio: false
generated: true
lang: ar
layout: post
title: وقت تشغيل جافا في فيجوال ستوديو كود
translated: true
type: note
---

لاستخدام `java.configuration.runtimes` في إعدادات Visual Studio Code (VS Code)، تحتاج إلى تكوينه في ملف `settings.json` الخاص بك. يسمح لك هذا الإعداد بتحديد إصدارات متعددة من Java Development Kit (JDK) يمكن لـ VS Code استخدامها لمشاريع Java الخاصة بك. إنه مفيد بشكل خاص عند العمل مع مشاريع مختلفة تتطلب إصدارات محددة من Java. إليك دليل خطوة بخطوة لإعداده:

### خطوات تكوين `java.configuration.runtimes`

1. **افتح إعدادات VS Code**:
   - في Windows/Linux: انتقل إلى `File > Preferences > Settings` أو اضغط على `Ctrl + ,`.
   - في macOS: انتقل إلى `Code > Preferences > Settings` أو اضغط على `Cmd + ,`.

2. **الوصول إلى ملف إعدادات JSON**:
   - في واجهة مستخدم الإعدادات، ابحث عن `java.configuration.runtimes`.
   - سترى خيارًا مثل "Java: Configuration: Runtimes". انقر على "Edit in settings.json" (عادة ما يكون رابطًا أسفل وصف الإعداد) لفتح ملف `settings.json`.

3. **تحرير `settings.json`**:
   - في ملف `settings.json`، أضف أو عدّل مصفوفة `java.configuration.runtimes`. تحتوي هذه المصفوفة على كائنات، يمثل كل منها إصدار JDK تريد أن يتعرف عليه VS Code.
   - يتضمن كل كائن عادةً:
     - `name`: معرف إصدار Java (على سبيل المثال، `JavaSE-1.8`، `JavaSE-11`، `JavaSE-17`).
     - `path`: المسار المطلق لدليل تثبيت JDK على نظامك.
     - `default` (اختياري): اضبطه على `true` لجعل هذا الإصدار هو JDK الافتراضي للمجلدات غير المدارة (المشاريع بدون أدوات بناء مثل Maven أو Gradle).

   إليك مثال على التكوين:

   ```json
   {
       "java.configuration.runtimes": [
           {
               "name": "JavaSE-1.8",
               "path": "C:/Program Files/Java/jdk1.8.0_351",
               "default": true
           },
           {
               "name": "JavaSE-11",
               "path": "C:/Program Files/Java/jdk-11.0.15"
           },
           {
               "name": "JavaSE-17",
               "path": "C:/Program Files/Java/jdk-17.0.6"
           }
       ]
   }
   ```

4. **تحقق من مسارات JDK**:
   - تأكد من أن `path` يشير إلى الدليل الجذري لتثبيت JDK الخاص بك (على سبيل المثال، حيث يوجد مجلد `bin` الذي يحتوي على `java.exe` أو `java`).
   - في Windows، استخدم الشرطة المائلة للأمام (`/`) أو اهرب من الشرطة المائلة العكسية (`\\`) في المسار.
   - في macOS/Linux، استخدم مسار نظام الملفات المناسب (على سبيل المثال، `/usr/lib/jvm/java-17-openjdk`).

5. **احفظ وأعد التحميل**:
   - احفظ ملف `settings.json`.
   - أعد تشغيل VS Code أو أعد تحميل النافذة (`Ctrl + R` أو `Cmd + R`) لتطبيق التغييرات.

6. **تحقق من التكوين**:
   - افتح Command Palette (`Ctrl + Shift + P` أو `Cmd + Shift + P`) وشغّل الأمر `Java: Configure Java Runtime`.
   - يفتح هذا عرضًا يظهر JDKs المتاحة لمشاريعك. تحقق من ظهور وقت التشغيل الذي قمت بتكوينه تحت علامة التبويب "Project JDKs".

### كيف يعمل
- **المجلدات غير المدارة**: للمشاريع بدون أدوات بناء (على سبيل المثال، ملفات Java عادية)، يستخدم VS Code JDK الافتراضي المحدد في `java.configuration.runtimes`.
- **المشاريع المدارة (Maven/Gradle)**: للمشاريع التي تستخدم أدوات بناء، يتم تحديد إصدار JDK من خلال تكوين الأداة (على سبيل المثال، `pom.xml` أو `build.gradle`)، ولكن سيظل VS Code يتعرف على أوقات التشغيل المدرجة هنا لأغراض التوافق.
- **خادم اللغة**: يتطلب Java Language Server (جزء من إضافات Java) JDK 17+ لتشغيله. يمكنك تحديد هذا بشكل منفصل باستخدام `java.jdt.ls.java.home` إذا لزم الأمر (على سبيل المثال، `"java.jdt.ls.java.home": "C:/Program Files/Java/jdk-17.0.6"`).

### مثال مع عدة إصدارات من JDK
إذا كنت تستخدم جهاز Mac ولديك JDK 8 و 17 مثبتين عبر Homebrew، فقد يبدو التكوين الخاص بك كما يلي:

```json
{
    "java.configuration.runtimes": [
        {
            "name": "JavaSE-1.8",
            "path": "/Library/Java/JavaVirtualMachines/jdk1.8.0_351.jdk/Contents/Home",
            "default": true
        },
        {
            "name": "JavaSE-17",
            "path": "/Library/Java/JavaVirtualMachines/jdk-17.0.6.jdk/Contents/Home"
        }
    ]
}
```

### نصائح
- استخدم تنسيق `name` الصحيح (`JavaSE-<version>`)، مطابقًا لإصدار Java (على سبيل المثال، `JavaSE-11` لـ Java 11).
- إذا كان لديك JDK واحد فقط، فلا يزال بإمكانك إدراجه لضمان استخدام VS Code له بشكل صريح.
- للعثور على مسار JDK الخاص بك، شغّل `java -version` في الطرفية وتحقق من دليل التثبيت (على سبيل المثال، عبر `where java` في Windows أو `which java` في الأنظمة الشبيهة بـ Unix، ثم تتبع المسار للعودة إلى الجذر JDK).

يمنحك هذا الإعداد المرونة للعمل مع إصدارات متعددة من Java في VS Code بسلاسة! دعني أعلم إذا كنت بحاجة إلى مساعدة في العثور على مسارات JDK الخاصة بك أو استكشاف الأخطاء وإصلاحها.