---
audio: false
generated: true
image: false
lang: hi
layout: post
title: गिटहब कोड खोज युक्तियाँ जेसन
translated: true
type: note
---

आप GitHub कोड खोज क्वेरी इस प्रकार लिख सकते हैं:

```
"deepseek/deepseek-chat-v3.1" language:JSON
```

### नोट्स:

* कोट्स यह सुनिश्चित करते हैं कि GitHub सटीक स्ट्रिंग `deepseek/deepseek-chat-v3.1` खोजता है।
* `language:JSON` (या `lang:json`, दोनों काम करते हैं) परिणामों को JSON फ़ाइलों तक सीमित करता है।
* यदि आप JSON जैसे दिखने वाले कॉन्फ़िग्स शामिल करना चाहते हैं जो `.json` फ़ाइलों में नहीं हैं (जैसे `.ipynb` या `.eslintrc`), तो आप `lang:` फ़िल्टर हटा सकते हैं।

उदाहरण:

* केवल JSON फ़ाइलें खोजें:

  ```
  "deepseek/deepseek-chat-v3.1" lang:json
  ```

* सभी फ़ाइल प्रकार खोजें लेकिन फिर भी JSON परिणामों को हाइलाइट करें:

  ```
  "deepseek/deepseek-chat-v3.1"
  ```

क्या आप चाहते हैं कि मैं आपको इसे और परिष्कृत करने का तरीका दिखाऊं — उदाहरण के लिए, केवल रिपॉजिटरी, इश्यूज़, या कोड के अंदर खोजना?