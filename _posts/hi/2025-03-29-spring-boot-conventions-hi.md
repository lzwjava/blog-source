---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग बूट जावा कोडिंग कन्वेंशन्स
translated: true
type: note
---

## 1. मूल सिद्धांत
- मानक Java Code Conventions का पालन करें
- पठनीयता और रखरखाव योग्यता को प्राथमिकता दें
- Spring इकोसिस्टम में एकरूपता बनाए रखें
- मूल Java की सर्वोत्तम प्रथाओं के साथ संरेखित करें

## 2. कोड फ़ॉर्मैटिंग

### सामान्य दिशा-निर्देश
- IntelliJ IDEA के डिफ़ॉल्ट फ़ॉर्मैटिंग का उपयोग करें
- 4-स्पेस इंडेंटेशन (टैब्स नहीं)
- अधिकतम लाइन लंबाई 120 वर्ण
- मानक Java ब्रेसिंग शैली का उपयोग करें

### विशिष्ट फ़ॉर्मैटिंग नियम
- मेथड्स के बीच खाली लाइन
- ट्रेलिंग व्हाइटस्पेस नहीं
- Unix-शैली लाइन समाप्ति (LF) का उपयोग करें

## 3. नामकरण परंपराएं

### क्लास नामकरण
- वर्णनात्मक, सार्थक नामों का उपयोग करें
- UpperCamelCase का उपयोग करें
- उदाहरण:
  - `ConfigurationProperties`
  - `AutoConfigurationImportSelector`
  - `SpringApplication`

### मेथड नामकरण
- lowerCamelCase का उपयोग करें
- क्रिया या क्रिया वाक्यांश
- उदाहरण:
  - `configure()`
  - `registerBeanDefinitions()`
  - `isEnabledByDefault()`

## 4. एनोटेशन प्रथाएं

### एनोटेशन क्रम
- एनोटेशन के लिए मानक क्रम:
  1. ओवरराइड एनोटेशन (`@Override`)
  2. स्कोप एनोटेशन (`@Component`, `@Service`)
  3. डिपेंडेंसी इंजेक्शन एनोटेशन
  4. ट्रांजैक्शनल एनोटेशन
  5. कस्टम प्रोजेक्ट एनोटेशन

### एनोटेशन प्लेसमेंट
```java
@Component
@Transactional
public class UserService {
    @Autowired
    private UserRepository repository;
}
```

## 5. डिपेंडेंसी इंजेक्शन

### पसंदीदा इंजेक्शन विधि
- कंस्ट्रक्टर इंजेक्शन
- फ़ील्ड इंजेक्शन से बचें
- कंस्ट्रक्टर पर `@Autowired` का उपयोग करें

```java
@Service
public class UserService {
    private final UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }
}
```

## 6. लॉगिंग
- लॉगिंग के लिए SLF4J का उपयोग करें
- `private static final Logger` या Lombok के `@Slf4j` का उपयोग करें

```java
@Slf4j
@Service
public class UserService {
    public void processUser(User user) {
        log.info("Processing user: {}", user.getUsername());
    }
}
```

## 7. एरर हैंडलिंग
- विशिष्ट एक्सेप्शन का उपयोग करें
- सार्थक एरर संदेश प्रदान करें
- ग्लोबल एक्सेप्शन हैंडलिंग के लिए `@ControllerAdvice` का उपयोग करें

## 8. कॉन्फ़िगरेशन
- `application.properties` पर `application.yml` का उपयोग करें
- प्रोफ़ाइल-विशिष्ट कॉन्फ़िगरेशन का उपयोग करें
- कॉन्फ़िगरेशन वैल्यूज़ को एक्सटर्नलाइज़ करें

## 9. टेस्टिंग
- JUnit 5 का उपयोग करें
- Spring Boot Test यूटिलिटीज़ का लाभ उठाएं
- Arrange-Act-Assert पैटर्न का पालन करें

## 10. अतिरिक्त संसाधन
- [Spring Boot GitHub Coding Style](https://github.com/spring-projects/spring-boot/blob/main/CONTRIBUTING.md)
- [Spring Framework Guidelines](https://github.com/spring-projects/spring-framework/wiki/Code-Style)