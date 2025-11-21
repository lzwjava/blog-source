---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4.1-fast
title: वास वातावरण विन्यास के लिए मेवेन प्रोफाइल्स
translated: true
type: note
---

आईबीएम वेबस्फीयर एप्लिकेशन सर्वर (पारंपरिक WAS, लिबर्टी नहीं) के लिए, मानक पैकेजिंग एक **EAR** फ़ाइल होती है (यहां तक कि सरल वेब ऐप्स के लिए भी, क्योंकि WAS स्टैंडअलोन WAR पर EAR को प्राथमिकता देता है)। विभिन्न वातावरणों को हैंडल करने का सर्वोत्तम अभ्यास — जैसे स्थानीय विकास (परीक्षण के लिए फिक्स्ड/हार्डकोडेड लॉगिन उपयोगकर्ता) बनाम सर्वर/प्रोडक्शन (SSO या उचित सुरक्षा रियल्म) — एक ही `pom.xml` में **Maven बिल्ड प्रोफाइल** का उपयोग करना है। यह कई अलग-अलग POM फ़ाइलों (जैसे, `pom.xml` और `build_pom.xml`) को बनाए रखने से बचाता है, जो त्रुटि-प्रवण है और मावेन के लिए स्वाभाविक नहीं है।

### एकाधिक POMs के बजाय प्रोफाइल क्यों?
- एक ही स्रोत सत्य (सिंगल POM)।
- आसान सक्रियण: `mvn package -Plocal` या `mvn package -Pserver`।
- प्रोफाइल संसाधनों को फ़िल्टर कर सकती हैं, फ़ाइलों को ओवरराइड कर सकती हैं, प्लगइन कॉन्फ़िगरेशन बदल सकती हैं, या बाइंडिंग्स को एडजस्ट कर सकती हैं (जैसे, WAS-विशिष्ट ऑथ के लिए `ibm-web-bnd.xml`, `ibm-application-ext.xml`)।
- आमतौर पर डेव/टेस्ट/प्रोड अंतरों के लिए उपयोग किया जाता है, जिसमें प्रमाणीकरण सेटअप शामिल हैं।

### अनुशंसित संरचना
कॉन्फ़िगरेशन फ़ाइलों (जैसे, `web.xml`, `properties` फ़ाइलें, Spring सुरक्षा कॉन्फ़िग, या WAS बाइंडिंग्स) को स्वैप करने के लिए फ़िल्टरिंग + प्रोफाइल-विशिष्ट संसाधन निर्देशिकाओं के साथ Maven संसाधन प्लगइन का उपयोग करें।

निर्देशिका लेआउट उदाहरण:
```
src/
├── main/
│   ├── resources/          (सामान्य कॉन्फ़िग)
│   ├── webapp/
│   │   ├── WEB-INF/
│   │   │   ├── web.xml      (सामान्य या आधार संस्करण)
│   │   │   └── ibm-web-bnd.xml (वैकल्पिक, JNDI/ऑथ बाइंडिंग के लिए)
│   └── ...
├── local/                   (प्रोफाइल-विशिष्ट संसाधन, केवल स्थानीय के लिए कॉपी/फ़िल्टर किए गए)
│   └── webapp/
│       └── WEB-INF/
│           ├── web.xml      (फॉर्म-लॉगिन + हार्डकोडेड उपयोगकर्ता/भूमिका या कोई सुरक्षा नहीं के साथ स्थानीय संस्करण)
│           └── ...
└── server/                  (प्रोडक्शन/SSO के लिए प्रोफाइल-विशिष्ट)
    └── webapp/
        └── WEB-INF/
            ├── web.xml      (SSO के लिए <login-config><auth-method>CLIENT-CERT</auth-method> या SPNEGO के साथ सर्वर संस्करण)
            └── ...
```

### उदाहरण pom.xml स्निपेट
```xml
<project ...>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>my-was-app</artifactId>
    <version>1.0.0</version>
    <packaging>ear</packaging>   <!-- या war यदि आप WAR के रूप में डिप्लॉय करते हैं, लेकिन WAS के लिए EAR प्राथमिकता प्राप्त है -->

    <properties>
        <maven.compiler.source>11</maven.compiler.source> <!-- या आपका Java वर्जन -->
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- आपके ऐप डिपेंडेंसी -->
        <!-- WAS कंपाइल-टाइम APIs के लिए (provided स्कोप) -->
        <dependency>
            <groupId>com.ibm.tools.target</groupId>
            <artifactId>was</artifactId>
            <version>9.0</version> <!-- अपने WAS वर्जन से मिलाएं, जैसे, 8.5.5 या 9.0 -->
            <type>pom</type>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- EAR बनाएं (WAR के लिए एडजस्ट करें यदि जरूरत हो) -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-ear-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <!-- आपका EAR कॉन्फ़िग, मॉड्यूल्स, आदि -->
                </configuration>
            </plugin>

            <!-- संसाधन फ़िल्टरिंग और प्रोफाइल-विशिष्ट ओवरराइड्स -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-resources-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <useDefaultDelimiters>true</useDefaultDelimiters>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <!-- प्रोफाइल्स -->
    <profiles>
        <!-- स्थानीय/डेव प्रोफाइल: फिक्स्ड उपयोगकर्ता, फॉर्म लॉगिन या कोई सुरक्षा नहीं -->
        <profile>
            <id>local</id>
            <activation>
                <activeByDefault>true</activeByDefault> <!-- स्थानीय बिल्ड्स के लिए डिफ़ॉल्ट -->
            </activation>
            <build>
                <resources>
                    <!-- सामान्य संसाधन -->
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                    <!-- स्थानीय-विशिष्ट फ़ाइलों के साथ ओवरराइड करें -->
                    <resource>
                        <directory>src/local/webapp</directory>
                        <targetPath>${project.build.directory}/${project.artifactId}/WEB-INF</targetPath>
                    </resource>
                </resources>
            </build>
            <properties>
                <!-- स्थानीय हार्डकोडेड उपयोगकर्ता के लिए उदाहरण फ़िल्टर्ड गुण -->
                <app.login.user>devuser</app.login.user>
                <app.login.password>devpass</app.login.password>
            </properties>
        </profile>

        <!-- सर्वर/प्रोड प्रोफाइल: रियल SSO (जैसे, SPNEGO, LTPA, या OpenIDConnect) -->
        <profile>
            <id>server</id>
            <build>
                <resources>
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                    <resource>
                        <directory>src/server/webapp</directory>
                        <targetPath>${project.build.directory}/${project.artifactId}/WEB-INF</targetPath>
                    </resource>
                </resources>
            </build>
            <properties>
                <!-- प्रोड गुण, जैसे, SSO फ्लैग्स सक्षम करें -->
                <app.auth.method>SSO</app.auth.method>
            </properties>
        </profile>
    </profiles>
</project>
```

### प्रमाणीकरण अंतरों के लिए मुख्य बिंदु
- **स्थानीय**: `web.xml` या प्रॉपर्टीज़ फ़ाइल में सरल उपयोगकर्ताओं/भूमिकाओं के साथ FORM लॉगिन का उपयोग करें, या सुरक्षा को पूरी तरह से अक्षम करें (`<security-constraint>` हटा दिया गया)।
- **सर्वर**: `web.xml` में WAS-विशिष्ट SSO कॉन्फ़िगर करें (जैसे, SPNEGO के साथ `<auth-method>FORM</auth-method>`, या लिबर्टी-स्टाइल में OpenID Connect फीचर का उपयोग करें, लेकिन पारंपरिक WAS के लिए अक्सर LTPA + ग्लोबल सिक्योरिटी रियल्म)। उपयोगकर्ता/भूमिका मैपिंग के लिए WAS बाइंडिंग्स (`ibm-web-bnd.xml`) को भी प्रति प्रोफाइल ओवरराइड किया जा सकता है।
- यदि Spring Security या इसी तरह का उपयोग कर रहे हैं, तो `applicationContext-security.xml` या प्रॉपर्टीज़ को उसी तरह स्वैप करें।
- हार्डकोडेड स्थानीय उपयोगकर्ता के लिए: रियल हार्डकोडेड क्रेडेंशियल्स से बचें; एक स्थानीय `users.properties` में मैप किए गए टेस्ट उपयोगकर्ता का उपयोग करें या एक फ्लैग के माध्यम से ऑथ चेक को अक्षम करें।

### बिल्ड कमांड्स
- स्थानीय (डिफ़ॉल्ट): `mvn clean package`
- सर्वर/प्रोड: `mvn clean package -Pserver`

यह **एक ही कोडबेस** से प्रत्येक वातावरण के लिए तैयार किए गए अलग-अलग EARs का उत्पादन करता है। यदि आपको वास्तव में अलग-अलग आर्टिफैक्ट नामों (जैसे, `myapp-local.ear` बनाम `myapp.ear`) की आवश्यकता है, तो प्रोफाइल-विशिष्ट `<build>` सेक्शन में `<finalName>${project.artifactId}-${profile}</finalName>` जोड़ें।

[Maven प्रोफाइल गाइड](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)  
[Maven EAR प्लगइन](https://maven.apache.org/plugins/maven-ear-plugin/)  
[IBM WAS Maven इंटीग्रेशन](https://www.ibm.com/docs/en/wasdtfe/9.7.0?topic=suye-configuring-dependency-pom-files-that-emulate-classpath-specific-websphere-runtime-environments)