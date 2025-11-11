---
audio: false
generated: true
lang: hi
layout: post
title: जेकिल में KaTeX का उपयोग
translated: true
type: note
---

अपने मौजूदा सेटअप में MathJax के बजाय KaTeX का उपयोग करने के लिए, आपको MathJax स्क्रिप्ट्स को KaTeX से बदलना होगा और अपने Jekyll कॉन्फ़िगरेशन को एडजस्ट करना होगा। KaTeX, MathJax की तुलना में तेज़ और हल्का है, लेकिन इसके लिए एक अलग तरीके की आवश्यकता है क्योंकि यह MathJax की सभी सुविधाओं का समर्थन नहीं करता है (उदाहरण के लिए, स्वचालित समीकरण नंबरिंग अधिक मैनुअल है)। नीचे आपकी Jekyll साइट में KaTeX पर स्विच करने के लिए एक चरण-दर-चरण मार्गदर्शिका दी गई है:

### 1. अपने Jekyll कॉन्फ़िगरेशन को अपडेट करें
Kramdown के लिए KaTeX को math engine के रूप में उपयोग करने के लिए अपनी `_config.yml` को संशोधित करें। `kramdown` सेक्शन को निम्नानुसार अपडेट करें:

```yaml
kramdown:
  math_engine: katex
  input: GFM
  syntax_highlighter: rouge
```

यह Kramdown को MathJax के बजाय KaTeX का उपयोग करके LaTeX math expressions को रेंडर करने के लिए कहता है।

### 2. अपने HTML में KaTeX को शामिल करें
अपने HTML से MathJax स्क्रिप्ट्स को हटा दें और उन्हें KaTeX से बदल दें। आप KaTeX को CDN के माध्यम से शामिल कर सकते हैं। अपनी Jekyll लेआउट फ़ाइल (जैसे, `_layouts/default.html`) के `<head>` सेक्शन में निम्नलिखित जोड़ें:

```html
<!-- KaTeX CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" integrity="sha384-nB0miv6/jRmo5SLY8cTjmnkA3wC7o1L0jOey4Cki5N3kdjdPD/mW59G1Qsxa8c3y" crossorigin="anonymous">

<!-- KaTeX JS -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" integrity="sha384-7zkKLzPD3M4y9W8FWsN4Z0yO5eLu8qUn0QHY6hZ2r3fDzqjk0McYc3vJrmE2h6cZ" crossorigin="anonymous"></script>

<!-- Auto-render extension (वैकल्पिक, math के स्वचालित रेंडरिंग के लिए) -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" integrity="sha384-43gviWU0YVjaDtb/GhzOouOXtZMP/7XUzwPTL0xF3iS9Ho94fSc31UyUyIDgWvB4" crossorigin="anonymous"></script>

<!-- Auto-render configuration -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: "$$", right: "$$", display: true}, // Block math
        {left: "\\[", right: "\\]", display: true}, // Block math
        {left: "\\(", right: "\\)", display: false}, // Inline math
        {left: "$", right: "$", display: false} // Inline math
      ],
      throwOnError: false
    });
  });
</script>
```

### 3. MathJax कॉन्फ़िगरेशन को हटाएं
अपनी लेआउट फ़ाइल से MathJax-संबंधित कोड को हटा दें, जिसमें `<script type="text/x-mathjax-config">` ब्लॉक और MathJax CDN स्क्रिप्ट शामिल है। KaTeX, MathJax के `tex2jax` जैसे कॉन्फ़िगरेशन का उपयोग नहीं करता है, और उपरोक्त auto-render स्क्रिप्ट समान कार्यक्षमता को संभालती है।

### 4. अपने Markdown में Math लिखें
KaTeX और Kramdown के कॉन्फ़िगर हो जाने के बाद, आप पहले की तरह ही डिलीमीटर्स का उपयोग करके अपनी Markdown फ़ाइलों में LaTeX math लिख सकते हैं:

- **Inline math**: `$...$` या `\(...\)` का उपयोग करें (उदाहरण के लिए, `$E=mc^2$` या `\(E=mc^2\)`)।
- **Display math**: `$$...$$` या `\[...\]` का उपयोग करें (उदाहरण के लिए, `$$E=mc^2$$` या `\[E=mc^2\]`)।

उदाहरण के लिए:

```markdown
Inline math: $E=mc^2$ or \(E=mc^2\).

Display math:
$$E=mc^2$$

or

\[E=mc^2\]
```

KaTeX math engine के साथ Kramdown इन्हें HTML में प्रोसेस कर देगा जिसे KaTeX रेंडर करता है।

### 5. KaTeX बनाम MathJax पर नोट्स
- **स्वचालित समीकरण नंबरिंग**: KaTeX, MathJax के `autoNumber: "AMS"` जैसी स्वचालित समीकरण नंबरिंग का समर्थन नहीं करता है। यदि आपको समीकरण नंबरों की आवश्यकता है, तो आपको अपने LaTeX कोड में `\tag{}` का उपयोग करके उन्हें मैन्युअल रूप से जोड़ना होगा (उदाहरण के लिए, `$$E=mc^2 \tag{1}$$`)।
- **प्रदर्शन**: KaTeX, MathJax की तुलना में काफी तेज़ है, जो Jekyll जैसी स्टेटिक साइट्स के लिए आदर्श है।
- **फीचर सेट**: KaTeX, MathJax की तुलना में कम LaTeX कमांड्स का समर्थन करता है। सुनिश्चित करने के लिए [KaTeX supported functions](https://katex.org/docs/supported.html) देखें कि आपके math expressions संगत हैं।
- **रेंडरिंग**: उपरोक्त auto-render स्क्रिप्ट निर्दिष्ट डिलीमीटर्स के भीतर math expressions को स्वचालित रूप से रेंडर करके MathJax के व्यवहार की नकल करती है। यदि आप डिलीमीटर्स को बदलना या सीमित करना चाहते हैं तो स्क्रिप्ट में `delimiters` ऐरे को एडजस्ट करें।

### 6. अपने सेटअप का परीक्षण करें
अपनी Jekyll साइट को स्थानीय रूप से चलाएं (`jekyll serve`) और सत्यापित करें कि math expressions सही ढंग से रेंडर हो रहे हैं। यदि आपको कोई समस्या आती है:
- KaTeX-संबंधित त्रुटियों के लिए ब्राउज़र कंसोल जांचें।
- सुनिश्चित करें कि KaTeX CDN URLs अप-टू-डेट हैं (उपरोक्त वाले संस्करण 0.16.11 का उपयोग करते हैं, मेरे ज्ञान के अनुसार नवीनतम)।
- पुष्टि करें कि आपकी Markdown फ़ाइलें मान्य KaTeX-संगत LaTeX सिंटैक्स का उपयोग करती हैं।

### 7. वैकल्पिक: स्थानीय KaTeX फ़ाइलें
यदि आप CDN निर्भरता से बचने के लिए स्थानीय रूप से KaTeX फ़ाइलों को होस्ट करना पसंद करते हैं:
1. [KaTeX GitHub releases](https://github.com/KaTeX/KaTeX/releases) से `katex.min.css`, `katex.min.js`, और `auto-render.min.js` डाउनलोड करें।
2. उन्हें अपने Jekyll assets फ़ोल्डर में रखें (जैसे, `assets/katex/`)।
3. `<link>` और `<script>` टैग्स को अपनी स्थानीय फ़ाइलों की ओर इशारा करने के लिए अपडेट करें (जैसे, `/assets/katex/katex.min.css`)।

### 8. समस्या निवारण
- **Math रेंडर नहीं हो रहा**: सुनिश्चित करें कि KaTeX स्क्रिप्ट्स सही ढंग से लोड हो रही हैं और `kramdown.math_engine` को `katex` पर सेट किया गया है।
- **डिलीमीटर समस्याएं**: सत्यापित करें कि auto-render स्क्रिप्ट में आपके डिलीमीटर्स आपकी Markdown में मौजूद डिलीमीटर्स से मेल खाते हैं।
- **असमर्थित कमांड्स**: यदि कोई LaTeX कमांड विफल हो जाती है, तो समर्थित कमांड्स के लिए KaTeX दस्तावेज़ देखें या एक्सप्रेशन को फिर से लिखें।

यदि आपको किसी विशेष math expression या कॉन्फ़िगरेशन के साथ विशिष्ट सहायता की आवश्यकता है, तो विवरण साझा करें, और मैं विशेष रूप से अनुरूप मार्गदर्शन प्रदान कर सकता हूं!