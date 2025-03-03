---
audio: false
generated: true
lang: hi
layout: post
title: Markdown के लिए JavaScript लाइब्रेरी
translated: true
---

यह लगता है कि आप `marked` लाइब्रेरी, वर्जन `^0.3.6` के बारे में पूछ रहे हैं, जो एक JavaScript लाइब्रेरी है जो Markdown पाठ को HTML में परिवर्तित करने के लिए है। क्योंकि आप एक विशेष वर्जन को संदर्भित कर रहे हैं `^0.3.6` (शायद एक `package.json` फ़ाइल से एक Node.js प्रोजेक्ट में), मैं आपको इस पुराने वर्जन का उपयोग करने में मार्गदर्शन करूँगा। ध्यान रखें कि वर्जन `0.3.6` काफी पुराना है (लगभग 2016 में जारी किया गया था), और लाइब्रेरी तब से काफी विकसित हो गई है। फिर भी, मैं उस पर ध्यान केंद्रित करूँगा जो उस वर्जन के लिए काम करता है।

### चरण 1: इंस्टॉलेशन
अगर आप एक Node.js वातावरण में काम कर रहे हैं, तो आप `marked` वर्जन `0.3.6` का उपयोग कर सकते हैं:

```bash
npm install marked@0.3.6
```

एक `package.json` में `^0.3.6` का मतलब है कि यह `0.3.6` या किसी भी संगत पैच अपडेट (जैसे `0.3.7`) को इंस्टॉल करेगा, लेकिन स्पष्टता के लिए, ऊपर दिए गए कमांड को ठीक `0.3.6` पर लॉक करता है।

### चरण 2: बुनियादी उपयोग
यहाँ `marked` वर्जन `0.3.6` का उपयोग करने के तरीके हैं:

#### Node.js में
1. **लाइब्रेरी को आवश्यक बनाएं**:
   एक फ़ाइल बनाएं (जैसे `index.js`) और नीचे दिए गए कोड को जोड़ें:

   ```javascript
   var marked = require('marked');
   ```

2. **Markdown को HTML में परिवर्तित करें**:
   `marked()` फ़ंक्शन का उपयोग करके एक Markdown स्ट्रिंग को पास करें। उदाहरण के लिए:

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
   आप एक CDN का उपयोग कर सकते हैं या `marked@0.3.6` डाउनलोड कर सकते हैं और इसे एक `<script>` टैग के माध्यम से शामिल कर सकते हैं। उदाहरण के लिए, एक ऐतिहासिक CDN लिंक (यदि उपलब्ध है) या एक स्थानीय फ़ाइल का उपयोग करके:

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **इसका उपयोग JavaScript में करें**:
   स्क्रिप्ट को शामिल करने के बाद, `marked` ग्लोबल रूप से उपलब्ध होगा:

   ```html
   <script>
     var markdownString = '# Hello World\nThis is **bold** text.';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### चरण 3: विकल्प (वर्जन 0.3.6 के लिए)
वर्जन `0.3.6` कुछ अनुकूलन विकल्पों का समर्थन करता है। आप `marked()` के दूसरे अर्ग्युमेंट के रूप में एक विकल्प ऑब्जेक्ट को पास कर सकते हैं। यहाँ एक उदाहरण है:

```javascript
var markdownString = '# Hello\nThis is *text* with `code`.';
var html = marked(markdownString, {
  gfm: true,         // GitHub Flavored Markdown को सक्षम करें
  tables: true,      // GFM टेबल को सक्षम करें
  breaks: false,     // अगर सत्य है, तो एकल लाइन ब्रेक पर <br> जोड़ें
  pedantic: false,   // अगर सत्य है, तो कड़ी Markdown स्पेक को पालन करें
  sanitize: false,   // अगर सत्य है, तो सुरक्षा के लिए HTML टैग को हटा दें
  smartLists: true,  // सूची रेंडरिंग को बेहतर बनाएं
  smartypants: false // अगर सत्य है, तो "smart" टाइपोग्राफी का उपयोग करें (जैसे, कर्ली क्वोट्स)
});
console.log(html);
```

### 0.3.6 में मुख्य विशेषताएं
- **बुनियादी Markdown**: हेडिंग (`#`), बोल्ड (`**`), इटैलिक (`*`), सूची, कोड ब्लॉक (```) आदि का समर्थन करता है।
- **GFM समर्थन**: GitHub Flavored Markdown (जैसे टेबल और टास्क सूची) उपलब्ध है अगर `gfm: true` सेट है।
- **कस्टम रेंडरर समर्थन नहीं**: नए वर्जनों के विपरीत, `0.3.6` कस्टम रेंडरर्स का समर्थन नहीं करता है, इसलिए आप इसके डिफ़ॉल्ट आउटपुट तक सीमित हैं।

### अधिक Markdown के साथ उदाहरण
यहाँ एक पूर्ण उदाहरण Node.js में है:

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
- **सैनिटाइज़ेशन**: अगर आप उपयोगकर्ता इनपुट को रेंडर कर रहे हैं, तो सुरक्षा के लिए कच्चे HTML को हटाने के लिए `sanitize: true` सेट करें (जैसे, `<script>` टैग)। फिर भी, यह `0.3.6` में बुनियादी है और आधुनिक विकल्पों से कम मजबूत है।
- **सीमाएं**: इस वर्जन में बाद के रिलीज में जोड़े गए विशेषताओं (जैसे, एसिंक पर्सिंग, कस्टम टोकनाइज़र) की कमी है, इसलिए अगर आपको अधिक चाहिए, तो एक नए वर्जन जैसे `5.x` पर अपग्रेड करने की सोचें।
- **डिबगिंग**: अगर यह काम नहीं कर रहा है, तो सुनिश्चित करें कि लाइब्रेरी सही तरह से लोड हो रही है और Markdown सिंटैक्स को चेक करें।