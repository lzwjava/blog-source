---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: आईबीएम एमक्यू वेबस्फीयर एप्लिकेशन सर्वर कॉन्फ़िगरेशन
translated: true
type: note
---

### पूर्वापेक्षाएँ
IBM WebSphere Application Server (WAS) में IBM MQ (पूर्व में WebSphere MQ) कॉन्फ़िगर करने से पहले, निम्नलिखित सुनिश्चित करें:
- IBM MQ एक समर्पित सर्वर पर इंस्टॉल है (या फिर WAS के साथ ही स्थानीय बाइंडिंग्स मोड के लिए)।
- IBM MQ में एक क्यू मैनेजर बनाया गया है (उदाहरण के लिए, `crtmqm QMNAME` का उपयोग करके)।
- क्यू मैनेजर में आवश्यक क्यू बनाए गए हैं (उदाहरण के लिए, MQ Explorer या `runmqsc` का उपयोग करके)।
- IBM MQ क्लाइंट लाइब्रेरीज़ (JAR फ़ाइलें जैसे `com.ibm.mq.allclient.jar`, `com.ibm.mqjms.jar`) उपलब्ध हैं। यदि WAS, MQ से रिमोट है, तो WAS मशीन पर IBM MQ क्लाइंट इंस्टॉल करें।
- अनुमतियों के लिए WAS प्रक्रिया उपयोगकर्ता को `mqm` समूह में जोड़ें।
- Unix-like सिस्टम पर गैर-रूट उपयोगकर्ताओं के लिए, अनुमतियाँ देने के लिए `setmqaut` का उपयोग करें।

### चरण-दर-चरण कॉन्फ़िगरेशन
कॉन्फ़िगरेशन में WAS एडमिनिस्ट्रेटिव कंसोल में JMS प्रोवाइडर, कनेक्शन फैक्ट्रीज़, और डेस्टिनेशन सेट अप करना शामिल है। यह TCP/IP पर वितरित (क्लाइंट) मोड कनेक्शन मानता है; यदि स्थानीय है तो बाइंडिंग्स मोड के लिए समायोजित करें।

1. **WAS एडमिनिस्ट्रेटिव कंसोल तक पहुँचें**:
   - WAS सर्वर शुरू करें।
   - एक ब्राउज़र खोलें और `https://localhost:9043/ibm/console` पर नेविगेट करें (अपने होस्ट/पोर्ट से बदलें)।
   - एडमिन क्रेडेंशियल्स के साथ लॉग इन करें।

2. **IBM MQ JMS प्रोवाइडर कॉन्फ़िगर करें**:
   - **Resources > JMS > Providers** पर जाएँ।
   - **New** पर क्लिक करें।
   - **WebSphere MQ messaging provider** चुनें।
   - विवरण भरें:
     - **Name**: उदाहरण के लिए, `MQProvider`।
     - **Description**: वैकल्पिक।
     - **Class path**: MQ JAR फ़ाइलों का पथ (उदाहरण के लिए, `/opt/mqm/java/lib/*` या `<WAS_HOME>/lib/ext` में कॉपी करें)।
     - **Native library path**: बाइंडिंग्स मोड के लिए आवश्यक (MQ लाइब्रेरीज़ का पथ, उदाहरण के लिए, `/opt/mqm/lib64`)।
     - **External initial context factory name**: `com.ibm.mq.jms.context.WMQInitialContextFactory` (क्लाइंट मोड के लिए)।
     - **External context provider URL**: उदाहरण के लिए, `host:1414/CHANNEL` (host = MQ सर्वर IP, 1414 = डिफ़ॉल्ट पोर्ट, CHANNEL = उदाहरण के लिए, `SYSTEM.DEF.SVRCONN`)।
   - कॉन्फ़िगरेशन सहेजें।

3. **एक क्यू कनेक्शन फैक्ट्री बनाएँ**:
   - **Resources > JMS > Queue connection factories** पर जाएँ (अपने सर्वर या सेल के स्कोप में)।
   - **New** पर क्लिक करें।
   - चरण 2 में बनाए गए प्रोवाइडर को चुनें।
   - भरें:
     - **Name**: उदाहरण के लिए, `MQQueueCF`।
     - **JNDI name**: उदाहरण के लिए, `jms/MQQueueCF`।
     - **Queue manager**: आपका MQ क्यू मैनेजर नाम (उदाहरण के लिए, `QM1`)।
     - **Host**: MQ सर्वर होस्टनाम या IP।
     - **Port**: 1414 (डिफ़ॉल्ट)।
     - **Channel**: उदाहरण के लिए, `SYSTEM.DEF.SVRCONN`।
     - **Transport type**: `CLIENT` (TCP/IP के लिए) या `BINDINGS` (स्थानीय)।
     - **Security credentials**: आवश्यकता होने पर User ID और पासवर्ड।
   - वैकल्पिक उन्नत गुण: कनेक्शन पूल आकार सेट करें (उदाहरण के लिए, आपके लोड के आधार पर अधिकतम कनेक्शन)।
   - सहेजें।

4. **क्यू डेस्टिनेशन बनाएँ**:
   - **Resources > JMS > Queues** पर जाएँ।
   - **New** पर क्लिक करें।
   - प्रोवाइडर चुनें।
   - प्रत्येक क्यू के लिए:
     - **Name**: उदाहरण के लिए, `MyQueue`।
     - **JNDI name**: उदाहरण के लिए, `jms/MyQueue`।
     - **Queue name**: MQ में सटीक क्यू नाम (उदाहरण के लिए, `MY.LOCAL.QUEUE`)।
     - **Queue manager**: ऊपर के समान।
     - **Target client type**: `MQ` या `JMS`।
   - सहेजें। पब/सब का उपयोग करने पर टॉपिक्स के लिए दोहराएँ।

5. **(वैकल्पिक) बाइंडिंग्स मोड के लिए WebSphere MQ Server कॉन्फ़िगर करें**:
   - यदि स्थानीय बाइंडिंग्स का उपयोग कर रहे हैं, तो **Servers > Server Types > WebSphere MQ servers** पर जाएँ।
   - **New** पर क्लिक करें।
   - **Name**, **Queue manager name** सेट करें।
   - **MQ installations** निर्दिष्ट करें (MQ इंस्टॉल का पथ)।
   - सर्वर को सहेजें और पुनरारंभ करें।

6. **JCA रिसोर्स एडाप्टर कॉन्फ़िगर करें (MDBs के लिए)**:
   - **Resources > Resource Adapters > J2C connection factories** पर जाएँ।
   - यदि बिल्ट-इन MQ RA का उपयोग कर रहे हैं, तो सुनिश्चित करें कि वह डिप्लॉय है (WAS में `wmq.jmsra.rar` शामिल है)।
   - गुण सेट करें जैसे अधिकतम कनेक्शन (उदाहरण के लिए, लोड के आधार पर 10-50)।

7. **कॉन्फ़िगरेशन टेस्ट करें**:
   - एक सैंपल JMS एप्लिकेशन डिप्लॉय करें या WAS JMS सैंपल का उपयोग करें।
   - त्रुटियों के लिए लॉग्स जांचें (उदाहरण के लिए, पोर्ट 1414 पर कनेक्शन रिफ्यूज़्ड)।
   - MQ में सत्यापित करें: क्यू डेप्थ और चैनल्स की निगरानी के लिए MQ Explorer का उपयोग करें।

8. **सुरक्षा और उन्नत सेटअप**:
   - SSL सक्षम करें: WAS और MQ में कीस्टोर्स कॉन्फ़िगर करें (चैनल `SSLCIPH` के साथ)।
   - प्रमाणीकरण सेट करें: MQ उपयोगकर्ता समूह या वैकल्पिक उपयोगकर्ता ID का उपयोग करें।
   - क्लस्टर्स के लिए: नोड्स में कॉन्फ़िगरेशन सिंक्रनाइज़ करें।

### समस्या निवारण सुझाव
- **ClassNotFoundException**: सुनिश्चित करें कि MQ JARs क्लासपाथ में हैं।
- **कनेक्शन विफलताएँ**: पोर्ट 1414 पर फ़ायरवॉल, चैनल स्थिति जांचें (`runmqsc` में `DISPLAY CHSTATUS(*)`)।
- **बाइंडिंग्स मोड समस्याएँ**: नेटिव लाइब्स और `mqm` समूह में उपयोगकर्ता सत्यापित करें।
   - परिवर्तनों के बाद WAS को पुनरारंभ करें।

वर्शन-विशिष्ट विवरणों के लिए (उदाहरण के लिए, WAS 9.x with MQ 9.x), आधिकारिक IBM डॉक्स देखें।

[Using WebSphere Application Server with IBM MQ](https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=together-using-websphere-application-server-mq)  
[Configuring WebSphere Application Server for use with IBM MQ](https://help.hcl-software.com/commerce/9.0.0/integration/tasks/tcvconfigure_was_for_mq.html)  
[Creating a WebSphere MQ server definition](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.multiplatform.doc/ae/tjfp0004_.html)