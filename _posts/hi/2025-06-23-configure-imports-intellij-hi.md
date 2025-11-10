---
audio: false
generated: true
lang: hi
layout: post
title: इंटेलिजे आईडीईए में सिंगल-क्लास इम्पोर्ट्स कॉन्फ़िगर करना
translated: true
type: note
---

IntelliJ IDEA आयातों को हैंडल करने के लिए सेटिंग्स प्रदान करता है, जिसमें wildcards के उपयोग को रोकना भी शामिल है। यहां बताया गया है कि आप इसे हमेशा single-class imports का उपयोग करने के लिए कैसे कॉन्फ़िगर कर सकते हैं:

1.  **Settings/Preferences खोलें:**
    * **Windows/Linux:** `Ctrl + Alt + S`
    * **macOS:** `Cmd + ,` (Comma)

2.  **Code Style for Java पर नेविगेट करें:**
    * Settings डायलॉग के बाएं पैन में, यहां नेविगेट करें:
        `Editor` -> `Code Style` -> `Java`

3.  **"Imports" टैब पर जाएं:**
    * दाईं ओर, `Imports` टैब का चयन करें।

4.  **Import सेटिंग्स कॉन्फ़िगर करें:**
    यहां आपको कुछ महत्वपूर्ण सेटिंग्स दिखाई देंगी:

    * **`Use single class import`**: **इस चेकबॉक्स को चेक करें।** यह प्राथमिक सेटिंग है जो IntelliJ को wildcard imports पर व्यक्तिगत क्लास imports को प्राथमिकता देने के लिए कहती है।

    * **`Class count to use import with '*'`**: यह सेटिंग निर्धारित करती है कि किसी एक पैकेज से कितनी कक्षाओं को आयात किया जाना चाहिए इससे पहले कि IntelliJ स्वचालित रूप से एक wildcard import (जैसे, `java.util.*`) पर स्विच करे। wildcard imports को प्रभावी ढंग से अक्षम करने के लिए, **इसे एक बहुत अधिक संख्या पर सेट करें**, जैसे `999` या `9999`। यह सुनिश्चित करता है कि आप लगभग कभी भी wildcard import के लिए थ्रेसहोल्ड तक नहीं पहुंचेंगे।

    * **`Names count to use static import with '*'`**: यह ऊपर वाले के समान है लेकिन static imports के लिए। wildcard static imports को रोकने के लिए इसे भी एक उच्च संख्या (जैसे, `999` या `9999`) पर सेट करें।

    * **`Packages to Use Imports with '*'`**: यह टेबल उन पैकेजों को सूचीबद्ध करती है जिनके लिए IntelliJ अन्य सेटिंग्स की परवाह किए बिना *हमेशा* wildcard imports का उपयोग करेगा। यदि आप wildcard imports से पूरी तरह बचना चाहते हैं तो **सुनिश्चित करें कि यह टेबल खाली है**। यदि आपको `java.util.*` या `java.awt.*` जैसी एंट्री दिखाई देती हैं, तो उन्हें हटा दें।

5.  **परिवर्तन लागू करें:**
    * अपने परिवर्तनों को सहेजने के लिए `Apply` और फिर `OK` पर क्लिक करें।

**ये परिवर्तन करने के बाद:**

* जब आप "Auto Import" फीचर का उपयोग करते हैं (उदाहरण के लिए, एक अनरेजॉल्व्ड क्लास पर `Alt + Enter` दबाकर), IntelliJ अब wildcards के बजाय व्यक्तिगत क्लास imports डालेगा।
* यदि आपके पास wildcard imports वाली मौजूदा फाइलें हैं, तो आप उन्हें अपनी नई सेटिंग्स के अनुसार single-class imports में बदलने के लिए "Optimize Imports" एक्शन (Windows/Linux पर `Ctrl + Alt + O`, macOS पर `Cmd + Option + O`) का उपयोग कर सकते हैं।

इन चरणों का पालन करके, आप Java फाइलों के लिए IntelliJ IDEA द्वारा wildcard imports का उपयोग करने को प्रभावी ढंग से रोक सकते हैं।