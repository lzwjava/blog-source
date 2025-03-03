---
audio: false
generated: true
lang: hi
layout: post
title: सप्रिंग बूट में प्रॉपर्टी फाइल चयन
translated: true
---

एक Spring Boot Maven प्रोजेक्ट में, आपके पास दो प्रॉपर्टी फ़ाइलें हैं, `appProperties.properties` और `appProperties-hk.properties`, जो `src/main/resources` के नीचे स्थित हैं। प्रॉपर्टी फ़ाइल का उपयोग करने को नियंत्रित करने के लिए, विशेष रूप से `-hk` प्रॉपर्टी का उपयोग करने के लिए, आप Spring Boot की कॉन्फ़िगरेशन यंत्रों का उपयोग कर सकते हैं। यहाँ यह कैसे किया जा सकता है:

### समाधान

1. **एक `application.properties` फ़ाइल बनाएं**
   - डिफ़ॉल्ट रूप से, Spring Boot `src/main/resources` में `application.properties` या `application.yml` को खोजता है ताकि कॉन्फ़िगरेशन सेटिंग्स लोड कर सके।
   - अपने कस्टम प्रॉपर्टी फ़ाइलों (`appProperties.properties` और `appProperties-hk.properties`) का उपयोग करने के लिए, आप Spring Boot को `application` के बजाय `appProperties` के आधार नाम के साथ फ़ाइलें खोजने के लिए सूचित कर सकते हैं।
   - नए `application.properties` फ़ाइल में `src/main/resources` में निम्न लाइन जोड़ें:

     ```properties
     spring.config.name=appProperties
     ```

   - यह सेटिंग Spring Boot को `appProperties.properties` को आधार कॉन्फ़िगरेशन फ़ाइल के रूप में लोड करने के लिए बताती है, और जब एक प्रोफ़ाइल सक्रिय है, तो यह `appProperties-{profile}.properties` जैसे प्रोफ़ाइल-विशिष्ट विकल्पों को भी स्वचालित रूप से खोजेगा।

2. **Spring प्रोफ़ाइल का उपयोग करके `-hk` प्रॉपर्टी निर्दिष्ट करें**
   - Spring Boot प्रोफ़ाइल का समर्थन करता है, जो सक्रिय प्रोफ़ाइल के आधार पर अतिरिक्त या ओवरराइड प्रॉपर्टी फ़ाइलें लोड करने की अनुमति देता है।
   - जब आपका फ़ाइल `appProperties-hk.properties` नामित है, तो यह `appProperties-{profile}.properties` पैटर्न का पालन करता है। यहाँ, "hk" एक प्रोफ़ाइल नाम के रूप में संबोधित किया जा सकता है।
   - `appProperties-hk.properties` का उपयोग करने के लिए, अपने एप्लिकेशन को चलाते समय "hk" प्रोफ़ाइल सक्रिय करें। Spring Boot तब दोनों `appProperties.properties` और `appProperties-hk.properties` लोड करेगा, और `appProperties-hk.properties` में परिभाषित प्रॉपर्टी `appProperties.properties` में किसी भी मिलने वाले प्रॉपर्टी को ओवरराइड कर देंगे।

3. **“hk” प्रोफ़ाइल सक्रिय करने का तरीका**
   - **कमांड लाइन के माध्यम से**: अपने Spring Boot एप्लिकेशन को चलाते समय सक्रिय प्रोफ़ाइल को `--spring.profiles.active` अर्ग्यूमेंट के साथ निर्दिष्ट करें। उदाहरण के लिए:
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     `myapp.jar` को आपकी एप्लिकेशन के द्वारा Maven द्वारा जनरेट किए गए JAR फ़ाइल के नाम से बदलें।

   - **Maven के माध्यम से**: अगर आप `spring-boot:run` लक्ष्य का उपयोग करके एप्लिकेशन को चलाते हैं, तो प्रोफ़ाइल को `pom.xml` में कॉन्फ़िगर करें:
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
     फिर चलाएं:
     ```bash
     mvn spring-boot:run
     ```

   - **सिस्टम प्रॉपर्टी के माध्यम से**: प्रोफ़ाइल को एक JVM अर्ग्यूमेंट के रूप में सेट करें:
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **परिवेश परिवर्तन के माध्यम से**: प्रोफ़ाइल को आपकी परिस्थिति में निर्यात करें (उदाहरण के लिए, एक Unix-प्रकार के सिस्टम में):
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### यह कैसे काम करता है
- जब `spring.config.name=appProperties` `application.properties` में सेट है, तो Spring Boot `appProperties` को कॉन्फ़िगरेशन फ़ाइलों के लिए आधार नाम के रूप में उपयोग करता है।
- जब कोई प्रोफ़ाइल सक्रिय नहीं है, तो केवल `appProperties.properties` लोड होती है।
- जब "hk" प्रोफ़ाइल सक्रिय होता है (उदाहरण के लिए, `--spring.profiles.active=hk` के माध्यम से), तो Spring Boot दोनों `appProperties.properties` और `appProperties-hk.properties` लोड करता है। `appProperties-hk.properties` में परिभाषित प्रॉपर्टी `appProperties.properties` में किसी भी डुप्लिकेट प्रॉपर्टी को ओवरराइड कर देंगे।

### अंतिम कदम
- सुनिश्चित करें कि दोनों `appProperties.properties` और `appProperties-hk.properties` `src/main/resources` में हैं।
- `application.properties` के साथ `spring.config.name=appProperties` को `src/main/resources` में जोड़ें।
- "hk" प्रोफ़ाइल सक्रिय करके अपने एप्लिकेशन को चलाएं ताकि `-hk` प्रॉपर्टी का उपयोग किया जा सके।

यह तरीका Spring Boot के अनुकरणों के साथ मेल खाता है, जिससे यह आपके प्रोजेक्ट में उपयोग किए जाने वाले प्रॉपर्टी फ़ाइल का नियंत्रण करने का एक सामान्य और सरल तरीका बन जाता है। `-hk` प्रॉपर्टी का विशेष रूप से उपयोग करने के लिए, ऊपर वर्णित तरीके से "hk" प्रोफ़ाइल सक्रिय करें।