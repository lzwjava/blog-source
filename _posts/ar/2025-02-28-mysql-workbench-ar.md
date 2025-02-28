---
audio: false
lang: ar
layout: post
title: استخدام MySQL Workbench
translated: true
---

### النقاط الرئيسية
- MySQL Workbench هو أداة مجانية ومفتوحة المصدر لإدارة قواعد البيانات MySQL، متاحة على Windows، macOS، وLinux.
- يمكنك تحميلها من الموقع الرسمي، وتثبيتها، وإعداد اتصال باستخدام تفاصيل الخادم مثل اسم المضيف والمستخدم.
- تشير الأبحاث إلى أن يمكنك إنشاء قواعد البيانات، الجداول، وتنفيد الاستعلامات باستخدام الطرق الرسومية والSQL.
- تشير الأدلة إلى أن لديها ميزات متقدمة مثل نمذجة البيانات وإدارة الخادم، والتي قد تكون غير متوقعة للمبتدئين.

### ما هو MySQL Workbench؟
MySQL Workbench هو أداة تساعدك على تصميم، تطوير، وإدارة قواعد البيانات MySQL. إنه مجاني ومفتوح المصدر، ويعمل على Windows، macOS، وLinux، مما يجعله متاحًا لمستخدمين كثيرين. يوفر واجهة رسومية، مما يعني أنك لا تحتاج دائمًا إلى كتابة الكود لإدارة قواعد البيانات، ولكن يمكنك ذلك إذا كنت تفضل ذلك.

### البدء
لبدء العمل، زور الصفحة الرسمية لتحميل من [https://www.mysql.com/products/workbench/](https://www.mysql.com/products/workbench/) واحصل على الإصدار المناسب لنظام التشغيل الخاص بك. اتبع خطوات التثبيت التي يتم تقديمها، والتي هي بسيطة ومتطابقة عبر المنصات.

### الإعداد والاستخدام
بعد التثبيت، افتح MySQL Workbench وانشئ اتصالًا جديدًا عن طريق النقر على زر '+' بجوار "MySQL Connections." ستحتاج إلى تفاصيل مثل اسم المضيف للخادم، الميناء (عادة 3306)، اسم المستخدم، وكلمة المرور. اختبر الاتصال لضمان عمله.

بعد الاتصال، يمكنك:
- **إنشاء قاعدة بيانات:** استخدم محرر SQL لإجراء `CREATE DATABASE database_name;` أو انقر بالزر الأيمن على "Schemas" واختر "Create Schema..."
- **إنشاء جدول:** أكتب بيان CREATE TABLE في محرر SQL أو استخدم الخيار الرسومي عن طريق النقر بالزر الأيمن على قاعدة البيانات.
- **تنفيذ الاستعلامات:** أكتب استعلام SQL في محرر SQL ونفذه لرؤية النتائج.

### الميزات المتقدمة
بخلاف الأساسيات، يوفر MySQL Workbench ميزات غير متوقعة مثل نمذجة البيانات، حيث يمكنك تصميم قاعدة البيانات بصورًا باستخدام مخططات ER، وأدوات لإدارة الخادم مثل إدارة المستخدمين والإعدادات. يمكن استكشاف هذه الميزات من خلال علامة التبويب "Model" وأخرى.

---

### ملاحظة الاستطلاع: دليل شامل لاستخدام MySQL Workbench

يقدم هذا القسم استكشافًا مفصلًا لاستخدام MySQL Workbench، ويوسع على الإجابة المباشرة مع سياق وتفاصيل فنية إضافية. يهدف إلى تغطية جميع الجوانب التي تم بحثها، مما يضمن فهمًا شاملًا للمستخدمين في مختلف مستويات الخبرة.

#### مقدمة إلى MySQL Workbench
MySQL Workbench يُصف بأنه أداة بصريّة موحدة للمهندسين المعماريين للبيانات، المطورين، ومديري قواعد البيانات (DBAs). إنه مجاني ومفتوح المصدر، متاح على أنظمة التشغيل الرئيسية بما في ذلك Windows، macOS، وLinux، كما هو موضح في صفحة المنتج الرسمية [MySQL Workbench](https://www.mysql.com/products/workbench/). توفر هذه المتاحة عبر المنصات إمكانية الوصول، ويطور وتستخدمن مع MySQL Server 8.0، مع إمكانية وجود مشاكل التوافق مع الإصدارات 8.4 واكثر، وفقًا للمدونة [MySQL Workbench Manual](https://dev.mysql.com/doc/workbench/en/). يدمج الأداة نمذجة البيانات، تطوير SQL، وإدارة، مما يجعلها حلًا شاملًا لإدارة قواعد البيانات.

#### عملية التثبيت
تختلف عملية التثبيت حسب نظام التشغيل، ولكن تم العثور على خطوات مفصلة لWindows في دليل [Ultimate MySQL Workbench Installation Guide](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench-installation). بالنسبة لWindows، يزور المستخدمون [MySQL Downloads](https://www.mysql.com/downloads/) لاختيار المثبّت، ويختارون إعدادًا مخصصًا، ويثبِتون MySQL Server، Workbench، وshell. تتضمن العملية منح الإذن، إعداد الشبكة، وإعداد كلمة مرور الجذر، مع أن الإعدادات الافتراضية تكون كافية عادةً. بالنسبة للنظم الأخرى، تكون العملية مشابهة، ويوصى المستخدمون بالاتباع التعليمات الخاصة بالنظام، مع التأكيد على عدم الحاجة إلى Java، خلافًا للتفكير الأولي، حيث يستخدم MySQL Workbench إطار Qt.

يقدم الجدول التالي ملخصًا للخطوات التثبيت لWindows من أجل الوضوح:

| رقم الخطوة | الإجراء                                                                                     | التفاصيل                                                                 |
|-------------|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| 0           | افتح موقع MySQL                                                                         | زور [MySQL Downloads](https://www.mysql.com/downloads/)               |
| 1           | اختر خيار التحميل                                                                    | -                                                                       |
| 2           | اختر مثبّت MySQL لWindows                                                         | -                                                                       |
| 3           | اختر المثبّت المرغوب فيه وانقر على تحميل                                                | -                                                                       |
| 4           | افتح المثبّت الذي تم تحميله                                                                  | -                                                                       |
| 5           | اعطِ الإذن واختر نوع الإعداد                                                     | انقر على نعم، ثم اختر مخصص                                           |
| 6           | انقر على التالي                                                                                | -                                                                       |
| 7           | تثبيت MySQL server، Workbench، وshell                                                 | اختر المكونات واسحبها في المثبّت                             |
| 8           | انقر على التالي، ثم تنفيذ                                                                   | تحميل وإثبات المكونات                                         |
| 9           | اعد إعداد المنتج، استخدم الإعدادات الافتراضية للنوع والشبكة                                | انقر على التالي                                                             |
| 10          | اعد إعداد كلمة المرور إلى تشفير كلمة مرور قوية، اعد كلمة مرور MySQL Root                  | انقر على التالي                                                             |
| 11          | استخدم الإعدادات الافتراضية لخدمة Windows، تطبيق الإعدادات                                  | انقر على تنفيذ، ثم انقر على إتمام بعد الإعداد                          |
| 12          | اكمل التثبيت، افتح MySQL Workbench وShell                                    | اختر المثال المحلي، أدخل كلمة المرور لاستخدام                            |

بعد التثبيت، يمكن للمستخدمين التحقق من ذلك عن طريق تنفيذ أوامر SQL أساسية مثل `Show Databases;`, كما هو موضح في الدليل.

#### إعداد الاتصال
إعداد الاتصال إلى خادم MySQL هو خطوة حاسمة، وتم العثور على توجيهات مفصلة في مصادر متعددة، بما في ذلك [SiteGround Tutorials](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/) و[w3resource MySQL Workbench Tutorial](https://www.w3resource.com/mysql/administration-tools/mysql-workbench-tutorial.php). يفتح المستخدمون MySQL Workbench، ينقرون على زر '+' بجوار "MySQL Connections," ويدخلون تفاصيل مثل اسم الاتصال، الطريقة (عادة TCP/IP القياسي)، اسم المضيف، الميناء (الافتراضي 3306)، اسم المستخدم، كلمة المرور، واختياريًا، المخطط الافتراضي. يُوصى باختبار الاتصال، ويقدم عرض شاشات في دليل w3resource توجيهًا بصريًا من "MySQL Workbench New Connection Step 1" إلى "Step 4," مما يؤكد العملية.

لإتصالات بعيدة، تشمل المعايير الإضافية التأكد من أن عنوان IP مسموح به في حائط الحماية للخادم، كما هو موضح في [Connect MySQL Workbench](https://www.inmotionhosting.com/support/website/connect-database-remotely-mysql-workbench/). هذا هو حاسم للمستخدمين الذين يربطون إلىInstances MySQL السحابية، مثل Azure Database for MySQL، كما هو موضح في [Quickstart: Connect MySQL Workbench](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench).

#### تنفيذ عمليات قاعدة البيانات
بعد الاتصال، يمكن للمستخدمين تنفيذ عمليات مختلفة، مع توفر طرق رسومية وSQL. يمكن إنشاء قاعدة بيانات عن طريق محرر SQL مع `CREATE DATABASE database_name;`, أو رسوميًا عن طريق النقر بالزر الأيمن على "Schemas" واختيار "Create Schema...," كما هو موضح في الدروس. على نفس النحو، يمكن إنشاء الجداول عن طريق كتابة بيان CREATE TABLE أو استخدام الواجهة الرسومية، مع خيارات لتحرير بيانات الجدول وإدارة المخططات، كما هو موضح في [A Complete Guide on MySQL Workbench](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench).

تنفيذ الاستعلامات يتم من خلال محرر SQL، الذي يوفر تبييض النص، إكمال تلقائي، وسجل الاستعلامات، مما يزيد من سهولة الاستخدام. تم توضيح هذه الميزات في [MySQL Workbench](https://www.mysql.com/products/workbench/)، مما يجعله سهل الاستخدام للمبتدئين والمستخدمين المتقدمين.

#### الميزات المتقدمة والأدوات
يوسع MySQL Workbench عن الأساسيات مع ميزات متقدمة مثل نمذجة البيانات باستخدام مخططات ER، الهندسة العكسيّة، وإدارة التغييرات، كما هو موضح في [MySQL Workbench Manual](https://dev.mysql.com/doc/workbench/en/). تسمح علامة التبويب "Model" بتصميم بصري، وإنتاج مخططات SQL، وهو مفيد بشكل خاص للمهندسين المعماريين للبيانات. تشمل أدوات إدارة الخادم إدارة المستخدمين، الصلاحيات، والإعدادات، مع واجهة مستخدم بصريّة لتحسين الرؤية، كما هو موضح في [MySQL Workbench](https://www.mysql.com/products/workbench/).

تشمل الميزات الأخرى هجرة قاعدة البيانات، تحسين الأداء، وقدرات النسخ الاحتياطي/استعادة، مع أدوات مثل Data Export لنسخ احتياطي قواعد البيانات، كما هو موضح في [SiteGround Tutorials](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/). يمكن أن تكون هذه الميزات المتقدمة غير متوقعة للمستخدمين الجدد في إدارة قواعد البيانات، وتوفر مجموعة قوية لإدارة قاعدة البيانات الشاملة.

#### النصائح والأفضليات
يجب على المستخدمين التأكد من تشغيل خادم MySQL وصدق تفاصيل الاتصال، مع فحص إعدادات حائط الحماية للاتصالات البعيدة. يُوصى باستخدام كلمات مرور قوية وأسلوب آمن، خاصة للبيانات الحساسة. حفظ مخططات SQL واستكشاف التحكم في الإصدار يمكن تحسين سير العمل، على الرغم من عدم توضيح ذلك في الإجابة المباشرة، فهو جزء من أفضليات المجتمع.

#### الخاتمة
يقدم هذا ملخص الاستطلاع دليلًا شاملًا لاستخدام MySQL Workbench، يغطي التثبيت، إعداد الاتصال، العمليات الأساسية والمتقدمة، والنصائح. يستفيد من مصادر موثوقة متعددة، مما يضمن الدقة اعتبارًا من 28 فبراير 2025، ويصمم للمستخدمين الذين يبحثون عن توجيهات فنية مفصلة.

#### الإشارات الرئيسية
- [MySQL Workbench Manual](https://dev.mysql.com/doc/workbench/en/)
- [MySQL Workbench product page](https://www.mysql.com/products/workbench/)
- [Ultimate MySQL Workbench Installation Guide](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench-installation)
- [SiteGround Tutorials MySQL Workbench](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/)
- [w3resource MySQL Workbench Tutorial](https://www.w3resource.com/mysql/administration-tools/mysql-workbench-tutorial.php)
- [Connect MySQL Workbench remotely](https://www.inmotionhosting.com/support/website/connect-database-remotely-mysql-workbench/)
- [Quickstart Connect MySQL Workbench Azure](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench)
- [A Complete Guide on MySQL Workbench](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench)