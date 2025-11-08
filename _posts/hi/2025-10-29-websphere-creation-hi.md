---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: वेबस्फीयर एप्लिकेशन सर्वर निर्माण को सही करें
translated: true
type: note
---

नहीं, `nodeName -name serverName admin create applciation server` (ध्यान दें "applciation" में टाइपो) कमांड IBM WebSphere Application Server (WAS) में wsadmin स्क्रिप्टिंग का उपयोग करके एप्लिकेशन सर्वर बनाने के लिए सही नहीं है।

### सही सिंटैक्स
सही कमांड Jython (wsadmin के लिए अनुशंसित स्क्रिप्टिंग भाषा) में `AdminTask.createApplicationServer` मेथड का उपयोग करती है। इसके लिए आवश्यक है:
- पहले आर्ग्युमेंट के रूप में **नोड नाम** (एक स्ट्रिंग)।
- दूसरे आर्ग्युमेंट के रूप में **ऑप्शन की एक लिस्ट**, जिसमें सर्वर नाम के लिए `-name` शामिल है।

**बेसिक उदाहरण:**
```jython
AdminTask.createApplicationServer('YourNodeName', ['-name', 'YourServerName'])
```

- `'YourNodeName'` को एक्चुअल नोड से बदलें (उदाहरण के लिए, `ndnode1`)।
- `'YourServerName'` को वांछित सर्वर नाम से बदलें (उदाहरण के लिए, `appServer1`)।
- ऑप्शनल पैरामीटर को लिस्ट में जोड़ा जा सकता है, जैसे डिफ़ॉल्ट सर्वर टेम्पलेट का उपयोग करने के लिए `'-templateName', 'default'`।

### इसे चलाने के चरण
1. Jython मोड में wsadmin शुरू करें: `./wsadmin.sh -lang jython -user admin -password pass`।
2. ऊपर दिए गए कमांड को एक्जीक्यूट करें।
3. कॉन्फ़िगरेशन सेव करें: `AdminConfig.save()`।
4. बाहर निकलें: `quit`।

यह निर्दिष्ट नोड पर एक बेसिक एप्लिकेशन सर्वर बनाता है। अधिक ऑप्शन (जैसे, पोर्ट, JVM सेटिंग्स) के लिए, पूर्ण AdminTask डॉक्यूमेंटेशन देखें।

[AdminTask ऑब्जेक्ट के लिए ServerManagement कमांड ग्रुप](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-servermanagement-command-group-admintask-object)  
[स्क्रिप्टिंग का उपयोग करके एक सर्वर बनाना](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-creating-server-using)