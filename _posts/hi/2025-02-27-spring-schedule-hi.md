---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग में कार्यों का निर्धारण
translated: true
type: note
---

स्प्रिंग में टास्क शेड्यूल करना एक सामान्य आवश्यकता है जो दोहराए जाने वाले कार्यों को स्वचालित करने के लिए होती है, जैसे ईमेल भेजना, रिपोर्ट जनरेट करना, या सिस्टम रखरखाव करना। स्प्रिंग अपने `@Scheduled` एनोटेशन और स्प्रिंग टास्क स्केड्यूलर के माध्यम से एक शक्तिशाली और उपयोग में आसान टास्क शेड्यूलिंग सुविधा प्रदान करता है। नीचे, मैं आपको इसे सेट अप करने के चरणों के माध्यम से लेकर चलूंगा और मुख्य अवधारणाओं को समझाऊंगा।

### 1. **अपने स्प्रिंग एप्लिकेशन में शेड्यूलिंग सक्षम करें**
शेड्यूलिंग का उपयोग करने के लिए, आपको इसे अपने स्प्रिंग एप्लिकेशन में सक्षम करना होगा। यह एक कॉन्फ़िगरेशन क्लास में `@EnableScheduling` एनोटेशन जोड़कर किया जाता है।

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@EnableScheduling
public class SchedulerConfig {
    // कॉन्फ़िगरेशन क्लास तब तक खाली रह सकती है जब तक आपको कस्टम स्केड्यूलर सेटिंग्स की आवश्यकता न हो
}
```

यह स्प्रिंग को `@Scheduled` एनोटेशन वाली मेथड्स को खोजने और उन्हें उनके परिभाषित शेड्यूल के अनुसार निष्पादित करने के लिए कहता है।

---

### 2. **शेड्यूल करने के लिए एक टास्क बनाएं**
आप किसी भी स्प्रिंग-मैनेज्ड बीन (जैसे `@Component` या `@Service`) में एक मेथड परिभाषित कर सकते हैं और उसे `@Scheduled` से एनोटेट कर सकते हैं। यहां एक उदाहरण दिया गया है:

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class MyScheduledTasks {

    // हर 5 सेकंड में चलता है
    @Scheduled(fixedRate = 5000)
    public void performTask() {
        System.out.println("Task executed at: " + System.currentTimeMillis());
    }
}
```

इस उदाहरण में:
- `@Component` क्लास को एक स्प्रिंग बीन बनाता है।
- `@Scheduled(fixedRate = 5000)` मेथड को हर 5 सेकंड (5000 मिलीसेकंड) में चलाता है।

---

### 3. **शेड्यूलिंग विकल्पों के प्रकार**
स्प्रिंग कार्यों को चलाने के समय को परिभाषित करने के लिए कई तरीके प्रदान करता है:

#### a) **फिक्स्ड रेट (Fixed Rate)**
- टास्क को एक निश्चित अंतराल पर निष्पादित करता है, भले ही टास्क को कितना समय लगता हो।
- उदाहरण: `@Scheduled(fixedRate = 5000)` (हर 5 सेकंड)।

#### b) **फिक्स्ड डिले (Fixed Delay)**
- एक निष्पादन के अंत और अगले निष्पादन की शुरुआत के बीच एक निश्चित देरी के साथ टास्क को निष्पादित करता है।
- उदाहरण: `@Scheduled(fixedDelay = 5000)` (पिछला टास्क समाप्त होने के 5 सेकंड बाद)।

#### c) **क्रॉन एक्सप्रेशन (Cron Expression)**
- अधिक जटिल शेड्यूल (जैसे, "हर वीकडे 9 AM पर") के लिए क्रॉन-जैसी सिंटैक्स का उपयोग करता है।
- उदाहरण: `@Scheduled(cron = "0 0 9 * * MON-FRI")`।

#### d) **इनिशियल डिले (Initial Delay)**
- टास्क के पहले निष्पादन में देरी करता है। इसे `fixedRate` या `fixedDelay` के साथ संयोजित करें।
- उदाहरण: `@Scheduled(fixedRate = 5000, initialDelay = 10000)` (10 सेकंड के बाद शुरू होता है, फिर हर 5 सेकंड में चलता है)।

---

### 4. **क्रॉन सिंटैक्स बेसिक्स**
यदि आप क्रॉन का उपयोग करते हैं, तो यहां एक त्वरित संदर्भ दिया गया है:
- फॉर्मेट: `सेकंड मिनट घंटा महीने-का-दिन महीना सप्ताह-का-दिन`
- उदाहरण: `@Scheduled(cron = "0 15 10 * * ?")` (हर दिन 10:15 AM पर चलता है)।

| फील्ड         | स्वीकृत मान         |
|---------------|----------------------|
| सेकंड        | 0-59                |
| मिनट        | 0-59                |
| घंटा          | 0-23                |
| महीने का दिन  | 1-31                |
| महीना         | 1-12 या JAN-DEC     |
| सप्ताह का दिन   | 0-7 या SUN-SAT (0 या 7 रविवार है) |

विशेष करैक्टर जैसे `*` (सभी), `,` (सूची), `-` (रेंज), `/` (वृद्धि) का उपयोग किया जा सकता है।

---

### 5. **डिपेंडेंसीज़ (Dependencies)**
यदि आप स्प्रिंग बूट का उपयोग कर रहे हैं, तो शेड्यूलिंग सुविधा `spring-boot-starter` डिपेंडेंसी में डिफ़ॉल्ट रूप से शामिल होती है। एक गैर-बूट स्प्रिंग प्रोजेक्ट के लिए, सुनिश्चित करें कि आपके पास है:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.3</version> <!-- नवीनतम वर्जन का उपयोग करें -->
</dependency>
```

---

### 6. **स्प्रिंग बूट के साथ पूर्ण उदाहरण**
यहां एक संपूर्ण स्प्रिंग बूट उदाहरण दिया गया है:

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
        System.out.println("Running every 5 seconds: " + System.currentTimeMillis());
    }

    @Scheduled(cron = "0 */1 * * * *")
    public void runEveryMinute() {
        System.out.println("Running every minute: " + System.currentTimeMillis());
    }
}
```

---

### 7. **स्केड्यूलर को कस्टमाइज़ करना (वैकल्पिक)**
डिफ़ॉल्ट रूप से, स्प्रिंग एक सिंगल-थ्रेडेड स्केड्यूलर का उपयोग करता है। यदि आपको समवर्ती (concurrent) टास्क निष्पादन की आवश्यकता है, तो आप एक कस्टम `TaskScheduler` कॉन्फ़िगर कर सकते हैं:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskScheduler;

@Configuration
public class SchedulerConfig {

    @Bean
    public ThreadPoolTaskScheduler taskScheduler() {
        ThreadPoolTaskScheduler scheduler = new ThreadPoolTaskScheduler();
        scheduler.setPoolSize(10); // थ्रेड्स की संख्या
        scheduler.setThreadNamePrefix("my-scheduler-");
        return scheduler;
    }
}
```

यह कई कार्यों को समानांतर में चलाने की अनुमति देता है।

---

### 8. **अपने शेड्यूल्ड टास्क्स का परीक्षण करना**
- अपने एप्लिकेशन को रन करें और यह सत्यापित करने के लिए कंसोल लॉग्स की जांच करें कि टास्क अपेक्षा के अनुरूप निष्पादित हो रहे हैं।
- परिणामों को शीघ्रता से देखने के लिए परीक्षण के दौरान छोटे अंतराल (जैसे, हर 2 सेकंड) का उपयोग करें।