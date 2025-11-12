---
audio: false
generated: true
lang: ja
layout: post
title: Spring Data Redis
translated: true
type: note
---

Spring Data Redisは、Springアプリケーションに高性能なインメモリデータストアであるRedisを統合するための素晴らしいツールです。Redis操作を簡素化し、使い慣れたリポジトリスタイルのインターフェースと低レベルRedis操作の抽象化を提供します。セットアップ方法と使用方法をステップバイステップで見ていきましょう。

### 1. **プロジェクトのセットアップ**
まず、プロジェクトにSpring Data Redisの依存関係を含めます。Mavenを使用している場合は、`pom.xml`に以下を追加します：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

Gradleの場合は、以下を使用します：

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
```

これにはRedisクライアント（JedisまたはLettuce - デフォルトはLettuce）が含まれます。Jedisを優先する場合は、明示的に追加し、Lettuceを除外できます：

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
`application.properties`または`application.yml`でRedis接続を設定します。デフォルトポート（6379）で実行されているローカルRedisインスタンスの場合：

```properties
spring.redis.host=localhost
spring.redis.port=6379
spring.redis.password= # オプション、Redisサーバーにパスワードがある場合
spring.redis.database=0 # デフォルトのデータベースインデックス
```

リモートのRedisサーバーやAWS ElastiCacheなどのサービスを使用している場合は、ホストと認証情報を適宜更新してください。

### 3. **RedisTemplateを使用した基本的な使用方法**
Spring Data Redisは低レベル操作のために`RedisTemplate`を提供します。サービスやコンポーネントに自動注入できます：

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
- `opsForValue()`は単純なキー値操作用です。他のメソッドには、さまざまなRedisデータ構造用の`opsForList()`、`opsForSet()`、`opsForHash()`などがあります。

### 4. **オブジェクトでの使用**
Javaオブジェクトを保存および取得するには、シリアライザーを使用して`RedisTemplate`を設定します。Spring Bootは自動設定しますが、必要に応じてカスタマイズできます：

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

これでオブジェクトを保存および取得できます：

```java
public class Person {
    private String firstName;
    private String lastName;

    // デフォルトコンストラクタ（デシリアライゼーション用）
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
より高レベルの抽象化には、Spring Data Redisリポジトリを使用します。エンティティとリポジトリを定義します：

```java
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@RedisHash("Person") // プレフィックス「Person」のRedisハッシュにマッピング
public class Person {
    @Id
    private String id; // Redisキーは「Person:<id>」になります
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

以下のように使用します：

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
- リポジトリはすぐに使用できるCRUD操作を提供します。

### 6. **アプリケーションの実行**
Redisがローカルで実行されていることを確認します（例：Dockerを使用：`docker run -d -p 6379:6379 redis`）、またはリモートインスタンスに接続します。その後、Spring Bootアプリを起動します：

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
- **TTL（Time-to-Live）：** `redisTemplate.expire(key, 10, TimeUnit.MINUTES)`でキーの有効期限を設定します。
- **ハッシュ：** `opsForHash()`を使用してRedisハッシュを直接操作します。
- **Pub/Sub：** メッセージングに`RedisMessageListenerContainer`を使用します。

### ワークフローの例
1. `repository.save()`または`redisTemplate.opsForValue().set()`で`Person`オブジェクトを保存します。
2. `repository.findById()`または`redisTemplate.opsForValue().get()`で取得します。
3. Redisインスタンス（例：`redis-cli`を使用）をチェックしてデータを確認します。

これで基本を網羅しました！キャッシング、pub/sub、または特定の何かを探求したい場合は、あなたが目指していることを教えてください。さらに深く掘り下げます。これはあなたがやろうとしていることとどのように合致しますか？