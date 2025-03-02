---
audio: false
generated: true
lang: hi
layout: post
title: Java Servlet Application with Maven का अनुवाद
translated: true
---

यह एक पूर्ण मार्गदर्शिका है WebSphere Liberty Profile (WLP) पर एक सरल Java Servlet अनुप्रयोग बनाने और डिप्लॉय करने के लिए, जिसमें Maven को प्रोजेक्ट बनाने के लिए और Liberty Maven प्लगइन को डिप्लॉय करने के लिए उपयोग किया जाता है। इस उदाहरण में, एक बुनियादी Servlet बनाया जाता है जो "Hello World!" लौटाता है जब उसे एक्सेस किया जाता है, इसे Maven के साथ एक WAR फ़ाइल में बनाया जाता है, और इसे WLP पर डिप्लॉय किया जाता है। हम मानते हैं कि आपने पहले से ही WLP को `servlet-4.0` फीचर के साथ सेट अप कर लिया है, क्योंकि यह आवश्यक Servlet समर्थन प्रदान करता है।

---

## चरण-दर-चरण मार्गदर्शिका

### 1. Maven प्रोजेक्ट संरचना बनाएं
एक मानक Maven वेब अनुप्रयोग संरचना सेट अप करने से शुरू करें। आप इसे मैन्युअल रूप से या Maven का उपयोग करके बना सकते हैं।

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

- **मैन्युअल रूप से बनाएं:**
  इस कमांड को चलाएं संरचना को बनाने के लिए, फिर आवश्यकतानुसार समायोजित करें:
  ```bash
  mvn archetype:generate -DgroupId=com.example -DartifactId=simple-servlet-app -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
  ```
  यह एक बुनियादी वेबएप संरचना बनाता है, जिसे आप अगले चरणों में संशोधित करेंगे।

### 2. Servlet कोड लिखें
`src/main/java/com/example/` में `HelloServlet.java` नामक एक फ़ाइल बनाएं, जिसमें निम्नलिखित सामग्री हो:

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

- **विवरण:** यह Servlet HTTP GET अनुरोधों को "Hello World!" के साथ प्लेन टेक्स्ट में जवाब देता है। यह एक सरल `doGet` विधि का उपयोग करता है और अनुप्रयोग के साथ अनुकूलित होने के लिए `@WebServlet` अनुप्रयोगों को छोड़ देता है।

### 3. `web.xml` डिप्लॉयमेंट डिस्क्रिप्टर बनाएं
`src/main/webapp/WEB-INF/` में `web.xml` नामक एक फ़ाइल बनाएं, जिसमें निम्नलिखित सामग्री हो:

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

- **विवरण:** `web.xml` फ़ाइल `HelloServlet` वर्ग को और इसे `/hello` URL पैटर्न से मैप करता है। यह आवश्यक है क्योंकि हम `@WebServlet` अनुप्रयोगों का उपयोग नहीं कर रहे हैं।

### 4. Maven `pom.xml` को कॉन्फ़िगर करें
`SimpleServletApp/` डायरेक्टरी में `pom.xml` बनाएं या निम्नलिखित सामग्री के साथ अपडेट करें:

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
        <!-- Servlet API (provided by WLP) -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Maven WAR Plugin to build the WAR file -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <finalName>myapp</finalName>
                </configuration>
            </plugin>
            <!-- Liberty Maven Plugin for deployment -->
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

- **विवरण:**
  - **कोर्डिनेट्स:** प्रोजेक्ट को `groupId`, `artifactId`, और `version` के साथ परिभाषित करता है। `packaging` को `war` के लिए सेट किया गया है वेब अनुप्रयोग के लिए।
  - **गुण:** Java 8 को स्रोत और लक्ष्य संस्करण के रूप में सेट करता है।
  - **अनुप्रयोग:** Servlet API को `provided` स्कोप के साथ शामिल करता है, क्योंकि यह WLP द्वारा रनटाइम पर प्रदान किया जाता है।
  - **Maven WAR प्लगइन:** WAR फ़ाइल का नाम `myapp.war` को सेट करता है `<finalName>` का उपयोग करके।
  - **Liberty Maven प्लगइन:** डिप्लॉयमेंट को `/opt/ibm/wlp` पर एक Liberty सर्वर पर कॉन्फ़िगर करता है, सर्वर नाम `myServer`, `dropins` डायरेक्टरी में डिप्लॉय करता है।

### 5. प्रोजेक्ट बनाएं
`SimpleServletApp/` डायरेक्टरी से Maven का उपयोग करके WAR फ़ाइल बनाएं:

```bash
mvn clean package
```

- **परिणाम:** यह Servlet को कॉम्पाइल करता है, इसे `web.xml` के साथ `target/myapp.war` में पैक करता है, और इसे डिप्लॉय करने के लिए तैयार करता है।

### 6. WebSphere Liberty पर डिप्लॉय और चलाएं
सुरक्षित करें कि आपका Liberty सर्वर (`myServer`) `servlet-4.0` फीचर के साथ सेट अप किया गया है। `server.xml` में निम्नलिखित को जांचें:
```xml
<featureManager>
    <feature>servlet-4.0</feature>
</featureManager>
```

Liberty Maven प्लगइन का उपयोग करके अनुप्रयोग को डिप्लॉय और चलाएं:

```bash
mvn liberty:run
```

- **क्या होता है:**
  - सर्वर को फॉरग्राउंड में शुरू करता है (अगर पहले से चल रहा नहीं है).
  - `myapp.war` को `dropins` डायरेक्टरी में स्वचालित रूप से डिप्लॉय करता है।
  - सर्वर को रोकने तक चलता रहता है।

- **डिप्लॉयमेंट की पुष्टि करें:** एक लॉग संदेश जैसा देखें:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  लॉग आम तौर पर `/opt/ibm/wlp/usr/servers/myServer/logs/console.log` में होते हैं।

### 7. अनुप्रयोग तक पहुंचें
एक ब्राउज़र खोलें और निम्नलिखित पर जाएं:

```
http://localhost:9080/myapp/hello
```

- **अपेक्षित आउटपुट:**
  ```
  Hello World!
  ```

- **URL का विश्लेषण:**
  - `9080`: WLP के लिए डिफ़ॉल्ट HTTP पोर्ट.
  - `/myapp`: WAR फ़ाइल नाम (`myapp.war`) से कॉन्टेक्स्ट रूट.
  - `/hello`: `web.xml` से URL पैटर्न.

### 8. सर्वर को रोकें
`mvn liberty:run` सर्वर को फॉरग्राउंड में चलाता है, इसलिए इसे टर्मिनल में `Ctrl+C` दबाकर रोकें।

---

## टिप्पणियाँ
- **प्रारंभिक आवश्यकताएँ:**
  - Maven को आपके सिस्टम पर स्थापित और कॉन्फ़िगर किया जाना चाहिए।
  - Liberty को `/opt/ibm/wlp` पर स्थापित किया जाना चाहिए, और सर्वर इंस्टेंस `myServer` होना चाहिए। `installDirectory` और `serverName` को `pom.xml` में समायोजित करें अगर आपका सेटअप अलग है (जैसे `/usr/local/wlp` या `defaultServer`).
  - `server.xml` में `servlet-4.0` फीचर को सक्षम किया जाना चाहिए।

- **अल्टर्नेटिव डिप्लॉयमेंट:**
  - अलग से बनाएं और डिप्लॉय करें:
    ```bash
    mvn clean package
    mvn liberty:deploy
    ```
    आवश्यकता हो तो सर्वर को मैन्युअल रूप से शुरू करें:
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **पोर्ट कॉन्फ़िगरेशन:** अगर आपका Liberty सर्वर एक अलग HTTP पोर्ट का उपयोग करता है, तो `server.xml` में `<httpEndpoint>` को जांचें और URL को अनुकूलित करें।

- **कॉन्टेक्स्ट रूट:** `pom.xml` में `<finalName>` को बदलें (जैसे `<finalName>app</finalName>`) कॉन्टेक्स्ट रूट को `/app` में बदलने के लिए।

- **संघर्ष:** अगर डिप्लॉयमेंट विफल हो जाता है, तो `pom.xml` में `installDirectory` और `serverName` को सत्यापित करें। लॉग को `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` में त्रुटियों के लिए जांचें। सुनिश्चित करें कि Java 8 या बाद का उपयोग किया जाता है, `maven.compiler` सेटिंग्स के साथ मेल खाता है।

---

## सारांश
यह मार्गदर्शिका दिखाता है कि कैसे:
1. एक Maven प्रोजेक्ट को एक सरल Servlet (`HelloServlet.java`) और `web.xml` के साथ सेट अप करें।
2. `pom.xml` को Servlet API, Maven WAR प्लगइन, और Liberty Maven प्लगइन के साथ कॉन्फ़िगर करें।
3. अनुप्रयोग को `mvn clean package` का उपयोग करके `myapp.war` में बनाएं।
4. इसे WLP पर `mvn liberty:run` का उपयोग करके डिप्लॉय और चलाएं।
5. "Hello World!" को `http://localhost:9080/myapp/hello` पर पहुंचें।

यह एक स्ट्रीमलाइन, Maven आधारित तरीका प्रदान करता है Servlet अनुप्रयोग को WebSphere Liberty Profile पर विकसित और डिप्लॉय करने के लिए।