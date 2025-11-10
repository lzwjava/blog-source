---
audio: false
generated: true
image: false
lang: hi
layout: post
title: एआई मॉडल संदर्भ विंडो क्षमताएँ
translated: true
type: note
---

यहाँ आपके द्वारा सूचीबद्ध मॉडल्स की **वर्तमान अधिकतम टोकन क्षमताएँ (संदर्भ विंडो आकार)** दी गई हैं, जो हालिया दस्तावेज़ीकरण और घोषणाओं पर आधारित हैं:

---

### Anthropic मॉडल

* **Claude Opus 4 / Opus 4.1**
  **200,000 टोकन** की एक संदर्भ विंडो प्रदान करता है, जो निरंतर तर्क और जटिल वर्कफ़्लो के लिए आदर्श है ([Anthropic][1], [Amazon Web Services, Inc.][2])।

* **Claude Sonnet 4**
  यह भी मूल रूप से **200,000 टोकन** के संदर्भ का समर्थन करता है ([Prompthub][3])।
  इसके अतिरिक्त, एक **बीटा अपग्रेड** अब एंटरप्राइज़/API उपयोगकर्ताओं के लिए **विशाल 1 मिलियन टोकन** के संदर्भ को सक्षम करता है ([Anthropic][4])।

---

### Mistral AI मॉडल

* **Mistral Medium 3.1**
  इसकी संदर्भ विंडो **128,000 टोकन** की है ([OpenRouter][5])।

* **Mistral Large 2**
  यह भी **128,000 टोकन** की संदर्भ लंबाई का समर्थन करता है ([Wikipedia][6])।

* **Mistral Medium (पहले के संस्करण)**
  पहले, संदर्भ के लिए मानक **32,000 टोकन** था ([Clarifai][7], [Mistral AI][8])।

* **Mistral Small 3.1**
  इस नए संस्करण में इसकी संदर्भ विंडो को **32K से 128K टोकन** तक अपग्रेड किया गया है ([Wikipedia][6])。

---

### अतिरिक्त नोट्स

* एक विकिपीडिया अवलोकन इस बात की पुष्टि करता है कि **Claude 3 Opus** की **200K टोकन** की संदर्भ विंडो थी, जो कुछ मामलों में **1 मिलियन टोकन** तक विस्तारित हो गई थी ([Wikipedia][9])।

* **Mistral की स्लाइडिंग विंडो अटेंशन मैकेनिज्म** सैद्धांतिक रूप से **4096 × 32 = 131,072 टोकन** तक का समर्थन करता है, जो रिपोर्ट किए गए 128K आंकड़ों के करीब है ([Hugging Face][10])।

---

### सारांश (संक्षिप्त प्रारूप)

* **Claude Opus 4 / 4.1**: 200,000 टोकन
* **Claude Sonnet 4**: 200,000 टोकन (मानक), **1 मिलियन टोकन** तक (बीटा/एंटरप्राइज़)
* **Mistral Medium 3.1**: 128,000 टोकन
* **Mistral Large 2**: 128,000 टोकन
* **Mistral Small 3.1**: 128,000 टोकन (32K से अपग्रेड)

---

यदि आप अन्य मॉडल्स या आर्किटेक्चर-विशिष्ट क्षमताओं पर अधिक जानकारी चाहते हैं तो मुझे बताएं!

* [The Verge](https://www.theverge.com/ai-artificial-intelligence/757998/anthropic-just-made-its-latest-move-in-the-ai-coding-wars?utm_source=chatgpt.com)
* [Tom's Guide](https://www.tomsguide.com/ai/anthropic-looks-to-beat-gpt-5-and-grok-4-with-this-one-major-upgrade?utm_source=chatgpt.com)

[1]: https://www.anthropic.com/claude/opus?utm_source=chatgpt.com "Claude Opus 4.1"
[2]: https://aws.amazon.com/bedrock/anthropic/?utm_source=chatgpt.com "Anthropic's Claude in Amazon Bedrock"
[3]: https://www.prompthub.us/blog/the-complete-guide-to-claude-opus-4-and-claude-sonnet-4?utm_source=chatgpt.com "The Complete Guide to Claude Opus 4 and Claude Sonnet 4"
[4]: https://www.anthropic.com/news/1m-context?utm_source=chatgpt.com "Claude Sonnet 4 now supports 1M tokens of context"
[5]: https://openrouter.ai/mistralai/mistral-medium-3.1?utm_source=chatgpt.com "Mistral Medium 3.1 - API, Providers, Stats"
[6]: https://en.wikipedia.org/wiki/Mistral_AI?utm_source=chatgpt.com "Mistral AI"
[7]: https://clarifai.com/mistralai/completion/models/mistral-medium?utm_source=chatgpt.com "mistral-medium model | Clarifai - The World's AI"
[8]: https://mistral.ai/news/mistral-large?utm_source=chatgpt.com "Au Large"
[9]: https://en.wikipedia.org/wiki/Claude_%28language_model%29?utm_source=chatgpt.com "Claude (language model)"
[10]: https://huggingface.co/docs/transformers/en/model_doc/mistral?utm_source=chatgpt.com "Mistral"