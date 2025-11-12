---
audio: false
generated: true
lang: hi
layout: post
title: जैकोको मेवन प्लगइन
translated: true
type: note
---

यहाँ **JaCoCo Maven प्लगइन का उपयोग कैसे करें** पर एक चरण-दर-चरण मार्गदर्शिका दी गई है, जो एक Maven-आधारित Java प्रोजेक्ट में code coverage मापने के लिए है। JaCoCo (Java Code Coverage) एक टूल है जो Maven के साथ एकीकृत होकर यह ट्रैक करता है कि आपका कोड टेस्ट, आमतौर पर यूनिट टेस्ट, द्वारा कितना execute होता है। अपने प्रोजेक्ट में JaCoCo Maven प्लगइन को जोड़कर और कॉन्फ़िगर करके, आप बिल्ड प्रक्रिया के दौरान विस्तृत coverage रिपोर्ट generate कर सकते हैं।

---

### **JaCoCo Maven प्लगइन का उपयोग करने के चरण**

#### **1. अपने `pom.xml` में JaCoCo Maven प्लगइन जोड़ें**
JaCoCo Maven प्लगइन का उपयोग करने के लिए, आपको इसे अपने प्रोजेक्ट की `pom.xml` फ़ाइल के `<build><plugins>` सेक्शन में शामिल करना होगा। नीचे एक बुनियादी कॉन्फ़िगरेशन दी गई है जो प्लगइन को सेट अप करती है:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version> <!-- उपलब्ध नवीनतम संस्करण का उपयोग करें -->
            <executions>
                <execution>
                    <goals>
                        <goal>prepare-agent</goal>
                    </goals>
                </execution>
                <execution>
                    <id>report</id>
                    <phase>verify</phase>
                    <goals>
                        <goal>report</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`groupId`, `artifactId`, और `version`**: ये JaCoCo Maven प्लगइन की पहचान करते हैं। `0.8.12` को [Maven Central Repository](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin) पर उपलब्ध नवीनतम संस्करण से बदलें।
- **`<executions>`**: यह सेक्शन कॉन्फ़िगर करता है कि Maven बिल्ड लाइफसाइकल के दौरान प्लगइन कब और कैसे चलता है:
  - **`<goal>prepare-agent</goal>`**: टेस्ट execution के दौरान coverage डेटा एकत्र करने के लिए JaCoCo एजेंट को तैयार करता है। डिफ़ॉल्ट रूप से, यह एक शुरुआती फेज (जैसे `initialize`) से बंधा होता है और कस्टमाइज़ किए जाने तक एक स्पष्ट फेज की आवश्यकता नहीं होती है।
  - **`<goal>report</goal>`**: टेस्ट चलने के बाद coverage रिपोर्ट generate करता है। यह यहाँ `verify` फेज से बंधा है, जो `test` फेज के बाद होता है, यह सुनिश्चित करता है कि सभी टेस्ट डेटा उपलब्ध है।

#### **2. सुनिश्चित करें कि टेस्ट कॉन्फ़िगर हैं**
JaCoCo प्लगइन टेस्ट execution का विश्लेषण करके काम करता है, आमतौर पर Maven Surefire Plugin द्वारा चलाए गए यूनिट टेस्ट। अधिकांश Maven प्रोजेक्ट्स में, Surefire डिफ़ॉल्ट रूप से शामिल होता है और `src/test/java` में स्थित टेस्ट चलाता है। जब तक आपके टेस्ट गैर-मानक नहीं हैं, तब तक किसी अतिरिक्त कॉन्फ़िगरेशन की आवश्यकता नहीं है। सत्यापित करें कि:
- आपके पास यूनिट टेस्ट लिखे गए हैं (जैसे, JUnit या TestNG का उपयोग करके)।
- Surefire प्लगइन मौजूद है (अधिकांश मामलों में यह डिफ़ॉल्ट Maven parent POM से विरासत में मिला होता है)।

यदि आपको Surefire को स्पष्ट रूप से कॉन्फ़िगर करने की आवश्यकता है, तो यह इस तरह दिख सकता है:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.0</version> <!-- नवीनतम संस्करण का उपयोग करें -->
</plugin>
```

`prepare-agent` गोल `argLine` प्रॉपर्टी को संशोधित करके JaCoCo एजेंट को सेट अप करता है, जिसका उपयोग Surefire coverage ट्रैकिंग सक्षम करके टेस्ट चलाने के लिए करता है।

#### **3. Maven बिल्ड चलाएँ**
Coverage रिपोर्ट generate करने के लिए, अपने प्रोजेक्ट डायरेक्टरी में निम्नलिखित कमांड execute करें:

```bash
mvn verify
```

- **`mvn verify`**: यह `verify` तक के सभी फेज चलाता है, जिसमें `compile`, `test`, और `verify` शामिल हैं। JaCoCo प्लगइन:
  1. टेस्ट चलने से पहले एजेंट को तैयार करेगा।
  2. `test` फेज (जब Surefire टेस्ट execute करता है) के दौरान coverage डेटा एकत्र करेगा।
  3. `verify` फेज के दौरान रिपोर्ट generate करेगा।

वैकल्पिक रूप से, यदि आप केवल `verify` पर आगे बढ़े बिना टेस्ट चलाना चाहते हैं, तो उपयोग करें:

```bash
mvn test
```

हालाँकि, चूंकि इस कॉन्फ़िगरेशन में `report` गोल `verify` से बंधा है, इसलिए रिपोर्ट देखने के लिए आपको `mvn verify` चलाना होगा। यदि आप चाहते हैं कि रिपोर्ट `mvn test` के दौरान generate हो, तो आप `report` execution के लिए `<phase>` को `test` में बदल सकते हैं, हालाँकि `verify` एक आम परंपरा है।

#### **4. Coverage रिपोर्ट देखें**
`mvn verify` चलाने के बाद, JaCoCo डिफ़ॉल्ट रूप से एक HTML रिपोर्ट generate करता है। आप इसे यहाँ पा सकते हैं:

```
target/site/jacoco/index.html
```

- इस फ़ाइल को वेब ब्राउज़र में खोलें ताकि code coverage का विस्तृत विवरण देख सकें, जिसमें पैकेज, क्लास, मेथड और लाइन के लिए प्रतिशत शामिल हैं।
- रिपोर्ट में समान डायरेक्टरी (`jacoco.xml` और `jacoco.csv`) में XML और CSV फॉर्मेट भी शामिल हैं, जो CI सिस्टम जैसे टूल के साथ एकीकरण के लिए उपयोगी हैं।

---

### **वैकल्पिक अनुकूलन**
अधिक उन्नत उपयोग के मामलों के लिए, आप प्लगइन कॉन्फ़िगरेशन को ट्वीक कर सकते हैं:

- **क्लास या पैकेज बाहर करें**:
  Coverage विश्लेषण से कुछ कोड (जैसे, जेनरेट किया गया कोड) को बाहर करने के लिए, एक `<configuration>` सेक्शन जोड़ें:

  ```xml
  <configuration>
      <excludes>
          <exclude>**/generated/**/*</exclude>
      </excludes>
  </configuration>
  ```

  इसे `<executions>` के ऊपर, `<plugin>` टैग के अंदर रखें।

- **Coverage थ्रेशोल्ड लागू करें**:
  यदि coverage एक निश्चित सीमा से नीचे गिरती है तो बिल्ड को फेल करने के लिए, `check` गोल जोड़ें:

  ```xml
  <execution>
      <id>check</id>
      <phase>verify</phase>
      <goals>
          <goal>check</goal>
      </goals>
      <configuration>
          <rules>
              <rule>
                  <element>BUNDLE</element>
                  <limits>
                      <limit>
                          <counter>LINE</counter>
                          <value>COVEREDRATIO</value>
                          <minimum>0.80</minimum> <!-- 80% लाइन कवरेज -->
                      </limit>
                  </limits>
              </rule>
          </rules>
      </configuration>
  </execution>
  ```

- **रिपोर्ट आउटपुट डायरेक्टरी बदलें**:
  रिपोर्ट लोकेशन को कस्टमाइज़ करने के लिए, जोड़ें:

  ```xml
  <configuration>
      <destFile>${project.build.directory}/custom-jacoco.exec</destFile>
      <dataFile>${project.build.directory}/custom-jacoco.exec</dataFile>
      <outputDirectory>${project.build.directory}/custom-reports</outputDirectory>
  </configuration>
  ```

---

### **सारांश**
JaCoCo Maven प्लगइन का उपयोग करने के लिए:
1. अपने `pom.xml` में `prepare-agent` और `report` गोल के साथ प्लगइन जोड़ें।
2. सुनिश्चित करें कि आपके प्रोजेक्ट में टेस्ट कॉन्फ़िगर हैं (आमतौर पर Surefire के माध्यम से)।
3. Coverage रिपोर्ट generate करने के लिए `mvn verify` चलाएँ।
4. `target/site/jacoco/index.html` पर रिपोर्ट जांचें।

यह सेटअप आपकी Maven बिल्ड प्रक्रिया में code coverage को एकीकृत करने का एक सीधा तरीका प्रदान करता है, जो आपके टेस्ट की प्रभावशीलता का आकलन करने में आपकी सहायता करता है। नवीनतम प्लगइन संस्करण या उन्नत कॉन्फ़िगरेशन के लिए, [आधिकारिक JaCoCo दस्तावेज़ीकरण](https://www.jacoco.org/jacoco/trunk/doc/maven.html) देखें।