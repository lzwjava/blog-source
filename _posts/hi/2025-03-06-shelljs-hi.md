---
audio: false
generated: true
lang: hi
layout: post
title: शेलजेएस का उपयोग करके शेल कमांड निष्पादित करना
translated: true
type: note
---

ShellJS एक JavaScript लाइब्रेरी है जो Node.js प्रोजेक्ट्स में उपयोग के लिए Unix शेल कमांड्स (जैसे `cp`, `mkdir`, `exec`, आदि) प्रदान करती है। यह cross-platform स्क्रिप्ट्स लिखने को सरल बनाती है, जिससे आप JavaScript में सीधे परिचित शेल कमांड्स execute कर सकते हैं। हालाँकि, जब frontend development की बात आती है—जो आमतौर पर ब्राउज़र में चलने वाले कोड को संदर्भित करती है—तो ShellJS सीधे लागू नहीं होती क्योंकि यह Node.js APIs पर निर्भर करती है जो ब्राउज़र environment में उपलब्ध नहीं हैं। नीचे, मैं समझाऊंगा कि ऐसा क्यों है और आप frontend development workflows के संदर्भ में ShellJS का प्रभावी ढंग से उपयोग कैसे कर सकते हैं।

### ShellJS सीधे ब्राउज़र में क्यों नहीं चल सकती
- **Node.js डिपेंडेंसी**: ShellJS Node.js रनटाइम के ऊपर बनी है, जो file system access, process execution, और अन्य system-level operations के लिए APIs प्रदान करता है। ये APIs ब्राउज़र में उसके sandboxed सुरक्षा मॉडल के कारण उपलब्ध नहीं हैं।
- **ब्राउज़र सुरक्षा प्रतिबंध**: ब्राउज़र JavaScript को local file system तक पहुँचने या मनमाने commands execute करने से रोकते हैं ताकि users को दुर्भावनापूर्ण स्क्रिप्ट्स से बचाया जा सके। चूंकि ShellJS commands जैसे `exec` (बाहरी प्रक्रियाएं चलाने के लिए) या `cp` (फ़ाइलों को कॉपी करने के लिए) इन क्षमताओं पर निर्भर करती हैं, वे ब्राउज़र environment में कार्य नहीं कर सकतीं।

परिणामस्वरूप, आप ब्राउज़र में चलने वाले client-side JavaScript में ShellJS का सीधे उपयोग नहीं कर सकते। हालाँकि, ShellJS आपकी build processes या development tools में इसे एकीकृत करके frontend development में अभी भी एक मूल्यवान भूमिका निभा सकती है, जो आमतौर पर Node.js पर चलती हैं।

### Frontend Development Workflows में ShellJS का उपयोग कैसे करें
हालांकि ShellJS ब्राउज़र में execute नहीं होती, आप अपने frontend development का समर्थन करने वाले tasks को automate करने के लिए Node.js-आधारित स्क्रिप्ट्स में इसका लाभ उठा सकते हैं। Frontend प्रोजेक्ट्स अक्सर Webpack, Gulp, या Grunt जैसे build tools पर निर्भर करते हैं, जो Node.js पर चलते हैं और workflows को सुव्यवस्थित करने के लिए ShellJS को शामिल कर सकते हैं। यहाँ बताया गया है कि इसे कैसे करें:

#### 1. ShellJS इंस्टॉल करें
सबसे पहले, सुनिश्चित करें कि आपके सिस्टम पर Node.js इंस्टॉल है। फिर, npm या yarn का उपयोग करके ShellJS को अपने प्रोजेक्ट में जोड़ें:

```bash
npm install shelljs
```

या

```bash
yarn add shelljs
```

#### 2. ShellJS के साथ एक Node.js स्क्रिप्ट बनाएँ
एक स्क्रिप्ट लिखें जो ShellJS का उपयोग आपके frontend प्रोजेक्ट से संबंधित कार्यों को करने के लिए करती है, जैसे फ़ाइलों को कॉपी करना, निर्देशिकाएँ बनाना, या command-line tools चलाना। इस स्क्रिप्ट को एक `.js` फ़ाइल (जैसे, `build.js`) के रूप में सहेजें।

यहाँ एक उदाहरण स्क्रिप्ट है जो frontend assets तैयार करती है:

```javascript
const shell = require('shelljs');

// एक build निर्देशिका बनाएँ यदि यह मौजूद नहीं है
shell.mkdir('-p', 'build');

// HTML फ़ाइलों को build निर्देशिका में कॉपी करें
shell.cp('-R', 'src/*.html', 'build/');

// Sass को CSS में compile करें
shell.exec('sass src/styles.scss build/styles.css');

// JavaScript फ़ाइलों को कॉपी करें
shell.cp('-R', 'src/*.js', 'build/');
```

- **`shell.mkdir('-p', 'build')`**: एक `build` निर्देशिका बनाता है, `-p` यह सुनिश्चित करता है कि यदि यह पहले से मौजूद है तो कोई error नहीं होगी।
- **`shell.cp('-R', 'src/*.html', 'build/')`**: `src` से सभी HTML फ़ाइलों को `build` में कॉपी करता है, `-R` recursive copying के लिए है।
- **`shell.exec('sass src/styles.scss build/styles.css')`**: CSS generate करने के लिए Sass compiler चलाता है।

#### 3. स्क्रिप्ट को अपने Workflow में एकीकृत करें
आप इस स्क्रिप्ट को कई तरीकों से चला सकते हैं:
- **सीधे Node.js के माध्यम से**:
  ```bash
  node build.js
  ```
- **एक npm स्क्रिप्ट के रूप में**: इसे अपने `package.json` में जोड़ें:
  ```json
  "scripts": {
    "build": "node build.js"
  }
  ```
  फिर चलाएँ:
  ```bash
  npm run build
  ```
- **Build Tools के साथ**: ShellJS को Gulp जैसे tools में शामिल करें। उदाहरण के लिए:
  ```javascript
  const gulp = require('gulp');
  const shell = require('shelljs');

  gulp.task('build', function(done) {
    shell.exec('sass src/styles.scss build/styles.css');
    shell.cp('-R', 'src/*.js', 'build/');
    done();
  });
  ```

#### 4. Frontend Development में उपयोग के मामले
ShellJS आपके frontend workflow में विभिन्न कार्यों को automate कर सकती है:
- **Asset Management**: images, fonts, या अन्य static files को एक build निर्देशिका में कॉपी करना।
- **CSS/JavaScript प्रोसेसिंग**: Sass, PostCSS, या UglifyJS जैसे tools को `shell.exec` के माध्यम से चलाना।
- **टेस्टिंग और लिंटिंग**: test runners या linters execute करना (जैसे, `shell.exec('eslint src/*.js')`)।
- **डेप्लॉयमेंट तैयारी**: फ़ाइलों को bundle करना या निर्देशिकाओं को साफ़ करना (जैसे, `shell.rm('-rf', 'build/*')`)।

### उदाहरण: एक Frontend Build प्रक्रिया को स्वचालित करना
कल्पना करें कि आप HTML, Sass, और JavaScript के साथ एक साधारण web app बना रहे हैं। यहाँ बताया गया है कि आप build को automate करने के लिए ShellJS का उपयोग कैसे कर सकते हैं:

**निर्देशिका संरचना**:
```
project/
├── src/
│   ├── index.html
│   ├── styles.scss
│   └── app.js
├── build.js
└── package.json
```

**build.js**:
```javascript
const shell = require('shelljs');

// build निर्देशिका साफ़ करें
shell.rm('-rf', 'build/*');

// build निर्देशिका बनाएँ
shell.mkdir('-p', 'build');

// HTML कॉपी करें
shell.cp('src/index.html', 'build/');

// Sass compile करें
shell.exec('sass src/styles.scss build/styles.css');

// JavaScript कॉपी करें
shell.cp('src/app.js', 'build/');
```

**package.json**:
```json
{
  "scripts": {
    "build": "node build.js"
  },
  "dependencies": {
    "shelljs": "^0.8.5"
  }
}
```

`npm run build` चलाएँ, और ShellJS compiled और copied files के साथ आपकी `build` निर्देशिका तैयार कर देगी, जो deployment के लिए तैयार है।

### मुख्य बातें
- **ब्राउज़र उपयोग के लिए नहीं**: ShellJS, Node.js और system-level operations पर अपनी निर्भरता के कारण ब्राउज़र में नहीं चल सकती।
- **Build स्क्रिप्ट्स के लिए परफेक्ट**: file manipulation और command execution जैसे frontend tasks को automate करने के लिए इसे Node.js-आधारित स्क्रिप्ट्स में उपयोग करें।
- **Cross-Platform**: ShellJS यह सुनिश्चित करती है कि आपकी स्क्रिप्ट्स Windows, Linux, और macOS में लगातार काम करें, जिससे यह विविध development environments के लिए आदर्श बनती है।

अपने Node.js-संचालित build processes में ShellJS को शामिल करके, आप शक्तिशाली automation के साथ अपने frontend development workflow को बढ़ा सकते हैं, भले ही यह सीधे ब्राउज़र में नहीं चलती।