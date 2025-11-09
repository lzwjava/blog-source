---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: गिटहब कोपायलॉट प्रमाणीकरण प्रवाह
translated: true
type: note
---

अच्छा सवाल — GitHub Copilot का प्रमाणीकरण प्रवाह मूल रूप से एक मानक **OAuth2 डिवाइस कोड ग्रांट** है, लेकिन उसके ऊपर Copilot सेवा के लिए कुछ GitHub-विशिष्ट टोकन जोड़े गए हैं। मैं इसे चरण दर चरण समझाता हूँ:

---

### 1. **डिवाइस फ्लो (`/login/device/code`)**

* जब आप पहली बार लॉग इन करते हैं, तो Copilot क्लाइंट (जैसे, VS Code एक्सटेंशन, JetBrains प्लगइन, या CLI) GitHub के OAuth एंडपॉइंट को कॉल करता है:

  ```
  POST https://github.com/login/device/code
  ```
* यह **client_id** (GitHub Copilot के लिए विशिष्ट) के साथ रिक्वेस्ट भेजता है।
* GitHub जवाब देता है:

  * `device_code` (पोलिंग के लिए उपयोग किया जाने वाला आंतरिक कोड),
  * `user_code` (वह कोड जो आपको ब्राउज़र में दिखता और दर्ज करना होता है),
  * `verification_uri` (वह URL जहाँ आप कोड दर्ज करने जाते हैं),
  * `interval` (क्लाइंट को कितनी बार पोल करना चाहिए)।

---

### 2. **एक्सेस टोकन के लिए पोलिंग**

* Copilot क्लाइंट फिर पोल करता है:

  ```
  POST https://github.com/login/oauth/access_token
  ```
* इसमें `device_code` और `client_id` शामिल होते हैं।
* एक बार जब आप ब्राउज़र में स्वीकृत कर देते हैं, GitHub लौटाता है:

  * `access_token` (एक **GitHub OAuth टोकन** जो Copilot उपयोग के लिए स्कोप किया गया है),
  * `token_type=bearer`,
  * `expires_in` (जीवनकाल)।

यह `access_token` एक **सामान्य GitHub OAuth2 टोकन** है।

---

### 3. **`copilot_internal` टोकन के लिए एक्सचेंज**

* Copilot क्लाइंट, GitHub OAuth टोकन का उपयोग सीधे Copilot API को कॉल करने के लिए नहीं कर सकता।
* इसके बजाय, वह इसे Copilot सेवा के साथ एक्सचेंज करता है:

  ```
  POST https://api.github.com/copilot_internal/v2/token
  Authorization: Bearer <GitHub OAuth access_token>
  ```
* प्रतिक्रिया होती है:

  ```json
  {
    "token": "<copilot_internal token>",
    "expires_at": "...",
    "user": { ... }
  }
  ```
* यह **`copilot_internal` v2 टोकन** वह टोकन है जिसका उपयोग Copilot क्लाइंट **Copilot इन्फ़रेंस सेवा** (जैसे, `https://copilot-proxy.githubusercontent.com`) से बात करने के लिए करता है।

---

### 4. **`copilot_internal` टोकन का उपयोग**

* सभी बाद की कम्प्लीशन या चैट रिक्वेस्ट इसके साथ प्रमाणित होती हैं:

  ```
  Authorization: Bearer <copilot_internal token>
  ```
* इस टोकन का जीवनकाल छोटा होता है (आमतौर पर ~1 घंटा) और यह आपके GitHub अकाउंट और Copilot सब्सक्रिप्शन स्थिति से बंधा होता है।
* क्लाइंट GitHub OAuth एक्सेस टोकन का फिर से एक्सचेंज करके इसे समय-समय पर रिफ़्रेश करता रहता है।

---

✅ **संक्षेप में:**

* `/login/device/code` → आपको ब्राउज़र में प्रमाणीकरण के लिए एक कोड देता है।
* `/login/oauth/access_token` → आपको एक GitHub OAuth टोकन देता है।
* `/copilot_internal/v2/token` → उस टोकन को एक अल्पकालिक Copilot टोकन के लिए एक्सचेंज करता है, जो कम्प्लीशन के लिए उपयोग किया जाने वाला *वास्तविक* क्रेडेंशियल है।

---

क्या आप **सटीक अनुरोध/प्रतिक्रिया उदाहरण** (हेडर और नमूना JSON के साथ) भी देखना चाहेंगे ताकि आप व्यवहार में देख सकें कि पेलोड कैसा दिखता है?