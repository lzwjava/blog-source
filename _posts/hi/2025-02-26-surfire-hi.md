---
audio: false
generated: true
lang: hi
layout: post
title: मेवेन स्योरफायर प्लगइन
translated: true
type: note
---

नीचे **Maven Surefire Plugin** की व्याख्या दी गई है, जो Maven-आधारित प्रोजेक्ट्स में बिल्ड प्रक्रिया के दौरान यूनिट टेस्ट चलाने के लिए एक महत्वपूर्ण घटक है। यह व्याख्या इसके उद्देश्य, कॉन्फ़िगरेशन, उपयोग और अनुकूलन विकल्पों को कवर करती है।

---

## Maven Surefire Plugin क्या है?

**Maven Surefire Plugin** Apache Maven में एक प्लगइन है जो बिल्ड लाइफसाइकल के दौरान यूनिट टेस्ट को execute करने के लिए डिज़ाइन किया गया है। यह Maven के `test` चरण के साथ seamlessly integrate होता है और स्वचालित रूप से तब ट्रिगर होता है जब आप `mvn test`, `mvn package`, या `mvn install` जैसे कमांड चलाते हैं। यह प्लगइन JUnit (वर्जन 3, 4, और 5) और TestNG जैसे लोकप्रिय टेस्ट फ्रेमवर्क को सपोर्ट करता है, और यह डेवलपर्स को टेस्ट परिणामों का आकलन करने में मदद करने के लिए टेस्ट रिपोर्ट generate करता है।

### मुख्य विशेषताएं
- अलगाव के लिए एक अलग JVM प्रक्रिया में टेस्ट चलाता है।
- कई टेस्ट फ्रेमवर्क (JUnit, TestNG, आदि) को सपोर्ट करता है।
- XML और plain text जैसे फॉर्मेट में टेस्ट रिपोर्ट generate करता है।
- टेस्ट्स को स्किप करने, विशिष्ट टेस्ट चलाने, या execution को customize करने की लचीलापन प्रदान करता है।

---

## `pom.xml` में बेसिक सेटअप

Surefire Plugin डिफ़ॉल्ट रूप से Maven की बिल्ड लाइफसाइकल में शामिल होता है, इसलिए बुनियादी उपयोग के लिए आपको इसे configure करने की आवश्यकता नहीं होती है। हालाँकि, आप एक वर्जन निर्दिष्ट करने या इसके व्यवहार को customize करने के लिए इसे अपनी `pom.xml` फ़ाइल में स्पष्ट रूप से declare कर सकते हैं।

### न्यूनतम कॉन्फ़िगरेशन
यदि आप कोई कॉन्फ़िगरेशन नहीं जोड़ते हैं, तो Maven डिफ़ॉल्ट सेटिंग्स के साथ प्लगइन का उपयोग करता है:
- टेस्ट `src/test/java` में स्थित होते हैं।
- टेस्ट फ़ाइलें नामकरण पैटर्न जैसे `**/*Test.java`, `**/Test*.java`, या `**/*Tests.java` का पालन करती हैं।

### स्पष्ट घोषणा
प्लगइन को customize करने या किसी विशिष्ट वर्जन को सुनिश्चित करने के लिए, इसे अपनी `pom.xml` के `<build><plugins>` सेक्शन में जोड़ें। यहाँ एक उदाहरण दिया गया है:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M5</version> <!-- नवीनतम वर्जन का उपयोग करें -->
        </plugin>
    </plugins>
</build>
```

---

## Surefire के साथ टेस्ट चलाना

यह प्लगइन Maven लाइफसाइकल के `test` चरण से जुड़ा हुआ है। इसे उपयोग करने का तरीका यहाँ बताया गया है:

### सभी टेस्ट चलाएं
सभी यूनिट टेस्ट execute करने के लिए, चलाएं:

```
mvn test
```

### एक बड़े बिल्ड में टेस्ट चलाएं
जब आप ऐसे कमांड चलाते हैं जिनमें `test` चरण शामिल होता है, तो टेस्ट स्वचालित रूप से execute हो जाते हैं, जैसे:

```
mvn package
mvn install
```

### टेस्ट स्किप करें
आप कमांड-लाइन फ्लैग्स का उपयोग करके टेस्ट execution को स्किप कर सकते हैं:
- **टेस्ट चलाना स्किप करें**: `-DskipTests`
  ```
  mvn package -DskipTests
  ```
- **टेस्ट कंपाइलेशन और execution स्किप करें**: `-Dmaven.test.skip=true`
  ```
  mvn package -Dmaven.test.skip=true
  ```

---

## Surefire Plugin को Customize करना

आप `pom.xml` में एक `<configuration>` सेक्शन जोड़कर प्लगइन के व्यवहार को tailor कर सकते हैं। यहाँ कुछ सामान्य अनुकूलन दिए गए हैं:

### विशिष्ट टेस्ट शामिल या बाहर करें
पैटर्न का उपयोग करके निर्दिष्ट करें कि कौन से टेस्ट चलाने हैं या स्किप करने हैं:
```xml
<configuration>
    <includes>
        <include>**/My*Test.java</include>
    </includes>
    <excludes>
        <exclude>**/SlowTest.java</exclude>
    </excludes>
</configuration>
```

### टेस्ट समानांतर में चलाएं
टेस्ट्स को concurrently चलाकर execution की गति बढ़ाएं:
```xml
<configuration>
    <parallel>methods</parallel>
    <threadCount>2</threadCount>
</configuration>
```
*नोट*: इसे enable करने से पहले सुनिश्चित करें कि आपके टेस्ट thread-safe हैं।

### सिस्टम प्रॉपर्टीज पास करें
टेस्ट JVM के लिए properties सेट करें:
```xml
<configuration>
    <systemPropertyVariables>
        <propertyName>propertyValue</propertyName>
    </systemPropertyVariables>
</configuration>
```

### रिपोर्ट Generate करें
डिफ़ॉल्ट रूप से, रिपोर्ट्स `target/surefire-reports` में सेव होती हैं। एक HTML रिपोर्ट के लिए, `maven-surefire-report-plugin` का उपयोग करें:
```xml
<reporting>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-report-plugin</artifactId>
            <version>3.0.0-M5</version>
        </plugin>
    </plugins>
</reporting>
```
HTML रिपोर्ट generate करने के लिए `mvn surefire-report:report` चलाएं।

---

## टेस्ट फेलियर को हैंडल करना

### टेस्ट फेल होने पर बिल्ड फेल करें
डिफ़ॉल्ट रूप से, एक फेल होने वाला टेस्ट बिल्ड को फेल कर देता है। फेलियर को ignore करने और जारी रखने के लिए:
```
mvn test -Dmaven.test.failure.ignore=true
```

### फेल हुए टेस्ट को दोबारा चलाएं
फेल हुए टेस्ट्स को दोबारा चलाकर flaky टेस्ट्स को हैंडल करें:
```xml
<configuration>
    <rerunFailingTestsCount>2</rerunFailingTestsCount>
</configuration>
```
यह फेल हुए टेस्ट्स को अधिकतम 2 बार दोबारा चलाएगा।

---

## टेस्ट फ्रेमवर्क के साथ Surefire का उपयोग करना

यह प्लगइन न्यूनतम सेटअप के साथ विभिन्न टेस्ट फ्रेमवर्क को सपोर्ट करता है:

### JUnit 4
किसी अतिरिक्त कॉन्फ़िगरेशन की आवश्यकता नहीं है; Surefire JUnit 4 टेस्ट्स को स्वचालित रूप से detect कर लेता है।

### JUnit 5
JUnit 5 dependency जोड़ें:
```xml
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>5.8.1</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
पूर्ण सपोर्ट के लिए Surefire वर्जन 2.22.0 या बाद का उपयोग करें।

### TestNG
TestNG dependency जोड़ें:
```xml
<dependencies>
    <dependency>
        <groupId>org.testng</groupId>
        <artifactId>testng</artifactId>
        <version>7.4.0</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
Surefire स्वचालित रूप से TestNG टेस्ट्स को चलाएगा।

---

## मुख्य नोट्स

- **टेस्ट लोकेशन**: टेस्ट `src/test/java` में होने चाहिए, resources के साथ `src/test/resources` में।
- **नामकरण परंपराएं**: डिफ़ॉल्ट पैटर्न में `**/*Test.java`, `**/Test*.java`, आदि शामिल हैं, लेकिन इन्हें customize किया जा सकता है।
- **प्लगइन वर्जन**: नवीनतम फीचर्स और फ्रेमवर्क सपोर्ट के लिए एक recent वर्जन (जैसे, 3.0.0-M5) का उपयोग करें।

---

## सारांश

**Maven Surefire Plugin** Maven प्रोजेक्ट्स में यूनिट टेस्ट चलाने के लिए आवश्यक है। इसका उपयोग करने के लिए:
1. इसके डिफ़ॉल्ट व्यवहार पर भरोसा करें या customization के लिए इसे `pom.xml` में स्पष्ट रूप से declare करें।
2. `mvn test` या `mvn package` जैसे बड़े बिल्ड्स के हिस्से के रूप में टेस्ट चलाएं।
3. इसे include/exclude पैटर्न, parallel execution, या system properties जैसे विकल्पों के साथ customize करें।
4. टेस्ट्स को स्किप करके, उन्हें ignore करके, या flaky टेस्ट्स को दोबारा चलाकर फेलियर को हैंडल करें।
5. सही dependencies जोड़कर अपने टेस्ट फ्रेमवर्क (JUnit, TestNG) के साथ compatibility सुनिश्चित करें।

यह प्लगइन आपके Maven प्रोजेक्ट्स में यूनिट टेस्टिंग को manage करने का एक robust और flexible तरीका प्रदान करता है!