---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: सफारी लोकलहोस्ट प्रमाणीकरण सुधार
translated: true
type: note
---

यह समस्या इसलिए उत्पन्न होती है क्योंकि macOS पर Safari, localhost URLs के लिए Chrome की तुलना में सख्त सुरक्षा नीतियों को लागू करता है। विशेष रूप से, LibreChat जैसे HTTP पर चलने वाले ऐप्स के लिए लगातार लॉगआउट लूप्स या हर बार पुनः प्रमाणीकरण को रोकने के लिए, Safari लगातार कुकीज़ और प्रमाणीकरण सत्रों की अनुमति देने के लिए एक सुरक्षित HTTPS संदर्भ की आवश्यकता होती है। Chrome localhost पर HTTP के साथ अधिक अनुमेय है, इसीलिए वहाँ प्रमाणीकरण बना रहता है लेकिन Safari में नहीं।[1][2][3]

### मुख्य कारक
- **ब्राउज़र नीतियाँ**: Safari जैसे आधुनिक ब्राउज़र मिश्रित-सामग्री चेतावनियों और सत्र असुरक्षा से बचने के लिए localhost पर HTTPS चाहते हैं।
- **LibreChat व्यवहार**: LibreAuth प्रमाणीकरण के लिए सुरक्षित कुकी या localStorage-आधारित टोकन का उपयोग करता है, जो HTTP पर Safari में इसकी गैर-सुरक्षित मूल के सख्त हैंडलिंग के कारण टूट जाते हैं।

### समाधान (सरलता और प्रभावशीलता के अनुसार क्रमबद्ध)
1. **Localhost के लिए HTTPS सेट अप करें (अनुशंसित)**:
   - LibreChat का अपना दस्तावेज़ीकरण और ब्लॉग HTTP-प्रेरित लॉगआउट को रोकने के लिए इसे सुझाते हैं।[1]
   - Localhost के लिए स्थानीय SSL प्रमाणपत्र उत्पन्न करने और उन पर भरोसा करने के लिए `mkcert` (एक निःशुल्क टूल) का उपयोग करें:
     - `brew install mkcert` के माध्यम से `mkcert` इंस्टॉल करें या GitHub से डाउनलोड करें।
     - रूट CA इंस्टॉल करने के लिए `mkcert -install` चलाएँ।
     - प्रमाणपत्र बनाएँ: `mkcert localhost 127.0.0.1`।
     - LibreChat को इन प्रमाणपत्रों का उपयोग करने के लिए कॉन्फ़िगर करें (जैसे, Docker env vars या config के माध्यम से): अपनी `.env` फ़ाइल या वातावरण में `HTTPS=true`, `SSL_CRT_FILE=/path/to/localhost.pem`, और `SSL_KEY_FILE=/path/to/localhost-key.pem` जोड़ें।
     - LibreChat को पुनरारंभ करें और `https://localhost:3080` के माध्यम से एक्सेस करें।
     - Safari अब इसे सुरक्षित मानेगा, जिससे सीमलेस लॉगिन की अनुमति मिलेगी।

2. **विकल्प: localhost के बजाय 127.0.0.1 का उपयोग करें**:
   - Safari कभी-कभी `localhost` के साथ अलग तरह से व्यवहार करता है (IPv6 या DNS रिज़ॉल्यूशन के कारण)। `http://127.0.0.1:3080` एक्सेस करने का प्रयास करें – इसने कुछ मामलों में इसी तरह के कनेक्शन मुद्दों को हल किया है, हालाँकि यह प्रमाणीकरण दृढ़ता को पूरी तरह से ठीक नहीं कर सकता है।[4][4][5]

3. **localhost के लिए Safari वेबसाइट डेटा साफ़ करें**:
   - Safari > Preferences > Privacy > Manage Website Data पर जाएं > "localhost" खोजें > कोई भी प्रविष्टियाँ हटाएँ।
   - यह Safari को HTTPS अपग्रेड या कैश्ड असुरक्षित संदर्भों को लागू करना बंद करने के लिए मजबूर करता है।[3][2]
   - Safari को पुनरारंभ करें और परीक्षण करें; यदि LibreChat इसका समर्थन करता है, तो प्रमाणीकरण बना रहना चाहिए।

यदि इनमें से कोई भी काम नहीं करता है, तो प्रमाणीकरण त्रुटियों के लिए LibreChat लॉग्स जांचें, सुनिश्चित करें कि आपके `.env` में कोई विरोधाभासी फ़्लैग्स नहीं हैं (जैसे, `ALLOW_ANONYMOUS=true` यदि वांछित हो तो प्रमाणीकरण को पूरी तरह से अक्षम कर देता है), और पुष्टि करें कि आप Safari के प्राइवेट ब्राउज़िंग मोड में नहीं हैं, जो लगातार स्टोरेज को ब्लॉक करता है।[6][7] यदि समस्या बनी रहती है, तो गहन समस्या निवारण के लिए अपना LibreChat संस्करण और .env कॉन्फ़िग प्रदान करें।

सन्दर्भ:
[1] https://www.librechat.ai/blog/2024-05-16_unsecured_http
[2] https://github.com/danny-avila/LibreChat/discussions/529
[3] https://stackoverflow.com/questions/46394682/safari-keeps-forcing-https-on-localhost
[4] https://superuser.com/questions/30827/safari-is-unable-to-reach-localhost-127-0-0-1
[5] https://apple.stackexchange.com/questions/422556/localhost-has-stopped-working-on-chrome-and-safari-since-upgrading-to-big-sur
[6] https://www.librechat.ai/docs/configuration/authentication
[7] https://discussions.apple.com/thread/255906354