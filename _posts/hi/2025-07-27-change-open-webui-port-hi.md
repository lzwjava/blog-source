---
audio: false
generated: true
image: false
lang: hi
layout: post
title: ओपन वेबयूआई पोर्ट बदलें
translated: true
type: note
---

`open-webui serve` कमांड (आमतौर पर pip के माध्यम से इंस्टॉल करने के बाद) का उपयोग करके Open WebUI चलाते समय पोर्ट बदलने के लिए, `--port` फ्लैग के बाद अपना वांछित पोर्ट नंबर निर्दिष्ट करें। डिफ़ॉल्ट पोर्ट 8080 है।

### चरण:
1. सुनिश्चित करें कि Open WebUI इंस्टॉल है:  
   ```
   pip install open-webui
   ```

2. सर्वर को एक अलग पोर्ट (उदाहरण के लिए, 3000) पर चलाएँ:  
   ```
   open-webui serve --port 3000
   ```

   - इससे WebUI `http://localhost:3000` (या आपके सर्वर के IP पते के साथ नए पोर्ट) पर एक्सेस करने योग्य हो जाएगी।
   - ध्यान दें: `serve` कमांड का उपयोग करते समय `PORT` एनवायरनमेंट वेरिएबल को नज़रअंदाज कर दिया जाता है; आपको इसके स्थान पर `--port` फ्लैग का उपयोग करना होगा।

यदि आप सीधे इंस्टॉलेशन के बजाय Docker का उपयोग कर रहे हैं:
- `PORT` एनवायरनमेंट वेरिएबल सेट करें, उदाहरण के लिए, `docker run -e PORT=3000 ...`।
- पोर्ट को बाहरी रूप से `-p <host_port>:3000` के साथ मैप करें (आवश्यकतानुसार समायोजित करें)।

पूर्ण इंस्टॉलेशन और कॉन्फ़िगरेशन विवरण के लिए, आधिकारिक दस्तावेज़ देखें।

[Environment Variable Configuration | Open WebUI](https://docs.openwebui.com/getting-started/env-configuration/)  
[Quick Start | Open WebUI](https://docs.openwebui.com/getting-started/quick-start/)