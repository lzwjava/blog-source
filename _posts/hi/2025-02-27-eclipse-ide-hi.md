---
audio: false
generated: true
lang: hi
layout: post
title: एक्लिप्स का उपयोग
translated: true
type: note
---

### मुख्य बिंदु
- ऐसा प्रतीत होता है कि Eclipse को IBM Websphere Liberty, Spring, Spring Boot, और Maven के साथ प्रभावी रूप से उपयोग किया जा सकता है, लेकिन सेटअप के लिए विशिष्ट कॉन्फ़िगरेशन की आवश्यकता होती है।
- शोध से पता चलता है कि बेहतर कार्यक्षमता के लिए Eclipse में Spring Tool Suite (STS) और IBM Liberty Developer Tools प्लग-इन स्थापित करने की सलाह दी जाती है।
- प्रमाण इस ओर इशारा करते हैं कि STS या Spring Initializr का उपयोग करके एक Spring Boot प्रोजेक्ट बनाया जाए, और फिर इसे Websphere Liberty डिप्लॉयमेंट के लिए कॉन्फ़िगर किया जाए।

### Eclipse सेटअप
शुरुआत करने के लिए, [Eclipse डाउनलोड](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) से "Eclipse IDE for Enterprise Java and Web Developers" डाउनलोड और इंस्टॉल करें। सुनिश्चित करें कि आपके सिस्टम पर JDK 17 या नया वर्जन इंस्टॉल है, जिसे आप अपने टर्मिनल में `java -version` चलाकर सत्यापित कर सकते हैं।

### Spring और Spring Boot के लिए कॉन्फ़िगरेशन
Eclipse में Help -> Eclipse Marketplace पर जाकर "Spring Tools" खोजें और उचित वर्जन इंस्टॉल करके Spring Tool Suite (STS) प्लग-इन इंस्टॉल करें। यह Spring और Spring Boot डेवलपमेंट को बेहतर बनाता है। आप Eclipse में सीधे File -> New -> Spring Starter Project के माध्यम से एक नया Spring Boot प्रोजेक्ट बना सकते हैं, बिल्ड टूल के रूप में Maven चुन सकते हैं और Spring Web जैसी आवश्यक डिपेंडेंसीज जोड़ सकते हैं।

### IBM Websphere Liberty के साथ एकीकरण
Eclipse Marketplace में "IBM Liberty Developer Tools" खोजें और इंस्टॉलेशन प्रॉम्प्ट का पालन करके IBM Liberty Developer Tools इंस्टॉल करें। Window -> Preferences -> Servers -> Runtime Environments पर जाकर एक नया Websphere Liberty रनटाइम जोड़कर, और File -> New -> Other -> Server के माध्यम से एक सर्वर इंस्टेंस बनाकर एक Websphere Liberty सर्वर सेट अप करें। सुनिश्चित करें कि सर्वर के server.xml में Spring Boot सपोर्ट के लिए `<feature>springBoot-2.0</feature>` शामिल है, जैसा कि [Open Liberty डॉक्स](https://openliberty.io/docs/latest/deploy-spring-boot.html) में विस्तृत है।

### अपनी एप्लिकेशन को डिप्लॉय करना
अपनी Spring Boot एप्लिकेशन को एक एम्बेडेड सर्वर शुरू करने वाले मुख्य मेथड के बजाय `SpringBootServletInitializer` का विस्तार करने के लिए संशोधित करें, अपने pom.xml में `<packaging>war</packaging>` सेट करके इसे एक WAR फ़ाइल के रूप में पैकेज करें। प्रोजेक्ट पर राइट-क्लिक करके, "Run As -> Run on Server" चुनकर, और अपने Liberty सर्वर का चयन करके डिप्लॉय करें। यह सुनिश्चित करता है कि एप्लिकेशन Liberty के वेब कंटेनर पर चले।

---

### सर्वे नोट: Eclipse को IBM Websphere Liberty, Spring, Spring Boot, और Maven के साथ उपयोग करने की व्यापक गाइड

यह गाइड इन इकोसिस्टम में काम करने वाले डेवलपर्स के लिए तैयार की गई है, जो IBM Websphere Liberty, Spring, Spring Boot, और Maven के संयोजन में Eclipse का प्रभावी ढंग से उपयोग करने के लिए एक विस्तृत वॉकथ्रू प्रदान करती है। इस प्रक्रिया में Eclipse सेटअप, आवश्यक प्लग-इन इंस्टॉल करना, प्रोजेक्ट बनाना और कॉन्फ़िगर करना, और एप्लिकेशन को डिप्लॉय करना शामिल है, जिसमें 27 फरवरी, 2025 तक एकीकरण और सर्वोत्तम प्रथाओं पर ध्यान केंद्रित किया गया है।

#### Eclipse सेटअप और पूर्वापेक्षाएँ
Eclipse एंटरप्राइज़ एप्लिकेशन के लिए, विशेष रूप से Java डेवलपमेंट के लिए एक मजबूत IDE के रूप में कार्य करता है। इस सेटअप के लिए, [Eclipse डाउनलोड](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) से "Eclipse IDE for Enterprise Java and Web Developers" वर्जन 2024-06 डाउनलोड करें। सुनिश्चित करें कि आपके सिस्टम पर JDK 17 या नया वर्जन है, जिसे आप टर्मिनल में `java -version` चलाकर जांच सकते हैं। यह वर्जन आधुनिक Spring और Liberty फीचर्स के साथ संगतता सुनिश्चित करता है।

#### आवश्यक प्लग-इन इंस्टॉल करना
Spring और Spring Boot डेवलपमेंट के लिए Eclipse को बेहतर बनाने के लिए, Spring टूलिंग की अगली पीढ़ी, Spring Tool Suite (STS) इंस्टॉल करें। इसे Help -> Eclipse Marketplace पर एक्सेस करें, "Spring Tools" खोजें, और "Spring Tools (aka Spring IDE and Spring Tool Suite)" लेबल वाली एंट्री को इंस्टॉल करें। यह प्लग-इन, जिसका विवरण [Spring टूल्स](https://spring.io/tools/) पर है, Spring-आधारित एप्लिकेशन के लिए विश्व-स्तरीय सपोर्ट प्रदान करता है, जो प्रोजेक्ट निर्माण और डीबगिंग जैसी सुविधाओं के लिए Eclipse के साथ सहजता से एकीकृत होता है।

IBM Websphere Liberty एकीकरण के लिए, Eclipse Marketplace में "IBM Liberty Developer Tools" खोजकर IBM Liberty Developer Tools भी इंस्टॉल करें। यह प्लग-इन, जिसे Eclipse 2024-06 के लिए [IBM Liberty Developer टूल्स](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools) में नोट किया गया है, Liberty पर Java EE एप्लिकेशन बनाने और डिप्लॉय करने की सुविधा प्रदान करता है, जो 2019-12 तक के वर्जन के लिए सपोर्ट के साथ आता है।

#### एक Spring Boot प्रोजेक्ट बनाना
STS इंस्टॉल होने पर Eclipse में Spring Boot प्रोजेक्ट बनाने के दो प्राथमिक तरीके हैं:

1. **Spring Initializr का उपयोग करना**: [Spring Initializr](https://start.spring.io/) पर जाएं, बिल्ड टूल के रूप में Maven चुनें, अपनी प्रोजेक्ट मेटाडेटा (Group, Artifact, आदि) चुनें, और Spring Web जैसी डिपेंडेंसीज जोड़ें। प्रोजेक्ट को ZIP फ़ाइल के रूप में जनरेट करें, इसे एक्सट्रैक्ट करें, और File -> Import -> Existing Maven Project के माध्यम से एक्सट्रैक्टेड फोल्डर का चयन करके Eclipse में इम्पोर्ट करें।

2. **STS का सीधे उपयोग करना**: Eclipse खोलें, File -> New -> Other पर जाएं, Spring Boot का विस्तार करें, और "Spring Starter Project" चुनें। विजार्ड का पालन करें, यह सुनिश्चित करते हुए कि प्रकार के रूप में Maven चुना गया है, और डिपेंडेंसीज का चयन करें। यह विधि, जैसा कि [Eclipse और Maven के साथ Spring Boot प्रोजेक्ट बनाना](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven) में वर्णित है, Eclipse के वर्कस्पेस के साथ इसके एकीकरण के कारण पसंद की जाती है।

दोनों विधियां Spring Boot के साथ डिपेंडेंसी मैनेजमेंट के लिए महत्वपूर्ण, एक Maven-आधारित प्रोजेक्ट सुनिश्चित करती हैं।

#### Websphere Liberty डिप्लॉयमेंट के लिए कॉन्फ़िगरेशन
Websphere Liberty पर डिप्लॉय करने के लिए, अपनी Spring Boot एप्लिकेशन को एक एम्बेडेड सर्वर शुरू करने के बजाय Liberty के वेब कंटेनर पर चलने के लिए संशोधित करें। इसमें शामिल है:

- यह सुनिश्चित करना कि मुख्य एप्लिकेशन क्लास `SpringBootServletInitializer` का विस्तार करती है। उदाहरण के लिए:

  ```java
  @SpringBootApplication
  public class MyApplication extends SpringBootServletInitializer {
      // कोई मुख्य मेथड नहीं; Liberty स्टार्टअप को संभालता है
  }
  ```

- WAR फ़ाइल के रूप में पैकेज करने के लिए pom.xml को अपडेट करें:

  ```xml
  <packaging>war</packaging>
  ```

  यह पारंपरिक सर्वलेट कंटेनर डिप्लॉयमेंट के लिए आवश्यक है, जैसा कि [Spring Boot एप्लिकेशन डिप्लॉय करना](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet) में नोट किया गया है।

Websphere Liberty, विशेष रूप से इसके ओपन-सोर्स वेरिएंट Open Liberty, विशिष्ट फीचर्स के साथ Spring Boot एप्लिकेशन का समर्थन करता है। सुनिश्चित करें कि Liberty सर्वर के server.xml में Spring Boot 2.x सपोर्ट के लिए `<feature>springBoot-2.0</feature>` शामिल है, जैसा कि [Open Liberty डॉक्स](https://openliberty.io/docs/latest/deploy-spring-boot.html) में विस्तृत है। यह कॉन्फ़िगरेशन एम्बेडेड वेब कंटेनर को अक्षम करता है, और इसके बजाय Liberty का लाभ उठाता है।

#### Eclipse में Websphere Liberty सर्वर सेट अप और कॉन्फ़िगर करना
IBM Liberty Developer Tools इंस्टॉल होने पर, एक Liberty सर्वर सेट अप करें:

- Window -> Preferences -> Servers -> Runtime Environments पर नेविगेट करें, "Add" पर क्लिक करें, और "WebSphere Application Server Liberty" चुनें। अपनी Liberty इंस्टॉलेशन को लोकेट करने के लिए विजार्ड का पालन करें, जो आमतौर पर `<Liberty_Root>/wlp` जैसे डायरेक्टरी में होती है, जैसा कि [Liberty और Eclipse](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9) में उल्लेख किया गया है।

- File -> New -> Other -> Server के माध्यम से एक नया सर्वर इंस्टेंस बनाएं, "WebSphere Application Server Liberty" और आपके द्वारा कॉन्फ़िगर किए गए रनटाइम का चयन करें। सर्वर का नाम दें और आवश्यकतानुसार सेटिंग्स समायोजित करें।

- सर्वर के server.xml को संपादित करें, जो Servers व्यू के माध्यम से एक्सेस किया जा सकता है, ताकि आवश्यक फीचर्स शामिल किए जा सकें। Spring Boot के लिए, जोड़ें:

  ```xml
  <featureManager>
      <feature>springBoot-2.0</feature>
      <!-- वेब सपोर्ट के लिए servlet-3.1 जैसे अन्य फीचर्स -->
  </featureManager>
  ```

यह सेटअप, [IBM WebSphere Liberty](https://www.ibm.com/docs/en/was-liberty/base?topic=liberty-overview) द्वारा समर्थित, Spring Boot एप्लिकेशन के साथ संगतता सुनिश्चित करता है।

#### एप्लिकेशन को डिप्लॉय और रन करना
डिप्लॉय करने के लिए, Project Explorer में अपने प्रोजेक्ट पर राइट-क्लिक करें, "Run As -> Run on Server" चुनें, अपने Liberty सर्वर का चयन करें, और Finish पर क्लिक करें। Eclipse WAR फ़ाइल को Liberty सर्वर पर डिप्लॉय करेगा, और आप Console व्यू में लॉग की निगरानी कर सकते हैं। सुनिश्चित करें कि एप्लिकेशन कॉन्टेक्स्ट रूट server.xml में सही ढंग से सेट है, आमतौर पर `<webApplication>` टैग के तहत, ताकि आप उचित URL, जैसे `http://localhost:9080/yourapp` के माध्यम से अपनी एप्लिकेशन तक पहुंच सकें।

डीबगिंग के लिए, Debug परस्पेक्टिव का उपयोग करें, आवश्यकतानुसार ब्रेकपॉइंट सेट करते हुए, [Eclipse और Liberty के साथ डीबगिंग](https://stackoverflow.com/questions/41428156/how-to-debug-web-service-with-eclipse-websphere-liberty) में चर्चा के अनुसार रिमोट डीबगिंग के लिए Liberty के सपोर्ट का लाभ उठाएं।

#### अतिरिक्त विचार
- **पैकेजिंग विकल्प**: जबकि WAR सर्वलेट कंटेनर के लिए मानक है, Open Liberty JAR डिप्लॉयमेंट का भी समर्थन करता है, जैसा कि [Open Liberty पर Spring Boot को कॉन्फ़िगर और डिप्लॉय करना](https://openliberty.io/docs/latest/deploy-spring-boot.html) में देखा गया है। JAR के लिए, सुनिश्चित करें कि एप्लिकेशन एक एम्बेडेड सर्वर शुरू न करने के लिए कॉन्फ़िगर है, जिसके लिए अतिरिक्त Liberty फीचर्स या कॉन्फ़िगरेशन की आवश्यकता हो सकती है।
- **Maven एकीकरण**: डिपेंडेंसी मैनेजमेंट के लिए Maven का उपयोग करें, यह सुनिश्चित करते हुए कि स्वचालित डिप्लॉयमेंट के लिए `liberty-maven-plugin` शामिल है, जैसा कि [IBM Liberty Maven प्लगइन](https://github.com/WASdev/ci.maven#liberty-maven-plugin) में नोट किया गया है।
- **समस्या निवारण**: यदि कोई समस्या उत्पन्न होती है, तो अपने Liberty सर्वर इंस्टेंस के तहत `logs` डायरेक्टरी में सर्वर लॉग जांचें, और Liberty वर्जन और Spring Boot के बीच संगतता सुनिश्चित करें, क्योंकि Liberty 8.5.5.9 या उच्चतर जैसे वर्जन रननेबल JAR का समर्थन करते हैं, [Stack Overflow चर्चा](https://stackoverflow.com/questions/36132791/how-to-use-websphere-liberty-in-spring-boot-application) के अनुसार।

यह व्यापक सेटअप बिल्ड मैनेजमेंट के लिए Maven का लाभ उठाते हुए, IBM Websphere Liberty पर Spring Boot एप्लिकेशन डेवलप और डिप्लॉय करने के लिए Eclipse के प्रभावी उपयोग को सुनिश्चित करता है।

#### तालिका: डिप्लॉयमेंट विकल्पों की तुलना

| डिप्लॉयमेंट प्रकार | फायदे                                      | नुकसान                                      | कॉन्फ़िगरेशन नोट्स                          |
|-----------------|-------------------------------------------|-------------------------------------------|----------------------------------------------|
| WAR फ़ाइल        | सर्वलेट कंटेनर के लिए मानक, व्यापक रूप से समर्थित | `SpringBootServletInitializer` का विस्तार करने की आवश्यकता | pom.xml में `<packaging>war</packaging>` सेट करें  |
| JAR फ़ाइल        | डेवलपमेंट के लिए सरल, Open Liberty द्वारा समर्थित | अतिरिक्त Liberty फीचर्स की आवश्यकता हो सकती है   | सुनिश्चित करें कि कोई एम्बेडेड सर्वर शुरू न हो, springBoot फीचर का उपयोग करें |

यह तालिका, [Open Liberty डॉक्स](https://openliberty.io/docs/latest/deploy-spring-boot.html) से ली गई है, प्रोजेक्ट की आवश्यकताओं के आधार पर उपयुक्त डिप्लॉयमेंट रणनीति चुनने में सहायता करती है।

### मुख्य उद्धरण
- [Eclipse और Maven के साथ Spring Boot प्रोजेक्ट बनाना, चरण-दर-चरण गाइड](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)
- [IBM Liberty Developer Tools, Java EE एप्लिकेशन के लिए Eclipse प्लगइन](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)
- [Open Liberty डॉक्स, Spring Boot एप्लिकेशन डिप्लॉय करना](https://openliberty.io/docs/latest/deploy-spring-boot.html)
- [Spring टूल्स, Spring डेवलपमेंट के लिए अगली पीढ़ी की टूलिंग](https://spring.io/tools/)
- [Eclipse डाउनलोड, एंटरप्राइज़ Java डेवलपमेंट के लिए पैकेज](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers)
- [Liberty और Eclipse, डेवलपमेंट एनवायरनमेंट इंस्टॉल करना](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9)
- [Spring Boot एप्लिकेशन डिप्लॉय करना, Spring Boot संदर्भ](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet)