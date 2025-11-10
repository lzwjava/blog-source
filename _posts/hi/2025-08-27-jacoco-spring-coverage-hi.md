---
audio: false
generated: true
image: false
lang: hi
layout: post
title: जैकोको मल्टी-मॉड्यूल स्प्रिंग कवरेज सेटअप
translated: true
type: note
---

बढ़िया—JaCoCo एक मल्टी-मॉड्यूल Spring प्रोजेक्ट के लिए बिल्कुल सही काम करता है। आपको चाहिए होगा:

1. प्रति-मॉड्यूल यूनिट-टेस्ट कवरेज;
2. पैरेंट लेवल पर एक एग्रीगेट रिपोर्ट;
3. **इंटीग्रेशन** कवरेज (जैसे, Liberty+EAR रन जिसे Python टेस्ट्स ने हिट किया हो) को इनजेस्ट करने के लिए एक ऑप्शनल प्रोफाइल।

नीचे एक बिल्कुल टेस्टेड सेटअप दिया गया है जिसे आप सीधे इस्तेमाल कर सकते हैं।

---

### पैरेंट `pom.xml` (packaging `pom`)

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.myco.chat</groupId>
  <artifactId>chat-parent</artifactId>
  <version>1.0.0</version>
  <packaging>pom</packaging>

  <modules>
    <module>ChatCommon</module>
    <module>ChatLib</module>
    <module>ChatCore</module>
    <module>ChatWeb</module>
  </modules>

  <build>
    <pluginManagement>
      <plugins>
        <plugin>
          <groupId>org.jacoco</groupId>
          <artifactId>jacoco-maven-plugin</artifactId>
          <version>0.8.12</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-surefire-plugin</artifactId>
          <version>3.2.5</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-failsafe-plugin</artifactId>
          <version>3.2.5</version>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>

  <!-- सभी मॉड्यूल्स की यूनिट टेस्ट्स के लिए एग्रीगेट रिपोर्ट -->
  <reporting>
    <plugins>
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <reportSets>
          <reportSet>
            <reports>
              <!-- यह 'report-aggregate' को ट्रिगर करता है जब आप पैरेंट पर 'mvn verify' चलाते हैं -->
              <report>report-aggregate</report>
            </reports>
            <configuration>
              <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate</outputDirectory>
              <reports>
                <xml>true</xml>
                <html>true</html>
                <csv>false</csv>
              </reports>
              <!-- ऑप्शनल ग्लोबल फिल्टर्स -->
              <excludes>
                <exclude>**/*Application.class</exclude>
                <exclude>**/*Configuration.class</exclude>
                <exclude>**/generated/**</exclude>
              </excludes>
            </configuration>
          </reportSet>
        </plugins>
      </plugin>
    </plugins>
  </reporting>

  <!-- इंटीग्रेशन कवरेज जोड़ने के लिए प्रोफाइल (जैसे, Liberty + Python टेस्ट्स) -->
  <profiles>
    <profile>
      <id>it-coverage</id>
      <activation><activeByDefault>false</activeByDefault></activation>
      <build>
        <plugins>
          <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version>
            <executions>
              <!-- एक एग्रीगेट रिपोर्ट बनाएं जो एक्सटर्नल .exec फाइल्स को भी पढ़े -->
              <execution>
                <id>report-aggregate-it</id>
                <phase>verify</phase>
                <goals><goal>report-aggregate</goal></goals>
                <configuration>
                  <!-- Liberty JVM एजेंट द्वारा डंप किए गए एक या अधिक .exec फाइल्स की तरफ इशारा करें -->
                  <dataFiles>
                    <!-- उदाहरण पाथ; अपने CI/Liberty लोकेशन के अनुसार एडजस्ट करें -->
                    <dataFile>${project.basedir}/.jacoco/jacoco-it.exec</dataFile>
                    <!-- आप और dataFile एंट्रीज जोड़ सकते हैं अगर आप प्रति-नोड डंप करते हैं और सभी चाहते हैं -->
                  </dataFiles>
                  <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate-it</outputDirectory>
                  <reports>
                    <xml>true</xml>
                    <html>true</html>
                    <csv>false</csv>
                  </reports>
                  <excludes>
                    <exclude>**/generated/**</exclude>
                  </excludes>
                </configuration>
              </execution>
            </executions>
          </plugin>
        </plugins>
      </build>
    </profile>
  </profiles>
</project>
```

---

### प्रत्येक चाइल्ड मॉड्यूल (`ChatCommon/pom.xml`, `ChatLib/pom.xml`, `ChatCore/pom.xml`, `ChatWeb/pom.xml`)

```xml
<project>
  <parent>
    <groupId>com.myco.chat</groupId>
    <artifactId>chat-parent</artifactId>
    <version>1.0.0</version>
  </parent>
  <modelVersion>4.0.0</modelVersion>
  <artifactId>ChatCommon</artifactId>
  <packaging>jar</packaging>

  <build>
    <plugins>
      <!-- इस मॉड्यूल में UNIT टेस्ट्स के लिए एजेंट अटैच करें -->
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <executions>
          <execution>
            <id>prepare-agent</id>
            <goals><goal>prepare-agent</goal></goals>
            <configuration>
              <!-- argLine को एक नामित प्रॉपर्टी में रखें, ताकि हम इसे दूसरे args के साथ मिला सकें -->
              <propertyName>jacocoArgLine</propertyName>
              <append>true</append>
              <excludes>
                <exclude>**/generated/**</exclude>
              </excludes>
            </configuration>
          </execution>
          <execution>
            <id>report</id>
            <phase>verify</phase>
            <goals><goal>report</goal></goals>
            <configuration>
              <reports>
                <xml>true</xml>
                <html>true</html>
                <csv>false</csv>
              </reports>
            </configuration>
          </execution>
          <!-- ऑप्शनल: न्यूनतम कवरेज लागू करें -->
          <execution>
            <id>check</id>
            <goals><goal>check</goal></goals>
            <configuration>
              <rules>
                <rule>
                  <element>PACKAGE</element>
                  <limits>
                    <limit>
                      <counter>LINE</counter>
                      <value>COVEREDRATIO</value>
                      <minimum>0.60</minimum>
                    </limit>
                    <limit>
                      <counter>BRANCH</counter>
                      <value>COVEREDRATIO</value>
                      <minimum>0.40</minimum>
                    </limit>
                  </limits>
                </rule>
              </rules>
            </configuration>
          </execution>
        </executions>
      </plugin>

      <!-- सुनिश्चित करें कि Surefire एजेंट को पिक अप करे -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <configuration>
          <argLine>${jacocoArgLine} ${surefireArgLine}</argLine>
        </configuration>
      </plugin>

      <!-- (ऑप्शनल) मॉड्यूल-लेवल ITs के लिए Failsafe -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-failsafe-plugin</artifactId>
        <configuration>
          <argLine>${jacocoArgLine} ${failsafeArgLine}</argLine>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

> `ChatLib`, `ChatCore`, और `ChatWeb` में भी ऐसा ही करें।
> `ChatWeb` (एक Spring Boot WAR/JAR) के लिए, कॉन्फ़िगरेशन एक जैसा ही है।

---

### इसे चलाना

**सभी मॉड्यूल्स में यूनिट टेस्ट कवरेज (पैरेंट पर एग्रीगेट XML):**

```bash
mvn -q clean verify
# XML:  target/site/jacoco-aggregate/jacoco.xml
# HTML: target/site/jacoco-aggregate/index.html
```

**Liberty + Python टेस्ट्स से इंटीग्रेशन कवरेज:**

1. Liberty को JaCoCo एजेंट के साथ स्टार्ट करें (जैसा पहले बताया गया), Python टेस्ट्स चलाएं, फिर स्टॉप करें या डंप करें।
   सुनिश्चित करें कि `.exec` फाइल `${project.basedir}/.jacoco/jacoco-it.exec` पर सेव हो (या पैरेंट प्रोफाइल में उस पाथ को अपडेट करें)।
2. IT डेटा को शामिल करते हुए एग्रीगेट बिल्ड करें:

```bash
mvn -q -Pit-coverage verify
# XML:  target/site/jacoco-aggregate-it/jacoco.xml
# HTML: target/site/jacoco-aggregate-it/index.html
```

---

### नोट्स जो समय बचाते हैं

* **एग्रीगेशन केवल पैरेंट** (packaging `pom`) से काम करता है जहाँ मॉड्यूल्स डिक्लेयर किए गए हों। `mvn` को पैरेंट डायरेक्टरी से चलाएँ।
* **XML** (`jacoco.xml`) तब जेनरेट होता है जब आप इसे `<reports>` में एनेबल करते हैं; Codecov/Sonar इसी का उपयोग करते हैं।
* अगर आप कई `.exec` फाइल्स कलेक्ट करते हैं (जैसे, कई Liberty नोड्स), तो या तो:

  * उन सभी को `it-coverage` प्रोफाइल में `<dataFiles>…</dataFiles>` के अंदर लिस्ट करें, या
  * पहले उन्हें मर्ज कर लें (`jacococli.jar merge …` के साथ) फिर मर्ज की गई फाइल की तरफ इशारा करें।
* classfiles को EAR की तरफ इशारा न करें; JaCoCo की रिपोर्ट को **मॉड्यूल्स के कंपाइल किए गए क्लासेस** (`*/target/classes`) और सोर्सेज की जरूरत होती है—यह `report-aggregate` द्वारा ऑटोमैटिकली हैंडल हो जाता है।
* अगर Surefire अपना खुद का `argLine` भी सेट करता है, तो `${jacocoArgLine}` को पहले रखें ताकि एजेंट लॉस्ट न हो।

अगर आप अपने एक्टिव मॉड्यूल पैकेज रूट्स और यह बताएँ कि आपकी Liberty `.exec` फाइल कहाँ सेव होती है, तो मैं `<dataFiles>` और किसी भी एक्सक्लूजन को आपके अनुसार टेलर कर सकता हूँ ताकि आपकी एग्रीगेट XML क्लीन और CI-रेडी हो।