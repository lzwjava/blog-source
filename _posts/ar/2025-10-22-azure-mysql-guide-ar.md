---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل خادم Azure قاعدة بيانات MySQL المرن
translated: true
type: note
---

Azure Database for MySQL هي خدمة قاعدة بيانات علائقية مُدارة بالكامل وتعمل بواسطة إصدار مجتمع MySQL. فهي تتولى المهام الروتينية مثل النسخ الاحتياطي والترقيات والمراقبة، مما يسمح لك بالتركيز على تطبيقك. خيار النشر الموصى به هو **الخادم المرن** **Flexible Server**، والذي يقدم خيارات تكوين أكثر وأداءً أفضل من الخادم الفردي القديم (الذي يتم إيقافه).

يغطي هذا الدليل إنشاء خادم، والاتصال به، وتنفيذ العمليات الأساسية. وهو يعتمد على بوابة Azure من أجل البساطة.

## المتطلبات الأساسية
-   اشتراك Azure نشط (يمكنك إنشاء واحد على [azure.microsoft.com](https://azure.microsoft.com/free/) إذا لزم الأمر).
-   الوصول إلى بوابة Azure (portal.azure.com).
-   الإلمام الأساسي بمفاهيم MySQL.
-   وصول شبكة صادر عبر المنفذ 3306 (الافتراضي لـ MySQL).
-   تثبيت MySQL Workbench للاتصال (يمكنك التنزيل من [mysql.com](https://dev.mysql.com/downloads/workbench/)).

## الخطوة 1: إنشاء خادم مرن في بوابة Azure
اتبع هذه الخطوات لتوفير الخادم الخاص بك.

1.  سجّل الدخول إلى [بوابة Azure](https://portal.azure.com).
2.  ابحث عن "Azure Database for MySQL Flexible Servers" في شريط البحث العلوي وحدده.
3.  انقر فوق **إنشاء** **Create** لبدء المعالج.
4.  في علامة التبويب **الأساسيات** **Basics**، قم بالتكوين:
    -   **الاشتراك** **Subscription**: حدد اشتراكك.
    -   **مجموعة الموارد** **Resource group**: أنشئ مجموعة جديدة (مثل `myresourcegroup`) أو اختر مجموعة موجودة.
    -   **اسم الخادم** **Server name**: اسم فريد (مثل `mydemoserver`)، من 3 إلى 63 حرفًا، أحرف صغيرة/أرقام/شرطات. اسم المضيف الكامل سيكون `<name>.mysql.database.azure.com`.
    -   **المنطقة** **Region**: اختر الأقرب إلى مستخدميك.
    -   **إصدار MySQL** **MySQL version**: 8.0 (أحدث إصدار رئيسي).
    -   **نوع عبء العمل** **Workload type**: تطوير Development (للالاختبار؛ استخدم Small/Medium للإنتاج).
    -   **الحوسبة + التخزين** **Compute + storage**: فئة قابلة للانفجار Burstable، Standard_B1ms (1 نواة افتراضية vCore)، تخزين 10 جيبيبايت، 100 عملية إدخال/إخراج في الثانية IOPS، نسخ احتياطي لمدة 7 أيام. اضبط حسب الاحتياجات (مثل زيادة IOPS للهجرة).
    -   **منطقة التوفر** **Availability zone**: لا تفضيل No preference (أو طابق منطقة التطبيق الخاص بك).
    -   **التوافر العالي** **High availability**: معطل للمبتدئين Disabled for starters (مكّن مقاوم منطقة zone-redundant للإنتاج).
    -   **المصادقة** **Authentication**: MySQL و Microsoft Entra (للمرونة).
    -   **اسم مستخدم المسؤول** **Admin username**: مثل `mydemouser` (ليس root/admin/etc، بحد أقصى 32 حرفًا).
    -   **كلمة المرور** **Password**: كلمة مرور قوية (8-128 حرفًا، مزيج من أحرف كبيرة/صغيرة/أرقام/رموز).
5.  انتقل إلى علامة التبويب **الشبكات** **Networking**:
    -   **طريقة الاتصال** **Connectivity method**: وصول عام Public access (للبساطة؛ استخدم VNet خاص لأمان الإنتاج).
    -   **قواعد جدار الحماية** **Firewall rules**: أضف عنوان IP العميل الحالي (أو اسمح لخدمات Azure). لا يمكنك تغيير هذا لاحقًا.
6.  راجع الإعدادات في **المراجعة + الإنشاء** **Review + create**، ثم انقر فوق **إنشاء** **Create**. يستغرق النشر من 5 إلى 10 دقائق. راقب عبر الإشعارات.
7.  بمجرد الانتهاء، ثبّت على لوحة المعلومات وانتقل إلى صفحة **نظرة عامة** **Overview** للمورد. قواعد البيانات الافتراضية تشمل `information_schema`، `mysql`، إلخ.

## الخطوة 2: الاتصال بالخادم الخاص بك
استخدم MySQL Workbench للاتصال بواجهة المستخدم الرسومية. (بدائل: Azure Data Studio، أو سطر أوامر mysql، أو Azure Cloud Shell.)

1.  في البوابة، انتقل إلى **نظرة عامة** **Overview** للخادم الخاص بك ولاحظ:
    -   اسم الخادم (مثل `mydemoserver.mysql.database.azure.com`).
    -   اسم مستخدم المسؤول.
    -   إعادة تعيين كلمة المرور إذا لزم الأمر.
2.  افتح MySQL Workbench.
3.  انقر فوق **اتصال جديد** **New Connection** (أو حرر اتصالاً موجودًا).
4.  في علامة التبويب **المعلمات** **Parameters**:
    -   **اسم الاتصال** **Connection Name**: مثل `Demo Connection`.
    -   **طريقة الاتصال** **Connection Method**: قياسي Standard (TCP/IP).
    -   **اسم المضيف** **Hostname**: اسم الخادم الكامل.
    -   **المنفذ** **Port**: 3306.
    -   **اسم المستخدم** **Username**: اسم مستخدم المسؤول.
    -   **كلمة المرور** **Password**: أدخل وقم بتخزينها في الخزنة.
5.  انقر فوق **اختبار الاتصال** **Test Connection**. إذا فشل:
    -   تحقق من التفاصيل من البوابة.
    -   تأكد من أن جدار الحماية يسمح بعنوان IP الخاص بك.
    -   يتم فرض TLS/SSL (TLS 1.2)؛ قم بتنزيل شهادة CA من [DigiCert](https://dl.cacerts.digicert.com/DigiCertGlobalRootCA.crt.pem) وربطها في Workbench إذا لزم الأمر (ضمن علامة التبويب SSL: Use SSL > Require وحدد ملف CA).
6.  انقر فوق **موافق** **OK** للحفظ. انقر نقرًا مزدوجًا فوق مربع الاتصال لفتح محرر الاستعلامات.

## الخطوة 3: إنشاء قواعد البيانات وإدارتها
بمجرد الاتصال، قم بإدارة قواعد البيانات عبر البوابة أو العميل.

### عبر بوابة Azure:
1.  في صفحة الخادم الخاص بك، حدد **قواعد البيانات** **Databases** من القائمة اليسرى.
2.  انقر فوق **+ إضافة** **+ Add**:
    -   **اسم قاعدة البيانات** **Database name**: مثل `testdb`.
    -   **ترميز الحروف** **Charset**: utf8 (افتراضي).
    -   **المقارنة** **Collation**: utf8_general_ci.
3.  انقر فوق **حفظ** **Save**.

للحذف: حدد قاعدة البيانات (قواعد البيانات)، انقر فوق **حذف** **Delete**.

### عبر MySQL Workbench (استعلامات SQL):
شغّل هذه في محرر الاستعلامات:

-   إنشاء قاعدة بيانات: `CREATE DATABASE testdb CHARACTER SET utf8 COLLATE utf8_general_ci;`
-   عرض قواعد البيانات: `SHOW DATABASES;`
-   استخدام قاعدة بيانات: `USE testdb;`
-   إنشاء جدول: `CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));`
-   إدراج بيانات: `INSERT INTO users (name) VALUES ('Alice');`
-   استعلام: `SELECT * FROM users;`

أكد التغييرات باستخدام `COMMIT;` إذا لم تكن المؤازنة التلقائية مفعلة.

## نصائح الاستخدام الأساسية
-   **التحجيم** **Scaling**: من **نظرة عامة** **Overview** > **الحوسبة + التخزين** **Compute + storage**، اضبط النوى الافتراضية vCores/التخزين/عمليات الإدخال والإخراج في الثانية IOPS (لا يوجد توقف للخدمة لمعظم التغييرات).
-   **النسخ الاحتياطي** **Backups**: يومي تلقائي؛ استعادة إلى نقطة زمنية محددة حتى 35 يومًا (قم بتكوينها في إعدادات **النسخ الاحتياطي** **Backup**).
-   **المراقبة** **Monitoring**: استخدم **مقاييس** **Metrics** لرؤى وحدة المعالجة المركزية/التخزين؛ عيّن تنبيهات.
-   **الأمان** **Security**: استخدم دائمًا SSL (مفروض). للإنتاج، مكّن التوافر العالي HA، والشبكة الخاصة، ومصادقة Entra ID.
-   **الهجرة** **Migration**: استخدم mysqldump لقواعد البيانات الصغيرة؛ DMS للقواعد الكبيرة.
-   **التكاليف** **Costs**: ادفع مقابل الحوسبة/التخزين؛ ابدأ صغيرًا وقم بالتحجيم. استخدم الحاسبة على [azure.microsoft.com](https://azure.microsoft.com/pricing/calculator/).
-   **التنظيف** **Cleanup**: احذف مجموعة الموارد لإزالة الخادم وتجنب الرسوم.

للحصول على ميزات متقدمة مثل نسخ القراءة أو معلمات الخادم، استكشف القائمة اليسرى للبوابة.

## المراجع
-   [بدء سريع: إنشاء خادم مرن باستخدام بوابة Azure](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/quickstart-create-server-portal)
-   [الاتصال باستخدام MySQL Workbench](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench)
-   [إنشاء قواعد البيانات وإدارتها](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/how-to-create-manage-databases)
-   [توثيق Azure Database for MySQL](https://learn.microsoft.com/en-us/azure/mysql/)