---
audio: false
generated: true
lang: hi
layout: post
title: मेवन के साथ जावा सर्वलेट अनुप्रयोग
translated: true
type: note
---

यहाँ Maven का उपयोग करके प्रोजेक्ट बनाने और डिप्लॉयमेंट के लिए Liberty Maven प्लगइन का उपयोग करके WebSphere Liberty Profile (WLP) पर एक साधारण Java Servlet एप्लिकेशन बनाने और डिप्लॉय करने का एक संपूर्ण मार्गदर्शिका है। यह उदाहरण एक बुनियादी Servlet बनाता है जो एक्सेस करने पर "Hello World!" लौटाता है, इसे Maven के साथ एक WAR फ़ाइल में बनाता है, और इसे WLP पर डिप्लॉय करता है। हम मानकर चल रहे हैं कि आपने WLP को `servlet-4.0` फीचर के साथ सक्षम करके सेट अप कर लिया है, क्योंकि यह आवश्यक Servlet सपोर्ट प्रदान करता है।

---

## चरण-दर-चरण मार्गदर्शिका

### 1. Maven प्रोजेक्ट संरचना बनाएं
एक मानक Maven वेब एप्लिकेशन संरचना सेट अप करके शुरुआत करें। आप इसे मैन्युअल रूप से बना सकते हैं या इसे जनरेट करने के लिए Maven का उपयोग कर सकते हैं।

- **डायरेक्टरी संरचना:**
  ```
  SimpleServletApp/
  ├── pom.xml
  └── src/
      └── main/
          ├── java/
          │   └── com/
          │       └── example/
          │           └── HelloServlet.java
          └── webapp/
              └── WEB-INF/
                  └── web.xml
  ```

- **वैकल्पिक रूप से Maven के साथ जनरेट करें:**
  संरचना बनाने के लिए यह कमांड चलाएं, फिर आवश्यकतानुसार समायोजित करें:
  ```bash
  mvn archetype:generate -DgroupId=com.example -DartifactId=simple-servlet-app -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
  ```
  यह एक बुनियादी वेबएप संरचना बनाता है, जिसे आप अगले चरणों में संशोधित करेंगे।

### 2. Servlet कोड लिखें
`src/main/java/com/example/` में `HelloServlet.java` नाम की एक फ़ाइल बनाएं और निम्नलिखित सामग्री डालें:

```java
package com.example;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        resp.setContentType("text/plain");
        resp.getWriter().write("Hello World!");
    }
}
```

- **स्पष्टीकरण:** यह Servlet HTTP GET रिक्वेस्ट का जवाब "Hello World!" प्लेन टेक्स्ट में देता है। यह एक साधारण `doGet` मेथड का उपयोग करता है और एक्सप्लिसिट `web.xml` कॉन्फ़िगरेशन के लिए कंपैटिबिलिटी के लिए एनोटेशन से बचता है।

### 3. `web.xml` डिप्लॉयमेंट डिस्क्रिप्टर बनाएं
`src/main/webapp/WEB-INF/` में `web.xml` नाम की एक फ़ाइल बनाएं और निम्नलिखित सामग्री डालें:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
    <servlet>
        <servlet-name>HelloServlet</servlet-name>
        <servlet-class>com.example.HelloServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>HelloServlet</servlet-name>
        <url-pattern>/hello</url-pattern>
    </servlet-mapping>
</web-app>
```

- **स्पष्टीकरण:** `web.xml` फ़ाइल `HelloServlet` क्लास को परिभाषित करती है और इसे `/hello` URL पैटर्न पर मैप करती है। यह आवश्यक है क्योंकि हम `@WebServlet` एनोटेशन का उपयोग नहीं कर रहे हैं।

### 4. Maven `pom.xml` कॉन्फ़िगर करें
`SimpleServletApp/` डायरेक्टरी में `pom.xml` बनाएं या अपडेट करें और निम्नलिखित सामग्री डालें:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>simple-servlet-app</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <properties>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
    </properties>

    <dependencies>
        <!-- Servlet API (WLP द्वारा प्रदान किया गया) -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- WAR फ़ाइल बनाने के लिए Maven WAR प्लगइन -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <finalName>myapp</finalName>
                </configuration>
            </plugin>
            <!-- डिप्लॉयमेंट के लिए Liberty Maven प्लगइन -->
            <plugin>
                <groupId>io.openliberty.tools</groupId>
                <artifactId>liberty-maven-plugin</artifactId>
                <version>3.3.4</version>
                <configuration>
                    <installDirectory>/opt/ibm/wlp</installDirectory>
                    <serverName>myServer</serverName>
                    <appsDirectory>dropins</appsDirectory>
                    <looseApplication>false</looseApplication>
                    <stripVersion>true</stripVersion>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

- **स्पष्टीकरण:**
  - **कोऑर्डिनेट्स:** `groupId`, `artifactId`, और `version` के साथ प्रोजेक्ट को परिभाषित करता है। वेब एप्लिकेशन के लिए `packaging` को `war` पर सेट किया गया है।
  - **प्रॉपर्टीज़:** सोर्स और टार्गेट वर्जन के रूप में Java 8 सेट करता है।
  - **डिपेंडेंसीज़:** `provided` स्कोप के साथ Servlet API को शामिल करता है, क्योंकि यह रनटाइम पर WLP द्वारा सप्लाई किया जाता है।
  - **Maven WAR प्लगइन:** `<finalName>` का उपयोग करके WAR फ़ाइल का नाम `myapp.war` पर कॉन्फ़िगर करता है।
  - **Liberty Maven प्लगइन:** `/opt/ibm/wlp` पर एक Liberty सर्वर पर, सर्वर नाम `myServer`, `dropins` डायरेक्टरी में डिप्लॉय करने के लिए कॉन्फ़िगर करता है।

### 5. प्रोजेक्ट बिल्ड करें
`SimpleServletApp/` डायरेक्टरी से, Maven का उपयोग करके WAR फ़ाइल बनाएं:

```bash
mvn clean package
```

- **परिणाम:** यह Servlet को कंपाइल करता है, इसे `web.xml` के साथ `target/myapp.war` में पैकेज करता है, और इसे डिप्लॉयमेंट के लिए तैयार करता है।

### 6. WebSphere Liberty पर डिप्लॉय करें और रन करें
सुनिश्चित करें कि आपका Liberty सर्वर (`myServer`) `servlet-4.0` फीचर के साथ सक्षम करके सेट अप है। अपने `server.xml` में जांचें:
```xml
<featureManager>
    <feature>servlet-4.0</feature>
</featureManager>
```

Liberty Maven प्लगइन का उपयोग करके एप्लिकेशन को डिप्लॉय और रन करें:

```bash
mvn liberty:run
```

- **क्या होता है:**
  - Liberty सर्वर को फोरग्राउंड में शुरू करता है (यदि पहले से चल नहीं रहा है)।
  - `myapp.war` को `dropins` डायरेक्टरी में ऑटोमैटिकली डिप्लॉय करता है।
  - रोकने तक सर्वर को चलते रहने देता है।

- **डिप्लॉयमेंट सत्यापित करें:** इस तरह के एक लॉग मैसेज की तलाश करें:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  लॉग आमतौर पर `/opt/ibm/wlp/usr/servers/myServer/logs/console.log` में होते हैं।

### 7. एप्लिकेशन एक्सेस करें
एक ब्राउज़र खोलें और इस पर नेविगेट करें:

```
http://localhost:9080/myapp/hello
```

- **अपेक्षित आउटपुट:**
  ```
  Hello World!
  ```

- **URL ब्रेकडाउन:**
  - `9080`: WLP के लिए डिफ़ॉल्ट HTTP पोर्ट।
  - `/myapp`: WAR फ़ाइल नाम (`myapp.war`) से कॉन्टेक्स्ट रूट।
  - `/hello`: `web.xml` से URL पैटर्न।

### 8. सर्वर रोकें
चूंकि `mvn liberty:run` सर्वर को फोरग्राउंड में चलाता है, टर्मिनल में `Ctrl+C` दबाकर इसे रोकें।

---

## नोट्स
- **पूर्वापेक्षाएँ:**
  - Maven आपके सिस्टम पर इंस्टॉल और कॉन्फ़िगर होना चाहिए।
  - Liberty `/opt/ibm/wlp` पर इंस्टॉल होना चाहिए, और सर्वर इंस्टेंस `myServer` का अस्तित्व होना चाहिए। यदि आपका सेटअप अलग है (जैसे, `/usr/local/wlp` या `defaultServer`) तो `pom.xml` में `installDirectory` और `serverName` को एडजस्ट करें।
  - `servlet-4.0` फीचर `server.xml` में सक्षम होना चाहिए।

- **वैकल्पिक डिप्लॉयमेंट:**
  - अलग से बिल्ड और डिप्लॉय करने के लिए:
    ```bash
    mvn clean package
    mvn liberty:deploy
    ```
    यदि आवश्यक हो तो सर्वर को मैन्युअली शुरू करें:
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **पोर्ट कॉन्फ़िगरेशन:** यदि आपका Liberty सर्वर एक अलग HTTP पोर्ट का उपयोग करता है, तो `<httpEndpoint>` के लिए `server.xml` की जांच करें और URL को तदनुसार एडजस्ट करें।

- **कॉन्टेक्स्ट रूट:** कॉन्टेक्स्ट रूट को `/app` में बदलने के लिए `pom.xml` में `<finalName>` का नाम बदलें (उदाहरण के लिए, `<finalName>app</finalName>`)।

- **समस्या निवारण:**
  - यदि डिप्लॉयमेंट फेल हो जाता है, तो `pom.xml` में `installDirectory` और `serverName` को सत्यापित करें।
  - त्रुटियों के लिए `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` पर लॉग की जांच करें।
  - सुनिश्चित करें कि Java 8 या बाद का उपयोग किया गया है, जो `maven.compiler` सेटिंग्स से मेल खाता हो।

---

## सारांश
यह मार्गदर्शिका प्रदर्शित करती है कि कैसे:
1. एक साधारण Servlet (`HelloServlet.java`) और `web.xml` के साथ एक Maven प्रोजेक्ट सेट अप करें।
2. Servlet API, Maven WAR प्लगइन, और Liberty Maven प्लगइन के साथ `pom.xml` को कॉन्फ़िगर करें।
3. `mvn clean package` का उपयोग करके एप्लिकेशन को `myapp.war` में बिल्ड करें।
4. `mvn liberty:run` का उपयोग करके इसे WLP पर डिप्लॉय और रन करें।
5. `http://localhost:9080/myapp/hello` पर "Hello World!" एक्सेस करें।

यह WebSphere Liberty Profile पर एक Servlet एप्लिकेशन को डेवलप और डिप्लॉय करने के लिए एक स्ट्रीमलाइन्ड, Maven-आधारित दृष्टिकोण प्रदान करता है।