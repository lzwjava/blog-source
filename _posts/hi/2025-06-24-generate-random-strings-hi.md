---
audio: false
generated: true
lang: hi
layout: post
title: अपाचे कॉमन्स लैंग के साथ यादृच्छिक स्ट्रिंग्स जनरेट करना
translated: true
type: note
---

`RandomStringUtils` Apache Commons Lang लाइब्रेरी का एक अत्यंत उपयोगी क्लास है जो रैंडम स्ट्रिंग्स जनरेट करने के लिए विभिन्न स्टैटिक मेथड प्रदान करता है। इसमें विशिष्ट लंबाई वाली स्ट्रिंग्स, केवल अक्षरों वाली, केवल नंबर वाली, अल्फान्यूमेरिक करैक्टर वाली, या यहां तक कि कस्टम करैक्टर सेट से बनी स्ट्रिंग्स जनरेट करना शामिल है।

इसका उपयोग कैसे करें और आवश्यक Maven डिपेंडेंसी:

## `org.apache.commons.lang3.RandomStringUtils;` का उपयोग कैसे करें

सबसे पहले, आपको अपनी Java फाइल में इस क्लास को इम्पोर्ट करना होगा:

```java
import org.apache.commons.lang3.RandomStringUtils;
```

फिर आप इसकी स्टैटिक मेथड्स का उपयोग कर सकते हैं। यहां कुछ सामान्य उदाहरण दिए गए हैं:

1.  **विशिष्ट लंबाई की रैंडम अल्फान्यूमेरिक स्ट्रिंग जनरेट करें:**

    ```java
    String randomAlphaNumeric = RandomStringUtils.randomAlphanumeric(10);
    System.out.println("Random alphanumeric: " + randomAlphaNumeric); // e.g., "aB5cY2x9Pq"
    ```

2.  **विशिष्ट लंबाई की रैंडम अल्फाबेटिक स्ट्रिंग जनरेट करें:**

    ```java
    String randomAlphabetic = RandomStringUtils.randomAlphabetic(8);
    System.out.println("Random alphabetic: " + randomAlphabetic); // e.g., "GhJkLmNo"
    ```

3.  **विशिष्ट लंबाई की रैंडम न्यूमेरिक स्ट्रिंग जनरेट करें:**

    ```java
    String randomNumeric = RandomStringUtils.randomNumeric(6);
    System.out.println("Random numeric: " + randomNumeric); // e.g., "123456"
    ```

4.  **अक्षरों और नंबरों के मिश्रण वाली रैंडम स्ट्रिंग जनरेट करें, फ्लैग्स निर्दिष्ट करते हुए:**

    ```java
    String randomLettersAndNumbers = RandomStringUtils.random(12, true, true);
    System.out.println("Random letters and numbers: " + randomLettersAndNumbers); // e.g., "abC123DeF456"
    ```

5.  **कस्टम करैक्टर सेट से रैंडम स्ट्रिंग जनरेट करें:**

    ```java
    String chars = "abcdefg";
    String randomFromCustomSet = RandomStringUtils.random(5, chars);
    System.out.println("Random from custom set: " + randomFromCustomSet); // e.g., "gcfae"
    ```

## `pom.xml` में कौन सी लाइब्रेरी उपयोग करें

Maven प्रोजेक्ट में `RandomStringUtils` का उपयोग करने के लिए, आपको अपनी `pom.xml` फाइल में `commons-lang3` डिपेंडेंसी ऐड करनी होगी।

यहां डिपेंडेंसी स्निपेट दी गई है:

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.14.0</version> </dependency>
```

**महत्वपूर्ण नोट्स:**

  * **वर्जन:** `commons-lang3` के नवीनतम स्टेबल वर्जन के लिए हमेशा [Maven Central](https://mvnrepository.com/artifact/org.apache.commons/commons-lang3) चेक करें। मेरे आखिरी अपडेट के अनुसार, `3.14.0` या उससे ऊपर एक अच्छा विकल्प है, लेकिन उपलब्ध नवीनतम स्टेबल वर्जन का उपयोग करना सबसे अच्छा होता है।
  * **स्कोप:** डिपेंडेंसी के लिए डिफॉल्ट स्कोप `compile` होता है, जो आमतौर पर इस तरह की यूटिलिटी लाइब्रेरीज के लिए आपको चाहिए होता है। इसका मतलब है कि JAR कंपाइलेशन, टेस्टिंग और रनटाइम के दौरान उपलब्ध रहेगा। यदि आप इसका उपयोग केवल टेस्टिंग के लिए कर रहे होते, तो आप `<scope>test</scope>` का उपयोग कर सकते थे।
  * **डिप्रिकेशन:** ध्यान दें कि Apache Commons Lang 3 के नए वर्जन में `RandomStringUtils.randomAlphabetic(int count)` जैसी कुछ पुरानी मेथड्स डिप्रिकेटेड हैं। इसके बजाय, `secure()`, `secureStrong()`, या `insecure()` मेथड्स का उपयोग करने की सिफारिश की जाती है, जो रैंडमनेस सोर्स पर अधिक कंट्रोल प्रदान करते हैं। उदाहरण के लिए, `RandomStringUtils.secure().nextAlphanumeric(10)`। हालांकि, कई उपयोग के मामलों के लिए पुरानी मेथड्स अभी भी काम करती हैं।