---
audio: false
generated: true
lang: hi
layout: post
title: 'Java Servlet Application on WebSphere Liberty Profile का अनुवाद:


  Java Servlet Application on WebSphere Liberty Profile'
translated: true
---

यह एक पूर्ण गाइड है WebSphere Liberty Profile (WLP) पर एक बहुत ही सरल Java Servlet एप्लिकेशन चलाने के लिए। इस उदाहरण में, एक बेसिक Servlet बनाया जाता है जो "Hello World!" लौटाता है और इसे `dropins` डायरेक्टरी का उपयोग करके WLP पर डिप्लॉय किया जाता है। हम मानते हैं कि आपने पहले से ही WLP को `servlet-4.0` फीचर के साथ सेट अप कर लिया है, क्योंकि यह आवश्यक Servlet समर्थन प्रदान करता है। इस गाइड में Maven का उपयोग नहीं किया गया है और सभी आवश्यक कोड और डिप्लॉयमेंट कदम प्रदान किए गए हैं।

---

### कदम-दर-कदम गाइड

#### 1. Servlet एप्लिकेशन संरचना बनाएं
अपने Servlet एप्लिकेशन के लिए एक डायरेक्टरी संरचना को हाथ से बनाएं। आप किसी भी फोल्डर नाम का उपयोग कर सकते हैं, लेकिन इस उदाहरण के लिए, हम इसे `SimpleServletApp` कहेंगे।

- **डायरेक्टरी संरचना:**
  ```
  SimpleServletApp/
  ├── src/
  │   └── com/
  │       └── example/
  │           └── HelloServlet.java
  └── webapp/
      └── WEB-INF/
          └── web.xml
  ```

#### 2. Servlet कोड लिखें
`SimpleServletApp/src/com/example/` में `HelloServlet.java` नामक एक फाइल बनाएं, जिसमें निम्नलिखित सामग्री हो:

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

- **विवरण:** यह Servlet HTTP GET अनुरोधों का जवाब "Hello World!" के साथ plain text में देता है। हम एक सरल `doGet` विधि का उपयोग कर रहे हैं बिना एनोटेशन के अधिकतम संगतता और सरलता के लिए।

#### 3. `web.xml` डिप्लॉयमेंट डिस्क्रिप्टर बनाएं
`SimpleServletApp/webapp/WEB-INF/` में `web.xml` नामक एक फाइल बनाएं, जिसमें निम्नलिखित सामग्री हो:

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

- **विवरण:** `web.xml` फाइल `HelloServlet` क्लास को `/hello` URL पैटर्न से मैप करता है। यह आवश्यक है क्योंकि हम एनोटेशन जैसे `@WebServlet` का उपयोग नहीं कर रहे हैं।

#### 4. Servlet को कम्पाइल करें
`HelloServlet.java` फाइल को `javac` का उपयोग करके एक `.class` फाइल में कम्पाइल करें। आपको `javax.servlet-api` लाइब्रेरी को अपने क्लासपाथ में रखना होगा, जो WLP द्वारा प्रदान की जाती है लेकिन कम्पाइलेशन के दौरान उपलब्ध होना चाहिए।

- **कदम:**
  1. WLP इंस्टॉलेशन में Servlet API JAR को खोजें। उदाहरण के लिए, अगर WLP `/opt/ibm/wlp` पर इंस्टॉल है, तो JAR आमतौर पर यहाँ होता है:
     ```
     /opt/ibm/wlp/dev/api/spec/com.ibm.websphere.javaee.servlet.4.0_1.0.x.jar
     ```
     फाइल नाम WLP संस्करण पर आधारित हो सकता है।
  2. `SimpleServletApp` डायरेक्टरी से निम्न कमांड चलाएं:
     ```bash
     javac -cp "/opt/ibm/wlp/dev/api/spec/com.ibm.websphere.javaee.servlet.4.0_1.0.x.jar" src/com/example/HelloServlet.java
     ```
  3. यह `SimpleServletApp/src/com/example/` में `HelloServlet.class` बनाता है।

#### 5. एप्लिकेशन को एक WAR फाइल में पैकेज करें
कम्पाइल किए गए फाइलों को संगठित करें और एक WAR फाइल को हाथ से बनाएं।

- **कम्पाइल किए गए क्लास को स्थानांतरित करें:**
  एक `WEB-INF/classes` डायरेक्टरी बनाएं और कम्पाइल किए गए क्लास फाइलें स्थानांतरित करें:
  ```bash
  mkdir -p webapp/WEB-INF/classes/com/example
  mv src/com/example/HelloServlet.class webapp/WEB-INF/classes/com/example/
  ```

- **WAR फाइल बनाएं:**
  `SimpleServletApp` डायरेक्टरी से, `jar` कमांड का उपयोग करके `webapp` फोल्डर को एक WAR फाइल में पैकेज करें:
  ```bash
  cd webapp
  jar -cvf ../myapp.war .
  cd ..
  ```
  यह `SimpleServletApp` डायरेक्टरी में `myapp.war` बनाता है।

#### 6. WAR फाइल को WLP पर डिप्लॉय करें
WLP पर WAR फाइल को `dropins` डायरेक्टरी का उपयोग करके स्वचालित डिप्लॉयमेंट के लिए डिप्लॉय करें।

- **`dropins` डायरेक्टरी को खोजें:**
  WLP सर्वर की `dropins` डायरेक्टरी को खोजें। अगर WLP `/opt/ibm/wlp` पर इंस्टॉल है और आपका सर्वर `myServer` कहलाता है, तो पथ है:
  ```
  /opt/ibm/wlp/usr/servers/myServer/dropins
  ```

- **WAR फाइल को कॉपी करें:**
  WAR फाइल को `dropins` डायरेक्टरी में स्थानांतरित करें:
  ```bash
  cp myapp.war /opt/ibm/wlp/usr/servers/myServer/dropins/
  ```

- **सर्वर को शुरू करें (अगर चल रहा नहीं है):**
  अगर WLP चल नहीं रहा है, तो इसे शुरू करें:
  ```bash
  /opt/ibm/wlp/bin/server start myServer
  ```
  अगर यह पहले से चल रहा है, तो यह WAR फाइल को स्वचालित रूप से डिटेक्ट और डिप्लॉय करेगा।

- **डिप्लॉयमेंट की पुष्टि करें:**
  सर्वर लॉग या कंसोल में एक संदेश जैसे के लिए देखें:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  लॉग `/opt/ibm/wlp/usr/servers/myServer/logs/console.log` में हैं।

#### 7. एप्लिकेशन तक पहुंचें
एक ब्राउज़र में डिप्लॉय किए गए Servlet को टेस्ट करें।

- **अपना ब्राउज़र खोलें:**
  निम्नलिखित पर जाएं:
  ```
  http://localhost:9080/myapp/hello
  ```
  - `9080` WLP का डिफॉल्ट HTTP पोर्ट है।
  - `/myapp` WAR फाइल नाम से कंटेक्स्ट रूट है।
  - `/hello` `web.xml` में परिभाषित URL पैटर्न है।

- **अपेक्षित परिणाम:**
  आप निम्नलिखित को plain text के रूप में देखेंगे:
  ```
  Hello World!
  ```

---

### नोट्स
- **कोई JSP शामिल नहीं:** प्रश्न में JSP फाइलें पूछी गई थीं, लेकिन इसे *बहुत ही सरल* रखने के लिए, हमने एक बेसिक Servlet-केवल एप्लिकेशन पर ध्यान केंद्रित किया है। JSPs को आवश्यकता के अनुसार जोड़ सकते हैं, जो अतिरिक्त फाइलें और जटिलता लाएंगे।
- **कंटेक्स्ट रूट:** कंटेक्स्ट रूट (`/myapp`) WAR फाइल नाम से आता है। `myapp.war` को बदलकर इसे बदल सकते हैं (उदाहरण के लिए, `app.war` के लिए `/app`).
- **पोर्ट नंबर:** WLP डिफॉल्ट रूप से HTTP के लिए `9080` का उपयोग करता है। अगर यह अलग है, तो `server.xml` को जांचें।
- **Java संस्करण:** WLP के साथ संगत Java संस्करण का उपयोग करें (उदाहरण के लिए, Java 8 या 11).
- **संघर्ष:** अगर यह काम नहीं करता, तो `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` में त्रुटियों को जांचें, WAR फाइल को `dropins` में सुनिश्चित करें और सर्वर चल रहा है।

---

### सारांश
इस गाइड में दिखाया गया है कि कैसे:
1. एक सरल Servlet (`HelloServlet.java`) और `web.xml` बनाएं।
2. `javac` का उपयोग करके Servlet को Maven के बिना कम्पाइल करें।
3. इसे एक WAR फाइल (`myapp.war`) में हाथ से पैकेज करें।
4. इसे WLP की `dropins` डायरेक्टरी पर डिप्लॉय करें।
5. "Hello World!" को `http://localhost:9080/myapp/hello` पर पहुंचें।

यह एक सरल, न्यूनतम Servlet एप्लिकेशन प्रदान करता है जो WebSphere Liberty Profile पर चल रहा है बिना बिल्ड टूल जैसे Maven के।