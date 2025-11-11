---
audio: false
generated: true
lang: hi
layout: post
title: स्पॉटलेस का उपयोग कर कोड फॉर्मेट करना
translated: true
type: note
---

Maven Checkstyle Plugin में `mvn checkstyle:format` कमांड नहीं है। यह प्लगइन मुख्य रूप से कोड को Checkstyle कॉन्फ़िगरेशन के विरुद्ध जांचने और उल्लंघनों की रिपोर्ट करने के लिए डिज़ाइन किया गया है, न कि कोड को स्वचालित रूप से फ़ॉर्मेट करने के लिए। हालाँकि, आप Spotless या Maven Formatter Plugin जैसे अन्य टूल्स का उपयोग करके, जिन्हें आपके Checkstyle नियमों के साथ संरेखित करने के लिए कॉन्फ़िगर किया जा सकता है, Checkstyle कॉन्फ़िगरेशन के आधार पर कोड फ़ॉर्मेटिंग प्राप्त कर सकते हैं।

नीचे, मैं समझाऊंगा कि कैसे **Spotless Maven Plugin** का उपयोग करके अपने Checkstyle कॉन्फ़िगरेशन के आधार पर कोड फ़ॉर्मेट करें, क्योंकि यह इस उद्देश्य के लिए एक लोकप्रिय विकल्प है और Checkstyle नियमों के साथ एकीकृत हो सकता है।

### समाधान: Checkstyle कॉन्फ़िगरेशन के साथ Spotless का उपयोग करना

Spotless Maven Plugin, Checkstyle कॉन्फ़िगरेशन फ़ाइल (जैसे, `checkstyle.xml`) के अनुसार Java कोड को फ़ॉर्मेट कर सकता है। इसे सेट अप करने का तरीका यहां बताया गया है:

#### 1. अपने `pom.xml` में Spotless जोड़ें
अपने `pom.xml` में Spotless प्लगइन जोड़ें और इसे अपनी Checkstyle कॉन्फ़िगरेशन फ़ाइल का उपयोग करने के लिए कॉन्फ़िगर करें।

```xml
<build>
  <plugins>
    <plugin>
      <groupId>com.diffplug.spotless</groupId>
      <artifactId>spotless-maven-plugin</artifactId>
      <version>2.43.0</version> <!-- नवीनतम संस्करण का उपयोग करें -->
      <configuration>
        <java>
          <!-- अपनी Checkstyle कॉन्फ़िगरेशन फ़ाइल की ओर इशारा करें -->
          <googleJavaFormat>
            <version>1.22.0</version> <!-- वैकल्पिक: एक विशिष्ट संस्करण का उपयोग करें -->
            <style>GOOGLE</style> <!-- या AOSP, या डिफ़ॉल्ट के लिए छोड़ दें -->
          </googleJavaFormat>
          <formatAnnotations>
            <!-- फ़ॉर्मेटिंग के लिए Checkstyle कॉन्फ़िगरेशन का उपयोग करें -->
            <checkstyle>
              <file>${project.basedir}/checkstyle.xml</file> <!-- आपके Checkstyle कॉन्फ़िग का पथ -->
              <version>10.17.0</version> <!-- अपने Checkstyle संस्करण से मेल खाएं -->
            </checkstyle>
          </formatAnnotations>
        </java>
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>apply</goal> <!-- कोड को स्वचालित रूप से फ़ॉर्मेट करता है -->
          </goals>
          <phase>process-sources</phase> <!-- वैकल्पिक: एक चरण से बांधें -->
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

#### 2. सुनिश्चित करें कि आपका Checkstyle कॉन्फ़िगरेशन मौजूद है
सुनिश्चित करें कि आपकी प्रोजेक्ट में एक `checkstyle.xml` फ़ाइल है (जैसे, रूट डायरेक्टरी या किसी सबडायरेक्टरी में)। यह फ़ाइल कोडिंग मानकों (जैसे, इंडेंटेशन, व्हाइटस्पेस, आदि) को परिभाषित करती है जिनका उपयोग Spotless आपके कोड को फ़ॉर्मेट करने के लिए करेगा। यदि आप Google Java Format जैसे मानक का उपयोग कर रहे हैं, तो आप इसका संदर्भ दे सकते हैं, या अपनी प्रोजेक्ट के लिए तैयार कस्टम Checkstyle कॉन्फ़िगरेशन का उपयोग कर सकते हैं।

बुनियादी फ़ॉर्मेटिंग नियमों के लिए `checkstyle.xml` स्निपेट का उदाहरण:
```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN" "https://checkstyle.sourceforge.io/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="TreeWalker">
    <module name="Indentation">
      <property name="basicOffset" value="2"/>
      <property name="braceAdjustment" value="0"/>
    </module>
  </module>
</module>
```

#### 3. कोड फ़ॉर्मेट करने के लिए Spotless चलाएं
अपने Checkstyle कॉन्फ़िगरेशन के आधार पर अपने कोड को फ़ॉर्मेट करने के लिए, चलाएं:
```bash
mvn spotless:apply
```

यह कमांड आपकी प्रोजेक्ट की सभी Java फ़ाइलों को आपके Checkstyle कॉन्फ़िगरेशन में परिभाषित नियमों और किसी भी अतिरिक्त फ़ॉर्मेटिंग सेटिंग्स (जैसे, Google Java Format) के अनुसार फ़ॉर्मेट करेगी।

#### 4. Checkstyle के साथ फ़ॉर्मेटिंग सत्यापित करें
फ़ॉर्मेटिंग के बाद, यह सत्यापित करने के लिए कि फ़ॉर्मेट किया गया कोड आपके Checkstyle नियमों का अनुपालन करता है, आप `mvn checkstyle:check` चला सकते हैं। यदि आपने `<failOnViolation>false</failOnViolation>` सेट करने के पिछले सुझाव का पालन किया है, तो यह बिल्ड को रोके बिना किसी भी शेष उल्लंघन की रिपोर्ट करेगा।

### विकल्प: Maven Formatter Plugin
यदि आप Spotless का उपयोग नहीं करना चाहते हैं, तो आप **Maven Formatter Plugin** का उपयोग कर सकते हैं, जो नियमों के आधार पर फ़ॉर्मेटिंग का समर्थन भी करता है लेकिन सीधे Checkstyle कॉन्फ़िगरेशन के साथ कम इस्तेमाल किया जाता है। यहां एक बुनियादी सेटअप दिया गया है:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>net.revelc.code.formatter</groupId>
      <artifactId>formatter-maven-plugin</artifactId>
      <version>2.23.0</version> <!-- नवीनतम संस्करण का उपयोग करें -->
      <configuration>
        <configFile>${project.basedir}/checkstyle.xml</configFile> <!-- Checkstyle कॉन्फ़िग का पथ -->
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>format</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

फ़ॉर्मेटिंग इसके साथ चलाएं:
```bash
mvn formatter:format
```

### नोट्स
- **कोई सीधी Checkstyle फ़ॉर्मेट कमांड नहीं**: Checkstyle Maven Plugin एक `format` लक्ष्य प्रदान नहीं करता है। Checkstyle नियमों के आधार पर फ़ॉर्मेटिंग लागू करने के लिए Spotless या Formatter Plugin जैसे टूल्स की आवश्यकता होती है।
- **Checkstyle संस्करण संगतता**: सुनिश्चित करें कि Spotless (या Formatter) में निर्दिष्ट Checkstyle संस्करण आपके Checkstyle प्लगइन में उपयोग किए गए संस्करण से मेल खाता हो ताकि नियम बेमेल होने से बचा जा सके।
- **कस्टम Checkstyle नियम**: Spotless द्वारा उन्हें सही ढंग से लागू करने के लिए, आपके `checkstyle.xml` में फ़ॉर्मेटिंग-संबंधी नियम (जैसे, `Indentation`, `WhitespaceAround`, आदि) शामिल होने चाहिए।
- **मल्टी-मॉड्यूल प्रोजेक्ट्स**: एक मल्टी-मॉड्यूल Maven प्रोजेक्ट में, आप Spotless/Formatter कॉन्फ़िगरेशन को पैरेंट `pom.xml` में रख सकते हैं ताकि इसे सभी मॉड्यूल में लागू किया जा सके, या आवश्यकतानुसार प्रति मॉड्यूल कॉन्फ़िगर कर सकते हैं।
- **फ़ॉर्मेटिंग के बाद जांचें**: अनुपालन की पुष्टि करने के लिए, विशेष रूप से यदि आपके Checkstyle कॉन्फ़िगरेशन में गैर-फ़ॉर्मेटिंग नियम (जैसे, मेथड लंबाई, जटिलता) हैं, तो हमेशा फ़ॉर्मेटिंग के बाद `mvn checkstyle:check` चलाएं।

यदि आपके पास `checkstyle.xml` नहीं है या इसे बनाने में सहायता की आवश्यकता है, तो मुझे बताएं, और मैं एक नमूना प्रदान कर सकता हूं या आपको आगे मार्गदर्शन कर सकता हूं! साथ ही, यदि आप कोई अलग टूल पसंद करते हैं या आपकी कोई विशिष्ट फ़ॉर्मेटिंग आवश्यकताएं हैं, तो कृपया साझा करें, और मैं समाधान को समायोजित कर दूंगा।