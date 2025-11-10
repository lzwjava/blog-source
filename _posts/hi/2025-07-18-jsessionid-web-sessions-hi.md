---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast:free
title: जेसेशनआईडी और वेब सत्रों को समझना
translated: true
type: note
---

### वेब एप्लिकेशन में सत्र क्या होते हैं?

सत्र वेब एप्लिकेशन को HTTP अनुरोधों के बीच स्थिति (state) बनाए रखने की अनुमति देते हैं, जो स्वभाव से ही स्टेटलेस (stateless) होते हैं। Java servlets और Spring में, सत्र उपयोगकर्ता-विशिष्ट डेटा (जैसे लॉगिन स्थिति या शॉपिंग कार्ट आइटम) को सर्वर-साइड पर संग्रहीत करते हैं, जो एक अद्वितीय पहचानकर्ता के माध्यम से क्लाइंट से जुड़ा होता है, जिसे कुकी या URL पैरामीटर के रूप में भेजा जाता है।

JSESSIONID, Java EE कंटेनरों (जैसे, Tomcat, Jetty) और servlets पर बने Spring एप्लिकेशन द्वारा उपयोग किए जाने वाले सत्र पहचानकर्ता कुकी का मानक नाम है।

### JSESSIONID कैसे काम करता है

1. **सत्र निर्माण**:
   - जब कोई उपयोगकर्ता पहली बार किसी वेब ऐप तक पहुंचता है, तो servlet कंटेनर (या Spring `HttpSession` के माध्यम से) सर्वर पर एक नया `HttpSession` ऑब्जेक्ट बनाता है।
   - यह एक अद्वितीय ID (जैसे, "A1B2C3D4E5F6") को सत्र ID के रूप में निर्दिष्ट करता है।
   - यह ID एक `Set-Cookie` हेडर के माध्यम से क्लाइंट को भेजी जाती है: `JSESSIONID=A1B2C3D4E5F6; Path=/; HttpOnly`.

2. **क्लाइंट-सर्वर इंटरैक्शन**:
   - बाद के अनुरोधों पर, क्लाइंट `Cookie` हेडर में `JSESSIONID` शामिल करता है (यदि कुकीज़ का उपयोग कर रहा है) या इसे URLs में जोड़ता है (जैसे, URL रीराइटिंग के लिए `/app/page;jsessionid=A1B2C3D4E5F6`, हालांकि अब यह कम आम है)।
   - कंटेनर इस ID का उपयोग मेमोरी या स्टोरेज (जैसे डेटाबेस या Redis, यदि कॉन्फ़िगर किया गया हो) से मेल खाने वाले `HttpSession` को पुनः प्राप्त करने के लिए करता है।
   - डेटा अनुरोधों के बीच बना रहता है, और उस सत्र के लिए स्कोप किया जाता है।

3. **समाप्ति और सफाई**:
   - निष्क्रियता के बाद सत्र समाप्त हो जाते हैं (Tomcat में डिफ़ॉल्ट ~30 मिनट, `web.xml` या Spring के `server.servlet.session.timeout` के माध्यम से कॉन्फ़िगर करने योग्य)।
   - टाइमआउट पर, सत्र अमान्य कर दिया जाता है, और ID बेकार हो जाती है।
   - `HttpOnly` फ्लैग JavaScript एक्सेस को रोकता है, जिससे सुरक्षा बढ़ती है; HTTPS के लिए `Secure` जोड़ा जा सकता है।

सत्र डिफ़ॉल्ट रूप से मेमोरी में संग्रहीत होते हैं (जैसे, Tomcat का `StandardManager`), लेकिन स्केलेबिलिटी के लिए इन्हें `PersistentManager` या बाहरी स्टोर का उपयोग करके संग्रहीत किया जा सकता है।

### Java Servlets में सत्र प्रबंधन

सादे servlets में (जैसे, javax.servlet):

- **सत्र प्राप्त करना**:
  ```java
  HttpServletRequest request = // from doGet/doPost
  HttpSession session = request.getSession(); // Creates if none exists
  HttpSession session = request.getSession(false); // Retrieves existing or returns null
  ```

- **डेटा संग्रहीत/पुनः प्राप्त करना**:
  ```java
  session.setAttribute("username", "exampleUser");
  String user = (String) session.getAttribute("username");
  ```

- **अमान्य करना**:
  ```java
  session.invalidate();
  ```

`web.xml` में टाइमआउट कॉन्फ़िगर करें:
```xml
<session-config>
    <session-timeout>30</session-timeout> <!-- in minutes -->
</session-config>
```

### Spring Framework में सत्र प्रबंधन

Spring, servlet सत्रों पर बनता है लेकिन अमूर्तता (abstractions) प्रदान करता है:

- **HttpSession को सीधे उपयोग करना**:
  Servlets के समान; controllers में इसे इंजेक्ट करें:
  ```java
  @Controller
  public class MyController {
      @RequestMapping("/login")
      public String login(HttpSession session) {
          session.setAttribute("user", "example");
          return "redirect:/dashboard";
      }
  }
  ```

- **Spring Security एकीकरण**:
  यदि Spring Security का उपयोग कर रहे हैं, तो सत्र प्रमाणीकरण का प्रबंधन करते हैं। `application.properties` में कॉन्फ़िगर करें:
  ```
  server.servlet.session.timeout=30m
  ```

- **वितरित सत्र**:
  वितरित सेटअप के लिए, Redis या JDBC के साथ Spring Session का उपयोग करें:
  - निर्भरता जोड़ें: `spring-session-data-redis`.
  - `@Configuration` क्लास में कॉन्फ़िगर करें:
    ```java
    @EnableRedisHttpSession
    public class SessionConfig { }
    ```
  यह सर्वरों के बीच सत्रों को स्केलेबल बनाता है, और JSESSIONID लिंकेज को Redis में संग्रहीत करता है।

### सर्वोत्तम अभ्यास और सुरक्षा

- **सुरक्षा**: हमेशा `HttpOnly` और `Secure` कुकीज़ का उपयोग करें। संवेदनशील डेटा को सत्रों में संग्रहीत करने से बचें; सर्वर-साइड एन्क्रिप्शन का उपयोग करें।
- **टाइमआउट**: मेमोरी उपयोग को कम करने के लिए उचित टाइमआउट सेट करें।
- **स्केलेबिलिटी**: लोड-बैलेंस्ड ऐप्स के लिए, सत्र हानि को रोकने के लिए स्टिकी सत्र (जैसे, AWS ELB के माध्यम से) या साझा स्टोर (जैसे Redis) का उपयोग करें।
- **परीक्षण**: JSESSIONID कुकीज़ का निरीक्षण करने या अनुरोधों का सिमुलेशन करने के लिए Postman जैसे टूल्स का उपयोग करें।
- **विकल्प**: REST APIs के लिए, स्टेटफुलनेस से बचने के लिए सर्वर-साइड सत्रों के बजाय JWTs पर विचार करें।

यह तंत्र Java EE specification में मानकीकृत है; विवरण के लिए, Oracle Java EE डॉक्स या Spring Boot रेफरेंस देखें। यदि आपका ऐप किसी कंटेनर में है, तो विशिष्ट व्यवहारों (जैसे, Tomcat का सत्र प्रबंधन) के लिए उसके डॉक्स देखें।