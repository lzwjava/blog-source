---
audio: false
generated: true
lang: ar
layout: post
title: 'Liquibase: إدارة مخطط قاعدة البيانات'
translated: true
---

هنا دليل شامل حول كيفية استخدام **Liquibase** في تطبيق Spring Boot لإدارة تغييرات مخطط قاعدة البيانات بشكل فعال:

---

### 1. إضافة اعتماد Liquibase
لبدء العمل، عليك إضافة اعتماد Liquibase في مشروعك. إذا كنت تستخدم **Maven**، أضف هذا إلى ملف `pom.xml`:

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
```

للمستخدمين **Gradle**، أضف هذا إلى ملف `build.gradle`:

```groovy
implementation 'org.liquibase:liquibase-core'
```

هذا يجلب مكتبة Liquibase الأساسية إلى مشروعك.

---

### 2. تهيئة Liquibase
يستخدم Liquibase ملف **changelog** لإدارة تغييرات مخطط قاعدة البيانات. بافتراضية، يبحث Spring Boot عن ملف باسم `db/changelog/db.changelog-master.yaml`، `db/changelog/db.changelog-master.xml`، أو `db/changelog/db.changelog-master.sql` في المسار. يمكنك تخصيص هذا الموقع بإضافة خاصية إلى ملف `application.properties` (أو `application.yml`):

```properties
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

هذا يوضح Spring Boot مكان ملف changelog.

---

### 3. إنشاء ملف changelog
يحدد ملف changelog التغييرات التي تريد تطبيقها على قاعدة البيانات. يمكنك كتابته في صيغ مثل XML، YAML، أو SQL. إليك مثال ملف **XML changelog** موجود في `src/main/resources/db/changelog/db.changelog-master.xml`:

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

هذا المثال يخلق جدول `users` مع ثلاثة أعمدة: `id`، `username`، و `email`. يمثل كل `<changeSet>` مجموعة من التغييرات التي سيتم تطبيقها.

---

### 4. تشغيل تطبيق Spring Boot
عند بدء تطبيق Spring Boot، يقوم Liquibase تلقائيًا:
- قراءة ملف changelog.
- التحقق من التغييرات التي تم تطبيقها بالفعل (متابعة في جدول يسمى `DATABASECHANGELOG`).
- تنفيذ أي تغييرات جديدة على قاعدة البيانات.

لا تحتاج إلى كتابة أي كود إضافي—تساعدك Spring Boot في التهيئة الذاتية.

---

### 5. تخصيص Liquibase (اختياري)
يمكنك تعديل سلوك Liquibase باستخدام الخصائص في `application.properties`. إليك بعض الخيارات الشائعة:

```properties
spring.liquibase.enabled=true          # تمكين أو تعطيل Liquibase
spring.liquibase.drop-first=false      # حذف قاعدة البيانات قبل تطبيق التغييرات (استخدم بحذر)
spring.liquibase.contexts=dev,prod     # تشغيل التغييرات فقط في بيئات محددة
```

تسمح هذه الإعدادات لك بتكيف Liquibase مع بيئتك أو عملية العمل.

---

### 6. استغلال الميزات المتقدمة
يقدم Liquibase ميزات قوية لتحسين إدارة المخطط:
- **البيانات والمواضيع**: التحكم في التغييرات التي سيتم تنفيذها في بيئات محددة (مثل `dev` مقابل `prod`).
- **الشرطيات السابقة**: التأكد من أن بعض الشروط (مثل وجود جدول) تم الوفاء بها قبل تطبيق تغيير.
- **التراجع**: تعريف كيفية التراجع عن تغيير إذا لزم الأمر.
- **إعادة التهيئة**: استخدام الدعم المدمج لتغييرات قاعدة البيانات المعقدة (مثل إعادة تسمية الأعمدة).

على سبيل المثال، إضافة سياق إلى تغيير:

```xml
<changeSet id="2" author="your-name" context="dev">
    <addColumn tableName="users">
        <column name="created_at" type="timestamp"/>
    </addColumn>
</changeSet>
```

هذا التغيير فقط يتم تنفيذ في سياق `dev`.

---

### 7. الاختبار مع قاعدة بيانات في الذاكرة
لاختبار، استخدم Liquibase مع قاعدة بيانات في الذاكرة مثل H2. أضف اعتماد H2:

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

ثم قم بتهيئة ملف `application.properties` للاختبار:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

سيقوم Liquibase بتطبيق التغييرات على قاعدة البيانات في الذاكرة أثناء الاختبارات.

---

### 8. التحكم بالنسخة من changelog
حفظ ملفات changelog في نظام التحكم بالنسخ (مثل Git) بجانب كود التطبيق. هذا يضمن أن مخطط قاعدة البيانات يتطور في نفس الوقت مع كودك، مما يجعل الإصدارات والتراجع أكثر توقعًا.

---

### ملخص
لاستخدام Liquibase في تطبيق Spring Boot:
1. أضف اعتماد Liquibase.
2. تهيئة موقع ملف changelog.
3. إنشاء ملف changelog مع تغييرات قاعدة البيانات.
4. قم بتشغيل تطبيقك—Liquibase يدير الباقي.

Liquibase أداة قوية لإدارة تغييرات مخطط قاعدة البيانات بطريقة منظمة ومضبوطة، متكاملة بشكل سلس مع Spring Boot.