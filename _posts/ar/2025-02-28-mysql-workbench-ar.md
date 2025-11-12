---
audio: false
generated: true
lang: ar
layout: post
title: استخدام ماي إس كيو إل وورك بينش
translated: true
type: note
---

### النقاط الرئيسية
- من المرجح أن MySQL Workbench أداة مجانية ومفتوحة المصدر لإدارة قواعد بيانات MySQL، متاحة على أنظمة Windows وmacOS وLinux.
- يبدو أنه يمكنك تنزيله من الموقع الرسمي، وتثبيته، وإعداد اتصال باستخدام تفاصيل الخادم مثل اسم المضيف واسم المستخدم.
- تشير الأبحاث إلى أنه يمكنك إنشاء قواعد البيانات والجداول وتنفيذ الاستعلامات باستخدام الطرق الرسومية و SQL.
- تميل الأدلة إلى أنه يقدم ميزات متقدمة مثل نمذجة البيانات وإدارة الخادم، والتي قد تكون غير متوقعة للمبتدئين.

### ما هو MySQL Workbench؟
MySQL Workbench هي أداة تساعدك في تصميم وتطوير وإدارة قواعد بيانات MySQL. إنها مجانية ومفتوحة المصدر وتعمل على أنظمة Windows وmacOS وLinux، مما يجعلها في متناول العديد من المستخدمين. توفر واجهة رسومية، مما يعني أنك لست مضطرًا دائمًا لكتابة التعليمات البرمجية لإدارة قواعد البيانات، على الرغم من أنه يمكنك ذلك إذا فضلت.

### البدء
للبدء، قم بزيارة صفحة التنزيل الرسمية على [https://www.mysql.com/products/workbench/](https://www.mysql.com/products/workbench/) واحصل على الإصدار المناسب لنظام التشغيل الخاص بك. اتبع خطوات التثبيت المقدمة، وهي مباشرة ومتشابهة عبر المنصات.

### الإعداد والاستخدام
بعد التثبيت، افتح MySQL Workbench وأنشئ اتصالاً جديدًا بالنقر على زر '+' بجوار "MySQL Connections". ستحتاج إلى تفاصيل مثل اسم مضيف الخادم، والمنفذ (عادة 3306)، واسم المستخدم، وكلمة المرور. اختبر الاتصال للتأكد من أنه يعمل.

بعد الاتصال، يمكنك:
- **إنشاء قاعدة بيانات:** استخدم محرر SQL لتشغيل `CREATE DATABASE database_name;` أو انقر بزر الماوس الأيمن على "Schemas" واختر "Create Schema..."
- **إنشاء جدول:** اكتب عبارة CREATE TABLE في محرر SQL أو استخدم الخيار الرسومي بالنقر بزر الماوس الأيمن على قاعدة البيانات.
- **تشغيل الاستعلامات:** اكتب استعلام SQL الخاص بك في محرر SQL ونفذه لرؤية النتائج.

### الميزات المتقدمة
بعد الأساسيات، تقدم MySQL Workbench ميزات غير متوقعة مثل نمذجة البيانات، حيث يمكنك تصميم قاعدة البيانات الخاصة بك بصريًا باستخدام مخططات ER، وأدوات لإدارة الخادم، مثل إدارة المستخدمين والتكوينات. يمكن استكشاف هذه الميزات من خلال علامة التبويب "Model" والقوائم الأخرى.

---

### ملاحظة المسح: دليل شامل لاستخدام MySQL Workbench

يقدم هذا القسم استكشافًا مفصلاً لاستخدام MySQL Workbench، مع توسيع نطاق الإجابة المباشرة لتشمل سياقًا إضافيًا وتفاصيلًا تقنية. يهدف إلى تغطية جميع الجوانب التي تمت مناقشتها في البحث، مما يضمن فهمًا شاملاً للمستخدمين بمستويات مختلفة من الخبرة.

#### مقدمة إلى MySQL Workbench
يوصف MySQL Workbench كأداة بصرية موحدة لمهندسي قواعد البيانات والمطورين ومسؤولي قواعد البيانات (DBAs). إنه مجاني ومفتوح المصدر، ومتاح لأنظمة التشغيل الرئيسية بما في ذلك Windows وmacOS وLinux، كما هو مذكور في صفحة المنتج الرسمية [MySQL Workbench](https://www.mysql.com/products/workbench/). يضمن هذا التوافر عبر المنصات إمكانية الوصول إليه، ويتم تطويره واختباره مع MySQL Server 8.0، مع الإشارة إلى وجود مشاكل توافق محتملة للإصدارات 8.4 وما فوق، وفقًا للدليل [MySQL Workbench Manual](https://dev.mysql.com/doc/workbench/en/). تدمج الأداة نمذجة البيانات وتطوير SQL والإدارة، مما يجعلها حلاً شاملاً لإدارة قواعد البيانات.

#### عملية التثبيت
تختلف عملية التثبيت حسب نظام التشغيل، ولكن تم العثور على خطوات مفصلة لنظام Windows في برنامج تعليمي [Ultimate MySQL Workbench Installation Guide](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench-installation). بالنسبة لنظام Windows، يزور المستخدمون [MySQL Downloads](https://www.mysql.com/downloads/) لتحديد برنامج التثبيت، واختيار إعداد مخصص، وتثبيت MySQL Server وWorkbench وShell. تتضمن العملية منح الأذونات، وإعداد الشبكات، وتكوين كلمة مرور root، حيث تكون الإعدادات الافتراضية كافية في كثير من الأحيان. بالنسبة لأنظمة التشغيل الأخرى، تكون العملية مماثلة، وينصح المستخدمون باتباع التعليمات الخاصة بكل منصة، مع التأكد من أن Java غير مطلوبة، على عكس التكهنات الأولية، حيث يستخدم MySQL Workbench إطار عمل Qt.

يتم تقديم جدول يلخص خطوات التثبيت لنظام Windows أدناه من أجل الوضوح:

| رقم الخطوة | الإجراء                                                                                     | التفاصيل                                                                 |
|----------|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| 0        | افتح موقع MySQL                                                                         | قم بزيارة [MySQL Downloads](https://www.mysql.com/downloads/)               |
| 1        | حدد خيار Downloads                                                                    | -                                                                       |
| 2        | حدد MySQL Installer for Windows                                                         | -                                                                       |
| 3        | اختر برنامج التثبيت المطلوب وانقر على download                                                | -                                                                       |
| 4        | افتح برنامج التثبيت الذي تم تنزيله                                                                  | -                                                                       |
| 5        | منح الإذن واختيار نوع الإعداد                                                     | انقر فوق Yes، ثم اختر Custom                                           |
| 6        | انقر فوق Next                                                                                | -                                                                       |
| 7        | قم بتثبيت MySQL server وWorkbench وShell                                                 | حدد المكونات وانقلها في برنامج التثبيت                             |
| 8        | انقر فوق Next، ثم Execute                                                                   | قم بتنزيل المكونات وتثبيتها                                         |
| 9        | قم بتكوين المنتج، استخدم إعدادات Type وNetworking الافتراضية                                | انقر فوق Next                                                             |
| 10       | عيّن المصادقة على strong password encryption، عيّن MySQL Root password                  | انقر فوق Next                                                             |
| 11       | استخدم إعدادات Windows service الافتراضية، طبق التكوين                                  | انقر فوق Execute، ثم Finish بعد اكتمال التكوين                          |
| 12       | أكمل التثبيت، شغّل MySQL Workbench وShell                                    | اختر Local instance، أدخل كلمة المرور للاستخدام                            |

بعد التثبيت، يمكن للمستخدمين التحقق من خلال تشغيل أوامر SQL أساسية مثل `Show Databases;`، كما هو مقترح في البرنامج التعليمي، مما يضمن الوظيفة.

#### إعداد الاتصال
يعد الاتصال بخادم MySQL خطوة حاسمة، وتم العثور على إرشادات مفصلة في مصادر متعددة، بما في ذلك [SiteGround Tutorials](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/) و [w3resource MySQL Workbench Tutorial](https://www.w3resource.com/mysql/administration-tools/mysql-workbench-tutorial.php). يفتح المستخدمون MySQL Workbench، وينقرون على زر '+' بجوار "MySQL Connections"، ويدخلون التفاصيل مثل اسم الاتصال، والطريقة (عادة Standard TCP/IP)، واسم المضيف، والمنفذ (الافتراضي 3306)، واسم المستخدم، وكلمة المرور، واختياريًا، المخطط الافتراضي. يوصى باختبار الاتصال، ويقوم عرض شرائح في برنامج w3resource التعليمي بتوجيه المستخدم بصريًا خلال "MySQL Workbench New Connection Step 1" إلى "Step 4"، مؤكدًا العملية.

للوصول عن بُعد، تشمل الاعتبارات الإضافية التأكد من أن عنوان IP مسموح به في جدار حماية الخادم، كما هو مذكور في [Connect MySQL Workbench](https://www.inmotionhosting.com/support/website/connect-database-remotely-mysql-workbench/). هذا أمر بالغ الأهمية للمستخدمين الذين يتصلون بنسخ MySQL المستندة إلى السحابة، مثل Azure Database for MySQL، الموضحة في [Quickstart: Connect MySQL Workbench](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench).

#### تنفيذ عمليات قاعدة البيانات
بعد الاتصال، يمكن للمستخدمين تنفيذ عمليات متنوعة، مع توفر كل من الطرق الرسومية والقائمة على SQL. يمكن إنشاء قاعدة بيانات عبر محرر SQL باستخدام `CREATE DATABASE database_name;`، أو رسوميًا بالنقر بزر الماوس الأيمن على "Schemas" واختيار "Create Schema..."، كما هو موضح في البرامج التعليمية. وبالمثل، يتضمن إنشاء الجداول كتابة عبارات CREATE TABLE أو استخدام الواجهة الرسومية، مع خيارات لتحرير بيانات الجدول وإدارة المخططات، كما هو موضح في [A Complete Guide on MySQL Workbench](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench).

تسهل محرر SQL تشغيل الاستعلامات، حيث تقدم تمييزًا للنحو، والإكمال التلقائي، وتاريخ الاستعلام، مما يعزز قابلية الاستخدام. تم تسليط الضوء على هذه الميزات في [MySQL Workbench](https://www.mysql.com/products/workbench/)، مما يجعلها سهلة الاستخدام لكل من المبتدئين والمستخدمين المتقدمين.

#### الميزات والأدوات المتقدمة
يمتد MySQL Workbench إلى ما هو أبعد من الأساسيات بميزات متقدمة، مثل نمذجة البيانات باستخدام مخططات الكيانات والعلاقات (ER)، والهندسة الأمامية والعكسية، وإدارة التغيير، كما هو مذكور في [MySQL Workbench Manual](https://dev.mysql.com/doc/workbench/en/). تسمح علامة التبويب "Model" بالتصميم المرئي، وتوليد نصوص SQL، وهو أمر مفيد بشكل خاص لمهندسي قواعد البيانات. تتضمن أدوات إدارة الخادم إدارة المستخدمين والامتيازات والتكوينات، مع وجود وحدات تحكم مرئية لتحسين الرؤية، كما هو موضح في [MySQL Workbench](https://www.mysql.com/products/workbench/).

تشمل الميزات الأخرى ترحيل قواعد البيانات، وتحسين الأداء، وإمكانيات النسخ الاحتياطي والاستعادة، مع أدوات مثل Data Export لنسخ قواعد البيانات احتياطيًا، الموضحة في [SiteGround Tutorials](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/). قد تكون هذه الوظائف المتقدمة غير متوقعة للمستخدمين الجدد في إدارة قواعد البيانات، حيث تقدم مجموعة قوية للإدارة الشاملة لقواعد البيانات.

#### النصائح وأفضل الممارسات
يجب على المستخدمين التأكد من أن خادم MySQL قيد التشغيل وأن تفاصيل الاتصال صحيحة، مع التحقق من إعدادات جدار الحماية للاتصالات البعيدة. يوصى باستخدام كلمات مرور قوية وطرق آمنة، خاصة للبيانات الحساسة. يمكن أن يؤدي حفظ نصوص SQL واستكشاف التحكم في الإصدار إلى تحسين سير العمل، على الرغم من عدم تفصيله في الإجابة المباشرة، إلا أنه جزء من أفضل الممارسات من خلال الرؤى المجتمعية.

#### الخلاصة
توفر ملاحظة المسح هذه دليلاً شاملاً لاستخدام MySQL Workbench، covering التثبيت، وإعداد الاتصال، والعمليات الأساسية والمتقدمة، والنصائح. تعتمد على مصادر موثوقة متعددة، مما يضمن الدقة اعتبارًا من 28 فبراير 2025، وهي مصممة للمستخدمين الذين يبحثون عن إرشادات تقنية مفصلة.

#### الاقتباسات الرئيسية
- [MySQL Workbench Manual about 10 words](https://dev.mysql.com/doc/workbench/en/)
- [MySQL Workbench product page about 10 words](https://www.mysql.com/products/workbench/)
- [Ultimate MySQL Workbench Installation Guide about 10 words](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench-installation)
- [SiteGround Tutorials MySQL Workbench about 10 words](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/)
- [w3resource MySQL Workbench Tutorial about 10 words](https://www.w3resource.com/mysql/administration-tools/mysql-workbench-tutorial.php)
- [Connect MySQL Workbench remotely about 10 words](https://www.inmotionhosting.com/support/website/connect-database-remotely-mysql-workbench/)
- [Quickstart Connect MySQL Workbench Azure about 10 words](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench)
- [A Complete Guide on MySQL Workbench about 10 words](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench)