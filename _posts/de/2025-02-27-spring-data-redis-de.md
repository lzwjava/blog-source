---
audio: false
generated: true
lang: de
layout: post
title: Spring Data Redis
translated: true
type: note
---

Spring Data Redis ist ein fantastisches Tool, um Redis – einen hochleistungsfähigen, speicherinternen Datenspeicher – in Ihre Spring-Anwendung zu integrieren. Es vereinfacht die Arbeit mit Redis, indem es eine vertraute Repository-ähnliche Schnittstelle und Abstraktionen über Low-Level-Redis-Operationen bereitstellt. Lassen Sie uns Schritt für Schritt durchgehen, wie Sie es einrichten und verwenden.

### 1. **Richten Sie Ihr Projekt ein**
Fügen Sie zunächst die Spring Data Redis-Abhängigkeit zu Ihrem Projekt hinzu. Wenn Sie Maven verwenden, fügen Sie dies Ihrer `pom.xml` hinzu:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

Für Gradle verwenden Sie:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
```

Dies schließt den Redis-Client ein (Jedis oder Lettuce – Lettuce ist die Standardeinstellung). Wenn Sie Jedis bevorzugen, können Sie es explizit hinzufügen und Lettuce ausschließen:

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

### 2. **Konfigurieren Sie Redis**
Konfigurieren Sie Ihre Redis-Verbindung in `application.properties` oder `application.yml`. Für eine lokale Redis-Instanz, die auf dem Standardport (6379) läuft:

```properties
spring.redis.host=localhost
spring.redis.port=6379
spring.redis.password= # Optional, falls Ihr Redis-Server ein Passwort hat
spring.redis.database=0 # Standard-Datenbankindex
```

Wenn Sie einen entfernten Redis-Server oder einen Dienst wie AWS ElastiCache verwenden, aktualisieren Sie den Host und die Anmeldedaten entsprechend.

### 3. **Grundlegende Verwendung mit RedisTemplate**
Spring Data Redis stellt `RedisTemplate` für Low-Level-Operationen bereit. Sie können es in Ihren Service oder Ihre Komponente autowiren:

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

- `RedisTemplate` ist generisch: `<String, String>` bedeutet, dass Schlüssel und Werte Strings sind. Sie können andere Typen verwenden (z.B. `<String, Object>`).
- `opsForValue()` ist für einfache Schlüssel-Wert-Operationen. Andere Methoden umfassen `opsForList()`, `opsForSet()`, `opsForHash()`, etc. für verschiedene Redis-Datenstrukturen.

### 4. **Verwendung mit Objekten**
Um Java-Objekte zu speichern und abzurufen, konfigurieren Sie `RedisTemplate` mit Serializern. Spring Boot konfiguriert es automatisch, aber Sie können es bei Bedarf anpassen:

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

Jetzt können Sie Objekte speichern und abrufen:

```java
public class Person {
    private String firstName;
    private String lastName;

    // Standardkonstruktor (für Deserialisierung)
    public Person() {}

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // Getter und Setter
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

### 5. **Repository-Ansatz**
Für eine höhere Abstraktionsebene verwenden Sie Spring Data Redis Repositories. Definieren Sie eine Entität und ein Repository:

```java
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@RedisHash("Person") // Ordnet einer Redis-Hash-Struktur mit Präfix "Person" zu
public class Person {
    @Id
    private String id; // Redis-Schlüssel wird "Person:<id>" sein
    private String firstName;
    private String lastName;

    // Konstruktoren, Getter, Setter (wie oben)
}
```

```java
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, String> {
}
```

Verwenden Sie es wie folgt:

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

- `@RedisHash` ordnet die Entität einer Redis-Hash-Struktur zu.
- Das Repository bietet CRUD-Operationen sofort.

### 6. **Starten Sie Ihre Anwendung**
Stellen Sie sicher, dass Redis lokal läuft (z.B. via Docker: `docker run -d -p 6379:6379 redis`) oder verbinden Sie sich mit einer entfernten Instanz. Starten Sie dann Ihre Spring-Boot-App:

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

### 7. **Erweiterte Funktionen**
- **TTL (Time-to-Live):** Setzen Sie die Ablaufzeit für Schlüssel mit `redisTemplate.expire(key, 10, TimeUnit.MINUTES)`.
- **Hashes:** Verwenden Sie `opsForHash()`, um direkt mit Redis-Hashes zu arbeiten.
- **Pub/Sub:** Verwenden Sie `RedisMessageListenerContainer` für Messaging.

### Beispielhafter Workflow
1. Speichern Sie ein `Person`-Objekt mit `repository.save()` oder `redisTemplate.opsForValue().set()`.
2. Rufen Sie es mit `repository.findById()` oder `redisTemplate.opsForValue().get()` ab.
3. Überprüfen Sie Ihre Redis-Instanz (z.B. mit `redis-cli`), um die Daten zu sehen.

Das deckt die Grundlagen ab! Wenn Sie Caching, Pub/Sub oder etwas Spezifisches erkunden möchten, lassen Sie mich wissen, was Sie anstreben, und ich gehe tiefer darauf ein. Wie passt das zu dem, was Sie versuchen zu erreichen?