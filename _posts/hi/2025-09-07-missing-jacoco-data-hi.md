---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hi
layout: post
title: जैकोको एक्ज़िक्यूशन डेटा फ़ाइल का समाधान
translated: true
type: note
---

JaCoCo एक्ज़िक्यूशन डेटा फ़ाइल जनरेट करने के लिए, जिसे अक्सर **'.exec' फ़ाइल** कहा जाता है, आपको JaCoCo एजेंट को संलग्न करके अपने टेस्ट चलाने होंगे। "Skipping JaCoCo execution due to missing execution data file" लॉग संदेश इंगित करता है कि `report` गोल को `prepare-agent` गोल के सफलतापूर्वक चलाए बिना ही एक्ज़िक्यूट किया गया है।

-----

### चरण 1: JaCoCo Maven प्लगइन कॉन्फ़िगर करें

सबसे पहले, सुनिश्चित करें कि आपकी `pom.xml` फ़ाइल में JaCoCo Maven प्लगइन ठीक से कॉन्फ़िगर है। यह कुछ इस तरह दिखनी चाहिए:

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.12</version>
    <executions>
        <execution>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
        </execution>
        <execution>
            <id>report</id>
            <phase>test</phase>
            <goals>
                <goal>report</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

**`prepare-agent`** गोल महत्वपूर्ण है क्योंकि यह JaCoCo रनटाइम एजेंट को सेट अप करता है। यह एजेंट टेस्ट रन के दौरान कवरेज डेटा एकत्र करने के लिए आपके कोड को इंस्ट्रूमेंट करता है।

-----

### चरण 2: टेस्ट चलाएं

प्लगइन कॉन्फ़िगर करने के बाद, अपना Maven बिल्ड चलाएं। टेस्ट चलाने और रिपोर्ट जनरेट करने के लिए आमतौर पर निम्नलिखित कमांड दी जाती है:

`mvn clean install`

जब आप यह कमांड चलाते हैं, तो Maven सबसे पहले `prepare-agent` गोल को एक्ज़िक्यूट करता है, जो JVM से JaCoCo एजेंट को संलग्न करता है। फिर, जब `test` फेज चलती है, तो एजेंट कोड कवरेज डेटा रिकॉर्ड करता है और इसे आमतौर पर **`target/jacoco.exec`** पथ पर स्थित एक फ़ाइल में सेव कर देता है। इसके बाद `report` गोल एक्ज़िक्यूट होता है, जो इस `.exec` फ़ाइल को पढ़ता है और अंतिम HTML या XML रिपोर्ट जनरेट करता है।

यदि आपको अभी भी समस्या आ रही है, तो निम्नलिखित बातों की जाँच करें:

  * **प्रोजेक्ट संरचना**: सुनिश्चित करें कि आपके टेस्ट स्टैंडर्ड Maven डायरेक्टरी `src/test/java` में स्थित हैं।
  * **टेस्ट फेलियर**: यदि आपके टेस्ट फेल हो रहे हैं, तो बिल्ड `.exec` फ़ाइल जनरेट होने से पहले ही रुक सकता है। पहले किसी भी टेस्ट फेलियर को ठीक करें।
  * **वर्जन मिसमैच**: सुनिश्चित करें कि JaCoCo प्लगइन का वर्जन आपके Maven और Java वर्जन के साथ संगत है।