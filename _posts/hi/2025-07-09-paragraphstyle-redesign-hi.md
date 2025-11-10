---
audio: false
generated: true
lang: hi
layout: post
title: मध्यम वज़न के लिए अनुच्छेद शैली को पुनर्परिभाषित करें
translated: true
type: note
---

`cvparagraph` पर्यावरण को `\bodyfontlight` के बजाय `\mdseries` का उपयोग करने के लिए बदलने के लिए, आपको `\paragraphstyle` कमांड को पुनर्परिभाषित करने की आवश्यकता है। इसे awesome-cv क्लास लोड करने के बाद अपने प्रीएम्बल में जोड़ें:

```latex
\renewcommand*{\paragraphstyle}{\fontsize{11pt}{1em}\mdseries\upshape\color{text}}
```

यह पैराग्राफ स्टाइल को बदल देगा:
- `\bodyfontlight` (जो लाइट वेट है)

से:
- `\mdseries` (जो मीडियम वेट है, डिस्क्रिप्शन स्टाइल के समान)

इस तरह, आपका संपूर्ण `cvparagraph` पर्यावरण `\descriptionstyle` की तरह मीडियम वेट फ़ॉन्ट सीरीज़ का उपयोग करेगा।