---
audio: false
generated: true
lang: hi
layout: post
title: जेकिल गिटहब पेजेज़ पर जीटैग.जेएस प्रदर्शन का अनुकूलन
translated: true
type: note
---

Jekyll के साथ बनाए गए GitHub Pages साइट पर `gtag.js` का उपयोग करने से कुछ विशेष सीमाएँ पैदा होती हैं, क्योंकि GitHub Pages की सर्वर-साइड नियंत्रण सीमित है और इसमें कैशिंग हेडर या सर्वर-साइड स्क्रिप्टिंग की सीधी पहुंच नहीं है। हालांकि, आप क्लाइंट-साइड तकनीकों और Jekyll-विशिष्ट कॉन्फ़िगरेशन का उपयोग करके `https://www.googletagmanager.com/gtag/js?id=UA-66656236-1` की फ़ेच गति को अभी भी ऑप्टिमाइज़ कर सकते हैं। इस संदर्भ में इसके प्रदर्शन को सुधारने के लिए नीचे लक्षित रणनीतियाँ दी गई हैं:

---

### 1. **`gtag.js` को एसिंक्रोनस लोड करें**
पेज रेंडरिंग को ब्लॉक होने से बचाने के लिए सुनिश्चित करें कि `gtag.js` स्क्रिप्ट एसिंक्रोनस लोड हो। अपनी Jekyll साइट में:
- स्क्रिप्ट को अपने Jekyll लेआउट या इंक्लूड फ़ाइल में जोड़ें (जैसे, `_includes/analytics.html` या सीधे अपने `default.html` लेआउट में)।
- `async` एट्रिब्यूट का उपयोग करें:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
```
- इसे अपने Jekyll टेम्पलेट (जैसे, `_layouts/default.html`) में `<head>` में या `</body>` से ठीक पहले रखें:
```html
<head>
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-66656236-1');
  </script>
</head>
```
- **यह कैसे मदद करता है**: `async` सुनिश्चित करता है कि स्क्रिप्ट HTML पार्सिंग को ब्लॉक नहीं करती, जिससे लोड टाइम कम महसूस होता है।

---

### 2. **Google के डोमेन के लिए Preconnect जोड़ें**
`googletagmanager.com` के लिए एक `preconnect` हिंट जोड़कर DNS लुकअप और कनेक्शन लेटेंसी कम करें। अपने Jekyll लेआउट (`_layouts/default.html` या `_includes/head.html`) में:
```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
```
- इसे `<head>` में `gtag.js` स्क्रिप्ट से पहले रखें।
- **यह कैसे मदद करता है**: DNS रेजोल्यूशन और TCP कनेक्शन जल्दी शुरू करता है, जिससे `gtag.js` का फ़ेच तेज होता है।

---

### 3. **`gtag.js` को Lazy-Load करें**
चूंकि GitHub Pages स्टेटिक है, आप क्रिटिकल कंटेंट को प्राथमिकता देने के लिए `gtag.js` को लेज़ी-लोड कर सकते हैं। निम्नलिखित JavaScript को अपने Jekyll टेम्पलेट या एक अलग JS फ़ाइल (जैसे, `assets/js/analytics.js`) में जोड़ें:
```javascript
window.addEventListener('load', () => {
  const script = document.createElement('script');
  script.src = 'https://www.googletagmanager.com/gtag/js?id=UA-66656236-1';
  script.async = true;
  document.head.appendChild(script);
  script.onload = () => {
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-66656236-1');
  };
});
```
- इस स्क्रिप्ट को अपने Jekyll लेआउट में शामिल करें:
```html
<script src="{{ '/assets/js/analytics.js' | relative_url }}"></script>
```
- **यह कैसे मदद करता है**: `gtag.js` के लोडिंग को पेज के क्रिटिकल रिसोर्सेज (जैसे, HTML, CSS) के लोड होने तक विलंबित करता है, जिससे इनिशियल पेज स्पीड में सुधार होता है।

---

### 4. **Cloudflare के माध्यम से CDN प्रॉक्सी का उपयोग करें**
GitHub Pages कस्टम कैशिंग हेडर की अनुमति नहीं देता है, लेकिन आप `gtag.js` को Cloudflare जैसे CDN के माध्यम से प्रॉक्सी कर सकते हैं ताकि इसे अपने यूजर्स के करीब कैश किया जा सके:
1. **Cloudflare सेटअप करें**:
   - अपनी GitHub Pages साइट को Cloudflare में जोड़ें (जैसे, `username.github.io`)।
   - अपने डोमेन के लिए Cloudflare के DNS और प्रॉक्सी को सक्षम करें।
2. **`gtag.js` को प्रॉक्सी करें**:
   - `gtag.js` स्क्रिप्ट को कैश करने के लिए Cloudflare में एक पेज रूल बनाएं या अपनी Jekyll साइट के `_site` फ़ोल्डर में एक लोकल कॉपी होस्ट करें (जैसे, `assets/js/gtag.js`)।
   - अपने स्क्रिप्ट टैग को अपडेट करें:
```html
<script async src="{{ '/assets/js/gtag.js' | relative_url }}"></script>
```
   - यह सुनिश्चित करने के लिए कि यह अप-टू-डेट है, लोकल कॉपी को Google के `gtag.js` के साथ समय-समय पर सिंक करें (मैन्युअल प्रक्रिया या CI/CD स्क्रिप्ट के माध्यम से)।
3. **कैश सेटिंग्स**:
   - Cloudflare में, स्क्रिप्ट के लिए एक कैश रूल सेट करें (जैसे, `Cache Everything` जिसमें TTL 1 घंटे की हो)।
- **यह कैसे मदद करता है**: Cloudflare के एज सर्वर स्क्रिप्ट को आपके यूजर्स के करीब के स्थान से सर्व करके लेटेंसी कम करते हैं।
- **नोट**: Google की स्क्रिप्ट्स को प्रॉक्सी करने में सावधानी बरतें, क्योंकि वे अक्सर अपडेट हो सकती हैं। यह सुनिश्चित करने के लिए कि ट्रैकिंग काम करती है, अच्छी तरह से टेस्ट करें।

---

### 5. **Jekyll बिल्ड और डिलीवरी को ऑप्टिमाइज़ करें**
सुनिश्चित करें कि आपकी Jekyll साइट समग्र पेज लोड टाइम को कम करने के लिए ऑप्टिमाइज़ की गई है, जो `gtag.js` के प्रदर्शन में अप्रत्यक्ष रूप से मदद करती है:
- **एसेट्स को मिनिफाई करें**:
  - HTML, CSS, और JS को मिनिफाई करने के लिए `jekyll-compress` या `jekyll-minifier` जैसे Jekyll प्लगइन का उपयोग करें।
  - अपने `_config.yml` में जोड़ें:
```yaml
plugins:
  - jekyll-compress
```
- **Gzip कम्प्रेशन सक्षम करें**:
  - GitHub Pages समर्थित फ़ाइलों के लिए स्वचालित रूप से Gzip सक्षम करता है, लेकिन ब्राउज़र डेव टूल्स में `Content-Encoding` हेडर चेक करके पुष्टि करें कि आपकी CSS/JS फ़ाइलें कंप्रेस हैं।
- **ब्लॉकिंग रिसोर्सेज कम करें**:
  - `gtag.js` से पहले लोड होने वाले रेंडर-ब्लॉकिंग CSS/JS फ़ाइलों की संख्या कम से कम करें।
  - एसेट डिलीवरी को ऑप्टिमाइज़ करने के लिए `jekyll-assets` या इसी तरह के टूल का उपयोग करें:
```yaml
plugins:
  - jekyll-assets
```
- **क्रिटिकल CSS को इनलाइन करें**:
  - क्रिटिकल CSS को `<head>` में इनलाइन करें और नॉन-क्रिटिकल CSS को डिफर करें ताकि रेंडर-ब्लॉकिंग टाइम कम हो, जिससे `gtag.js` का लोड तेज दिखाई दे सकता है।
- **इमेज ऑप्टिमाइज़ेशन**:
  - समग्र पेज वेट कम करने के लिए `jekyll-picture-tag` या इसी तरह के प्लगइन का उपयोग करके इमेज को कंप्रेस करें, जिससे `gtag.js` के लिए बैंडविड्थ मुक्त होती है।

---

### 6. **मिनिमल एनालिटिक्स पर स्विच करें**
यदि `gtag.js` अभी भी धीमा है या एनालिटिक्स क्रिटिकल नहीं है:
- Plausible या Fathom जैसे हल्के विकल्पों पर विचार करें, जो छोटी स्क्रिप्ट्स (~1 KB बनाम `gtag.js` के ~50 KB) का उपयोग करते हैं।
- Plausible के लिए उदाहरण:
```html
<script defer data-domain="yourdomain.com" src="https://plausible.io/js/plausible.js"></script>
```
- इसे अपने Jekyll `_includes/analytics.html` में जोड़ें और इसे अपने लेआउट में शामिल करें।
- **यह कैसे मदद करता है**: छोटी स्क्रिप्ट्स तेजी से लोड होती हैं, खासकर GitHub Pages के स्टेटिक इन्फ्रास्ट्रक्चर पर।

---

### 7. **प्रदर्शन का परीक्षण और मॉनिटरिंग करें**
- **फ़ेच टाइम मापें**:
  - `gtag.js` लोड टाइम चेक करने के लिए Chrome DevTools (नेटवर्क टैब) का उपयोग करें।
  - समग्र पेज प्रदर्शन का आकलन करने के लिए Lighthouse या WebPageTest जैसे टूल से टेस्ट करें।
- **यूजर लोकेशन सिम्युलेट करें**:
  - अपने ऑडियंस के स्थान वाले क्षेत्रों से लोड टाइम टेस्ट करने के लिए Pingdom जैसे टूल का उपयोग करें, क्योंकि GitHub Pages और Google के CDN प्रदर्शन में भौगोलिक रूप से भिन्नता होती है।
- **रियल यूजर मेट्रिक्स मॉनिटर करें**:
  - यदि Google Analytics का उपयोग कर रहे हैं, तो `gtag.js` के प्रभाव को ट्रैक करने के लिए साइट स्पीड रिपोर्ट चेक करें।
- **Jekyll-विशिष्ट डीबगिंग**:
  - अपनी साइट में धीमी बिल्डिंग वाले कंपोनेंट्स की पहचान करने के लिए `jekyll build --profile` चलाएं जो प्रदर्शन को अप्रत्यक्ष रूप से प्रभावित कर सकते हैं।

---

### 8. **GitHub Pages की सीमाएँ**
- **सर्वर-साइड नियंत्रण नहीं**: GitHub Pages एक स्टेटिक होस्ट है, इसलिए आप `gtag.js` के लिए सर्वर-साइड टैगिंग या कस्टम कैश हेडर लागू नहीं कर सकते।
- **HTTP/3 नहीं**: GitHub Pages HTTP/2 का उपयोग करता है, जो तेज है लेकिन HTTP/3 जितना ऑप्टिमाइज़ नहीं है। Cloudflare जैसा CDN HTTP/3 में अपग्रेड कर सकता है।
- **भौगोलिक लेटेंसी**: GitHub Pages सर्वर मुख्य रूप से US-आधारित हैं, इसलिए US से दूर के यूजर्स को धीमा लोड अनुभव हो सकता है। एक CDN इससे निपटने में मदद करता है।

---

### Jekyll सेटअप उदाहरण
यहाँ `preconnect` और `async` को मिलाने के लिए आपकी Jekyll साइट के लिए एक नमूना `_includes/analytics.html` दिया गया है:
```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-66656236-1');
</script>
```
इसे अपने लेआउट (`_layouts/default.html`) में शामिल करें:
```html
<head>
</head>
```

---

### अगले कदम
- **वर्तमान प्रदर्शन का परीक्षण करें**: `gtag.js` के लिए वर्तमान फ़ेच टाइम (ब्राउज़र डेव टूल से) या अपनी साइट का URL साझा करें, और मैं इसका और विश्लेषण कर सकता हूँ।
- **भौगोलिक संदर्भ**: मुझे अपने ऑडियंस का प्राथमिक स्थान बताएं (जैसे, US, Europe, Asia) ताकि CDN या प्रॉक्सी सिफारिशों को तैयार किया जा सके।
- **Cloudflare सेटअप**: यदि आप Cloudflare का उपयोग करने के लिए तैयार हैं, तो मैं `gtag.js` को प्रॉक्सी करने के लिए विस्तृत चरण प्रदान कर सकता हूँ।
- **वैकल्पिक एनालिटिक्स**: यदि आप Google Analytics से स्विच करने के लिए तैयार हैं, तो मैं विशिष्ट हल्के टूल और उनके Jekyll इंटीग्रेशन की सिफारिश कर सकता हूँ।

क्या आप चाहते हैं कि मैं इनमें से किसी विशेष पहलू पर ध्यान केंद्रित करूं या कोई विशिष्ट विश्लेषण करूं (जैसे, आपकी साइट के प्रदर्शन का परीक्षण करना या Cloudflare सेटअप गाइड प्रदान करना)?