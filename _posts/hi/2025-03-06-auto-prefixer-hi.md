---
audio: false
generated: true
lang: hi
layout: post
title: ऑटोप्रीफ़िक्सर का उपयोग
translated: true
type: note
---

मैं फ्रंटएंड डेवलपमेंट में Autoprefixer के उपयोग के बारे में समझाऊंगा। Autoprefixer एक PostCSS प्लगइन है जो आपके CSS में स्वचालित रूप से वेंडर प्रीफिक्स जोड़ता है, जिससे क्रॉस-ब्राउज़र कंपैटिबिलिटी सुनिश्चित होती है।

यहां Autoprefixer को अपने फ्रंटएंड वर्कफ़्लो में शामिल करने के मुख्य तरीके दिए गए हैं:

1. npm के साथ उपयोग करना (सबसे आम तरीका)
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

b) Vite (बिल्ट-इन सपोर्ट)
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

4. कॉन्फ़िगरेशन विकल्प
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer')({
      overrideBrowserslist: ['> 1%', 'last 2 versions'], // टार्गेट ब्राउज़र
      grid: true, // ग्रिड प्रीफिक्स सक्षम करें
      flexbox: 'no-2009' // फ्लेक्सबॉक्स सपोर्ट विकल्प
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
- Can I Use डेटा के आधार पर स्वचालित रूप से प्रीफिक्स जोड़ता है
- browserslist द्वारा नियंत्रित (आमतौर पर package.json में)
- पुराने CSS से अप्रचलित प्रीफिक्स हटाता है
- कस्टम प्रॉपर्टीज जैसी आधुनिक CSS फीचर्स के साथ काम करता है

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

# या अपनी npm स्क्रिप्ट के साथ
npm run build:css
```

अपने प्रोजेक्ट के मौजूदा सेटअप (Webpack, Vite, आदि) के आधार पर इंटीग्रेशन विधि चुनें। आधुनिक फ्रंटएंड डेवलपमेंट में Webpack या Vite तरीके सबसे आम हैं क्योंकि ये मौजूदा बिल्ड प्रक्रियाओं के साथ अच्छी तरह से एकीकृत होते हैं।