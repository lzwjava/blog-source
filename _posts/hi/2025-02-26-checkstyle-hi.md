---
audio: false
generated: true
lang: hi
layout: post
title: मेवेन चेकस्टाइल प्लगइन
translated: true
type: note
---

## Maven Checkstyle Plugin क्या है?

**Maven Checkstyle Plugin** एक ऐसा टूल है जो Checkstyle—एक स्टैटिक कोड एनालिसिस टूल—को आपकी Maven बिल्ड प्रक्रिया में इंटीग्रेट करता है। Checkstyle आपके Java कोड की जाँच पूर्वनिर्धारित नियमों के सेट के खिलाफ करता है, जैसे नेमिंग कन्वेंशन, कोड फॉर्मेटिंग, और कॉम्प्लेक्सिटी, ताकि कोडिंग स्टैंडर्ड्स को लागू किया जा सके। Maven में इस फंक्शनैलिटी को एम्बेड करके, यह प्लगइन आपको अपनी बिल्ड के दौरान इन चेकों को ऑटोमेट करने की अनुमति देता है, यह सुनिश्चित करते हुए कि आपका कोडबेस सुसंगत स्टाइल और क्वालिटी गाइडलाइन्स का पालन करता है।

## Maven Checkstyle Plugin का उपयोग क्यों करें?

Maven Checkstyle Plugin का उपयोग करने के कई फायदे हैं:

- **सुसंगतता**: यह सुनिश्चित करता है कि सभी डेवलपर्स एक ही कोडिंग स्टैंडर्ड्स का पालन करें, जिससे पठनीयता और रखरखाव क्षमता में सुधार होता है।
- **गुणवत्ता**: यह संभावित मुद्दों का जल्द पता लगाता है, जैसे अत्यधिक जटिल मेथड्स या गायब Javadoc कमेंट्स।
- **स्वचालन**: चेक Maven बिल्ड प्रक्रिया के हिस्से के रूप में स्वचालित रूप से चलते हैं।
- **अनुकूलनशीलता**: आप नियमों को अपनी प्रोजेक्ट की विशिष्ट आवश्यकताओं के अनुरूप बना सकते हैं।

## Maven Checkstyle Plugin को कैसे सेट अप करें

अपने Maven प्रोजेक्ट में इस प्लगइन के साथ शुरुआत करने का तरीका यहां बताया गया है:

### 1. प्लगइन को अपने `pom.xml` में जोड़ें

प्लगइन को अपने `pom.xml` के `<build><plugins>` सेक्शन में शामिल करें। यदि आप किसी पैरेंट POM (जैसे `spring-boot-starter-parent`) का उपयोग कर रहे हैं, तो संस्करण आपके लिए मैनेज किया जा सकता है; अन्यथा, इसे स्पष्ट रूप से निर्दिष्ट करें।

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.1.2</version> <!-- नवीनतम संस्करण के साथ बदलें -->
        </plugin>
    </plugins>
</build>
```

### 2. प्लगइन को कॉन्फ़िगर करें

एक Checkstyle कॉन्फ़िगरेशन फ़ाइल (जैसे, `checkstyle.xml`) निर्दिष्ट करें जो लागू करने के लिए नियमों को परिभाषित करती है। आप बिल्ट-इन कॉन्फ़िगरेशन जैसे Sun Checks या Google Checks का उपयोग कर सकते हैं या अपनी स्वयं की कस्टम फ़ाइल बना सकते हैं।

उदाहरण कॉन्फ़िगरेशन:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.1.2</version>
            <configuration>
                <configLocation>checkstyle.xml</configLocation>
            </configuration>
        </plugin>
    </plugins>
</build>
```

### 3. एक Checkstyle कॉन्फ़िगरेशन फ़ाइल प्रदान करें

अपनी `checkstyle.xml` को प्रोजेक्ट रूट या किसी सबडायरेक्टरी में रखें। वैकल्पिक रूप से, किसी बाहरी कॉन्फ़िगरेशन को रेफरेंस करें, जैसे Google का:

```xml
<configLocation>google_checks.xml</configLocation>
```

Google Checks जैसे बाहरी कॉन्फ़िगरेशन का उपयोग करने के लिए, आपको Checkstyle डिपेंडेंसी जोड़ने की आवश्यकता हो सकती है:

```xml
<dependencies>
    <dependency>
        <groupId>com.puppycrawl.tools</groupId>
        <artifactId>checkstyle</artifactId>
        <version>8.44</version>
    </dependency>
</dependencies>
```

## Maven Checkstyle Plugin चलाना

यह प्लगइन Maven के लाइफसाइकल के साथ इंटीग्रेट होता है और इसे विभिन्न तरीकों से निष्पादित किया जा सकता है:

- **स्पष्ट रूप से Checkstyle चलाएं**:
  उल्लंघनों की जांच करने और संभावित रूप से बिल्ड को फेल करने के लिए:
  ```
  mvn checkstyle:check
  ```

- **बिल्ड के दौरान चलाएं**:
  डिफ़ॉल्ट रूप से, प्लगइन `verify` फेज से बाइंड होता है। उपयोग करें:
  ```
  mvn verify
  ```
  बिल्ड को फेल किए बिना रिपोर्ट जनरेट करने के लिए:
  ```
  mvn checkstyle:checkstyle
  ```

रिपोर्ट आमतौर पर `target/site/checkstyle.html` में जनरेट होती हैं।

## प्लगइन को कस्टमाइज़ करना

आप अपने `pom.xml` के `<configuration>` सेक्शन में प्लगइन के व्यवहार को समायोजित कर सकते हैं:

- **उल्लंघन पर फेल होना**:
  डिफ़ॉल्ट रूप से, यदि उल्लंघन पाए जाते हैं तो बिल्ड फेल हो जाती है। इसे अक्षम करने के लिए:
  ```xml
  <configuration>
      <failOnViolation>false</failOnViolation>
  </configuration>
  ```

- **फ़ाइलों को शामिल या बाहर करना**:
  नियंत्रित करें कि किन फ़ाइलों की जांच की जाए:
  ```xml
  <configuration>
      <includes>**/*.java</includes>
      <excludes>**/generated/**/*.java</excludes>
  </configuration>
  ```

- **उल्लंघन गंभीरता सेट करना**:
  वह गंभीरता स्तर परिभाषित करें जो बिल्ड फेल्योर को ट्रिगर करता है:
  ```xml
  <configuration>
      <violationSeverity>warning</violationSeverity>
  </configuration>
  ```

## उदाहरण `checkstyle.xml`

यहाँ एक बेसिक `checkstyle.xml` फ़ाइल है जो नेमिंग कन्वेंशन और Javadoc आवश्यकताओं को लागू करती है:

```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
    "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
    "https://checkstyle.org/dtds/configuration_1_3.dtd">

<module name="Checker">
    <module name="TreeWalker">
        <module name="JavadocMethod"/>
        <module name="MethodName"/>
        <module name="ConstantName"/>
    </module>
</module>
```

## सामान्य उपयोग के मामले

यह प्लगइन विभिन्न प्रकार के चेकों का समर्थन करता है, जिनमें शामिल हैं:
- कक्षाओं, विधियों और चरों के लिए नेमिंग कन्वेंशन।
- व्हाइटस्पेस और फॉर्मेटिंग का उचित उपयोग।
- Javadoc टिप्पणियों की उपस्थिति और शुद्धता।
- जटिल या लंबी विधियों का पता लगाना।

## एकीकरण और समस्या निवारण

- **IDE एकीकरण**: IntelliJ IDEA और Eclipse जैसे टूल रियल-टाइम फीडबैक के लिए एक ही `checkstyle.xml` का उपयोग कर सकते हैं।
- **निरंतर एकीकरण**: हर कमिट पर मानकों को लागू करने के लिए अपने CI पाइपलाइन में Checkstyle जोड़ें।
- **समस्या निवारण**: यदि कॉन्फ़िगरेशन फ़ाइल नहीं मिल रही है, तो `<configLocation>` पथ सत्यापित करें। सुनिश्चित करें कि डिपेंडेंसी संस्करण प्लगइन के साथ संरेखित हों।

## सारांश

**Maven Checkstyle Plugin** Maven का उपयोग करने वाले किसी भी Java प्रोजेक्ट के लिए एक मूल्यवान अतिरिक्त है। इसका उपयोग करने के लिए:
1. अपने `pom.xml` में प्लगइन को जोड़ें और कॉन्फ़िगर करें।
2. अपने वांछित नियमों के साथ एक `checkstyle.xml` प्रदान करें।
3. मानकों को लागू करने के लिए `mvn checkstyle:check` चलाएं या रिपोर्ट के लिए `mvn checkstyle:checkstyle` चलाएं।
4. अपने वर्कफ़्लो के अनुरूप आवश्यकतानुसार अनुकूलित करें।

यह प्लगइन न्यूनतम प्रयास के साथ उच्च-गुणवत्ता, सुसंगत कोड बनाए रखने में मदद करता है!