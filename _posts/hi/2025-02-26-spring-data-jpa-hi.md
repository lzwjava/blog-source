---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग डेटा जेपीए
translated: true
type: note
---

Spring Boot प्रोजेक्ट में रिपॉजिटरी को डेटा स्रोत के रूप में उपयोग करने के लिए आमतौर पर डेटाबेस इंटरैक्शन को प्रबंधित करने हेतु Spring Data JPA (Java Persistence API) को एकीकृत किया जाता है। यहां बताया गया है कि इसे कैसे सेट अप करें:

### 1. डिपेंडेंसी जोड़ें
सबसे पहले, यदि आप Maven का उपयोग कर रहे हैं, तो आपको अपनी `pom.xml` फ़ाइल में आवश्यक डिपेंडेंसी जोड़नी होंगी। Spring Data JPA के लिए, आपको निम्नलिखित की आवश्यकता होगी:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

### 2. डेटाबेस कॉन्फ़िगर करें
`application.properties` फ़ाइल में अपनी डेटाबेस सेटिंग्स कॉन्फ़िगर करें। उदाहरण के लिए, यदि आप H2 इन-मेमोरी डेटाबेस का उपयोग कर रहे हैं:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.h2.console.enabled=true
```

### 3. एक एंटिटी बनाएँ
एक एंटिटी क्लास को परिभाषित करें जो एक डेटाबेस टेबल से मैप होती है। मैपिंग निर्दिष्ट करने के लिए JPA एनोटेशन का उपयोग करें:

```java
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String email;

    // Getters and setters
}
```

### 4. एक रिपॉजिटरी इंटरफेस बनाएँ
एक रिपॉजिटरी इंटरफेस बनाएँ जो `JpaRepository` को एक्सटेंड करता हो। यह इंटरफेस `User` एंटिटी के लिए CRUD ऑपरेशन प्रदान करेगा:

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
    // कस्टम क्वेरी मेथड्स यहाँ परिभाषित किए जा सकते हैं
}
```

### 5. सर्विस में रिपॉजिटरी का उपयोग करें
डेटाबेस ऑपरेशन करने के लिए रिपॉजिटरी को एक सर्विस क्लास में इंजेक्ट करें:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;

    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    public User getUserById(Long id) {
        return userRepository.findById(id).orElse(null);
    }

    public User saveUser(User user) {
        return userRepository.save(user);
    }

    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
}
```

### 6. एक कंट्रोलर बनाएँ
`User` एंटिटी के साथ इंटरैक्ट करने के लिए एंडपॉइंट्स एक्सपोज़ करने हेतु एक REST कंट्रोलर बनाएँ:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
public class UserController {
    @Autowired
    private UserService userService;

    @GetMapping
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }

    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        return userService.getUserById(id);
    }

    @PostMapping
    public User createUser(@RequestBody User user) {
        return userService.saveUser(user);
    }

    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
    }
}
```

### 7. एप्लिकेशन रन करें
अपना Spring Boot एप्लिकेशन रन करें। अब आप REST एंडपॉइंट्स का उपयोग करके `User` एंटिटी पर CRUD ऑपरेशन करने में सक्षम होने चाहिए।

यह सेटअप एक Spring Boot प्रोजेक्ट में डेटा स्रोत के रूप में रिपॉजिटरी का उपयोग करने के लिए एक बुनियादी संरचना प्रदान करता है। आप इसे कस्टम क्वेरीज़ जोड़कर, एक्सेप्शन हैंडलिंग करके, और अधिक जटिल बिजनेस लॉजिक लागू करके आगे बढ़ा सकते हैं।