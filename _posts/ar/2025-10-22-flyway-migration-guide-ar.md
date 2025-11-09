---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل ترحيل قاعدة البيانات باستخدام Flyway
translated: true
type: note
---

### مقدمة عن Flyway
Flyway هو أداة مفتوحة المصدر شائعة لإدارة هجرات مخطط قاعدة البيانات بطريقة خاضعة للتحكم بالإصدار. تتيح لك تطبيق تغييرات تدريجية على قاعدة البيانات الخاصة بك (مثل إنشاء الجداول، أو تعديل الأعمدة، أو إدراج البيانات) بطريقة قابلة للتكرار وآمنة. في تطبيقات Java، يمكن دمج Flyway عبر واجهة برمجة التطبيقات الخاصة به، وغالبًا ما يتم تشغيله عند بدء تشغيل التطبيق لضمان أن مخطط قاعدة بيانات محدث قبل أن يتفاعل الكود الخاص بك معه. يعمل مع معظم قواعد البيانات عبر JDBC (مثل PostgreSQL، MySQL، Oracle).

### الخطوة 1: إضافة تبعية Flyway
أضف Flyway إلى ملف البناء الخاص بك. استخدم الإصدار مفتوح المصدر ما لم تكن بحاجة إلى ميزات المؤسسة.

**Maven (`pom.xml`)**:
```xml
<dependencies>
    <dependency>
        <groupId>org.flywaydb</groupId>
        <artifactId>flyway-core</artifactId>
        <version>11.14.1</version> <!-- تحقق من أحدث إصدار -->
    </dependency>
    <!-- أضف مشغل JDBC لقاعدة البيانات الخاصة بك، على سبيل المثال، لـ PostgreSQL -->
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
        <version>42.7.3</version>
    </dependency>
</dependencies>
```

**Gradle (`build.gradle`)**:
```groovy
dependencies {
    implementation 'org.flywaydb:flyway-core:11.14.1'
    // أضف مشغل JDBC لقاعدة البيانات الخاصة بك
    implementation 'org.postgresql:postgresql:42.7.3'
}
```

ستحتاج أيضًا إلى مشغل JDBC لقاعدة البيانات المستهدفة.

### الخطوة 2: تكوين Flyway
يستخدم Flyway واجهة برمجة تطبيقات Fluent للتكوين. تشمل الإعدادات الرئيسية تفاصيل اتصال قاعدة البيانات، ومواقع نصوص الهجرة، ووظائف الاستدعاء الاختيارية.

في كود Java الخاص بك، أنشئ نسخة من `Flyway`:
```java
import org.flywaydb.core.Flyway;

public class DatabaseMigration {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb";
        String user = "username";
        String password = "password";

        Flyway flyway = Flyway.configure()
                .dataSource(url, user, password)
                .locations("classpath:db/migration")  // مجلد لنصوص SQL (الافتراضي: db/migration)
                .load();
    }
}
```
- `locations`: يشير إلى مكان تخزين ملفات الهجرة الخاصة بك (على سبيل المثال، `src/main/resources/db/migration` للمسار classpath).
- تكوينات شائعة أخرى: `.baselineOnMigrate(true)` لإنشاء خط أساس للمخططات الموجودة، أو `.table("flyway_schema_history")` لتخصيص جدول السجل.

### الخطوة 3: كتابة نصوص الهجرة
نصوص الهجرة هي ملفات SQL توضع في الموقع المُكون (على سبيل المثال، `src/main/resources/db/migration`). يقوم Flyway بتطبيقها بالترتيب.

#### اصطلاحات التسمية
- **هجرات مُصَرفة** (لتغييرات المخطط لمرة واحدة): `V<version>__<description>.sql` (على سبيل المثال، `V1__Create_person_table.sql`، `V2__Add_age_column.sql`).
  - تنسيق الإصدار: استخدم الشرطات السفلية للأجزاء (على سبيل المثال، `V1_1__Initial.sql`).
- **هجرات قابلة للتكرار** (لمهام مستمرة مثل العروض): `R__<description>.sql` (على سبيل المثال، `R__Update_view.sql`). يتم تشغيلها في كل مرة إذا تغيرت.
- يتم تطبيق الملفات بالترتيب المعجمي.

#### نصوص مثال
أنشئ هذه الملفات في `src/main/resources/db/migration`.

**V1__Create_person_table.sql**:
```sql
CREATE TABLE person (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO person (id, name) VALUES (1, 'John Doe');
```

**V2__Add_age_column.sql**:
```sql
ALTER TABLE person ADD COLUMN age INT;
```

**R__Populate_names.sql** (قابل للتكرار):
```sql
UPDATE person SET name = CONCAT(name, ' (Updated)') WHERE id = 1;
```

يتتبع Flyway الهجرات المطبقة في جدول `flyway_schema_history`.

للحسابات المعقدة غير المناسبة لـ SQL، استخدم الهجرات القائمة على Java (نفذ `org.flywaydb.core.api.migration.java.JavaMigration`).

### الخطوة 4: تشغيل الهجرات برمجيًا
استدعِ `migrate()` لتطبيق الهجرات المعلقة. قم بدمج هذا في بدء تشغيل تطبيقك (على سبيل المثال، في `main()` أو Spring `@PostConstruct`).

```java
import org.flywaydb.core.Flyway;
import org.flywaydb.core.api.FlywayException;

public class DatabaseMigration {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb";
        String user = "username";
        String password = "password";

        Flyway flyway = Flyway.configure()
                .dataSource(url, user, password)
                .locations("classpath:db/migration")
                .load();

        try {
            flyway.migrate();  // يطبق جميع الهجرات المعلقة
            System.out.println("تمت هجرة قاعدة البيانات بنجاح!");
        } catch (FlywayException e) {
            System.err.println("فشلت الهجرة: " + e.getMessage());
            // تعامل مع الخطأ (على سبيل المثال، الخروج أو التراجع)
        }

        // الآن ابدأ بقية تطبيقك
    }
}
```

- `migrate()`: يطبق الهجرات المُصَرفة بالترتيب، ثم القابلة للتكرار.
- أوامر أخرى: `flyway.info()` للحالة، `flyway.repair()` لإصلاح المشكلات، `flyway.validate()` للتحقق من الاتساق.
- شغّل هذا قبل أي عمليات على قاعدة البيانات لضمان توافق المخطط.

### أفضل الممارسات
- حافظ على الهجرات عديمة التأثير (آمنة لإعادة التشغيل).
- اختبر الهجرات على نسخة من بيانات الإنتاج.
- استخدم التحكم بالإصدار لملفات الهجرة.
- لـ Spring Boot، أضف `spring-boot-starter-jdbc` وعيّن `spring.flyway.enabled=true` في `application.properties` للتكوين التلقائي.

### المراجع
- [توثيق Flyway API (Java)](https://documentation.red-gate.com/fd/api-java-277579358.html)
- [توثيق هجرات Flyway](https://documentation.red-gate.com/fd/migrations-271585107.html)
- [بدء استخدام Flyway](https://documentation.red-gate.com/fd/getting-started-with-flyway-184127223.html)