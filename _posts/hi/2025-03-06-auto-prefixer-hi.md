---
audio: false
generated: true
lang: hi
layout: post
title: Autoprefixer का उपयोग
translated: true
---

मैं Autoprefixer का उपयोग करने की व्याख्या करूँगा, जो एक PostCSS प्लगइन है जो आपके CSS में वेंडर प्रिफिक्स को स्वचालित रूप से जोड़ता है, जिससे क्रॉस-ब्राउज़र संगतता सुनिश्चित होती है।

Autoprefixer को अपने फ्रंटएंड वर्कफ्लो में एकीकृत करने के मुख्य तरीके हैं:

1. npm के साथ उपयोग (सबसे आम तरीका)
```bash
# autoprefixer और postcss इंस्टॉल करें
npm install autoprefixer postcss --save-dev
```

2. PostCSS CLI के साथ बेसिक सेटअप
```bash
# postcss-cli इंस्टॉल करें
npm install postcss-cli --save-dev

# एक postcss.config.js फ़ाइल बनाएं
module.exports = {
  plugins: [
    require('autoprefixer')
  ]
}

# package.json स्क्रिप्ट्स में जोड़ें
"scripts": {
  "build:css": "postcss src/styles.css -o dist/styles.css"
}
```

3. बिल्ड टूल्स के साथ:

a) Webpack के साथ postcss-loader
```bash
npm install postcss-loader --save-dev
```

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader',
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: ['autoprefixer']
              }
            }
          }
        ]
      }
    ]
  }
}
```

b) Vite (बिल्ट-इन समर्थन)
```javascript
// vite.config.js
import autoprefixer from 'autoprefixer'

export default {
  css: {
    postcss: {
      plugins: [autoprefixer()]
    }
  }
}
```

4. कॉन्फ़िगरेशन ऑप्शंस
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer')({
      overrideBrowserslist: ['> 1%', 'last 2 versions'], // ब्राउज़र लक्ष्य
      grid: true, // ग्रिड प्रिफिक्स को सक्षम करें
      flexbox: 'no-2009' // फ्लेक्सबॉक्स समर्थन विकल्प
    })
  ]
}
```

5. CSS में उदाहरण उपयोग
```css
/* इनपुट */
.container {
  display: flex;
  justify-content: space-between;
}

/* आउटपुट (Autoprefixer के बाद) */
.container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
```

मुख्य विशेषताएं और टिप्स:
- Can I Use डेटा के आधार पर स्वचालित रूप से प्रिफिक्स जोड़ता है
- browserslist द्वारा नियंत्रित (आम तौर पर package.json में)
- पुराने CSS से अपडेटेड प्रिफिक्स को हटाता है
- कस्टम प्रॉपर्टीज जैसे आधुनिक CSS विशेषताओं के साथ काम करता है

package.json में बेसिक browserslist उदाहरण:
```json
{
  "browserslist": [
    "> 1%",
    "last 2 versions",
    "not dead"
  ]
}
```

चलाने के लिए:
```bash
# PostCSS CLI के साथ
npx postcss src/*.css --dir dist

# या अपने npm स्क्रिप्ट के साथ
npm run build:css
```

अपने प्रोजेक्ट के मौजूदा सेटअप (Webpack, Vite आदि) के आधार पर एकीकृत करने का तरीका चुनें। Webpack या Vite तरीके आधुनिक फ्रंटएंड विकास में सबसे आम हैं क्योंकि वे मौजूदा बिल्ड प्रक्रियाओं के साथ अच्छी तरह से एकीकृत होते हैं।