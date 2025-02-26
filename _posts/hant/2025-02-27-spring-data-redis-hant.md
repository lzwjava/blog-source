---
audio: false
lang: hant
layout: post
title: Spring Data Redis
translated: true
---

Spring Data Redis 是一個非常棒的工具，用於將 Redis—a high-performance, in-memory data store—整合到您的 Spring 應用程式中。它通過提供熟悉的儲存庫風格介面和對低級 Redis 操作的抽象來簡化與 Redis 的工作。讓我們逐步了解如何設置和使用它。

### 1. **設置您的項目**
首先，在項目中包含 Spring Data Redis 依賴。如果您使用 Maven，請將以下內容添加到您的 `pom.xml`：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

對於 Gradle，使用：

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
```

這包括 Redis 客戶端（Jedis 或 Lettuce—Lettuce 是預設）。如果您更喜歡 Jedis，可以明確添加它並排除 Lettuce：

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

### 2. **配置 Redis**
在 `application.properties` 或 `application.yml` 中配置您的 Redis 連接。對於在默認端口（6379）運行的本地 Redis 實例：

```properties
spring.redis.host=localhost
spring.redis.port=6379
spring.redis.password= # 可選，如果您的 Redis 伺服器有密碼
spring.redis.database=0 # 默認數據庫索引
```

如果您使用遠程 Redis 伺服器或類似 AWS ElastiCache 的服務，請相應更新主機和憑證。

### 3. **使用 RedisTemplate 基本操作**
Spring Data Redis 提供 `RedisTemplate` 進行低級操作。您可以將其自動連接到您的服務或組件中：

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

- `RedisTemplate` 是泛型的：`<String, String>` 意味著鍵和值是字符串。您可以使用其他類型（例如 `<String, Object>`）。
- `opsForValue()` 用於簡單的鍵值操作。其他方法包括 `opsForList()`、`opsForSet()`、`opsForHash()` 等，用於不同的 Redis 數據結構。

### 4. **使用對象**
要存儲和檢索 Java 對象，請配置 `RedisTemplate` 使用序列化器。Spring Boot 會自動配置它，但如果需要可以自定義：

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

現在您可以存儲和檢索對象：

```java
public class Person {
    private String firstName;
    private String lastName;

    // 默認構造函數（用於反序列化）
    public Person() {}

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // Getters 和 Setters
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

### 5. **儲存庫方法**
對於更高級別的抽象，使用 Spring Data Redis 儲存庫。定義一個實體和一個儲存庫：

```java
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@RedisHash("Person") // 映射到具有前綴 "Person" 的 Redis 哈希
public class Person {
    @Id
    private String id; // Redis 鍵將是 "Person:<id>"
    private String firstName;
    private String lastName;

    // 构造函數、Getters 和 Setters（如上）
}
```

```java
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, String> {
}
```

使用方法如下：

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

- `@RedisHash` 將實體映射到 Redis 哈希。
- 儲存庫提供了 CRUD 操作。

### 6. **運行您的應用程式**
確保 Redis 本地運行（例如，通過 Docker：`docker run -d -p 6379:6379 redis`）或連接到遠程實例。然後啟動您的 Spring Boot 應用程式：

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

### 7. **高級功能**
- **TTL（生存時間）**：使用 `redisTemplate.expire(key, 10, TimeUnit.MINUTES)` 為鍵設置過期時間。
- **哈希**：使用 `opsForHash()` 直接與 Redis 哈希一起工作。
- **Pub/Sub**：使用 `RedisMessageListenerContainer` 進行消息傳遞。

### 範例工作流程
1. 使用 `repository.save()` 或 `redisTemplate.opsForValue().set()` 保存 `Person` 對象。
2. 使用 `repository.findById()` 或 `redisTemplate.opsForValue().get()` 檢索它。
3. 檢查您的 Redis 實例（例如，使用 `redis-cli`）以查看數據。

這涵蓋了基本知識！如果您想探索快取、pub/sub 或其他特定內容，請告訴我您的目標，我將深入探討。這與您正在嘗試的內容如何相符？