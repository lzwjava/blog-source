---
audio: false
generated: true
lang: hi
layout: post
title: एग्जेक मेवेन प्लगइन
translated: true
type: note
---

अपने Maven प्रोजेक्ट में `org.codehaus.mojo` Exec Maven Plugin का उपयोग करने के लिए, आपको इसे अपनी `pom.xml` फ़ाइल में कॉन्फ़िगर करना होगा और तय करना होगा कि आप अपनी build प्रक्रिया के दौरान प्रोग्राम कैसे execute करना चाहते हैं—चाहे वह बाहरी कमांड हों या Java प्रोग्राम। यह प्लगइन दो मुख्य लक्ष्य प्रदान करता है: बाहरी प्रोग्राम चलाने के लिए `exec:exec` और Java classes को execute करने के लिए `exec:java`। नीचे, मैं आपको इसे सेट अप करने और प्रभावी ढंग से उपयोग करने के चरणों के माध्यम से मार्गदर्शन करूंगा।

### चरण 1: प्लगइन को अपनी `pom.xml` में जोड़ें
सबसे पहले, Exec Maven Plugin को अपनी `pom.xml` के `<build><plugins>` सेक्शन में शामिल करें। `groupId`, `artifactId`, और एक version निर्दिष्ट करें (अभी के लिए नवीनतम `3.1.0` है):

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

यह आपके प्रोजेक्ट में प्लगइन को जोड़ता है, लेकिन जब तक आप इसे कॉन्फ़िगर नहीं करते या इसके लक्ष्यों को मैन्युअली नहीं चलाते, तब तक यह कुछ नहीं करेगा।

### चरण 2: अपना लक्ष्य चुनें
प्लगइन दो प्राथमिक लक्ष्य प्रदान करता है:
- **`exec:exec`**: कोई भी बाहरी प्रोग्राम execute करता है (जैसे, shell scripts, binaries, या यहां तक कि `java` कमांड)।
- **`exec:java`**: आपके प्रोजेक्ट की एक Java class को एक `main` method के साथ, Maven के समान JVM में चलाता है।

आप इन लक्ष्यों का उपयोग या तो कमांड लाइन से मैन्युअली चलाकर कर सकते हैं (जैसे, `mvn exec:exec`) या उन्हें Maven build lifecycle में किसी विशिष्ट चरण से बांधकर।

### विकल्प 1: `exec:java` के साथ एक Java प्रोग्राम चलाना
यदि आप अपने प्रोजेक्ट की एक Java class को execute करना चाहते हैं, तो `exec:java` लक्ष्य का उपयोग करें। यह आपके प्रोजेक्ट के किसी class में `main` method को चलाने के लिए आदर्श है, जो प्रोजेक्ट के runtime classpath (dependencies सहित) का स्वचालित रूप से लाभ उठाता है।

#### मैन्युअल एक्जिक्यूशन
मुख्य वर्ग निर्दिष्ट करने के लिए एक कॉन्फ़िगरेशन जोड़ें:

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

यह `com.example.Main` को Maven के समान JVM में execute करता है, Maven की JVM सेटिंग्स को inherit करता है।

#### बिल्ड के दौरान स्वचालित एक्जिक्यूशन
इसे किसी build चरण (जैसे, `test`) के दौरान स्वचालित रूप से चलाने के लिए, `<executions>` सेक्शन का उपयोग करें:

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

अब, जब आप `mvn test` चलाएंगे, तो `com.example.Main` वर्ग `test` चरण के दौरान execute होगी।

#### आर्गुमेंट्स या सिस्टम प्रॉपर्टीज़ पास करना
आप `main` method को आर्गुमेंट्स पास कर सकते हैं या सिस्टम प्रॉपर्टीज़ सेट कर सकते हैं:

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

ध्यान दें कि `exec:java` Maven के समान JVM में चलता है, इसलिए JVM विकल्प (जैसे, `-Xmx`) इस बात से inherit होते हैं कि Maven को कैसे invoke किया गया है (जैसे, `mvn -Xmx512m exec:java`)।

### विकल्प 2: `exec:exec` के साथ एक बाहरी प्रोग्राम चलाना
Shell scripts या commands जैसे बाहरी प्रोग्राम execute करने के लिए, `exec:exec` लक्ष्य का उपयोग करें।

#### मैन्युअल एक्जिक्यूशन
एक script चलाने के लिए प्लगइन को कॉन्फ़िगर करें:

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

इसे इसके साथ चलाएं:

```bash
mvn exec:exec
```

यह `myScript.sh` को दिए गए आर्गुमेंट्स के साथ निर्दिष्ट working directory में execute करता है।

#### बिल्ड के दौरान स्वचालित एक्जिक्यूशन
इसे किसी चरण से बांधें, जैसे integration tests के लिए एक सर्वर को start और stop करना:

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

`mvn integration-test` चलाने से tests से पहले सर्वर start होगा और बाद में stop हो जाएगा।

#### कस्टम JVM विकल्पों के साथ Java चलाना
यदि आपको विशिष्ट विकल्पों वाले एक अलग JVM की आवश्यकता है (`exec:java` के विपरीत), तो `java` executable के साथ `exec:exec` का उपयोग करें। आपको classpath को मैन्युअली manage करने की आवश्यकता होगी। यहां एक उदाहरण दिया गया है:

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

Classpath में dependencies शामिल करने के लिए, आप इसे generate करने के लिए `maven-dependency-plugin` का उपयोग कर सकते हैं:

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

आवश्यकतानुसार classpath separator (`:` यूनिक्स के लिए, `;` विंडोज के लिए) adjust करें।

### अतिरिक्त कॉन्फ़िगरेशन विकल्प
- **एनवायरनमेंट वेरिएबल्स** (`exec:exec` के लिए):
  ```xml
  <configuration>
      <executable>myScript.sh</executable>
      <environmentVariables>
          <MY_VAR>value</MY_VAR>
      </environmentVariables>
  </configuration>
  ```
- **वर्किंग डायरेक्टरी**: कमांड कहां चलेगा यह सेट करने के लिए `<workingDirectory>` का उपयोग करें।

### सारांश
Exec Maven Plugin बहुमुखी है:
- अपने प्रोजेक्ट की Java classes को आसानी से चलाने के लिए `exec:java` का उपयोग करें, प्रोजेक्ट के classpath का लाभ उठाते हुए, लेकिन यह Maven के JVM में चलता है।
- बाहरी प्रोग्राम या कस्टम JVM विकल्पों के साथ Java के लिए `exec:exec` का उपयोग करें, जिसके लिए आवश्यकता पड़ने पर मैन्युअल classpath प्रबंधन की आवश्यकता होती है।
- इसे `pom.xml` में कॉन्फ़िगर करें और या तो इसे मैन्युअली चलाएं (`mvn exec:java` or `mvn exec:exec`) या इसे `<executions>` के साथ build चरणों से बांधें।

यह सेटअप आपको अपनी Maven build प्रक्रिया में कस्टम executions को सहजता से एकीकृत करने की अनुमति देता है!