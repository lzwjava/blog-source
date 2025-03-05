---
audio: false
generated: true
lang: hi
layout: post
title: PostCSS के उपयोग से CSS को बदलना
translated: true
---

मैं आपको बताऊंगा कि कैसे एक फ्रंटएंड प्रोजेक्ट में PostCSS का उपयोग करें। PostCSS एक टूल है जो JavaScript प्लगइन्स के साथ CSS को ट्रांसफॉर्म करने के लिए है, जो ऑटोप्रिफिक्सिंग, मिनिफिकेशन और फ्यूचर CSS सिंटैक्स सपोर्ट जैसी सुविधाएं प्रदान करता है। यहाँ एक स्टेप-बाय-स्टेप गाइड है:

### 1. **प्रोजेक्ट सेट अप करें**
यदि आपके पास Node.js के साथ एक फ्रंटएंड प्रोजेक्ट नहीं है, तो एक प्रोजेक्ट को इनिशियलाइज़ करें:
```bash
mkdir my-project
cd my-project
npm init -y
```

### 2. **PostCSS और आवश्यक टूल्स इंस्टॉल करें**
PostCSS, PostCSS CLI और आप चाहें तो किसी भी प्लगइन्स को इंस्टॉल करें (जैसे कि `autoprefixer` वेंडर प्रिफिक्स के लिए या `cssnano` मिनिफिकेशन के लिए):
```bash
npm install --save-dev postcss postcss-cli autoprefixer cssnano
```

### 3. **एक CSS फ़ाइल बनाएं**
एक स्रोत CSS फ़ाइल बनाएं, उदाहरण के लिए, `src/styles.css`:
```css
/* src/styles.css */
.container {
  display: flex;
  transition: all 0.3s ease;
}
```

### 4. **PostCSS को कॉन्फ़िगर करें**
प्रोजेक्ट रूट में एक `postcss.config.js` फ़ाइल बनाएं ताकि प्लगइन्स को स्पेसिफाई किया जा सके:
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'), // वेंडर प्रिफिक्स जोड़ता है
    require('cssnano')({ preset: 'default' }) // CSS को मिनिफाई करता है
  ]
};
```

### 5. **एक बिल्ड स्क्रिप्ट जोड़ें**
अपने `package.json` में एक स्क्रिप्ट जोड़ें ताकि PostCSS के साथ CSS को प्रोसेस किया जा सके:
```json
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```
- `src/styles.css`: इनपुट फ़ाइल
- `dist/styles.css`: आउटपुट फ़ाइल

### 6. **PostCSS चलाएं**
बिल्ड कमांड चलाएं:
```bash
npm run build:css
```
यह `src/styles.css` को प्रोसेस करता है और ट्रांसफॉर्म्ड CSS को `dist/styles.css` में आउटपुट करता है। उदाहरण के लिए, `autoprefixer` प्रिफिक्स जोड़ सकता है और `cssnano` इसे मिनिफाई कर सकता है:
```css
/* dist/styles.css */
.container{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-transition:all .3s ease;transition:all .3s ease}
```

### 7. **एक बिल्ड टूल के साथ इंटिग्रेट करें (ऑप्शनल)**
एक अधिक रॉबस्ट सेटअप के लिए, PostCSS को Webpack, Vite या Gulp जैसी टूल्स के साथ इंटिग्रेट करें:

#### **Vite के साथ**
Vite का उपयोग करते हुए, `postcss` को इंस्टॉल करें और `vite.config.js` में कॉन्फ़िगर करें:
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
Vite CSS फ़ाइलें इम्पोर्ट करने पर PostCSS को स्वचालित रूप से हैंडल करता है।

#### **Webpack के साथ**
`postcss-loader` को इंस्टॉल करें:
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

### 8. **परिवर्तन के लिए वॉच करें (ऑप्शनल)**
विकास के दौरान CSS को स्वचालित रूप से प्रोसेस करने के लिए, अपने `package.json` स्क्रिप्ट को संशोधित करें:
```json
"scripts": {
  "watch:css": "postcss src/styles.css -o dist/styles.css --watch"
}
```
`npm run watch:css` चलाएं ताकि फ़ाइल परिवर्तन के लिए वॉच किया जा सके।

### 9. **सामान्य प्लगइन्स**
यहाँ कुछ लोकप्रिय PostCSS प्लगइन्स हैं:
- `autoprefixer`: ब्राउज़र सपोर्ट के आधार पर वेंडर प्रिफिक्स जोड़ता है।
- `cssnano`: CSS को मिनिफाई करता है।
- `postcss-preset-env`: आज ही भविष्य के CSS फीचर्स का उपयोग करने देता है।
- `postcss-import`: `@import` रूल्स को रिज़ॉल्व करता है।
उनको आवश्यकता के अनुसार इंस्टॉल करें:
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
2. `npm run build:css` चलाएं।
3. `dist/styles.css` में प्रोसेस्ड CSS प्राप्त करें जिसमें प्रिफिक्स, रिज़ॉल्व्ड वेरिएबल्स और मिनिफिकेशन शामिल हैं।

### टिप्स
- CLI में `--map` का उपयोग करें (`postcss src/styles.css -o dist/styles.css --map`) ताकि डिबगिंग के लिए स्रोत मैप्स जनरेट करें।
- प्लगइन्स के डॉक्यूमेंटेशन को चेक करें ताकि विशेष कॉन्फ़िगरेशन ऑप्शन्स के लिए।
- एक फ्रंटएंड फ्रेमवर्क (React, Vue, आदि) के साथ संयोजित करें ताकि आउटपुट CSS को आपकी HTML या बंडलर से लिंक किया जा सके।

मुझे किसी विशेष सेटअप या प्लगइन के साथ मदद की जरूरत हो तो मुझे बताएं!