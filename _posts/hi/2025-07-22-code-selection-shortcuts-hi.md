---
audio: false
generated: true
lang: hi
layout: post
title: त्वरित कोड चयन एवं एआई संपादन
translated: true
type: note
---

नीचे **Visual Studio Code (VS Code)**, **Cursor**, और **IntelliJ IDEA** में शॉर्टकट का उपयोग करके किसी फ़ंक्शन या मेथड को जल्दी से चुनने (Select) का एक सिंहावलोकन दिया गया है, इसके बाद चुने गए कोड को ठीक करने या संपादित करने के लिए उनकी AI सुविधाओं का लाभ उठाने के तरीके बताए गए हैं।

### Visual Studio Code (VS Code)
VS Code में आपके कर्सर के फ़ंक्शन/मेथड के अंदर होने पर उसे पूरा चुनने के लिए कोई सीधा शॉर्टकट नहीं है, लेकिन आप निम्नलिखित तरीके अपना सकते हैं:
- **सिलेक्शन बढ़ाएँ (Expand Selection)**: सिलेक्शन के दायरे को बढ़ाने के लिए `Ctrl+Shift+.` (Windows/Linux) या `Cmd+Shift+.` (Mac) दबाएँ। बार-बार दबाने से उसे घेरने वाला ब्लॉक चुना जाता है (जैसे, फ़ंक्शन बॉडी, फिर पूरा फ़ंक्शन)। यह JavaScript, Python आदि के लिए अच्छी तरह काम करता है।
- **स्मार्ट सिलेक्शन (Smart Select)**: सिंटैक्स के आधार पर सिलेक्शन बढ़ाने के लिए `Ctrl+Shift+Right Arrow` (Windows/Linux) या `Cmd+Shift+Right Arrow` (Mac) का उपयोग करें (पूरा फ़ंक्शन कैप्चर करने के लिए कई बार दबाना पड़ सकता है)।
- **एक्सटेंशन: Select By**: "Select By" एक्सटेंशन इंस्टॉल करें और लैंग्वेज-स्पेसिफिक पैटर्न के आधार पर फ़ंक्शन/मेथड को चुनने के लिए एक कीबाइंडिंग (जैसे, `Ctrl+K, Ctrl+S`) कॉन्फ़िगर करें।

**GitHub Copilot के साथ AI एडिटिंग**:
- फ़ंक्शन को चुनने के बाद, Copilot की इनलाइन चैट खोलने के लिए `Ctrl+I` (Windows/Linux) या `Cmd+I` (Mac) दबाएँ। "fix bugs in this function" या "refactor to use arrow functions" जैसा कोई प्रॉम्प्ट टाइप करें।
- वैकल्पिक रूप से, चुने हुए हिस्से पर राइट-क्लिक करें, और "Copilot > Fix" या "Copilot > Refactor" चुनें ताकि AI सुझाव मिल सकें।
- Copilot Chat व्यू (`Ctrl+Alt+I`) में, चुना हुआ कोड पेस्ट करें और संपादन के लिए कहें (जैसे, "optimize this function")।

### Cursor AI Code Editor
Cursor, VS Code पर बना है, जो सिलेक्शन और AI इंटीग्रेशन को बेहतर बनाता है:
- **एनक्लोजिंग ब्लॉक चुनें (Select Enclosing Block)**: एनक्लोजिंग फ़ंक्शन/मेथड तक सिलेक्शन बढ़ाने के लिए `Ctrl+Shift+.` (Windows/Linux) या `Cmd+Shift+.` (Mac) दबाएँ, जो VS Code के समान है। Python या TypeScript जैसी भाषाओं के लिए Cursor की लैंग्वेज मॉडल जागरूकता इसे अक्सर अधिक सटीक बनाती है।
- **कस्टम कीबाइंडिंग (Custom Keybindings)**: आप फ़ंक्शन स्कोप को सीधे चुनने के लिए `settings.json` में एक कस्टम कीबाइंडिंग (जैसे, `editor.action.selectToBracket`) सेट कर सकते हैं।

**Cursor में AI एडिटिंग**:
- फ़ंक्शन को चुनने के बाद, `Ctrl+K` (Windows/Linux) या `Cmd+K` (Mac) दबाएँ, फिर बदलावों का वर्णन करें (जैसे, "add error handling to this function")। Cursor AI-जनरेटेड संपादनों का एक डिफ़ (diff) पूर्वावलोकन दिखाता है।
- फ़ंक्शन को फाइलों में ठीक करने या ऑप्टिमाइज़ करने के लिए, पुनरावृत्त फीडबैक के साथ `Ctrl+I` का उपयोग करके एजेंट मोड (Agent Mode) का उपयोग करें।
- कंपोज़र मोड (Composer Mode) (UI के माध्यम से एक्सेस करने योग्य) मल्टी-फाइल एडिट की अनुमति देता है यदि फ़ंक्शन कोडबेस के अन्य हिस्सों को प्रभावित करता है।

### IntelliJ IDEA
IntelliJ IDEA फ़ंक्शन/मेथड चुनने के लिए मजबूत शॉर्टकट प्रदान करता है:
- **कोड ब्लॉक चुनें (Select Code Block)**: अपने कर्सर को किसी मेथड के अंदर रखकर, एनक्लोजिंग ब्लॉक को चुनने के लिए `Ctrl+W` (Windows/Linux) या `Cmd+W` (Mac) दबाएँ। बार-बार दबाने से पूरी मेथड (सिग्नेचर सहित) तक विस्तार हो जाता है। यह Java, Kotlin, Python आदि में काम करता है।
- **सिलेक्शन सिकोड़ें (Extend Selection)**: यदि आप सिलेक्शन को जरूरत से ज्यादा बढ़ा देते हैं, तो इसे सिकोड़ने के लिए `Ctrl+Shift+W` (Windows/Linux) या `Cmd+Shift+W` (Mac) का उपयोग करें।
- **स्ट्रक्चर-अवेयर सिलेक्शन (Structure-Aware Selection)**: स्ट्रक्चर ट्री के माध्यम से एनक्लोजिंग मेथड को सीधे चुनने के लिए `Ctrl+Alt+Shift+Up` (Windows/Linux) या `Cmd+Option+Shift+Up` (Mac) दबाएँ।

**JetBrains AI Assistant के साथ AI एडिटिंग**:
- मेथड को चुनने के बाद, `Alt+Enter` दबाएँ या राइट-क्लिक करके "AI Actions" > "Fix with AI" या "Suggest Refactoring" चुनें। AI Assistant एक डिफ़ व्यूअर में संदर्भ-अवेयर सुझाव प्रदान करता है।
- चुनी हुई मेथड को सीधे संपादित करने के लिए इनलाइन प्रॉम्प्ट का उपयोग करें (`Tab` दबाएँ, उदाहरण के लिए, `/refactor to use streams` टाइप करें)।
- जटिल बदलावों का वर्णन करने (जैसे, "add logging to this method") और जनरेट किए गए कोड को लागू करने के लिए AI Assistant टूल विंडो खोलें।

### सारांश
- **VS Code**: सिलेक्शन बढ़ाने के लिए `Ctrl+Shift+.` का उपयोग करें, फिर Copilot AI संपादन के लिए `Ctrl+I` दबाएँ।
- **Cursor**: सटीक AI-चालित संपादन के लिए समान सिलेक्शन शॉर्टकट (`Ctrl+Shift+.`) और `Ctrl+K` का उपयोग करें।
- **IntelliJ IDEA**: त्वरित मेथड सिलेक्शन के लिए `Ctrl+W` का उपयोग करें, फिर AI Assistant फिक्स के लिए `Alt+Enter` दबाएँ।

IntelliJ में मेथड चुनने के लिए सबसे सटीक बिल्ट-इन शॉर्टकट (`Ctrl+W`) है, जबकि चुने गए कोड को संपादित करने के लिए Cursor का AI इंटीग्रेशन सबसे सहज है। VS Code लचीला है लेकिन तेज फ़ंक्शन सिलेक्शन के लिए एक्सटेंशन की आवश्यकता हो सकती है।

संदर्भ:  
[Visual Studio Code में कोड नेविगेशन](https://code.visualstudio.com/docs/editor/editingevolved)  
[Cursor AI: 10 प्रैक्टिकल उदाहरणों के साथ एक गाइड](https://www.datacamp.com/tutorial/cursor-ai-code-editor)  
[IntelliJ IDEA में कोड एडिटिंग](https://www.jetbrains.com/help/idea/working-with-source-code.html)  
[एडिटर में AI का उपयोग करें | IntelliJ IDEA डॉक्यूमेंटेशन](https://www.jetbrains.com/help/idea/use-ai-in-editor.html)