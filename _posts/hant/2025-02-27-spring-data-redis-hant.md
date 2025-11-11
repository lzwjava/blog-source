---
audio: false
generated: true
lang: hant
layout: post
title: Spring Data Redis
translated: true
type: note
---

Spring Data Redis 是一個極佳的工具，能將 Redis——一個高效能的記憶體資料儲存系統——整合到您的 Spring 應用程式中。它透過提供熟悉的儲存庫風格介面以及對底層 Redis 操作進行抽象化，簡化了與 Redis 的互動。讓我們逐步了解如何設定和使用它。

### 1. **設定您的專案**
首先，在您的專案中包含 Spring Data Redis 的依賴項。如果您使用 Maven，請將以下內容新增至您的 `pom.xml`：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

若使用 Gradle，請使用：

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
```

這包含了 Redis 客戶端（Jedis 或 Lettuce——Lettuce 是預設選項）。如果您偏好 Jedis，可以明確新增並排除 Lettuce：

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

### 2. **設定 Redis**
在 `application.properties` 或 `application.yml` 中設定您的 Redis 連線。對於在本機執行於預設連接埠 (6379) 的 Redis 實例：

```properties
spring.redis.host=localhost
spring.redis.port=6379
spring.redis.password= # 可選，如果您的 Redis 伺服器設有密碼
spring.redis.database=0 # 預設資料庫索引
```

如果您使用遠端 Redis 伺服器或如 AWS ElastiCache 等服務，請相應地更新主機和憑證。

### 3. **使用 RedisTemplate 進行基本操作**
Spring Data Redis 提供 `RedisTemplate` 用於底層操作。您可以將其自動裝配到您的服務或元件中：

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

- `RedisTemplate` 是泛型的：`<String, String>` 表示鍵和值均為字串。您可以使用其他型別（例如 `<String, Object>`）。
- `opsForValue()` 用於簡單的鍵值操作。其他方法包括 `opsForList()`、`opsForSet()`、`opsForHash()` 等，用於不同的 Redis 資料結構。

### 4. **與物件一起使用**
要儲存和檢索 Java 物件，請使用序列化器設定 `RedisTemplate`。Spring Boot 會自動設定，但您可以根據需要進行自訂：

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

現在您可以儲存和檢索物件：

```java
public class Person {
    private String firstName;
    private String lastName;

    // 預設建構函式（用於反序列化）
    public Person() {}

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // Getter 和 Setter 方法
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
為了更高層次的抽象，使用 Spring Data Redis 儲存庫。定義一個實體和一個儲存庫：

```java
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@RedisHash("Person") // 對映到前綴為 "Person" 的 Redis 雜湊
public class Person {
    @Id
    private String id; // Redis 鍵將為 "Person:<id>"
    private String firstName;
    private String lastName;

    // 建構函式、getter、setter（同上）
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

- `@RedisHash` 將實體對映到 Redis 雜湊。
- 儲存庫提供開箱即用的 CRUD 操作。

### 6. **執行您的應用程式**
確保 Redis 在本機執行（例如透過 Docker：`docker run -d -p 6379:6379 redis`）或連線到遠端實例。然後啟動您的 Spring Boot 應用程式：

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

### 7. **進階功能**
- **TTL（存活時間）：** 使用 `redisTemplate.expire(key, 10, TimeUnit.MINUTES)` 設定鍵的過期時間。
- **雜湊：** 使用 `opsForHash()` 直接操作 Redis 雜湊。
- **發佈/訂閱：** 使用 `RedisMessageListenerContainer` 進行訊息傳遞。

### 範例工作流程
1. 使用 `repository.save()` 或 `redisTemplate.opsForValue().set()` 儲存 `Person` 物件。
2. 使用 `repository.findById()` 或 `redisTemplate.opsForValue().get()` 檢索它。
3. 檢查您的 Redis 實例（例如使用 `redis-cli`）以查看資料。

這涵蓋了基本知識！如果您想探索快取、發佈/訂閱或特定功能，請告訴我您的目標，我將深入探討。這與您正在嘗試實現的目標如何契合？