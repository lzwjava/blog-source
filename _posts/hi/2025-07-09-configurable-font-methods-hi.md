---
audio: false
generated: true
lang: hi
layout: post
title: लेटेक्स में विन्यास योग्य फ़ॉन्ट्स
translated: true
type: note
---

आप LaTeX दस्तावेज़ के शीर्ष पर चर बनाकर फ़ॉन्ट को विन्यास योग्य बना सकते हैं। यहां कुछ तरीके दिए गए हैं:

## Method 1: Simple Variables (Recommended)
## Method 2: Using conditionals for different systems
मैं स्वचालित OS डिटेक्शन के साथ एक और अधिक उन्नत संस्करण बनाता हूं:
## Method 3: Using separate configuration file

आप फ़ॉन्ट कॉन्फ़िगरेशन के लिए एक अलग फ़ाइल भी बना सकते हैं:
और फिर अपने मुख्य दस्तावेज़ में:
## Common Linux Font Alternatives

यहां Linux सिस्टम के लिए कुछ अच्छे फ़ॉन्ट विकल्प दिए गए हैं:

**चीनी/CJK फ़ॉन्ट्स के लिए:**
- `Noto Sans CJK SC` (recommended)
- `Source Han Sans SC`
- `WenQuanYi Micro Hei`
- `Droid Sans Fallback`

**अंग्रेजी फ़ॉन्ट्स के लिए:**
- `Liberation Serif` (Times New Roman alternative)
- `DejaVu Serif`
- `Linux Libertine`
- `TeX Gyre Termes`

## Usage

1. **Method 1** सबसे सरल है - जरूरत पड़ने पर बस Linux फ़ॉन्ट लाइनों को अनकमेंट करें
2. **Method 2** आपको विभिन्न सिस्टमों के बीच स्विच करने के लिए सिर्फ एक चर (`\fontsystem`) बदलने की अनुमति देता है
3. **Method 3** फ़ॉन्ट कॉन्फ़िगरेशन को अलग रखता है, जिससे विभिन्न संस्करणों को बनाए रखना आसान हो जाता है

वह तरीका चुनें जो आपके वर्कफ़्लो के लिए सबसे उपयुक्त हो!