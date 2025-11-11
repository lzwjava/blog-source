---
audio: false
generated: true
lang: hi
layout: post
title: पोस्टसीएसएस का उपयोग करके सीएसएस का रूपांतरण
translated: true
type: note
---

मैं एक फ्रंटएंड प्रोजेक्ट में PostCSS का उपयोग कैसे करूं, इसके बारे में समझाऊंगा। PostCSS, JavaScript प्लगइन्स के साथ CSS को रूपांतरित करने का एक टूल है, जो ऑटोप्रीफिक्सिंग, मिनिफिकेशन और भविष्य की CSS सिंटैक्स सपोर्ट जैसी सुविधाएँ प्रदान करता है। यहाँ एक चरण-दर-चरण मार्गदर्शिका दी गई है:

### 1. **अपना प्रोजेक्ट सेट अप करें**
सुनिश्चित करें कि आपके पास Node.js इंस्टॉल किया हुआ एक फ्रंटएंड प्रोजेक्ट है। यदि नहीं है, तो एक प्रारंभ करें:
```bash
mkdir my-project
cd my-project
npm init -y
```

### 2. **PostCSS और आवश्यक टूल्स इंस्टॉल करें**
PostCSS, PostCSS CLI, और कोई भी प्लगइन जिसका आप उपयोग करना चाहते हैं (जैसे वेंडर प्रीफिक्स के लिए `autoprefixer` या मिनिफिकेशन के लिए `cssnano`) इंस्टॉल करें:
```bash
npm install --save-dev postcss postcss-cli autoprefixer cssnano
```

### 3. **एक CSS फ़ाइल बनाएँ**
एक स्रोत CSS फ़ाइल बनाएँ, उदाहरण के लिए, `src/styles.css`:
```css
/* src/styles.css */
.container {
  display: flex;
  transition: all 0.3s ease;
}
```

### 4. **PostCSS कॉन्फ़िगर करें**
प्लगइन्स निर्दिष्ट करने के लिए अपने प्रोजेक्ट रूट में एक `postcss.config.js` फ़ाइल बनाएँ:
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'), // वेंडर प्रीफिक्स जोड़ता है
    require('cssnano')({ preset: 'default' }) // CSS को मिनिफाई करता है
  ]
};
```

### 5. **एक बिल्ड स्क्रिप्ट जोड़ें**
अपने `package.json` में, PostCSS के साथ अपनी CSS को प्रोसेस करने के लिए एक स्क्रिप्ट जोड़ें:
```json
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```
- `src/styles.css`: इनपुट फ़ाइल
- `dist/styles.css`: आउटपुट फ़ाइल

### 6. **PostCSS चलाएँ**
बिल्ड कमांड चलाएँ:
```bash
npm run build:css
```
यह `src/styles.css` को प्रोसेस करता है और रूपांतरित CSS को `dist/styles.css` में आउटपुट करता है। उदाहरण के लिए, `autoprefixer` प्रीफिक्स जोड़ सकता है, और `cssnano` इसे मिनिफाई करेगा:
```css
/* dist/styles.css */
.container{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-transition:all .3s ease;transition:all .3s ease}
```

### 7. **एक बिल्ड टूल के साथ एकीकृत करें (वैकल्पिक)**
अधिक मजबूत सेटअप के लिए, PostCSS को Webpack, Vite, या Gulp जैसे टूल्स के साथ एकीकृत करें:

#### **Vite के साथ**
यदि Vite का उपयोग कर रहे हैं, तो `postcss` इंस्टॉल करें और इसे `vite.config.js` में कॉन्फ़िगर करें:
```javascript
// vite.config.js
import postcss from 'postcss';
import autoprefixer from 'autoprefixer';

export default {
  css: {
    postcss: {
      plugins: [autoprefixer()]
    }
  }
};
```
जब आप CSS फ़ाइलों को इम्पोर्ट करते हैं तो Vite स्वचालित रूप से PostCSS को हैंडल करता है।

#### **Webpack के साथ**
`postcss-loader` इंस्टॉल करें:
```bash
npm install --save-dev postcss-loader
```
अपने `webpack.config.js` को अपडेट करें:
```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader', 'postcss-loader']
      }
    ]
  }
};
```

### 8. **परिवर्तनों के लिए वॉच करें (वैकल्पिक)**
डेवलपमेंट के दौरान CSS को स्वचालित रूप से प्रोसेस करने के लिए, अपनी `package.json` स्क्रिप्ट को संशोधित करें:
```json
"scripts": {
  "watch:css": "postcss src/styles.css -o dist/styles.css --watch"
}
```
फ़ाइल परिवर्तनों को वॉच करने के लिए `npm run watch:css` चलाएँ।

### 9. **सामान्य प्लगइन्स**
यहाँ कुछ लोकप्रिय PostCSS प्लगइन्स दिए गए हैं:
- `autoprefixer`: ब्राउज़र सपोर्ट के आधार पर वेंडर प्रीफिक्स जोड़ता है।
- `cssnano`: CSS को मिनिफाई करता है।
- `postcss-preset-env`: आपको आज ही भविष्य की CSS सुविधाओं का उपयोग करने देता है।
- `postcss-import`: `@import` नियमों को रिज़ॉल्व करता है।
आवश्यकतानुसार उन्हें इंस्टॉल करें:
```bash
npm install --save-dev postcss-preset-env postcss-import
```
उन्हें `postcss.config.js` में जोड़ें:
```javascript
module.exports = {
  plugins: [
    require('postcss-import'),
    require('postcss-preset-env'),
    require('autoprefixer'),
    require('cssnano')({ preset: 'default' })
  ]
};
```

### उदाहरण वर्कफ़्लो
1. `src/styles.css` में आधुनिक CSS लिखें:
```css
@custom-media --viewport-medium (width >= 768px);

:root {
  --main-color: #1a73e8;
}

.container {
  color: var(--main-color);
  display: grid;
}

@media (--viewport-medium) {
  .container {
    grid-template-columns: 1fr 1fr;
  }
}
```
2. `npm run build:css` चलाएँ।
3. प्रीफिक्स, रिज़ॉल्व्ड वेरिएबल्स और मिनिफिकेशन के साथ `dist/styles.css` में प्रोसेस्ड CSS प्राप्त करें।

### सुझाव
- डीबगिंग के लिए सोर्स मैप जनरेट करने के लिए CLI में `--map` का उपयोग करें (`postcss src/styles.css -o dist/styles.css --map`)।
- विशिष्ट कॉन्फ़िगरेशन विकल्पों के लिए प्लगइन डॉक्स चेक करें।
- आउटपुट CSS को अपने HTML या बंडलर से लिंक करके एक फ्रंटएंड फ्रेमवर्क (React, Vue, आदि) के साथ संयोजित करें।

यदि आपको किसी विशिष्ट सेटअप या प्लगइन में सहायता की आवश्यकता है, तो मुझे बताएं!