---
audio: false
generated: true
lang: ar
layout: post
title: تهيئة الوكيل لـ Gradle في VSCode
translated: true
type: note
---

لتكوين وكيل لـ Gradle في Visual Studio Code (VSCode) حتى يتمكن من تنزيل التبعيات عبر الوكيل، تحتاج إلى إعداد إعدادات الوكيل في تكوين Gradle. يستخدم Gradle ملف خصائص لإدارة مثل هذه الإعدادات، ويعتمد VSCode على نظام بناء Gradle لمشاريع Gradle. إليك كيفية القيام بذلك:

### خطوات تكوين الوكيل لـ Gradle في VSCode

1.  **تحديد موقع أو إنشاء ملف خصائص Gradle**
    - يستخدم Gradle ملفًا يسمى `gradle.properties` لتخزين إعدادات التكوين العامة.
    - يوجد هذا الملف عادةً في دليل المستخدم الرئيسي لـ Gradle:
        - في Windows: `C:\Users\<اسم_المستخدم>\.gradle\gradle.properties`
        - في macOS/Linux: `~/.gradle/gradle.properties`
    - إذا كان الملف غير موجود، قم بإنشائه في الموقع المذكور أعلاه.

2.  **إضافة إعدادات الوكيل إلى `gradle.properties`**
    - افتح ملف `gradle.properties` في محرر نصوص.
    - أضف الأسطر التالية، مع استبدال العناصر النائبة (`<proxyHost>`, `<proxyPort>`, `<username>`, `<password>`) ببيانات الوكيل الفعلية الخاصة بك:
        ```
        systemProp.http.proxyHost=<proxyHost>
        systemProp.http.proxyPort=<proxyPort>
        systemProp.http.proxyUser=<username>
        systemProp.http.proxyPassword=<password>
        systemProp.https.proxyHost=<proxyHost>
        systemProp.https.proxyPort=<proxyPort>
        systemProp.https.proxyUser=<username>
        systemProp.https.proxyPassword=<password>
        ```
    - مثال بقيم حقيقية:
        ```
        systemProp.http.proxyHost=proxy.example.com
        systemProp.http.proxyPort=8080
        systemProp.http.proxyUser=myuser
        systemProp.http.proxyPassword=mypassword
        systemProp.https.proxyHost=proxy.example.com
        systemProp.https.proxyPort=8080
        systemProp.https.proxyUser=myuser
        systemProp.https.proxyPassword=mypassword
        ```
    - إذا كان الوكيل الخاص بك لا يتطلب المصادقة (اسم مستخدم/كلمة مرور)، يمكنك حذف سطري `proxyUser` و `proxyPassword`.

3.  **اختياري: تكوين الوكيل لكل مشروع**
    - إذا كنت تريد تطبيق إعدادات الوكيل على مشروع محدد فقط (بدلاً من تطبيقها عالميًا)، يمكنك إضافة ملف `gradle.properties` إلى الدليل الجذري لمشروعك (على سبيل المثال، `<project-root>/gradle.properties`) بنفس المحتوى المذكور أعلاه.

4.  **التحقق من استخدام Gradle للوكيل**
    - افتح مشروع Gradle الخاص بك في VSCode.
    - قم بتشغيل مهمة بناء (مثل `gradle build`) عبر طرفية VSCode أو امتداد Gradle.
    - يجب أن يقوم Gradle الآن بتوجيه تنزيلاته (مثل التبعيات من الموقع الرسمي) عبر الوكيل المحدد.

5.  **ملاحظات خاصة بـ VSCode**
    - تأكد من تثبيت **Java Extension Pack** وامتداد **Gradle for Java** في VSCode، حيث إنهما يعززان دعم مشاريع Gradle.
    - إذا كانت VSCode لا تزال تواجه مشاكل، فتحقق من أن وقت تشغيل Java (الذي يستخدمه Gradle) يحترم إعدادات الوكيل أيضًا. قد تحتاج إلى تعيين وسيطات JVM للوكيل:
        - في VSCode، انتقل إلى `File > Preferences > Settings`.
        - ابحث عن `java.gradle.build.jvmArguments`.
        - أضف شيئًا مشابهًا لما يلي:
            ```
            -Dhttp.proxyHost=<proxyHost> -Dhttp.proxyPort=<proxyPort> -Dhttps.proxyHost=<proxyHost> -Dhttps.proxyPort=<proxyPort>
            ```

6.  **اختبار التكوين**
    - أعد تحميل مشروعك في VSCode (على سبيل المثال، أغلقه وأعد فتحه أو استخدم زر "Refresh" في الشريط الجانبي لـ Gradle).
    - قم بتشغيل مهمة Gradle (مثل `gradle build` أو `gradle dependencies`) للتأكد من أنه يقوم بتنزيل الملفات عبر الوكيل.

### استكشاف الأخطاء وإصلاحها
-   **التحقق من تفاصيل الوكيل**: تأكد من صحة مضيف الوكيل ومنفذه وبيانات الاعتماد الخاصة بك.
-   **جدار الحماية أو الشبكة**: إذا استمر الفشل، قد يقوم الوكيل أو الشبكة بحجب عناوين URL محددة لـ Gradle (مثل `https://services.gradle.org`). اختبر باستخدام أمر مثل `curl` أو استشر مسؤول الشبكة.
-   **نتائج مفصلة**: قم بتشغيل Gradle مع `--debug` أو `--info` (على سبيل المثال، `gradle build --debug`) في طرفية VSCode لرؤية سجلات مفصلة حول طلبات الشبكة.

يجب أن يسمح هذا الإعداد لـ Gradle في VSCode بتنزيل التبعيات عبر الوكيل الخاص بك بنجاح.