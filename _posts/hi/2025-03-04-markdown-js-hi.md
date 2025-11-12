---
audio: false
generated: true
lang: hi
layout: post
title: मार्कडाउन के लिए जावास्क्रिप्ट लाइब्रेरी
translated: true
type: note
---

ऐसा लगता है कि आप `marked` लाइब्रेरी, वर्जन `^0.3.6` के उपयोग के बारे में पूछ रहे हैं, जो Markdown टेक्स्ट को पार्स करके HTML में बदलने के लिए एक JavaScript लाइब्रेरी है। चूंकि आप `^0.3.6` नोटेशन (संभवतः एक Node.js प्रोजेक्ट की `package.json` फ़ाइल से) के साथ एक विशिष्ट वर्जन का जिक्र कर रहे हैं, मैं आपको इस `marked` के पुराने वर्जन का उपयोग करने के तरीके के बारे में बताऊंगा। ध्यान दें कि वर्जन `0.3.6` काफी पुराना है (लगभग 2016 में रिलीज़ हुआ), और तब से यह लाइब्रेरी काफी विकसित हो चुकी है। हालाँकि, मैं उसी के अनुसार चलूंगा जो उस वर्जन के लिए काम करता है।

### चरण 1: इंस्टालेशन
यदि आप Node.js वातावरण में काम कर रहे हैं, तो आप npm का उपयोग करके `marked` वर्जन `0.3.6` इंस्टॉल कर सकते हैं:

```bash
npm install marked@0.3.6
```

`package.json` में `^0.3.6` का मतलब है कि यह `0.3.6` या कोई भी संगत पैच अपडेट (जैसे, `0.3.7`) इंस्टॉल करेगा, लेकिन स्पष्टता के लिए, उपरोक्त कमांड इसे सटीक `0.3.6` पर लॉक कर देती है।

### चरण 2: बेसिक उपयोग
यहां बताया गया है कि `marked` वर्जन `0.3.6` को विभिन्न वातावरणों में कैसे उपयोग करें:

#### Node.js में
1. **लाइब्रेरी को require करें**:
   एक फ़ाइल (जैसे, `index.js`) बनाएं और निम्नलिखित जोड़ें:

   ```javascript
   var marked = require('marked');
   ```

2. **Markdown को HTML में बदलें**:
   एक Markdown स्ट्रिंग पास करके `marked()` फ़ंक्शन का उपयोग करें। उदाहरण के लिए:

   ```javascript
   var markdownString = '# Hello World\nThis is **bold** text.';
   var html = marked(markdownString);
   console.log(html);
   ```

   **आउटपुट**:
   ```html
   <h1>Hello World</h1>
   <p>This is <strong>bold</strong> text.</p>
   ```

#### ब्राउज़र में
1. **लाइब्रेरी को शामिल करें**:
   आप एक CDN का उपयोग कर सकते हैं या `marked@0.3.6` डाउनलोड करके इसे `<script>` टैग के माध्यम से शामिल कर सकते हैं। उदाहरण के लिए, एक ऐतिहासिक CDN लिंक (यदि उपलब्ध हो) या स्थानीय फ़ाइल का उपयोग करना:

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **JavaScript में इसका उपयोग करें**:
   स्क्रिप्ट को शामिल करने के बाद, `marked` ग्लोबली उपलब्ध होगा:

   ```html
   <script>
     var markdownString = '# Hello World\nThis is **bold** text.';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### चरण 3: विकल्प (वर्जन 0.3.6 के लिए)
वर्जन `0.3.6` कुछ कस्टमाइज़ेशन विकल्पों को सपोर्ट करता है। आप `marked()` के दूसरे आर्ग्युमेंट के रूप में एक ऑप्शन ऑब्जेक्ट पास कर सकते हैं। यहाँ एक उदाहरण है:

```javascript
var markdownString = '# Hello\nThis is *text* with `code`.';
var html = marked(markdownString, {
  gfm: true,         // GitHub Flavored Markdown सक्षम करें
  tables: true,      // GFM टेबल्स सक्षम करें
  breaks: false,     // यदि true है, तो सिंगल लाइन ब्रेक पर <br> जोड़ता है
  pedantic: false,   // यदि true है, तो सख्त Markdown स्पेक का पालन करता है
  sanitize: false,   // यदि true है, तो सुरक्षा के लिए HTML टैग्स हटा देता है
  smartLists: true,  // लिस्ट रेंडरिंग में सुधार करता है
  smartypants: false // यदि true है, तो "स्मार्ट" टाइपोग्राफी (जैसे, कर्ली कोट्स) का उपयोग करता है
});
console.log(html);
```

### 0.3.6 में मुख्य विशेषताएं
- **बेसिक Markdown**: हेडिंग (`#`), बोल्ड (`**`), इटैलिक (`*`), लिस्ट्स, कोड ब्लॉक्स (```), आदि को सपोर्ट करता है।
- **GFM सपोर्ट**: GitHub Flavored Markdown (जैसे टेबल्स और टास्क लिस्ट्स) उपलब्ध है यदि `gfm: true` सेट किया गया है।
- **रेंडरर कस्टमाइज़ेशन नहीं**: नए वर्जन के विपरीत, `0.3.6` कस्टम रेंडरर को सपोर्ट नहीं करता है, इसलिए आप इसके डिफ़ॉल्ट आउटपुट तक सीमित हैं।

### अधिक Markdown के साथ उदाहरण
यहाँ Node.js में एक पूर्ण उदाहरण है:

```javascript
var marked = require('marked');

var markdown = `
# My Title
## Subtitle

- Item 1
- Item 2

\`\`\`
console.log("Hello");
\`\`\`

| Name  | Age |
|-------|-----|
| Alice | 25  |
| Bob   | 30  |
`;

var html = marked(markdown, { gfm: true, tables: true });
console.log(html);
```

**आउटपुट**:
```html
<h1>My Title</h1>
<h2>Subtitle</h2>
<ul>
<li>Item 1</li>
<li>Item 2</li>
</ul>
<pre><code>console.log("Hello");
</code></pre>
<table>
<thead>
<tr>
<th>Name</th>
<th>Age</th>
</tr>
</thead>
<tbody>
<tr>
<td>Alice</td>
<td>25</td>
</tr>
<tr>
<td>Bob</td>
<td>30</td>
</tr>
</tbody>
</table>
```

### नोट्स
- **सैनिटाइज़ेशन**: यदि आप यूजर इनपुट रेंडर कर रहे हैं, तो सुरक्षा के लिए रॉ HTML (जैसे, `<script>` टैग्स) को हटाने के लिए `sanitize: true` सेट करें। हालाँकि, यह `0.3.6` में बेसिक है और आधुनिक विकल्पों जितना मजबूत नहीं है।
- **सीमाएँ**: इस वर्जन में बाद के रिलीज़ में जोड़ी गई विशेषताओं (जैसे, async पार्सिंग, कस्टम टोकनाइज़र) का अभाव है, इसलिए यदि आपको अधिक की आवश्यकता है, तो `5.x` जैसे नए वर्जन में अपग्रेड करने पर विचार करें।
- **डीबगिंग**: यदि यह काम नहीं कर रहा है, तो सुनिश्चित करें कि लाइब्रेरी सही तरीके से लोड हो गई है और Markdown सिंटैक्स की जाँच करें।