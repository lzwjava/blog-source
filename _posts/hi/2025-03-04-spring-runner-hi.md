---
audio: true
generated: true
lang: hi
layout: post
title: SpringRunner को Java Tests में उपयोग करना
translated: true
---

`SpringRunner` को JUnit के `@RunWith` रनर के साथ Java टेस्ट में उपयोग करने के लिए, इन चरणों का पालन करें। ध्यान दें कि मैं आपकी पूछताछ में "SpringRuner" को एक टाइपो मानता हूँ और आप `SpringRunner` का मतलब हैं। यहाँ एक पूर्ण गाइड है:

### चरण 1: Spring Test Dependency जोड़ें
`SpringRunner` का उपयोग करने के लिए, आपको अपने प्रोजेक्ट में Spring Test मॉड्यूल की आवश्यकता है। अगर आप Maven का उपयोग कर रहे हैं, तो इस निर्भरता को अपने `pom.xml` में जोड़ें:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```

`${spring.version}` को आपका उपयोग करने वाला Spring का संस्करण (जैसे, `5.3.22`) से बदलें। अगर आप Gradle का उपयोग कर रहे हैं, तो अपने `build.gradle` में यह जोड़ें:

```gradle
testImplementation 'org.springframework:spring-test:${springVersion}'
```

यह सुनिश्चित करता है कि `SpringRunner` और अन्य Spring टेस्टिंग यूटिलिटी उपलब्ध हैं।

### चरण 2: टेस्ट क्लास को `@RunWith(SpringRunner.class)` से एनोटेट करें
`@RunWith` एनोटेशन JUnit को एक विशेष रनर का उपयोग करने के लिए बताता है, इसके डिफॉल्ट के बजाय। Spring इंटीग्रेशन के लिए, `SpringRunner` का उपयोग करें, जो Spring TestContext फ्रेमवर्क का हिस्सा है। इस एनोटेशन को अपने टेस्ट क्लास में जोड़ें:

```java
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class MyServiceTest {
    // टेस्ट कोड यहाँ जाए
}
```

`SpringRunner` Spring विशेषताओं जैसे निर्भरता इंजेक्शन और कंटेक्स्ट लोडिंग को टेस्ट में सक्षम बनाता है। ध्यान दें कि `@RunWith` एक JUnit 4 एनोटेशन है, इसलिए यह रणनीति JUnit 4 का उपयोग करने की उम्मीद करता है। JUnit 5 के लिए, आप `@ExtendWith(SpringExtension.class)` का उपयोग करेंगे, लेकिन आपकी "RunWith runner" का उल्लेख JUnit 4 का सुझाव देता है।

### चरण 3: Spring एप्लिकेशन कंटेक्स्ट को `@ContextConfiguration` के साथ कॉन्फ़िगर करें
Spring-प्रबंधित बीन्स को अपने टेस्ट में उपयोग करने के लिए, आपको एक Spring एप्लिकेशन कंटेक्स्ट लोड करना होगा। `@ContextConfiguration` एनोटेशन यह बताता है कि कैसे करना है। उदाहरण के लिए, अगर आपके पास एक कॉन्फ़िगरेशन क्लास है (जैसे, `AppConfig`), तो:

```java
import org.springframework.test.context.ContextConfiguration;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    // टेस्ट कोड यहाँ जाए
}
```

अगर आपका कॉन्फ़िगरेशन एक XML फ़ाइल में है (जैसे, `applicationContext.xml`), तो:

```java
@ContextConfiguration(locations = "classpath:applicationContext.xml")
```

यह `SpringRunner` को टेस्ट के लिए कौन से बीन्स और कॉन्फ़िगरेशन लोड करने के लिए बताता है।

### चरण 4: Spring बीन्स को `@Autowired` के साथ इंजेक्ट करें
एक बार जब कंटेक्स्ट लोड हो गया है, तो आप अपने टेस्ट क्लास में Spring-प्रबंधित बीन्स को `@Autowired` का उपयोग करके इंजेक्ट कर सकते हैं। उदाहरण के लिए, अगर आपके पास एक सेवा है जिसे `MyService` कहा जाता है:

```java
import org.springframework.beans.factory.annotation.Autowired;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    // टेस्ट विधियाँ यहाँ जाएँ
}
```

यह आपको अपने टेस्ट में इंजेक्टेड बीन का उपयोग करने की अनुमति देता है।

### चरण 5: `@Test` के साथ टेस्ट विधियाँ लिखें
JUnit के `@Test` एनोटेशन का उपयोग करके अपने टेस्ट विधियाँ परिभाषित करें। उदाहरण के लिए:

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    @Test
    public void testMyServiceMethod() {
        String result = myService.doSomething();
        assertEquals("Expected result", result);
    }
}
```

`@Test` एनोटेशन उन विधियों को चिह्नित करता है जो JUnit को टेस्ट के रूप में कार्यान्वित करने चाहिए। `SpringRunner` के साथ, ये विधियाँ Spring कंटेक्स्ट के साथ इंटरैक्ट कर सकते हैं।

### उदाहरण: सब कुछ एक साथ रखना
यहाँ एक पूर्ण उदाहरण है:

```java
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringRunner;
import static org.junit.Assert.assertEquals;

// टेस्ट के लिए कॉन्फ़िगरेशन क्लास
@Configuration
class AppConfig {
    @Bean
    public MyService myService() {
        return new MyService();
    }
}

// टेस्ट करने वाला सेवा क्लास
class MyService {
    public String doSomething() {
        return "Hello, Spring!";
    }
}

// टेस्ट क्लास
@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    @Test
    public void testMyServiceMethod() {
        String result = myService.doSomething();
        assertEquals("Hello, Spring!", result);
    }
}
```

### अतिरिक्त टिप्पणियाँ
- **उद्देश्य**: `SpringRunner` उन इंटीग्रेशन टेस्ट के लिए आदर्श है जहां आपको Spring की निर्भरता इंजेक्शन या कंटेक्स्ट विशेषताओं की आवश्यकता होती है। यूनिट टेस्ट के लिए, Mockito या सरल JUnit का विचार करें।
- **सामान्य समस्याएँ**: सुनिश्चित करें कि `spring-test` निर्भरता शामिल है, अन्यथा आप `ClassNotFoundException` जैसे त्रुटियों का सामना कर सकते हैं। भी, यह सुनिश्चित करें कि `@ContextConfiguration` एक वैध कॉन्फ़िगरेशन पर इशारा करता है।
- **वैकल्पिक एनोटेशन**: डेटाबेस को संशोधित करने वाले टेस्टों के लिए `@Transactional` का उपयोग करें (परिवर्तन को वापस लेना) या एक प्रोफ़ाइल (जैसे, "test") को निर्दिष्ट करने के लिए `@ActiveProfiles` का उपयोग करें।

यह सेटअप आपको JUnit टेस्ट को Spring के टेस्टिंग समर्थन के साथ चलाने की अनुमति देता है, जैसे निर्भरता इंजेक्शन और कंटेक्स्ट प्रबंधन जैसे विशेषताओं का लाभ उठाते हुए।