---
audio: false
generated: true
lang: ar
layout: post
title: 'Spring Data JDBC


  بِسْمِ اللهِ الرَّحْمنِ الرَّحِيمِ


  Spring Data JDBC'
translated: true
---

Spring Data JDBC هو مكتبة قوية تسهل تعاملات قاعدة البيانات في تطبيق Spring من خلال تقديم نهج خفيف الوزن، يعتمد على التعليقات، للعمل مع قواعد البيانات العلائقية. إنه أقل تعليقات من Spring Data JPA ويركز على طريقة أبسط، أكثر وضوحًا، لتخزين الكائنات في جداول قاعدة البيانات. أدخلك في الأساسيات حول كيفية استخدامه.

### 1. **إعداد مشروعك**
لبدء العمل، عليك تضمين Spring Data JDBC في مشروعك. إذا كنت تستخدم Maven، أضف التبعية التالية إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jdbc</artifactId>
</dependency>
```

سيحتاجك أيضًا إلى سائق JDBC لقاعدة البيانات الخاصة بك (مثل H2، MySQL، PostgreSQL). على سبيل المثال، لـ H2:

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

إذا كنت تستخدم Gradle، فسيكون المقابل:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-jdbc'
runtimeOnly 'com.h2database:h2'
```

### 2. **تكوين قاعدة البيانات**
في ملف `application.properties` أو `application.yml` الخاص بك، قم بتكوين اتصال قاعدة البيانات. على سبيل المثال، لقاعدة بيانات H2 في الذاكرة:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.h2.console.enabled=true
```

لقاعدة بيانات حقيقية مثل PostgreSQL، قم بتعديل URL، اسم المستخدم، وكلمة المرور وفقًا لذلك.

### 3. **تعريف نموذج المجال**
إنشاء فئة كيان بسيطة لتمثيل جدول في قاعدة البيانات الخاصة بك. Spring Data JDBC يستخدم التقاليد حيث يتم Mapping اسم الفئة إلى اسم الجدول (بشكل افتراضي بالخط الصغير)، و يتم Mapping الحقول إلى الأعمدة.

```java
import org.springframework.data.annotation.Id;

public class Person {
    @Id
    private Long id;
    private String firstName;
    private String lastName;

    // Constructor افتراضي (مطلوب من Spring Data JDBC)
    public Person() {}

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // Getters and setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getFirstName() { return firstName; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public String getLastName() { return lastName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
}
```

- `@Id` يحدد المفتاح الأساسي.
- Spring Data JDBC يتوقع Constructor بدون Arguments.
- سيتم تسمية الجدول `person` إلا إذا تم تجاوز ذلك.

### 4. **إنشاء مستودع**
تعريف واجهة تمتد `CrudRepository` لتسجيل العمليات الأساسية CRUD:

```java
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, Long> {
}
```

هذا كل شيء! لا تحتاج إلى تنفيذها - Spring Data JDBC يولد التنفيذ في وقت التشغيل.

### 5. **استخدام المستودع**
قم بإدخال المستودع في خدمة أو Controller واستخدمه:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class PersonService {
    private final PersonRepository repository;

    @Autowired
    public PersonService(PersonRepository repository) {
        this.repository = repository;
    }

    public void savePerson() {
        Person person = new Person("John", "Doe");
        repository.save(person);
        System.out.println("Saved person with ID: " + person.getId());
    }

    public void listPeople() {
        Iterable<Person> people = repository.findAll();
        people.forEach(p -> System.out.println(p.getFirstName() + " " + p.getLastName()));
    }
}
```

### 6. **تشغيل تطبيقك**
إذا كنت تستخدم Spring Boot، قم بإنشاء فئة رئيسية مع `@SpringBootApplication` و قم بتشغيلها:

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

Spring Boot سيقوم بتكوين المصدر و Spring Data JDBC تلقائيًا.

### 7. **اختياري: استعلامات مخصصة**
إذا كنت تحتاج إلى استعلامات مخصصة، يمكنك إضافة طرق إلى مستودعك مع `@Query`:

```java
import org.springframework.data.jdbc.repository.query.Query;
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, Long> {
    @Query("SELECT * FROM person WHERE first_name = :name")
    List<Person> findByFirstName(String name);
}
```

### النقاط الرئيسية التي يجب تذكرها
- **لا يوجد تحميل متأخر:** على عكس JPA، Spring Data JDBC لا يدعم التحميل المتأخر. العلاقات (مثل واحد إلى العديد) تحتاج إلى نمذجة صريحة مع جذور التجمعات.
- **جذر التجمع:** كل كيان جزء من تجمع، و فقط الجذر يتم حفظه أو استرجاعه مباشرة.
- **إنشاء الهيكل:** Spring Data JDBC لا يخلق الجداول تلقائيًا. عليك توفير الهيكل (على سبيل المثال، عبر `schema.sql` في `src/main/resources`):

```sql
CREATE TABLE person (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);
```

### مثال على سير العمل
1. ابدأ تطبيقك.
2. احفظ كائن `Person` باستخدام `repository.save()`.
3. استرجعها باستخدام `repository.findById()` أو `findAll()`.

هذا هو الأساس! إذا كنت تريد الغوص في العلاقات، أو المappings المخصصة، أو شيء معين، فقل لي ما هو هدفك، وسأقوم بتخصيص التفسير. كيف يعمل هذا حتى الآن؟