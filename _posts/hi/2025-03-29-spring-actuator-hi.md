---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग एक्ट्यूएटर
translated: true
type: note
---

Spring Actuator Spring Boot में एक शक्तिशाली फीचर है जो आपके एप्लिकेशन की मॉनिटरिंग और प्रबंधन के लिए प्रोडक्शन-रेडी टूल्स प्रदान करता है। यहां बताया गया है कि इसका उपयोग कैसे करें:

### 1. **Spring Actuator डिपेंडेंसी जोड़ें**
Spring Actuator का उपयोग करने के लिए, आपको इसे अपने प्रोजेक्ट में शामिल करना होगा। यदि आप Maven का उपयोग कर रहे हैं, तो इसे अपने `pom.xml` में जोड़ें:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

Gradle के लिए, इसे अपने `build.gradle` में जोड़ें:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-actuator'
```

### 2. **अपना Spring Boot एप्लिकेशन शुरू करें**
एक बार डिपेंडेंसी जोड़ने के बाद, अपना Spring Boot एप्लिकेशन शुरू करें। Spring Actuator स्वचालित रूप से एंडपॉइंट्स का एक सेट सक्षम कर देगा जिसका उपयोग आप अपने ऐप की निगरानी और इंटरैक्ट करने के लिए कर सकते हैं।

### 3. **डिफ़ॉल्ट एंडपॉइंट्स तक पहुंचें**
Spring Actuator डिफ़ॉल्ट रूप से HTTP के माध्यम से कई एंडपॉइंट्स एक्सपोज़ करता है। बेस पाथ `/actuator` है। यहां कुछ सामान्यतः उपयोग किए जाने वाले एंडपॉइंट्स दिए गए हैं (मान लें कि आपका ऐप `localhost:8080` पर चल रहा है):
- **हेल्थ चेक**: `http://localhost:8080/actuator/health`
  - आपके एप्लिकेशन की स्थिति लौटाता है (उदाहरण के लिए, `{"status":"UP"}`)।
- **एप्लिकेशन जानकारी**: `http://localhost:8080/actuator/info`
  - मनमानी एप्लिकेशन जानकारी प्रदर्शित करता है (कॉन्फ़िगर करने योग्य)।
- **मेट्रिक्स**: `http://localhost:8080/actuator/metrics`
  - मेमोरी उपयोग, CPU, और बहुत कुछ जैसे विस्तृत मेट्रिक्स प्रदान करता है।

सुरक्षा कारणों से, डिफ़ॉल्ट रूप से केवल `/health` और `/info` सक्षम होते हैं। अधिक एंडपॉइंट्स को एक्सपोज़ करने के लिए, आपको उन्हें कॉन्फ़िगर करने की आवश्यकता है।

### 4. **Actuator एंडपॉइंट्स कॉन्फ़िगर करें**
आप अपनी `application.properties` या `application.yml` फ़ाइल में यह कस्टमाइज़ कर सकते हैं कि कौन से एंडपॉइंट्स एक्सपोज़ होंगे। उदाहरण के लिए:

#### `application.properties`
```properties
# विशिष्ट एंडपॉइंट्स सक्षम करें
management.endpoints.web.exposure.include=health,info,metrics,beans

# बेस पाथ बदलें (वैकल्पिक)
management.endpoints.web.base-path=/manage
```

#### `application.yml`
```yaml
management:
  endpoints:
    web:
      exposure:
        include: health, info, metrics, beans
      base-path: /manage
```

इस कॉन्फ़िगरेशन के साथ, `/manage/metrics` या `/manage/beans` जैसे एंडपॉइंट्स उपलब्ध होंगे।

### 5. **उपलब्ध एंडपॉइंट्स एक्सप्लोर करें**
यहां कुछ उपयोगी Actuator एंडपॉइंट्स दिए गए हैं जिन्हें आप सक्षम कर सकते हैं:
- `/actuator/beans`: आपके एप्लिकेशन में सभी Spring beans की सूची देता है।
- `/actuator/env`: एनवायरनमेंट प्रॉपर्टीज़ दिखाता है।
- `/actuator/loggers`: लॉगर लेवल दिखाता और संशोधित करता है।
- `/actuator/shutdown`: ऐप को सुरुचिपूर्वक बंद करता है (डिफ़ॉल्ट रूप से अक्षम)।

टेस्टिंग के लिए सभी एंडपॉइंट्स सक्षम करने के लिए, उपयोग करें:
```properties
management.endpoints.web.exposure.include=*
```

### 6. **Actuator एंडपॉइंट्स सुरक्षित करें**
चूंकि Actuator संवेदनशील डेटा एक्सपोज़ करता है, आपको इसे प्रोडक्शन में सुरक्षित करना चाहिए:
- Spring Security जोड़ें:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```
- `application.properties` में सुरक्षा कॉन्फ़िगर करें:
```properties
spring.security.user.name=admin
spring.security.user.password=secret
management.endpoints.web.exposure.include=health,metrics
```
अब, एंडपॉइंट्स तक पहुंचने के लिए प्रमाणीकरण (उदाहरण के लिए, `admin:secret`) की आवश्यकता होगी।

### 7. **कस्टम हेल्थ चेक जोड़ें (वैकल्पिक)**
आप `HealthIndicator` इंटरफेस को इम्प्लीमेंट करके कस्टम हेल्थ इंडिकेटर बना सकते हैं। उदाहरण:

```java
import org.springframework.boot.actuate.health.Health;
import org.springframework.boot.actuate.health.HealthIndicator;
import org.springframework.stereotype.Component;

@Component
public class CustomHealthCheck implements HealthIndicator {
    @Override
    public Health health() {
        boolean isHealthy = checkSomeCondition();
        if (isHealthy) {
            return Health.up().withDetail("customCheck", "All good!").build();
        }
        return Health.down().withDetail("customCheck", "Something's wrong").build();
    }

    private boolean checkSomeCondition() {
        // आपका लॉजिक यहां
        return true;
    }
}
```

यह `/actuator/health` एंडपॉइंट में दिखाई देगा।

### 8. **मेट्रिक्स की निगरानी करें**
मेट्रिक्स में गहराई से जाने के लिए, `/metrics` सक्षम करें और विशिष्ट मेट्रिक्स एक्सप्लोर करें जैसे:
- `http://localhost:8080/actuator/metrics/jvm.memory.used`
- `http://localhost:8080/actuator/metrics/http.server.requests`

उन्नत निगरानी के लिए आप Prometheus या Grafana जैसे टूल्स के साथ इंटीग्रेट कर सकते हैं।

### 9. **इसका परीक्षण करें**
अपना ऐप चलाएं और एंडपॉइंट्स को ब्राउज़र, `curl`, या Postman जैसे टूल्स का उपयोग करके एक्सेस करें। उदाहरण के लिए:
```bash
curl http://localhost:8080/actuator/health
```

### सुझाव
- कस्टम जानकारी (जैसे ऐप संस्करण) एक्सपोज़ करने के लिए `/actuator/info` का उपयोग करें, इसे जोड़कर:
```properties
info.app.name=MyApp
info.app.version=1.0.0
```
- कॉन्फ़िगरेशन परिवर्तन करने के बाद अपने ऐप को पुनरारंभ करें।

ये थीं मूल बातें! यदि आपको किसी विशिष्ट उपयोग के मामले या समस्या निवारण में सहायता चाहिए तो मुझे बताएं।