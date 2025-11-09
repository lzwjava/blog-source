---
audio: false
date: 2025-09-14
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: लिबरेचैट प्रमाणीकरण वर्कअराउंड अक्षम करना
translated: true
type: note
---

संक्षिप्त उत्तर: आप LibreChat में प्रमाणीकरण (authentication) को पूरी तरह से बंद नहीं कर सकते, लेकिन आप "बार-बार लॉगिन करने के लिए कहने" की समस्या को रोक सकते हैं और इसे "बिना-लॉगिन" जैसा महसूस करा सकते हैं। यहां बताया गया है कि वास्तव में क्या काम करता है (और क्यों):

### 1) आप प्रमाणीकरण को पूरी तरह से अक्षम नहीं कर सकते

यह रखरखावकर्ता (maintainer) द्वारा पुष्टि की गई है: पंजीकरण (registration) को अक्षम किया जा सकता है, लेकिन प्रमाणीकरण प्रणाली को स्वयं बंद नहीं किया जा सकता। ([GitHub][1])

### 2) आप बार-बार लॉग आउट क्यों होते हैं

यदि आप **HTTP** (जैसे, LAN IP) के माध्यम से अपने इंस्टेंस तक पहुंचते हैं, तो प्रोडक्शन में कुकीज़ (cookies) को `secure` चिह्नित किया जाता है, इसलिए ब्राउज़र उन्हें नहीं रखेगा; आप लॉगिन पर वापस चले जाते हैं। **HTTPS** (यहां तक कि सेल्फ-साइन्ड) का उपयोग करें या API को एक डेव मोड में चलाएं जो सिक्योर कुकीज़ को अक्षम कर दे। ([GitHub][1])

### 3) दो विश्वसनीय समाधान

#### विकल्प A — उचित/सुरक्षित (अनुशंसित)

* LibreChat को HTTPS के पीछे रखें (nginx/caddy/traefik; LAN पर सेल्फ-साइन्ड ठीक है)।
* फिर अपनी `.env` फ़ाइल में सत्र (session) समय सीमा बढ़ाएँ:

  ```
  SESSION_EXPIRY=1000 * 60 * 60 * 24       # 24 घंटे
  REFRESH_TOKEN_EXPIRY=(1000 * 60 * 60 * 24) * 30  # 30 दिन
  ```
* env बदलने के बाद कंटेनरों को पुनरारंभ (restart) करें।
  यह आपको दिनों/हफ्तों तक लॉग इन रखता है और कुकी ड्रॉप की समस्या को ठीक करता है। ([GitHub][2])

#### विकल्प B — "मैं एक प्राइवेट LAN पर हूं और बस यह चाहता हूं कि यह लॉग आउट होना बंद हो जाए"

* एक `docker-compose.override.yml` फ़ाइल बनाएं और API को डेव मोड में चलाएं (जो सिक्योर कुकीज़ को अक्षम कर देता है):

  ```yaml
  services:
    api:
      command: npm run backend:dev
  ```
* लागू करने के लिए `docker compose up -d` चलाएं।
  यह कम सुरक्षित है (कुकीज़ `secure` नहीं होतीं), लेकिन यह सादे HTTP पर जबरदस्ती पुनः-लॉगिन को रोक देता है। ([librechat.ai][3])

### 4) वैकल्पिक सुविधा-संबंधी समायोजन (Quality-of-life tweaks)

* **नए साइनअप को अक्षम करें** ताकि यह प्रभावी रूप से सिंगल-यूजर बन जाए:

  ```
  ALLOW_REGISTRATION=false
  ```

  (यदि आवश्यक हो तो भी आप `npm run create-user` के माध्यम से उपयोगकर्ता जोड़ सकते हैं।) ([librechat.ai][4])
* यदि आप सबसे सरल लॉगिन पथ चाहते हैं, तो `.env` में अन्य ऑथ टॉगल (ईमेल/सोशल लॉगिन फ्लैग) रखें। ([librechat.ai][5])

### 5) आपके मामले के लिए त्वरित चेकलिस्ट (v0.8.0-rc3)

1. तय करें: HTTPS प्रॉक्सी (सर्वोत्तम) **या** डेव मोड (त्वरित LAN फिक्स)।
2. `.env` में लंबा `SESSION_EXPIRY` और `REFRESH_TOKEN_EXPIRY` सेट करें।
3. स्टैक को पुनरारंभ करें ताकि env परिवर्तन प्रभावी हों।
4. (वैकल्पिक) "सिंगल-यूजर" अनुभव के लिए पंजीकरण बंद कर दें।

यदि आप चाहें, तो अपनी मौजूदा `docker-compose.yml` और `.env` फ़ाइल (बिना सीक्रेट्स के) पेस्ट करें। मैं चिह्नित कर दूंगा कि आपकी सेटअप के लिए क्या जोड़ना/बदलना है।

[1]: https://github.com/danny-avila/LibreChat/discussions/572 "[Question]: Require login every time refresh · danny-avila LibreChat · Discussion #572 · GitHub"
[2]: https://github.com/danny-avila/LibreChat/discussions/2571?utm_source=chatgpt.com "Is there a way to increase or disable the auto-logoff time?"
[3]: https://www.librechat.ai/blog/2024-05-16_unsecured_http "GitHub"
[4]: https://www.librechat.ai/docs/configuration/authentication "GitHub"
[5]: https://www.librechat.ai/docs/configuration/dotenv "GitHub"