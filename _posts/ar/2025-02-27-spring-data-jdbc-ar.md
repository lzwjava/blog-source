---
audio: false
generated: true
lang: ar
layout: post
title: ربيع البيانات جي دي بي سي
translated: true
type: note
---

Spring Data JDBC هي مكتبة قوية تبسط التفاعلات مع قواعد البيانات في تطبيقات Spring من خلال توفير نهج خفيف الوزن يعتمد على التوضيحات annotation للعمل مع قواعد البيانات العلائقية. إنه أقل توجيهاً من Spring Data JPA ويركز على طريقة أبسط وأكثر وضوحاً لتعيين الكائنات إلى جداول قاعدة البيانات. أدناه، سأرشدك خلال الأساسيات حول كيفية استخدامه.

### 1. **إعداد مشروعك**
للبدء، ستحتاج إلى تضمين Spring Data JDBC في مشروعك. إذا كنت تستخدم Maven، أضف التبعية التالية إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jdbc</artifactId>
</dependency>
```

ستحتاج أيضًا إلى مشغل JDBC لقاعدة البيانات الخاصة بك (مثل H2 أو MySQL أو PostgreSQL). على سبيل المثال، لـ H2:

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

إذا كنت تستخدم Gradle، فإن المكافئات ستكون:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-jdbc'
runtimeOnly 'com.h2database:h2'
```

### 2. **تكوين قاعدة البيانات الخاصة بك**
في ملف `application.properties` أو `application.yml` الخاص بك، قم بتكوين اتصال قاعدة البيانات. لقاعدة بيانات H2 في الذاكرة، قد يبدو كما يلي:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.h2.console.enabled=true
```

لقاعدة بيانات حقيقية مثل PostgreSQL، قم بتعديل الرابط URL واسم المستخدم وكلمة المرور وفقًا لذلك.

### 3. **تحديد نموذج النطاق Domain Model الخاص بك**
أنشئ فئة كيان بسيطة لتمثيل جدول في قاعدة البيانات الخاصة بك. يستخدم Spring Data JDBC اصطلاحات حيث يتم تعيين اسم الفئة إلى اسم الجدول (بالحروف الصغيرة بشكل افتراضي)، وتتعين الحقول إلى أعمدة.

```java
import org.springframework.data.annotation.Id;

public class Person {
    @Id
    private Long id;
    private String firstName;
    private String lastName;

    // المُنشئ الافتراضي (مطلوب من قبل Spring Data JDBC)
    public Person() {}

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // وسائل الجلب والتعيين Getters and setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getFirstName() { return firstName; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public String getLastName() { return lastName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
}
```

- `@Id` تحدد المفتاح الأساسي.
- يتوقع Spring Data JDBC مُنشئًا بدون وسائط.
- سيتم تسمية الجدول `person` ما لم يتم التجاوز.

### 4. **إنشاء مستودع Repository**
حدد واجهة interface تمتد من `CrudRepository` للتعامل مع عمليات CRUD الأساسية:

```java
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, Long> {
}
```

هذا كل شيء! لا تحتاج إلى تنفيذها — فـ Spring Data JDBC يولد التنفيذ أثناء وقت التشغيل.

### 5. **استخدام المستودع Repository**
احقن المستودع في خدمة service أو وحدة تحكم controller واستخدمه:

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
إذا كنت تستخدم Spring Boot، فأنشئ فئة رئيسية مع `@SpringBootApplication` وقم بتشغيلها:

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

سيقوم Spring Boot بالتكوين التلقائي لمصدر البيانات وـ Spring Data JDBC.

### 7. **اختياري: استعلامات مخصصة**
إذا كنت بحاجة إلى استعلامات مخصصة، يمكنك إضافة طرق إلى مستودعك مع `@Query`:

```java
import org.springframework.data.jdbc.repository.query.Query;
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, Long> {
    @Query("SELECT * FROM person WHERE first_name = :name")
    List<Person> findByFirstName(String name);
}
```

### نقاط رئيسية يجب تذكرها
- **لا يوجد تحميل كسول Lazy Loading:** على عكس JPA، لا يدعم Spring Data JDBC التحميل الكسول. تحتاج العلاقات (مثل one-to-many) إلى نمذجة صريحة مع جذور التجميع Aggregate Roots.
- **جذر التجميع Aggregate Root:** كل كيان هو جزء من تجميع aggregate، ويتم حفظ أو استرجاع الجذر فقط مباشرة.
- **إنشاء المخطط Schema:** لا ينشئ Spring Data JDBC الجداول تلقائيًا. ستحتاج إلى توفير المخطط (على سبيل المثال، عبر `schema.sql` في `src/main/resources`):

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
3. استرجعه باستخدام `repository.findById()` أو `findAll()`.

هذه هي الأساسيات! إذا كنت ترغب في التعمق أكثر في العلاقات أو التعيينات المخصصة أو شيء محدد، دعني أعرف ما الذي تهدف إليه وسأخصص الشرح accordingly. كيف يعمل هذا بالنسبة لك حتى الآن؟