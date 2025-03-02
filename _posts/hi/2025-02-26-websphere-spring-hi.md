---
audio: true
generated: true
lang: hi
layout: post
title: Spring Boot को WebSphere Liberty Profile पर Deploy करना
translated: true
---

यह एक पूर्ण मार्गदर्शिका है कि WebSphere Liberty Profile (WLP) पर एक सरल Spring Boot अनुप्रयोग चलाने के लिए। इस उदाहरण में, एक Spring Boot अनुप्रयोग बनाया जाता है जिसमें एक बुनियादी REST एंडपॉइंट है जो "Hello World!" लौटाता है और इसे `dropins` डायरेक्टरी का उपयोग करके WLP पर डिप्लॉय किया जाता है। हम मानते हैं कि आपने पहले से ही WLP को `javaee-8.0` फीचर के साथ सेट अप कर लिया है, क्योंकि यह आवश्यक Servlet समर्थन प्रदान करता है।

---

### चरण-दर-चरण मार्गदर्शिका

#### 1. एक Spring Boot अनुप्रयोग बनाएं
एक नया Spring Boot प्रोजेक्ट Spring Initializr (या आपका पसंदीदा तरीका) का उपयोग करके शुरू करें। हम Maven, Java, और Spring Web निर्भरता का उपयोग करके एक सरल वेब अनुप्रयोग बनाएंगे।

- **प्रोजेक्ट बनाएं:**
  - [Spring Initializr](https://start.spring.io/) पर जाएं।
  - निम्नलिखित को कॉन्फ़िगर करें:
    - **प्रोजेक्ट:** Maven
    - **भाषा:** Java
    - **Spring Boot संस्करण:** 2.7.x (या सबसे नया स्थिर संस्करण)
    - **समूह:** `com.example`
    - **आर्टिफैक्ट:** `demo`
    - **निर्भरताएं:** Spring Web
  - "Generate" पर क्लिक करें ताकि प्रोजेक्ट ZIP डाउनलोड करें, फिर इसे अनज़िप करें और इसे अपने IDE में खोलें।

- **एक सरल REST कंट्रोलर जोड़ें:**
  `src/main/java/com/example/demo` के अंदर, `HelloController.java` नामक एक फाइल बनाएं जिसमें यह सामग्री होगी:
  ```java
  package com.example.demo;

  import org.springframework.web.bind.annotation.GetMapping;
  import org.springframework.web.bind.annotation.RestController;

  @RestController
  public class HelloController {
      @GetMapping("/")
      public String hello() {
          return "Hello World!";
      }
  }
  ```
  यह एक REST एंडपॉइंट बनाता है जो मूल पथ (`/`) पर "Hello World!" को सरल पाठ के रूप में लौटाता है।

#### 2. अनुप्रयोग को WAR डिप्लॉयमेंट के लिए कॉन्फ़िगर करें
डिफ़ॉल्ट रूप से, Spring Boot अनुप्रयोगों को एक एम्बेडेड सर्वर (जैसे टोमकैट) के साथ JAR फाइलों के रूप में पैकेज करता है। WLP पर डिप्लॉय करने के लिए, हमें इसे एक WAR फाइल के रूप में पैकेज करना होगा और इसे WLP के Servlet कंटेनर के साथ काम करने के लिए कॉन्फ़िगर करना होगा।

- **मुख्य अनुप्रयोग क्लास को संशोधित करें:**
  `src/main/java/com/example/demo/DemoApplication.java` को संपादित करें ताकि यह `SpringBootServletInitializer` को विस्तारित करे, जो अनुप्रयोग को एक बाहरी Servlet कंटेनर जैसे WLP में चलने की अनुमति देता है:
  ```java
  package com.example.demo;

  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;
  import org.springframework.boot.builder.SpringApplicationBuilder;
  import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;

  @SpringBootApplication
  public class DemoApplication extends SpringBootServletInitializer {

      @Override
      protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
          return application.sources(DemoApplication.class);
      }

      public static void main(String[] args) {
          SpringApplication.run(DemoApplication.class, args);
      }
  }
  ```

- **`pom.xml` को WAR पैकेजिंग के लिए अपडेट करें:**
  `pom.xml` खोलें और इन परिवर्तनों को करें:
  - WAR पैकेजिंग को सेट करने के लिए इस लाइन को टॉप पर (`<modelVersion>` के नीचे) जोड़ें:
    ```xml
    <packaging>war</packaging>
    ```
  - एम्बेडेड टोमकैट निर्भरता को `provided` के रूप में चिह्नित करें ताकि यह WAR में शामिल न हो (WLP अपना स्वयं का Servlet कंटेनर प्रदान करता है)। `spring-boot-starter-web` निर्भरता (जिसमें टोमकैट शामिल है) को इस प्रकार संशोधित करें:
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    ```
    इसके नीचे यह जोड़ें:
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-tomcat</artifactId>
        <scope>provided</scope>
    </dependency>
    ```
  अब आपका `pom.xml` निर्भरताओं का खंड कुछ इस तरह दिखना चाहिए:
  ```xml
  <dependencies>
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-web</artifactId>
      </dependency>
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-tomcat</artifactId>
          <scope>provided</scope>
      </dependency>
      <!-- अन्य निर्भरताएं जैसे spring-boot-starter-test बने रह सकती हैं -->
  </dependencies>
  ```

#### 3. WAR फाइल बनाएं
Maven का उपयोग करके अनुप्रयोग को एक WAR फाइल में पैकेज करें।

- **बिल्ड कमांड चलाएं:**
  प्रोजेक्ट रूट डायरेक्टरी (जहां `pom.xml` है) से, यह चलाएं:
  ```bash
  mvn clean package
  ```
  यह `target` डायरेक्टरी में WAR फाइल पैदा करता है, उदाहरण के लिए, `target/demo-0.0.1-SNAPSHOT.war`.

- **WAR फाइल का नाम बदलें (वैकल्पिक):**
  एक साफ़ URL के लिए, WAR फाइल का नाम `myapp.war` में बदलें:
  ```bash
  mv target/demo-0.0.1-SNAPSHOT.war target/myapp.war
  ```
  यह कंटेक्स्ट रूट को `/myapp` में बदल देता है, `/demo-0.0.1-SNAPSHOT` के बजाय।

#### 4. WAR फाइल को WLP पर डिप्लॉय करें
`dropins` डायरेक्टरी का उपयोग करके WAR फाइल को WLP पर डिप्लॉय करें, जो स्वचालित डिप्लॉयमेंट को सक्षम करता है।

- **`dropins` डायरेक्टरी को खोजें:**
  WLP सर्वर की `dropins` डायरेक्टरी को खोजें। अगर WLP `/opt/ibm/wlp` पर इंस्टॉल है और आपका सर्वर `myServer` नाम है, तो पथ है:
  ```
  /opt/ibm/wlp/usr/servers/myServer/dropins
  ```

- **WAR फाइल को कॉपी करें:**
  WAR फाइल को `dropins` डायरेक्टरी में ले जाएं:
  ```bash
  cp target/myapp.war /opt/ibm/wlp/usr/servers/myServer/dropins/
  ```

- **सर्वर को शुरू करें (अगर चल रहा नहीं है):**
  अगर WLP चल नहीं रहा है, तो इसे शुरू करें:
  ```bash
  /opt/ibm/wlp/bin/server start myServer
  ```
  अगर यह पहले से चल रहा है, तो यह WAR फाइल को स्वचालित रूप से डिटेक्ट और डिप्लॉय करेगा।

- **डिप्लॉयमेंट की पुष्टि करें:**
  सर्वर लॉग या कंसोल में एक संदेश जैसा देखें:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  - लॉग `/opt/ibm/wlp/usr/servers/myServer/logs/console.log` में हैं (बैकग्राउंड मोड) या टर्मिनल में प्रदर्शित होते हैं (फॉरग्राउंड मोड के साथ `./server run myServer`).

#### 5. अनुप्रयोग तक पहुंचें
एक ब्राउज़र में डिप्लॉय किया गया Spring Boot अनुप्रयोग को टेस्ट करें।

- **अपना ब्राउज़र खोलें:**
  इस पर जाएं:
  ```
  http://localhost:9080/myapp/
  ```
  - `9080` WLP का डिफ़ॉल्ट HTTP पोर्ट है।
  - `/myapp` WAR फाइल नाम से कंटेक्स्ट रूट है।
  - `/` कंट्रोलर में `@GetMapping("/")` के साथ मिलता है।

- **अपेक्षित परिणाम:**
  आप यह देखेंगे:
  ```
  Hello World!
  ```
  सरल पाठ के रूप में प्रदर्शित।

---

### टिप्पणियाँ
- **कंटेक्स्ट रूट:** कंटेक्स्ट रूट (`/myapp`) WAR फाइल नाम से प्राप्त होता है। इसे आवश्यकता के अनुसार WAR फाइल का नाम बदलकर संशोधित करें।
- **पोर्ट संख्या:** WLP डिफ़ॉल्ट रूप से HTTP के लिए `9080` का उपयोग करता है। अगर आपका सर्वर एक अलग पोर्ट का उपयोग करता है, तो URL को अनुकूलित करें।
- **Java संस्करण:** सुनिश्चित करें कि WLP और आपका बिल्ड पर्यावरण एक संगत Java संस्करण का उपयोग करते हैं (जैसे Java 8 या 11 के लिए Spring Boot 2.7.x).
- **WLP फीचर्स:** `javaee-8.0` फीचर Servlet 4.0 समर्थन शामिल करता है, जो Spring Boot 2.7.x की आवश्यकताओं (Servlet 3.1+) के साथ संगत है।
- **संघर्ष करने के लिए:**
  - अगर पृष्ठ लोड नहीं होता है, तो `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` में त्रुटियों की जांच करें।
  - WAR फाइल `dropins` में है और सर्वर चल रहा है, यह सुनिश्चित करें।

---

### सारांश
इस मार्गदर्शिका में दिखाया गया है कि कैसे:
1. एक REST एंडपॉइंट के साथ एक Spring Boot अनुप्रयोग बनाएं।
2. इसे WAR डिप्लॉयमेंट के लिए कॉन्फ़िगर करें `SpringBootServletInitializer` को विस्तारित करके और टोमकैट को `provided` सेट करके।
3. WAR फाइल को WLP के `dropins` डायरेक्टरी में बनाएं और डिप्लॉय करें।
4. `http://localhost:9080/myapp/` पर "Hello World!" आउटपुट तक पहुंचें।

यह दृष्टिकोण WLP के स्वचालित डिप्लॉयमेंट क्षमताओं और Spring Boot की लचीलापन का लाभ उठाता है, WebSphere Liberty Profile पर एक सरल परन्तु कार्यात्मक वेब अनुप्रयोग प्रदान करता है।