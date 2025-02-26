---
audio: true
lang: hi
layout: post
title: WebSphere Liberty Profile में Deployment की समस्या निपटाएं
translated: true
---

जब आप अपने Spring Boot एप्लिकेशन को `http://localhost:9080/myapp/` पर एक्सेस करने की कोशिश करते हैं और WebSphere Liberty Profile (WLP) पर "context root not found" error मिलता है, तो यह इंगित करता है कि WLP ने आपका एप्लिकेशन अपेक्षित context root (`/myapp`) के तहत सफलतापूर्वक डिप्लॉय नहीं किया है। इस समस्या का आम तौर पर डिप्लॉयमेंट कॉन्फ़िगरेशन, सर्वर सेटअप या WAR फ़ाइल के साथ समस्याएं होती हैं। नीचे इस समस्या को ट्रबलशूट और सुलझाने के लिए एक व्यापक गाइड है।

---

### समस्या को समझना
"context root not found" error का मतलब है कि WLP `/myapp` पर डिप्लॉय किया गया एप्लिकेशन नहीं ढूंढ पा रहा है। आम तौर पर, जब आप `myapp.war` नामक एक WAR फ़ाइल को WLP के `dropins` डायरेक्टरी में रखते हैं, तो यह स्वचालित रूप से `/myapp` के साथ डिप्लॉय हो जाना चाहिए, जिससे यह `http://localhost:9080/myapp/` पर एक्सेस करने योग्य हो जाता है। क्योंकि यह हो नहीं रहा है, हमें पता लगाना होगा कि डिप्लॉयमेंट क्यों फेल हो गया।

---

### ट्रबलशूटिंग कदम

#### 1. **सर्वर लॉग्स में डिप्लॉयमेंट संदेशों की जांच करें**
पहला कदम यह सुनिश्चित करना है कि WLP ने आपका एप्लिकेशन डिप्लॉय किया है या नहीं।

- **लॉग्स को खोजें:**
  - अगर आपका सर्वर `myServer` नाम का है, तो लॉग्स को निम्न स्थान पर देखें:
    ```
    /opt/ibm/wlp/usr/servers/myServer/logs/messages.log
    ```
    या
    ```
    /opt/ibm/wlp/usr/servers/myServer/logs/console.log
    ```
  - अगर आप डिफ़ॉल्ट सर्वर का उपयोग कर रहे हैं, तो `myServer` को `defaultServer` से बदलें।

- **डिप्लॉयमेंट की पुष्टि के लिए देखें:**
  - आपको एक संदेश मिलना चाहिए जैसे:
    ```
    [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
    ```
    यह इंगित करता है कि एप्लिकेशन डिप्लॉय और उपलब्ध है।
  - इसके अलावा, देखें:
    ```
    CWWKZ0001I: Application myapp started in X.XXX seconds.
    ```
    यह पुष्टि करता है कि एप्लिकेशन सफलतापूर्वक शुरू हो गया है।

- **क्या करना है:**
  - अगर ये संदेश अनुपस्थित हैं, तो एप्लिकेशन डिप्लॉय नहीं हुआ है। लॉग्स में किसी भी `ERROR` या `WARNING` संदेशों को देखें जो क्यों हो सकता है (जैसे, मिसिंग फीचर्स, फ़ाइल अनुमतियाँ, या स्टार्टअप फेल्यर्स)।
  - अगर आप Spring Boot स्टार्टअप लॉग्स देखते हैं (जैसे, Spring Boot बैनर), तो एप्लिकेशन लोड हो रहा है और समस्या context root या URL मैपिंग के साथ हो सकती है।

#### 2. **WAR फ़ाइल की स्थिति और अनुमतियों की पुष्टि करें**
सुनिश्चित करें कि WAR फ़ाइल सही तरह से `dropins` डायरेक्टरी में रखा गया है और WLP द्वारा एक्सेस किया जा सकता है।

- **पथ की जांच करें:**
  - एक सर्वर `myServer` के लिए, WAR फ़ाइल को निम्न स्थान पर होना चाहिए:
    ```
    /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```
  - अगर `defaultServer` का उपयोग कर रहे हैं, तो अनुकूलित करें:
    ```
    /opt/ibm/wlp/usr/servers/defaultServer/dropins/myapp.war
    ```

- **अनुमतियों की पुष्टि करें:**
  - सुनिश्चित करें कि WLP प्रक्रिया को फ़ाइल पढ़ने की अनुमति है। एक Unix-like सिस्टम पर, चलाएं:
    ```bash
    ls -l /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```
    फ़ाइल को WLP द्वारा चलाए जाने वाले उपयोगकर्ता द्वारा पढ़ा जा सकता होना चाहिए (जैसे, `rw-r--r--`).

- **क्या करना है:**
  - अगर फ़ाइल गायब है या गलत जगह पर है, इसे सही `dropins` डायरेक्टरी में कॉपी करें:
    ```bash
    cp target/myapp.war /opt/ibm/wlp/usr/servers/myServer/dropins/
    ```
  - आवश्यकता के अनुसार अनुमतियाँ ठीक करें:
    ```bash
    chmod 644 /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```

#### 3. **`server.xml` में `dropins` मॉनिटरिंग की पुष्टि करें**
WLP का `dropins` डायरेक्टरी डिफ़ॉल्ट रूप से सक्रिय है, लेकिन कस्टम कॉन्फ़िगरेशन इसे निष्क्रिय कर सकते हैं।

- **`server.xml` की जांच करें:**
  - सर्वर कॉन्फ़िगरेशन फ़ाइल को खोलें:
    ```
    /opt/ibm/wlp/usr/servers/myServer/server.xml
    ```
  - `applicationMonitor` तत्व को देखें:
    ```xml
    <applicationMonitor updateTrigger="polled" pollingRate="5s" dropins="dropins" />
    ```
    यह पुष्टि करता है कि WLP `dropins` डायरेक्टरी को नए एप्लिकेशन के लिए हर 5 सेकंड में मॉनिटर करता है।

- **क्या करना है:**
  - अगर अनुपस्थित है, तो ऊपर दिए गए लाइन को `<server>` टैग के भीतर जोड़ें या सुनिश्चित करें कि कोई ओवरराइडिंग कॉन्फ़िगरेशन `dropins` को निष्क्रिय नहीं करता है।
  - बदलावों के बाद सर्वर को रीस्टार्ट करें:
    ```bash
    /opt/ibm/wlp/bin/server stop myServer
    /opt/ibm/wlp/bin/server start myServer
    ```

#### 4. **आवश्यक फीचर्स सक्रिय हों
WLP को एक Spring Boot WAR फ़ाइल डिप्लॉय करने के लिए विशेष फीचर्स की आवश्यकता होती हैं, जैसे Servlet समर्थन।

- **`server.xml` की जांच करें:**
  - `featureManager` सेक्शन में सुनिश्चित करें कि शामिल है:
    ```xml
    <featureManager>
        <feature>javaee-8.0</feature>
    </featureManager>
    ```
    `javaee-8.0` फीचर Servlet 4.0 को शामिल करता है, जो Spring Boot के साथ संगत है। वैकल्पिक रूप से, कम से कम `servlet-4.0` मौजूद होना चाहिए।

- **क्या करना है:**
  - अगर अनुपस्थित है, तो फीचर जोड़ें और सर्वर को रीस्टार्ट करें।

#### 5. **WAR फ़ाइल का संरचना की पुष्टि करें**
एक बिगड़ा हुआ या गलत ढंग से संरचित WAR फ़ाइल डिप्लॉयमेंट को रोक सकता है।

- **WAR को जांचें:**
  - WAR फ़ाइल को खोलें और इसकी सामग्री की जांच करें:
    ```bash
    unzip -l myapp.war
    ```
  - देखें:
    - `WEB-INF/classes/com/example/demo/HelloController.class` (आपका कंट्रोलर क्लास).
    - `WEB-INF/lib/` में Spring Boot निर्भरताएं (जैसे, `spring-web-x.x.x.jar`).

- **क्या करना है:**
  - अगर संरचना गलत है, तो WAR को फिर से बनाएं:
    ```bash
    mvn clean package
    ```
    सुनिश्चित करें कि आपका `pom.xml` में `<packaging>war</packaging>` सेट है और `spring-boot-starter-tomcat` को `<scope>provided</scope>` के रूप में चिह्नित किया गया है।

#### 6. **`apps` डायरेक्टरी के माध्यम से वैकल्पिक डिप्लॉयमेंट**
अगर `dropins` फेल हो जाता है, तो एप्लिकेशन को स्पष्ट रूप से `apps` डायरेक्टरी के माध्यम से डिप्लॉय करने की कोशिश करें।

- **कदम:**
  - WAR फ़ाइल को हटाएं:
    ```bash
    mv /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war /opt/ibm/wlp/usr/servers/myServer/apps/
    ```
  - `server.xml` को संपादित करें और जोड़ें:
    ```xml
    <application id="myapp" name="myapp" type="war" location="${server.config.dir}/apps/myapp.war">
        <context-root>/myapp</context-root>
    </application>
    ```
  - सर्वर को रीस्टार्ट करें:
    ```bash
    /opt/ibm/wlp/bin/server restart myServer
    ```

- **फिर से टेस्ट करें:**
  - `http://localhost:9080/myapp/` पर एक्सेस करें। अगर यह काम करता है, तो समस्या `dropins` के साथ थी।

#### 7. **सर्वर स्थिति की पुष्टि करें**
सुनिश्चित करें कि सर्वर सही तरह से चल रहा है।

- **स्थिति की जांच करें:**
  ```bash
  /opt/ibm/wlp/bin/server status myServer
  ```
  - अगर रोक दिया गया है, तो इसे शुरू करें:
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **WLP को खुद टेस्ट करें:**
  - `http://localhost:9080/` पर जाएं। अगर WLP चल रहा है, तो आप एक स्वागत पेज देखेंगे (अगर ओवरराइड नहीं किया गया है)। अगर यह फेल हो जाता है, तो एक व्यापक सर्वर समस्या है।

---

### समाधान
"context root not found" error को सुलझाने के लिए:

1. **यहाँ से शुरू करें:**
   - सर्वर लॉग्स (`messages.log` या `console.log`) में डिप्लॉयमेंट संदेशों या त्रुटियों की जांच करें।
   - सुनिश्चित करें कि `myapp.war` `dropins` डायरेक्टरी में है और सही अनुमतियाँ हैं।

2. **अगले कदम:**
   - सुनिश्चित करें कि `server.xml` `javaee-8.0` फीचर को सक्रिय करता है और `dropins` को मॉनिटर करता है।
   - अगर समस्या हल नहीं होती, तो `apps` डायरेक्टरी के माध्यम से एक स्पष्ट `<application>` कॉन्फ़िगरेशन के साथ डिप्लॉय करें।

3. **अंतिम पुष्टि:**
   - बदलावों के बाद WLP को रीस्टार्ट करें और `http://localhost:9080/myapp/` पर एक्सेस करें। अगर डिप्लॉयमेंट सफल होता है, तो आप "Hello World!" देखेंगे।

इन कदमों का पालन करके, आप यह पता लगाएंगे कि समस्या सर्वर कॉन्फ़िगरेशन, WAR प्लेसमेंट या WAR फ़ाइल के साथ है, और इसे अनुकूलित रूप से सुलझाएंगे।