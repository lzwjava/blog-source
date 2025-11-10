---
audio: false
generated: true
lang: hi
layout: post
title: लॉग्स में खाली `traceId` और `spanId` का समस्या निवारण
translated: true
type: note
---

आपकी लॉग लाइनों `[blog-server,,]` में `traceId` और `spanId` खाली होने की संभावना निम्नलिखित में से किसी एक कारण से है:

* **Sleuth Dependency का गायब या गलत होना:** सुनिश्चित करें कि `spring-cloud-starter-sleuth` dependency आपके प्रोजेक्ट के `pom.xml` (Maven के लिए) या `build.gradle` (Gradle के लिए) में सही तरीके से जोड़ी गई है, और आप संगत Spring Boot और Spring Cloud versions का उपयोग कर रहे हैं। इस dependency के बिना, Spring Cloud Sleuth की auto-configuration सक्रिय नहीं होगी।

    ```xml
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-sleuth</artifactId>
    </dependency>
    ```

* **कस्टम लॉगिंग पैटर्न:** यदि आपने एक कस्टम लॉगिंग पैटर्न परिभाषित किया है (जैसे `logback-spring.xml` या `application.properties` में), तो आपको `traceId` और `spanId` के लिए प्लेसहोल्डर्स को स्पष्ट रूप से शामिल करना होगा। यदि ये प्लेसहोल्डर्स गायब हैं, तो भले ही Sleuth सक्रिय हो, ये ID आपकी लॉग्स में दिखाई नहीं देंगे।

    Logback के लिए, सुनिश्चित करें कि आपके पैटर्न में `%X{traceId}` और `%X{spanId}` शामिल हैं:

    ```xml
    <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level [${spring.application.name:-},%X{traceId:-},%X{spanId:-}] %thread %logger{36} - %msg%n</pattern>
    ```

* **कोई सक्रिय Trace/Span Context न होना:** हालांकि Sleuth कई Spring components (जैसे HTTP requests के लिए `DispatcherServlet`) का स्वचालित रूप से इंस्ट्रुमेंटेशन करता है, यह संभव है कि ये विशिष्ट लॉग संदेश एक ऐसे context में generate हो रहे हों जहाँ कोई trace या span अभी तक शुरू नहीं किया गया है या propagate नहीं किया गया है। उदाहरण के लिए, एप्लिकेशन startup की कुछ बहुत शुरुआती लॉग्स या ऐसे threads से आने वाली लॉग्स जिन्हें Sleuth के context propagation द्वारा manage नहीं किया जाता है, में ये ID नहीं हो सकते हैं। हालाँकि, सक्रिय HTTP request प्रोसेसिंग के दौरान की लॉग्स, जैसे `HttpEntityMethodProcessor` और `DispatcherServlet` द्वारा एक request को पूरा करना, के लिए यह स्थिति कम सामान्य है यदि Sleuth ठीक से सेट अप है।

समस्या निवारण के लिए, पहले अपनी dependencies और लॉगिंग कॉन्फ़िगरेशन को सत्यापित करें। यदि वे सही हैं, तो सुनिश्चित करें कि requests वास्तव में आपकी एप्लिकेशन तक पहुँच रही हैं और Spring MVC `DispatcherServlet` द्वारा प्रोसेस की जा रही हैं, जिससे Sleuth का इंस्ट्रुमेंटेशन ट्रिगर होना चाहिए।