---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: जावा एसएसएल टीएलएस डिबगिंग सक्षम करें
translated: true
type: note
---

### Java में SSL/TLS डिबगिंग सक्षम करना

Java में SSL/TLS-संबंधित गतिविधियों (जैसे, हैंडशेक, प्रमाणपत्र सत्यापन, कुंजी विनिमय) के लिए विस्तृत लॉगिंग सक्षम करने के लिए, आप JVM सिस्टम प्रॉपर्टी `-Djavax.net.debug` का उपयोग करते हैं। यह आपके Java एप्लिकेशन के चलने पर कंसोल (stdout/stderr) पर डिबग जानकारी आउटपुट करता है।

#### चरण-दर-चरण निर्देश

1. **डिबग स्तर चुनें**:
   - बुनियादी SSL/TLS हैंडशेक विवरण के लिए `ssl` का उपयोग करें।
   - वर्बोज़ हैंडशेक संदेशों (साइफर सूट और प्रमाणपत्रों सहित) के लिए `ssl:handshake` का उपयोग करें।
   - व्यापक डिबगिंग के लिए `all` का उपयोग करें (इसमें SSL के साथ-साथ अन्य नेटवर्क प्रोटोकॉल शामिल होते हैं—इसका उपयोग संयम से करें क्योंकि यह बहुत अधिक वर्बोज़ होता है)।
   - सामान्य सिफारिश: लक्षित SSL जानकारी के लिए `ssl:handshake:verbose,keymanager:trustmanager` से शुरुआत करें।

2. **अपना Java एप्लिकेशन चलाते समय प्रॉपर्टी सेट करें**:
   - **कमांड-लाइन एक्जिक्यूशन** (उदाहरण के लिए, `java` कमांड के माध्यम से):
     ```
     java -Djavax.net.debug=ssl:handshake -jar your-app.jar
     ```
     `your-app.jar` को अपने वास्तविक एप्लिकेशन या क्लास (उदाहरण के लिए, `com.example.Main`) से बदलें।

   - **एक IDE में (उदाहरण के लिए, IntelliJ IDEA, Eclipse)**:
     - Run/Debug Configurations पर जाएं।
     - **VM options** फ़ील्ड में `-Djavax.net.debug=ssl:handshake` जोड़ें।
     - कॉन्फ़िगरेशन को रन या डिबग करें।

   - **एक बिल्ड टूल में (उदाहरण के लिए, Maven या Gradle)**:
     - **Maven** (`pom.xml` में `<build><plugins><plugin>` के अंतर्गत surefire के लिए):
       ```xml
       <configuration>
         <argLine>-Djavax.net.debug=ssl:handshake</argLine>
       </configuration>
       ```
     - **Gradle** (`build.gradle` में):
       ```groovy
       test {
         jvmArgs '-Djavax.net.debug=ssl:handshake'
       }
       ```

3. **लॉग कैप्चर करें**:
   - आउटपुट आपके कंसोल/टर्मिनल में दिखाई देता है।
   - आसान समीक्षा के लिए इसे एक फ़ाइल में रीडायरेक्ट करें:
     ```
     java -Djavax.net.debug=ssl:handshake -jar your-app.jar > ssl-debug.log 2>&1
     ```
   - `***` से शुरू होने वाली लाइनों (जैसे, हैंडशेक शुरू होने के लिए `*** ClientHello`) या `javax.net.ssl` उपसर्गों की तलाश करें।

4. **इसे अक्षम करें**:
   - जब काम पूरा हो जाए, तो बस `-D` फ्लैग को हटा दें—यह डिफ़ॉल्ट रूप से सेट नहीं होता है ताकि परफॉर्मेंस ओवरहेड से बचा जा सके।

#### आउटपुट स्निपेट का उदाहरण
जब सक्षम होता है, तो आप कुछ इस तरह देखेंगे:
```
*** ServerHello, TLSv1.2
RandomCookie:  GMT: 1731000000 bytes = { ... }
Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
Compression Method: 0
***
```

#### सुझाव
- यह Java 8+ (11, 17, 21 सहित) के लिए काम करता है। नए वर्जन में, आप प्रोटोकॉल-विशिष्ट लॉग के लिए `-Djdk.tls.client.protocols=TLSv1.2,TLSv1.3` भी सक्षम कर सकते हैं।
- उच्च वर्बोसिटी आपके ऐप को धीमा कर सकती है और लॉग को फ्लड कर सकती है—इसे एक डेव वातावरण में टेस्ट करें।
- यदि Spring Boot जैसे फ्रेमवर्क का उपयोग कर रहे हैं, तो इसे `application.properties` में जोड़ें: `debug=true` (सामान्य के लिए) या कमांड-लाइन आर्ग्स के माध्यम से।

अधिक जानकारी के लिए, आधिकारिक Oracle डॉक्स देखें: [Java Secure Socket Extension (JSSE) Reference Guide](https://docs.oracle.com/en/java/javase/17/docs/specs/security/standard-names.html#jsse-cipher-suite-names).