---
audio: true
lang: ar
layout: post
title: 'Spring Data Redis'
translated: true
---

Spring Data Redis هو أداة رائعة لتكامل Redis، وهو مخزن بيانات في الذاكرة ذو أداء عالٍ، في تطبيق Spring الخاص بك. يسهل العمل مع Redis من خلال تقديم واجهة مستودع مألوفة وعبارات على العمليات المنخفضة المستوى لRedis. دعونا نمر عبر كيفية إعداده واستخدامه خطوة بخطوة.

### 1. **إعداد مشروعك**
أولاً، أضف التبعية Spring Data Redis إلى مشروعك. إذا كنت تستخدم Maven، أضف هذا إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

للمباني، استخدم:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
```

هذا يتضمن عميل Redis (Jedis أو Lettuce—Lettuce هو الافتراضي). إذا كنت تفضل Jedis، يمكنك إضافته بشكل صريح واستبعاد Lettuce:

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
قم بتكوين اتصال Redis في `application.properties` أو `application.yml`. لمثال Redis محلي يعمل على الميناء الافتراضي (6379):

```properties
spring.redis.host=localhost
spring.redis.port=6379
spring.redis.password= # اختياري، إذا كان لديك كلمة مرور على خادم Redis الخاص بك
spring.redis.database=0 # الفهرس الافتراضي للمخزن
```

إذا كنت تستخدم خادم Redis عن بُعد أو خدمة مثل AWS ElastiCache، قم بتحديث المضيف والمعلومات المعتمدة وفقًا لذلك.

### 3. **الاستخدام الأساسي مع RedisTemplate**
يوفر Spring Data Redis `RedisTemplate` للعمليات المنخفضة المستوى. يمكنك حقنها في خدمة أو مكون:

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

- `RedisTemplate` هو عام: `<String, String>` يعني أن المفاتيح والقيم هي من نوع نصي. يمكنك استخدام أنواع أخرى (مثل `<String, Object>`).
- `opsForValue()` هو للعمليات البسيطة للمفاتيح والقيم. هناك طرق أخرى مثل `opsForList()`, `opsForSet()`, `opsForHash()`, إلخ، للعمل مع مختلف هياكل بيانات Redis.

### 4. **الاستخدام مع الكائنات**
لحفظ واسترجاع كائنات Java، قم بتكوين `RedisTemplate` مع محولين. Spring Boot يقوم بتكوينه تلقائيًا، ولكن يمكنك تخصيصه إذا كان ذلك ضروريًا:

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

الآن يمكنك حفظ واسترجاع الكائنات:

```java
public class Person {
    private String firstName;
    private String lastName;

    // المبدئ الافتراضي (للترميز)
    public Person() {}

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // المحددات والمحددات
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

### 5. **الاستخدام مع المستودعات**
لاستخدام مستوى أعلى من التعبئة، استخدم مستودعات Spring Data Redis. حدد كيانًا ومستودعًا:

```java
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@RedisHash("Person") // يربط إلى هاش Redis مع البادئة "Person"
public class Person {
    @Id
    private String id; // المفتاح Redis سيكون "Person:<id>"
    private String firstName;
    private String lastName;

    // المبدئات والمحددات والمحددات (كما أعلاه)
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
        System.out.println("حفظ شخص مع ID: " + person.getId());
    }

    public void findPerson(String id) {
        Person person = repository.findById(id).orElse(null);
        if (person != null) {
            System.out.println(person.getFirstName() + " " + person.getLastName());
        }
    }
}
```

- `@RedisHash` يربط الكيان إلى هاش Redis.
- المستودع يوفر عمليات CRUD من دون أي تهيئة.

### 6. **تشغيل تطبيقك**
تأكد من تشغيل Redis محليًا (مثلًا عبر Docker: `docker run -d -p 6379:6379 redis`) أو اتصل إلى مثيل عن بُعد. ثم ابدأ تطبيق Spring Boot الخاص بك:

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
- **TTL (وقت الحياة):** قم بتعيين انتهاء صلاحية المفاتيح مع `redisTemplate.expire(key, 10, TimeUnit.MINUTES)`.
- **الهاشات:** استخدم `opsForHash()` للعمل مع الهاشات مباشرة.
- **النشر/الاستماع:** استخدم `RedisMessageListenerContainer` للرسائل.

### مثال على سير العمل
1. احفظ كائن `Person` مع `repository.save()` أو `redisTemplate.opsForValue().set()`.
2. استرجعها مع `repository.findById()` أو `redisTemplate.opsForValue().get()`.
3. تحقق من مثيل Redis الخاص بك (مثلًا مع `redis-cli`) لرؤية البيانات.

هذا يغطي الأساسيات! إذا كنت تريد استكشاف التخزين المؤقت، النشر/الاستماع، أو شيء محدد، أخبرني ما الذي تحاول تحقيقه، وسأغوص أكثر. كيف يتوافق هذا مع ما تحاول تحقيقه؟