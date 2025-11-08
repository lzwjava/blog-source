---
audio: false
generated: true
image: false
lang: hi
layout: post
model: anthropic/claude-4.5-sonnet
title: आईबीएम वेबस्फीयर रिक्वेस्ट राउटिंग एक्सप्लेंड
translated: true
type: note
---

मैं समझाता हूं कि IBM WebSphere Application Server (WAS) आने वाले अनुरोधों और रूटिंग को कैसे संभालता है:

## IBM WAS में अनुरोध प्रवाह

जब IBM WAS को एक अनुरोध आता है, तो यहां एक सामान्य प्रवाह होता है:

**1. वेब सर्वर लेयर (वैकल्पिक)**
- अनुरोध सबसे पहले IBM HTTP Server (IHS) या किसी अन्य वेब सर्वर से टकराता है
- वेब सर्वर प्लगइन उचित WAS इंस्टेंस पर रूट करता है

**2. वेब कंटेनर एंट्री पॉइंट**
अनुरोध WAS में **वेब कंटेनर** के माध्यम से प्रवेश करता है, जो मुख्य servlet इंजन का हिस्सा है। मुख्य पैकेज संरचना है:

```
com.ibm.ws.webcontainer.*
```

**3. अनुरोध प्रोसेसिंग चेन**

रूटिंग कई घटकों के माध्यम से होती है:

**ट्रांसपोर्ट चैनल फ्रेमवर्क**
- `com.ibm.ws.channel.*` - नेटवर्क संचार संभालता है
- HTTP ट्रांसपोर्ट चैनल अनुरोध प्राप्त करते हैं

**वेब कंटेनर प्रोसेसिंग**
```
com.ibm.ws.webcontainer.servlet.ServletWrapper
com.ibm.ws.webcontainer.filter.WebAppFilterManager
```

**4. फिल्टर चेन एक्सेक्यूशन**

फिल्टर बिल्कुल स्टैंडर्ड Java Servlet फिल्टर की तरह काम करते हैं लेकिन WAS द्वारा प्रबंधित किए जाते हैं:

- **web.xml में परिभाषित** आपके एप्लिकेशन के
- फिल्टर निर्दिष्ट क्रम में श्रृंखलाबद्ध होते हैं
- प्रत्येक फिल्टर अनुरोध और प्रतिक्रिया का निरीक्षण/संशोधन कर सकता है
- स्टैंडर्ड `javax.servlet.Filter` इंटरफेस का उपयोग करता है

```xml
<filter>
    <filter-name>MyFilter</filter-name>
    <filter-class>com.example.MyFilter</filter-class>
</filter>

<filter-mapping>
    <filter-name>MyFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

**फिल्टर एक्सेक्यूशन ऑर्डर:**
1. WAS एप्लिकेशन स्टार्टअप पर फिल्टर कॉन्फ़िगरेशन लोड करता है
2. WebAppFilterManager फिल्टर चेन बनाता है
3. प्रत्येक अनुरोध पर: Request → Filter1 → Filter2 → ... → Servlet

## IBM WAS में मुख्य पैकेज

**कोर पैकेज:**
- `com.ibm.ws.webcontainer.*` - वेब कंटेनर इम्प्लीमेंटेशन
- `com.ibm.ws.runtime.*` - रनटाइम सर्विसेज
- `com.ibm.websphere.servlet.*` - WAS-विशिष्ट servlet एक्सटेंशन
- `com.ibm.ws.channel.*` - ट्रांसपोर्ट लेयर
- `com.ibm.ejs.*` - EJB कंटेनर सर्विसेज
- `com.ibm.ws.naming.*` - JNDI इम्प्लीमेंटेशन

## रूटिंग मैकेनिज्म

**वर्चुअल होस्ट रूटिंग:**
- WAS एडमिन कंसोल में कॉन्फ़िगर किया गया
- `hostname:port` संयोजनों को एप्लिकेशन से मैप करता है
- कॉन्फ़िगरेशन: `VirtualHost → Host Aliases → Applications`

**कॉन्टेक्स्ट रूट रूटिंग:**
- प्रत्येक एप्लिकेशन का एक कॉन्टेक्स्ट रूट होता है (जैसे, `/myapp`)
- WAS तैनात एप्लिकेशन का एक रजिस्ट्री रखता है
- URI मैपिंग: `http://server:port/contextRoot/servletPath`

**Servlet मैपिंग:**
- web.xml या एनोटेशन में परिभाषित
- पैटर्न मिलान (सटीक, पथ, एक्सटेंशन, डिफ़ॉल्ट)

## एप्लिकेशन स्टार्टअप अनुक्रम

जब एप्लिकेशन शुरू होता है:
1. **ClassLoader इनिशियलाइज़ेशन** - ऐप को अपना क्लासलोडर मिलता है
2. **web.xml पार्सिंग** - फिल्टर, servlets, listeners लोड होते हैं
3. **ServletContextListeners फायर** - `contextInitialized()`
4. **फिल्टर इंस्टेंटिएटेड** - `init()` मेथड कॉल की गई
5. **लोड-ऑन-स्टार्टअप servlets** - ईगर servlets को इनिशियलाइज़ करें
6. **एप्लिकेशन चिह्नित STARTED** - अनुरोधों को स्वीकार करने के लिए तैयार

रूटिंग रजिस्ट्री अपडेट की जाती है, और एप्लिकेशन अब अपने कॉन्टेक्स्ट रूट पर उपलब्ध है।

क्या यह स्पष्ट करता है कि WAS अनुरोध रूटिंग और फिल्टरिंग को कैसे संभालता है?