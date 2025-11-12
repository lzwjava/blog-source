---
audio: false
generated: true
lang: hi
layout: post
title: एक साथ उपयोग करना
translated: true
type: note
---

ऐसा लगता है कि आप फ्रंटएंड डेवलपमेंट के संदर्भ में "concurrently" के उपयोग के बारे में पूछ रहे हैं। हालाँकि, "concurrently" आमतौर पर एक Node.js पैकेज है जिसका उपयोग एक साथ कई कमांड या स्क्रिप्ट चलाने के लिए किया जाता है, अक्सर बैकएंड या डेवलपमेंट वर्कफ़्लो के संदर्भ में, सीधे फ्रंटएंड कोड में नहीं। क्या आपका मतलब यह था कि इसे फ्रंटएंड प्रोजेक्ट सेटअप (जैसे, स्क्रिप्ट चलाना) में कैसे उपयोग करें, या आप कुछ और जैसे फ्रंटएंड JavaScript में concurrent ऑपरेशंस (जैसे, प्रॉमिसेज़, async/await) की बात कर रहे थे? अभी के लिए मैं पहले वाले को मानकर चलूंगा, लेकिन आप स्पष्ट करने के लिए स्वतंत्र हैं!

### फ्रंटएंड प्रोजेक्ट में `concurrently` का उपयोग

यदि आप किसी फ्रंटएंड प्रोजेक्ट (जैसे, React, Vue, या Angular) पर काम कर रहे हैं, तो `concurrently` का उपयोग आमतौर पर डेवलपमेंट में एक साथ कई प्रक्रियाएं चलाने के लिए किया जाता है—जैसे कि एक डेवलपमेंट सर्वर और एक बिल्ड वॉचर शुरू करना। यहां बताया गया है कि आप इसका उपयोग कैसे कर सकते हैं:

#### 1. `concurrently` इंस्टॉल करें
पहले, इसे अपने प्रोजेक्ट में एक dev डिपेंडेंसी के रूप में इंस्टॉल करें:
```bash
npm install --save-dev concurrently
```

#### 2. `package.json` में स्क्रिप्ट्स जोड़ें
अपनी `package.json` में वे स्क्रिप्ट्स परिभाषित करें जिन्हें आप एक साथ चलाना चाहते हैं। उदाहरण के लिए, यदि आप एक फ्रंटएंड डेव सर्वर और Sass जैसा CSS प्रीप्रोसेसर चला रहे हैं:
```json
{
  "scripts": {
    "start:frontend": "react-scripts start", // या आपका फ्रंटएंड डेव कमांड
    "watch:css": "sass --watch src/styles:dist/styles",
    "dev": "concurrently \"npm run start:frontend\" \"npm run watch:css\""
  }
}
```

- `start:frontend`: आपका फ्रंटएंड डेवलपमेंट सर्वर चलाता है (जैसे, React, Vite, आदि)।
- `watch:css`: आपकी CSS फ़ाइलों को देखता है और कंपाइल करता है।
- `dev`: `concurrently` का उपयोग करके दोनों कमांड्स को एक साथ चलाता है।

#### 3. Concurrent स्क्रिप्ट्स चलाएं
अपने टर्मिनल में, बस चलाएं:
```bash
npm run dev
```
यह फ्रंटएंड सर्वर और CSS वॉचर दोनों को एक साथ शुरू कर देगा। आपको दोनों प्रक्रियाओं का आउटपुट एक ही टर्मिनल में दिखाई देगा, और `concurrently` उन्हें एक साथ चलाए रखता है।

#### 4. वैकल्पिक कॉन्फ़िगरेशन
आप `concurrently` को विकल्पों के साथ अनुकूलित कर सकते हैं, जैसे:
- `--kill-others`: यदि एक प्रक्रिया विफल हो जाती है तो सभी प्रक्रियाओं को रोक देता है।
- `--names`: स्पष्ट आउटपुट के लिए प्रत्येक प्रक्रिया को लेबल करता है।

`package.json` में विकल्पों के साथ उदाहरण:
```json
"dev": "concurrently --names \"Frontend,CSS\" --kill-others \"npm run start:frontend\" \"npm run watch:css\""
```
आउटपुट कुछ ऐसा दिख सकता है:
```
[Frontend] Starting frontend server...
[CSS] Watching CSS files...
```

#### फ्रंटएंड वर्कफ़्लो में उपयोग का उदाहरण
कल्पना करें कि आप एक अलग API सर्वर के साथ एक React ऐप बना रहे हैं:
- फ्रंटएंड: `npm run start` (React डेव सर्वर पोर्ट 3000 पर)।
- API: `npm run start:api` (जैसे, Node.js सर्वर पोर्ट 5000 पर)।
`concurrently` के साथ, आप दोनों चला सकते हैं:
```json
"dev": "concurrently \"npm run start\" \"npm run start:api\""
```

### यदि आपका मतलब फ्रंटएंड में Concurrent JavaScript था
यदि आप फ्रंटएंड कोड में concurrent ऑपरेशंस को हैंडल करने (जैसे, एक साथ कई APIs फ़ेच करना) के बारे में पूछ रहे थे, तो यहाँ `Promise.all` का उपयोग करके एक त्वरित उदाहरण दिया गया है:
```javascript
async function fetchData() {
  const [userData, postsData] = await Promise.all([
    fetch('https://api.example.com/user').then(res => res.json()),
    fetch('https://api.example.com/posts').then(res => res.json())
  ]);
  console.log(userData, postsData);
}
fetchData();
```
यह API कॉल्स को concurrently चलाता है और दोनों के रिज़ॉल्व होने की प्रतीक्षा करता है।

### यदि आवश्यक हो तो स्पष्ट करें!
मुझे बताएं कि क्या आप "फ्रंटएंड में concurrently" से कुछ अलग मतलब रखते थे—जैसे कोई विशिष्ट लाइब्रेरी, फ़्रेमवर्क, या उपयोग का मामला—और मैं जवाब को और अनुकूलित कर दूंगा!