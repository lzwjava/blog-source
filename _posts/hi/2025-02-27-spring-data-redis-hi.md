---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग डेटा रेडिस
translated: true
type: note
---

Spring Data Redis आपके Spring एप्लिकेशन में Redis—एक उच्च-प्रदर्शन, इन-मेमोरी डेटा स्टोर—को एकीकृत करने के लिए एक शानदार टूल है। यह Redis के साथ काम करने को एक परिचित रिपॉजिटरी-स्टाइल इंटरफेस और लो-लेवल Redis ऑपरेशन्स पर एब्स्ट्रैक्शन प्रदान करके सरल बनाता है। आइए चरण-दर-चरण देखते हैं कि इसे कैसे सेट अप करें और उपयोग करें।

### 1. **अपना प्रोजेक्ट सेट अप करें**
सबसे पहले, अपने प्रोजेक्ट में Spring Data Redis डिपेंडेंसी शामिल करें। यदि आप Maven का उपयोग कर रहे हैं, तो इसे अपने `pom.xml` में जोड़ें:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

Gradle के लिए, उपयोग करें:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
```

इसमें Redis क्लाइंट (Jedis या Lettuce—Lettuce डिफ़ॉल्ट है) शामिल होता है। यदि आप Jedis पसंद करते हैं, तो आप इसे स्पष्ट रूप से जोड़ सकते हैं और Lettuce को बाहर कर सकते हैं:

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

### 2. **Redis कॉन्फ़िगर करें**
`application.properties` या `application.yml` में अपना Redis कनेक्शन कॉन्फ़िगर करें। डिफ़ॉल्ट पोर्ट (6379) पर चल रहे एक स्थानीय Redis इंस्टेंस के लिए:

```properties
spring.redis.host=localhost
spring.redis.port=6379
spring.redis.password= # वैकल्पिक, यदि आपके Redis सर्वर का पासवर्ड है
spring.redis.database=0 # डिफ़ॉल्ट डेटाबेस इंडेक्स
```

यदि आप किसी रिमोट Redis सर्वर या AWS ElastiCache जैसी सेवा का उपयोग कर रहे हैं, तो होस्ट और क्रेडेंशियल्स को तदनुसार अपडेट करें।

### 3. **RedisTemplate के साथ बेसिक उपयोग**
Spring Data Redis लो-लेवल ऑपरेशन्स के लिए `RedisTemplate` प्रदान करता है। आप इसे अपने सर्विस या कंपोनेंट में ऑटोवायर कर सकते हैं:

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

- `RedisTemplate` जेनेरिक है: `<String, String>` का मतलब है कि keys और values स्ट्रिंग हैं। आप अन्य प्रकार (जैसे, `<String, Object>`) का उपयोग कर सकते हैं।
- `opsForValue()` साधारण key-value ऑपरेशन्स के लिए है। अन्य विधियों में विभिन्न Redis डेटा स्ट्रक्चर्स के लिए `opsForList()`, `opsForSet()`, `opsForHash()`, आदि शामिल हैं।

### 4. **ऑब्जेक्ट्स के साथ उपयोग**
Java ऑब्जेक्ट्स को स्टोर और रिट्रीव करने के लिए, `RedisTemplate` को सीरियलाइज़र्स के साथ कॉन्फ़िगर करें। Spring Boot इसे ऑटो-कॉन्फ़िगर करता है, लेकिन आवश्यकता पड़ने पर आप इसे कस्टमाइज़ कर सकते हैं:

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

अब आप ऑब्जेक्ट्स को स्टोर और रिट्रीव कर सकते हैं:

```java
public class Person {
    private String firstName;
    private String lastName;

    // डिफ़ॉल्ट कंस्ट्रक्टर (डी-सीरियलाइज़ेशन के लिए)
    public Person() {}

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // Getters और setters
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

### 5. **रिपॉजिटरी एप्रोच**
एक उच्च-स्तरीय एब्स्ट्रैक्शन के लिए, Spring Data Redis रिपॉजिटरीज़ का उपयोग करें। एक एंटिटी और एक रिपॉजिटरी को परिभाषित करें:

```java
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

@RedisHash("Person") // "Person" उपसर्ग के साथ एक Redis हैश पर मैप करता है
public class Person {
    @Id
    private String id; // Redis key "Person:<id>" होगी
    private String firstName;
    private String lastName;

    // कंस्ट्रक्टर्स, getters, setters (ऊपर के अनुसार)
}
```

```java
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, String> {
}
```

इसका उपयोग इस प्रकार करें:

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

- `@RedisHash` एंटिटी को एक Redis हैश पर मैप करता है।
- रिपॉजिटरी बॉक्स के बाहर ही CRUD ऑपरेशन्स प्रदान करती है।

### 6. **अपना एप्लिकेशन रन करें**
सुनिश्चित करें कि Redis स्थानीय रूप से चल रहा है (उदाहरण के लिए, Docker के माध्यम से: `docker run -d -p 6379:6379 redis`) या किसी रिमोट इंस्टेंस से कनेक्ट करें। फिर अपना Spring Boot ऐप स्टार्ट करें:

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

### 7. **एडवांस्ड फीचर्स**
- **TTL (Time-to-Live):** `redisTemplate.expire(key, 10, TimeUnit.MINUTES)` के साथ keys पर एक्सपायरेशन सेट करें।
- **Hashes:** Redis hashes के साथ सीधे काम करने के लिए `opsForHash()` का उपयोग करें।
- **Pub/Sub:** मैसेजिंग के लिए `RedisMessageListenerContainer` का उपयोग करें।

### उदाहरण वर्कफ़्लो
1. `repository.save()` या `redisTemplate.opsForValue().set()` के साथ एक `Person` ऑब्जेक्ट सेव करें।
2. `repository.findById()` या `redisTemplate.opsForValue().get()` के साथ इसे रिट्रीव करें।
3. डेटा देखने के लिए अपने Redis इंस्टेंस (उदाहरण के लिए, `redis-cli` के साथ) की जाँच करें।

यह मूल बातें कवर करता है! यदि आप कैशिंग, pub/sub, या कुछ विशिष्ट का पता लगाना चाहते हैं, तो मुझे बताएं कि आप क्या करना चाह रहे हैं, और मैं गहराई से बताऊंगा। यह आपके इरादों के साथ कैसे फिट बैठता है?