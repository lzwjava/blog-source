---
audio: false
generated: true
image: false
lang: hi
layout: post
title: मार्कडाउन लिंटिंग फॉर कंसिस्टेंट क्लीन फाइल्स
translated: true
type: note
---

यहाँ **markdownlint** प्रोजेक्ट का डेविड‌ एनसन द्वारा लिखित एक साफ़ और पाठक-हितैषी परिचय दिया गया है:

---

## **markdownlint** क्या है?

**markdownlint** मार्कडाउन/कॉमनमार्क फ़ाइलों के लिए एक स्टैटिक विश्लेषण टूल है, जो Node.js पर बना है। इसका मुख्य उद्देश्य मार्कडाउन कॉन्टेंट में एकरूपता और शैली नियमों को लागू करना है—जिससे लेखक एक साफ़, समान प्रारूप बनाए रख सकें और उन संरचनाओं से बच सकें जो विभिन्न पार्सरों में टूट सकती हैं या असंगत रूप से दिख सकती हैं ([GitHub][1])।

Ruby आधारित markdownlint (markdownlint/mdl) से प्रेरित, यह टूल लिंटिंग नियमों की एक समृद्ध लाइब्रेरी का उपयोग करता है। यह कॉमनमार्क सपोर्ट के लिए micromark पार्सर का लाभ उठाता है और इसे GitHub Flavored Markdown (GFM) फीचर्स जैसे टेबल्स, ऑटोलिंक्स, डायरेक्टिव्स, फ़ुटनोट्स और मैथ के साथ विस्तारित करता है ([GitHub][1])।

## मुख्य विशेषताएँ और एकीकरण

* **नियम कवरेज**: हेडिंग स्टाइल्स और लिस्ट इंडेंटेशन से लेकर ट्रेलिंग स्पेस और लाइन लंबाई तक, बिल्ट-इन नियमों का एक व्यापक सेट प्रदान करता है (जैसे MD001, MD009, MD013…) ([GitHub][1])।
* **इकोसिस्टम संगतता**:

  * **कमांड लाइन टूल्स**:

    * `markdownlint-cli` – एक पारंपरिक CLI इंटरफ़ेस।
    * `markdownlint-cli2` – एक तेज़, कॉन्फ़िगरेशन-आधारित CLI जिसमें लचीले फ़ॉर्मेटिंग विकल्प और ग्लॉब्स, आउटपुट फ़ॉर्मेट्स, ऑटोफिक्सिंग और CI वर्कफ़्लोज़ के साथ एकीकरण का सपोर्ट शामिल है ([GitHub][2], [GitHub][3])।
  * **VS Code एक्सटेंशन**:

    * `vscode‑markdownlint` आपके एडिटर में रियल-टाइम लिंटिंग लाता है। उल्लंघनों को इनलाइन चिह्नित किया जाता है (अंडरलाइन किया गया), जिसमें होवर-योग्य टूलटिप्स और क्विक-फिक्स सुझाव शामिल होते हैं ([GitHub][4])।
  * **GitHub Action**:

    * `markdownlint‑cli2‑action` आपको अपने CI पाइपलाइन में markdownlint को एम्बेड करने देता है, जिससे GitHub वर्कफ़्लोज़ के दौरान स्वचालित जांच (और वैकल्पिक ऑटोफिक्स) सक्षम होती है ([GitHub][5])।

---

## इसका उपयोग क्यों करें?

* **एकरूपता**: यह सुनिश्चित करता है कि मार्कडाउन फ़ाइलें एक परिभाषित स्टाइल गाइड का पालन करें, जिससे प्रोजेक्ट में फ़ॉर्मेटिंग ड्रिफ्ट कम होती है।
* **एडिटर सहायता**: VS Code और अन्य एकीकरणों में इनलाइन फीडबैक साफ़ और तेज़ लेखन को संभव बनाता है।
* **स्वचालन**: CI पाइपलाइनों में लिंट टूल्स या GitHub Actions के साथ उपयोग करके मर्ज से पहले मानकों को लागू किया जा सकता है।
* **अनुकूलन योग्य**: आप कॉन्फ़िग फ़ाइलों या इनलाइन कमेंट्स के माध्यम से नियम सेट को अनुकूलित कर सकते हैं या नियमों को अक्षम भी कर सकते हैं (जैसे, लंबी लाइनों के लिए MD013 को अक्षम करना) ([GitHub][5], [Software Recommendations Stack Exchange][6])।

---

क्या आप इसे npm के साथ सेटअप करने, VS Code एक्सटेंशन का उपयोग करने, या इसे CI वर्कफ़्लोज़ में इंटीग्रेट करने के लिए एक क्विक-स्टार्ट गाइड चाहेंगे?

[1]: https://github.com/DavidAnson/markdownlint?utm_source=chatgpt.com "DavidAnson/markdownlint: A Node.js style checker and lint ..."
[2]: https://github.com/markdownlint/markdownlint?utm_source=chatgpt.com "Markdown lint tool"
[3]: https://github.com/DavidAnson/markdownlint-cli2?utm_source=chatgpt.com "DavidAnson/markdownlint-cli2"
[4]: https://github.com/DavidAnson/vscode-markdownlint?utm_source=chatgpt.com "DavidAnson/vscode-markdownlint: Markdown linting and ..."
[5]: https://github.com/DavidAnson/markdownlint-cli2-action?utm_source=chatgpt.com "DavidAnson/markdownlint-cli2-action"
[6]: https://softwarerecs.stackexchange.com/questions/7138/markdown-lint-tool?utm_source=chatgpt.com "validation - Markdown lint tool"