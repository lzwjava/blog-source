---
audio: false
lang: ja
layout: post
title: Spring Data Redisの
translated: true
---

Spring Data Redisは、SpringアプリケーションにRedis—a高性能、インメモリデータストア—toを統合するための素晴らしいツールです。Redisとの作業を簡素化するために、低レベルのRedis操作に対する抽象化と、リポジトリスタイルのインターフェースを提供します。それでは、設定方法と使用方法をステップバイステップで説明します。

### 1. **プロジェクトの設定**
まず、プロジェクトにSpring Data Redisの依存関係を追加します。Mavenを使用している場合は、`pom.xml`に以下を追加します：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

Gradleを使用している場合は、以下を使用します：

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
```

これにより、Redisクライアント（JedisまたはLettuce—Lettuceがデフォルト）が含まれます。Jedisを明示的に追加し、Lettuceを排除する場合は、以下のようにします：

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

### 2. **Redisの設定**
`application.properties`または`application.yml`でRedis接続を設定します。ローカルのRedisインスタンスがデフォルトポート（6379）で実行されている場合：

```properties
spring.redis.host=localhost
spring.redis.port=6379
spring.redis.password= # パスワードが設定されている場合にのみ必要
spring.redis.database=0 # デフォルトのデータベースインデックス
```

リモートのRedisサーバーまたはAWS ElastiCacheなどのサービスを使用している場合は、ホストと認証情報を適宜更新してください。

### 3. **RedisTemplateを使用した基本的な使用方法**
Spring Data Redisは、`RedisTemplate`を低レベルの操作に提供します。サービスまたはコンポーネントに自動的に注入できます：

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

- `RedisTemplate`はジェネリックです：`<String, String>`はキーと値が文字列であることを意味します。他の型（例：`<String, Object>`）も使用できます。
- `opsForValue()`は、シンプルなキー値操作に使用されます。他のメソッドには、`opsForList()`、`opsForSet()`、`opsForHash()`など、異なるRedisデータ構造に対応するものがあります。

### 4. **オブジェクトの使用**
Javaオブジェクトを保存および取得するには、`RedisTemplate`をシリアライザで設定します。Spring Bootは自動的に設定しますが、必要に応じてカスタマイズできます：

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

これで、オブジェクトを保存および取得できます：

```java
public class Person {
    private String firstName;
    private String lastName;

    // デシリアライズ用のデフォルトコンストラクタ
    public Person() {}

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // ゲッターとセッター
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

### 5. **リポジトリアプローチ**
より高度な抽象化を使用するには、Spring Data Redisリポジトリを使用します。エンティティとリポジトリを定義します：

```java
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@RedisHash("Person") // プレフィックス "Person" のRedisハッシュにマッピング
public class Person {
    @Id
    private String id; // Redisキーは "Person:<id>" となります
    private String firstName;
    private String lastName;

    // コンストラクタ、ゲッター、セッター（上記と同じ）
}
```

```java
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, String> {
}
```

このように使用します：

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

- `@RedisHash`はエンティティをRedisハッシュにマッピングします。
- リポジトリは、CRUD操作を自動的に提供します。

### 6. **アプリケーションの実行**
Redisがローカルで実行されていることを確認します（例：Dockerを使用して `docker run -d -p 6379:6379 redis`）またはリモートインスタンスに接続します。次に、Spring Bootアプリケーションを起動します：

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

### 7. **高度な機能**
- **TTL（Time-to-Live）**：キーに有効期限を設定するには、`redisTemplate.expire(key, 10, TimeUnit.MINUTES)`を使用します。
- **ハッシュ**：`opsForHash()`を使用して、Redisハッシュを直接操作します。
- **Pub/Sub**：メッセージングには`RedisMessageListenerContainer`を使用します。

### 例のワークフロー
1. `repository.save()`または`redisTemplate.opsForValue().set()`を使用して`Person`オブジェクトを保存します。
2. `repository.findById()`または`redisTemplate.opsForValue().get()`を使用して取得します。
3. Redisインスタンス（例：`redis-cli`）を確認してデータを確認します。

これらが基本的な内容です！キャッシュ、pub/sub、または特定の機能について詳しく知りたい場合は、目的を教えてください。