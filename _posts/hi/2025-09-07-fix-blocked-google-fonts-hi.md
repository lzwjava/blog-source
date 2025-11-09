---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hi
layout: post
title: गूगल फॉन्ट्स अनुरोध ब्लॉक होने का समाधान
translated: true
type: note
---

वह अनुरोध आपके पेज द्वारा Google Fonts से एक वेबफ़ॉन्ट स्टाइलशीट लोड करने का प्रयास है:

* **यह क्या है:** `https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap` वह CSS है जो **Open Sans** फ़ॉन्ट फेस को परिभाषित करता है। आपकी थीम या कस्टम CSS इसे शामिल कर रही है ताकि साइट Open Sans में रेंडर हो सके।
* **आपको "Status: — / 0 B / no headers" क्यों दिखता है:** DevTools यह तब दिखाता है जब अनुरोध **ब्लॉक या कैंसिल** हो जाता है (उदाहरण के लिए, किसी एड-/प्राइवेसी-ब्लॉकर, सख्त Content-Security-Policy, नेटवर्क में खराबी, या देश-स्तरीय ब्लॉकिंग के कारण)। पेज फिर भी इसे रिक्वेस्ट करने का *प्रयास* करता है, इसलिए नेटवर्क रो दिखती है।

### जेकिल ब्लॉग में यह संभावित रूप से कहाँ से आता है

इनमें से एक आमतौर पर सही होता है:

1. **थीम इसे `<head>` में शामिल करती है**
   `_layouts/default.html` या `_includes/head.html` (या आपके द्वारा `remote_theme` का उपयोग करने पर थीम के समकक्ष) में इस तरह की लाइन देखें:
   `<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap" rel="stylesheet">`

2. **SCSS इसे इम्पोर्ट करती है**
   `/assets/css/*.scss` या `/_sass/**` में यह चेक करें:
   `@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap");`

3. **रिमोट थीम** (जैसे, jekyll-theme-cayman) अपने head include में Google Fonts को हार्डकोड करती है। अपने रेपो में थीम के head/layout को ओवरराइड करने से आप इसे हटा सकते हैं।

### इसे तेज़ी से कैसे खोजें

अपनी साइट रेपो रूट से, इनमें से कोई भी कोशिश करें:

```
rg -n "fonts.googleapis.com"
rg -n "Open Sans"
rg -n "display=swap"
```

### इसे ठीक करने या बदलने के विकल्प

**A) Google Fonts हटाएं और सिस्टम फ़ॉन्ट स्टैक का उपयोग करें (सबसे तेज़ और प्राइवेसी-फ्रेंडली)**

1. उस `<link>` (या SCSS `@import`) को डिलीट करें जो Google Fonts लाता है।
2. अपनी मुख्य स्टाइलशीट में, एक सिस्टम स्टैक सेट करें:

   ```css
   html, body {
     font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu,
                  "Helvetica Neue", Arial, "Noto Sans", sans-serif,
                  "Apple Color Emoji", "Segoe UI Emoji";
   }
   ```

   (Jekyll में, इसे `assets/css/style.scss` में शीर्ष पर फ्रंट-मैटर `---` लाइनों के साथ डालें।)

**B) Open Sans रखें लेकिन उसे सेल्फ-होस्ट करें**

1. Open Sans (400 & 700) के लिए WOFF2 फाइलें डाउनलोड करें और उन्हें `assets/fonts/` के अंदर रखें।
2. अपने CSS में जोड़ें:

   ```css
   @font-face {
     font-family: "Open Sans";
     font-style: normal;
     font-weight: 400;
     font-display: swap;
     src: url("/assets/fonts/OpenSans-400.woff2") format("woff2");
   }
   @font-face {
     font-family: "Open Sans";
     font-style: normal;
     font-weight: 700;
     font-display: swap;
     src: url("/assets/fonts/OpenSans-700.woff2") format("woff2");
   }
   body { font-family: "Open Sans", system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; }
   ```
3. Google Fonts का `<link>`/`@import` हटा दें।

**C) इसे वैसे ही छोड़ दें लेकिन अनुरोध के फेल होने से रोकें**

* अपनी साइट के लिए ब्लॉकिंग एक्सटेंशन को डिसेबल करें, या अपने CSP को ढीला करें ताकि `https://fonts.googleapis.com` और `https://fonts.gstatic.com` की अनुमति मिल सके।
* यदि आप ऐसे क्षेत्र में हैं जहाँ ये डोमेन ब्लॉक हैं, तो विकल्प A या B को प्राथमिकता दें।

### Jekyll-विशिष्ट ओवरराइड टिप्स

* **रिमोट थीम:** थीम की `/_includes/head.html` या `/_layouts/default.html` को उसी पाथ के साथ अपने रेपो में कॉपी करें, Google Fonts लाइन को हटा दें, और Jekyll आपके ओवरराइड का उपयोग करेगा।
* **मिनिफाइड head include:** कभी-कभी थीम फ़ॉन्ट्स को एक वेरिएबल के माध्यम से इंजेक्ट करती है। यदि ऐसा है, तो उस वेरिएबल को खाली सेट करें या फ़ॉन्ट्स को बाहर करने के लिए include को ओवरराइड करें।

यदि आप अपनी थीम का नाम (या अपनी `_config.yml` में `theme` / `remote_theme`) पेस्ट करते हैं, तो मैं ओवरराइड करने के लिए सटीक फ़ाइल और न्यूनतम अंतर दिखा सकता हूँ।