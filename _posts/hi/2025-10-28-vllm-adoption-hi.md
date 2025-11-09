---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: एआई प्रदाताओं द्वारा वीएलएलएम अपनाना
translated: true
type: note
---

### AI प्रदाताओं द्वारा vLLM का उपयोग

vLLM एक ओपन-सोर्स इंफरेंस इंजन है जिसे ओपन-वेट मॉडल को कुशलतापूर्वक सर्व करने के लिए आमतौर पर सिफारिश की जाती है। हालाँकि, उत्पादन सेवाओं में इसके अपनाने का तरीका अलग-अलग है। उपलब्ध जानकारी के आधार पर यहाँ विवरण दिया गया है:

| प्रदाता/मॉडल | क्या उत्पादन में vLLM का उपयोग करता है? | विवरण |
|---------------|---------------------------|---------|
| **क्लॉड (एंथ्रोपिक)** | नहीं | एंथ्रोपिक क्लॉड मॉडल को सर्व करने के लिए मालिकाना इन्फ्रास्ट्रक्चर पर निर्भर करता है। vLLM एंथ्रोपिक के API की नकल करने वाले स्थानीय या तीसरे पक्ष के डेप्लॉयमेंट के लिए संगतता प्रदान करता है, लेकिन आंतरिक उपयोग का कोई सबूत नहीं है। |
| **ओपनएआई (जीपीटी मॉडल)** | नहीं | ओपनएआई पैमाने के लिए अनुकूलित कस्टम, इन-हाउस सर्विंग सिस्टम का उपयोग करता है। vLLM स्थानीय इंफरेंस के लिए ओपनएआई-संगत API का समर्थन करता है, लेकिन ओपनएआई अपने उत्पादन का आधार vLLM पर नहीं रखता है। |
| **मिनीमैक्स AI** | नहीं | मिनीमैक्स मिनीमैक्स-एम1/एम2 जैसे मॉडल ओपन-सोर्स करता है और इसके प्रदर्शन के कारण उपयोगकर्ता डेप्लॉयमेंट के लिए vLLM की सिफारिश करता है। उनके मुख्य उत्पादन API में vLLM के उपयोग की कोई पुष्टि नहीं है; वे फोर्क या कस्टम सेटअप का उपयोग कर सकते हैं। |
| **किमी (मूनशॉट AI)** | नहीं | मूनशॉट किमी-के2 के सेल्फ-होस्टिंग के लिए vLLM की सिफारिश करता है, और उनका चेकपॉइंट-इंजन टूल वजन अपडेट के लिए इसके साथ एकीकृत होता है। हालाँकि, उनका उत्पादन इंफरेंस संभवतः SGLang या TensorRT-LLM जैसे इंजनों के साथ-साथ मालिकाना ऑप्टिमाइजेशन का उपयोग करता है। |
| **डीपसीक AI** | हाँ | डीपसीक ने vLLM पर सीधे बने एक कस्टम इंफरेंस इंजन को ओपन-सोर्स किया है, जिसमें उनके शोध से ऑप्टिमाइजेशन शामिल हैं। इसका उपयोग डीपसीक-वी3 और आर1 जैसे मॉडल के लिए किया जाता है, और vLLM प्रोजेक्ट में योगदान वापस किया जाता है। |

### संदर्भ
- [DeepSeek Open-Sources Custom Inference Engine Built on vLLM](https://www.ainews.com/p/deepseek-open-sources-custom-inference-engine-built-on-vllm)
- [The path to open-sourcing the DeepSeek inference engine](https://news.ycombinator.com/item?id=43682088)
- [MiniMax-M1 Hybrid Architecture Meets vLLM](https://blog.vllm.ai/2025/06/30/minimax-m1.html)
- [Kimi K2: Open Agentic Intelligence](https://moonshotai.github.io/Kimi-K2/)
- [OpenAI-Compatible Server - vLLM](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html)
- [Support Anthropic API `/v1/messages` endpoint · Issue #21313 · vllm-project/vllm](https://github.com/vllm-project/vllm/issues/21313)