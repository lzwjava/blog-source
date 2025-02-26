---
audio: true
lang: hi
layout: post
title: Spring Data Redis का उपयोग
translated: true
---

Spring Data Redis एक बहुत ही अच्छा औजार है जो Redis—a high-performance, in-memory data store—को अपने Spring application में integrate करने के लिए है। यह Redis के साथ काम करने को सरल बनाता है, एक familiar repository-style interface और low-level Redis operations पर abstractions प्रदान करते hue.

### 1. **Project Setup**
पहले, अपने project में Spring Data Redis dependency include करें। अगर आप Maven use कर रहे हैं, तो `pom.xml` में यह add करें:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

Gradle के लिए:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
```

यह Redis client (Jedis या Lettuce—Lettuce default है) include करता है। अगर आप Jedis prefer करते हैं, तो आप explicitly add कर सकते हैं और Lettuce exclude कर सकते हैं:

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

### 2. **Redis Configuration**
`application.properties` या `application.yml` में Redis connection configure करें। एक local Redis instance के लिए, default port (6379) पर:

```properties
spring.redis.host=localhost
spring.redis.port=6379
spring.redis.password= # Optional, अगर आपके Redis server पर password है
spring.redis.database=0 # Default database index
```

अगर आप remote Redis server या AWS ElastiCache जैसे service use कर रहे हैं, तो host और credentials update करें.

### 3. **Basic Usage with RedisTemplate**
Spring Data Redis `RedisTemplate` provide करता है low-level operations के लिए। आप isse autowire कर सकते हैं service या component में:

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

- `RedisTemplate` generic है: `<String, String>` means keys और values strings हैं। आप other types (e.g., `<String, Object>`) use कर सकते हैं।
- `opsForValue()` simple key-value operations के लिए है। अन्य methods include `opsForList()`, `opsForSet()`, `opsForHash()`, etc., different Redis data structures के लिए.

### 4. **Using with Objects**
Java objects को store और retrieve करने ke liye, `RedisTemplate` ko serializers ke sath configure करें। Spring Boot auto-configures it, but आप customize kar sakte hain agar zaroorat ho:

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

अब आप objects ko store aur retrieve kar sakte hain:

```java
public class Person {
    private String firstName;
    private String lastName;

    // Default constructor (for deserialization)
    public Person() {}

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // Getters and setters
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

### 5. **Repository Approach**
एक higher-level abstraction ke liye, Spring Data Redis repositories use karein। Define karein ek entity aur ek repository:

```java
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@RedisHash("Person") // Maps to a Redis hash with prefix "Person"
public class Person {
    @Id
    private String id; // Redis key will be "Person:<id>"
    private String firstName;
    private String lastName;

    // Constructors, getters, setters (as above)
}
```

```java
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, String> {
}
```

Isse use karein:

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

- `@RedisHash` entity ko ek Redis hash ke sath map karta hai.
- Repository CRUD operations out of the box provide karta hai.

### 6. **Run Your Application**
Ensure Redis locally running hai (e.g., via Docker: `docker run -d -p 6379:6379 redis`) ya connect karein ek remote instance ke sath. Phir start karein aapka Spring Boot app:

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

### 7. **Advanced Features**
- **TTL (Time-to-Live):** Keys par expiration set karein `redisTemplate.expire(key, 10, TimeUnit.MINUTES)` ke sath.
- **Hashes:** `opsForHash()` use karein Redis hashes ke sath directly kaam karne ke liye.
- **Pub/Sub:** `RedisMessageListenerContainer` use karein messaging ke liye.

### Example Workflow
1. `Person` object ko `repository.save()` ya `redisTemplate.opsForValue().set()` ke sath save karein.
2. Isse retrieve karein `repository.findById()` ya `redisTemplate.opsForValue().get()` ke sath.
3. Apne Redis instance ko check karein (e.g., `redis-cli` ke sath) data dekhne ke liye.

Yeh essentials cover karta hai! Agar aap caching, pub/sub, ya kuch specific explore karna chaahte hain, toh bataiye ki aap kya aim kar rahe hain, aur main deeper dive karta hoon. Yeh aapke sath kya fit hota hai?