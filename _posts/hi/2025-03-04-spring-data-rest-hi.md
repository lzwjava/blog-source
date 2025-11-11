---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग डेटा रेस्ट मॉड्यूल
translated: true
type: note
---

**spring-data-rest-core** का उपयोग करने के लिए, आप Spring Data REST मॉड्यूल का लाभ उठा सकते हैं ताकि आपके Spring Data repositories को आपके एप्लिकेशन में RESTful endpoints के रूप में एक्सपोज़ किया जा सके। आरंभ करने के लिए नीचे एक संपूर्ण, चरण-दर-चरण मार्गदर्शिका दी गई है:

---

### 1. Spring Data REST डिपेंडेंसी जोड़ें
Spring Data REST का उपयोग करने के लिए, आपको अपने प्रोजेक्ट में इसकी डिपेंडेंसी शामिल करनी होगी। यदि आप **Spring Boot** का उपयोग कर रहे हैं (एक सामान्य परिदृश्य), तो अपनी बिल्ड फ़ाइल में निम्नलिखित डिपेंडेंसी जोड़ें:

- **Maven**:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-data-rest</artifactId>
  </dependency>
  ```

- **Gradle**:
  ```gradle
  implementation 'org.springframework.boot:spring-boot-starter-data-rest'
  ```

यह स्टार्टर `spring-data-rest-core` को अन्य आवश्यक घटकों के साथ लाता है। गैर- Spring Boot प्रोजेक्ट्स के लिए, आप सीधे `spring-data-rest-core` शामिल कर सकते हैं, लेकिन सरलता के लिए Spring Boot स्टार्टर की सिफारिश की जाती है।

---

### 2. अपनी Entities को परिभाषित करें
JPA (Java Persistence API) जैसी पर्सिस्टेंस टेक्नोलॉजी का उपयोग करके एंटिटी क्लासेज़ को परिभाषित करके अपना डोमेन मॉडल बनाएं। उदाहरण के लिए:

```java
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.GeneratedValue;

@Entity
public class User {
    @Id
    @GeneratedValue
    private Long id;
    private String name;

    // Constructors
    public User() {}
    public User(String name) {
        this.name = name;
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

यह `User` एंटिटी आपकी डेटाबेस में एक `id` और `name` के साथ एक सरल टेबल का प्रतिनिधित्व करती है।

---

### 3. Repository Interfaces बनाएं
Spring Data के repository interfaces में से किसी एक को extend करके, जैसे `JpaRepository`, अपनी एंटिटी के लिए एक repository interface को परिभाषित करें। उदाहरण के लिए:

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
```

`JpaRepository` को extend करके, आपको बुनियादी CRUD (Create, Read, Update, Delete) ऑपरेशन मुफ्त में मिल जाते हैं। Spring Data REST स्वचालित रूप से इस repository को एक RESTful endpoint के रूप में एक्सपोज़ कर देगा।

---

### 4. अपना एप्लिकेशन रन करें
डिपेंडेंसी जोड़ने और आपकी entities और repositories को परिभाषित करने के बाद, अपना Spring Boot एप्लिकेशन शुरू करें। Spring Data REST आपके repository के आधार पर स्वचालित रूप से REST endpoints जनरेट कर देगा। ऊपर दिए गए `UserRepository` के लिए, आप एक्सेस कर सकते हैं:

- **GET /users**: सभी users की सूची प्राप्त करें।
- **GET /users/{id}**: ID द्वारा एक विशिष्ट user प्राप्त करें।
- **POST /users**: एक नया user बनाएं (एक JSON पेलोड के साथ, उदा. `{"name": "Alice"}`)।
- **PUT /users/{id}**: एक मौजूदा user को अपडेट करें।
- **DELETE /users/{id}**: एक user को हटाएं।

उदाहरण के लिए, यदि आपका एप्लिकेशन `localhost:8080` पर चलता है, तो आप परीक्षण करने के लिए `curl` या ब्राउज़र जैसे टूल का उपयोग कर सकते हैं:

```bash
curl http://localhost:8080/users
```

प्रतिक्रिया में HATEOAS लिंक शामिल होंगे, जो क्लाइंट्स को संबंधित संसाधनों में गतिशील रूप से नेविगेट करने की अनुमति देते हैं।

---

### 5. (वैकल्पिक) REST Endpoints को कस्टमाइज़ करें
आप एनोटेशन या कॉन्फ़िगरेशन का उपयोग करके कस्टमाइज़ कर सकते हैं कि आपके repositories कैसे एक्सपोज़ होते हैं:

- **Endpoint Path बदलें**:
  एक कस्टम पथ निर्दिष्ट करने के लिए `@RepositoryRestResource` एनोटेशन का उपयोग करें:
  ```java
  import org.springframework.data.rest.core.annotation.RepositoryRestResource;

  @RepositoryRestResource(path = "people")
  public interface UserRepository extends JpaRepository<User, Long> {
  }
  ```
  अब, endpoint `/users` के बजाय `/people` होगा।

- **ग्लोबल सेटिंग्स कॉन्फ़िगर करें**:
  `RepositoryRestConfigurer` को इम्प्लीमेंट करके बेस पथ या अन्य सेटिंग्स को कस्टमाइज़ करें:
  ```java
  import org.springframework.data.rest.webmvc.config.RepositoryRestConfigurer;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.data.rest.core.config.RepositoryRestConfiguration;

  @Configuration
  public class RestConfig implements RepositoryRestConfigurer {
      @Override
      public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config) {
          config.setBasePath("/api"); // सभी endpoints /api से शुरू होंगे
      }
  }
  ```
  इसके साथ, आपके users `/api/users` पर एक्सेसिबल होंगे।

---

### Spring Data REST की मुख्य विशेषताएं
- **HATEOAS सपोर्ट**: प्रतिक्रियाओं में संबंधित संसाधनों के हाइपरमीडिया लिंक शामिल होते हैं।
- **पेजिनेशन और सॉर्टिंग**: परिणामों को पेजिनेट और सॉर्ट करने के लिए `?page=0&size=10&sort=name,asc` जैसे क्वेरी पैरामीटर का उपयोग करें।
- **फ़िल्टरिंग**: अतिरिक्त endpoints को एक्सपोज़ करने के लिए अपने repository में कस्टम क्वेरी मेथड्स जोड़ें (उदा. `findByName(String name)`)।

---

### सारांश
`spring-data-rest-core` का उपयोग करने के लिए:
1. Spring Data REST डिपेंडेंसी शामिल करें (उदा. Spring Boot के लिए `spring-boot-starter-data-rest`)।
2. उपयुक्त एनोटेशन (उदा. JPA के लिए `@Entity`) के साथ अपनी entities को परिभाषित करें।
3. Spring Data interfaces (उदा. `JpaRepository`) को extend करते हुए repository interfaces बनाएं।
4. स्वचालित रूप से जनरेट किए गए REST endpoints तक पहुंचने के लिए अपना एप्लिकेशन रन करें।
5. वैकल्पिक रूप से, endpoint paths या व्यवहार को आवश्यकतानुसार कस्टमाइज़ करें।

यह दृष्टिकोण आपको न्यूनतम कोड के साथ तेजी से एक RESTful API बनाने की अनुमति देता है, जो Spring Data REST की core functionality का लाभ उठाता है।