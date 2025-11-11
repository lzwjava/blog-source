---
audio: false
generated: true
lang: hi
layout: post
title: वीएस कोड वीएसआईएक्स डाउनलोड
translated: true
type: note
---

Visual Studio Code (VS Code) एक्सटेंशन के लिए `.vsix` फ़ाइल को मैन्युअल रूप से डाउनलोड करने के लिए, आप Visual Studio Marketplace का उपयोग कर सकते हैं, जो सभी ऑफिसियल एक्सटेंशन होस्ट करता है। `.vsix` फ़ाइल VS Code एक्सटेंशन के लिए पैकेज्ड फॉर्मेट है, और हालांकि Marketplace हमेशा डायरेक्ट डाउनलोड बटन प्रदान नहीं करता, आप डाउनलोड URL को मैन्युअल रूप से बना सकते हैं या वैकल्पिक तरीकों का उपयोग कर सकते हैं। यहां बताया गया है कि इसे स्टेप-बाय-स्टेप कैसे करें:

### `.vsix` फ़ाइल को मैन्युअल रूप से डाउनलोड करने के चरण

1.  **Visual Studio Marketplace पर एक्सटेंशन ढूंढें**
    - अपने वेब ब्राउज़र में [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode) पर जाएं।
    - वह एक्सटेंशन सर्च करें जिसे आप चाहते हैं (उदाहरण के लिए, Microsoft द्वारा "Python", "Prettier - Code formatter", आदि)।
    - एक्सटेंशन के पेज को खोलें। उदाहरण के लिए, Python एक्सटेंशन का URL कुछ इस तरह दिख सकता है:
      `https://marketplace.visualstudio.com/items?itemName=ms-python.python`.

2.  **पब्लिशर और एक्सटेंशन नाम की पहचान करें**
    - एक्सटेंशन के पेज पर, **पब्लिशर** और **एक्सटेंशन आइडेंटिफायर** नोट करें। ये URL का हिस्सा होते हैं या पेज पर दिखाए जाते हैं।
    - उदाहरण के लिए, `ms-python.python` में, `ms-python` पब्लिशर है और `python` एक्सटेंशन का नाम है।

3.  **डाउनलोड URL बनाएं**
    - `.vsix` फ़ाइल को सीधे Marketplace द्वारा प्रदान किए गए एक विशिष्ट URL पैटर्न का उपयोग करके डाउनलोड किया जा सकता है। सामान्य फॉर्मेट है:
      ```
      https://<publisher>.gallery.vsassets.io/_apis/public/gallery/publisher/<publisher>/extension/<extension-name>/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
      ```
    - `<publisher>` को पब्लिशर के नाम से और `<extension-name>` को एक्सटेंशन नाम से बदलें।
    - Python एक्सटेंशन (`ms-python.python`) के लिए, URL यह होगा:
      ```
      https://ms-python.gallery.vsassets.io/_apis/public/gallery/publisher/ms-python/extension/python/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
      ```
    - इस URL को अपने ब्राउज़र में पेस्ट करें, और यह `.vsix` फ़ाइल का डाउनलोड शुरू कर देगा।

4.  **विकल्प: Marketplace पेज के "Download Extension" लिंक का उपयोग करें (अगर उपलब्ध हो)**
    - कुछ एक्सटेंशन पेजों में **Resources** सेक्शन या कहीं और "Download Extension" लिंक शामिल होता है। अगर मौजूद हो, तो `.vsix` फ़ाइल को सीधे डाउनलोड करने के लिए उस पर क्लिक करें। हालांकि, यह कम कॉमन है, इसलिए URL विधि अधिक विश्वसनीय है।

5.  **डाउनलोड को वेरिफाई करें**
    - डाउनलोड की गई फ़ाइल में `.vsix` एक्सटेंशन होगा (उदाहरण के लिए, `ms-python.python-<version>.vsix`)।
    - फ़ाइल का साइज और नाम चेक करें ताकि यह सुनिश्चित हो सके कि यह आपके अपेक्षित एक्सटेंशन और वर्जन से मेल खाता है।

6.  **VS Code में `.vsix` फ़ाइल इंस्टॉल करें (ऑप्शनल)**
    - VS Code खोलें।
    - एक्सटेंशन्स व्यू (`Ctrl+Shift+X` या macOS पर `Cmd+Shift+X`) पर जाएं।
    - एक्सटेंशन्स पेन के ऊपर-दाईं ओर तीन-डॉट मेन्यू (`...`) पर क्लिक करें।
    - **Install from VSIX** चुनें, फिर डाउनलोड की गई `.vsix` फ़ाइल को ब्राउज़ करके सेलेक्ट करें।

### उदाहरण वॉकथ्रू
मान लीजिए आपको Dirk Baeumer द्वारा **ESLint** एक्सटेंशन चाहिए:
- Marketplace URL: `https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint`
- पब्लिशर: `dbaeumer`
- एक्सटेंशन नाम: `vscode-eslint`
- डाउनलोड URL:
  ```
  https://dbaeumer.gallery.vsassets.io/_apis/public/gallery/publisher/dbaeumer/extension/vscode-eslint/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
  ```
- इस URL को अपने ब्राउज़र में खोलें, और `.vsix` फ़ाइल (उदाहरण के लिए, `dbaeumer.vscode-eslint-<version>.vsix`) डाउनलोड हो जाएगी।

### नोट्स
-   **वर्जन**: URL का `/latest/` भाग यह सुनिश्चित करता है कि आपको सबसे नवीनतम वर्जन मिले। अगर आपको किसी विशिष्ट वर्जन की आवश्यकता है, तो आपको आमतौर पर वर्जन नंबर (Marketplace के "Version History" टैब पर दिखाई देता है) की एक्सेस की आवश्यकता होगी और URL को एडजस्ट करना पड़ सकता है या `ovsx` जैसे टूल का उपयोग करना पड़ सकता है (नीचे देखें), हालांकि Marketplace API आसानी से डायरेक्ट URL के माध्यम से पुराने वर्जन को एक्सपोज़ नहीं करता है।
-   **ब्लॉक्ड डाउनलोड**: अगर URL काम नहीं करता है, तो पब्लिशर ने डायरेक्ट एक्सेस को रिस्ट्रिक्ट किया हो सकता है, या आपका ब्राउज़र/नेटवर्क इसे ब्लॉक कर रहा हो सकता है। ऐसे मामलों में, कोई अलग ब्राउज़र या डाउनलोड मैनेजर आज़माएं।
-   **वैकल्पिक टूल्स**: आप एक्सटेंशन डाउनलोड करने के लिए कमांड-लाइन टूल जैसे `ovsx` (Open VSX Registry से) का उपयोग कर सकते हैं। इसे npm के माध्यम से इंस्टॉल करें (`npm install -g ovsx`), फिर रन करें:
    ```
    ovsx download ms-python.python
    ```
    यह प्रोग्रामेटिक रूप से `.vsix` फ़ाइल डाउनलोड करता है।

### अंतिम उत्तर
VS Code एक्सटेंशन के लिए `.vsix` फ़ाइल को मैन्युअल रूप से डाउनलोड करने के लिए:
1.  [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode) पर एक्सटेंशन के पेज पर जाएं।
2.  पब्लिशर और एक्सटेंशन नाम की पहचान करें (उदाहरण के लिए, `ms-python.python`)।
3.  अपने ब्राउज़र में इस URL फॉर्मेट का उपयोग करें:
    ```
    https://<publisher>.gallery.vsassets.io/_apis/public/gallery/publisher/<publisher>/extension/<extension-name>/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
    ```
4.  `.vsix` फ़ाइल डाउनलोड करें और ऑप्शनली इसे VS Code में इंस्टॉल करें।