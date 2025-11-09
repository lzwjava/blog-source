---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: जेएसपी से शुरुआत करना
translated: true
type: note
---

JavaServer Pages (JSP) Java एप्लिकेशन में डायनामिक वेब कंटेंट बनाने के लिए इस्तेमाल होने वाली एक सर्वर-साइड टेक्नोलॉजी है। यह आपको Java कोड को सीधे HTML पेज में एम्बेड करने की अनुमति देती है, जिससे यूजर इनपुट या डेटा के आधार पर डायनामिक रिस्पॉन्स जनरेट करना आसान हो जाता है। JSP, Jakarta EE (पहले Java EE) प्लेटफॉर्म का हिस्सा है और वेब एप्लिकेशन में सर्वलेट्स के साथ अच्छी तरह काम करती है।

नीचे JSP के साथ शुरुआत करने के लिए एक स्टेप-बाय-स्टेप गाइड दी गई है, सेटअप से लेकर डिप्लॉयमेंट तक। यह Java और HTML के बेसिक नॉलेज को मानकर चलती है।

## 1. आवश्यक शर्तें
- **Java Development Kit (JDK)**: JDK 8 या बाद का वर्जन इंस्टॉल करें (मॉडर्न ऐप्स के लिए JDK 17+ रिकमेंडेड है)। [Oracle](https://www.oracle.com/java/technologies/downloads/) से डाउनलोड करें या OpenJDK का उपयोग करें।
- **वेब सर्वर/कंटेनर**: Apache Tomcat (बिगिनर्स के लिए फ्री और आसान) का उपयोग करें। [Apache Tomcat](https://tomcat.apache.org/) से डाउनलोड करें।
- **IDE (ऑप्शनल लेकिन रिकमेंडेड)**: आसान डेवलपमेंट के लिए IntelliJ IDEA, Eclipse, या VS Code with Java एक्सटेंशन।

## 2. अपना एनवायरनमेंट सेट करें
1. Tomcat इंस्टॉल करें:
   - Tomcat आर्काइव को एक डायरेक्टरी में एक्सट्रैक्ट करें (जैसे, Windows पर `C:\tomcat` या Linux पर `/opt/tomcat`)।
   - `bin/startup.bat` (Windows) या `bin/startup.sh` (Unix) चलाकर Tomcat स्टार्ट करें। यह सत्यापित करने के लिए कि यह चल रहा है, अपने ब्राउज़र में `http://localhost:8080` एक्सेस करें।

2. प्रोजेक्ट स्ट्रक्चर बनाएँ:
   - Tomcat की `webapps` फोल्डर में, अपनी ऐप के लिए एक नई डायरेक्टरी बनाएँ (जैसे, `my-jsp-app`)।
   - इसके अंदर, बनाएँ:
     - `WEB-INF/web.xml` (डिप्लॉयमेंट डिस्क्रिप्टर, JSP 2.2+ में ऑप्शनल लेकिन कॉन्फ़िग के लिए अच्छा)।
     - JSP फाइलों के लिए एक रूट फोल्डर (जैसे, `index.jsp`)।

   बेसिक `web.xml` उदाहरण:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee
            https://jakarta.ee/xml/ns/jakartaee/web-app_5_0.xsd"
            version="5.0">
       <display-name>My JSP App</display-name>
   </web-app>
   ```

## 3. अपना पहला JSP पेज लिखें
JSP फाइलों का एक्सटेंशन `.jsp` होता है और ये HTML को Java कोड के साथ स्क्रिप्टलेट्स (`<% %>`), एक्सप्रेशन (`<%= %>`), और डिक्लेरेशन (`<%! %>`) का उपयोग करके कंबाइन करती हैं। मॉडर्न बेस्ट प्रैक्टिसेज के लिए, रॉ स्क्रिप्टलेट्स से बचने के लिए JSP Expression Language (EL) और JSTL (JavaServer Pages Standard Tag Library) का उपयोग करें।

उदाहरण: अपनी ऐप के रूट में `index.jsp` बनाएँ:
```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>  <!-- JSTL के लिए, अगर इस्तेमाल करें तो -->

<html>
<head>
    <title>Hello JSP</title>
</head>
<body>
    <h1>Welcome to JSP!</h1>
    
    <!-- Scriptlet: Java code -->
    <% 
        String name = request.getParameter("name") != null ? request.getParameter("name") : "World";
        java.util.Date now = new java.util.Date();
    %>
    
    <!-- Expression: Output value -->
    <p>Hello, <%= name %>! The time is <%= now %>.</p>
    
    <!-- Using EL (Expression Language) for cleaner output -->
    <p>Your name via EL: ${param.name}</p>
    
    <!-- JSTL example: Loop over a list -->
    <c:set var="fruits" value="${{'Apple', 'Banana', 'Cherry'}}" />
    <ul>
        <c:forEach var="fruit" items="${fruits}">
            <li>${fruit}</li>
        </c:forEach>
    </ul>
</body>
</html>
```

- **मुख्य एलिमेंट्स**:
  - **डायरेक्टिव्स**: `<%@ page ... %>` पेज प्रॉपर्टीज सेट करती है; `<%@ taglib ... %>` टैग लाइब्रेरीज इम्पोर्ट करती है।
  - **स्क्रिप्टलेट्स**: Java कोड एम्बेड करें (कम इस्तेमाल करें; EL/JSTL को प्राथमिकता दें)।
  - **EL**: डेटा एक्सेस करने के लिए `${expression}` (बिना स्क्रिप्टलेट्स के)।
  - **JSTL**: [Apache Taglibs](https://tomcat.apache.org/taglibs/standard/) से डाउनलोड करें और JARs को `WEB-INF/lib` में रखें।

## 4. डिप्लॉय और रन करें
1. अपनी ऐप फोल्डर (जैसे, `my-jsp-app`) को Tomcat की `webapps` डायरेक्टरी में रखें।
2. Tomcat को रीस्टार्ट करें।
3. ब्राउज़र में एक्सेस करें: `http://localhost:8080/my-jsp-app/index.jsp`।
4. क्वेरी पैरामीटर के साथ टेस्ट करें: `http://localhost:8080/my-jsp-app/index.jsp?name=Grok` डायनामिक आउटपुट देखने के लिए।

## 5. कॉमन फीचर्स और बेस्ट प्रैक्टिसेज
- **फॉर्म और यूजर इनपुट**: सबमिशन हैंडल करने के लिए `<form>` टैग और `request.getParameter()` या EL (`${param.field}`) का उपयोग करें।
- **सेशन और बीन्स**: स्टेट मैनेजमेंट के लिए `session.setAttribute()` का उपयोग करें; रियूजेबल डेटा के लिए JavaBeans।
- **एरर हैंडलिंग**: `web.xml` में `<error-page>` जोड़ें या `<%@ page errorPage="error.jsp" %>` का उपयोग करें।
- **सिक्योरिटी**: XSS को रोकने के लिए इनपुट सैनिटाइज़ करें; प्रोडक्शन में HTTPS का उपयोग करें।
- **मॉडर्न अल्टरनेटिव्स**: JSP अभी भी इस्तेमाल होती है, लेकिन नए प्रोजेक्ट्स के लिए Thymeleaf या Spring MVC पर विचार करें क्योंकि वे ज़्यादा फ्लेक्सिबल हैं।
- **डीबगिंग**: एरर के लिए Tomcat लॉग (`logs/catalina.out`) चेक करें।

## 6. एडवांस्ड टॉपिक्स
- सर्वलेट्स के साथ इंटीग्रेट करें: व्यू के लिए JSP, लॉजिक के लिए सर्वलेट्स (MVC पैटर्न)।
- डेटाबेस कनेक्टिविटी: JDBC या JPA (जैसे, H2 या MySQL के साथ) का उपयोग करें।
- बिल्ड टूल्स: JSTL जैसी डिपेंडेंसी के लिए Maven/Gradle का उपयोग करें।

हैंड्स-ऑन प्रैक्टिस के लिए, एक सिंपल "Hello World" से शुरुआत करें और धीरे-धीरे फीचर्स जोड़ें। अगर आप एक फुल वेब ऐप बना रहे हैं, तो Jakarta EE ट्यूटोरियल एक्सप्लोर करें।

## संदर्भ
- [Oracle JSP Tutorial](https://docs.oracle.com/javaee/7/tutorial/jspx.htm)
- [Baeldung: Introduction to JSP](https://www.baeldung.com/jsp-tutorial)
- [Apache Tomcat JSP Examples](https://tomcat.apache.org/tomcat-10.1-doc/jsp-examples/)