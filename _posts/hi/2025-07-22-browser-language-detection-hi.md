---
audio: false
generated: true
lang: hi
layout: post
title: उपयोगकर्ता भाषा वरीयता का पता लगाएं
translated: true
type: note
---

### उपयोगकर्ता के देश या भाषा वरीयता का पता लगाना

चूंकि आपकी Jekyll ब्लॉग स्टैटिक (जेनरेट किए गए HTML/JS) है, आप इसे बिना किसी होस्टिंग प्लेटफॉर्म के एकीकृत किए आसानी से सर्वर-साइड डिटेक्शन नहीं कर सकते (जैसे, Netlify functions या GitHub Pages जिसकी अपनी सीमाएं हैं)। सबसे अच्छा तरीका है पेज लोड पर क्लाइंट-साइड JavaScript डिटेक्शन। आपके पास दो मुख्य विकल्प हैं:

1.  **ब्राउज़र भाषा वरीयता** (आपके उपयोग के मामले के लिए अनुशंसित): यह उपयोगकर्ता की ब्राउज़र सेटिंग्स से उनकी पसंदीदा भाषा का पता लगाता है (`navigator.language` या `navigator.languages` के माध्यम से)। यह तेज़ है, बाहरी APIs की आवश्यकता नहीं है, उपयोगकर्ता की गोपनीयता का सम्मान करता है (कोई IP साझाकरण नहीं), और सीधे देश के बजाय भाषा से जुड़ा होता है। अक्सर देशों में कई भाषाएं होती हैं (उदाहरण के लिए, भारत में हिंदी के साथ-साथ अंग्रेजी का व्यापक रूप से उपयोग होता है), इसलिए ड्रॉपडाउन को स्वचालित रूप से सेट करने के लिए यह अधिक सटीक है।

2.  **IP-आधारित देश डिटेक्शन**: यह उपयोगकर्ता के IP पते से देश प्राप्त करने के लिए एक मुफ्त जियोलोकेशन API का उपयोग करता है, फिर इसे एक भाषा से मैप करता है। यह तब उपयोगी होता है जब आपको विशेष रूप से देश की जानकारी चाहिए (जैसे, एनालिटिक्स के लिए), लेकिन इसके लिए बाहरी फ़ेच की आवश्यकता होती है, गोपनीयता के निहितार्थ हो सकते हैं, और यह हमेशा सटीक नहीं होता (VPN, प्रॉक्सी)। देश को भाषा से मैप करना अनुमानित होता है।

आपका लक्ष्य `<select id="sort-select">` ड्रॉपडाउन में भाषा को स्वचालित रूप से चुनना प्रतीत होता है (जैसे, अंग्रेजी के लिए 'date-desc|en')। मैं दोनों विधियों के लिए कोड प्रदान करूंगा, जिसे आप अपने `<script>` टैग के अंदर, `const sortSelect = document.getElementById('sort-select');` के ठीक बाद जोड़ सकते हैं।

`localStorage` की जांच को प्राथमिकता दें (जैसा कि आपका कोड पहले से करता है), फिर यदि कोई सहेजी गई वरीयता मौजूद नहीं है तो डिटेक्शन पर वापस आ जाएं।

#### विकल्प 1: ब्राउज़र भाषा का उपयोग करना (सरल और पसंदीदा)
इस कोड स्निपेट को जोड़ें। यह `navigator.language` से प्राथमिक भाषा कोड की जांच करता है (जैसे, 'en-US' -> 'en', 'zh-CN' -> 'zh') और इसे आपके ड्रॉपडाउन मानों से मैप करता है। यदि कोई मेल नहीं होता है तो यह अंग्रेजी पर डिफ़ॉल्ट हो जाता है।

```javascript
// Inside window.addEventListener('load', function () { ... });

// After const sortSelect = ...;

// Restore from localStorage if available
const savedSort = localStorage.getItem('sortOption');
if (savedSort) {
  sortSelect.value = savedSort;
} else {
  // Detect browser language if no saved preference
  let lang = navigator.language.toLowerCase().split('-')[0]; // e.g., 'en-US' -> 'en'
  
  // Special handling for Chinese variants (zh-Hant for traditional)
  if (lang === 'zh') {
    const fullLang = navigator.language.toLowerCase();
    if (fullLang.includes('tw') || fullLang.includes('hk') || fullLang.includes('hant')) {
      lang = 'hant';
    } else {
      lang = 'zh'; // Simplified Chinese
    }
  }

  // Map to your dropdown options (add more if needed)
  const langMap = {
    'en': 'date-desc|en',
    'zh': 'date-desc|zh',
    'ja': 'date-desc|ja',
    'es': 'date-desc|es',
    'hi': 'date-desc|hi',
    'fr': 'date-desc|fr',
    'de': 'date-desc|de',
    'ar': 'date-desc|ar',
    'hant': 'date-desc|hant'
  };

  sortSelect.value = langMap[lang] || 'date-desc|en'; // Default to English
}

updatePosts();
```

यह लोड पर सिंक्रोनस रूप से चलता है, इसलिए कोई देरी नहीं होती। इसे अपनी ब्राउज़र भाषा सेटिंग्स बदलकर टेस्ट करें (जैसे, Chrome में: Settings > Languages)।

#### विकल्प 2: IP-आधारित देश डिटेक्शन का उपयोग करना
इसके लिए एक मुफ्त API को एक async फ़ेच की आवश्यकता होती है। मैं `country.is` की सलाह देता हूं क्योंकि यह सरल है और सिर्फ देश कोड लौटाता है (जैसे, {country: 'US'})। यह मुफ्त है, कोई API key की आवश्यकता नहीं है, और ओपन-सोर्स है।

इस कोड को जोड़ें। ध्यान दें: यह async है, इसलिए हम UI को ब्लॉक करने से बचने के लिए `await` का उपयोग करते हैं और इसे एक async फ़ंक्शन में लपेटते हैं। यदि फ़ेच विफल हो जाती है (जैसे, ad-blockers के कारण), तो यह अंग्रेजी पर डिफ़ॉल्ट हो जाती है।

```javascript
// Inside window.addEventListener('load', async function () { ... });  // Make the load handler async

// After const sortSelect = ...;

// Restore from localStorage if available
const savedSort = localStorage.getItem('sortOption');
if (savedSort) {
  sortSelect.value = savedSort;
  updatePosts();
} else {
  try {
    // Fetch country code
    const response = await fetch('https://country.is/');
    const data = await response.json();
    const country = data.country.toUpperCase(); // e.g., 'US'

    // Map country codes to your languages (ISO 3166-1 alpha-2 codes)
    // This is approximate; expand as needed (e.g., multiple countries per language)
    const countryLangMap = {
      'US': 'date-desc|en',  // USA -> English
      'GB': 'date-desc|en',  // UK -> English
      'CN': 'date-desc|zh',  // China -> Simplified Chinese
      'TW': 'date-desc|hant', // Taiwan -> Traditional Chinese
      'HK': 'date-desc|hant', // Hong Kong -> Traditional Chinese
      'JP': 'date-desc|ja',  // Japan -> Japanese
      'ES': 'date-desc|es',  // Spain -> Spanish
      'MX': 'date-desc|es',  // Mexico -> Spanish (example for Latin America)
      'IN': 'date-desc|hi',  // India -> Hindi
      'FR': 'date-desc|fr',  // France -> French
      'DE': 'date-desc|de',  // Germany -> German
      'SA': 'date-desc|ar',  // Saudi Arabia -> Arabic
      'AE': 'date-desc|ar'   // UAE -> Arabic
    };

    sortSelect.value = countryLangMap[country] || 'date-desc|en'; // Default to English
  } catch (error) {
    console.warn('Country detection failed:', error);
    sortSelect.value = 'date-desc|en'; // Fallback
  }

  updatePosts();
}
```

-   **नोट्स**:
    -   `window.addEventListener` को `async function ()` में अपडेट करें जैसा कि दिखाया गया है।
    -   गोपनीयता के लिए: यदि आवश्यक हो तो उपयोगकर्ताओं को सूचित करें (EU में GDPR)। कुछ ब्राउज़र/APIs क्रॉस-ओरिजिन रिक्वेस्ट्स को ब्लॉक कर सकते हैं; अच्छी तरह से टेस्ट करें।
    -   यदि आप कोई अलग API पसंद करते हैं, तो विकल्पों में `https://ip-api.com/json/` (अधिक डेटा लौटाता है जैसे `{ "countryCode": "US" }`) या `https://ipgeolocation.io/ip_location/` (फ्री टियर के लिए साइन अप करें) शामिल हैं।
    -   रेट लिमिट: ये व्यक्तिगत ब्लॉग्स के लिए उदार हैं, लेकिन यदि ट्रैफ़िक बढ़ता है तो निगरानी करें।

#### अतिरिक्त विचार
-   **फॉलबैक और उपयोगकर्ता ओवरराइड**: उपयोगकर्ता हमेशा ड्रॉपडाउन बदल सकते हैं, और यह localStorage में सेव हो जाता है। यदि ऑटो-डिटेक्शन हमेशा वांछित नहीं है तो आप एक "Detect Language" बटन जोड़ सकते हैं।
-   **टेस्टिंग**: विभिन्न देशों का अनुकरण करने के लिए VPNs का उपयोग करें या भाषाओं को स्पूफ करने के लिए ब्राउज़र एक्सटेंशन का उपयोग करें।
-   **गोपनीयता**: ब्राउज़र भाषा कम जोखिम वाली है। IP विधियों के लिए, यदि आपका दर्शक संवेदनशील है तो एक सहमति प्रॉम्प्ट जोड़ने पर विचार करें।
-   **दोनों को संयोजित करना**: पहले ब्राउज़र भाषा का उपयोग करें, फिर IP यदि यह आपके समर्थित लोगों से मेल नहीं खाती (लेकिन इसे सरल रखें)।
-   **Jekyll-विशिष्ट**: Jekyll config में कोई बदलाव की आवश्यकता नहीं है। यदि आप Netlify/Vercel पर होस्ट करते हैं, तो आप सर्वर-साइड डिटेक्शन के लिए edge functions का उपयोग कर सकते हैं, लेकिन यहां यह अति-परिश्रम है।

यदि यह काम नहीं करता है या आप त्रुटियां साझा कर सकते हैं, तो अधिक विवरण प्रदान करें!

[Country.is API](https://country.is/)  
[IP-API Geolocation](https://ip-api.com/)  
[ipgeolocation.io](https://ipgeolocation.io/)