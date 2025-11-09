---
audio: false
date: 2025-09-10
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: मेवेन में एंगुलर बिल्ड को छोड़ना
translated: true
type: note
---

संक्षिप्त उत्तर: हाँ—आप Angular/npm बिल्ड को छोड़ सकते हैं, लेकिन `--skip-web` जैसे बिल्ट-इन फ्लैग के साथ नहीं। इनमें से किसी एक तरीके का उपयोग करें।

### 1) मल्टी-मॉड्यूल बिल्ड में वेब मॉड्यूल को बाहर करें

यदि आपका Angular ऐप अपना स्वयं का Maven मॉड्यूल है (जैसे, `web`), तो रिएक्टर में इसे बाहर कर दें:

```
mvn -pl '!web' -am clean package
```

या केवल बैकएंड मॉड्यूल बनाएं:

```
mvn -pl :backend -am clean package
```

(`-am` आवश्यक डिपेंडेंसी बनाता है; `!web` सिंटैक्स उस मॉड्यूल को बाहर करता है।)

### 2) एक "skip frontend" प्रॉपर्टी जोड़ें (frontend-maven-plugin या exec के साथ काम करता है)

npm गोल्स को एक प्रॉपर्टी से गार्ड करें और कमांड लाइन से इसे फ्लिप करें।

**POM (वेब मॉड्यूल या पैरेंट):**

```xml
<properties>
  <skip.frontend>false</skip.frontend>
</properties>

<build>
  <plugins>
    <!-- उदाहरण: com.github.eirslett:frontend-maven-plugin -->
    <plugin>
      <groupId>com.github.eirslett</groupId>
      <artifactId>frontend-maven-plugin</artifactId>
      <version>...your version...</version>
      <configuration>
        <skip>${skip.frontend}</skip>
      </configuration>
      <executions>
        <execution>
          <id>npm-build</id>
          <phase>prepare-package</phase>
          <goals>
            <goal>npm</goal>
          </goals>
          <configuration>
            <arguments>run build</arguments>
          </configuration>
        </execution>
      </executions>
    </plugin>

    <!-- यदि आप npm को कॉल करने के लिए exec-maven-plugin का उपयोग करते हैं -->
    <plugin>
      <groupId>org.codehaus.mojo</groupId>
      <artifactId>exec-maven-plugin</artifactId>
      <version>...your version...</version>
      <executions>
        <execution>
          <id>npm-build</id>
          <phase>prepare-package</phase>
          <goals><goal>exec</goal></goals>
          <configuration>
            <skip>${skip.frontend}</skip>
            <executable>npm</executable>
            <arguments>
              <argument>run</argument>
              <argument>build</argument>
            </arguments>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

**CLI:**

```
mvn -Dskip.frontend=true clean package
```

### 3) Maven प्रोफाइल्स का उपयोग करें

फ्रंटएंड बिल्ड को केवल एक "with-frontend" प्रोफाइल में बांधें और डेव में एक "skip-frontend" प्रोफाइल को डिफ़ॉल्ट बनाएं।

**POM:**

```xml
<profiles>
  <profile>
    <id>with-frontend</id>
    <activation>
      <property>
        <name>!skip.frontend</name>
      </property>
    </activation>
    <build>
      <plugins>
        <!-- skip के बिना ऊपर जैसी ही प्लगइन कॉन्फ़िगरेशन -->
      </plugins>
    </build>
  </profile>
</profiles>
```

**CLI:**

* सामान्य (स्किप करें): `mvn -Dskip.frontend clean package`
* रिलीज़ (UI बनाएं): `mvn -Pwith-frontend clean package`

---

## स्पीड टिप्स यदि आप *UI बनाते* हैं

* सुनिश्चित करें कि Angular का persistent cache चालू है (Angular CLI डिफ़ॉल्ट रूप से कैश करता है; CI में `node_modules` और `.angular/cache` को कैश्ड रखें)।
* रिलीज़ के लिए केवल `ng build` चलाएं; डेव में, UI को अलग से सर्व करें (`npm start`) और Spring को प्रीबिल्ट स्टैटिक एसेट्स सर्व करने दें (जैसे, पैकेज्ड बिल्ड्स के लिए `dist/` को `src/main/resources/static` के अंतर्गत रखें)।
* रिपो को विभाजित करने पर विचार करें ताकि Angular ऐप Maven मॉड्यूल बिल्कुल न हो; इसे केवल तब बनाएं जब फ्रंटएंड फाइलें बदलती हैं।
* यदि आप हाल के Angular पर हैं, तो डिफ़ॉल्ट esbuild/Vite बिल्डर का उपयोग करें और CI रिलीज़ बिल्ड्स में सोर्स मैप्स को डिसेबल रखें।

---

### निष्कर्ष

वेब मॉड्यूल को बाहर करने के लिए `-pl '!web'` का उपयोग करें, **या** एक `skip.frontend` प्रॉपर्टी जोड़ें और अपनी प्लगइन एक्ज़िक्यूशन्स को इसका सम्मान करने के लिए वायर करें। कोई मानक `mvn package --skip-web` नहीं है, लेकिन ऊपर दिए गए दो पैटर्न विश्वसनीय और सामान्य हैं।