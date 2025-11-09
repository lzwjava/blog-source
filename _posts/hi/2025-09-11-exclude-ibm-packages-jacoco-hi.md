---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hi
layout: post
model: mistralai/mistral-medium-3.1
title: जैकोको में आईबीएम पैकेजों को बाहर करें
translated: true
type: note
---

**`com.ibm`** पैकेजों (या किसी अन्य पैकेजों) को **WebSphere Liberty Profile** वातावरण में JaCoCo कवरेज से बाहर करने के लिए, आप अपनी **`pom.xml`** फ़ाइल में बहिष्करण कॉन्फ़िगर कर सकते हैं। यह आमतौर पर **JaCoCo Maven प्लगइन** कॉन्फ़िगरेशन में किया जाता है।

---

### **`pom.xml` में `com.ibm` पैकेजों को बाहर करने का तरीका**

आप कवरेज रिपोर्टिंग से किन classes या packages को बाहर रखा जाना चाहिए, यह निर्दिष्ट करने के लिए JaCoCo प्लगइन कॉन्फ़िगरेशन में `<excludes>` टैग का उपयोग कर सकते हैं।

#### **उदाहरण कॉन्फ़िगरेशन:**

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.11</version> <!-- नवीनतम संस्करण का उपयोग करें -->
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
                    <configuration>
                        <outputDirectory>${project.reporting.outputDirectory}/jacoco</outputDirectory>
                        <excludes>
                            <!-- सभी com.ibm packages को बाहर करें -->
                            <exclude>com/ibm/**</exclude>
                        </excludes>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

---

### **स्पष्टीकरण:**
- **`<excludes>`**: यह सेक्शन निर्दिष्ट करता है कि किन classes या packages को कवरेज रिपोर्टिंग से बाहर रखा जाना चाहिए।
- **`<exclude>com/ibm/**</exclude>`**: यह `com.ibm` पैकेज और उसके सब-पैकेजों के अंतर्गत आने वाली सभी classes को बाहर कर देता है।

---

### **अतिरिक्त नोट्स:**
- यदि आप एक से अधिक packages को बाहर करना चाहते हैं, तो और `<exclude>` एंट्रीज जोड़ें:
  ```xml
  <excludes>
      <exclude>com/ibm/**</exclude>
      <exclude>org/apache/**</exclude>
  </excludes>
  ```
- यदि आप **JaCoCo को WebSphere Liberty के साथ** उपयोग कर रहे हैं, तो सुनिश्चित करें कि JaCoCo एजेंट आपकी `server.env` या `jvm.options` फ़ाइल में ठीक से कॉन्फ़िगर है, और `pom.xml` में बहिष्करण आपकी आवश्यकताओं के अनुरूप हैं।

---

### **सर्वोत्तम अभ्यास:**
- एक कवरेज रिपोर्ट चलाकर और जाँच करके हमेशा बहिष्करण को सत्यापित करें कि बहिष्कृत packages परिणामों में शामिल नहीं हैं।
- यदि आपको रनटाइम पर packages को बाहर करने की आवश्यकता है (उदाहरण के लिए, JaCoCo एजेंट arguments में), तो आप एजेंट arguments में `excludes` पैरामीटर का उपयोग कर सकते हैं:
  ```plaintext
  -javaagent:/path/to/jacocoagent.jar=destfile=/path/to/jacoco.exec,excludes=com.ibm.*
  ```