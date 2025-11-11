---
audio: false
generated: true
lang: hi
layout: post
title: 'मेवेन चेकस्टाइल: स्कैनिंग जारी रखें'
translated: true
type: note
---

`mvn checkstyle:check` को सभी मॉड्यूल्स का स्कैन जारी रखने के लिए, जो उल्लंघनों पर पहले ही फेल होने से रोकता है, आपको Checkstyle Maven प्लगइन को `failOnViolation` विकल्प को अक्षम करने के लिए कॉन्फ़िगर करना होगा। डिफ़ॉल्ट रूप से, `failOnViolation` `true` पर सेट होता है, जो बिल्ड को उल्लंघन मिलते ही रोक देता है। इसे `false` पर सेट करने से स्कैन सभी मॉड्यूल्स में पूरा हो पाता है, और सभी उल्लंघनों की रिपोर्ट किए बिना बिल्ड रुकता नहीं है।

### समाधान
अपनी `pom.xml` को निम्नलिखित तरीके से Checkstyle प्लगइन को कॉन्फ़िगर करने के लिए अपडेट करें:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-checkstyle-plugin</artifactId>
      <version>3.3.1</version> <!-- नवीनतम वर्जन का उपयोग करें -->
      <configuration>
        <failOnViolation>false</failOnViolation>
        <logViolationsToConsole>true</logViolationsToConsole> <!-- वैकल्पिक: उल्लंघनों को कंसोल पर लॉग करता है -->
      </configuration>
      <executions>
        <execution>
          <id>checkstyle</id>
          <phase>validate</phase> <!-- या आपका पसंदीदा फेज -->
          <goals>
            <goal>check</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

### व्याख्या
- **`<failOnViolation>false</failOnViolation>`**: यह सेटिंग बिल्ड को Checkstyle उल्लंघनों का पता चलने पर फेल होने से रोकती है, जिससे स्कैन सभी मॉड्यूल्स में जारी रह पाता है।
- **`<logViolationsToConsole>true</logViolationsToConsole>`**: (वैकल्पिक) सुनिश्चित करता है कि उल्लंघन दृश्यता के लिए कंसोल पर प्रिंट होते हैं, भले ही बिल्ड फेल न हो।
- **एक्जिक्यूशन फेज**: `<phase>validate</phase>` Checkstyle चेक को Maven लाइफसाइकल के `validate` फेज से बांधता है। यदि आप इसे किसी अलग स्टेज (जैसे, `compile`, `verify`) पर चलाना चाहते हैं, तो फेज को एडजस्ट करें।

### कमांड चलाना
कमांड को फिर से चलाएं:
```bash
mvn checkstyle:check
```
`failOnViolation` को `false` पर सेट करने के साथ, Maven सभी मॉड्यूल्स को स्कैन करेगा, सभी उल्लंघनों की रिपोर्ट करेगा और बिल्ड को बीच में रोके बिना पूरा करेगा।

### नोट्स
- सुनिश्चित करें कि आप `maven-checkstyle-plugin` के एक हाल के वर्जन (जैसा कि 3.3.1 दिखाया गया है) का उपयोग कर रहे हैं। यदि आवश्यक हो तो Maven Central पर नवीनतम वर्जन की जांच करें।
- यदि आप मल्टी-मॉड्यूल प्रोजेक्ट में काम कर रहे हैं, तो यह कॉन्फ़िगरेशन सभी मॉड्यूल्स पर लागू होगी, जब तक कि चाइल्ड `pom.xml` में इसे ओवरराइड न किया गया हो।
- उल्लंघनों की एक रिपोर्ट जनरेट करने के लिए, इसके बजाय `mvn checkstyle:checkstyle` चलाने पर विचार करें, जो डिफ़ॉल्ट रूप से बिल्ड को फेल किए बिना एक HTML रिपोर्ट तैयार करता है।

यदि आपकी कोई विशिष्ट आवश्यकताएं हैं (जैसे, कस्टम Checkstyle नियम या कोई अलग सेटअप), तो मुझे बताएं, और मैं समाधान को और अनुकूलित कर सकता हूं!