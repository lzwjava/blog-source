---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग बूट में प्रॉपर्टी फ़ाइल चयन
translated: true
type: note
---

एक Spring Boot Maven प्रोजेक्ट में, आपके पास दो प्रॉपर्टीज़ फाइलें हैं, `appProperties.properties` और `appProperties-hk.properties`, जो `src/main/resources` के अंदर स्थित हैं। यह नियंत्रित करने के लिए कि किस प्रॉपर्टीज़ फाइल का उपयोग किया जाए, विशेष रूप से `-hk` प्रॉपर्टीज़ के उपयोग को निर्दिष्ट करने के लिए, आप Spring Boot की कॉन्फ़िगरेशन व्यवस्था का लाभ उठा सकते हैं। यहाँ बताया गया है कि आप इसे कैसे कर सकते हैं:

### समाधान

1. **एक `application.properties` फाइल बनाएँ**
   - डिफ़ॉल्ट रूप से, Spring Boot कॉन्फ़िगरेशन सेटिंग्स लोड करने के लिए `src/main/resources` में `application.properties` या `application.yml` की तलाश करता है।
   - अपनी कस्टम प्रॉपर्टीज़ फाइलों (`appProperties.properties` और `appProperties-hk.properties`) का उपयोग करने के लिए, आपको Spring Boot को यह बताने की आवश्यकता है कि डिफ़ॉल्ट `application` के बजाय `appProperties` बेस नाम वाली फाइलों की तलाश करें।
   - `src/main/resources` में एक नई `application.properties` फाइल में निम्न पंक्ति जोड़ें:

     ```properties
     spring.config.name=appProperties
     ```

   - यह सेटिंग Spring Boot को `appProperties.properties` को आधार कॉन्फ़िगरेशन फाइल के रूप में लोड करने के लिए कहती है, और जब कोई प्रोफाइल सक्रिय होती है तो यह स्वचालित रूप से प्रोफाइल-विशिष्ट वेरिएंट जैसे `appProperties-{profile}.properties` की भी तलाश करेगी।

2. **`-hk` प्रॉपर्टीज़ को निर्दिष्ट करने के लिए Spring प्रोफाइल्स का उपयोग करें**
   - Spring Boot प्रोफाइल्स का समर्थन करता है, जो आपको सक्रिय प्रोफाइल के आधार पर अतिरिक्त या ओवरराइडिंग प्रॉपर्टीज़ फाइलें लोड करने की अनुमति देता है।
   - चूंकि आपकी फाइल का नाम `appProperties-hk.properties` है, यह `appProperties-{profile}.properties` पैटर्न का पालन करती है। यहाँ, "hk" को एक प्रोफाइल नाम के रूप में माना जा सकता है।
   - `appProperties-hk.properties` का उपयोग करने के लिए, अपना एप्लिकेशन चलाते समय "hk" प्रोफाइल को सक्रिय करें। Spring Boot तो `appProperties.properties` और `appProperties-hk.properties` दोनों को लोड करेगा, जिसमें `appProperties-hk.properties` में परिभाषित प्रॉपर्टीज़ `appProperties.properties` में किसी भी मेल खाने वाली प्रॉपर्टीज़ को ओवरराइड कर देंगी।

3. **"hk" प्रोफाइल को कैसे सक्रिय करें**
   - **कमांड लाइन के माध्यम से**: जब आप अपना Spring Boot एप्लिकेशन चला रहे हों, तो `--spring.profiles.active` आर्ग्युमेंट का उपयोग करके सक्रिय प्रोफाइल निर्दिष्ट करें। उदाहरण के लिए:
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     `myapp.jar` को Maven द्वारा जनरेट किए गए आपके एप्लिकेशन के JAR फाइल के नाम से बदलें।

   - **Maven के माध्यम से**: यदि आप एप्लिकेशन को `spring-boot:run` गोल का उपयोग करके चला रहे हैं, तो अपनी `pom.xml` में प्रोफाइल कॉन्फ़िगर करें:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <profiles>
                 <profile>hk</profile>
             </profiles>
         </configuration>
     </plugin>
     ```
     फिर चलाएँ:
     ```bash
     mvn spring-boot:run
     ```

   - **सिस्टम प्रॉपर्टी के माध्यम से**: प्रोफाइल को JVM आर्ग्युमेंट के रूप में सेट करें:
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **एनवायरनमेंट वेरिएबल के माध्यम से**: अपने एनवायरनमेंट में प्रोफाइल एक्सपोर्ट करें (उदाहरण के लिए, यूनिक्स-जैसी सिस्टम में):
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### यह कैसे काम करता है
- `application.properties` में `spring.config.name=appProperties` सेट होने के साथ, Spring Boot कॉन्फ़िगरेशन फाइलों के लिए `appProperties` को बेस नाम के रूप में उपयोग करता है।
- जब कोई प्रोफाइल सक्रिय नहीं होती है, तो केवल `appProperties.properties` लोड होती है।
- जब "hk" प्रोफाइल सक्रिय होती है (उदाहरण के लिए, `--spring.profiles.active=hk` के माध्यम से), Spring Boot `appProperties.properties` और `appProperties-hk.properties` दोनों को लोड करता है। यदि कोई डुप्लिकेट हैं तो `appProperties-hk.properties` में परिभाषित प्रॉपर्टीज़ `appProperties.properties` वाली प्रॉपर्टीज़ पर प्राथमिकता ले लेती हैं।

### अंतिम चरण
- सुनिश्चित करें कि `appProperties.properties` और `appProperties-hk.properties` दोनों `src/main/resources` में मौजूद हैं।
- `spring.config.name=appProperties` के साथ `application.properties` को `src/main/resources` में जोड़ें।
- `-hk` प्रॉपर्टीज़ का उपयोग करने के लिए, "hk" प्रोफाइल को सक्रिय करके अपना एप्लिकेशन चलाएँ।

यह दृष्टिकोण Spring Boot परंपराओं के साथ संरेखित होता है, जिससे यह आपके प्रोजेक्ट में किस प्रॉपर्टीज़ फाइल का उपयोग किया जाएगा इसे नियंत्रित करने का एक सामान्य और सीधा तरीका बन जाता है। विशेष रूप से `-hk` प्रॉपर्टीज़ का उपयोग करने के लिए, बस ऊपर बताए अनुसार "hk" प्रोफाइल को सक्रिय करें।