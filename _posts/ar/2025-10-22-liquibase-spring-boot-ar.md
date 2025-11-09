---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دمج Liquibase مع Spring Boot
translated: true
type: note
---

## دمج Liquibase مع Spring Boot

Liquibase هو أداة مفتوحة المصدر شائعة لإدارة تغييرات مخطط قاعدة البيانات (الترحيل) بطريقة خاضعة لتحكم الإصدار. يوفر Spring Boot دعمًا ممتازًا للتكوين التلقائي لـ Liquibase، مما يسهل عملية الدمج. يفترض هذا الدليل أنك تستخدم Spring Boot 3.x (الأحدث اعتبارًا من 2025) مع Maven، لكن المفاهيم تنطبق على Gradle أيضًا. سنغطي الأساسيات خطوة بخطوة.

### المتطلبات الأساسية
- مشروع Spring Boot تم إعداده (على سبيل المثال، عبر Spring Initializr).
- قاعدة بيانات (مثل H2 للاختبار، أو PostgreSQL/MySQL للإنتاج) مُكونة في ملف `application.properties`.

### الخطوة 1: إضافة اعتماد Liquibase
قم بتضمين أداة بدء تشغيل Liquibase Spring Boot في ملف `pom.xml` الخاص بك. هذا يسحب Liquibase ويدمجه بسلاسة.

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId> <!-- For database connectivity -->
</dependency>
```

بالنسبة لـ Gradle، أضف إلى `build.gradle`:
```groovy
implementation 'org.liquibase:liquibase-core'
implementation 'org.springframework.boot:spring-boot-starter-jdbc'
```

قم بتشغيل `mvn clean install` (أو `./gradlew build`) لجلب التبعيات.

### الخطوة 2: تكوين Liquibase
يقوم Spring Boot بالكشف التلقائي عن Liquibase إذا قمت بوضع ملفات سجل التغييرات في الموقع الافتراضي. قم بالتخصيص عبر `application.properties` (أو المكافئ بـ `.yml`).

مثال `application.properties`:
```properties
# إعداد قاعدة البيانات (اضبطها حسب قاعدة البيانات الخاصة بك)
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driver-class-name=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# تكوين Liquibase
spring.liquibase.change-log=classpath:db/changelog/db.changelog-master.xml
spring.liquibase.enabled=true  # الإعداد الافتراضي هو true
spring.liquibase.drop-first=false  # اضبط على true في بيئة التطوير لحذف المخطط عند بدء التشغيل
```

- `change-log`: المسار إلى ملف سجل التغييرات الرئيسي (الافتراضي: `db/changelog/db.changelog-master.xml`).
- تمكين/تعطيل باستخدام `spring.liquibase.enabled`.
- بالنسبة للسياقات/الملفات الشخصية، استخدم `spring.liquibase.contexts=dev` لتشغيل تغييرات محددة.

### الخطوة 3: إنشاء ملفات سجل التغييرات
يستخدم Liquibase "سجلات التغييرات" لتحديد تغييرات المخطط. قم بإنشاء هيكل دليل تحت `src/main/resources`:
```
src/main/resources/
└── db/
    └── changelog/
        ├── db.changelog-master.xml  # الملف الرئيسي الذي يتضمن الآخرين
        └── changes/
            ├── 001-create-users-table.xml  # التغييرات الفردية
            └── 002-add-email-column.xml
```

#### سجل التغييرات الرئيسي (`db.changelog-master.xml`)
هذا يتضمن سجلات التغييرات الأخرى:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.24.xsd">

    <include file="changes/001-create-users-table.xml"/>
    <include file="changes/002-add-email-column.xml"/>
</databaseChangeLog>
```

#### نموذج تغيير (`001-create-users-table.xml`)
تحديد إنشاء جدول:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                                       http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.24.xsd">

    <changeSet id="001" author="yourname">
        <createTable tableName="users">
            <column name="id" type="bigint">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="name" type="varchar(255)">
                <constraints nullable="false"/>
            </column>
        </createTable>
    </changeSet>
</databaseChangeLog>
```

- استخدم تنسيقات XML أو YAML أو JSON أو SQL لسجلات التغييرات.
- كل `<changeSet>` يمثل ترحيلًا بمعرف (للتتبع).
- قم بتشغيل `java -jar target/your-app.jar` لبدء التطبيق — يطبق Liquibase التغييرات تلقائيًا أثناء التهيئة.

### الخطوة 4: التشغيل والاختبار
- **عند بدء التشغيل**: يقوم Spring Boot بتشغيل Liquibase قبل أن يبدأ تطبيقك بالكامل.
- **التراجع**: استخدم `spring.liquibase.rollback-file` أو واجهة سطر الأوامر للاختبار.
- **دمج واجهة سطر الأوامر**: للتشغيل اليدوي، أضف إضافة Maven الخاصة بـ Liquibase:
  ```xml
  <plugin>
      <groupId>org.liquibase</groupId>
      <artifactId>liquibase-maven-plugin</artifactId>
      <version>4.24.0</version>
      <configuration>
          <changeLogFile>src/main/resources/db/changelog/db.changelog-master.xml</changeLogFile>
          <url>jdbc:h2:mem:testdb</url>
          <username>sa</username>
          <password></password>
      </configuration>
  </plugin>
  ```
  ثم قم بتشغيل `mvn liquibase:update`.

- **التحقق**: قم بتمكين `spring.liquibase.validate-on-migrate=true` للتحقق من سجلات التغييرات.

### نصائح شائعة
- **الملفات الشخصية**: استخدم `@Profile("dev")` على beans إذا لزم الأمر، لكن Liquibase يعمل بشكل عام ما لم يتم تصفيته.
- **الشروط المسبقة**: أضف `<preConditions>` في مجموعات التغيير للتحقق من حالة قاعدة البيانات.
- **تنسيق SQL**: لـ SQL الخام، أنشئ ملفات `.sql` وقم بتضمينها: `<sqlFile path="changes/create-users.sql" relativeToChangelogFile="true"/>`.
- **استكشاف الأخطاء وإصلاحها**: تحقق من السجلات للبحث عن أخطاء (مثل تلك ذات البادئة `liquibase`). تأكد من صحة عنوان URL لقاعدة البيانات.
- **الإنتاج**: استخدم Flyway إذا كنت تفضل ذلك، لكن Liquibase يتفوق في التغييرات المعقدة ودعم قواعد البيانات المتعددة.

للحصول على ميزات متقدمة مثل التراجع الموسوم أو الامتدادات المخصصة، راجع الوثائق.

### المراجع
- [تكوين Spring Boot التلقائي لـ Liquibase](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#io.liquibase)
- [الوثائق الرسمية لـ Liquibase](https://docs.liquibase.com/start/home.html)
- [برنامج Spring Boot + Liquibase التعليمي على Baeldung](https://www.baeldung.com/liquibase-refactor-schema-of-jpa-entity-in-spring-boot)