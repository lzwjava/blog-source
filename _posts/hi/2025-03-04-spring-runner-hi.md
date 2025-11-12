---
audio: false
generated: true
lang: hi
layout: post
title: जावा टेस्ट में स्प्रिंगरनर का उपयोग
translated: true
type: note
---

Java tests में JUnit के `@RunWith` runner के साथ `SpringRunner` का उपयोग करने के लिए, इन चरणों का पालन करें। ध्यान दें कि मैं मान रहा हूं कि आपके प्रश्न में "SpringRuner" एक टाइपो है और आपका मतलब `SpringRunner` से है। यहां एक पूर्ण मार्गदर्शिका दी गई है:

### चरण 1: Spring Test Dependency जोड़ें
`SpringRunner` का उपयोग करने के लिए, आपके प्रोजेक्ट में Spring Test मॉड्यूल की आवश्यकता होती है। यदि आप Maven का उपयोग कर रहे हैं, तो अपने `pom.xml` में यह dependency जोड़ें:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```

`${spring.version}` को आपके द्वारा उपयोग की जा रही Spring की version से बदलें (उदाहरण के लिए, `5.3.22`)। यदि आप Gradle का उपयोग कर रहे हैं, तो इसे अपने `build.gradle` में जोड़ें:

```gradle
testImplementation 'org.springframework:spring-test:${springVersion}'
```

यह सुनिश्चित करता है कि `SpringRunner` और अन्य Spring testing utilities उपलब्ध हों।

### चरण 2: Test Class को `@RunWith(SpringRunner.class)` के साथ Annotate करें
`@RunWith` annotation JUnit को उसके default runner के बजाय एक विशिष्ट runner का उपयोग करने के लिए कहता है। Spring integration के लिए, `SpringRunner` का उपयोग करें, जो Spring TestContext Framework का हिस्सा है। इसे अपनी test class में जोड़ें:

```java
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class MyServiceTest {
    // Test code goes here
}
```

`SpringRunner` आपके tests में dependency injection और context loading जैसी Spring features को सक्षम बनाता है। ध्यान दें कि `@RunWith` एक JUnit 4 annotation है, इसलिए यह approach मानती है कि आप JUnit 4 का उपयोग कर रहे हैं। JUnit 5 के लिए, आप `@ExtendWith(SpringExtension.class)` का उपयोग करेंगे, लेकिन "RunWith runner" का आपका उल्लेख JUnit 4 का सुझाव देता है।

### चरण 3: Spring Application Context को `@ContextConfiguration` के साथ Configure करें
अपने tests में Spring-managed beans का उपयोग करने के लिए, आपको एक Spring application context लोड करने की आवश्यकता है। `@ContextConfiguration` annotation निर्दिष्ट करता है कि यह कैसे करना है। उदाहरण के लिए, यदि आपके पास एक configuration class है (उदाहरण के लिए, `AppConfig`), तो उपयोग करें