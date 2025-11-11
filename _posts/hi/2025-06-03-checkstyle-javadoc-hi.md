---
audio: false
generated: true
lang: hi
layout: post
title: चेकस्टाइल में जावाडॉक जांच अक्षम करें
translated: true
type: note
---

Checkstyle को सभी Javadoc-संबंधित जांचों को अनदेखा करने और उन्हें उल्लंघन न मानने के लिए कॉन्फ़िगर करने के लिए, आपको अपनी Checkstyle कॉन्फ़िगरेशन फ़ाइल (आमतौर पर `checkstyle.xml`) को या तो Javadoc-संबंधित मॉड्यूल को अक्षम करने या दबाने के लिए संशोधित करना होगा। यहां बताया गया है कि आप इसे कैसे कर सकते हैं:

### विकल्प 1: Javadoc-संबंधित जांचें अक्षम करें
Checkstyle में कई Javadoc-संबंधित मॉड्यूल हैं, जैसे `JavadocMethod`, `JavadocType`, `JavadocVariable`, `JavadocStyle`, और `JavadocPackage`। इन्हें अक्षम करने के लिए, सुनिश्चित करें कि ये मॉड्यूल आपकी कॉन्फ़िगरेशन फ़ाइल में या तो हटा दिए गए हैं या टिप्पणी में डाल दिए गए हैं। उदाहरण के लिए:

```xml
<module name="Checker">
    <!-- अन्य मॉड्यूल -->
    <!-- Javadoc-संबंधित जांचों को टिप्पणी में डालें या हटा दें -->
    <!--
    <module name="JavadocMethod"/>
    <module name="JavadocType"/>
    <module name="JavadocVariable"/>
    <module name="JavadocStyle"/>
    <module name="JavadocPackage"/>
    -->
</module>
```

यदि ये मॉड्यूल आपकी कॉन्फ़िगरेशन में मौजूद नहीं हैं, तो Checkstyle Javadoc जांचें लागू नहीं करेगा।

### विकल्प 2: Suppression Filters का उपयोग करके Javadoc जांचों को दबाएं
आप अपने पूरे कोडबेस में सभी Javadoc-संबंधित जांचों को दबाने के लिए Checkstyle के `SuppressionFilter` का उपयोग कर सकते हैं। एक अलग दमन फ़ाइल (जैसे, `suppressions.xml`) में एक दमन नियम जोड़ें और इसे अपनी Checkstyle कॉन्फ़िगरेशन में संदर्भित करें।

1. **एक दमन फ़ाइल बनाएं** (जैसे, `suppressions.xml`):
   ```xml
   <!DOCTYPE suppressions PUBLIC
       "-//Checkstyle//DTD Suppression DTD 1.0//EN"
       "https://checkstyle.org/dtds/suppressions_1_0.dtd">
   <suppressions>
       <!-- सभी Javadoc-संबंधित जांचों को दबाएं -->
       <suppress checks="Javadoc.*" files=".*"/>
   </suppressions>
   ```

   `checks="Javadoc.*"` पैटर्न "Javadoc" से शुरू होने वाली सभी जांचों (जैसे, `JavadocMethod`, `JavadocType`, आदि) से मेल खाता है, और `files=".*"` दमन को सभी फ़ाइलों पर लागू करता है।

2. **अपनी Checkstyle कॉन्फ़िगरेशन में दमन फ़ाइल को संदर्भित करें**:
   ```xml
   <module name="Checker">
       <module name="SuppressionFilter">
           <property name="file" value="suppressions.xml"/>
       </module>
       <!-- अन्य मॉड्यूल -->
   </module>
   ```

### विकल्प 3: `@SuppressWarnings` एनोटेशन का उपयोग करें
यदि आप विशिष्ट कक्षाओं या विधियों के लिए Javadoc जांचों को दबाना चाहते हैं, तो आप अपने Java कोड में `@SuppressWarnings("checkstyle:javadoc")` एनोटेशन का उपयोग कर सकते हैं। उदाहरण के लिए:

```java
@SuppressWarnings("checkstyle:javadoc")
public class MyClass {
    // Javadoc के बिना कोड उल्लंघन नहीं ट्रिगर करेगा
}
```

यह दृष्टिकोण लक्षित दमन के लिए उपयोगी है लेकिन इसके लिए कोड में एनोटेशन जोड़ने की आवश्यकता होती है, जो Javadoc जांचों को वैश्विक रूप से अक्षम करने के लिए आदर्श नहीं हो सकता है।

### नोट्स
- **अपनी कॉन्फ़िगरेशन सत्यापित करें**: कॉन्फ़िगरेशन संशोधित करने के बाद, यह सुनिश्चित करने के लिए Checkstyle चलाएं कि Javadoc-संबंधित उल्लंघन अब रिपोर्ट नहीं किए जाते हैं। उदाहरण के लिए, कमांड का उपयोग करें:
  ```bash
  java -jar checkstyle.jar -c checkstyle.xml YourSourceFiles
  ```
- **सामान्य Javadoc मॉड्यूल**: सुनिश्चित करें कि आप सभी प्रासंगिक मॉड्यूलों को संबोधित करते हैं, जिनमें `JavadocMethod`, `JavadocType`, `JavadocVariable`, `JavadocStyle`, `JavadocPackage`, `MissingJavadocMethod`, `MissingJavadocType`, और `InvalidJavadocPosition` शामिल हैं।
- **Checkstyle संस्करण**: सटीक मॉड्यूल नाम और दमन सिंटैक्स आपके Checkstyle संस्करण के आधार पर थोड़े भिन्न हो सकते हैं। उपरोक्त उदाहरण Checkstyle 8.x और बाद के संस्करणों के साथ संगत हैं।
- **वैश्विक दमन**: `SuppressionFilter` दृष्टिकोण (विकल्प 2) आमतौर पर मूल कॉन्फ़िगरेशन में व्यापक संशोधन किए बिना सभी Javadoc जांचों को अक्षम करने का सबसे साफ़ तरीका है।

यदि आप कोई विशिष्ट बिल्ड टूल जैसे Maven या Gradle उपयोग कर रहे हैं, तो मुझे बताएं, और मैं अद्यतन Checkstyle कॉन्फ़िगरेशन को एकीकृत करने के लिए अतिरिक्त मार्गदर्शन प्रदान कर सकता हूं!