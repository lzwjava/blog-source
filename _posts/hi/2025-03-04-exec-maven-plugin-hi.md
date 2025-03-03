---
audio: false
generated: true
lang: hi
layout: post
title: Maven Plugin
translated: true
---

`org.codehaus.mojo` Exec Maven Plugin को अपने Maven प्रोजेक्ट में उपयोग करने के लिए, आपको इसे अपने `pom.xml` फ़ाइल में कॉन्फ़िगर करना होगा और यह तय करना होगा कि आप अपने बिल्ड प्रोसेस के दौरान प्रोग्राम कैसे चलाना चाहते हैं—या तो बाहरी कमांड या Java प्रोग्राम। प्लगइन दो मुख्य लक्ष्यों को प्रदान करता है: `exec:exec` बाहरी प्रोग्राम चलाने के लिए और `exec:java` Java क्लास चलाने के लिए। नीचे, मैं आपको इसे सेटअप करने और प्रभावी रूप से उपयोग करने के लिए चरणों के बारे में मार्गदर्शन करूँगा।

### चरण 1: `pom.xml` में प्लगइन जोड़ें
पहले, Exec Maven Plugin को `pom.xml` के `<build><plugins>` सेक्शन में शामिल करें। `groupId`, `artifactId` और एक संस्करण (अब तक की सबसे नई संस्करण `3.1.0` है) को स्पेसिफाई करें:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
        </plugin>
    </plugins>
</build>
```

यह प्लगइन को आपके प्रोजेक्ट में जोड़ता है, लेकिन यह अभी तक कुछ भी नहीं करेगा जब तक कि आप इसे कॉन्फ़िगर नहीं करते या इसके लक्ष्यों को मैन्युअल रूप से नहीं चलाते।

### चरण 2: अपने लक्ष्य चुनें
प्लगइन दो प्राथमिक लक्ष्यों को ऑफर करता है:
- **`exec:exec`**: किसी भी बाहरी प्रोग्राम (जैसे शेल स्क्रिप्ट, बाइनरी, या `java` कमांड) को चलाता है।
- **`exec:java`**: प्रोजेक्ट से एक Java क्लास को उसी JVM में चलाता है जहां Maven है।

आप इन लक्ष्यों को कमांड लाइन से मैन्युअल रूप से चलाने के लिए (जैसे `mvn exec:exec`) या उन्हें Maven बिल्ड लाइफसाइकिल के किसी विशिष्ट चरण से बाइंड करने के लिए उपयोग कर सकते हैं।

### विकल्प 1: `exec:java` के साथ एक Java प्रोग्राम चलाएं
अगर आप अपने प्रोजेक्ट से एक Java क्लास चलाना चाहते हैं, तो `exec:java` लक्ष्य का उपयोग करें। यह एक `main` विधि वाले क्लास को चलाने के लिए आदर्श है जो आपके प्रोजेक्ट का हिस्सा है, जो प्रोजेक्ट के रनटाइम क्लासपाथ (जिसमें निर्भरताएं शामिल हैं) को स्वचालित रूप से लेवरेज करता है।

#### मैन्युअल एक्सिक्यूशन
एक मुख्य क्लास को स्पेसिफाई करने के लिए एक कॉन्फ़िगरेशन जोड़ें:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <mainClass>com.example.Main</mainClass>
            </configuration>
        </plugin>
    </plugins>
</build>
```

फिर, इसे कमांड लाइन से चलाएं:

```bash
mvn exec:java
```

यह `com.example.Main` को Maven के साथ उसी JVM में चलाता है, जो Maven के JVM सेटिंग्स को विरासत में लेता है।

#### बिल्ड के दौरान स्वचालित एक्सिक्यूशन
इसे एक बिल्ड चरण (जैसे `test`) के दौरान स्वचालित रूप से चलाने के लिए, `<executions>` सेक्शन का उपयोग करें:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>run-my-java</id>
                    <phase>test</phase>
                    <goals>
                        <goal>java</goal>
                    </goals>
                    <configuration>
                        <mainClass>com.example.Main</mainClass>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

अब, जब आप `mvn test` चलाते हैं, तो `com.example.Main` क्लास `test` चरण के दौरान चल जाएगा।

#### Arguments या System Properties पास करें
आप `main` विधि को arguments पास कर सकते हैं या system properties सेट कर सकते हैं:

```xml
<configuration>
    <mainClass>com.example.Main</mainClass>
    <arguments>
        <argument>arg1</argument>
        <argument>arg2</argument>
    </arguments>
    <systemProperties>
        <systemProperty>
            <key>propertyName</key>
            <value>propertyValue</value>
        </systemProperty>
    </systemProperties>
</configuration>
```

ध्यान दें कि `exec:java` Maven के साथ उसी JVM में चलता है, इसलिए JVM options (जैसे `-Xmx`) Maven को कैसे चलाया गया है (जैसे `mvn -Xmx512m exec:java`) से विरासत में लेते हैं।

### विकल्प 2: `exec:exec` के साथ एक बाहरी प्रोग्राम चलाएं
बाहरी प्रोग्राम जैसे शेल स्क्रिप्ट या कमांड चलाने के लिए, `exec:exec` लक्ष्य का उपयोग करें।

#### मैन्युअल एक्सिक्यूशन
प्लगइन को एक स्क्रिप्ट चलाने के लिए कॉन्फ़िगर करें:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <executable>myScript.sh</executable>
                <workingDirectory>/path/to/dir</workingDirectory>
                <arguments>
                    <argument>param1</argument>
                    <argument>param2</argument>
                </arguments>
            </configuration>
        </plugin>
    </plugins>
</build>
```

इसे चलाएं:

```bash
mvn exec:exec
```

यह `myScript.sh` को दिए गए arguments के साथ दिए गए working directory में चलाता है।

#### बिल्ड के दौरान स्वचालित एक्सिक्यूशन
इसे एक चरण से बाइंड करें, जैसे एक सर्वर को शुरू करने और इंटीग्रेशन टेस्ट के लिए बंद करने:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>start-server</id>
                    <phase>pre-integration-test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>startServer.sh</executable>
                    </configuration>
                </execution>
                <execution>
                    <id>stop-server</id>
                    <phase>post-integration-test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>stopServer.sh</executable>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

`mvn integration-test` चलाने से पहले सर्वर शुरू होगा और बाद में बंद होगा।

#### कस्टम JVM Options के साथ Java चलाएं
अगर आपको एक अलग JVM के साथ विशिष्ट options (जैसे `exec:java`) की आवश्यकता है, तो `exec:exec` के साथ `java` executable का उपयोग करें। आपको क्लासपाथ को मैन्युअल रूप से प्रबंधित करना होगा। यहां एक उदाहरण है:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <executable>java</executable>
                <arguments>
                    <argument>-Xmx512m</argument>
                    <argument>-classpath</argument>
                    <argument>${project.build.outputDirectory}</argument>
                    <argument>com.example.Main</argument>
                </arguments>
            </configuration>
        </plugin>
    </plugins>
</build>
```

निर्भरताओं को क्लासपाथ में शामिल करने के लिए, आप इसे जनरेट करने के लिए `maven-dependency-plugin` का उपयोग कर सकते हैं:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>3.2.0</version>
            <executions>
                <execution>
                    <id>build-classpath</id>
                    <phase>generate-resources</phase>
                    <goals>
                        <goal>build-classpath</goal>
                    </goals>
                    <configuration>
                        <outputProperty>project.classpath</outputProperty>
                    </configuration>
                </execution>
            </executions>
        </plugin>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>run-java</id>
                    <phase>test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>java</executable>
                        <arguments>
                            <argument>-Xmx512m</argument>
                            <argument>-classpath</argument>
                            <argument>${project.classpath}:${project.build.outputDirectory}</argument>
                            <argument>com.example.Main</argument>
                        </arguments>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

क्लासपाथ सेपरेटर (`:` Unix के लिए, `;` Windows के लिए) को आवश्यकता के अनुसार सेट करें।

### अतिरिक्त कॉन्फ़िगरेशन विकल्प
- **Environment Variables** (के लिए `exec:exec`):
  ```xml
  <configuration>
      <executable>myScript.sh</executable>
      <environmentVariables>
          <MY_VAR>value</MY_VAR>
      </environmentVariables>
  </configuration>
  ```
- **Working Directory**: कमांड को चलाने के लिए `<workingDirectory>` सेट करें।

### सारांश
Exec Maven Plugin बहुमुखी है:
- `exec:java` का उपयोग करके अपने प्रोजेक्ट से Java क्लास को आसानी से चलाएं, जो प्रोजेक्ट के क्लासपाथ का उपयोग करता है, लेकिन यह Maven के JVM में चलता है।
- `exec:exec` बाहरी प्रोग्रामों या कस्टम JVM options के साथ Java के लिए, जो आवश्यकता पड़ने पर क्लासपाथ प्रबंधन करने की आवश्यकता होती है।
- इसे `pom.xml` में कॉन्फ़िगर करें और इसे मैन्युअल रूप से (`mvn exec:java` या `mvn exec:exec`) चलाएं या इसे `<executions>` के साथ बिल्ड चरणों से बाइंड करें।

इस सेटअप के साथ, आप अपने Maven बिल्ड प्रोसेस में कस्टम एक्सिक्यूशन को आसानी से इंटीग्रेट कर सकते हैं!