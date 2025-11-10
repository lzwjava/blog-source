---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: लॉग4ज कॉन्फ़िगरेशन गाइड
translated: true
type: note
---

### Log4j कॉन्फ़िगरेशन का अवलोकन
Log4j एक लोकप्रिय Java लॉगिंग फ्रेमवर्क है जो आपको लॉग आउटपुट स्तर और गंतव्यों को नियंत्रित करने की अनुमति देता है। संस्करण 2.x (अनुशंसित) के लिए, कॉन्फ़िगरेशन आमतौर पर एक XML, JSON, YAML, या Properties फ़ाइल (जैसे, `log4j2.xml`) में परिभाषित किए जाते हैं। इस सेटअप में शामिल है:

- **लॉगर्स**: विशिष्ट कक्षाओं या पैकेजों के लिए किस स्तर के संदेशों (जैसे, DEBUG, INFO, WARN, ERROR) को लॉग करना है, यह परिभाषित करता है।
- **ऐपेंडर्स**: निर्दिष्ट करता है कि लॉग कहाँ भेजे जाते हैं, जैसे कंसोल (मानक आउटपुट) या फ़ाइलें (रोटेशन जैसे विकल्पों के साथ)।
- **रूट लॉगर**: एक डिफ़ॉल्ट लॉगर जो विशिष्ट लॉगर्स द्वारा कवर नहीं की गई सभी कक्षाओं पर लागू होता है।

कंसोल और फ़ाइल लॉगिंग दोनों को कॉन्फ़िगर करने के लिए, आप आमतौर पर एक `ConsoleAppender` और एक `RollingFileAppender` (स्वचालित रोटेशन वाली फ़ाइल लॉग्स के लिए) जोड़ेंगे। कॉन्फ़िग फ़ाइल को अपनी क्लासपाथ (जैसे, Maven प्रोजेक्ट्स में `src/main/resources`) में रखें।

यदि आप Log4j 1.x का उपयोग कर रहे हैं, तो 2.x में अपग्रेड करें—यह तेज़ है और इसमें बेहतर सुविधाएँ हैं। नीचे एक सैंपल XML कॉन्फ़िग के साथ एक चरण-दर-चरण मार्गदर्शिका दी गई है।

### फ़ाइल और कंसोल लॉगर्स कॉन्फ़िगर करने के चरण
1. **निर्भरताएँ जोड़ें**: सुनिश्चित करें कि Log4j 2.x आपके pom.xml (Maven) या build.gradle (Gradle) में है। Maven के लिए उदाहरण:
   ```
   <dependency>
       <groupId>org.apache.logging.log4j</groupId>
       <artifactId>log4j-core</artifactId>
       <version>2.23.1</version>  <!-- नवीनतम संस्करण का उपयोग करें -->
   </dependency>
   <dependency>
       <groupId>org.apache.logging.log4j</groupId>
       <artifactId>log4j-api</artifactId>
       <version>2.23.1</version>
   </dependency>
   ```

2. **एक कॉन्फ़िगरेशन फ़ाइल बनाएँ**: अपने resources फोल्डर में `log4j2.xml` बनाएँ।

3. **ऐपेंडर्स परिभाषित करें**:
   - ConsoleAppender: टर्मिनल/कंसोल पर आउटपुट देता है।
   - RollingFileAppender: एक फ़ाइल में लिखता है और आकार के आधार पर इसे रोटेट करता है (जैसे, जब यह 10MB तक पहुँच जाए, तो यह एक नई फ़ाइल बनाता है)।

4. **लॉगर्स कॉन्फ़िगर करें**: लॉगिंग स्तर (जैसे, INFO) सेट करें और ऐपेंडर्स निर्दिष्ट करें। रूट लॉगर वैश्विक लॉगिंग को संभालता है।

5. **कोड में उपयोग करें**: अपनी Java कक्षाओं में, इस तरह एक लॉगर प्राप्त करें:
   ```java
   import org.apache.logging.log4j.LogManager;
   import org.apache.logging.log4j.Logger;
   
   public class MyClass {
       private static final Logger logger = LogManager.getLogger(MyClass.class);
       // लॉग संदेश: logger.debug("Debug message"); logger.info("Info message");
   }
   ```

### सैंपल कॉन्फ़िगरेशन (log4j2.xml)
यहाँ कंसोल और रोटेटिंग फ़ाइल लॉगिंग के लिए एक पूर्ण XML कॉन्फ़िग है। यह INFO और उससे ऊपर के स्तर को कंसोल पर लॉग करता है, और सभी स्तरों को एक ऐसी फ़ाइल में लॉग करता है जो दैनिक या 10MB होने पर रोटेट होती है।

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">  <!-- आंतरिक Log4j लॉगिंग स्तर -->

    <!-- ऐपेंडर्स सेक्शन -->
    <Appenders>

        <!-- कंसोल ऐपेंडर -->
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%t] %-5level %logger{36} - %msg%n"/>
        </Console>

        <!-- रोलिंग फ़ाइल ऐपेंडर -->
        <RollingFile name="File" fileName="logs/app.log" filePattern="logs/app-%d{yyyy-MM-dd}-%i.log.gz">
            <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%t] %-5level %logger{36} - %msg%n"/>
            <Policies>
                <TimeBasedTriggeringPolicy />  <!-- दैनिक रोटेट करें -->
                <SizeBasedTriggeringPolicy size="10MB"/>  <!-- या आकार के आधार पर -->
            </Policies>
            <DefaultRolloverStrategy max="7"/>  <!-- अधिकतम 7 पुरानी फ़ाइलें रखें -->
        </RollingFile>

    </Appenders>

    <!-- लॉगर्स सेक्शन -->
    <Loggers>

        <!-- आपके पैकेज के लिए विशिष्ट लॉगर (वैकल्पिक) -->
        <Logger name="com.yourapp" level="DEBUG" additivity="false">
            <AppenderRef ref="File"/>  <!-- इस पैकेज के लिए केवल फ़ाइल में -->
        </Logger>

        <!-- रूट लॉगर -->
        <Root level="INFO">
            <AppenderRef ref="Console"/>  <!-- कंसोल पर Debug/info -->
            <AppenderRef ref="File"/>     <!-- फ़ाइल में सभी स्तर -->
        </Root>

    </Loggers>

</Configuration>
```

- **पैटर्न लेआउट**: लॉग प्रारूप को परिभाषित करता है (जैसे, टाइमस्टैम्प, थ्रेड, लॉग स्तर, लॉगर नाम, संदेश)।
- **रोलिंग पॉलिसीज़**: फ़ाइलें समय (जैसे, `-d{yyyy-MM-dd}`) या आकार के आधार पर रोटेट होती हैं; `.gz` के साथ संपीड़ित।
- **स्तर**: विस्तृत डेवलपमेंट लॉग्स के लिए `DEBUG` सेट करें, प्रोडक्शन के लिए `INFO` (आवश्यकतानुसार समायोजित करें)।
- **परीक्षण**: अपना ऐप चलाएँ और कंसोल आउटपुट + फ़ाइलों के लिए `logs/` फोल्डर की जाँच करें।

Properties-आधारित कॉन्फ़िग के लिए, Log4j दस्तावेज़ देखें—यह सरल है लेकिन कम लचीला है। यदि आपको JSON/YAML या संस्करण-विशिष्ट ट्वीक्स की आवश्यकता है, तो [आधिकारिक Log4j 2 कॉन्फ़िगरेशन डॉक्स](https://logging.apache.org/log4j/2.x/manual/configuration.html) देखें। यदि यह आपके सेटअप से मेल नहीं खाता (जैसे, Log4j 1.x), तो अधिक विवरण प्रदान करें!