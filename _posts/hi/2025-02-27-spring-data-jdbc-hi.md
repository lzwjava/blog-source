---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग डेटा जेडीबीसी
translated: true
type: note
---

Spring Data JDBC एक शक्तिशाली लाइब्रेरी है जो Spring एप्लिकेशन में डेटाबेस इंटरैक्शन को सरल बनाती है, जो रिलेशनल डेटाबेस के साथ काम करने के लिए एक हल्के, एनोटेशन-संचालित दृष्टिकोण प्रदान करती है। यह Spring Data JPA की तुलना में कम राय-आधारित है और ऑब्जेक्ट्स को डेटाबेस टेबल्स में मैप करने के एक सरल, अधिक स्पष्ट तरीके पर केंद्रित है। नीचे, मैं आपको इसके उपयोग की मूल बातें समझाऊंगा।

### 1. **अपना प्रोजेक्ट सेट अप करें**
आरंभ करने के लिए, आपको अपने प्रोजेक्ट में Spring Data JDBC शामिल करना होगा। यदि आप Maven का उपयोग कर रहे हैं, तो अपनी `pom.xml` में निम्नलिखित डिपेंडेंसी जोड़ें:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jdbc</artifactId>
</dependency>
```

आपको अपने डेटाबेस (जैसे, H2, MySQL, PostgreSQL) के लिए एक JDBC ड्राइवर की भी आवश्यकता होगी। उदाहरण के लिए, H2 के लिए:

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

यदि आप Gradle का उपयोग कर रहे हैं, तो समकक्ष होंगे:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-jdbc'
runtimeOnly 'com.h2database:h2'
```

### 2. **अपना डेटाबेस कॉन्फ़िगर करें**
अपने `application.properties` या `application.yml` में, डेटाबेस कनेक्शन कॉन्फ़िगर करें। एक H2 इन-मेमोरी डेटाबेस के लिए, यह इस तरह दिख सकता है:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.h2.console.enabled=true
```

PostgreSQL जैसे वास्तविक डेटाबेस के लिए, URL, यूजरनेम और पासवर्ड को तदनुसार समायोजित करें।

### 3. **अपना डोमेन मॉडल परिभाषित करें**
अपने डेटाबेस में एक टेबल का प्रतिनिधित्व करने के लिए एक सरल एंटिटी क्लास बनाएं। Spring Data JDBC कन्वेंशन का उपयोग करता है जहां क्लास का नाम टेबल नाम (डिफ़ॉल्ट रूप से लोअरकेस) से मैप होता है, और फ़ील्ड्स कॉलम से मैप होते हैं।

```java
import org.springframework.data.annotation.Id;

public class Person {
    @Id
    private Long id;
    private String firstName;
    private String lastName;

    // डिफ़ॉल्ट कंस्ट्रक्टर (Spring Data JDBC द्वारा आवश्यक)
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

- `@Id` प्राइमरी की को चिह्नित करता है।
- Spring Data JDBC को नो-आर्ग्स कंस्ट्रक्टर की अपेक्षा होती है।
- जब तक ओवरराइड न किया जाए, टेबल का नाम `person` होगा।

### 4. **एक रिपॉजिटरी बनाएं**
बेसिक CRUD ऑपरेशन को हैंडल करने के लिए एक इंटरफेस परिभाषित करें जो `CrudRepository` का विस्तार करता हो:

```java
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, Long> {
}
```

बस हो गया! आपको इसे इम्प्लीमेंट करने की आवश्यकता नहीं है—Spring Data JDBC रनटाइम पर इम्प्लीमेंटेशन जेनरेट करता है।

### 5. **रिपॉजिटरी का उपयोग करें**
रिपॉजिटरी को एक सर्विस या कंट्रोलर में इंजेक्ट करें और इसका उपयोग करें:

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

### 6. **अपना एप्लिकेशन रन करें**
यदि आप Spring Boot का उपयोग कर रहे हैं, तो `@SpringBootApplication` के साथ एक मेन क्लास बनाएं और इसे रन करें:

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

Spring Boot डेटासोर्स और Spring Data JDBC को ऑटो-कॉन्फ़िगर कर देगा।

### 7. **वैकल्पिक: कस्टम क्वेरीज़**
यदि आपको कस्टम क्वेरीज़ की आवश्यकता है, तो आप `@Query` के साथ अपनी रिपॉजिटरी में मेथड्स जोड़ सकते हैं:

```java
import org.springframework.data.jdbc.repository.query.Query;
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, Long> {
    @Query("SELECT * FROM person WHERE first_name = :name")
    List<Person> findByFirstName(String name);
}
```

### याद रखने योग्य मुख्य बिंदु
- **कोई Lazy Loading नहीं:** JPA के विपरीत, Spring Data JDBC लेज़ी लोडिंग का समर्थन नहीं करता है। रिलेशनशिप (जैसे, one-to-many) को एग्रीगेट रूट्स के साथ स्पष्ट मॉडलिंग की आवश्यकता होती है।
- **एग्रीगेट रूट:** प्रत्येक एंटिटी एक एग्रीगेट का हिस्सा होती है, और केवल रूट को सीधे सेव या रिट्रीव किया जाता है।
- **स्कीमा निर्माण:** Spring Data JDBC स्वचालित रूप से टेबल्स नहीं बनाता है। आपको स्कीमा प्रदान करना होगा (जैसे, `src/main/resources` में `schema.sql` के माध्यम से):

```sql
CREATE TABLE person (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);
```

### उदाहरण वर्कफ़्लो
1. अपना ऐप स्टार्ट करें।
2. `repository.save()` का उपयोग करके एक `Person` ऑब्जेक्ट सेव करें।
3. `repository.findById()` या `findAll()` के साथ इसे रिट्रीव करें।

ये थीं मूल बातें! यदि आप रिलेशनशिप, कस्टम मैपिंग, या किसी विशिष्ट चीज में गहराई से जाना चाहते हैं, तो मुझे बताएं कि आपका लक्ष्य क्या है, और मैं स्पष्टीकरण को अनुकूलित करूंगा। अब तक यह आपके लिए कैसा काम कर रहा है?