---
audio: false
lang: hi
layout: post
title: Eclipse का उपयोग
translated: true
---

### मुख्य बिंदु
- यह संभव लगता है कि Eclipse को IBM Websphere Liberty, Spring, Spring Boot, और Maven के साथ प्रभावी रूप से उपयोग किया जा सकता है, लेकिन सेटअप के लिए विशेष कनफिगरेशन की आवश्यकता होती है।
- अनुसंधान सुझाव देता है कि Eclipse में Spring Tool Suite (STS) और IBM Liberty Developer Tools को प्लग-इन के रूप में इंस्टॉल करने के लिए, बढ़े हुए कार्यक्षमता के लिए।
- सबूत Spring Boot प्रोजेक्ट बनाने की ओर इशारा करता है, STS या Spring Initializr का उपयोग करके, फिर इसे Websphere Liberty डिप्लॉयमेंट के लिए कनफिगर करने के लिए।

### Eclipse सेटअप
शुरू करने के लिए, "Eclipse IDE for Enterprise Java and Web Developers" को [Eclipse Downloads](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) से डाउनलोड और इंस्टॉल करें। सुनिश्चित करें कि आपके पास JDK 17 या नया इंस्टॉल किया गया है, जिसे आप अपने टर्मिनल में `java -version` चलाकर जांच सकते हैं।

### Spring और Spring Boot के लिए कनफिगरेशन
Eclipse में Help -> Eclipse Marketplace पर जाएं, "Spring Tools" खोजें, और उपयुक्त संस्करण इंस्टॉल करें। यह Spring और Spring Boot विकास को बढ़ाता है। आप Eclipse में File -> New -> Spring Starter Project से नया Spring Boot प्रोजेक्ट सीधे बना सकते हैं, Maven को बिल्ड टूल के रूप में चुनें और आवश्यक निर्भरताओं जैसे Spring Web जोड़ें।

### IBM Websphere Liberty के साथ एकीकृत
Eclipse Marketplace से "IBM Liberty Developer Tools" इंस्टॉल करें, "IBM Liberty Developer Tools" खोजें और इंस्टॉलेशन प्रोम्प्ट्स का पालन करें। एक Websphere Liberty सर्वर सेटअप करें, Window -> Preferences -> Servers -> Runtime Environments पर जाएं, नया Websphere Liberty रनटाइम जोड़ें, और File -> New -> Other -> Server के माध्यम से सर्वर इंस्टेंस बनाएं। सुनिश्चित करें कि सर्वर के server.xml में `<feature>springBoot-2.0</feature>` शामिल है, Spring Boot समर्थन के लिए, जैसा कि [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html) में विस्तार से बताया गया है।

### आपका एप्लिकेशन डिप्लॉय करें
अपने Spring Boot एप्लिकेशन को `SpringBootServletInitializer` से विस्तारित करने के बजाय, एक एम्बेडेड सर्वर शुरू करने के लिए एक मुख्य विधि का उपयोग करने के बजाय, इसे एक WAR फ़ाइल के रूप में पैकेज करें, अपने pom.xml में `<packaging>war</packaging>` सेट करके। डिप्लॉय करने के लिए, प्रोजेक्ट पर दाएं क्लिक करें, "Run As -> Run on Server" चुनें, और अपने Liberty सर्वर चुनें। यह सुनिश्चित करता है कि एप्लिकेशन Liberty के वेब कंटेनर पर चलता है।

---

### सर्वेक्षण नोट: Eclipse के साथ IBM Websphere Liberty, Spring, Spring Boot, और Maven का उपयोग करने का व्यापक मार्गदर्शन

यह मार्गदर्शन Eclipse को IBM Websphere Liberty, Spring, Spring Boot, और Maven के साथ प्रभावी रूप से उपयोग करने के लिए एक विस्तृत मार्गदर्शन प्रदान करता है, जो इन इकोसिस्टम में काम करने वाले डेवलपर्स के लिए तैयार किया गया है। इस प्रक्रिया में Eclipse सेटअप, आवश्यक प्लग-इन इंस्टॉल, प्रोजेक्ट बनाना और कनफिगर करना, और एप्लिकेशन डिप्लॉय करना शामिल है, एकीकृत और फरवरी 27, 2025 तक के सर्वश्रेष्ठ प्रथाओं पर ध्यान केंद्रित किया गया है।

#### Eclipse सेटअप और पूर्व-आवश्यकताएं
Eclipse एक मजबूत IDE है Java विकास के लिए, विशेष रूप से एंटरप्राइज एप्लिकेशन के लिए। इस सेटअप के लिए, "Eclipse IDE for Enterprise Java and Web Developers" संस्करण 2024-06 डाउनलोड करें, जो [Eclipse Downloads](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) पर उपलब्ध है। सुनिश्चित करें कि आपके सिस्टम में JDK 17 या नया है, जिसे आप टर्मिनल में `java -version` चलाकर जांच सकते हैं। यह संस्करण आधुनिक Spring और Liberty विशेषताओं के साथ संगतता सुनिश्चित करता है।

#### आवश्यक प्लग-इन इंस्टॉल करें
Eclipse को Spring और Spring Boot विकास के लिए बढ़ाने के लिए, Spring Tool Suite (STS) इंस्टॉल करें, Spring टूलिंग का अगला संस्करण। इस तक पहुंचने के लिए Help -> Eclipse Marketplace पर जाएं, "Spring Tools" खोजें, और "Spring Tools (aka Spring IDE and Spring Tool Suite)" के रूप में लेबल किए गए प्रवेश इंस्टॉल करें। यह प्लग-इन, [Spring Tools](https://spring.io/tools/) पर विस्तार से बताया गया है, जो Spring आधारित एप्लिकेशन के लिए विश्व स्तर का समर्थन प्रदान करता है, Eclipse के साथ सीमित रूप से एकीकृत होता है, जैसे प्रोजेक्ट बनाना और डिबग करना।

IBM Websphere Liberty एकीकृत करने के लिए, Eclipse Marketplace से "IBM Liberty Developer Tools" इंस्टॉल करें, "IBM Liberty Developer Tools" खोजें। यह प्लग-इन, [IBM Liberty Developer Tools](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools) में Eclipse 2024-06 के लिए परीक्षण किया गया है, Liberty पर Java EE एप्लिकेशन बनाना और डिप्लॉय करना सुविधा प्रदान करता है, 2019-12 से संस्करणों का समर्थन करता है।

#### एक Spring Boot प्रोजेक्ट बनाएं
Eclipse में STS इंस्टॉल किए गए Spring Boot प्रोजेक्ट बनाने के दो प्रमुख तरीके हैं:

1. **Spring Initializr का उपयोग करें**: [Spring Initializr](https://start.spring.io/) पर जाएं, Maven को बिल्ड टूल के रूप में चुनें, अपने प्रोजेक्ट मेटाडेटा (ग्रुप, आर्टिफैक्ट आदि) चुनें, और निर्भरताओं जैसे Spring Web जोड़ें। प्रोजेक्ट को एक ZIP फ़ाइल के रूप में जनरेट करें, इसे एक्सट्रैक्ट करें, और Eclipse में File -> Import -> Existing Maven Project के माध्यम से इम्पोर्ट करें, एक्सट्रैक्ट किए गए फ़ोल्डर चुनें।

2. **STS सीधे उपयोग करें**: Eclipse खोलें, File -> New -> Other पर जाएं, Spring Boot को विस्तारित करें, और "Spring Starter Project" चुनें। वाइज़र्ड का पालन करें, सुनिश्चित करें कि Maven को प्रकार के रूप में चुना गया है, और निर्भरताओं को चुनें। यह विधि, [Creating Spring Boot Project with Eclipse and Maven](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven) में वर्णित है, Eclipse के वर्कस्पेस के साथ एकीकृत होने के लिए पसंद की जाती है।

दोनों विधियाँ सुनिश्चित करती हैं कि एक Maven आधारित प्रोजेक्ट है, जो Spring Boot के साथ निर्भरता प्रबंधन के लिए आवश्यक है।

#### Websphere Liberty डिप्लॉयमेंट के लिए कनफिगर करें
Websphere Liberty पर डिप्लॉय करने के लिए, अपने Spring Boot एप्लिकेशन को Liberty के वेब कंटेनर पर चलने के लिए कनफिगर करें, एक एम्बेडेड सर्वर शुरू करने के बजाय। इसमें शामिल है:

- सुनिश्चित करें कि मुख्य एप्लिकेशन क्लास `SpringBootServletInitializer` से विस्तारित है। उदाहरण के लिए:

  ```java
  @SpringBootApplication
  public class MyApplication extends SpringBootServletInitializer {
      // कोई मुख्य विधि नहीं; Liberty शुरू करता है
  }
  ```

- pom.xml को एक WAR फ़ाइल के रूप में पैकेज करने के लिए अपडेट करें, जोड़ें:

  ```xml
  <packaging>war</packaging>
  ```

  यह आवश्यक है, जैसा कि [Deploying Spring Boot Applications](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet) में वर्णित है, परंपरागत सर्वलेट कंटेनर डिप्लॉयमेंट के लिए।

Websphere Liberty, विशेष रूप से इसके ओपन-सोर्स संस्करण Open Liberty, Spring Boot एप्लिकेशन के साथ विशेषताओं के साथ समर्थन करता है। सुनिश्चित करें कि Liberty सर्वर के server.xml में `<feature>springBoot-2.0</feature>` शामिल है, Spring Boot 2.x समर्थन के लिए, जैसा कि [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html) में विस्तार से बताया गया है। यह कनफिगरेशन एम्बेडेड वेब कंटेनर को अक्षम करता है, Liberty का उपयोग करता है।

#### Eclipse में Websphere Liberty सर्वर सेटअप और कनफिगर करें
IBM Liberty Developer Tools इंस्टॉल किए गए, एक Liberty सर्वर सेटअप करें:

- Window -> Preferences -> Servers -> Runtime Environments पर जाएं, "Add" पर क्लिक करें, और "WebSphere Application Server Liberty" चुनें। वाइज़र्ड का पालन करें, अपने Liberty इंस्टॉलेशन को खोजें, जो आमतौर पर एक डायरेक्टरी में होता है जैसे `<Liberty_Root>/wlp`, जैसा कि [Liberty and Eclipse](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9) में उल्लेख किया गया है।

- File -> New -> Other -> Server पर जाएं, "WebSphere Application Server Liberty" और आपने कनफिगर किया है रनटाइम चुनें, एक नया सर्वर इंस्टेंस बनाएं। सर्वर का नाम दें और आवश्यकतानुसार सेटिंग्स को समायोजित करें।

- सर्वर के server.xml को संपादित करें, जो Servers view के माध्यम से पहुंचा जा सकता है, आवश्यक विशेषताओं को शामिल करने के लिए। Spring Boot के लिए, जोड़ें:

  ```xml
  <featureManager>
      <feature>springBoot-2.0</feature>
      <!-- अन्य विशेषताएं जैसे servlet-3.1 वेब समर्थन के लिए -->
  </featureManager>
  ```

यह सेटअप, [IBM WebSphere Liberty](https://www.ibm.com/docs/en/was-liberty/base?topic=liberty-overview) द्वारा समर्थित है, जो Spring Boot एप्लिकेशन के साथ संगतता सुनिश्चित करता है।

#### एप्लिकेशन डिप्लॉय और चलाएं
डिप्लॉय करने के लिए, प्रोजेक्ट एक्सप्लोरर में अपने प्रोजेक्ट पर दाएं क्लिक करें, "Run As -> Run on Server" चुनें, अपने Liberty सर्वर चुनें, और Finish पर क्लिक करें। Eclipse WAR फ़ाइल को Liberty सर्वर पर डिप्लॉय करेगा, और आप Console view में लॉग्स को मॉनिटर कर सकते हैं। सुनिश्चित करें कि एप्लिकेशन कंटेक्स्ट रूट सर्वर.xml में सही तरह से सेट है, आमतौर पर `<webApplication>` टैग के नीचे, ताकि आप अपने एप्लिकेशन को सही URL के माध्यम से पहुंच सकें, उदाहरण के लिए, `http://localhost:9080/yourapp`।

डिबग करने के लिए, डिबग पर्स्पेक्टिव का उपयोग करें, आवश्यकतानुसार ब्रेकपॉइंट सेट करें, Liberty के लिए रिमोट डिबगिंग का समर्थन का लाभ उठाएं, जैसा कि [Debugging with Eclipse and Liberty](https://stackoverflow.com/questions/41428156/how-to-debug-web-service-with-eclipse-websphere-liberty) में चर्चा की गई है।

#### अतिरिक्त विचार
- **पैकेजिंग विकल्प**: जबकि WAR सर्वलेट कंटेनर के लिए मानक है, Open Liberty भी JAR डिप्लॉयमेंट का समर्थन करता है, जैसा कि [Configure and Deploy Spring Boot to Open Liberty](https://openliberty.io/docs/latest/deploy-spring-boot.html) में देखा गया है। JAR के लिए, सुनिश्चित करें कि एप्लिकेशन को एक एम्बेडेड सर्वर शुरू करने के लिए कनफिगर किया गया है, जो Liberty विशेषताओं या कनफिगरेशन की अतिरिक्त आवश्यकता हो सकती है।
- **Maven एकीकृत**: Maven का उपयोग निर्भरता प्रबंधन के लिए करें, सुनिश्चित करें कि `liberty-maven-plugin` शामिल है, जैसा कि [IBM Liberty Maven Plugin](https://github.com/WASdev/ci.maven#liberty-maven-plugin) में उल्लेख किया गया है, स्वचालित डिप्लॉयमेंट के लिए।
- **संघर्ष समाधान**: अगर समस्याएं उठती हैं, सर्वर लॉग्स को `logs` डायरेक्टरी में अपने Liberty सर्वर इंस्टेंस के नीचे जांचें, और Liberty संस्करण और Spring Boot के बीच संगतता सुनिश्चित करें, जैसे Liberty 8.5.5.9 या उससे अधिक संस्करण, जो रनने योग्य JARs का समर्थन करते हैं, जैसा कि [Stack Overflow Discussion](https://stackoverflow.com/questions/36132791/how-to-use-websphere-liberty-in-spring-boot-application) में उल्लेख किया गया है।

यह व्यापक सेटअप सुनिश्चित करता है कि Eclipse का उपयोग Spring Boot एप्लिकेशन को IBM Websphere Liberty पर विकसित और डिप्लॉय करने के लिए प्रभावी है, Maven के लिए बिल्ड प्रबंधन का उपयोग करता है।

#### तालिका: डिप्लॉयमेंट विकल्पों की तुलना

| डिप्लॉयमेंट प्रकार | फायदे                                      | नुकसान                                      | कनफिगरेशन नोट्स                          |
|-----------------|-------------------------------------------|-------------------------------------------|----------------------------------------------|
| WAR फ़ाइल        | सर्वलेट कंटेनर के लिए मानक, व्यापक समर्थन | `SpringBootServletInitializer` से विस्तारित करना आवश्यक है | pom.xml में `<packaging>war</packaging>` सेट करें  |
| JAR फ़ाइल        | विकास के लिए सरल, Open Liberty द्वारा समर्थित | Liberty विशेषताओं की अतिरिक्त आवश्यकता हो सकती है   | सुनिश्चित करें कि कोई एम्बेडेड सर्वर शुरू नहीं होता, springBoot विशेषता का उपयोग करें |

यह तालिका, [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html) से ली गई है, प्रोजेक्ट की आवश्यकताओं के आधार पर उपयुक्त डिप्लॉयमेंट रणनीति चुनने में मदद करता है।

### मुख्य संदर्भ
- [Creating Spring Boot Project with Eclipse and Maven, चरण-दर-चरण मार्गदर्शन](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)
- [IBM Liberty Developer Tools, Eclipse प्लग-इन Java EE एप्लिकेशन के लिए](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)
- [Open Liberty Docs, Spring Boot एप्लिकेशन डिप्लॉय करने](https://openliberty.io/docs/latest/deploy-spring-boot.html)
- [Spring Tools, अगला पीढ़ी का टूलिंग Spring विकास के लिए](https://spring.io/tools/)
- [Eclipse Downloads, एंटरप्राइज Java विकास के लिए पैकेज](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers)
- [Liberty and Eclipse, विकास वातावरण इंस्टॉल करने](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9)
- [Deploying Spring Boot Applications, Spring Boot संदर्भ](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet)