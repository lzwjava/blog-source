---
audio: false
lang: ar
layout: post
title: رنتايمات جاڤا في فيجوال ستوديو كود
translated: true
---

لاستخدام `java.configuration.runtimes` في إعدادات Visual Studio Code (VS Code)، يجب عليك تهيئته في ملف `settings.json` الخاص بك. تسمح هذه الإعدادة لك بتحديد عدة إصدارات من Java Development Kit (JDK) يمكن أن يستخدمها VS Code لمشاريعك Java. وهي مفيدة بشكل خاص عند العمل مع مشاريع مختلفة تتطلب إصدارات Java محددة. إليك دليل خطوة بخطوة لتكوينها:

### خطوات تكوين `java.configuration.runtimes`

1. **فتح إعدادات VS Code**:
   - على Windows/Linux: اذهب إلى `File > Preferences > Settings` أو اضغط على `Ctrl + ,`.
   - على macOS: اذهب إلى `Code > Preferences > Settings` أو اضغط على `Cmd + ,`.

2. **الوصول إلى ملف إعدادات JSON**:
   - في واجهة الإعدادات، ابحث عن `java.configuration.runtimes`.
   - ستجد خيارًا مثل "Java: Configuration: Runtimes". انقر على "Edit in settings.json" (عادة ما يكون رابطًا أسفل وصف الإعداد) لتفتح ملف `settings.json`.

3. **تحرير `settings.json`**:
   - في ملف `settings.json`، أضف أو تعديل مصفوفة `java.configuration.runtimes`. تحتوي هذه المصفوفة على كائنات، كل منها يمثل إصدارًا من JDK تريد VS Code أن يعترف به.
   - تحتوي كل كائن عادةً على:
     - `name`: معرف إصدار Java (مثل `JavaSE-1.8`, `JavaSE-11`, `JavaSE-17`).
     - `path`: المسار المطلق إلى دليل تثبيت JDK على نظامك.
     - `default` (اختياري): قم بتعيينه إلى `true` لجعل هذا JDK الافتراضي لمجلدات غير المدارة (المشاريع بدون أدوات بناء مثل Maven أو Gradle).

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
   - تأكد من أن `path` يشير إلى دليل الجذر لتثبيت JDK الخاص بك (مثل حيث يوجد مجلد `bin` يحتوي على `java.exe` أو `java`).
   - على Windows، استخدم شريطين مائلين (`/`) أو شريطين مائلين مفرطين (`\\`) في المسار.
   - على macOS/Linux، استخدم المسار المناسب للنظام الملفات (مثل `/usr/lib/jvm/java-17-openjdk`).

5. **حفظ وتحديث**:
   - احفظ ملف `settings.json`.
   - أعيد تشغيل VS Code أو اعد تحميل النافذة (`Ctrl + R` أو `Cmd + R`) لتطبيق التغييرات.

6. **تحقق من التكوين**:
   - افتح لوحة الأوامر (`Ctrl + Shift + P` أو `Cmd + Shift + P`) واسحب الأمر `Java: Configure Java Runtime`.
   - هذا يفتح عرضًا يظهر JDKs المتاحة لمشاريعك. تأكد من أن الإصدارات المحدد لها تظهر تحت علامة التبويب "Project JDKs".

### كيفية العمل
- **مجلدات غير المدارة**: لمشاريع بدون أدوات بناء (مثل ملفات Java البسيطة)، يستخدم VS Code JDK الافتراضي المحدد في `java.configuration.runtimes`.
- **المشاريع المدارة (Maven/Gradle)**: لمشاريع مع أدوات بناء، يتم تحديد إصدار JDK بواسطة تكوين البناء (مثل `pom.xml` أو `build.gradle`), ولكن VS Code سيستمر في التعرف على الإصدارات المدرجة هنا للتوافق.
- **خادم اللغة**: يتطلب خادم لغة Java (جزء من الإضافات Java) JDK 17+ للعمل. يمكنك تحديد هذا بشكل منفصل باستخدام `java.jdt.ls.java.home` إذا لزم الأمر (مثل `"java.jdt.ls.java.home": "C:/Program Files/Java/jdk-17.0.6"`).

### مثال مع عدة JDKs
إذا كنت على Mac و لديك JDK 8 و 17 مثبتين عبر Homebrew، قد يبدو التكوين كالتالي:

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
- استخدم الصيغة الصحيحة للاسم (`JavaSE-<version>`)، متطابقًا مع إصدار Java (مثل `JavaSE-11` لـ Java 11).
- إذا كنت تمتلك JDK واحد فقط، يمكنك إدراجه لضمان استخدامه بشكل صريح من قبل VS Code.
- لتحديد مسار JDK، قم بتشغيل `java -version` في شريط الأوامر وتحقق من دليل التثبيت (مثل `where java` على Windows أو `which java` على أنظمة Unix، ثم تتبع إلى الجذر JDK).

يوفر هذا التكوين لك مرونة للعمل مع عدة إصدارات من Java في VS Code بسهولة! اتصل بي إذا كنت بحاجة إلى مساعدة في العثور على مسارات JDK أو حل المشاكل.