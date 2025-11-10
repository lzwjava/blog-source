---
audio: false
generated: true
lang: hi
layout: post
title: इंडेंटेशन डिटेक्टिंग इन चेकस्टाइल
translated: true
type: note
---

मुझे लगता है कि आप सोच रहे हैं कि Checkstyle आपकी `logAfter` मेथड में `System.out.println` स्टेटमेंट से पहले गायब इंडेंटेशन को क्यों नहीं पकड़ रहा है। आइए इस मुद्दे को पहचानने और ठीक करने के लिए चरण दर चरण विश्लेषण करते हैं।

### Checkstyle को इंडेंटेशन समस्या का पता क्यों नहीं चल रहा है?
Checkstyle कोडिंग मानकों को लागू करने के लिए विशिष्ट मॉड्यूल का उपयोग करता है, और इंडेंटेशन के लिए, यह `Indentation` मॉड्यूल पर निर्भर करता है। यदि यह मॉड्यूल आपके Checkstyle सेटअप में ठीक से कॉन्फ़िगर या शामिल नहीं है, तो यह आपके कोड में मौजूद इंडेंटेशन त्रुटियों का पता नहीं लगा पाएगा।

आपका वर्तमान कोड यहाँ है:

```java
package org.lzwjava;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class DebugAspect {
    @After("execution(* org.lzwjava..*(..))")
    public void logAfter(JoinPoint joinPoint) {
    System.out.println("Method executed: " + joinPoint.getSignature());  // No indentation
    }
}
```

मानक Java conventions में, एक मेथड के अंदर की स्टेटमेंट्स (जैसे `System.out.println`) को मेथड डिक्लेरेशन के सापेक्ष इंडेंट किया जाना चाहिए। आपके कोड में, `System.out.println` लाइन में कोई इंडेंटेशन नहीं है, जिसे Checkstyle को एक त्रुटि के रूप में चिह्नित करना चाहिए यदि वह ठीक से कॉन्फ़िगर है। यहाँ सबसे संभावित कारण बताए गए हैं कि यह पता क्यों नहीं चल रहा है:

1. **`Indentation` मॉड्यूल आपकी Checkstyle कॉन्फ़िगरेशन फ़ाइल** (जैसे `checks.xml`) में **शामिल नहीं है**।
2. **मॉड्यूल शामिल है लेकिन गलत तरीके से कॉन्फ़िगर है**, इसलिए यह अपेक्षित इंडेंटेशन नियमों को लागू नहीं कर रहा है।
3. **आपकी कॉन्फ़िगरेशन कुछ फ़ाइलों या पैकेजों को बाहर कर रही है**, जिससे यह चेक इस कोड पर चल नहीं पा रही है।
4. **Checkstyle को चलाने के तरीके में कोई समस्या है** (जैसे Maven या IDE के माध्यम से), जो अपेक्षित व्यवहार को ओवरराइड कर रहा है।

आइए इन संभावनाओं को संबोधित करें और इसे काम करने दें।

---

### चरण 1: अपनी कॉन्फ़िगरेशन में `Indentation` मॉड्यूल सत्यापित करें
सबसे पहले, अपनी Checkstyle कॉन्फ़िगरेशन फ़ाइल (संभवतः `checks.xml`) जांचें कि क्या `Indentation` मॉड्यूल शामिल है। यहाँ बताया गया है कि कैसे:

1. **अपनी `checks.xml` फ़ाइल का पता लगाएं**। यह आमतौर पर आपके प्रोजेक्ट डायरेक्टरी में होती है (जैसे `/home/lzw/Projects/blog-server/checks.xml` अगर आप ऐसे सेटअप का उपयोग कर रहे हैं)।
2. **`TreeWalker` सेक्शन के अंदर `Indentation` मॉड्यूल देखें**। यह इस तरह दिखना चाहिए:

   ```xml
   <module name="TreeWalker">
       <!-- अन्य चेक -->
       <module name="Indentation">
           <property name="basicOffset" value="4"/>  <!-- प्रति इंडेंटेशन लेवल 4 स्पेस -->
           <property name="lineWrappingIndentation" value="4"/>  <!-- वैकल्पिक: रैप की गई लाइनों के लिए -->
       </module>
       <!-- अन्य चेक -->
   </module>
   ```

   - **यदि आपको यह मॉड्यूल नहीं दिखता**, तो यही समस्या है—Checkstyle इंडेंटेशन की जाँच बिल्कुल नहीं कर रहा है।
   - **यदि यह मौजूद है**, तो जांचें कि `basicOffset` एक उचित मान पर सेट है (जैसे 4 स्पेस, जो Java के लिए मानक है)।

---

### चरण 2: `Indentation` मॉड्यूल जोड़ें या ठीक करें
यदि मॉड्यूल गायब है या सही तरीके से सेट नहीं है, तो इसे ठीक करने का तरीका यहाँ बताया गया है:

#### यदि यह गायब है: `Indentation` मॉड्यूल जोड़ें
अपनी `checks.xml` के `TreeWalker` सेक्शन के अंदर निम्नलिखित जोड़ें:

```xml
<module name="Indentation">
    <property name="basicOffset" value="4"/>  <!-- 4 स्पेस विशिष्ट है -->
    <property name="lineWrappingIndentation" value="4"/>
</module>
```

#### यदि यह मौजूद है: सेटिंग्स सत्यापित करें
सुनिश्चित करें:
- `basicOffset` आपके अपेक्षित इंडेंटेशन के लिए स्पेस की संख्या पर सेट है (जैसे 4)।
- कोई भी प्रॉपर्टी चेक को डिसेबल या ओवरराइड नहीं कर रही है जिससे आपका कोड स्किप हो जाए।

परिवर्तन करने के बाद फ़ाइल सेव करें।

---

### चरण 3: बहिष्करण के लिए जांचें
कभी-कभी, Checkstyle कॉन्फ़िगरेशन कुछ फ़ाइलों या पैकेजों को बाहर कर देती है। अपनी `checks.xml` में देखें:
- एक `SuppressionFilter` या `SuppressionCommentFilter` जो `org.lzwjava` पैकेज या इस विशिष्ट फ़ाइल को स्किप कर सकता है।
- कोई भी पैटर्न जो `.java` फ़ाइलों या विशिष्ट डायरेक्टरी को बाहर करता है।

यदि आपको अपने कोड को प्रभावित करने वाला ऐसा बहिष्करण मिलता है, तो उसे हटा दें या समायोजित करें ताकि `DebugAspect.java` की जाँच की जा सके।

---

### चरण 4: फिक्स का परीक्षण करें
अपनी कॉन्फ़िगरेशन अपडेट करने के बाद, Checkstyle को फिर से चलाएँ। यदि आप Maven का उपयोग कर रहे हैं, उदाहरण के लिए:

```bash
mvn clean checkstyle:check
```

आउटपुट जांचें। आपको इस तरह की त्रुटि दिखनी चाहिए:

```
[ERROR] DebugAspect.java:13: 'System.out.println' should be indented +4 spaces relative to its enclosing block.
```

यह संकेत देगा कि Checkstyle अब गायब इंडेंटेशन का पता लगा रहा है। संदर्भ के लिए, उचित इंडेंटेशन के साथ आपका कोड कैसा दिखना *चाहिए*:

```java
@Aspect
@Component
public class DebugAspect {
    @After("execution(* org.lzwjava..*(..))")
    public void logAfter(JoinPoint joinPoint) {
        System.out.println("Method executed: " + joinPoint.getSignature());  // 4 स्पेस इंडेंट
    }
}
```

---

### चरण 5: यदि यह अभी भी काम नहीं करता है तो समस्या निवारण
यदि Checkstyle अभी भी समस्या को फ्लैग नहीं करता है:
- **डीबग आउटपुट के साथ चलाएँ**: यह देखने के लिए कि Checkstyle क्या कर रहा है, एक विस्तृत कमांड का उपयोग करें:
  ```bash
  mvn -X checkstyle:check
  ```
  `Indentation` मॉड्यूल या स्किप की गई फ़ाइलों के बारे में संदेशों के लिए देखें।
- **एक न्यूनतम कॉन्फ़िगरेशन के साथ परीक्षण करें**: केवल `Indentation` चेक के साथ एक अस्थायी `checks.xml` बनाएँ:
  ```xml
  <?xml version="1.0"?>
  <!DOCTYPE module PUBLIC
      "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
      "https://checkstyle.org/dtds/configuration_1_3.dtd">
  <module name="Checker">
      <module name="TreeWalker">
          <module name="Indentation">
              <property name="basicOffset" value="4"/>
          </module>
      </module>
  </module>
  ```
  Checkstyle को इस फ़ाइल की ओर इंगित करें और समस्या को अलग करने के लिए फिर से परीक्षण करें।
- **अपना सेटअप जांचें**: यदि आप किसी IDE (जैसे IntelliJ या Eclipse) के माध्यम से Checkstyle चला रहे हैं, तो सुनिश्चित करें कि IDE अपडेट किए गए `checks.xml` का उपयोग कर रहा है न कि कोई पुरानी या अलग कॉन्फ़िगरेशन।

---

### निष्कर्ष
Checkstyle गायब इंडेंटेशन का पता नहीं लगा रहा है क्योंकि `Indentation` मॉड्यूल संभवतः आपके `checks.xml` में गायब या गलत तरीके से कॉन्फ़िगर है। इस मॉड्यूल को जोड़कर या सही करके और यह सुनिश्चित करके कि कोई बहिष्करण लागू नहीं होता है, Checkstyle को `System.out.println` से पहले इंडेंटेशन की कमी को फ्लैग करना चाहिए। अपनी कॉन्फ़िगरेशन को दिखाए अनुसार अपडेट करें, Checkstyle को फिर से चलाएँ, और आपको त्रुटि की अपेक्षा के अनुसार रिपोर्ट दिखनी चाहिए। यदि आपको अगले चरणों में सहायता की आवश्यकता हो तो मुझे बताएं!