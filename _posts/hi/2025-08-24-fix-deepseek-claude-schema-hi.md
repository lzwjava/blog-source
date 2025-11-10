---
audio: false
generated: true
image: false
lang: hi
layout: post
title: डीपसीक क्लॉड कोड स्कीमा बेमेल को ठीक करें
translated: true
type: note
---

संक्षिप्त उत्तर: स्कीमा मिसमैच।

क्लॉड कोड "Anthropic की भाषा बोलता है" (इसे Anthropic-Messages शैली के टूल यूज की उम्मीद होती है, जैसे `tool_use` / `tool_result` ब्लॉक)। OpenRouter पर DeepSeek V3.1 "OpenAI की भाषा बोलता है" (यह OpenAI-शैली के `tool_calls` / फंक्शन कॉलिंग उत्पन्न करता है)। यदि आपका क्लॉड कोड राउटर किसी टास्क को DeepSeek V3.1 पर बिना रिक्वेस्ट/रिस्पॉन्स को ट्रांसफॉर्म किए फॉरवर्ड करता है, तो असिस्टेंट के टूल-कॉलिंग मैसेज पार्स नहीं होंगे—और आपको तुरंत एरर दिखाई देंगे, ठीक तब जब एजेंट टूल्स प्लान/रन करने या आउटपुट स्ट्रीम करने की कोशिश करता है। ([Anthropic][1], [OpenRouter][2], [DeepSeek API Docs][3])

क्या करें (त्वरित समाधान):

1. राउटर के ट्रांसफॉर्मर का उपयोग करें
   अपने क्लॉड कोड राउटर में OpenRouter↔︎Anthropic रिक्वेस्ट/रिस्पॉन्स ट्रांसफॉर्मर को सक्षम करें ताकि `tool_calls` ⇄ `tool_use` दोनों तरफ मैप हो जाएं। लोकप्रिय कम्युनिटी राउटर इसे स्पष्ट रूप से सपोर्ट करता है; इसके "Request/Response Transformation" सेक्शन और उदाहरण कॉन्फ़िग को चेक करें। ([GitHub][4], [ClaudeLog][5])

2. सही मॉडल स्लैग चुनें
   DeepSeek V3.1 के विशिष्ट OpenRouter स्लैग हैं (जैसे, V3.1/V3 फैमिली एंट्रीज)। एक गलत या पुराना स्लैग भी स्ट्रीमिंग या टूल फेज के दौरान एरर दे सकता है। OpenRouter के DeepSeek पेज पर दिखाए गए सटीक मॉडल आईडी को वेरीफाई करें और उसे अपने राउटर मैपिंग में इस्तेमाल करें। ([OpenRouter][6])

3. "चैट" (न कि "रीज़नर") में बने रहें, जब तक आपने इसके फील्ड्स को मैप नहीं किया है
   यदि आप कोई रीज़निंग वेरिएंट आज़माते हैं जो विशेष रीज़निंग फील्ड्स स्ट्रीम करता है, तो आपके राउटर को उनका अनुवाद करना होगा—नहीं तो क्लॉड कोड उन्हें प्रोसेस नहीं कर पाएगा। स्टैंडर्ड चैट मॉडल को प्राथमिकता दें या अतिरिक्त "थिंकिंग" आउटपुट को तब तक डिसेबल कर दें जब तक आपका ट्रांसफॉर्मर उसे हैंडल नहीं करता। (DeepSeek के डॉक्स OpenAI-शैली की फंक्शन कॉलिंग पर जोर देते हैं; आपको बस उसे ही मैप करना चाहिए।) ([DeepSeek API Docs][3])

4. नवीनतम राउटर बिल्ड पर अपडेट करें
   हाल की कम्युनिटी बिल्ड्स में गैर-Anthropic प्रोवाइडर्स के लिए कम्पैटिबिलिटी ट्वीक्स जोड़े गए हैं; टेस्टिंग से पहले अपग्रेड करें। ([GitHub][4])

यह समस्या केवल V3.1 के साथ ही क्यों होती है
V3.1 ने डिफ़ॉल्ट रूप से मजबूत एजेंट/टूल-कॉलिंग जोड़ी है। इससे संभावना बढ़ जाती है कि आपका क्लॉड कोड फ्लो अन-ट्रांसलेटेड टूल मैसेज से टकराएगा, जहां ठीक इसी स्कीमा मिसमैच की समस्या होती है। ([DeepSeek API Docs][7])

यदि आप सटीक एरर टेक्स्ट शेयर करते हैं, तो मैं आपकी कॉन्फ़िग में डालने के लिए सटीक ट्रांसफॉर्मर स्निपेट बता सकता हूं।

[1]: https://www.anthropic.com/engineering/claude-code-best-practices?utm_source=chatgpt.com "Claude Code: Best practices for agentic coding"
[2]: https://openrouter.ai/docs/features/tool-calling?utm_source=chatgpt.com "Tool & Function Calling"
[3]: https://api-docs.deepseek.com/guides/function_calling?utm_source=chatgpt.com "Function Calling"
[4]: https://github.com/musistudio/claude-code-router?utm_source=chatgpt.com "musistudio/claude-code-router"
[5]: https://claudelog.com/claude-code-mcps/claude-code-router/?utm_source=chatgpt.com "Claude Code Router"
[6]: https://openrouter.ai/models?q=deepseek&utm_source=chatgpt.com "Models: 'deepseek'"
[7]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 Release"