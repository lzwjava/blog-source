---
audio: false
generated: true
lang: hi
layout: post
title: ह्यूगो में लेटेक्स रेंडरिंग
translated: true
type: note
---

आपके द्वारा वर्णित समस्या तब उत्पन्न होती है जब **MathJax** को गणित इंजन के रूप में उपयोग करते हुए **Kramdown** के साथ **Jekyll** का उपयोग किया जाता है। Kramdown, जब `math_engine: mathjax` के साथ कॉन्फ़िगर किया जाता है, Markdown सामग्री में कोष्ठकों `( )` को इनलाइन मैथ के लिए LaTeX डिलीमीटर (जैसे `\( \)`) के रूप में व्याख्या करता है, जो कोष्ठक वाले सामान्य टेक्स्ट को तोड़ सकता है। ऐसा इसलिए है क्योंकि MathJax आपके कॉन्फ़िगरेशन में दिखाए अनुसार इनलाइन मैथ के लिए `\( \)` या `$ $` को पार्स करने के लिए सेट किया गया है।

**Hugo** में, यह समस्या डिफ़ॉल्ट रूप से होने की संभावना कम होती है, लेकिन यह Hugo के Markdown प्रोसेसर और MathJax इंटीग्रेशन को आप कैसे कॉन्फ़िगर करते हैं, उस पर निर्भर करता है। नीचे, मैं समझाऊंगा कि Hugo अधिकांश मामलों में इस समस्या से कैसे बचता है, Jekyll में इसे कैसे रोका या ठीक किया जाए, और यह सुनिश्चित किया जाए कि Hugo में ऐसा न हो।

---

### **क्या Hugo में यह समस्या है?**
Hugo आमतौर पर इस समस्या से बचता है क्योंकि:
1.  **Markdown प्रोसेसर**: Hugo अपने डिफ़ॉल्ट Markdown रेंडरर के रूप में **Goldmark** (या वैकल्पिक रूप से Blackfriday) का उपयोग करता है, जो डिफ़ॉल्ट रूप से MathJax या LaTeX पार्सिंग को सक्षम नहीं करता है। जब तक आप स्पष्ट रूप से Hugo को MathJax का उपयोग करने और `\( \)` जैसे इनलाइन मैथ डिलीमीटर सेटअप करने के लिए कॉन्फ़िगर नहीं करते, आपकी सामग्री में सामान्य कोष्ठक `( )` LaTeX के रूप में गलत व्याख्या नहीं किए जाएंगे।
2.  **MathJax इंटीग्रेशन**: Hugo मूल रूप से LaTeX को पार्स नहीं करता है। यदि आप MathJax सपोर्ट चाहते हैं, तो आपको अपनी थीम के टेम्पलेट्स (जैसे, `layouts/partials/head.html` में) में MathJax स्क्रिप्ट्स को मैन्युअल रूप से जोड़ना होगा और डिलीमीटर कॉन्फ़िगर करने होंगे। Hugo की लचीलापन आपको यह नियंत्रित करने की अनुमति देता है कि MathJax सामग्री को कैसे प्रोसेस करता है, जिससे स्पष्ट रूप से सक्षम किए बिना `( )` के स्वचालित पार्सिंग से बचा जा सकता है।
3.  **गणित के लिए शॉर्टकोड**: Hugo उपयोगकर्ता अक्सर शॉर्टकोड (जैसे, `{{< math >}}...{{< /math >}}`) का उपयोग करके LaTeX रेंडरिंग लागू करते हैं, जो स्पष्ट रूप से गणित सामग्री को निर्दिष्ट करते हैं, जिससे सामान्य कोष्ठकों को LaTeX के लिए गलत नहीं समझा जाता है।

संक्षेप में, Hugo में यह समस्या तब तक नहीं होगी जब तक आप समान इनलाइन डिलीमीटर (`\( \)`) के साथ MathJax को कॉन्फ़िगर नहीं करते और उचित सुरक्षा उपायों के बिना स्वचालित पार्सिंग सक्षम नहीं करते। शॉर्टकोड का उपयोग करके या `\( \)` को डिलीमीटर के रूप में उपयोग करने से बचकर, Hugo इस समस्या से पूरी तरह बच सकता है।

---

### **Jekyll में समस्या का समाधान**
Jekyll में, यह समस्या इसलिए होती है क्योंकि Kramdown की `math_engine: mathjax` सेटिंग, आपके MathJax कॉन्फ़िगरेशन के साथ मिलकर, `( )` को LaTeX के रूप में पार्स करने का कारण बनती है। इसे ठीक करने के तरीके यहां दिए गए हैं:

#### **1. MathJax इनलाइन डिलीमीटर बदलें**
MathJax कॉन्फ़िगरेशन को अलग इनलाइन मैथ डिलीमीटर, जैसे `$ $`, का उपयोग करने के लिए संशोधित करें, ताकि सामान्य कोष्ठकों के साथ संघर्ष से बचा जा सके। अपनी Jekyll साइट के HTML (जैसे, `_includes/head.html` में) स्क्रिप्ट को अपडेट करें:

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [['$','$']], // इनलाइन मैथ के लिए $ $ का उपयोग करें
      displayMath: [['$$','$$'], ['\[','\]']],
      processEscapes: true // $ को शाब्दिक रूप से उपयोग करने के लिए एस्केप करने की अनुमति दें
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": { linebreaks: { automatic: true } },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```

-   **यह क्यों काम करता है**: `inlineMath` से `['\(','\)']` को हटाकर, MathJax अब `( )` को LaTeX डिलीमीटर के रूप में व्याख्या नहीं करता है, जिससे वे सामान्य टेक्स्ट के लिए सुरक्षित रहते हैं। `processEscapes: true` सेटिंग आपको `\$` लिखकर एक शाब्दिक `$` प्रदर्शित करने की अनुमति देती है यदि आवश्यक हो।
-   **आपके Markdown में**: इनलाइन मैथ के लिए `\(x^2\)` के बजाय `$x^2$` का उपयोग करें। उदाहरण के लिए:
    ```markdown
    यह एक फॉर्मूला है: $x^2 + y^2 = z^2$. सामान्य टेक्स्ट (पार्स नहीं)।
    ```

#### **2. Markdown में कोष्ठकों को एस्केप करें**
यदि आप `\( \)` को डिलीमीटर के रूप में रखना चाहते हैं, तो Kramdown/MathJax द्वारा उन्हें LaTeX के रूप में पार्स करने से रोकने के लिए अपनी Markdown सामग्री में कोष्ठकों को एस्केप करें। प्रत्येक कोष्ठक से पहले बैकस्लैश `\` का उपयोग करें:

```markdown
सामान्य टेक्स्ट \(not a formula\)। यह एक वास्तविक फॉर्मूला है: \(x^2 + y^2\)।
```

-   **आउटपुट**: एस्केप किया गया `\(not a formula\)` `(not a formula)` के रूप में रेंडर होता है, जबकि `\(x^2 + y^2\)` एक LaTeX फॉर्मूला के रूप में रेंडर होता है।
-   **कमी**: इसके लिए आपकी सामग्री में `( )` के प्रत्येक उदाहरण को मैन्युअल रूप से एस्केप करने की आवश्यकता होती है, जो थकाऊ हो सकता है।

#### **3. विशिष्ट पेजों के लिए MathJax अक्षम करें**
यदि आपको केवल कुछ पेजों (जैसे, गणित-प्रधान पोस्ट्स) पर MathJax की आवश्यकता है, तो इसे डिफ़ॉल्ट रूप से अक्षम करें और केवल आवश्यकता वाले स्थानों पर सक्षम करें:
-   MathJax स्क्रिप्ट को अपने ग्लोबल `_layouts/default.html` या `_includes/head.html` से हटा दें।
-   अपने लेआउट या पेज फ्रंट मैटर में एक सशर्त इंक्लूड जोड़ें। उदाहरण के लिए, `_layouts/post.html` में:

```html
{% if page.mathjax %}
  <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      tex2jax: {
        inlineMath: [['$','$']],
        displayMath: [['$$','$$'], ['\[','\]']],
        processEscapes: true
      }
    });
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
{% endif %}
```

-   अपनी Markdown फ़ाइल के फ्रंट मैटर में, केवल विशिष्ट पेजों के लिए MathJax सक्षम करें:
    ```yaml
    ---
    title: मेरी गणित पोस्ट
    mathjax: true
    ---
    ```

-   **यह क्यों काम करता है**: `mathjax: true` के बिना पेज MathJax लोड नहीं करेंगे, इसलिए `( )` को LaTeX के रूप में पार्स नहीं किया जाएगा।

#### **4. एक अलग Math इंजन का उपयोग करें**
MathJax से Kramdown द्वारा समर्थित किसी अन्य math इंजन, जैसे **KaTeX**, पर स्विच करें, जो तेज़ है और स्पष्ट रूप से कॉन्फ़िगर किए बिना कोष्ठकों की गलत व्याख्या होने की संभावना कम होती है। अपनी Jekyll साइट में KaTeX इंस्टॉल करें:
-   `_includes/head.html` में KaTeX स्क्रिप्ट्स जोड़ें:
    ```html
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/auto-render.min.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false }
          ]
        });
      });
    </script>
    ```
-   `_config.yml` अपडेट करें:
    ```yaml
    kramdown:
      math_engine: katex
      input: GFM
      syntax_highlighter: rouge
    ```

-   **यह क्यों काम करता है**: KaTeX पार्सिंग के बारे में अधिक सख्त है और इनलाइन मैथ के लिए डिफ़ॉल्ट रूप से `$ $` का उपयोग करता है, जिससे `( )` के साथ संघर्ष कम होता है। यह MathJax से भी तेज़ है।

---

### **यह सुनिश्चित करना कि Hugo इस समस्या से बचे**
Hugo में MathJax का उपयोग करते हुए `( )` पार्सिंग समस्या में न पड़ने के लिए, इन चरणों का पालन करें:

1.  **Hugo में MathJax जोड़ें**:
    -   MathJax स्क्रिप्ट को अपनी थीम के पार्शियल्स (जैसे, `layouts/partials/head.html`) में रखें:
        ```html
        {{ if .Params.mathjax }}
        <script type="text/x-mathjax-config">
          MathJax.Hub.Config({
            tex2jax: {
              inlineMath: [['$','$']],
              displayMath: [['$$','$$'], ['\[','\]']],
              processEscapes: true
            },
            "HTML-CSS": { linebreaks: { automatic: true } },
            "CommonHTML": { linebreaks: { automatic: true } },
            TeX: { equationNumbers: { autoNumber: "AMS" } }
          });
        </script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
        {{ end }}
        ```
    -   विशिष्ट पेजों में फ्रंट मैटर में MathJax सक्षम करें:
        ```yaml
        ---
        title: मेरी गणित पोस्ट
        mathjax: true
        ---
        ```

2.  **गणित के लिए शॉर्टकोड का उपयोग करें**:
    गणित सामग्री को स्पष्ट रूप से लपेटने के लिए एक शॉर्टकोड (जैसे, `layouts/shortcodes/math.html`) बनाएं:
    ```html
    {{ if .IsNamedParams }}
      <span class="math">{{ .Get "content" | safeHTML }}</span>
    {{ else }}
      <span class="math">{{ .Inner | safeHTML }}</span>
    {{ end }}
    ```
    इसे अपने Markdown में उपयोग करें:
    ```markdown
    सामान्य टेक्स्ट (पार्स नहीं)। फॉर्मूला: {{< math >}}$x^2 + y^2${{< /math >}}।
    ```
    -   **यह क्यों काम करता है**: शॉर्टकोड यह सुनिश्चित करते हैं कि केवल स्पष्ट रूप से चिह्नित सामग्री को गणित के रूप में प्रोसेस किया जाता है, जिससे सामान्य टेक्स्ट में `( )` अछूते रहते हैं।

3.  **इसके बजाय KaTeX का उपयोग करें**:
    Hugo उपयोगकर्ता अक्सर इसकी गति के कारण KaTeX को प्राथमिकता देते हैं। `layouts/partials/head.html` में KaTeX जोड़ें:
    ```html
    {{ if .Params.math }}
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/auto-render.min.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false }
          ]
        });
      });
    </script>
    {{ end }}
    ```
    फ्रंट मैटर में इसे सक्षम करें:
    ```yaml
    math: true
    ```
    `( )` संघर्षों से बचने के लिए इनलाइन मैथ के लिए `$ $` का उपयोग करें।

---

### **सिफारिश**
-   **Jekyll के लिए**: `( )` पार्सिंग समस्याओं से बचने के लिए MathJax के लिए `$ $` डिलीमीटर पर स्विच करें या KaTeX का उपयोग करें। कोष्ठकों को एस्केप करना एक फॉलबैक है लेकिन बड़ी साइटों के लिए कम व्यावहारिक है।
-   **Hugo के लिए**: जब तक आप स्पष्ट रूप से `\( \)` डिलीमीटर के साथ MathJax को कॉन्फ़िगर नहीं करते, तब तक आपको इस समस्या का सामना करने की संभावना नहीं है। गणित रेंडरिंग के लिए शॉर्टकोड या KaTeX का उपयोग करें ताकि सामान्य कोष्ठक सुरक्षित रहें।

यदि आप Jekyll से Hugo में माइग्रेट कर रहे हैं और अपनी गणित सामग्री को रखना चाहते हैं, तो मैं स्पष्ट नियंत्रण के लिए शॉर्टकोड के साथ Hugo में KaTeX का उपयोग करने की सलाह देता हूं। यदि आपको Hugo के MathJax/KaTeX इंटीग्रेशन को सेटअप करने या अपनी Jekyll साइट की गणित सामग्री को कनवर्ट करने में मदद की आवश्यकता है, तो मुझे बताएं!