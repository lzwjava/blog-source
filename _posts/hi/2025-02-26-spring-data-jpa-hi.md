---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग डेटा जेपीए
translated: true
---

एक रिपॉजिटरी को एक डेटा स्रोत के रूप में एक स्प्रिंग बूट प्रोजेक्ट में उपयोग करने में आम तौर पर स्प्रिंग डेटा जेपीए (जावा पर्सिस्टेंस एपीआई) को डेटाबेस इंटरैक्शंस को प्रबंधित करने के लिए इंटिग्रेट करना शामिल होता है। यहां एक स्टेप-बाय-स्टेप गाइड है कि इसे कैसे सेट अप करें:

### 1. डिपेंडेंसेज़ जोड़ें
पहले, आपकी `pom.xml` फाइल में आवश्यक डिपेंडेंसेज़ जोड़ने होंगे अगर आप मैवेन का उपयोग कर रहे हैं। स्प्रिंग डेटा जेपीए के लिए, आपको निम्नलिखित चाहिए:

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

### 2. डेटाबेस को कॉन्फ़िगर करें
अपनी डेटाबेस सेटिंग्स को `application.properties` फाइल में कॉन्फ़िगर करें। उदाहरण के लिए, अगर आप एक एच2 इन-मेमोरी डेटाबेस का उपयोग कर रहे हैं:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.h2.console.enabled=true
```

### 3. एक एंटिटी बनाएं
एक एंटिटी क्लास को डिफाइन करें जो एक डेटाबेस टेबल से मैप होता है। जेपीए एनोटेशन का उपयोग करके मैपिंग को स्पेसिफाई करें:

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

### 4. एक रिपॉजिटरी इंटरफेस बनाएं
एक रिपॉजिटरी इंटरफेस बनाएं जो `JpaRepository` को एक्सटेंड करता है। यह इंटरफेस `User` एंटिटी के लिए सीआरयूडी ऑपरेशंस प्रदान करेगा:

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
    // Custom query methods can be defined here
}
```

### 5. रिपॉजिटरी को एक सर्विस में उपयोग करें
रिपॉजिटरी को एक सर्विस क्लास में इंजेक्ट करें ताकि डेटाबेस ऑपरेशंस को कर सकें:

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

### 6. एक कंट्रोलर बनाएं
एक रेस्ट कंट्रोलर बनाएं ताकि `User` एंटिटी के साथ इंटरैक्ट करने के लिए एंडपॉइंट्स को एक्सपोज करें:

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

### 7. एप्लिकेशन को चलाएं
अपनी स्प्रिंग बूट एप्लिकेशन को चलाएं। अब आप `User` एंटिटी पर सीआरयूडी ऑपरेशंस को रेस्ट एंडपॉइंट्स का उपयोग करके कर सकते हैं।

यह सेटअप एक स्प्रिंग बूट प्रोजेक्ट में एक रिपॉजिटरी को एक डेटा स्रोत के रूप में उपयोग करने के लिए एक बेसिक स्ट्रक्चर प्रदान करता है। आप इसे आगे बढ़ा सकते हैं कस्टम क्वेरीज, एक्सेप्शंस को हैंडल करने और अधिक जटिल बिजनेस लॉजिक को इम्प्लीमेंट करने के द्वारा।