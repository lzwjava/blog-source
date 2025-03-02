---
audio: false
generated: false
lang: hi
layout: post
title: Spring Data JDBC का उपयोग
translated: true
---

Spring Data JDBC एक शक्तिशाली लाइब्रेरी है जो एक Spring एप्लिकेशन में डेटाबेस इंटरैक्शंस को सरल बनाती है, एक लाइटवेट, एनोटेशन-ड्राइवन एप्रोच प्रदान करके रिलेशनल डेटाबेस के साथ काम करने के लिए। यह Spring Data JPA से कम ओपिनियनेटेड है और एक सरल, अधिक स्पष्ट तरीके से ऑब्जेक्ट्स को डेटाबेस टेबल्स में मैप करने पर ध्यान केंद्रित करता है। नीचे, मैं आपको इसके उपयोग के बेसिक्स के बारे में बताता हूँ।

### 1. **अपने प्रोजेक्ट को सेट अप करें**
शुरू करने के लिए, आपको अपने प्रोजेक्ट में Spring Data JDBC को शामिल करना होगा। अगर आप Maven का उपयोग कर रहे हैं, तो अपने `pom.xml` में निम्नलिखित डिपेंडेंसी जोड़ें:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jdbc</artifactId>
</dependency>
```

आपको अपने डेटाबेस के लिए एक JDBC ड्राइवर भी चाहिए (जैसे, H2, MySQL, PostgreSQL)। उदाहरण के लिए, H2 के लिए:

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

अगर आप Gradle का उपयोग कर रहे हैं, तो समकक्ष होंगे:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-jdbc'
runtimeOnly 'com.h2database:h2'
```

### 2. **अपने डेटाबेस को कॉन्फ़िगर करें**
अपने `application.properties` या `application.yml` में डेटाबेस कनेक्शन को कॉन्फ़िगर करें। एक H2 इन-मेमोरी डेटाबेस के लिए, यह इस तरह दिख सकता है:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.h2.console.enabled=true
```

एक वास्तविक डेटाबेस जैसे PostgreSQL के लिए, URL, यूजरनेम, और पासवर्ड को अनुकूलित करें।

### 3. **अपने डोमेन मॉडल को परिभाषित करें**
एक सरल एंटिटी क्लास बनाएं जो अपने डेटाबेस में एक टेबल को प्रतिनिधित्व करे। Spring Data JDBC में, क्लास नाम टेबल नाम (डिफ़ॉल्ट में लॉवर्केस) में मैप होता है, और फ़ील्ड्स कोलम्स में मैप होते हैं।

```java
import org.springframework.data.annotation.Id;

public class Person {
    @Id
    private Long id;
    private String firstName;
    private String lastName;

    // डिफ़ॉल्ट कन्स्ट्रक्टर (Spring Data JDBC द्वारा आवश्यक)
    public Person() {}

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // गेटर्स और सेटर्स
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getFirstName() { return firstName; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public String getLastName() { return lastName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
}
```

- `@Id` प्राथमिक की को चिह्नित करता है।
- Spring Data JDBC एक नो-आर्ग्स कन्स्ट्रक्टर की अपेक्षा करता है।
- टेबल का नाम `person` होगा, जब तक कि ओवरराइड नहीं किया गया।

### 4. **एक रिपोजिटरी बनाएं**
एक इंटरफ़ेस परिभाषित करें जो `CrudRepository` को एक्सटेंड करता है, ताकि बेसिक CRUD ऑपरेशंस को हैंडल किया जा सके:

```java
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, Long> {
}
```

बस यही है! आपको इसे इम्प्लीमेंट करने की जरूरत नहीं है—Spring Data JDBC इसे रनटाइम पर जनरेट करता है।

### 5. **रिपोजिटरी का उपयोग करें**
रिपोजिटरी को एक सेवा या कंट्रोलर में इंजेक्ट करें और इसका उपयोग करें:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

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

    public void listPeople() {
        Iterable<Person> people = repository.findAll();
        people.forEach(p -> System.out.println(p.getFirstName() + " " + p.getLastName()));
    }
}
```

### 6. **अपने एप्लिकेशन को चलाएं**
अगर आप Spring Boot का उपयोग कर रहे हैं, तो एक मुख्य क्लास बनाएं जिसमें `@SpringBootApplication` है और इसे चलाएं:

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

Spring Boot डेटासोर्स और Spring Data JDBC को ऑटो-कॉन्फ़िगर करेगा।

### 7. **वैकल्पिक: कस्टम क्वेरी**
अगर आपको कस्टम क्वेरी चाहिए, तो आप अपने रिपोजिटरी में `@Query` के साथ मेथड्स जोड़ सकते हैं:

```java
import org.springframework.data.jdbc.repository.query.Query;
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, Long> {
    @Query("SELECT * FROM person WHERE first_name = :name")
    List<Person> findByFirstName(String name);
}
```

### याद रखने के लिए मुख्य बिंदु
- **नो लेजी लोडिंग:** JPA के विपरीत, Spring Data JDBC लेजी लोडिंग का समर्थन नहीं करता है। संबंध (जैसे, एक-से-एक) को एक्सप्लिसिट मॉडलिंग के साथ एग्रीगेट रूट्स के साथ किया जाना चाहिए।
- **एग्रीगेट रूट:** प्रत्येक एंटिटी एक एग्रीगेट का हिस्सा है, और केवल रूट को सीधे सेभ या रिट्रीव किया जाता है।
- **स्कीमा क्रिएशन:** Spring Data JDBC टेबल को स्वचालित रूप से नहीं बनाता है। आपको स्कीमा प्रदान करना होगा (जैसे, `schema.sql` में `src/main/resources`):

```sql
CREATE TABLE person (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);
```

### उदाहरण वर्कफ्लो
1. अपने ऐप को शुरू करें।
2. `repository.save()` का उपयोग करके एक `Person` ऑब्जेक्ट को सेभ करें।
3. `repository.findById()` या `findAll()` के साथ इसे रिट्रीव करें।

यह बेसिक्स हैं! अगर आप संबंधों, कस्टम मैपिंग, या कुछ विशेष चीजों में गहरे जाना चाहते हैं, तो मुझे बताएं कि आप क्या लक्ष्य कर रहे हैं, और मैं व्याख्या को अनुकूलित करूँगा। यह आपको अभी तक कैसे लग रहा है?