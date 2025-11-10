---
audio: false
generated: true
image: false
lang: hi
layout: post
title: वॉर बनाम ईयर पैकेजिंग गाइड
translated: true
type: note
---

यहाँ Maven के **WAR** और **EAR** पैकेजिंग की एक व्यावहारिक, तालिका-रहित तुलना है और बताया गया है कि आप वास्तविक प्रोजेक्ट्स में इनमें से प्रत्येक का उपयोग कैसे करेंगे।

# प्रत्येक पैकेजिंग किस लिए है

* **WAR (`packaging: war`)** – एक एकल वेब एप्लिकेशन: servlets/Jakarta REST, JSP/JSF, Spring MVC/Boot (WAR के रूप में), आदि। इसे एक सर्वलेट कंटेनर (Tomcat/Jetty) या एक पूर्ण ऐप सर्वर के वेब टियर में डिप्लॉय किया जाता है।
* **EAR (`packaging: ear`)** – एक पूर्ण Java EE/Jakarta EE ऐप सर्वर (WildFly/JBoss EAP, WebLogic, WebSphere) में एक साथ डिप्लॉय किए जाने वाले कई मॉड्यूल्स का एक बंडल। इसमें आमतौर पर एक या अधिक WAR, EJB JAR और साझा लाइब्रेरीज़ होती हैं, जो एक डिप्लॉयमेंट यूनिट बनाती हैं।

# आमतौर पर कब चुनें

* **WAR** चुनें यदि आपके पास एक एकल वेब ऐप या Spring Boot ऐप है और आपको EJB या मल्टी-मॉड्यूल सर्वर फीचर्स की आवश्यकता नहीं है।
* **EAR** चुनें यदि आपको कई मॉड्यूल्स को एक साथ डिप्लॉय करना है (जैसे, EJB + कई WAR + साझा लाइब्रेरी), मॉड्यूल्स में ऐप-सर्वर सर्विसेज (XA, केंद्रीकृत सुरक्षा क्षेत्र, JMS, वितरित लेनदेन) की आवश्यकता है, या आपकी संगठन नीति EAR की अनिवार्य करती है।

# आर्टिफैक्ट के अंदर क्या होता है

* **WAR** की सामग्री: `/WEB-INF/classes`, `/WEB-INF/lib`, वैकल्पिक `web.xml` (या एनोटेशन), स्टेटिक एसेट्स। अधिकांश सर्वर में प्रति WAR एक क्लासलोडर होता है।
* **EAR** की सामग्री: `*.war`, `*.jar` (EJB/यूटिलिटी), `META-INF/application.xml` (या एनोटेशन/स्किनी कॉन्फ़िग), और मॉड्यूल में साझा की जाने वाली लाइब्रेरी के लिए वैकल्पिक `lib/`। यह एक EAR-लेवल क्लासलोडर प्रदान करता है जो सभी मॉड्यूल के लिए दृश्यमान होता है।

# डिपेंडेंसी और क्लासलोडिंग संबंधी विचार

* **WAR**: सर्वलेट/Jakarta EE API को `provided` के रूप में डिक्लेयर करें; बाकी सब कुछ `/WEB-INF/lib` के अंतर्गत जाता है। आइसोलेशन सरल है; वर्जन क्लैश कम होते हैं।
* **EAR**: सामान्य लाइब्रेरी को EAR के `lib/` में रखें (`maven-ear-plugin` के माध्यम से), ताकि सभी मॉड्यूल एक ही वर्जन शेयर करें। मॉड्यूल लाइब्रेरी और सर्वर-प्रदत्त API के बीच कॉन्फ्लिक्ट पर ध्यान दें; वर्जन को अलाइन करें और जहाँ उचित हो `provided` का उपयोग करें।

# आपके द्वारा उपयोग किए जाने वाले Maven प्लगइन्स

* **WAR प्रोजेक्ट**: `maven-war-plugin`
* **EAR एग्रीगेटर**: `maven-ear-plugin`
* **EJB मॉड्यूल (यदि कोई हो)**: `maven-ejb-plugin`
* पैरेंट/एग्रीगेटर अक्सर मॉड्यूल को एक साथ जोड़ने के लिए `packaging: pom` का उपयोग करता है।

# न्यूनतम उदाहरण

सिंगल वेबऐप (WAR):

```xml
<!-- pom.xml -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId><artifactId>my-web</artifactId><version>1.0.0</version>
  <packaging>war</packaging>

  <dependencies>
    <!-- सर्वर API के लिए provided का उपयोग करें -->
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-web-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
    <!-- आपकी ऐप डिपेंडेंसी -->
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.4.0</version>
        <!-- वैकल्पिक: webResources, warName, filtering कॉन्फ़िगर करें -->
      </plugin>
    </plugins>
  </build>
</project>
```

एक WAR और एक EJB वाला मल्टी-मॉड्यूल EAR:

```xml
<!-- parent/pom.xml -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId><artifactId>my-app</artifactId><version>1.0.0</version>
  <packaging>pom</packaging>
  <modules>
    <module>ejb-module</module>
    <module>web-module</module>
    <module>ear-assembly</module>
  </modules>
</project>
```

```xml
<!-- ejb-module/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>ejb-module</artifactId>
  <packaging>ejb</packaging>
  <dependencies>
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
  </dependencies>
</project>
```

```xml
<!-- web-module/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>web-module</artifactId>
  <packaging>war</packaging>
  <dependencies>
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-web-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
    <dependency>
      <groupId>com.example</groupId><artifactId>ejb-module</artifactId><version>1.0.0</version>
      <type>ejb</type> <!-- @EJB इंजेक्शन की अनुमति देता है -->
    </dependency>
  </dependencies>
</project>
```

```xml
<!-- ear-assembly/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>ear-assembly</artifactId>
  <packaging>ear</packaging>

  <dependencies>
    <dependency>
      <groupId>com.example</groupId><artifactId>web-module</artifactId><version>1.0.0</version>
      <type>war</type>
    </dependency>
    <dependency>
      <groupId>com.example</groupId><artifactId>ejb-module</artifactId><version>1.0.0</version>
      <type>ejb</type>
    </dependency>
    <!-- सभी मॉड्यूल द्वारा साझा की जाने वाली लाइब्रेरी को EAR/lib में रखने के लिए -->
    <dependency>
      <groupId>com.fasterxml.jackson.core</groupId><artifactId>jackson-databind</artifactId>
      <version>2.17.2</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-ear-plugin</artifactId>
        <version>3.4.0</version>
        <configuration>
          <defaultLibBundleDir>lib</defaultLibBundleDir>
          <modules>
            <webModule>
              <groupId>com.example</groupId>
              <artifactId>web-module</artifactId>
              <contextRoot>/myapp</contextRoot>
            </webModule>
            <ejbModule>
              <groupId>com.example</groupId>
              <artifactId>ejb-module</artifactId>
            </ejbModule>
          </modules>
          <!-- वैकल्पिक: application.xml जनरेट करें, या कस्टम प्रदान करें -->
          <generateApplicationXml>true</generateApplicationXml>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

बिल्ड परिणाम:

* `mvn -pl web-module -am clean package` → `web-module-1.0.0.war`
* `mvn -pl ear-assembly -am clean package` → `ear-assembly-1.0.0.ear` जिसमें WAR, EJB और `lib/` शामिल है।

# महत्वपूर्ण ऑपरेशनल अंतर

* **डिप्लॉयमेंट टार्गेट**

  * WAR: सर्वलेट कंटेनर या ऐप सर्वर वेब टियर।
  * EAR: पूर्ण ऐप सर्वर; सभी मॉड्यूल को एटोमिक रूप से डिप्लॉय करता है।
* **ट्रांजैक्शन और मैसेजिंग**

  * WAR अकेले कंटेनर द्वारा एक्सपोज की गई चीजों का उपयोग करता है; जटिल XA/JMS सेटअप अक्सर EAR के भीतर EJB में होते हैं।
* **वर्जनिंग और रोलआउट**

  * WAR: एक एकल ऐप को रीबिल्ड और रीडिप्लॉय करना सरल है।
  * EAR: कई मॉड्यूल के वर्जन को कोऑर्डिनेट करता है; स्थिरता के लिए एक डिप्लॉयमेंट यूनिट।
* **स्टार्ट-अप टाइम और लोकल डेव**

  * WAR: फास्ट फीडबैक, लाइटर रनटाइम।
  * EAR: हैवियर; IDE/सर्वर इंटीग्रेशन मदद करता है लेकिन साइकिल धीमी होती हैं।
* **मॉडर्न Spring Boot नोट**

  * Boot एक्जीक्यूटेबल **JAR** को प्राथमिकता देता है; यदि आप बाहरी कंटेनर में डिप्लॉय करते हैं तो WAR सपोर्टेड है।
  * Boot **EAR** को टार्गेट नहीं करता; यदि आपको ऐप सर्वर का उपयोग करना ही है, तो Boot को WAR के रूप में डिप्लॉय करें, और तब तक EAR से बचें जब तक कि आपका प्लेटफ़ॉर्म इसकी आवश्यकता न हो।

# आम गलतियाँ और टिप्स

* सर्वर API को बंडल करने से बचने के लिए `provided` का उपयोग करें।
* EAR के लिए, प्रत्येक WAR/EJB के अंदर डुप्लिकेट कॉपी को रोकने के लिए साझा लाइब्रेरी को `defaultLibBundleDir` में रखें।
* मॉड्यूल में Jakarta EE वर्जन को अलाइन करें; मिसमैच के कारण क्लासलोडिंग एरर आते हैं।
* WebLogic/WebSphere पर, क्लासलोडर पॉलिसी (parent-first vs parent-last) का ध्यान रखें; कभी-कभी वेंडर-स्पेसिफिक डिस्क्रिप्टर की आवश्यकता होती है।
* यदि आपको EJB/XA की आवश्यकता नहीं है, तो एक सादा WAR (या Boot JAR) सरल और आमतौर पर अधिक पोर्टेबल होता है।

यदि आप मुझे अपना ऐप सर्वर (Tomcat vs WildFly/WebLogic/आदि) बताते हैं और यह भी बताते हैं कि क्या आपके पास EJB या एकाधिक वेबऐप हैं, तो मैं आपके लिए आवश्यक सटीक POM और डिप्लॉयमेंट डिस्क्रिप्टर का स्केच बना सकता हूँ।