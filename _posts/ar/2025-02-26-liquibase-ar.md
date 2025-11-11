---
audio: false
generated: true
lang: ar
layout: post
title: 'ليكويبيز: إدارة مخطط قاعدة البيانات'
translated: true
type: note
---

إليك دليل شامل حول **كيفية استخدام Liquibase** في تطبيق Spring Boot لإدارة تغييرات مخطط قاعدة البيانات بشكل فعال:

---

### 1. إضافة تبعية Liquibase
للبدء، تحتاج إلى تضمين تبعية Liquibase في مشروعك. إذا كنت تستخدم **Maven**، أضف هذا إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
```

أما إذا كنت تستخدم **Gradle**، فأضف هذا إلى ملف `build.gradle` الخاص بك:

```groovy
implementation 'org.liquibase:liquibase-core'
```

هذا يقوم بإضافة مكتبة Liquibase الأساسية إلى مشروعك.

---

### 2. تكوين Liquibase
يستخدم Liquibase **ملف سجل التغييرات** لإدارة تغييرات مخطط قاعدة البيانات. افتراضيًا، يبحث Spring Boot عن ملف باسم `db/changelog/db.changelog-master.yaml`، أو `db/changelog/db.changelog-master.xml`، أو `db/changelog/db.changelog-master.sql` في مسار الفئات. يمكنك تخصيص هذا الموقع عن طريق إضافة خاصية إلى ملف `application.properties` (أو `application.yml`):

```properties
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

هذا يخبر Spring Boot عن مكان العثور على ملف سجل التغييرات الخاص بك.

---

### 3. إنشاء ملف سجل التغييرات
يحدد ملف سجل التغييرات التعديلات التي تريد تطبيقها على قاعدة البيانات الخاصة بك. يمكنك كتابته بصيغ مثل XML، أو YAML، أو SQL. إليك مثال على ملف **سجل التغييرات بصيغة XML** موجود في المسار `src/main/resources/db/changelog/db.changelog-master.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.8.xsd">

    <changeSet id="1" author="your-name">
        <createTable tableName="users">
            <column name="id" type="int">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="username" type="varchar(255)"/>
            <column name="email" type="varchar(255)"/>
        </createTable>
    </changeSet>

</databaseChangeLog>
```

يقوم هذا المثال بإنشاء جدول `users` بثلاثة أعمدة: `id`، و`username`، و`email`. يمثل كل `<changeSet>` مجموعة من التغييرات لتطبيقها.

---

### 4. تشغيل تطبيق Spring Boot الخاص بك
عند بدء تشغيل تطبيق Spring Boot الخاص بك، يقوم Liquibase تلقائيًا بما يلي:
- قراءة ملف سجل التغييرات.
- التحقق من مجموعات التغييرات التي تم تطبيقها مسبقًا (يتم تتبعها في جدول يسمى `DATABASECHANGELOG`).
- تنفيذ أي مجموعات تغييرات جديدة على قاعدة البيانات الخاصة بك.

لا حاجة لأي كود إضافي—فالتكوين التلقائي لـ Spring Boot يتولى ذلك نيابة عنك.

---

### 5. تخصيص Liquibase (اختياري)
يمكنك ضبط سلوك Liquibase باستخدام الخصائص في ملف `application.properties`. فيما يلي بعض الخيارات الشائعة:

```properties
spring.liquibase.enabled=true          # تمكين أو تعطيل Liquibase
spring.liquibase.drop-first=false      # إسقاط قاعدة البيانات قبل تطبيق التغييرات (استخدم بحذر)
spring.liquibase.contexts=dev,prod     # تشغيل مجموعات التغييرات فقط في سياقات محددة
```

تسمح لك هذه الإعدادات بتكييف Liquibase مع بيئتك أو سير العمل الخاص بك.

---

### 6. الاستفادة من الميزات المتقدمة
يقدم Liquibase ميزات قوية لتعزيز إدارة المخطط:
- **السياقات والوسوم**: التحكم في مجموعات التغييرات التي تعمل في بيئات محددة (مثل `dev` مقابل `prod`).
- **الشروط المسبقة**: التأكد من استيفاء شروط معينة (مثل وجود جدول) قبل تطبيق مجموعة التغييرات.
- **التراجعات**: تحديد كيفية التراجع عن مجموعة التغييرات إذا لزم الأمر.
- **إعادة الهيكلة**: استخدام الدعم المدمج لتغييرات قاعدة البيانات المعقدة (مثل إعادة تسمية الأعمدة).

على سبيل المثال، إضافة سياق إلى مجموعة التغييرات:

```xml
<changeSet id="2" author="your-name" context="dev">
    <addColumn tableName="users">
        <column name="created_at" type="timestamp"/>
    </addColumn>
</changeSet>
```

تعمل مجموعة التغييرات هذه فقط في سياق `dev`.

---

### 7. الاختبار باستخدام قاعدة بيانات في الذاكرة
لأغراض الاختبار، قم بإقران Liquibase مع قاعدة بيانات في الذاكرة مثل H2. أضف تبعية H2:

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

ثم قم بتكوين ملف `application.properties` الخاص بك للاختبار:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

سيقوم Liquibase بتطبيق التغييرات الخاصة بك على قاعدة البيانات في الذاكرة أثناء الاختبارات.

---

### 8. التحكم في الإصدارات لملف سجل التغييرات الخاص بك
قم بتخزين ملفات سجل التغييرات الخاصة بك في نظام التحكم في الإصدارات (مثل Git) جنبًا إلى جنب مع كود التطبيق الخاص بك. يضمن هذا تطور مخطط قاعدة البيانات الخاصة بك بشكل متزامن مع قاعدة الكود، مما يجعم عمليات النشر والتراجع أكثر قابلية للتنبؤ.

---

### الملخص
لاستخدام Liquibase في تطبيق Spring Boot:
1. أضف تبعية Liquibase.
2. قم بتكوين موقع ملف سجل التغييرات.
3. أنشئ ملف سجل التغييرات بتغييرات قاعدة البيانات الخاصة بك.
4. شغل تطبيقك—يتولى Liquibase الباقي.

يعد Liquibase أداة قوية لإدارة تغييرات مخطط قاعدة البيانات بطريقة منظمة وخاضعة للتحكم في الإصدارات، ومتكاملة بسلاس مع Spring Boot.