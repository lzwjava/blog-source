---
audio: false
date: 2025-09-08
generated: true
image: false
lang: hi
layout: post
title: जैकोको बहु-मॉड्यूल कवरेज रिपोर्टिंग रणनीति
translated: true
type: note
---

बिल्कुल। आपका विश्लेषण सटीक है, खासकर बाहरी एकीकरण परीक्षणों के साथ JaCoCo की जटिलताओं के संबंध में। बिल्ड को दो बार चलाना निश्चित रूप से आदर्श नहीं है।

आप जिस रणनीति की तलाश कर रहे हैं, उसमें परीक्षण निष्पादन को केंद्रीकृत करना और फिर परिणामों को एकत्रित करना शामिल है। आप बहुत करीब हैं, और `aggregate` लक्ष्य वास्तव में सही उपकरण है, लेकिन इस परिदृश्य के लिए इसे एक विशिष्ट तरीके से लागू करने की आवश्यकता है।

यहां अनुशंसित रणनीति है: **अपने वेब एप्लिकेशन मॉड्यूल में एक कवरेज फ़ाइल (`.exec`) उत्पन्न करें, और फिर सभी प्रासंगिक मॉड्यूल के लिए एक एकल, एकत्रित रिपोर्ट बनाने के लिए एक अलग, समर्पित रिपोर्टिंग मॉड्यूल का उपयोग करें।**

यह दृष्टिकोण साफ-सुथरा, स्केलेबल है और अनावश्यक बिल्ड से बचाता है।

-----

## मूल अवधारणा

जब आपका `PlaygroundWeb` एप्लिकेशन JaCoCo एजेंट के साथ Jetty पर चलता है, तो एजेंट **एप्लिकेशन के क्लासलोडर द्वारा लोड किए गए सभी क्लासेस** को इंस्ट्रूमेंट करता है। इसमें `PlaygroundWeb` के अपने क्लासेस *और* इसकी सभी निर्भरताएं, जैसे `PlaygroundUtils.jar` शामिल हैं।

इसलिए, `PlaygroundWeb` बिल्ड के दौरान उत्पन्न एकल `jacoco-it.exec` फ़ाइल में **दोनों मॉड्यूल** के लिए कवरेज डेटा पहले से ही मौजूद होता है। चुनौती केवल JaCoCo रिपोर्टिंग टूल को उन सभी मॉड्यूल के स्रोत कोड की ओर इंगित करना है जिनकी आवश्यकता अंतिम HTML रिपोर्ट बनाने के लिए है।

-----

## 4 चरणों में एक स्केलेबल रणनीति

यहां साफ-सुथरी, एकत्रित कवरेज रिपोर्टिंग के लिए आपकी परियोजना को रीफैक्टर करने के लिए एक चरण-दर-चरण मार्गदर्शिका दी गई है।

### चरण 1: एक समर्पित रिपोर्टिंग मॉड्यूल बनाएँ

सबसे पहले, केवल एकत्रीकरण के लिए एक नया मॉड्यूल बनाएं। यह एक Maven सर्वोत्तम अभ्यास है जो जिम्मेदारियों को अलग रखता है।

1.  अपने रूट `pom.xml` (`PlaygroundLib`) में, नया मॉड्यूल जोड़ें:
    ```xml
    <modules>
        <module>PlaygroundUtils</module>
        <module>PlaygroundWeb</module>
        <module>PlaygroundReports</module> </modules>
    ```
2.  रूट पर एक नया निर्देशिका `PlaygroundReports` बनाएं जिसमें उसका अपना `pom.xml` हो।

आपकी नई परियोजना संरचना इस तरह दिखेगी:

```
.
├── PlaygroundReports
│   └── pom.xml
├── PlaygroundUtils
│   └── pom.xml
├── PlaygroundWeb
│   └── pom.xml
└── pom.xml
```

### चरण 2: रिपोर्टिंग मॉड्यूल के `pom.xml` को कॉन्फ़िगर करें

यह नया `pom.xml` वह जगह है जहाँ जादू होता है। यह उन सभी मॉड्यूल पर निर्भर करेगा जिन्हें आप रिपोर्ट में चाहते हैं और `report-aggregate` लक्ष्य को चलाएगा।

**`PlaygroundReports/pom.xml`:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.lzw</groupId>
        <artifactId>PlaygroundLib</artifactId>
        <version>1.0</version>
    </parent>
    <artifactId>PlaygroundReports</artifactId>
    <packaging>pom</packaging>
    <name>PlaygroundReports</name>

    <dependencies>
        <dependency>
            <groupId>com.lzw</groupId>
            <artifactId>PlaygroundWeb</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>com.lzw</groupId>
            <artifactId>PlaygroundUtils</artifactId>
            <version>${project.version}</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <executions>
                    <execution>
                        <id>aggregate-report</id>
                        <phase>verify</phase>
                        <goals>
                            <goal>report-aggregate</goal>
                        </goals>
                        <configuration>
                            <dataFiles>
                                <dataFile>${project.basedir}/../PlaygroundWeb/target/jacoco-it.exec</dataFile>
                            </dataFiles>
                            <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate</outputDirectory>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### चरण 3: `PlaygroundWeb` मॉड्यूल को सरल बनाएं

आपका `PlaygroundWeb` मॉड्यूल अब केवल **कवरेज डेटा उत्पन्न करने** के लिए जिम्मेदार है, इस पर रिपोर्टिंग के लिए नहीं। आप इसके `pom.xml` से `jacoco:report` एक्ज़िक्यूशन को हटा सकते हैं।

**`PlaygroundWeb/pom.xml` (केवल परिवर्तन):**

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>prepare-agent</id>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
            <configuration>
                <propertyName>jacoco.it.agent</propertyName>
                <destFile>${project.build.directory}/jacoco-it.exec</destFile>
            </configuration>
        </execution>
        </executions>
</plugin>

<plugin>
    <groupId>org.eclipse.jetty</groupId>
    <artifactId>jetty-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>start-jetty</id>
            <phase>pre-integration-test</phase>
            <goals>
                <goal>start</goal>
            </goals>
            <configuration>
                <daemon>true</daemon>
                <jvmArgs>
                    ${jacoco.it.agent}
                </jvmArgs>
                </configuration>
        </execution>
        </executions>
</plugin>
```

*नोट*: मैंने `prepare-agent` कॉन्फ़िगरेशन को थोड़ा संशोधित किया है ताकि एक प्रॉपर्टी (`jacoco.it.agent`) का उपयोग किया जा सके और फिर उसे `jetty-maven-plugin` में संदर्भित किया जा सके। यह एजेंट स्ट्रिंग को पास करने का एक मजबूत तरीका है। आपके `pom.xml` में पिछली कॉन्फ़िगरेशन भी ठीक थी, लेकिन यह इरादे को और स्पष्ट करती है।

### चरण 4: `PlaygroundUtils` को साफ़ करें

`PlaygroundUtils` मॉड्यूल को एकीकरण परीक्षणों के लिए किसी JaCoCo प्लगइन कॉन्फ़िगरेशन की आवश्यकता नहीं है। इसका कोड `PlaygroundWeb` के माध्यम से कवर किया जाता है, और रिपोर्टिंग `PlaygroundReports` द्वारा संभाली जाती है। आप इसके `pom.xml` से किसी भी JaCoCo-संबंधित गुण या प्लगइन को हटा सकते हैं।

-----

## यह समस्या का समाधान कैसे करता है

1.  **सिंगल बिल्ड:** आप रूट डायरेक्टरी से `mvn clean verify` केवल एक बार चलाते हैं।
2.  **सही लाइफसाइकल:**
      * Maven `PlaygroundUtils` बनाता है।
      * Maven `PlaygroundWeb` बनाता है, JaCoCo एजेंट के साथ Jetty शुरू करता है, आपके Python टेस्ट चलाता है (जो दोनों मॉड्यूल में कोड को हिट करते हैं), Jetty को रोकता है, और `PlaygroundWeb/target/jacoco-it.exec` उत्पन्न करता है।
      * Maven `PlaygroundReports` बनाता है। `verify` फेज में, `report-aggregate` लक्ष्य चलता है। यह `PlaygroundWeb` से `.exec` फ़ाइल ढूंढता है और निर्भरताओं के कारण, यह जानता है कि `PlaygroundWeb` और `PlaygroundUtils` दोनों के स्रोत कोड कहां मिलेंगे।
      * यह दोनों मॉड्यूल के लिए कवरेज के साथ एक **एकीकृत HTML रिपोर्ट** उत्पन्न करता है।
3.  **स्केलेबिलिटी:** यदि आप दस और लाइब्रेरी मॉड्यूल जोड़ते हैं, तो आप बस उन्हें `PlaygroundReports/pom.xml` में निर्भरताओं के रूप में जोड़ देते हैं। मूल तर्क नहीं बदलता है। यह वह साफ, स्केलेबल समाधान है जिसकी आपको तलाश थी।