---
audio: false
generated: true
lang: hi
layout: post
title: यूवीए समस्याओं के लिए मेवेन संरचना
translated: true
type: note
---

आपके `uva/106` सबडायरेक्टरी की विशिष्ट संरचना साझा करने के लिए धन्यवाद। ऐसा लगता है कि आपकी परियोजना में एक अधिक सूक्ष्म संरचना है जहां प्रत्येक UVA समस्या (जैसे `106`) एक अलग निर्देशिका है जिसमें अपनी स्वयं की `src` फ़ोल्डर है जिसमें एक `Main.java` फ़ाइल और संभवतः इनपुट फ़ाइलें जैसे `1.in` शामिल हैं। इससे पता चलता है कि प्रत्येक समस्या को एक अलग उप-परियोजना या मॉड्यूल के रूप में माना जा सकता है। इसे Maven मल्टी-मॉड्यूल सेटअप में समायोजित करने के लिए, हम या तो:
1. प्रत्येक समस्या निर्देशिका (जैसे `uva/106`) को अपना स्वयं का Maven सबमॉड्यूल मानें।
2. `uva` को एक ही मॉड्यूल के रूप में रखें और समस्या फ़ाइलों को इसके `src/main/java` निर्देशिका के भीतर व्यवस्थित करें।

UVA समस्याओं की संख्या (जैसा कि आपकी पिछली सूची में देखा गया है: `100`, `10000`, आदि) को देखते हुए, प्रत्येक समस्या के लिए एक अलग Maven मॉड्यूल बनाने से मॉड्यूलों की एक बड़ी संख्या हो सकती है, जो बोझिल हो सकती है। इसके बजाय, मैं एक ऐसी संरचना प्रस्तावित करूंगा जहां `uva` एक ही मॉड्यूल है, और प्रत्येक समस्या का `Main.java` `uva/src/main/java` के भीतर एक पैकेज संरचना (जैसे समस्या 106 के लिए `com.algorithm.solutions.uva.p106`) के तहत व्यवस्थित है। यह परियोजना को प्रबंधनीय बनाए रखते हुए Maven के लाभों को बनाए रखता है।

हालाँकि, यदि आप उस सूक्ष्मता को पसंद करते हैं तो मैं एक वैकल्पिक दृष्टिकोण भी प्रदान करूंगा जहाँ प्रत्येक समस्या एक अलग सबमॉड्यूल है। नीचे, मैं आपकी संरचना के आधार पर `pom.xml` फ़ाइलों को अपडेट करूंगा और आपकी फ़ाइलों को पुनर्व्यवस्थित करने के चरण प्रदान करूंगा।

---

### विकल्प 1: समस्या पैकेजों के साथ एकल `uva` मॉड्यूल

#### अद्यतन निर्देशिका संरचना
```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── com/algorithm/solutions/nowcoder/
│                   ├── Main.java
│                   ├── nc140.java
│                   ├── nc45.java
│                   ├── nc78.java
│                   └── nc93.java
├── uva/
│   ├── pom.xml
│   ├── src/
│   │   └── main/
│   │       └── java/
│   │           └── com/algorithm/solutions/uva/
│   │               ├── p100/
│   │               │   └── Main.java
│   │               ├── p106/
│   │               │   └── Main.java
│   │               ├── p10000/
│   │               │   └── Main.java
│   │               └── (आदि)
│   └── resources/
│       └── uva/
│           ├── p100/
│           │   └── 1.in
│           ├── p106/
│           │   └── 1.in
│           └── (आदि)
└── README.md
```

#### पैरेंट `pom.xml` (रूट: `algorithm-solutions/pom.xml`)
यह पहले जैसा ही बना रहता है, जो `nowcoder` और `uva` को मॉड्यूल के रूप में परिभाषित करता है।

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

#### Nowcoder सबमॉड्यूल `pom.xml` (`nowcoder/pom.xml`)
यह पिछले उत्तर से अपरिवर्तित है, यह मानते हुए कि `nowcoder` फ़ाइलों को `src/main/java/com/algorithm/solutions/nowcoder/` में ले जाया गया है।

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
                            <mainClass>com.algorithm.solutions.nowcoder.Main</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### UVA सबमॉड्यूल `pom.xml` (`uva/pom.xml`)
इस मॉड्यूल में इनपुट फ़ाइलों जैसे `1.in` के लिए एक `resources` निर्देशिका शामिल है। प्रत्येक समस्या के लिए `Main.java` फ़ाइलें पैकेजों में व्यवस्थित हैं।

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
        <resources>
            <resource>
                <directory>src/main/resources</directory>
                <includes>
                    <include>**/*.in</include>
                </includes>
            </resource>
        </resources>
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

#### फ़ाइल संगठन
- **Java फ़ाइलें ले जाएँ**:
  - प्रत्येक समस्या (जैसे `uva/106/src/Main.java`) के लिए, `Main.java` को `uva/src/main/java/com/algorithm/solutions/uva/p106/Main.java` पर ले जाएँ।
  - `Main.java` फ़ाइल को पैकेज घोषणा शामिल करने के लिए अपडेट करें:
    ```java
    package com.algorithm.solutions.uva.p106;
    public class Main {
        // ... मौजूदा कोड ...
    }
    ```
  - यह सभी समस्याओं (जैसे `p100`, `p10000`, आदि) के लिए करें।

- **इनपुट फ़ाइलें ले जाएँ**:
  - इनपुट फ़ाइलों जैसे `uva/106/1.in` को `uva/src/main/resources/uva/p106/1.in` पर ले जाएँ।
  - यह Maven को इन फ़ाइलों को JAR में शामिल करने की अनुमति देता है, जिसे आपके Java कोड में `ClassLoader.getResource()` या इसी तरह के माध्यम से एक्सेस किया जा सकता है।

#### एक प्रोग्राम चलाना
किसी विशिष्ट UVA समस्या (जैसे समस्या 106) को चलाने के लिए:
```bash
mvn -pl uva exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
```

---

### विकल्प 2: प्रत्येक UVA समस्या एक सबमॉड्यूल के रूप में
यदि आप चाहते हैं कि प्रत्येक UVA समस्या (जैसे `106`, `100`) अपना स्वयं का Maven मॉड्यूल हो, तो यहां बताया गया है कि इसे कैसे सेटअप किया जाए। यह अधिक सूक्ष्म है लेकिन `pom.xml` फ़ाइलों की संख्या बढ़ाता है।

#### अद्यतन निर्देशिका संरचना
```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── com/algorithm/solutions/nowcoder/
│                   ├── Main.java
│                   ├── nc140.java
│                   ├── nc45.java
│                   ├── nc78.java
│                   └── nc93.java
├── uva/
│   ├── 106/
│   │   ├── pom.xml
│   │   ├── src/
│   │   │   └── main/
│   │   │       └── java/
│   │   │           └── com/algorithm/solutions/uva/p106/
│   │   │               └── Main.java
│   │   └── resources/
│   │       └── 1.in
│   ├── 100/
│   │   ├── pom.xml
│   │   ├── src/
│   │   │   └── main/
│   │   │       └── java/
│   │   │           └── com/algorithm/solutions/uva/p100/
│   │   │               └── Main.java
│   │   └── resources/
│   │       └── (इनपुट फ़ाइलें, यदि कोई हों)
│   └── (अन्य समस्या निर्देशिकाएँ)
└── README.md
```

#### पैरेंट `pom.xml` (रूट: `algorithm-solutions/pom.xml`)
प्रत्येक समस्या को एक मॉड्यूल के रूप में जोड़ें।

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
        <module>uva/106</module>
        <module>uva/100</module>
        <module>uva/10000</module>
        <module>uva/10006</module>
        <module>uva/10008</module>
        <module>uva/10009</module>
        <module>uva/10012</module>
        <module>uva/10013</module>
        <module>uva/10018</module>
        <module>uva/10019</module>
        <module>uva/10026</module>
        <module>uva/10033</module>
        <module>uva/10034</module>
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

#### Nowcoder सबमॉड्यूल `pom.xml` (`nowcoder/pom.xml`)
ऊपर के समान (अपरिवर्तित)।

#### UVA समस्या 106 सबमॉड्यूल `pom.xml` (`uva/106/pom.xml`)
प्रत्येक समस्या का अपना `pom.xml` होता है। यहाँ `uva/106` के लिए एक उदाहरण दिया गया है:

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

    <artifactId>uva-106</artifactId>
    <name>UVA Problem 106</name>
    <description>Solution for UVA problem 106</description>

    <build>
        <resources>
            <resource>
                <directory>resources</directory>
                <includes>
                    <include>**/*.in</include>
                </includes>
            </resource>
        </resources>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.4.2</version>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>com.algorithm.solutions.uva.p106.Main</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

- **अन्य समस्याओं के लिए दोहराएँ**: `uva/100`, `uva/10000`, आदि के लिए समान `pom.xml` फ़ाइलें बनाएँ, `artifactId` (जैसे `uva-100`), `name`, और `mainClass` (जैसे `com.algorithm.solutions.uva.p100.Main`) को समायोजित करते हुए।

#### फ़ाइल संगठन
- **Java फ़ाइलें ले जाएँ**:
  - `uva/106/src/Main.java` के लिए, `uva/106/src/main/java/com/algorithm/solutions/uva/p106/Main.java` पर ले जाएँ।
  - पैकेज घोषणा जोड़ें:
    ```java
    package com.algorithm.solutions.uva.p106;
    public class Main {
        // ... मौजूदा कोड ...
    }
    ```
- **इनपुट फ़ाइलें ले जाएँ**:
  - `uva/106/1.in` को `uva/106/resources/1.in` पर ले जाएँ।

#### एक प्रोग्राम चलाना
समस्या 106 को चलाने के लिए:
```bash
mvn -pl uva/106 exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
```

---

### सिफारिश
- **विकल्प 1 (एकल `uva` मॉड्यूल)** सरल और अधिक स्केलेबल है, खासकर यदि आपके पास कई UVA समस्याएं हैं। यह कई `pom.xml` फ़ाइलें बनाने से बचाता है और परियोजना संरचना को साफ रखता है। समस्याओं को तार्किक रूप से व्यवस्थित करने के लिए पैकेजों का उपयोग करें।
- **विकल्प 2 (प्रति-समस्या मॉड्यूल)** बेहतर है यदि आप चाहते हैं कि प्रत्येक समस्या पूरी तरह से स्वतंत्र हो (जैसे अलग तैनाती या परीक्षण के लिए)। हालाँकि, मॉड्यूलों की संख्या के कारण इसमें अधिक रखरखाव की आवश्यकता होती है।

### विकल्प 1 को लागू करने के चरण
1. **निर्देशिका संरचना बनाएँ**:
   - `algorithm-solutions` रूट में इन कमांडों को चलाएँ:
     ```bash
     mkdir -p uva/src/main/java/com/algorithm/solutions/uva
     mkdir -p uva/src/main/resources/uva
     mkdir -p nowcoder/src/main/java/com/algorithm/solutions/nowcoder
     ```
2. **फ़ाइलें ले जाएँ**:
   - प्रत्येक UVA समस्या (जैसे `106`) के लिए:
     ```bash
     mkdir -p uva/src/main/java/com/algorithm/solutions/uva/p106
     mv uva/106/src/Main.java uva/src/main/java/com/algorithm/solutions/uva/p106/Main.java
     mkdir -p uva/src/main/resources/uva/p106
     mv uva/106/1.in uva/src/main/resources/uva/p106/1.in
     ```
   - `nowcoder` के लिए:
     ```bash
     mv nowcoder/*.java nowcoder/src/main/java/com/algorithm/solutions/nowcoder/
     ```
3. **Java फ़ाइलें अपडेट करें**:
   - उचित पैकेज घोषणाएँ जोड़ें (जैसे `uva/106/Main.java` के लिए `package com.algorithm.solutions.uva.p106;`)।
4. **`pom.xml` फ़ाइलें जोड़ें**:
   - पैरेंट `pom.xml` को `algorithm-solutions/` में रखें।
   - `nowcoder/pom.xml` और `uva/pom.xml` को दिखाए अनुसार रखें।
5. **बिल्ड करें**:
   ```bash
   mvn clean install
   ```

### नोट्स
- **इनपुट फ़ाइलें**: यदि आपका `Main.java` इनपुट फ़ाइलें जैसे `1.in` पढ़ता है, तो कोड को अपडेट करें ताकि वे `getClass().getResource("/uva/p106/1.in")` या इसी तरह के माध्यम से एक्सेस हो सकें, क्योंकि वे अब `src/main/resources` में हैं।
- **`.iml` फ़ाइलों को अनदेखा करना**: वर्जन कंट्रोल से IntelliJ प्रोजेक्ट फ़ाइलों को बाहर करने के लिए `*.iml` के साथ एक `.gitignore` फ़ाइल जोड़ें।
- **अन्य निर्देशिकाएँ**: `codeforces`, `hacker_rank`, आदि के लिए, आप समान मॉड्यूल बना सकते हैं जब तैयार हों। यदि आपको उनके लिए `pom.xml` फ़ाइलों की आवश्यकता है तो मुझे बताएं।
- **Java वर्जन**: यदि आप एक अलग Java वर्जन का उपयोग करते हैं तो `<maven.compiler.source>` और `<maven.compiler.target>` को समायोजित करें।

यदि आप विकल्प 2 पसंद करते हैं या विशिष्ट समस्याओं (जैसे संसाधन लोडिंग के लिए `Main.java` को समायोजित करना) के साथ सहायता चाहते हैं, तो मुझे बताएं!