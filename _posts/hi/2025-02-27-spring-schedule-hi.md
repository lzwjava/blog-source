---
audio: true
generated: false
lang: hi
layout: post
title: कार्यक्रमण Spring में
translated: true
---

सचिवित करने के लिए Spring में कार्यक्रमण एक आम आवश्यकता है, जैसे कि ईमेल भेजना, रिपोर्ट बनाना, या सिस्टम रखरखाव करना। Spring एक शक्तिशाली और आसान-से-उपयोग करने योग्य कार्यक्रमण सुविधा प्रदान करता है, अपने `@Scheduled` एनोटेशन और Spring Task Scheduler के माध्यम से। नीचे, मैं आपको इसे सेटअप करने के चरणों के बारे में बताता हूँ और मुख्य अवधारणाओं को समझाता हूँ।

### 1. **अपने Spring एप्लिकेशन में कार्यक्रमण सक्षम करें**
किसी कार्यक्रमण का उपयोग करने के लिए, आपको अपने Spring एप्लिकेशन में इसे सक्षम करना होगा। यह एक कॉन्फ़िगरेशन क्लास में `@EnableScheduling` एनोटेशन जोड़कर किया जाता है।

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@EnableScheduling
public class SchedulerConfig {
    // कॉन्फ़िगरेशन क्लास खाली रह सकता है, जब तक कि आपको कस्टम स्केड्यूलर सेटिंग्स की आवश्यकता न हो
}
```

यह Spring को `@Scheduled` एनोटेशन से सज्जित विधियों को खोजने और उनके परिभाषित कार्यक्रमों के अनुसार उन्हें कार्यान्वित करने के लिए कहता है।

---

### 2. **एक कार्यक्रमित कार्य बनाएं**
आप किसी भी Spring-प्रबंधित बीन (जैसे कि एक `@Component` या `@Service`) में एक विधि परिभाषित कर सकते हैं और उसे `@Scheduled` से सज्जित कर सकते हैं। यहाँ एक उदाहरण है:

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class MyScheduledTasks {

    // हर 5 सेकंड पर चलता है
    @Scheduled(fixedRate = 5000)
    public void performTask() {
        System.out.println("कार्य कार्यान्वित हुआ: " + System.currentTimeMillis());
    }
}
```

इस उदाहरण में:
- `@Component` क्लास को एक Spring बीन बनाता है।
- `@Scheduled(fixedRate = 5000)` विधि को हर 5 सेकंड (5000 मिलीसेकंड) पर चलाता है।

---

### 3. **कार्यक्रमण विकल्पों के प्रकार**
Spring कई तरीकों से परिभाषित करता है कि एक कार्य कब चलना चाहिए:

#### a) **निश्चित दर**
- कार्यक्रमण को एक निश्चित अंतराल पर कार्यक्रमित करता है, चाहे कार्य कितना समय लेता हो।
- उदाहरण: `@Scheduled(fixedRate = 5000)` (हर 5 सेकंड पर).

#### b) **निश्चित विलंब**
- कार्यक्रमण को एक निश्चित विलंब के साथ कार्यक्रमित करता है, एक कार्यक्रमण के अंत और अगले कार्यक्रमण के आरंभ के बीच।
- उदाहरण: `@Scheduled(fixedDelay = 5000)` (पिछले कार्यक्रमण के समाप्त होने के 5 सेकंड बाद).

#### c) **क्रॉन अभिव्यक्ति**
- अधिक जटिल कार्यक्रमण के लिए क्रॉन-आधारित संकेतन का उपयोग करता है (उदाहरण: "हर सप्ताह के दिन 9 बजे").
- उदाहरण: `@Scheduled(cron = "0 0 9 * * MON-FRI")`.

#### d) **आरंभिक विलंब**
- कार्यक्रमण का पहला कार्यक्रमण विलंबित करता है। `fixedRate` या `fixedDelay` के साथ संयोजित करें।
- उदाहरण: `@Scheduled(fixedRate = 5000, initialDelay = 10000)` (10 सेकंड बाद शुरू होता है, फिर हर 5 सेकंड पर चलता है).

---

### 4. **क्रॉन संकेतन के आधार**
अगर आप क्रॉन का उपयोग करते हैं, तो यहाँ एक जल्दी संदर्भ है:
- प्रारूप: `सेकंड मिनट घंटा महीने का दिन महीना सप्ताह का दिन`
- उदाहरण: `@Scheduled(cron = "0 15 10 * * ?")` (हर दिन 10:15 बजे चलता है).

| क्षेत्र         | अनुमत मान       |
|---------------|----------------------|
| सेकंड        | 0-59                |
| मिनट        | 0-59                |
| घंटा          | 0-23                |
| महीने का दिन  | 1-31                |
| महीना         | 1-12 या JAN-DEC     |
| सप्ताह का दिन   | 0-7 या SUN-SAT (0 या 7 रविवार है) |

विशेष वर्ण जैसे `*` (सभी), `,` (सूची), `-` (रेंज), `/` (वृद्धि) का उपयोग किया जा सकता है।

---

### 5. **अनुप्रयोग**
अगर आप Spring Boot का उपयोग कर रहे हैं, तो कार्यक्रमण सुविधा `spring-boot-starter` निर्भरता में डिफ़ॉल्ट रूप से शामिल है। एक नॉन-बूट Spring प्रोजेक्ट के लिए, सुनिश्चित करें कि:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.3</version> <!-- नवीनतम संस्करण का उपयोग करें -->
</dependency>
```

---

### 6. **Spring Boot के साथ पूर्ण उदाहरण**
यह एक पूर्ण Spring Boot उदाहरण है:

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@SpringBootApplication
@EnableScheduling
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

@Component
class ScheduledTasks {

    @Scheduled(fixedRate = 5000)
    public void runEveryFiveSeconds() {
        System.out.println("हर 5 सेकंड पर चलता है: " + System.currentTimeMillis());
    }

    @Scheduled(cron = "0 */1 * * * *")
    public void runEveryMinute() {
        System.out.println("हर मिनट पर चलता है: " + System.currentTimeMillis());
    }
}
```

---

### 7. **स्केड्यूलर को कस्टमाइज़ करें (वैकल्पिक)**
डिफ़ॉल्ट रूप से, Spring एक एकल-थ्रेड स्केड्यूलर का उपयोग करता है। अगर आपको समांतर कार्यक्रमण की आवश्यकता है, तो आप एक कस्टम `TaskScheduler` को कॉन्फ़िगर कर सकते हैं:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskScheduler;

@Configuration
public class SchedulerConfig {

    @Bean
    public ThreadPoolTaskScheduler taskScheduler() {
        ThreadPoolTaskScheduler scheduler = new ThreadPoolTaskScheduler();
        scheduler.setPoolSize(10); // थ्रेडों की संख्या
        scheduler.setThreadNamePrefix("my-scheduler-");
        return scheduler;
    }
}
```

यह कई कार्यक्रमों को समांतर रूप से चलने की अनुमति देता है।

---

### 8. **अपने कार्यक्रमित कार्यों का परीक्षण करें**
- अपने एप्लिकेशन को चलाएं और कॉन्सोल लॉग्स को जांचें ताकि कार्यक्रमित कार्यों को कार्यान्वित होने की पुष्टि करें।
- परीक्षण के दौरान छोटे अंतराल (जैसे हर 2 सेकंड) का उपयोग करें ताकि जल्दी परिणाम देखें।