---
audio: false
generated: true
lang: ar
layout: post
title: ربيع بيانات ريديس
translated: true
type: note
---

Spring Data Redis هي أداة رائعة لدمج Redis - وهو مخزن بيانات في الذاكرة عالي الأداء - في تطبيق Spring الخاص بك. فهو يبسط العمل مع Redis من خلال توفير واجهة مألوفة على نمط المستودع وتجريدات فوق عمليات Redis منخفضة المستوى. دعنا نتناول كيفية إعداده واستخدامه خطوة بخطوة.

### 1. **إعداد مشروعك**
أولاً، قم بتضمين تبعية Spring Data Redis في مشروعك. إذا كنت تستخدم Maven، أضف هذا إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

أما بالنسبة لـ Gradle، فاستخدم:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
```

يتضمن هذا عميل Redis (Jedis أو Lettuce - حيث يعتبر Lettuce الافتراضي). إذا كنت تفضل Jedis، يمكنك إضافته صراحةً واستبعاد Lettuce:

```xml
<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
    <exclusions>
        <exclusion>
            <groupId>io.lettuce</groupId>
            <artifactId>lettuce-core</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

### 2. **تكوين Redis**
قم بتكوين اتصال Redis الخاص بك في `application.properties` أو `application.yml`. لنسخة Redis محلية تعمل على المنفذ الافتراضي (6379):

```properties
spring.redis.host=localhost
spring.redis.port=6379
spring.redis.password= # اختياري، إذا كان خادم Redis الخاص بك محميًا بكلمة مرور
spring.redis.database=0 # فهرس قاعدة البيانات الافتراضي
```

إذا كنت تستخدم خادم Redis بعيد أو خدمة مثل AWS ElastiCache، فقم بتحديث المضيف وبيانات الاعتماد وفقًا لذلك.

### 3. **الاستخدام الأساسي مع RedisTemplate**
يوفر Spring Data Redis `RedisTemplate` للعمليات منخفضة المستوى. يمكنك حقنه تلقائيًا في خدمتك أو مكونك:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

@Service
public class RedisService {
    private final RedisTemplate<String, String> redisTemplate;

    @Autowired
    public RedisService(RedisTemplate<String, String> redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    public void saveData(String key, String value) {
        redisTemplate.opsForValue().set(key, value);
    }

    public String getData(String key) {
        return redisTemplate.opsForValue().get(key);
    }
}
```

- `RedisTemplate` عام: `<String, String>` يعني أن المفاتيح والقيم هي سلاسل نصية. يمكنك استخدام أنواع أخرى (مثل `<String, Object>`).
- `opsForValue()` مخصص لعمليات المفتاح-القيمة البسيطة. تشمل الطرق الأخرى `opsForList()`، `opsForSet()`، `opsForHash()`، إلخ، لهياكل بيانات Redis المختلفة.

### 4. **الاستخدام مع الكائنات**
لتخزين واسترداد كائنات Java، قم بتكوين `RedisTemplate` مع المُسلسلات. يقوم Spring Boot بتكوينه تلقائيًا، ولكن يمكنك تخصيصه إذا لزم الأمر:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.Jackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;

@Configuration
public class RedisConfig {
    @Bean
    public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory connectionFactory) {
        RedisTemplate<String, Object> template = new RedisTemplate<>();
        template.setConnectionFactory(connectionFactory);
        template.setKeySerializer(new StringRedisSerializer());
        template.setValueSerializer(new Jackson2JsonRedisSerializer<>(Object.class));
        template.afterPropertiesSet();
        return template;
    }
}
```

الآن يمكنك تخزين واسترداد الكائنات:

```java
public class Person {
    private String firstName;
    private String lastName;

    // المُنشئ الافتراضي (لإلغاء التسلسل)
    public Person() {}

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // وسائل الوصول (Getters and setters)
    public String getFirstName() { return firstName; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public String getLastName() { return lastName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
}
```

```java
@Service
public class PersonRedisService {
    private final RedisTemplate<String, Object> redisTemplate;

    @Autowired
    public PersonRedisService(RedisTemplate<String, Object> redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    public void savePerson(String key, Person person) {
        redisTemplate.opsForValue().set(key, person);
    }

    public Person getPerson(String key) {
        return (Person) redisTemplate.opsForValue().get(key);
    }
}
```

### 5. **نهج المستودع (Repository)**
للحصول على تجريد عالي المستوى، استخدم مستودعات Spring Data Redis. قم بتعريف كيان ومستودع:

```java
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@RedisHash("Person") // يعين إلى تجزئة Redis بالبادئة "Person"
public class Person {
    @Id
    private String id; // سيكون مفتاح Redis هو "Person:<id>"
    private String firstName;
    private String lastName;

    // المنشئات، وسائل الوصول (كما ورد أعلاه)
}
```

```java
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, String> {
}
```

استخدمه هكذا:

```java
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

    public void findPerson(String id) {
        Person person = repository.findById(id).orElse(null);
        if (person != null) {
            System.out.println(person.getFirstName() + " " + person.getLastName());
        }
    }
}
```

- `@RedisHash` يعين الكيان إلى تجزئة Redis.
- يوفر المستودع عمليات CRUD جاهزة للاستخدام.

### 6. **تشغيل تطبيقك**
تأكد من أن Redis يعمل محليًا (على سبيل المثال، عبر Docker: `docker run -d -p 6379:6379 redis`) أو اتصل بنسخة بعيدة. ثم ابدأ تطبيق Spring Boot الخاص بك:

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

### 7. **الميزات المتقدمة**
- **‏TTL (مدة الصلاحية):** ‏عيّن تاريخ انتهاء الصلاحية على المفاتيح باستخدام `redisTemplate.expire(key, 10, TimeUnit.MINUTES)`.
- **‏Hashes (التجزئات):** ‏استخدم `opsForHash()` للعمل مع تجزئات Redis مباشرة.
- **‏النشر/الاشتراك (Pub/Sub):** ‏استخدم `RedisMessageListenerContainer` للتراسل.

### مثال على سير العمل
1. احفظ كائن `Person` باستخدام `repository.save()` أو `redisTemplate.opsForValue().set()`.
2. استرجعه باستخدام `repository.findById()` أو `redisTemplate.opsForValue().get()`.
3. تحقق من نسخة Redis الخاصة بك (على سبيل المثال، باستخدام `redis-cli`) لرؤية البيانات.

هذا يغطي الأساسيات! إذا كنت ترغب في استكشاف التخزين المؤقت، أو النشر/الاشتراك، أو شيء محدد، فأخبرني بما تهدف إليه، وسأتعمق أكثر. كيف يتناسب هذا مع ما تحاول القيام به؟