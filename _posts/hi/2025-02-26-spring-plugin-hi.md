---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग बूट मेवेन प्लगइन
translated: true
type: note
---

`spring-boot-maven-plugin` का उपयोग Maven-आधारित Spring Boot प्रोजेक्ट में करने के लिए, अपने एप्लिकेशन को बनाने, चलाने और प्रबंधित करने के लिए प्लगइन को कॉन्फ़िगर और उपयोग करने के लिए इन चरणों का पालन करें। नीचे एक व्यापक गाइड दी गई है:

---

### **1. सुनिश्चित करें कि आपका प्रोजेक्ट एक Spring Boot प्रोजेक्ट है**
`spring-boot-maven-plugin` का उपयोग करने से पहले, पुष्टि करें कि आपका प्रोजेक्ट एक Spring Boot प्रोजेक्ट के रूप में सेट अप है। इसमें आमतौर पर शामिल होता है:

- **`spring-boot-starter-parent` से विस्तार करना (अनुशंसित)**:
  - अपने `pom.xml` में, Spring Boot dependencies और प्लगइन संस्करणों को प्रबंधित करने के लिए `spring-boot-starter-parent` को पैरेंट के रूप में सेट करें।
  - उदाहरण:
    ```xml
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.5.4</version> <!-- अपने Spring Boot संस्करण से बदलें -->
        <relativePath/> <!-- रिपॉजिटरी से पैरेंट देखें -->
    </parent>
    ```

- **वैकल्पिक रूप से, `spring-boot-dependencies` BOM (बिल ऑफ मैटेरियल्स) का उपयोग करना**:
  - यदि आप `spring-boot-starter-parent` का उपयोग नहीं कर सकते हैं, तो `dependencyManagement` सेक्शन में `spring-boot-dependencies` BOM को इम्पोर्ट करें।
  - उदाहरण:
    ```xml
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.5.4</version> <!-- अपने Spring Boot संस्करण से बदलें -->
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    ```

सरलता के लिए `spring-boot-starter-parent` का उपयोग करने की अनुशंसा की जाती है, क्योंकि यह स्वचालित रूप से प्लगइन संस्करणों को प्रबंधित करता है।

---

### **2. अपने `pom.xml` में `spring-boot-maven-plugin` जोड़ें**
प्लगइन का उपयोग करने के लिए, आपको इसे अपने `pom.xml` के `<build><plugins>` सेक्शन में डिक्लेयर करना होगा।

- **यदि `spring-boot-starter-parent` का उपयोग कर रहे हैं**:
  - प्लगइन को बिना संस्करण निर्दिष्ट किए जोड़ें, क्योंकि यह पैरेंट द्वारा प्रबंधित होता है।
  - उदाहरण:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
    ```

- **यदि `spring-boot-starter-parent` का उपयोग नहीं कर रहे हैं**:
  - संस्करण को स्पष्ट रूप से निर्दिष्ट करें, जो उपयोग में आने वाले Spring Boot संस्करण से मेल खाता हो।
  - उदाहरण:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.5.4</version> <!-- अपने Spring Boot संस्करण से बदलें -->
            </plugin>
        </plugins>
    </build>
    ```

---

### **3. प्लगइन गोल्स का उपयोग करें**
`spring-boot-maven-plugin` आपके Spring Boot एप्लिकेशन को बनाने, चलाने और प्रबंधित करने में मदद के लिए कई गोल्स प्रदान करता है। नीचे सबसे अधिक उपयोग किए जाने वाले गोल्स दिए गए हैं:

- **`spring-boot:run`**
  - एक एम्बेडेड वेब सर्वर (जैसे, Tomcat) का उपयोग करके Maven से सीधे आपके Spring Boot एप्लिकेशन को चलाता है।
  - डेवलपमेंट और टेस्टिंग के लिए उपयोगी।
  - कमांड:
    ```
    mvn spring-boot:run
    ```

- **`spring-boot:repackage`**
  - `mvn package` द्वारा जेनरेट किए गए JAR या WAR फ़ाइल को एक एक्ज़िक्यूटेबल "फैट JAR" या WAR में रिपैकेज करता है जिसमें सभी dependencies शामिल होती हैं।
  - यह गोल स्वचालित रूप से `package` फेज के दौरान एक्ज़िक्यूट होता है यदि प्लगइन कॉन्फ़िगर किया गया है।
  - कमांड:
    ```
    mvn package
    ```
  - चलाने के बाद, आप एप्लिकेशन को इसके साथ शुरू कर सकते हैं:
    ```
    java -jar target/myapp.jar
    ```

- **`spring-boot:start` और `spring-boot:stop`**
  - इंटीग्रेशन टेस्ट के लिए उपयोग किया जाता है ताकि `pre-integration-test` और `post-integration-test` फेज के दौरान एप्लिकेशन को क्रमशः शुरू और बंद किया जा सके।
  - उदाहरण:
    ```
    mvn spring-boot:start
    mvn spring-boot:stop
    ```

- **`spring-boot:build-info`**
  - एक `build-info.properties` फ़ाइल जेनरेट करता है जिसमें बिल्ड जानकारी (जैसे, बिल्ड समय, संस्करण) शामिल होती है।
  - इस जानकारी को Spring Boot के `BuildProperties` बीन या `@Value` एनोटेशन का उपयोग करके आपके एप्लिकेशन में एक्सेस किया जा सकता है।
  - कमांड:
    ```
    mvn spring-boot:build-info
    ```

---

### **4. प्लगइन कॉन्फ़िगरेशन को कस्टमाइज़ करें (वैकल्पिक)**
आप `pom.xml` में कॉन्फ़िगरेशन विकल्प जोड़कर `spring-boot-maven-plugin` के व्यवहार को कस्टमाइज़ कर सकते हैं। नीचे कुछ सामान्य कस्टमाइज़ेशन दिए गए हैं:

- **मुख्य क्लास निर्दिष्ट करें**:
  - यदि प्लगइन मुख्य क्लास को स्वचालित रूप से डिटेक्ट नहीं कर सकता है, तो इसे मैन्युअल रूप से निर्दिष्ट करें।
  - उदाहरण:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <mainClass>com.example.MyApplication</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```

- **फैट JAR से Dependencies को बाहर करें**:
  - रनटाइम एनवायरनमेंट (जैसे, एक एक्सटर्नल सर्वलेट कंटेनर) द्वारा प्रदान की गई dependencies को बाहर करें।
  - उदाहरण:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>com.example</groupId>
                            <artifactId>some-dependency</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```

- **एप्लिकेशन आर्ग्युमेंट्स सेट करें**:
  - `spring-boot:run` के साथ चलाते समय एप्लिकेशन को पास करने के लिए आर्ग्युमेंट्स को कॉन्फ़िगर करें।
  - `pom.xml` में उदाहरण:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <arguments>
                        <argument>--server.port=8081</argument>
                    </arguments>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```
  - वैकल्पिक रूप से, कमांड लाइन के माध्यम से आर्ग्युमेंट्स पास करें:
    ```
    mvn spring-boot:run -Dspring-boot.run.arguments=--server.port=8081
    ```

- **WAR फ़ाइलें बनाना**:
  - यदि किसी एक्सटर्नल सर्वलेट कंटेनर पर डिप्लॉयमेंट के लिए WAR फ़ाइल बना रहे हैं, तो सुनिश्चित करें कि आपके प्रोजेक्ट पैकेजिंग को `pom.xml` में `war` पर सेट किया गया है:
    ```xml
    <packaging>war</packaging>
    ```
  - आपको एम्बेडेड सर्वलेट कंटेनर (जैसे, Tomcat) को बाहर करने की आवश्यकता हो सकती है यदि वे एनवायरनमेंट द्वारा प्रदान किए जाते हैं। निम्नलिखित dependency को `provided` के रूप में जोड़ें:
    ```xml
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-tomcat</artifactId>
            <scope>provided</scope>
        </dependency>
    </dependencies>
    ```

---

### **5. मुख्य नोट्स**
- **डिफ़ॉल्ट व्यवहार**:
  - जब आप `mvn package` चलाते हैं, तो प्लगइन स्वचालित रूप से `package` फेज के दौरान JAR/WAR को रिपैकेज करता है ताकि इसे एक्ज़िक्यूटेबल बनाया जा सके।
  - रिपैकेज्ड आर्टिफैक्ट मुख्य आर्टिफैक्ट होता है, और ओरिजिनल JAR/WAR एक क्लासिफायर (जैसे, `original`) के साथ अटैच होता है।

- **डेवलपमेंट वर्कफ़्लो**:
  - त्वरित डेवलपमेंट और टेस्टिंग के लिए `mvn spring-boot:run` का उपयोग करें।
  - एक डिप्लॉयेबल एक्ज़िक्यूटेबल JAR या WAR बनाने के लिए `mvn package` का उपयोग करें।

- **इंटीग्रेशन टेस्ट्स**:
  - इंटीग्रेशन टेस्टिंग के दौरान एप्लिकेशन लाइफसाइकल को प्रबंधित करने के लिए `spring-boot:start` और `spring-boot:stop` का उपयोग करें।

---

### **सारांश**
`spring-boot-maven-plugin` का उपयोग करने के लिए:
1. सुनिश्चित करें कि आपका प्रोजेक्ट एक Spring Boot प्रोजेक्ट है, आमतौर पर `spring-boot-starter-parent` से एक्सटेंड करके या `spring-boot-dependencies` BOM का उपयोग करके।
2. प्लगइन को अपने `pom.xml` के `<build><plugins>` सेक्शन में जोड़ें।
3. Maven कमांड्स का उपयोग करें जैसे:
   - एप्लिकेशन चलाने के लिए `mvn spring-boot:run`।
   - एक्ज़िक्यूटेबल JAR/WAR बनाने के लिए `mvn package`।
   - अन्य गोल्स जैसे `spring-boot:start`, `spring-boot:stop`, और `spring-boot:build-info` की आवश्यकतानुसार।
4. वैकल्पिक रूप से, उन्नत उपयोग के मामलों के लिए `pom.xml` में प्लगइन के कॉन्फ़िगरेशन को कस्टमाइज़ करें।

यह सेटअप आपको Maven का उपयोग करके Spring Boot एप्लिकेशन को कुशलतापूर्वक बनाने, चलाने और प्रबंधित करने में सक्षम बनाता है।