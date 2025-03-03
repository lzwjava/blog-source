---
audio: false
generated: true
lang: hi
layout: post
title: JaCoCo Maven Plugin का उपयोग
translated: true
---

यह एक चरण-दर-चरण मार्गदर्शिका है **JaCoCo Maven प्लगइन** का उपयोग करके एक Maven आधारित Java प्रोजेक्ट में कोड कवरेज मापने के लिए। JaCoCo (Java Code Coverage) एक टूल है जो Maven के साथ इंटीग्रेट होता है ताकि यह ट्रैक कर सके कि आपकी कितनी कोड टेस्टों द्वारा एक्सरसाइज की जाती है, आम तौर पर यूनिट टेस्ट्स। JaCoCo Maven प्लगइन को अपने प्रोजेक्ट में जोड़कर और कॉन्फ़िगर करके, आप बिल्ड प्रोसेस के दौरान विस्तृत कवरेज रिपोर्ट्स जनरेट कर सकते हैं।

---

### **JaCoCo Maven प्लगइन का उपयोग करने के चरण**

#### **1. JaCoCo Maven प्लगइन को `pom.xml` में जोड़ें**
JaCoCo Maven प्लगइन का उपयोग करने के लिए, आपको इसे अपने प्रोजेक्ट के `pom.xml` फ़ाइल के `<build><plugins>` सेक्शन में शामिल करना होगा। नीचे एक बेसिक कॉन्फ़िगरेशन दिया गया है जो प्लगइन को सेट अप करता है:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version> <!-- उपलब्ध सबसे नया संस्करण का उपयोग करें -->
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

- **`groupId`, `artifactId`, और `version`**: ये JaCoCo Maven प्लगइन को पहचानते हैं। `0.8.12` को [Maven Central Repository](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin) पर उपलब्ध सबसे नया संस्करण से बदलें।
- **`<executions>`**: यह सेक्शन कॉन्फ़िगर करता है कि प्लगइन Maven बिल्ड लाइफसाइकिल के दौरान कब और कैसे चलता है:
  - **`<goal>prepare-agent</goal>`**: JaCoCo एजेंट को टेस्ट एक्ज़ीक्यूशन के दौरान कवरेज डेटा को इकट्ठा करने के लिए तैयार करता है। डिफ़ॉल्ट में, यह एक अर्ली फेज (जैसे `initialize`) से बाइंड होता है और किसी स्पेशल फेज के लिए एक्सप्लिसिट फेज की आवश्यकता नहीं होती है जब तक कि इसे कस्टमाइज़ नहीं किया गया है।
  - **`<goal>report</goal>`**: टेस्ट्स चलने के बाद कवरेज रिपोर्ट जनरेट करता है। यह `verify` फेज से बाइंड है, जो `test` फेज के बाद होता है, जिससे सभी टेस्ट डेटा उपलब्ध हो जाता है।

#### **2. टेस्ट्स कॉन्फ़िगर किए गए हैं, यह सुनिश्चित करें**
JaCoCo प्लगइन टेस्ट एक्ज़ीक्यूशन का विश्लेषण करके काम करता है, आम तौर पर Maven Surefire प्लगइन द्वारा चलाए गए यूनिट टेस्ट्स। अधिकांश Maven प्रोजेक्टों में, Surefire डिफ़ॉल्ट में शामिल होता है और `src/test/java` में स्थित टेस्ट्स को चलाता है। कोई अतिरिक्त कॉन्फ़िगरेशन की आवश्यकता नहीं होती है जब तक कि आपके टेस्ट्स नॉन-स्टैंडर्ड नहीं हैं। सुनिश्चित करें कि:
- आपके पास यूनिट टेस्ट्स लिखे गए हैं (जैसे, JUnit या TestNG का उपयोग करके).
- Surefire प्लगइन मौजूद है (यह अधिकांश मामलों में डिफ़ॉल्ट Maven पेरेंट POM से विरासत में मिलता है).

अगर आपको Surefire को स्पेशल रूप से कॉन्फ़िगर करना है, तो यह इस तरह दिख सकता है:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.0</version> <!-- सबसे नया संस्करण का उपयोग करें -->
</plugin>
```

`prepare-agent` गोल `argLine` प्रॉपर्टी को बदलकर JaCoCo एजेंट को सेट अप करता है, जो Surefire टेस्ट्स को कवरेज ट्रैकिंग के साथ चलाने के लिए उपयोग करता है।

#### **3. Maven बिल्ड चलाएं**
कवरेज रिपोर्ट जनरेट करने के लिए, अपने प्रोजेक्ट डायरेक्टरी में निम्न कमांड चलाएं:

```bash
mvn verify
```

- **`mvn verify`**: यह `verify` तक सभी फेज चलाता है, जिसमें `compile`, `test`, और `verify` शामिल हैं। JaCoCo प्लगइन:
  1. टेस्ट्स चलने से पहले एजेंट को तैयार करता है।
  2. `test` फेज (जब Surefire टेस्ट्स चलाता है) के दौरान कवरेज डेटा इकट्ठा करता है।
  3. `verify` फेज के दौरान रिपोर्ट जनरेट करता है।

अल्टर्नेटिव रूप में, अगर आप केवल टेस्ट्स चलाना चाहते हैं बिना `verify` तक जाने, तो:

```bash
mvn test
```

हालाँकि, इस कॉन्फ़िगरेशन में `report` गोल `verify` से बाइंड है, इसलिए आपको रिपोर्ट देखने के लिए `mvn verify` चलाना होगा। अगर आप रिपोर्ट को `mvn test` के दौरान जनरेट करना चाहते हैं, तो आप `report` एक्ज़ीक्यूशन के लिए `<phase>` को `test` में बदल सकते हैं, हालाँकि `verify` एक आम परंपरा है।

#### **4. कवरेज रिपोर्ट देखें**
`mvn verify` चलाने के बाद, JaCoCo डिफ़ॉल्ट में एक HTML रिपोर्ट जनरेट करता है। आप इसे यहाँ पा सकते हैं:

```
target/site/jacoco/index.html
```

- इस फ़ाइल को एक वेब ब्राउज़र में खोलें ताकि पैकेज, क्लास, मेथड, और लाइनों के लिए कवरेज का विस्तृत ब्रेकडाउन देखें।
- रिपोर्ट में XML और CSV फॉर्मेट भी उसी डायरेक्टरी में (`jacoco.xml` और `jacoco.csv`) शामिल हैं, जो CI सिस्टम जैसे टूल्स के साथ इंटीग्रेशन के लिए उपयोगी हैं।

---

### **वैकल्पिक कस्टमाइज़ेशन**
अधिक उन्नत उपयोग के लिए, आप प्लगइन कॉन्फ़िगरेशन को ट्यूक कर सकते हैं:

- **क्लास या पैकेज को छोड़ें**:
  कवरेज विश्लेषण से कुछ कोड को छोड़ने के लिए (जैसे, जनरेटेड कोड), एक `<configuration>` सेक्शन जोड़ें:

  ```xml
  <configuration>
      <excludes>
          <exclude>**/generated/**/*</exclude>
      </excludes>
  </configuration>
  ```

  इसे `<plugin>` टैग के अंदर, `<executions>` के ऊपर रखें।

- **कवरेज थ्रेशोल्ड लागू करें**:
  अगर कवरेज एक थ्रेशोल्ड से नीचे गिर जाता है, तो बिल्ड को फेल करने के लिए `check` गोल जोड़ें:

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
  रिपोर्ट स्थान को कस्टमाइज़ करने के लिए, जोड़ें:

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
1. `pom.xml` में प्लगइन को `prepare-agent` और `report` गोल्स के साथ जोड़ें।
2. सुनिश्चित करें कि आपके प्रोजेक्ट में टेस्ट्स कॉन्फ़िगर किए गए हैं (आम तौर पर Surefire के माध्यम से).
3. `mvn verify` चलाएं ताकि कवरेज रिपोर्ट जनरेट हो सके।
4. रिपोर्ट को `target/site/jacoco/index.html` पर चेक करें।

इस सेटअप ने कोड कवरेज को अपने Maven बिल्ड प्रोसेस में एक सरल तरीके से इंटीग्रेट करने की सुविधा प्रदान की, जिससे आप अपने टेस्ट्स की प्रभावशीलता का मूल्यांकन कर सकते हैं। सबसे नए प्लगइन संस्करण या उन्नत कॉन्फ़िगरेशन के लिए, [अधिकारिक JaCoCo दस्तावेज़](https://www.jacoco.org/jacoco/trunk/doc/maven.html) पर संदर्भ करें।