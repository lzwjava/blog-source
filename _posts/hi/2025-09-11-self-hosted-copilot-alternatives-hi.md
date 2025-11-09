---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: स्व होस्टेड स्थानीय कोपायल्ट विकल्प
translated: true
type: note
---

आप स्थानीय रूप से "Copilot जैसा" अनुभव सेल्फ-होस्ट करने के लिए ओपन-सोर्स टूल्स की तलाश में हैं—ऐसे टूल जिन्हें आप खुद चला सकते हैं (अपने खुद के टोकन या मॉडल के साथ), शायद VS Code या अन्य IDE में इंटीग्रेटेड। कोई टेबल नहीं, बस साफ, स्पष्ट व्याख्याएं। यहां सबसे प्रसिद्ध विकल्प दिए गए हैं:

---

### **Tabby**

रस्ट में लिखा गया एक सेल्फ-होस्टेड AI कोडिंग असिस्टेंट। यह ओपन-सोर्स है, किसी बाहरी सेवा की आवश्यकता नहीं है, और एक OpenAPI-स्टाइल इंटरफेस प्रदान करता है—जिससे स्थानीय IDE और इन्फ्रास्ट्रक्चर के साथ इंटीग्रेशन सीधा हो जाता है। यह कंज्यूमर-ग्रेड GPU और Vim/Neovim सहित एडिटर इंटीग्रेशन को भी सपोर्ट करता है। ([GitHub][1], [Software Recommendations Stack Exchange][2])

---

### **FauxPilot**

GitHub Copilot के एक स्थानीय रूप से होस्ट किए गए विकल्प के रूप में डिजाइन किया गया एक ओपन-सोर्स प्रोजेक्ट। यह Salesforce के CodeGen मॉडल का लाभ उठाता है जो NVIDIA के Triton Inference Server (और FasterTransformer) के माध्यम से चलते हैं। Docker के माध्यम से डिप्लॉय करने योग्य, यह Copilot-जैसे क्लाइंट के साथ संगत है और एक सक्षम GPU के साथ सबसे अच्छा काम करता है। ([GitHub][3])

---

### **Privy**

एक और MIT-लाइसेंस्ड, ओपन-सोर्स टूल जो स्थानीय रूप से चलता है। यह GitHub Copilot के समान रीयल-टाइम कोड कम्प्लीशन और चैट फंक्शनैलिटी प्रदान करता है। यह Ollama, llama.cpp, या llamafile जैसे LLM रनटाइम के साथ इंटीग्रेट हो सकता है, और आपके हार्डवेयर के आधार पर लोकप्रिय कोडिंग मॉडल (जैसे CodeLlama वेरिएंट) को सपोर्ट करता है। ([GitHub][4])

---

### **GPT4All, Continue, LocalPilot** *(और इसी तरह के)*

Tabby और FauxPilot के साथ-साथ कई सेल्फ-होस्टेड टूल्स में उल्लेखित; ये स्थानीय, प्राइवेसी-केंद्रित कोडिंग सहायता प्रदान करते हैं। हालांकि हमेशा उतने पॉलिश्ड नहीं होते, लेकिन यदि हार्डवेयर की बाधाएं या विशिष्ट वर्कफ़्लो मांगते हैं तो ये व्यवहार्य हैं। ([Virtualization Howto][5])

---

### **Ollama (Docker के साथ)**

अपने आप में एक पूर्ण Copilot रिप्लेसमेंट नहीं, बल्कि LLM को स्थानीय रूप से चलाने के लिए एक शक्तिशाली ओपन-सोर्स टूल। आप Docker के माध्यम से Ollama का उपयोग करके Phi-2 जैसे मॉडल होस्ट कर सकते हैं, और फिर एक LLM एक्सटेंशन (जैसे Hugging Face का `llm-vscode`) का उपयोग करके VS Code से उनसे कनेक्ट हो सकते हैं। यह आपको अनिवार्य रूप से एक स्थानीय मॉडल से चैट करने या कोड सहायता प्राप्त करने की अनुमति देता है। ([Tommaso Colella][6], [Reddit][7])

---

### **कम्युनिटी बज़**

Reddit चर्चाओं से:

* "Ollama AI के साथ एक Docker सर्वर पर अपना खुद का 'Copilot' मुफ्त में सेल्फ होस्ट करें" — Ollama की प्रभावशीलता और VS Code के साथ इंटीग्रेशन पर प्रकाश डालता है। ([Reddit][7])
* "Tabby (अब) सबसे लोकप्रिय 'ओपन-सोर्स और लोकल' टूल है" — इसके बढ़ते अपनाने की ओर इशारा करता है। ([Reddit][8])

---

### **सारांश सिफारिशें**

* **यदि आप एक पॉलिश्ड, ओपन-सोर्स Copilot विकल्प चाहते हैं:** **Tabby** से शुरुआत करें।
* **यदि आप Copilot के इन्फ्रास्ट्रक्चर के करीब कुछ चाहते हैं (और एक ठोस GPU है):** **FauxPilot** देखें।
* **यदि आप मॉडल/रनटाइम पर लचीलापन के साथ कोड + चैट फीचर्स चाहते हैं:** **Privy** आज़माएं।
* **एंडपॉइंट और मॉडल पर पूरा कंट्रोल चाहते हैं?** **Ollama** को अपने खुद के LLM के साथ जोड़ें, फिर स्टैंडर्ड LLM इंटरफेस का उपयोग करके कनेक्ट करें।

---

### **आपके लिए अगले कदम**

1.  **हार्डवेयर का आकलन करें:** FauxPilot और Privy को एक अच्छे GPU की आवश्यकता हो सकती है; Tabby अधिक हल्का है।
2.  **एक रनटाइम/फ्रेमवर्क चुनें:**
    *   **Tabby**: एडिटर सपोर्ट के साथ बढ़िया ऑल-राउंड चॉइस।
    *   **FauxPilot**: Docker और Triton के साथ Copilot-जैसा।
    *   **Privy**: लचीला, मॉडल-अग्नोस्टिक सेटअप।
    *   **Ollama + LLM**: शुद्ध DIY—बढ़िया अगर आप एंडपॉइंट खुद बनाने में सहज हैं।
3.  **अपने IDE से कनेक्ट करें:** VS Code (या अन्य) इन्हें स्थानीय एंडपॉइंट के माध्यम से उपयोग करने का समर्थन करते हैं, बिल्कुल Copilot की तरह।

मुझे बताएं कि क्या आप किसी विशिष्ट टूल के साथ शुरुआत करने में मदद या सेटअप के लिए वॉकथ्रू चाहते हैं!

[1]: https://github.com/TabbyML/tabby?utm_source=chatgpt.com "TabbyML/tabby: Self-hosted AI coding assistant"
[2]: https://softwarerecs.stackexchange.com/questions/90507/foss-alternative-to-github-copilot?utm_source=chatgpt.com "FOSS alternative to GitHub Copilot?"
[3]: https://github.com/fauxpilot/fauxpilot?utm_source=chatgpt.com "FauxPilot - an open-source alternative to ..."
[4]: https://github.com/srikanth235/privy?utm_source=chatgpt.com "srikanth235/privy: An open-source alternative to ..."
[5]: https://www.virtualizationhowto.com/2025/05/best-self-hosted-github-copilot-ai-coding-alternatives/?utm_source=chatgpt.com "Best Self-hosted GitHub Copilot AI Coding Alternatives"
[6]: https://gioleppe.github.io/posts/diy-copilot-phi/?utm_source=chatgpt.com "DIY self-hosted Copilot using Phi-2 and Ollama"
[7]: https://www.reddit.com/r/vscode/comments/1by7njo/self_host_your_own_copilot_for_free_with_ollama/?utm_source=chatgpt.com "Self host your own \"Copilot\" for FREE with Ollama AI on a ..."
[8]: https://www.reddit.com/r/LocalLLaMA/comments/12m8fnm/best_local_equivalent_of_github_copilot/?utm_source=chatgpt.com "Best local equivalent of GitHub Copilot? : r/LocalLLaMA"