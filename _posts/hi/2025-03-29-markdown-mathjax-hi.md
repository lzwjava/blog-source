---
audio: false
generated: true
lang: hi
layout: post
title: मार्कडाउन रेंडरिंग मैथजैक्स या केटेक्स के साथ
translated: true
type: note
---

वेबपेज पर LaTeX गणित रेंडरिंग को **Markdown** रेंडरिंग के साथ जोड़ने के लिए, आप आमतौर पर एक JavaScript लाइब्रेरी (जैसे **MathJax** या **KaTeX**) का उपयोग करेंगे, साथ ही एक Markdown पार्सर जो मानक Markdown सिंटैक्स को प्रोसेस कर सकता है। लक्ष्य यह है कि उपयोगकर्ता Markdown के भीतर LaTeX में गणित के सूत्र लिख सकें और उन्हें पेज पर ठीक से रेंडर किया जा सके।

इसे प्राप्त करने का तरीका यहां बताया गया है:

### 1. **MathJax या KaTeX के साथ Markdown रेंडरिंग**

आप बुनियादी Markdown सामग्री को रेंडर करने के लिए **marked.js** या **remarkable.js** जैसे **Markdown पार्सर** का उपयोग कर सकते हैं। फिर, Markdown सामग्री को रेंडर करने के बाद, उसके अंदर LaTeX गणित को रेंडर करने के लिए MathJax या KaTeX का उपयोग करें।

नीचे इसे प्राप्त करने के लिए एक चरण-दर-चरण दृष्टिकोण दिया गया है।

---

### **चरण 1: लाइब्रेरीज़ शामिल करें**

आपको अपनी HTML फ़ाइल में एक **Markdown पार्सर** और एक **Math रेंडरिंग लाइब्रेरी** (MathJax या KaTeX) दोनों को शामिल करना होगा।

उन्हें शामिल करने का तरीका यहां बताया गया है:

```html
<!-- LaTeX रेंडरिंग के लिए KaTeX (या MathJax) शामिल करें -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.css">
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.js"></script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/contrib/auto-render.min.js"></script>

<!-- एक Markdown पार्सर (जैसे marked.js) शामिल करें -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.0.10/marked.min.js"></script>
```

वैकल्पिक रूप से, यदि आप KaTeX के बजाय **MathJax** पसंद करते हैं, तो आप MathJax को इस तरह शामिल कर सकते हैं:

```html
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

---

### **चरण 2: Markdown से LaTeX रेंडरिंग प्रक्रिया सेटअप करें**

अब, आप अपनी HTML संरचना लिख सकते हैं और Markdown को रेंडर करने के लिए JavaScript का उपयोग कर सकते हैं और फिर उस Markdown के भीतर किसी भी LaTeX फ़ॉर्मूला को प्रोसेस कर सकते हैं।

यहां एक सरल उदाहरण दिया गया है:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Markdown + Math Rendering</title>

  <!-- गणित रेंडरिंग के लिए KaTeX शामिल करें -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/contrib/auto-render.min.js"></script>

  <!-- Markdown रेंडरिंग के लिए marked.js शामिल करें -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.0.10/marked.min.js"></script>
</head>
<body>

  <h1>Markdown + Math Rendering Example</h1>

  <!-- Markdown इनपुट के लिए Textarea -->
  <textarea id="markdownInput" rows="10" cols="50">
This is a Markdown editor. You can add LaTeX math formulas like this:

Inline math: \( E = mc^2 \)

Block math:
\[
\int_0^1 x^2 \, dx = \frac{1}{3}
\]
  </textarea>

  <hr>

  <!-- रेंडर किए गए Markdown के लिए कंटेनर -->
  <div id="markdownOutput"></div>

  <script>
    // Markdown + Math रेंडर करने के लिए फ़ंक्शन
    function renderMarkdown() {
      // इनपुट Markdown प्राप्त करें
      const markdownText = document.getElementById('markdownInput').value;

      // Markdown सामग्री को रेंडर करें
      const htmlContent = marked(markdownText);

      // रेंडर की गई HTML को आउटपुट div में डालें
      document.getElementById('markdownOutput').innerHTML = htmlContent;

      // KaTeX का उपयोग करके HTML सामग्री के अंदर गणित रेंडर करें
      renderMathInElement(document.getElementById('markdownOutput'), {
        delimiters: [
          { left: "\\(", right: "\\)", display: false }, // inline math
          { left: "\\[", right: "\\]", display: true }   // block math
        ]
      });
    }

    // पेज लोड होने पर और उपयोगकर्ता के इनपुट बदलने पर renderMarkdown फ़ंक्शन को कॉल करें
    renderMarkdown();
    document.getElementById('markdownInput').addEventListener('input', renderMarkdown);
  </script>
</body>
</html>
```

### **कोड की व्याख्या:**

1. **Markdown पार्सिंग:**
   - `<textarea>` में लिखे गए इनपुट Markdown को HTML में बदलने के लिए `marked.js` लाइब्रेरी का उपयोग किया जाता है। Markdown सिंटैक्स को प्रोसेस किया जाएगा और `<div id="markdownOutput"></div>` कंटेनर में HTML में बदल दिया जाएगा।

2. **गणित रेंडरिंग:**
   - Markdown में LaTeX समीकरण (इनलाइन `\( ... \)` और ब्लॉक `\[ ... \]`) को **KaTeX** के `renderMathInElement()` फ़ंक्शन का उपयोग करके रेंडर किया जाता है।
   - **KaTeX** HTML सामग्री में इनलाइन मैथ के लिए `\( ... \)` और ब्लॉक मैथ के लिए `\[ ... \]` को ढूंढता है और उन्हें स्वचालित रूप से रेंडर कर देता है।

3. **इंटरएक्टिव Markdown एडिटर:**
   - जैसे ही उपयोगकर्ता `<textarea>` में टाइप करता है, Markdown को पार्स करने और LaTeX फ़ॉर्मूला को रेंडर करने के लिए सामग्री को गतिशील रूप से अपडेट करने हेतु `renderMarkdown` फ़ंक्शन को कॉल किया जाता है।

---

### **चरण 3: विभिन्न फ्रंटएंड फ्रेमवर्क के लिए अनुकूलित करना**

आप इस समाधान को **React**, **Vue**, या **Angular** जैसे किसी भी फ्रंटएंड फ्रेमवर्क के साथ काम करने के लिए अनुकूलित कर सकते हैं। उदाहरण के लिए, रीयल-टाइम Markdown + LaTeX रेंडरिंग के लिए यहां एक **React** कार्यान्वयन दिया गया है:

#### **React उदाहरण**

1. **npm के माध्यम से KaTeX और marked इंस्टॉल करें:**

```bash
npm install katex marked
```

2. **Markdown + Math रेंडरिंग के लिए React कंपोनेंट:**

```jsx
import React, { useState, useEffect } from 'react';
import marked from 'marked';
import katex from 'katex';
import 'katex/dist/katex.min.css';

const MarkdownEditor = () => {
  const [markdown, setMarkdown] = useState('');

  useEffect(() => {
    // कंपोनेंट माउंट होने के बाद KaTeX का उपयोग करके गणित के फ़ॉर्मूले रेंडर करें
    renderMath();
  }, [markdown]);

  const renderMath = () => {
    const renderedHTML = marked(markdown);
    document.getElementById('markdownOutput').innerHTML = renderedHTML;

    // KaTeX के साथ LaTeX गणित फ़ॉर्मूले रेंडर करें
    katex.renderMathInElement(document.getElementById('markdownOutput'), {
      delimiters: [
        { left: "\\(", right: "\\)", display: false }, // inline math
        { left: "\\[", right: "\\]", display: true }   // block math
      ]
    });
  };

  return (
    <div>
      <h1>Markdown + Math Rendering</h1>
      <textarea
        value={markdown}
        onChange={(e) => setMarkdown(e.target.value)}
        rows="10"
        cols="50"
      />
      <hr />
      <div id="markdownOutput"></div>
    </div>
  );
};

export default MarkdownEditor;
```

React वर्जन में, हम Markdown टेक्स्ट को HTML में बदलने के लिए `marked` लाइब्रेरी का उपयोग करते हैं, और HTML के अंदर किसी भी LaTeX गणित फ़ॉर्मूले को प्रोसेस और रेंडर करने के लिए KaTeX के `renderMathInElement()` फ़ंक्शन का उपयोग करते हैं।

---

### **सारांश**
- Markdown सिंटैक्स को HTML में बदलने के लिए एक **Markdown पार्सर** (जैसे `marked.js`) का उपयोग करें।
- Markdown सामग्री में एम्बेडेड LaTeX गणित व्यंजकों को रेंडर करने के लिए **MathJax** या **KaTeX** का उपयोग करें।
- Markdown को HTML में रेंडर करके और KaTeX/MathJax का उपयोग करके गणित फ़ॉर्मूला को गतिशील रूप से प्रोसेस करके दोनों को संयोजित करें।

यह दृष्टिकोण उपयोगकर्ताओं को रीयल-टाइम में गणितीय समीकरणों के साथ Markdown सामग्री लिखने और पूर्वावलोकन करने की अनुमति देता है, जो ब्लॉग एडिटर, नॉलेज बेस सिस्टम, या शैक्षिक टूल जैसे एप्लिकेशन के लिए एकदम सही है!