---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: मेवेन वार और ईयर मॉड्यूल सेटअप
translated: true
type: note
---

### WAR को EAR में बदलने के लिए Maven मल्टी-मॉड्यूल प्रोजेक्ट सेटअप

Maven में, एक मॉड्यूल को WAR (उदाहरण के लिए, एक वेब एप्लिकेशन) बनाने और दूसरे मॉड्यूल द्वारा उसे EAR (एंटरप्राइज आर्काइव) में असेंबल करने के लिए, मल्टी-मॉड्यूल प्रोजेक्ट स्ट्रक्चर का उपयोग करें। EAR मॉड्यूल `maven-ear-plugin` के माध्यम से WAR मॉड्यूल पर निर्भर करता है। यह सुनिश्चित करता है कि बिल्ड के दौरान WAR, EAR में शामिल हो जाए।

#### चरण 1: पैरेंट POM बनाएं
पैरेंट POM मॉड्यूल्स को परिभाषित करता है और साझा कॉन्फ़िगरेशन प्रबंधित करता है। इसके पैकेजिंग को `pom` पर सेट करें।

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>parent</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <modules>
        <module>web-module</module>  <!-- इसे पहले बिल्ड करें -->
        <module>ear-module</module>
    </modules>

    <!-- वैकल्पिक: साझा निर्भरताएं और प्लगइन वर्जन -->
    <dependencyManagement>
        <dependencies>
            <!-- चाइल्ड मॉड्यूल्स के लिए वर्जन यहाँ परिभाषित करें -->
        </dependencies>
    </dependencyManagement>

    <build>
        <pluginManagement>
            <plugins>
                <!-- प्लगइन वर्जन प्रबंधित करें -->
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-ear-plugin</artifactId>
                    <version>3.3.0</version>
                </plugin>
            </plugins>
        </pluginManagement>
    </build>
</project>
```

#### चरण 2: WAR मॉड्यूल कॉन्फ़िगर करें
यह मॉड्यूल वेब एप्लिकेशन को WAR के रूप में बनाता है। इसके पैकेजिंग को `war` पर सेट करें। यहाँ किसी विशेष EAR कॉन्फ़िगरेशन की आवश्यकता नहीं है—इसे केवल पहले बिल्ड होने की आवश्यकता है।

डायरेक्टरी स्ट्रक्चर: `web-module/pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>web-module</artifactId>
    <packaging>war</packaging>

    <dependencies>
        <!-- अपनी वेब निर्भरताएं जोड़ें, उदा., servlet-api -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.2</version>
            </plugin>
        </plugins>
    </build>
</project>
```

#### चरण 3: EAR मॉड्यूल कॉन्फ़िगर करें
यह मॉड्यूल EAR को असेंबल करता है। इसके पैकेजिंग को `ear` पर सेट करें और WAR मॉड्यूल को संदर्भित करने के लिए `maven-ear-plugin` का उपयोग करें। प्लगइन WAR आर्टिफैक्ट को खींचेगा और उसे EAR में बंडल कर देगा।

डायरेक्टरी स्ट्रक्चर: `ear-module/pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>ear-module</artifactId>
    <packaging>ear</packaging>

    <dependencies>
        <!-- बिल्ड में इसे शामिल करने के लिए WAR मॉड्यूल पर निर्भर रहें -->
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>web-module</artifactId>
            <version>${project.version}</version>
            <type>war</type>
        </dependency>
        <!-- वैकल्पिक: यदि आवश्यक हो तो EJB या अन्य मॉड्यूल जोड़ें -->
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-ear-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <!-- EAR वर्जन (उदा., Java EE के लिए) -->
                    <version>8</version>
                    
                    <!-- EAR में लाइब्रेरीज़ के लिए डायरेक्टरी -->
                    <defaultLibBundleDir>lib</defaultLibBundleDir>
                    
                    <!-- स्किनी WARs (उन निर्भरताओं को बाहर करें जो पहले से ही EAR लाइब्स में हैं) -->
                    <skinnyWars>true</skinnyWars>
                    
                    <!-- शामिल करने के लिए मॉड्यूल्स को परिभाषित करें -->
                    <modules>
                        <webModule>
                            <groupId>com.example</groupId>
                            <artifactId>web-module</artifactId>
                            <bundleDir>/</bundleDir>  <!-- EAR का रूट -->
                            <contextRoot>/mywebapp</contextRoot>  <!-- डिप्लॉयमेंट कॉन्टेक्स्ट -->
                        </webModule>
                        <!-- यदि आवश्यक हो तो अधिक <ejbModule> या <jarModule> जोड़ें -->
                    </modules>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### चरण 4: प्रोजेक्ट बिल्ड करें
- **पैरेंट डायरेक्टरी** से रन करें: `mvn clean install`
  - यह मॉड्यूल्स को क्रम में बिल्ड करता है (पहले WAR, फिर EAR)।
- EAR, `ear-module/target/ear-module-1.0-SNAPSHOT.ear` में होगी।
- केवल EAR बिल्ड करने के लिए (मान लें कि WAR पहले से ही बिल्ड है): `cd ear-module && mvn clean package`.

#### मुख्य नोट्स
- **बिल्ड ऑर्डर**: Maven द्वारा WAR को पहले बिल्ड करना सुनिश्चित करने के लिए पैरेंट के `<modules>` में WAR मॉड्यूल को EAR से पहले सूचीबद्ध करें।
- **निर्भरताएं**: WAR पर EAR मॉड्यूल की `<dependency>` यह सुनिश्चित करती है कि यह पैकेजिंग के दौरान रिज़ॉल्व हो जाए।
- **कस्टमाइज़ेशन**: वेब ऐप के URL पथ के लिए `<contextRoot>` एडजस्ट करें। `<modules>` में अधिक मॉड्यूल (उदा., EJB JARs) जोड़ें।
- **समस्या निवारण**: यदि WAR शामिल नहीं है, तो जांचें कि आर्टिफैक्ट कोऑर्डिनेट्स बिल्कुल मेल खाते हैं। सत्यापित करने के लिए EAR मॉड्यूल में `mvn dependency:tree` का उपयोग करें।

अधिक जानकारी के लिए, ऑफिशियल Maven EAR plugin डॉक्यूमेंटेशन देखें।

[Apache Maven EAR Plugin](https://maven.apache.org/plugins/maven-ear-plugin/)  
[Maven Multi-Module Projects](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#Multi-module_Projects)