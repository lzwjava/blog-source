---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: वेबस्फ़ीयर के लिए जेएमएस और जेएनडीआई एपीआई
translated: true
type: note
---

### जावा में JMS के लिए आवश्यक पैकेज और एपीआई

आपके द्वारा संदर्भित JMS कोड स्निपेट (आईबीएम वेबस्फीयर एप्लिकेशन सर्वर में JMS कनेक्शन फैक्ट्री को देखने और कनेक्ट करने के लिए) का उपयोग करने के लिए, आपको संबंधित जावा पैकेज आयात करने की आवश्यकता होगी। ये जावा EE/जकार्ता EE इकोसिस्टम से मानक एपीआई हैं:

- **JNDI (जावा नेमिंग एंड डायरेक्टरी इंटरफेस)**: `InitialContext` लुकअप के लिए।
  - पैकेज: `javax.naming` (या नए जकार्ता EE वर्जन में `jakarta.naming`)।
  - मुख्य क्लास: `InitialContext` – यह JNDI ऑपरेशन के लिए शुरुआती बिंदु है। यह संसाधनों (जैसे JMS फैक्ट्री या कतार) को उनके JNDI नाम (जैसे, `"jms/MyConnectionFactory"`) से देखने के लिए एक संदर्भ प्रदान करता है। WAS जैसे कंटेनर में, यह स्वचालित रूप से सर्वर की नेमिंग सर्विस से कनेक्ट हो जाता है।

- **JMS (जावा मैसेज सर्विस) एपीआई**: कनेक्शन, सत्र, प्रेषक/रिसीवर और संदेश बनाने के लिए।
  - पैकेज: `javax.jms` (JMS 1.1/2.0) या `jakarta.jms` (आधुनिक EE में जकार्ता JMS 3.0+)।
  - मुख्य इंटरफेस: `QueueConnectionFactory`, `QueueConnection`, `QueueSession`, `QueueSender`, `Queue`, `TextMessage`, आदि।

आपकी जावा क्लास के शीर्ष पर उदाहरण आयात:
```java
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueConnection;
import javax.jms.QueueSession;
import javax.jms.Queue;
import javax.jms.QueueSender;
import javax.jms.TextMessage;
import javax.jms.JMSException;
```

**`InitialContext` क्या है?**  
यह JNDI एपीआई में एक क्लास है जो एक नेमिंग सर्विस का प्रवेश बिंदु के रूप में कार्य करती है। आपके कोड में:  
```java
InitialContext ctx = new InitialContext();  // एक डिफ़ॉल्ट संदर्भ बनाता है जो ऐप सर्वर के JNDI वातावरण से बंधा होता है
QueueConnectionFactory qcf = (QueueConnectionFactory) ctx.lookup("jms/MyConnectionFactory");  // पूर्व-कॉन्फ़िगर फैक्ट्री को उसके JNDI नाम से देखता है
```  
WAS के *अंदर* चल रहे ऐप्स के लिए कंस्ट्रक्टर में किसी गुणों की आवश्यकता नहीं होती, क्योंकि कंटेनर वातावरण इंजेक्ट कर देता है (जैसे, `java.naming.factory.initial` के माध्यम से)। यदि WAS के *बाहर* एक स्टैंडअलोन क्लाइंट चला रहे हैं, तो आप प्रोवाइडर URL जैसे गुणों के साथ एक `Hashtable` पास करेंगे।

### मेवेन डिपेंडेंसीज़ (pom.xml)

यदि आपका जावा ऐप **WAS के अंदर डिप्लॉय और चल रहा है** (जैसे, एक वेब ऐप, EJB, या एंटरप्राइज बीन के रूप में):  
- **कोई अतिरिक्त डिपेंडेंसी आवश्यक नहीं**। WAS अपने जावा EE रनटाइम के हिस्से के रूप में JMS और JNDI एपीआई आउट-ऑफ-द-बॉक्स प्रदान करता है। बस उनके विरुद्ध कंपाइल करें (बिल्ड/डिप्लॉय के दौरान वे क्लासपाथ पर होते हैं)।  
- `pom.xml` में, आप उन्हें स्पष्ट रूप से `<scope>provided</scope>` के साथ डिक्लेयर कर सकते हैं ताकि आपके WAR/EAR में उन्हें बंडल होने से बचाया जा सके (इसे हल्का रखता है):  
  ```xml
  <dependencies>
      <dependency>
          <groupId>javax.jms</groupId>  <!-- या नए वर्जन के लिए jakarta.jms -->
          <artifactId>javax.jms-api</artifactId>
          <version>2.0.1</version>  <!-- JMS 2.0, WAS 8.5+ के साथ संगत -->
          <scope>provided</scope>
      </dependency>
      <dependency>
          <groupId>javax.naming</groupId>
          <artifactId>javax.naming-api</artifactId>
          <version>1.0</version>  <!-- JNDI 1.0, मानक -->
          <scope>provided</scope>
      </dependency>
  </dependencies>
  ```

यदि आपका ऐप एक **स्टैंडअलोन क्लाइंट** है (WAS के बाहर चल रहा है, जैसे, सर्वर से कनेक्ट होने वाला एक थिन क्लाइंट):  
- आपको IIOP पर पूर्ण JMS सपोर्ट के लिए **वेबस्फीयर एप्लिकेशन क्लाइंट** लाइब्रेरीज़ की आवश्यकता होगी। आईबीएम से "IBM WebSphere Application Server traditional" क्लाइंट पैकेज डाउनलोड करें, फिर उसे अपने क्लासपाथ में जोड़ें।  
- `pom.xml` में, शामिल करें:  
  ```xml
  <dependency>
      <groupId>com.ibm.ws</groupId>
      <artifactId>was-jms-client</artifactId>  <!-- अनुमानित; यदि उपलब्ध हो तो IBM के Maven रिपॉजिटरी का उपयोग करें -->
      <version>9.0.5</version>  <!-- अपने WAS वर्जन से मिलान करें -->
  </dependency>
  ```  
  या पूर्ण थिन क्लाइंट JARs (जैसे, `com.ibm.ws.orb_8.5.5.jar`, `com.ibm.ws.jndi_*.jar`) का उपयोग करें। सटीक सेटअप के लिए IBM डॉक्स चेक करें।

जकार्ता EE माइग्रेशन (2020 के बाद) के लिए, `jakarta.*` पैकेज पर स्विच करें, लेकिन WAS 9.x डिफ़ॉल्ट रूप से `javax.*` का उपयोग करता है—आवश्यकता होने पर फीचर पैक के माध्यम से जकार्ता सक्षम करें।

[IBM WebSphere JMS API Documentation](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-jms-api)  
[Java EE JNDI Tutorial](https://docs.oracle.com/javase/tutorial/jndi/)