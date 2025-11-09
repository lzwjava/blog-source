---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: जेडब्ल्यूटी सीक्रेट त्रुटि को ठीक करना
translated: true
type: note
---

### LibreChat में JWT सीक्रेट एरर को ठीक करना

लॉग्स दिखा रहे हैं कि API शुरू तो हो रहा है, लेकिन गायब JWT सीक्रेट के कारण क्रैश हो रहा है: `JwtStrategy requires a secret or key`। यह LibreChat में एक आम सेटअप समस्या है—बैकएंड प्रमाणीकरण के लिए JWT (JSON Web Tokens) का उपयोग करता है, और एक सीक्रेट key के बिना, यह रणनीति को आरंभ नहीं कर सकता। RAG API, अनुमतियाँ, और अन्य सेवाएँ ठीक हैं, लेकिन यह मुख्य API को पूरी तरह से शुरू होने से रोकता है, जिससे http://localhost:3080 तक पहुँच अवरुद्ध हो जाती है।

#### त्वरित समाधान: JWT_SECRET सेट करें
1. **एक सुरक्षित सीक्रेट जनरेट करें**:
   - एक यादृच्छिक 32+ वर्णों वाली स्ट्रिंग बनाने के लिए यह कमांड चलाएँ (इसे अपने JWT_SECRET के रूप में उपयोग करें):
     ```
     openssl rand -base64 32
     ```
     उदाहरण आउटपुट: `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6`

2. **अपनी `.env` फ़ाइल अपडेट करें**:
   - `.env` खोलें (अपने LibreChat प्रोजेक्ट रूट में)।
   - इस लाइन को जोड़ें या अनकमेंट करें (अपने जनरेट किए गए सीक्रेट से बदलें):
     ```
     JWT_SECRET=your_generated_secret_here
     ```
   - अगर यह पहले से मौजूद है लेकिन खाली/कमेंट की गई है, तो बस इसे भर दें।
   - फ़ाइल सेव करें।

3. **सेवाएँ पुनरारंभ करें**:
   ```
   docker compose down
   docker compose up -d
   ```
   - लॉग देखें: `docker logs -f api` (या अगर नाम अलग है तो `docker logs -f librechat_api`)।
   - JWT एरर के बिना सफल स्टार्टअप के लिए देखें। इसे "Server running on port 3080" जैसा कुछ लॉग करना चाहिए।

#### सत्यापित करें कि यह काम कर रहा है
- पुनरारंभ के बाद, चल रहे कंटेनर जांचें:
  ```
  docker ps
  ```
  - `api` कंटेनर "Up" होना चाहिए और पोर्ट 3080 एक्सपोज़ करना चाहिए।
- पहुँच परीक्षण: अपने ब्राउज़र में http://localhost:3080 खोलें। आपको LibreChat लॉगिन/सेटअप पेज दिखना चाहिए।
- अगर अभी भी समस्याएँ हैं, तो नए एरर के लिए लॉग टेल करें: `docker logs api`.

#### लॉग्स से अन्य नोट्स
- **पुराना कॉन्फ़िग**: आप v1.2.1 पर हैं, लेकिन v1.3.0 उपलब्ध है। JWT ठीक करने के बाद, नई सुविधाओं (जैसे, बेहतर ऑथ विकल्प) के लिए [चेंजलॉग](https://www.librechat.ai/changelog) देखें। नवीनतम इमेज पुल करके अपडेट करें: `docker compose pull`।
- **Turnstile Disabled**: लोकल डेवलपमेंट के लिए ठीक है; प्रोडक्शन CAPTCHA के लिए इसे बाद में सक्षम करें।
- **UID/GID Warnings**: अगर वे बने रहते हैं, तो भविष्य में अनुमति संबंधी दिक्कतों से बचने के लिए उन्हें पहले बताए अनुसार सेट करें।

इससे आपका सिस्टम चलने लगना चाहिए—JWT_SECRET ऑथ एंडपॉइंट्स के लिए आवश्यक है। अगर फिक्स के बाद लॉग कोई अलग एरर दिखाते हैं, तो उन्हें यहाँ पेस्ट करें।

[LibreChat Environment Variables](https://www.librechat.ai/docs/configuration/dotenv#jwt_secret)  
[Common Docker Issues](https://github.com/danny-avila/LibreChat/issues?q=is%3Aissue+is%3Aopen+label%3Adocker)