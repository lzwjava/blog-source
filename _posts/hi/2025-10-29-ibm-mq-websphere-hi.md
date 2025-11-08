---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: वेबस्फ़ेयर में आईबीएम एमक्यू कॉन्फ़िगर करना
translated: true
type: note
---

### आईबीएम वेबस्फीयर एप्लिकेशन सर्वर में मैसेज कतारों को कॉन्फ़िगर करना (आईबीएम एमक्यू को प्रदाता के रूप में उपयोग करके)

आईबीएम वेबस्फीयर एप्लिकेशन सर्वर (WAS) आईबीएम एमक्यू (पूर्व में वेबस्फीयर एमक्यू) के साथ Java Message Service (JMS) एकीकरण के माध्यम से मैसेज कतारिंग का समर्थन करता है। कॉन्फ़िगरेशन आमतौर पर **वेबस्फीयर इंटीग्रेटेड सॉल्यूशंस कंसोल** (प्रशासनिक इंटरफेस) के माध्यम से किया जाता है, जो `https://your-server:9043/ibm/console` (डिफ़ॉल्ट सुरक्षित पोर्ट; आवश्यकतानुसार समायोजित करें) पर एक्सेस होता है। यह गाइड पारंपरिक फुल-प्रोफाइल WAS (जैसे, संस्करण 9.0+) पर केंद्रित है, लेकिन वेबस्फीयर लिबर्टी के लिए चरण मामूली समायोजन के साथ समान हैं।

#### पूर्वापेक्षाएँ
- आईबीएम एमक्यू इंस्टॉल, चल रहा और एक्सेस करने योग्य होना चाहिए (जैसे, क्यू मैनेजर शुरू)।
- WAS सर्वर शुरू हो गया है, और आपके पास कंसोल तक व्यवस्थापक पहुंच है।
- आईबीएम एमक्यू JMS क्लाइंट लाइब्रेरीज़ (जैसे, `com.ibm.mq.allclient.jar`) को WAS की साझा लाइब्रेरीज़ में डाउनलोड और इंस्टॉल करें यदि पहले से मौजूद नहीं हैं (**Environment > Shared Libraries** के अंतर्गत)।
- सुनिश्चित करें कि वेबस्फीयर एमक्यू मैसेजिंग प्रदाता कॉन्फ़िगर है (**Resources > JMS > JMS providers** के अंतर्गत)। यदि नहीं है, तो होस्ट, पोर्ट (डिफ़ॉल्ट 1414), और क्यू मैनेजर नाम जैसे विवरणों के साथ एक बनाएँ।

कॉन्फ़िगरेशन के बाद, परिवर्तनों को सहेजें (शीर्ष पर **Save** बटन) और उन्हें प्रभावी होने के लिए एप्लिकेशन सर्वर को पुनरारंभ करें।

#### चरण 1: एक JMS क्यू कनेक्शन फैक्टरी बनाएँ
कनेक्शन फैक्टरी आईबीएम एमक्यू क्यू मैनेजर से कनेक्शन स्थापित करती है।

1. WAS एडमिन कंसोल में लॉग इन करें।
2. नेविगेशन पेन में, **Resources > JMS > Queue connection factories** का विस्तार करें।
3. ड्रॉपडाउन से उपयुक्त **Scope** (जैसे, Cell, Node, Server) चुनें और **Apply** पर क्लिक करें।
4. **New** पर क्लिक करें।
5. **WebSphere MQ messaging provider** चुनें और **OK** पर क्लिक करें।
6. अगली स्क्रीन पर:
   - **Name**: एक वर्णनात्मक नाम दर्ज करें (जैसे, `MyMQQueueConnectionFactory`)।
   - **JNDI name**: एक JNDI बाइंडिंग दर्ज करें (जैसे, `jms/MyQueueConnectionFactory`)।
   - **Next** पर क्लिक करें।
7. कनेक्शन विवरण दर्ज करें:
   - **Queue manager**: आपके आईबीएम एमक्यू क्यू मैनेजर का नाम (जैसे, `QM1`)।
   - **Host name**: आईबीएम एमक्यू सर्वर होस्टनाम या आईपी।
   - **Port**: लिसनर पोर्ट (डिफ़ॉल्ट: 1414)।
   - **Transport type**: CHANNEL (क्लाइंट मोड के लिए) या BINDINGS (एम्बेडेड के लिए)।
   - **Channel**: डिफ़ॉल्ट चैनल नाम (जैसे, `SYSTEM.DEF.SVRCONN`)।
   - **User ID** और **Password**: एमक्यू प्रमाणीकरण के लिए क्रेडेंशियल्स (यदि आवश्यक हो)।
   - **Next** पर क्लिक करें।
8. सारांश की समीक्षा करें और **Finish** पर क्लिक करें।
9. नई फैक्टरी को चुनें, **Additional Properties > Connection pool** (वैकल्पिक) पर जाएँ, और **Maximum connections** (जैसे, अपेक्षित लोड के आधार पर) जैसी सेटिंग्स को ट्यून करें।
10. सत्यापित करने के लिए **Test connection** पर क्लिक करें।

#### चरण 2: एक JMS क्यू डेस्टिनेशन बनाएँ
यह संदेश भेजने/प्राप्त करने के लिए वास्तविक क्यू एंडपॉइंट को परिभाषित करता है।

1. नेविगेशन पेन में, **Resources > JMS > Queues** का विस्तार करें।
2. उपयुक्त **Scope** (कनेक्शन फैक्टरी से मेल खाता हुआ) चुनें और **Apply** पर क्लिक करें।
3. **New** पर क्लिक करें।
4. **WebSphere MQ messaging provider** चुनें और **OK** पर क्लिक करें।
5. गुण निर्दिष्ट करें:
   - **Name**: वर्णनात्मक नाम (जैसे, `MyRequestQueue`)।
   - **JNDI name**: JNDI बाइंडिंग (जैसे, `jms/MyRequestQueue`)।
   - **Base queue name**: आईबीएम एमक्यू में सटीक क्यू नाम (जैसे, `REQUEST.QUEUE`; एमक्यू में मौजूद होना चाहिए या बनाया जाना चाहिए)।
   - **Target client**: JMS (JMS ऐप्स के लिए) या MQ (नेटिव एमक्यू ऐप्स के लिए)।
   - **Target destination mode**: Once only (विश्वसनीयता के लिए डिफ़ॉल्ट)।
   - **OK** पर क्लिक करें।
6. (वैकल्पिक) **Additional Properties** के अंतर्गत, Persistence, expiry, या priority सेटिंग्स कॉन्फ़िगर करें।
7. कॉन्फ़िगरेशन सहेजें।

#### चरण 3: (वैकल्पिक) मैसेज-ड्रिवन बीन्स (MDBs) के लिए एक एक्टिवेशन स्पेसिफिकेशन बनाएँ
यदि संदेशों को अतुल्यकालिक रूप से उपभोग करने के लिए MDBs का उपयोग कर रहे हैं:

1. नेविगेशन पेन में, **Resources > JMS > Activation specifications** का विस्तार करें।
2. **Scope** चुनें और **New** पर क्लिक करें।
3. **WebSphere MQ messaging provider** चुनें और **OK** पर क्लिक करें।
4. दर्ज करें:
   - **Name**: जैसे, `MyQueueActivationSpec`।
   - **JNDI name**: जैसे, `jms/MyQueueActivation`।
   - **Destination type**: Queue।
   - **Destination JNDI name**: आपकी क्यू की JNDI (जैसे, `jms/MyRequestQueue`)।
   - **Connection factory JNDI name**: आपकी कनेक्शन फैक्टरी की JNDI (जैसे, `jms/MyQueueConnectionFactory`)।
   - Message selector (वैकल्पिक): संदेशों को फ़िल्टर करने के लिए JMS सेलेक्टर।
5. **Additional Properties > Message Listener Service > Listener Ports** के अंतर्गत, यदि आवश्यक हो तो एक पोर्ट बनाएँ:
   - **Name**: जैसे, `MyListenerPort`।
   - **Connection factory JNDI**: ऊपर के अनुसार।
   - **Destination JNDI**: ऊपर के अनुसार।
   - **Component**: आपके MDB का deployment descriptor।
6. **OK** पर क्लिक करें और सहेजें।

#### चरण 4: सत्यापित करें और परीक्षण करें
- **कंसोल में परीक्षण**: फैक्टरियों और स्पेस पर **Test connection** का उपयोग करें।
- **एक ऐप डिप्लॉय करें**: एक सरल JMS क्लाइंट या MDB ऐप बनाएँ, इसे डिप्लॉय करें, और आईबीएम एमक्यू टूल्स (जैसे, MQ Explorer) के माध्यम से संदेश भेजें/परीक्षण करें।
- **मॉनिटरिंग**: **Monitoring and Tuning > Performance Viewer** या **Troubleshooting > Logs** के अंतर्गत, JMS-संबंधित त्रुटियों की जाँच करें।
- सामान्य समस्याएँ:
  - कनेक्शन विफलताएँ: फ़ायरवॉल, एमक्यू चैनल स्थिति (`DISPLAY CHANNEL`), और क्रेडेंशियल्स सत्यापित करें।
  - JNDI लुकअप त्रुटियाँ: सुनिश्चित करें कि बाइंडिंग सही हैं और ऐप सही स्कोप का उपयोग करता है।
  - Persistence: WAS और MQ के बीच स्थायित्व सेटिंग्स को संरेखित करें।

कमांड-लाइन विकल्पों (wsadmin स्क्रिप्टिंग) के लिए, आईबीएम डॉक्स देखें। अपने संस्करण के आधार पर ट्यून करें (जैसे, WAS 9.0.5+ JMS 2.0 का समर्थन करता है)।

#### संदर्भ
- [Configuring JMS resources in WebSphere Application Server](https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=resources-configuring-jms-in-websphere-application-server)
- [WebSphere MQ messaging provider queue settings](https://www.ibm.com/docs/en/was/8.5.5?topic=settings-websphere-mq-messaging-provider-queue)
- [Creating a WebSphere MQ messaging provider queue connection factory](https://help.hcl-software.com/commerce/7.0.0/com.ibm.commerce.integration.doc/tasks/tcvjmsqueuefactory.html)
- [Configure a JMS queue destination for WebSphere MQ](http://www.setgetweb.com/p/i5/portal/WAS60/Configure_JMS_queue_destinationfor_WebSphere_MQ.html)