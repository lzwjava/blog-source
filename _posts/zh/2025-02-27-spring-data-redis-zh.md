---
audio: true
generated: false
lang: zh
layout: post
title: Spring Data Redis
translated: true
---

Spring Data Redis 是一个将 Redis（高性能的内存数据存储）集成到 Spring 应用程序中的绝佳工具。它通过提供熟悉的仓库样式接口和对低级 Redis 操作的抽象来简化与 Redis 的工作。让我们逐步走一遍如何设置和使用它。

### 1. **设置项目**
首先，在项目中包含 Spring Data Redis 依赖。如果使用 Maven，将以下内容添加到 `pom.xml`：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

对于 Gradle，使用：

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
```

这包括 Redis 客户端（Jedis 或 Lettuce—Lettuce 是默认的）。如果你更喜欢 Jedis，可以明确添加它并排除 Lettuce：

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
在 `application.properties` 或 `application.yml` 中配置 Redis 连接。对于在默认端口（6379）运行的本地 Redis 实例：

```properties
spring.redis.host=localhost
spring.redis.port=6379
spring.redis.password= # 可选，如果你的 Redis 服务器有密码
spring.redis.database=0 # 默认数据库索引
```

如果使用远程 Redis 服务器或类似 AWS ElastiCache 的服务，请相应更新主机和凭据。

### 3. **使用 RedisTemplate 进行基本操作**
Spring Data Redis 提供 `RedisTemplate` 进行低级操作。可以将其自动注入到服务或组件中：

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

- `RedisTemplate` 是泛型的：`<String, String>` 表示键和值都是字符串。可以使用其他类型（例如 `<String, Object>`）。
- `opsForValue()` 用于简单的键值操作。其他方法包括 `opsForList()`、`opsForSet()`、`opsForHash()` 等，用于不同的 Redis 数据结构。

### 4. **使用对象**
要存储和检索 Java 对象，配置 `RedisTemplate` 使用序列化器。Spring Boot 会自动配置它，但如果需要可以自定义：

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

现在可以存储和检索对象：

```java
public class Person {
    private String firstName;
    private String lastName;

    // 默认构造函数（用于反序列化）
    public Person() {}

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // Getters 和 setters
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

### 5. **仓库方法**
对于更高级的抽象，使用 Spring Data Redis 仓库。定义一个实体和一个仓库：

```java
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@RedisHash("Person") // 映射到一个带有前缀 "Person" 的 Redis 哈希
public class Person {
    @Id
    private String id; // Redis 键将是 "Person:<id>"
    private String firstName;
    private String lastName;

    // 构造函数、getters 和 setters（如上）
}
```

```java
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, String> {
}
```

可以这样使用：

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

- `@RedisHash` 将实体映射到 Redis 哈希。
- 仓库提供了开箱即用的 CRUD 操作。

### 6. **运行应用程序**
确保 Redis 本地运行（例如，通过 Docker：`docker run -d -p 6379:6379 redis`）或连接到远程实例。然后启动 Spring Boot 应用：

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

### 7. **高级功能**
- **TTL（生存时间）**：使用 `redisTemplate.expire(key, 10, TimeUnit.MINUTES)` 为键设置过期时间。
- **哈希**：使用 `opsForHash()` 直接处理 Redis 哈希。
- **发布/订阅**：使用 `RedisMessageListenerContainer` 进行消息传递。

### 示例工作流
1. 使用 `repository.save()` 或 `redisTemplate.opsForValue().set()` 保存一个 `Person` 对象。
2. 使用 `repository.findById()` 或 `redisTemplate.opsForValue().get()` 检索它。
3. 检查 Redis 实例（例如，使用 `redis-cli`）查看数据。

这涵盖了基本内容！如果你想探索缓存、发布/订阅或其他特定内容，告诉我你的目标，我会深入探讨。这与你正在尝试的内容有什么关系？