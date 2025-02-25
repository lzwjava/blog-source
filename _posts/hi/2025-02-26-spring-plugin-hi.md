---
audio: false
lang: hi
layout: post
title: Spring Boot Maven Plugin का अनुवाद
translated: true
---

`spring-boot-maven-plugin` को एक Maven आधारित Spring Boot प्रोजेक्ट में उपयोग करने के लिए, नीचे दिए गए चरणों का पालन करें ताकि प्लगइन को कॉन्फ़िगर और उपयोग करें। नीचे एक विस्तृत गाइड है:

---

### **1. अपने प्रोजेक्ट को एक Spring Boot प्रोजेक्ट बनाएं**
`spring-boot-maven-plugin` का उपयोग करने से पहले, अपने प्रोजेक्ट को एक Spring Boot प्रोजेक्ट के रूप में सेट अप किया गया है, यह आम तौर पर शामिल होता है:

- **`spring-boot-starter-parent` से विस्तार (सिफारिश की जाती है)**:
  - अपने `pom.xml` में, `spring-boot-starter-parent` को पेरेंट के रूप में सेट करें ताकि Spring Boot dependencies और प्लगइन संस्करणों को प्रबंधित किया जा सके।
  - उदाहरण:
    ```xml
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.5.4</version> <!-- अपने Spring Boot संस्करण के साथ बदलें -->
        <relativePath/> <!-- रिपोजिटरी से पेरेंट खोजें -->
    </parent>
    ```

- **अल्टर्नेटिव, `spring-boot-dependencies` BOM (Bill of Materials) का उपयोग करें**:
  - अगर आप `spring-boot-starter-parent` का उपयोग नहीं कर सकते, तो `dependencyManagement` सेक्शन में `spring-boot-dependencies` BOM को इम्पोर्ट करें।
  - उदाहरण:
    ```xml
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.5.4</version> <!-- अपने Spring Boot संस्करण के साथ बदलें -->
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    ```

`spring-boot-starter-parent` का उपयोग करने की सिफारिश की जाती है, क्योंकि यह प्लगइन संस्करणों को स्वचालित रूप से प्रबंधित करता है।

---

### **2. `spring-boot-maven-plugin` को अपने `pom.xml` में जोड़ें**
प्लगइन का उपयोग करने के लिए, आपको इसे `pom.xml` के `<build><plugins>` सेक्शन में घोषित करना होगा।

- **अगर `spring-boot-starter-parent` का उपयोग किया जा रहा है**:
  - संस्करण को स्पष्ट करने के बिना प्लगइन को जोड़ें, क्योंकि इसे पेरेंट द्वारा प्रबंधित किया जाता है।
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

- **अगर `spring-boot-starter-parent` का उपयोग नहीं किया जा रहा है**:
  - संस्करण को स्पष्ट रूप से निर्दिष्ट करें, जो उपयोग में लाया जा रहा है Spring Boot संस्करण के साथ मिलता है।
  - उदाहरण:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.5.4</version> <!-- अपने Spring Boot संस्करण के साथ बदलें -->
            </plugin>
        </plugins>
    </build>
    ```

---

### **3. प्लगइन लक्ष्यों का उपयोग करें**
`spring-boot-maven-plugin` कई लक्ष्यों को प्रदान करता है ताकि आप अपने Spring Boot एप्लिकेशन को बनाएं, चलाएं और प्रबंधित करें। नीचे सबसे आम तौर पर उपयोग किए जाने वाले लक्ष्यों हैं:

- **`spring-boot:run`**
  - एक एम्बेडेड वेब सर्वर (जैसे टोमकैट) का उपयोग करके, Maven से Spring Boot एप्लिकेशन को सीधे चलाएं।
  - विकास और परीक्षण के लिए उपयोगी है।
  - कमांड:
    ```
    mvn spring-boot:run
    ```

- **`spring-boot:repackage`**
  - `mvn package` द्वारा बनाए गए JAR या WAR फ़ाइल को एक "fat JAR" या WAR में पुनः पैकेज करें जो सभी dependencies को शामिल करता है।
  - अगर प्लगइन कॉन्फ़िगर किया गया है, तो इस लक्ष्य को `package` चरण के दौरान स्वचालित रूप से कार्यान्वित किया जाता है।
  - कमांड:
    ```
    mvn package
    ```
  - चलाने के बाद, आप एप्लिकेशन को इस तरह से शुरू कर सकते हैं:
    ```
    java -jar target/myapp.jar
    ```

- **`spring-boot:start` और `spring-boot:stop`**
  - इन्टिग्रेशन टेस्ट के दौरान `pre-integration-test` और `post-integration-test` चरणों के दौरान एप्लिकेशन को शुरू और रोकने के लिए उपयोग किया जाता है।
  - उदाहरण:
    ```
    mvn spring-boot:start
    mvn spring-boot:stop
    ```

- **`spring-boot:build-info`**
  - एक `build-info.properties` फ़ाइल बनाएं जिसमें बिल्ड जानकारी (जैसे बिल्ड समय, संस्करण) शामिल है।
  - इस जानकारी को Spring Boot के `BuildProperties` बीन या `@Value` एनोटेशन का उपयोग करके अपने एप्लिकेशन में एक्सेस किया जा सकता है।
  - कमांड:
    ```
    mvn spring-boot:build-info
    ```

---

### **4. प्लगइन कॉन्फ़िगरेशन को कस्टमाइज़ करें (वैकल्पिक)**
आप `pom.xml` में कॉन्फ़िगरेशन विकल्पों को जोड़कर `spring-boot-maven-plugin` के व्यवहार को कस्टमाइज़ कर सकते हैं। नीचे कुछ आम कस्टमाइज़ेशन हैं:

- **मुख्य क्लास को स्पष्ट करें**:
  - अगर प्लगइन मुख्य क्लास को स्वचालित रूप से पता नहीं लगा सकता, तो इसे मैन्युअल रूप से स्पष्ट करें।
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

- **Fat JAR से dependencies को बाहर निकालें**:
  - रनटाइम पर्यावरण द्वारा प्रदान की गई dependencies (जैसे एक बाहरी सर्वलेट कंटेनर) को बाहर निकालें।
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

- **एप्लिकेशन तर्कों को सेट करें**:
  - `spring-boot:run` के साथ एप्लिकेशन को चलाने के लिए तर्कों को कॉन्फ़िगर करें।
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
  - या कमांड लाइन से तर्कों को पास करें:
    ```
    mvn spring-boot:run -Dspring-boot.run.arguments=--server.port=8081
    ```

- **WAR फ़ाइलें बनाएं**:
  - एक बाहरी सर्वलेट कंटेनर में डिप्लॉय करने के लिए WAR फ़ाइल बनाएं, तो अपने प्रोजेक्ट पैकेजिंग को `pom.xml` में `war` के रूप में सेट करें:
    ```xml
    <packaging>war</packaging>
    ```
  - आपको संभवतः एम्बेडेड सर्वलेट कंटेनरों (जैसे टोमकैट) को बाहर निकालने की आवश्यकता होगी अगर वे पर्यावरण द्वारा प्रदान किए गए हैं। नीचे दिए गए dependency को `provided` के रूप में जोड़ें:
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
  - जब आप `mvn package` चलाते हैं, तो प्लगइन स्वचालित रूप से `package` चरण के दौरान JAR/WAR को पुनः पैकेज करता है ताकि इसे एक्सिक्यूटेबल बनाया जा सके।
  - पुनः पैकेज किया गया आर्टिफैक्ट मुख्य आर्टिफैक्ट है, और मूल JAR/WAR एक क्लासिफायर के साथ जोड़ा जाता है (जैसे `original`).

- **विकास कार्यप्रणाली**:
  - विकास और परीक्षण के लिए `mvn spring-boot:run` का उपयोग करें।
  - एक एक्सिक्यूटेबल JAR या WAR बनाने के लिए `mvn package` का उपयोग करें।

- **इंटिग्रेशन टेस्ट**:
  - `spring-boot:start` और `spring-boot:stop` का उपयोग इंटिग्रेशन टेस्ट के दौरान एप्लिकेशन लाइफसाइकल को प्रबंधित करने के लिए करें।

---

### **सारांश**
`spring-boot-maven-plugin` का उपयोग करने के लिए:
1. अपने प्रोजेक्ट को एक Spring Boot प्रोजेक्ट बनाएं, आम तौर पर `spring-boot-starter-parent` से विस्तार करके या `spring-boot-dependencies` BOM का उपयोग करके।
2. प्लगइन को `pom.xml` के `<build><plugins>` सेक्शन में जोड़ें।
3. Maven कमांडों का उपयोग करें जैसे:
   - `mvn spring-boot:run` एप्लिकेशन को चलाने के लिए।
   - `mvn package` एक एक्सिक्यूटेबल JAR/WAR बनाने के लिए।
   - अन्य लक्ष्यों जैसे `spring-boot:start`, `spring-boot:stop`, और `spring-boot:build-info` जैसे आवश्यकता के अनुसार।
4. वैकल्पिक रूप से, `pom.xml` में प्लगइन कॉन्फ़िगरेशन को कस्टमाइज़ करें उन्नत उपयोग के लिए।

इस सेटअप के साथ, आप Maven का उपयोग करके Spring Boot एप्लिकेशन को बनाना, चलाना और प्रबंधित करना आसान हो जाएगा।