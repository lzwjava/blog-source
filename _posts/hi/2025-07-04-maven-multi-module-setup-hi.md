---
audio: false
generated: true
lang: hi
layout: post
title: रिपॉजिटरी को मेवेन मल्टी-मॉड्यूल में बदलें
translated: true
type: note
---

अपने `algorithm-solutions` रिपॉजिटरी को Maven द्वारा प्रबंधित एक मल्टी-मॉड्यूल Java प्रोजेक्ट में बदलने के लिए, आपको रूट डायरेक्टरी में एक पैरेंट `pom.xml` और प्रत्येक सबमॉड्यूल (`nowcoder` और `uva`) के लिए अलग-अलग `pom.xml` फाइलों की आवश्यकता होगी। पैरेंट `pom.xml` सामान्य कॉन्फ़िगरेशन को परिभाषित करेगा और सबमॉड्यूल्स को मैनेज करेगा, जबकि प्रत्येक सबमॉड्यूल का `pom.xml` उसकी विशिष्ट सेटिंग्स को संभालेगा।

नीचे, मैं पैरेंट प्रोजेक्ट और दोनों सबमॉड्यूल्स के लिए `pom.xml` फाइलें प्रदान करूंगा। मैं मानकर चल रहा हूं:
- प्रोजेक्ट Java 17 का उपयोग करता है (आधुनिक प्रोजेक्ट्स के लिए एक सामान्य संस्करण; जरूरत पड़ने पर समायोजित करें)।
- `nowcoder` और `uva` डायरेक्टरीज में एक मानक Maven संरचना (`src/main/java`) में Java सोर्स फाइलें हैं।
- अभी के लिए कोई बाहरी निर्भरताओं की आवश्यकता नहीं है, लेकिन संरचना आसानी से जोड़ने की अनुमति देती है।
- प्रत्येक सबमॉड्यूल को एक JAR के रूप में पैकेज किया जाएगा (चूंकि ये संभवतः स्टैंडअलोन एल्गोरिदम समाधान हैं)।

### डायरेक्टरी संरचना
सेटअप के बाद, आपकी डायरेक्टरी संरचना इस प्रकार दिखनी चाहिए:

```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── (आपकी Java फाइलें, जैसे, Main.java, nc140, आदि)
├── uva/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── (आपकी Java फाइलें, जैसे, 100.java, 10000.java, आदि)
└── README.md
```

### पैरेंट `pom.xml`
यह फाइल रूट डायरेक्टरी (`algorithm-solutions/pom.xml`) में जाती है। यह पैरेंट प्रोजेक्ट को परिभाषित करती है, सबमॉड्यूल्स को सूचीबद्ध करती है, और Java संस्करण और कंपाइलर सेटिंग्स जैसी सामान्य कॉन्फ़िगरेशन सेट करती है।

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.algorithm.solutions</groupId>
    <artifactId>algorithm-solutions</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <name>Algorithm Solutions Parent</name>
    <description>Parent project for algorithm solutions</description>

    <modules>
        <module>nowcoder</module>
        <module>uva</module>
    </modules>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.13.0</version>
                <configuration>
                    <source>${maven.compiler.source}</source>
                    <target>${maven.compiler.target}</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

### Nowcoder सबमॉड्यूल `pom.xml`
यह फाइल `nowcoder` डायरेक्टरी (`nowcoder/pom.xml`) में जाती है। यह पैरेंट से इनहेरिट करती है और अपनी स्वयं की आर्टिफैक्ट डिटेल्स निर्दिष्ट करती है।

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.algorithm.solutions</groupId>
        <artifactId>algorithm-solutions</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>nowcoder</artifactId>
    <name>Nowcoder Solutions</name>
    <description>Solutions for Nowcoder algorithm problems</description>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.4.2</version>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>Main</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

### UVA सबमॉड्यूल `pom.xml`
यह फाइल `uva` डायरेक्टरी (`uva/pom.xml`) में जाती है। यह भी पैरेंट से इनहेरिट करती है और अपनी स्वयं की आर्टिफैक्ट डिटेल्स निर्दिष्ट करती है। चूंकि UVA समाधानों में आमतौर पर एक एकल `Main` क्लास नहीं होती (प्रत्येक समस्या एक स्टैंडअलोन प्रोग्राम हो सकता है), मैं यहां कोई मुख्य क्लास निर्दिष्ट नहीं करूंगा, लेकिन आप जरूरत पड़ने पर एक जोड़ सकते हैं।

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.algorithm.solutions</groupId>
        <artifactId>algorithm-solutions</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>uva</artifactId>
    <name>UVA Solutions</name>
    <description>Solutions for UVA algorithm problems</description>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.4.2</version>
            </plugin>
        </plugins>
    </build>
</project>
```

### सेटअप करने के चरण
1.  **Maven डायरेक्टरी संरचना बनाएं**:
    *   `nowcoder` में आपकी Java फाइलों को `nowcoder/src/main/java/` में ले जाएं।
    *   `uva` में आपकी Java फाइलों को `uva/src/main/java/` में ले जाएं।
    *   उदाहरण के लिए, `nowcoder/Main.java` को `nowcoder/src/main/java/Main.java` में होना चाहिए।

2.  **`pom.xml` फाइलें रखें**:
    *   पैरेंट `pom.xml` को `algorithm-solutions` रूट डायरेक्टरी में रखें।
    *   `nowcoder/pom.xml` को `nowcoder` डायरेक्टरी में रखें।
    *   `uva/pom.xml` को `uva` डायरेक्टरी में रखें।

3.  **प्रोजेक्ट बिल्ड करें**:
    *   एक टर्मिनल में `algorithm-solutions` रूट डायरेक्टरी में नेविगेट करें।
    *   दोनों सबमॉड्यूल्स को बिल्ड करने के लिए `mvn clean install` चलाएं।

4.  **एक विशिष्ट प्रोग्राम रन करें**:
    *   `nowcoder` के लिए, यदि `Main.java` एंट्री पॉइंट है, तो आप इसे इसके साथ रन कर सकते हैं:
        ```bash
        mvn -pl nowcoder exec:java -Dexec.mainClass="Main"
        ```
    *   UVA समाधानों के लिए, चूंकि प्रत्येक फाइल एक स्टैंडअलोन प्रोग्राम हो सकती है, आप एक विशिष्ट क्लास (जैसे, `100.java`) को इसके साथ रन कर सकते हैं:
        ```bash
        mvn -pl uva exec:java -Dexec.mainClass="100"
        ```

### नोट्स
-   **Java संस्करण**: मैंने Java 17 का उपयोग किया है। यदि आपको किसी भिन्न संस्करण की आवश्यकता है, तो पैरेंट `pom.xml` में `<maven.compiler.source>` और `<maven.compiler.target>` गुणों को अपडेट करें।
-   **निर्भरताएं**: यदि आपके समाधानों को लाइब्रेरीज़ (जैसे, इनपुट/आउटपुट यूटिलिटीज़ के लिए) की आवश्यकता है, तो उन्हें सबमॉड्यूल के `pom.xml` में एक `<dependencies>` सेक्शन के अंतर्गत जोड़ें।
-   **फाइल नामकरण**: सुनिश्चित करें कि आपकी Java फाइलों के नाम क्लास नामों से मेल खाते हों (जैसे, `100.java` में `public class 100` होना चाहिए)।
-   **अन्य डायरेक्टरीज**: आपके रिपो में `codeforces`, `hacker_rank`, आदि शामिल हैं। यदि आप इन्हें सबमॉड्यूल्स के रूप में शामिल करना चाहते हैं, तो पैरेंट `pom.xml` में `<module>codeforces</module>` (आदि) जोड़ें और उन डायरेक्टरीज में `nowcoder` और `uva` के समान संबंधित `pom.xml` फाइलें बनाएं।

यदि आपको अतिरिक्त सबमॉड्यूल्स या विशिष्ट कॉन्फ़िगरेशन की आवश्यकता है तो मुझे बताएं!