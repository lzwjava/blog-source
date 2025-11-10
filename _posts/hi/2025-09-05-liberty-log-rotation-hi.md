---
audio: false
generated: true
image: false
lang: hi
layout: post
title: लिबर्टी लॉग रोटेशन कॉन्फ़िगरेशन गाइड
translated: true
type: note
---

यहाँ संक्षिप्त संस्करण है, और उसके बाद उदाहरण हैं जिन्हें आप `server.xml` में पेस्ट कर सकते हैं।

### Liberty लॉग रोटेशन कैसे काम करता है

* **क्या रोटेट होता है:** `messages.log` और `trace.log`।
  रोटेशन **साइज़-आधारित** और/या **टाइम-आधारित** हो सकता है। ([openliberty.io][1])
* **क्या रोटेट नहीं होता है:** `console.log` (यह सिर्फ stdout/stderr है)। आप इसे कम या बंद कर सकते हैं। ([openliberty.io][2], [IBM][3])
* **कहाँ कॉन्फ़िगर करें:** `server.xml` में `<logging …/>` एलिमेंट। (आप समान वैल्यूज़ `bootstrap.properties`/env vars में भी सेट कर सकते हैं अगर आपको `server.xml` लोड होने से *पहले* उनके एप्लाई होने की ज़रूरत है।) ([openliberty.io][2])
* **एक्सेस लॉग:** HTTP एक्सेस लॉग के अपने **अलग** टाइम-आधारित रोलओवर सेटिंग्स हैं, जो `httpAccessLogging` / `accessLogging` के अंदर होते हैं। ([openliberty.io][4])
* **साइज़ + टाइम दोनों:** मॉडर्न Liberty, क्लासिक साइज़-आधारित ऑप्शन के अलावा टाइम-आधारित रोलओवर को सपोर्ट करता है, इसलिए आप कोई एक या दोनों इस्तेमाल कर सकते हैं (`console.log` को छोड़कर)। ([IBM][5])

---

### आम `server.xml` रेसिपीज़

#### 1) साइज़-आधारित रोटेशन (क्लासिक)

अधिकतम 10 फाइलें रखता है, प्रत्येक अधिकतम 256 MB की।

```xml
<logging
  logDirectory="${server.output.dir}/logs"
  maxFileSize="256"
  maxFiles="10"/>
```

प्रभाव: जब `messages.log` या `trace.log` 256 MB से अधिक हो जाता है, Liberty इसे एक टाइमस्टैम्प वाली फाइल में रोल कर देता है और ऐसी अधिकतम 10 फाइलें रखता है। (`console.log` को प्रभावित नहीं करता।) ([openliberty.io][1])

#### 2) टाइम-आधारित रोटेशन (उदाहरण के लिए, रोज़ाना मध्यरात्रि पर)

```xml
<logging
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>
```

प्रभाव: `messages.log` और `trace.log` हर दिन 00:00 पर रोल ओवर होते हैं। आप मिनट (`m`) या घंटे (`h`) भी इस्तेमाल कर सकते हैं, जैसे, `30m` या `6h`। ([openliberty.io][2])

#### 3) साइज़ + टाइम को कम्बाइन करें (टिपिकल प्रोडक्शन)

```xml
<logging
  logDirectory="${server.output.dir}/logs"
  maxFileSize="256"
  maxFiles="14"
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>
```

प्रभाव: रोल ओवर **जो भी पहले आए** (साइज़ या शेड्यूल), और 14-फाइल का हिस्ट्री रखें। ([IBM][5])

#### 4) `console.log` की ग्रोथ को कंट्रोल या डिसेबल करें

`console.log` रोटेट नहीं हो सकता; इसे कम करें या बंद कर दें और `messages.log` पर भरोसा करें।

```xml
<logging
  consoleLogLevel="OFF"
  copySystemStreams="false"/>
```

नोट्स: कंसोल को ऑफ करने से Liberty की अपनी लॉग कॉपी `console.log` में जाना बंद हो जाती है, लेकिन JVM अभी भी stdout/stderr में `-verbose:gc` जैसी चीज़ें लिख सकता है। ([openliberty.io][2])

#### 5) नाम/फॉर्मेट ट्वीक्स (ऑप्शनल)

```xml
<logging
  messageFileName="messages.log"
  traceFileName="trace.log"
  messageFormat="JSON"/>
```

JSON लॉग स्टैक को शिप करने के लिए अच्छा है; अगर आपको इसकी ज़रूरत नहीं है तो डिफॉल्ट छोड़ दें। ([openliberty.io][1])

---

### HTTP एक्सेस लॉग (ऊपर वाले से अलग)

एक्सेस लॉगिंग को एनेबल करें और इसे रोज़ाना मध्यरात्रि पर रोल करें:

```xml
<httpAccessLogging id="accessLogging"
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>

<httpEndpoint id="defaultHttpEndpoint"
  httpPort="9080" httpsPort="9443"
  accessLoggingRef="accessLogging"/>
```

(या `rolloverStartTime`/`rolloverInterval` को सीधे `httpEndpoint` के `<accessLogging …/>` चाइल्ड पर डालें।) ([openliberty.io][4])

---

### क्विक चेकलिस्ट

* साइज़-आधारित रोलओवर के लिए **`maxFileSize` + `maxFiles`** इस्तेमाल करें। ([openliberty.io][1])
* टाइम-आधारित रोलओवर के लिए **`rolloverStartTime` + `rolloverInterval`** इस्तेमाल करें। ([openliberty.io][2])
* **`console.log` के रोटेट होने की उम्मीद न करें**; अगर आप बड़ी कंसोल फाइलों से बचना चाहते हैं तो `consoleLogLevel="OFF"` और `copySystemStreams="false"` सेट करें। ([openliberty.io][2], [IBM][3])

अगर आप अपना करंट `server.xml` स्निपेट या अपने रिटेंशन गोल्स शेयर करते हैं (जैसे, "~7 दिन रखें" या "2 GB पर कैप करें"), तो मैं एकदम सही वैल्यूज़ तैयार कर दूंगा।

[1]: https://openliberty.io/docs/latest/reference/config/logging.html "Logging (logging) :: Open Liberty Docs"
[2]: https://openliberty.io/docs/latest/log-trace-configuration.html "Log and trace configuration :: Open Liberty Docs"
[3]: https://www.ibm.com/support/pages/how-turn-console-logging-prevent-excess-file-growth-and-use-only-message-log-rotation-liberty-profile-or-open-liberty?utm_source=chatgpt.com "How to turn off Console logging, prevent excess file growth ..."
[4]: https://openliberty.io/docs/latest/access-logging.html "HTTP access logging :: Open Liberty Docs"
[5]: https://www.ibm.com/support/pages/how-setup-liberty-log-rollover-both-time-based-and-size-based-options-similar-traditional-websphere-0?utm_source=chatgpt.com "How to setup Liberty Log Rollover with both Time-Based ..."