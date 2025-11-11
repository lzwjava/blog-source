---
audio: false
generated: true
lang: hi
layout: post
title: मेवेन निर्भरता समस्या
translated: true
type: note
---

### समस्या अवलोकन

उपयोगकर्ता Maven का उपयोग करके Spring Boot एप्लिकेशन चलाते समय एक बिल्ड विफलता का सामना कर रहा है। त्रुटि संदेश एक `IllegalArgumentException` को इंगित करता है जो `NoClassDefFoundError: org/springframework/beans/factory/aot/BeanRegistrationExcludeFilter` के कारण होता है। यह प्रोजेक्ट की dependencies के भीतर एक संस्करण असंगतता समस्या का सुझाव देता है, जो एप्लिकेशन को सही ढंग से शुरू होने से रोकता है। प्रदान किया गया `pom.xml` फ़ाइल और Maven आउटपुट हमें समस्या का निदान करने और हल करने के लिए आवश्यक संदर्भ देते हैं।

### मूल कारण

त्रुटि इसलिए होती है क्योंकि Spring Boot एप्लिकेशन `SharedMetadataReaderFactoryContextInitializer` को इंस्टेंटिएट करने में असमर्थ है, जो कि Spring Boot की ऑटो-कॉन्फ़िगरेशन प्रक्रिया में शामिल एक क्लास है। अंतर्निहित कारण एक गायब क्लास, `BeanRegistrationExcludeFilter` है, जो Spring Framework 6.0 और बाद के संस्करणों का हिस्सा है। प्रोजेक्ट Spring Boot 3.4.2 का उपयोग करता है, जो Spring Framework 6.1.14 पर निर्भर करता है। हालाँकि, `pom.xml` Spring Framework dependencies के पुराने, असंगत संस्करणों को निर्दिष्ट करता है, जिससे classpath conflict होती है।

`pom.xml` में पहचाने गए मुख्य मुद्दे यहां दिए गए हैं:

1. **असंगत Spring Boot Maven Plugin संस्करण:**
   - `spring-boot-maven-plugin` को संस्करण `2.7.0` पर सेट किया गया है, जो Spring Boot 2.x के लिए डिज़ाइन किया गया है, Spring Boot 3.4.2 (एक 3.x संस्करण) के लिए नहीं। यह बेमेल बिल्ड और रनटाइम चरणों के दौरान समस्याएं पैदा कर सकता है।

2. **स्पष्ट असंगत Spring Framework Dependencies:**
   - `pom.xml` स्पष्ट रूप से `spring-aop` और `spring-aspects` को संस्करण `5.3.23` (Spring Framework 5.x) के साथ डिक्लेयर करता है, जबकि Spring Boot 3.4.2 को Spring Framework 6.1.14 की आवश्यकता होती है। Maven Spring Boot द्वारा प्रबंधित संस्करणों पर इन स्पष्ट रूप से घोषित संस्करणों को प्राथमिकता देता है, जिसके परिणामस्वरूप classpath पर Spring Framework 5.x और 6.x का मिश्रण होता है। यह मिश्रण `NoClassDefFoundError` का कारण बनता है क्योंकि `BeanRegistrationExcludeFilter` (Spring Framework 6.x से) अनुपलब्ध है जब पुराने 5.x jars लोड होते हैं।

### समाधान

समस्या को हल करने के लिए, हमें यह सुनिश्चित करने की आवश्यकता है कि प्रोजेक्ट के सभी घटक Spring Boot 3.4.2 के साथ संगत हैं और Spring Boot conflicts से बचने के लिए अपनी dependencies के संस्करणों को प्रबंधित करता है। `pom.xml` में निम्नलिखित परिवर्तन किए जाने चाहिए:

1. **Spring Boot Maven Plugin संस्करण अपडेट करें:**
   - `spring-boot-maven-plugin` संस्करण को `2.7.0` से `3.4.2` में बदलें ताकि यह प्रोजेक्ट में उपयोग किए जा रहे Spring Boot संस्करण के साथ संरेखित हो।

2. **स्पष्ट Spring Framework Dependencies हटाएँ:**
   - `spring-aop` और `spring-aspects` की स्पष्ट घोषणाओं को संस्करण `5.3.23` के साथ हटा दें। Spring Boot 3.4.2 इन dependencies को अपने starters (जैसे, `spring-boot-starter-web` में `spring-aop` सही संस्करण, 6.1.14 के साथ शामिल है) के माध्यम से प्रबंधित करता है। इन्हें हटाकर, हम Maven को Spring Boot के dependency management को ओवरराइड करने से रोकते हैं।

### अपडेट किया गया `pom.xml`

नीचे सुधारा गया `pom.xml` फ़ाइल है जिसमें आवश्यक परिवर्तन लागू किए गए हैं:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.lzwjava</groupId>
    <artifactId>blog-server</artifactId>
    <version>1.0</version>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <version>3.4.2</version>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-engine</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
            <version>5.3.1</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <version>3.4.2</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjrt</artifactId>
            <version>1.9.22</version>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjweaver</artifactId>
            <version>1.9.22</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>3.4.2</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0-M8</version>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-checkstyle-plugin</artifactId>
                <version>3.1.1</version>
                <configuration>
                    <configLocation>google_checks.xml</configLocation>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>check</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### परिवर्तनों की व्याख्या

- **Spring Boot Maven Plugin अपडेट:**
  - `spring-boot-maven-plugin` कॉन्फ़िगरेशन में `<version>2.7.0</version>` को `<version>3.4.2</version>` में बदल दिया गया है। यह सुनिश्चित करता है कि प्लगइन Spring Boot 3.4.2 के साथ संगत है, जो 3.x श्रृंखला के लिए विशिष्ट फीचर्स और कॉन्फ़िगरेशन का समर्थन करता है।

- **`spring-aop` और `spring-aspects` को हटाना:**
  - निम्नलिखित dependencies को हटा दिया गया है:
    ```xml
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-aop</artifactId>
        <version>5.3.23</version>
    </dependency>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-aspects</artifactId>
        <version>5.3.23</version>
    </dependency>
    ```
  - `spring-aop` पहले से ही `spring-boot-starter-web` (via `spring-web`) में शामिल है, और Spring Boot इसके संस्करण को 6.1.14 पर प्रबंधित करता है, जो 3.4.2 के साथ संगत है।
  - `spring-aspects` Spring Boot starters में एक मानक dependency नहीं है। यदि प्रोजेक्ट को इसकी स्पष्ट रूप से आवश्यकता है (जैसे, custom aspects के लिए), इसे बिना संस्करण के (Spring Boot के dependency management को इसे हैंडल करने देते हुए) फिर से जोड़ा जा सकता है या `6.1.14` पर सेट किया जा सकता है। हालाँकि, चूंकि त्रुटि स्टार्टअप के दौरान होती है और ऑटो-कॉन्फ़िगरेशन से संबंधित है न कि गायब aspects से, यहाँ यह संभावित रूप से अनावश्यक है और इसे सुरक्षित रूप से हटाया जा सकता है।

### अतिरिक्त नोट्स

- **AspectJ Dependencies:**
  - `aspectjrt` और `aspectjweaver` dependencies (संस्करण 1.9.22) `pom.xml` में बनी रहती हैं क्योंकि वे Spring Framework 6.1.14 के साथ संगत हैं और यदि प्रोजेक्ट AspectJ फीचर्स का उपयोग करता है तो उनकी आवश्यकता हो सकती है। ये Spring Boot 3.4.2 के साथ conflict नहीं करती हैं।

- **सर्वोत्तम अभ्यास:**
  - Spring Boot प्रोजेक्ट्स के लिए, dependency संस्करणों को स्वचालित रूप से प्रबंधित करने के लिए `spring-boot-starter-parent` को parent POM के रूप में उपयोग करने या `spring-boot-dependencies` BOM को इम्पोर्ट करने की सिफारिश की जाती है। वर्तमान `pom.xml` न तो करता है, लेकिन समाधान इस परिवर्तन की आवश्यकता के बिना काम करता है क्योंकि `spring-boot-starter-web` और अन्य starters संस्करण स्थिरता को लागू करते हैं जब स्पष्ट ओवरराइड्स हटा दिए जाते हैं।

- **सत्यापन:**
  - इन परिवर्तनों को लागू करने के बाद, यह सत्यापित करने के लिए कि एप्लिकेशन बिना त्रुटियों के शुरू होता है, `mvn clean spring-boot:run` चलाएं। यदि प्रोजेक्ट `spring-aspects` पर निर्भर करता है (जैसे, विशिष्ट AOP functionality के लिए), और इसे हटाने से समस्याएँ आती हैं, तो इसे `<version>6.1.14</version>` के साथ वापस जोड़ें या संस्करण को छोड़ दें और उचित dependency management सुनिश्चित करें।

### निष्कर्ष

`spring-boot-maven-plugin` को संस्करण 3.4.2 में अपडेट करके और स्पष्ट `spring-aop` और `spring-aspects` dependencies को हटाकर, प्रोजेक्ट Spring Boot (3.4.2) और Spring Framework (6.1.14) के सुसंगत संस्करणों का उपयोग करेगा। यह `NoClassDefFoundError` का कारण बनने वाले classpath conflict को हल करता है और एप्लिकेशन को सफलतापूर्वक शुरू होने की अनुमति देता है।