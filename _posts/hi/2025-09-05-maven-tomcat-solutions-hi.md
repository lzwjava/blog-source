---
audio: false
generated: true
image: false
lang: hi
layout: post
title: मेवेन टॉमकैट प्लगइन समस्याओं के समाधान
translated: true
type: note
---

आपको सही क्लू अपने ही लॉग में मिल गया:

> `[INFO] Skipping non-war project`

कुछ भी शुरू नहीं हुआ क्योंकि **tomcat7-maven-plugin केवल उन्हीं वेबएप्स को चलाता है जो WAR के रूप में पैकेज होते हैं** और जिनकी क्लासिक `src/main/webapp` लेआउट होती है। आपका प्रोजेक्ट अभी लगभग निश्चित रूप से JAR के रूप में पैकेज है, इसलिए प्लगइन बिल्ड के बाद बस बाहर निकल जाता है।

एक दूसरी समस्या भी है: आप **Tomcat 11** (Jakarta `jakarta.*` APIs) चला रहे हैं, लेकिन आपकी डिपेंडेंसीज़ **Spring 5.2.x** (जो `javax.*` का उपयोग करती है) की हैं। यह मिसमैच का मतलब है कि भले ही Tomcat शुरू हो जाए, बिना माइग्रेशन के Tomcat 11 पर सीधे डिप्लॉय फेल हो जाएगा। Spring 5 के लिए Tomcat 9 (javax) का उपयोग करें, या फिर Tomcat 10/11 के लिए ऐप को Spring 6/Jakarta में अपग्रेड करें।

यहां साफ-सुथरे रास्ते हैं जिनमें से आप चुन सकते हैं—एक को चुनें और यह काम करेगा:

### रास्ता 1 — Spring 5 रखें, Jetty प्लगइन के साथ लोकल रन करें (सबसे तेज़)

WAR की जरूरत नहीं; हैकिंग के लिए अच्छा।

1. प्लगइन जोड़ें:

   ```xml
   <plugin>
     <groupId>org.eclipse.jetty</groupId>
     <artifactId>jetty-maven-plugin</artifactId>
     <version>9.4.54.v20240208</version>
   </plugin>
   ```
2. रन करें:

   ```bash
   mvn jetty:run -Djetty.port=8080
   ```

यह `javax.*` का उपयोग करता है, जो Spring 5 से मेल खाता है।

### रास्ता 2 — Spring 5 रखें, एक WAR बनाएं, और Tomcat7 प्लगइन का उपयोग करें

1. `pom.xml` में WAR पैकेजिंग सेट करें:

   ```xml
   <packaging>war</packaging>
   ```
2. सुनिश्चित करें कि वेबएप लेआउट मौजूद है:

   ```
   src/main/webapp/
   src/main/webapp/WEB-INF/web.xml   # वैकल्पिक अगर आपके पास Servlet 3 इनिशियलाइज़र है
   ```
3. (वैकल्पिक) प्लगइन कॉन्फ़िगरेशन जोड़ें:

   ```xml
   <plugin>
     <groupId>org.apache.tomcat.maven</groupId>
     <artifactId>tomcat7-maven-plugin</artifactId>
     <version>2.2</version>
     <configuration>
       <path>/</path>
       <port>8080</port>
     </configuration>
   </plugin>
   ```
4. रन करें:

   ```bash
   mvn tomcat7:run            # एक्सप्लोडेड वेबएप के लिए
   # या
   mvn package && mvn tomcat7:run-war
   ```

### रास्ता 3 — Spring 5 रखें, एक स्टैंडअलोन Tomcat 9 पर डिप्लॉय करें

यह बिना कोड बदले `javax.*` से मेल खाता है।

```bash
brew install tomcat@9
/opt/homebrew/opt/tomcat@9/bin/catalina start
```

अपना WAR बनाएं और उसे `.../tomcat@9/libexec/webapps/` में ड्रॉप कर दें।

### रास्ता 4 — ऐप को Spring 6/Jakarta में अपग्रेड करें, Tomcat 11 के साथ बने रहें

अगर आप आधुनिक Tomcat चाहते हैं:

* Spring Framework 6.x / Spring Boot 3.x में अपग्रेड करें।
* इम्पोर्ट्स को `javax.*` से `jakarta.*` में बदलें।
* फिर Tomcat 10/11 ठीक रहेगा।

---

#### क्यों `mvn tomcat7:run` ने सफलता प्रिंट की लेकिन "कुछ नहीं हुआ"

* Maven फेज सफलतापूर्वक पूरे हो गए, लेकिन प्लगइन ने **गैर-WAR पैकेजिंग** देखी, इसलिए इसने एक एम्बेडेड Tomcat **शुरू नहीं किया**। यही "Skipping non-war project" का सटीक मतलब है।

---

अगर आप मुझे बताएं कि आप कौन सा रास्ता पसंद करते हैं, तो मैं आपको उस सेटअप के लिए सटीक `pom.xml` और न्यूनतम फाइलें दूंगा (जिसमें एक छोटा सा कंट्रोलर और इसे `http://localhost:8080/hello` पर हिट करने का तरीका भी शामिल होगा)।