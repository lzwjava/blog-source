---
audio: false
generated: true
image: false
lang: hi
layout: post
title: ओपन ग्राफ प्रोटोकॉल की व्याख्या
translated: true
type: note
---

HTML मेटा टैग्स जैसे `<meta property="og:type" content="website">` के संदर्भ में, "og" का मतलब Open Graph होता है। यह Open Graph प्रोटोकॉल को संदर्भित करता है, जो एक मानक है जिसे मूल रूप से Facebook (अब Meta) द्वारा विकसित किया गया था ताकि वेब पेज अपनी सामग्री के बारे में संरचित मेटाडेटा प्रदान कर सकें। यह मेटाडेटा नियंत्रित करता है कि सोशल मीडिया प्लेटफॉर्म या मैसेजिंग ऐप पर साझा करने पर पेज कैसा दिखाई देता है, जैसे कि एक समृद्ध पूर्वावलोकन फॉर्मेट (उदाहरण के लिए, एक छवि और सारांश के साथ एक कार्ड) में शीर्षक, विवरण, छवि और अन्य विवरण प्रदर्शित करना।

यह प्रोटोकॉल "og:" उपसर्ग वाले गुणों का उपयोग निम्नलिखित तत्वों को परिभाषित करने के लिए करता है:
- `og:title`: सामग्री का शीर्षक।
- `og:description`: एक संक्षिप्त सारांश।
- `og:image`: एक पूर्वावलोकन छवि के लिए URL।
- `og:type`: सामग्री का प्रकार (जैसे, वेबसाइट, article, video)।

हालांकि इसे Facebook के लिए बनाया गया था, लिंक पूर्वावलोकन के लिए कई अन्य प्लेटफॉर्म और ऐप Open Graph टैग्स का समर्थन करते हैं, जिनमें WeChat भी शामिल है। जब आप WeChat पर कोई लिंक साझा करते हैं, तो यह अक्सर थंबनेल, शीर्षक और विवरण को सुसंगत रूप से उत्पन्न करने के लिए इन टैग्स को पार्स करता है। यदि ये टैग मौजूद नहीं हैं, तो प्लेटफॉर्म अन्य मेटा टैग्स पर वापस लौट सकते हैं या पेज की सामग्री को स्क्रैप कर सकते हैं, जिसके परिणामस्वरूप असंगत परिणाम हो सकते हैं।

"open gx" के बारे में आका अनुमान करीब लगता है—यह वास्तव में "Open Graph" है, "open gx" नहीं (संभवतः "graph" के लिए एक टाइपो या ऑटोकरेक्ट?)।

### संदर्भ
[The Open Graph protocol](https://ogp.me/)  
[Open Graph Meta Tags: Everything You Need to Know](https://ahrefs.com/blog/open-graph-meta-tags/)  
[What is Open Graph and how can I use it for my website?](https://www.freecodecamp.org/news/what-is-open-graph-and-how-can-i-use-it-for-my-website/)  
[How does wechat choose the link's thumbnail?](https://stackoverflow.com/questions/44564614/how-does-wechat-choose-the-links-thumbnail)  
[Meta tag - WeChat](https://github.com/freeCodeCamp/freeCodeCamp/issues/38707)