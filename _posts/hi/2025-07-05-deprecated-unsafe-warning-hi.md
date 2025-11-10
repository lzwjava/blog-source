---
audio: false
generated: true
lang: hi
layout: post
title: गुइस को अपग्रेड करके अनसेफ चेतावनी ठीक करें
translated: true
type: note
---

आपको जो चेतावनी दिखाई दे रही है:

```
WARNING: A terminally deprecated method in sun.misc.Unsafe has been called
WARNING: sun.misc.Unsafe::staticFieldBase has been called by com.google.inject.internal.aop.HiddenClassDefiner (file:/opt/homebrew/Cellar/maven/3.9.10/libexec/lib/guice-5.1.0-classes.jar)
WARNING: Please consider reporting this to the maintainers of class com.google.inject.internal.aop.HiddenClassDefiner
WARNING: sun.misc.Unsafe::staticFieldBase will be removed in a future release
```

यह **Java Virtual Machine (JVM) से एक चेतावनी है**, सीधे तौर पर आपके कोड से नहीं। इसका मतलब है कि आपके द्वारा उपयोग किया जा रहा एक लाइब्रेरी (इस मामले में, Guice, विशेष रूप से `guice-5.1.0-classes.jar`) आंतरिक रूप से `sun.misc.Unsafe` से एक मेथड (`staticFieldBase`) को कॉल कर रहा है।

`sun.misc.Unsafe` Java में एक आंतरिक API है, जो JDK के भीतर ही निम्न-स्तरीय ऑपरेशन्स के लिए होता है। यह मानक Java API का हिस्सा नहीं है और इसके उपयोग को हतोत्साहित किया जाता है क्योंकि इससे अस्थिर या अपरिभाषित व्यवहार हो सकता है और यह भविष्य के Java रिलीज़ में बदलने या हटाए जाने के अधीन है। JVM आपको एक संकेत दे रहा है कि यह विशेष मेथड "terminally deprecated" है और इसे हटा दिया जाएगा, जिसका मतलब है कि यह अंततः आपके एप्लिकेशन को तोड़ देगा यदि लाइब्रेरी बिना किसी विकल्प के इसका उपयोग जारी रखती है।

**इस चेतावनी को "हटाने" के लिए:**

आप इसे सीधे तौर पर अपना कोड बदलकर "हटा" नहीं सकते, क्योंकि इसका उपयोग एक तृतीय-पक्ष लाइब्रेरी (Guice) के भीतर है। यहां वह सूची दी गई है जो आप कर सकते हैं, प्राथमिकता के क्रम में:

1.  **Guice को अपग्रेड करें (सबसे अनुशंसित):**
    सबसे अच्छा और स्थायी समाधान Guice के एक नए वर्जन में अपग्रेड करना है जो अब `sun.misc.Unsafe` का उपयोग नहीं करता या मानक Java APIs जैसे `VarHandle` (JDK 9 में पेश किया गया) या Foreign Function & Memory API (JEP 454, JDK 22 में मानक) में माइग्रेट कर चुका है।

    वर्जन `guice-5.1.0-classes.jar` को देखते हुए, ऐसा लगता है कि आप Guice 5.1.0 का उपयोग कर रहे हैं। नए Java वर्जन पर `sun.misc.Unsafe` के उपयोग को विशेष रूप से संबोधित करने वाले अपडेट्स के लिए आधिकारिक Guice रिलीज़ और उनके डॉक्यूमेंटेशन को चेक करें। अक्सर, लाइब्रेरी मेंटेनर्स इन डिप्रिकेशन के बारे में जागरूक होते हैं और अपडेटेड वर्जन प्रदान करते हैं।

      * **कार्यवाही:** अपने `pom.xml` को नए Guice वर्जन का उपयोग करने के लिए संशोधित करें। आपको Guice का नवीनतम स्थिर वर्जन ढूंढना होगा जो आपके Java वर्जन (आपके मामले में JDK 21) के साथ संगत हो।

    ```xml
    <dependency>
        <groupId>com.google.inject</groupId>
        <artifactId>guice</artifactId>
        <version>LATEST_GUICE_VERSION</version> </dependency>
    ```

    यदि आपका प्रोजेक्ट उनका उपयोग करता है तो आपको `guice-assistedinject` या अन्य Guice मॉड्यूल शामिल करने की आवश्यकता हो सकती है।

2.  **चेतावनी को दबाएं (अस्थायी वर्कअराउंड - दीर्घकालिक अनुशंसित नहीं):**
    जबकि आपको इस पर लंबे समय तक भरोसा नहीं करना चाहिए, आप रनटाइम पर चेतावनी को दबा सकते हैं यदि यह विशुद्ध रूप से कॉस्मेटिक है और *अभी के लिए* आपके एप्लिकेशन की कार्यक्षमता में बाधा नहीं डालती है। यह JVM कमांड-लाइन आर्गुमेंट्स के माध्यम से किया जाता है।

    JDK 24 के लिए (आपका वर्तमान लक्ष्य 21 है, लेकिन जैसे-जैसे Java आगे बढ़ेगा यह जानना अच्छा है), डिफ़ॉल्ट `warn` है। इसे दबाने के लिए, आप इसे स्पष्ट रूप से `allow` पर सेट कर सकते हैं:

    आप इसे अपने `exec-maven-plugin` कॉन्फ़िगरेशन में जोड़ सकते हैं:

    ```xml
    <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>3.5.0</version>
        <configuration>
            <executable>bash</executable>
            <arguments>
                <argument>-c</argument>
                <argument>java --add-opens java.base/sun.misc=ALL-UNNAMED --sun-misc-unsafe-memory-access=allow -cp ${project.build.directory}/classes com.lzw.solutions.uva.${problem}.Main &lt; src/main/resources/uva/${problem}/1.in</argument>
            </arguments>
        </configuration>
    </plugin>
    ```

    *स्व-सुधार:* प्राथमिक चेतावनी "terminally deprecated" होने के बारे में है, illegal reflective access के बारे में नहीं। इसलिए, `--add-opens java.base/sun.misc=ALL-UNNAMED` यहां आवश्यक नहीं हो सकता है जब तक कि आपको "Illegal reflective access" की चेतावनियां भी नहीं मिल रही हों। "terminally deprecated" चेतावनी के लिए अधिक प्रत्यक्ष फ्लैग `--sun-misc-unsafe-memory-access=allow` है।

    **हालाँकि, यह एक अस्थायी ठीक है।** यह फ्लैग केवल JVM को चेतावनी प्रिंट किए बिना `sun.misc.Unsafe` मेथड्स के उपयोग की अनुमति देने के लिए कहता है। यह अंतर्निहित समस्या को *हल नहीं करता* कि `sun.misc.Unsafe` को अंततः हटा दिया जाएगा, और आपका एप्लिकेशन भविष्य के JDK वर्जन में काम करना बंद कर सकता है।

3.  **Guice मेंटेनर्स को रिपोर्ट करें (चेतावनी द्वारा पहले ही सुझाया गया):**
    चेतावनी स्वयं सुझाव देती है "कृपया इसे क्लास `com.google.inject.internal.aop.HiddenClassDefiner` के मेंटेनर्स को रिपोर्ट करने पर विचार करें।" हालाँकि आप एक विशिष्ट वर्जन का उपयोग कर रहे हैं, यदि आप पुष्टि कर सकते हैं कि यह समस्या नवीनतम Guice वर्जन में बनी रहती है (जो संभावित रूप से नहीं होनी चाहिए, क्योंकि वे इन्हें संबोधित करते हैं), तो इसे रिपोर्ट करना समुदाय के लिए फायदेमंद होगा।

**संक्षेप में, सबसे अच्छा तरीका यह है कि आप अपनी Guice डिपेंडेंसी को अपग्रेड करें।** `sun.misc.Unsafe` API एक चलती-फिरती लक्ष्य है, और लाइब्रेरीज़ को Java द्वारा प्रदान किए गए नए, सुरक्षित और आधिकारिक रूप से समर्थित APIs के अनुकूल होने की आवश्यकता है।