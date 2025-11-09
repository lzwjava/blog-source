---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: اختبار قاعدة بيانات H2 في سبرينغ بوت
translated: true
type: note
---

### استخدام قاعدة بيانات H2 في اختبارات JUnit مع Spring Boot

تُعتبر H2 قاعدة بيانات خفيفة الوزن تعمل في الذاكرة وهي مثالية للاختبارات الوحدوية والتكاملية في تطبيقات Java، خاصةً مع Spring Boot. تتيح لك تشغيل الاختبارات بسرعة دون الحاجة إلى إعداد قاعدة بيانات خارجية. فيما يلي دليل خطوة بخطوة يفترض وجود مشروع Spring Boot مع JPA/Hibernate. إذا كنت لا تستخدم Spring، فيمكنك استخدام H2 عبر JDBC العادي (انظر الملاحظات في النهاية).

#### الخطوة 1: إضافة تبعية H2
قم بتضمين تبعية H2 في ملف `pom.xml` (إذا كنت تستخدم Maven) أو `build.gradle` (إذا كنت تستخدم Gradle). حدد نطاقها كـ `test` لتجنب تضمينها في بيئة الإنتاج.

**Maven (`pom.xml`):**
```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>test</scope>
</dependency>
```

**Gradle (`build.gradle`):**
```gradle
testImplementation 'com.h2database:h2'
```

هذا يسحب ملف JAR الخاص بـ H2 لتنفيذ الاختبارات فقط.

#### الخطوة 2: تكوين H2 في خصائص الاختبار
أنشئ أو حدّث ملف `src/test/resources/application.properties` (أو `application-test.yml`) للإشارة إلى H2. هذا يتجاوز إعدادات قاعدة بيانات الإنتاج.

**application.properties:**
```
# تكوين قاعدة بيانات H2
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# وحدة تحكم H2 (اختياري، لأغراض التصحيح)
spring.h2.console.enabled=true

# إعدادات JPA/Hibernate
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.show-sql=true
```

- `mem:testdb`: قاعدة بيانات في الذاكرة باسم "testdb".
- `create-drop`: تنشئ الجداول تلقائيًا عند البدء وتحذفها عند الإغلاق.
- مكّن وحدة التحكم H2 على الرابط `http://localhost:8080/h2-console` أثناء الاختبارات للتفتيش (استخدم JDBC URL: `jdbc:h2:mem:testdb`).

إذا كنت تستخدم Profiles، فقم بتنشيطها باستخدام `@ActiveProfiles("test")` في فئة الاختبار الخاصة بك.

#### الخطوة 3: كتابة اختبار JUnit
استخدم `@SpringBootTest` لتحميل السياق الكامل أو `@DataJpaTest` للاختبارات المركزة على المستودع (Repository). علّق الاختبار بـ `@Test` واستخدم JUnit 5 (`@ExtendWith(SpringExtension.class)`).

**مثال: اختبار JPA Repository**
لنفترض أن لديك `Entity` مثل `User` و `UserRepository` يمتد من `JpaRepository`.

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.ActiveProfiles;

import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest  // يحمل فقط حبوب (Beans) المرتبطة بـ JPA لاختبارات أسرع
@ActiveProfiles("test")  // ينشط ملف تعريف الاختبار
public class UserRepositoryTest {

    @Autowired
    private UserRepository userRepository;

    @Test
    public void shouldSaveAndFindUser() {
        // Given
        User user = new User("John Doe", "john@example.com");
        userRepository.save(user);

        // When
        User foundUser = userRepository.findByEmail("john@example.com").orElse(null);

        // Then
        assertThat(foundUser).isNotNull();
        assertThat(foundUser.getName()).isEqualTo("John Doe");
    }
}
```

- `@DataJpaTest`: يُهيئ H2 تلقائيًا ويرجع المعاملات بعد كل اختبار.
- استخدم تأكيدات `AssertJ` أو `JUnit` للتحقق.
- لاختبارات طبقة الخدمة (Service Layer)، استخدم `@SpringBootTest` وقم بحقن الخدمات/المستودعات.

شغّل الاختبار باستخدام `mvn test` أو من خلال مشغّل الاختبارات في بيئة التطوير المتكاملة (IDE). يبدأ كل اختبار بقاعدة بيانات جديدة.

#### الخطوة 4: نصائح متقدمة
- **هجرة Flyway/Liquibase**: إذا كنت تستخدم هجرات Schema، أضفها إلى `src/test/resources` وسيقوم H2 بتطبيقها.
- **اختبار واقعي**: H2 تحاكي معظم لهجات SQL ولكن قد تختلف عن قاعدة بيانات الإنتاج (مثل PostgreSQL). للحصول على تطابق أوثق، فكّر في استخدام Testcontainers مع حاوية قاعدة بيانات حقيقية.
- **استبعاد تكوين الإنتاج**: في `pom.xml`، استخدم Profiles لاستبعاد برامج تشغيل قاعدة بيانات الحقيقية في الاختبارات:
  ```xml
  <profile>
      <id>test</id>
      <dependencies>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-data-jpa</artifactId>
              <exclusions>
                  <exclusion>
                      <groupId>mysql</groupId>  <!-- أو قاعدة بيانات الإنتاج الخاصة بك -->
                      <artifactId>mysql-connector-java</artifactId>
                  </exclusion>
              </exclusions>
          </dependency>
      </dependencies>
  </profile>
  ```
- **استكشاف الأخطاء وإصلاحها**: إذا كانت الاختبارات تستخدم قاعدة بيانات الإنتاج، تأكد من `spring.profiles.active=test` أو استخدم `@TestPropertySource`.

#### JUnit المستقل (بدون Spring)
لاستخدام JDBC العادي بدون Spring:
1. أضف تبعية H2 (كما هو مذكور أعلاه).
2. في اختبارك:
```java
import org.h2.jdbcx.JdbcDataSource;
import org.junit.jupiter.api.Test;

public class StandaloneH2Test {
    @Test
    public void testH2Connection() throws Exception {
        JdbcDataSource ds = new JdbcDataSource();
        ds.setURL("jdbc:h2:mem:test;DB_CLOSE_DELAY=-1");
        ds.setUser("sa");
        ds.setPassword("");

        try (Connection conn = ds.getConnection();
             Statement stmt = conn.createStatement()) {
            stmt.execute("CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255))");
            stmt.execute("INSERT INTO users VALUES (1, 'Test User')");
            ResultSet rs = stmt.executeQuery("SELECT * FROM users");
            assertTrue(rs.next());
        }
    }
}
```
هذا ينشئ قاعدة بيانات في الذاكرة لكل اختبار.

لمزيد من التفاصيل، انظر المراجع أدناه.

[Setting Up H2 for Testing in Spring Boot](https://medium.com/@paulkunda/setting-up-h2-for-testing-in-spring-boot-245d3a98e405)  
[Self-Contained Testing Using an In-Memory Database | Baeldung](https://www.baeldung.com/spring-jpa-test-in-memory-database)  
[Setting Up H2 for Testing in Spring Boot application](https://medium.com/@akshatakanaje08/setting-up-h2-for-testing-in-spring-boot-application-7f016220a475)  
[Test Spring Data Repositories with H2 in-memory database](https://www.geekyhacker.com/test-spring-data-repositories-with-h2-in-memory-database/)