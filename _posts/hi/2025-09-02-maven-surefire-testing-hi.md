---
audio: false
generated: true
image: false
lang: hi
layout: post
title: मेवेन सुरफायर प्लगइन इकाई परीक्षण गाइड
translated: true
type: note
---

**Maven Surefire Plugin** वह प्लगइन है जो Maven बिल्ड लाइफसाइकल के **test** चरण के दौरान आपके यूनिट टेस्ट चलाता है। यह सबसे अधिक इस्तेमाल किए जाने वाले Maven प्लगइन्स में से एक है क्योंकि लगभग हर प्रोजेक्ट को अपनी बिल्ड प्रक्रिया में ऑटोमेटेड टेस्टिंग को एकीकृत करने की आवश्यकता होती है।

---

## यह क्या है

* **नाम**: `maven-surefire-plugin`
* **उद्देश्य**: JUnit (3, 4, 5), TestNG, आदि जैसे फ्रेमवर्क्स में लिखे गए टेस्ट को एक्जीक्यूट करना।
* **चरण**: Maven की डिफॉल्ट लाइफसाइकल के `test` चरण से बंधा हुआ।
* **आउटपुट**: टेस्ट रिपोर्ट्स जनरेट करता है (डिफॉल्ट रूप से `target/surefire-reports` में)।

---

## यह कैसे काम करता है

1. जब आप `mvn test` या `mvn package` चलाते हैं, तो Maven Surefire प्लगइन को इनवोक करता है।
2. यह आपके `src/test/java` डायरेक्टरी को टेस्ट क्लासेस के लिए स्कैन करता है।
3. डिफॉल्ट रूप से, यह नामकरण कन्वेंशन से मेल खाने वाली फाइलों को ढूंढता है, जैसे:

   * `*Test.java`
   * `Test*.java`
   * `*Tests.java`
   * `*TestCase.java`
4. उन्हें एक आइसोलेटेड क्लासलोडर में एक्जीक्यूट करता है।
5. परिणामों को `target/surefire-reports` में लिखता है (प्लेन टेक्स्ट, XML, और कभी-कभी रिपोर्टिंग प्लगइन्स के माध्यम से HTML)।

---

## बेसिक यूसेज

आप इसे अपने `pom.xml` में कॉन्फ़िगर कर सकते हैं:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-surefire-plugin</artifactId>
      <version>3.2.5</version> <!-- use latest stable -->
    </plugin>
  </plugins>
</build>
```

इसके बाद, बस चलाएं:

```bash
mvn test
```

---

## कॉमन कॉन्फ़िगरेशन

* **इनक्लूड/एक्सक्लूड पैटर्न**:

```xml
<configuration>
  <includes>
    <include>**/*MyTest.java</include>
  </includes>
  <excludes>
    <exclude>**/IntegrationTest.java</exclude>
  </excludes>
</configuration>
```

* **सिस्टम प्रॉपर्टीज़**:

```xml
<configuration>
  <systemPropertyVariables>
    <env>dev</env>
  </systemPropertyVariables>
</configuration>
```

* **पैरेलल टेस्ट एक्जीक्यूशन**:

```xml
<configuration>
  <forkCount>2</forkCount>
  <reuseForks>true</reuseForks>
  <parallel>classes</parallel>
</configuration>
```

यह टेस्ट्स को मल्टीपल JVM फोर्क्स या थ्रेड्स में चलाता है।

---

## इसका उपयोग कब करें

* कभी भी जब आप **यूनिट टेस्टिंग** को अपने Maven लाइफसाइकल में एकीकृत करना चाहते हैं।
* **यूनिट टेस्ट्स (Surefire)** को **इंटीग्रेशन टेस्ट्स (Failsafe plugin)** से अलग करने के लिए:

  * Surefire → यूनिट टेस्ट (`mvn test`)
  * Failsafe → इंटीग्रेशन टेस्ट (`mvn verify`)

---

✅ **संक्षेप में**: `maven-surefire-plugin` Maven प्रोजेक्ट्स में यूनिट टेस्ट एक्जीक्यूशन के लिए आपकी मुख्य प्लगइन है। आप इसे `pom.xml` में कॉन्फ़िगर करते हैं, `mvn test` के साथ चलाते हैं, और रिपोर्ट्स को `target/surefire-reports` में रिव्यू करते हैं।

---

क्या आप चाहते हैं कि मैं **Surefire और Failsafe के बीच का अंतर** भी समझाऊं (चूंकि इन्हें अक्सर कन्फ्यूज किया जाता है)?