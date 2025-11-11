---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: सर्वश्रेष्ठ सस्ते कोडिंग मॉडल ओपनराउटर के माध्यम से
translated: true
type: note
---

### कोडेक्स CLI के माध्यम से OpenRouter पर कोडिंग के लिए सर्वोत्तम सस्ते मॉडल

हाल के बेंचमार्क, उपयोगकर्ता चर्चाओं और 2025 तक के मॉडल रैंकिंग के आधार पर, यहाँ कोडेक्स CLI में कोडिंग टास्क्स के लिए GPT-5-Codex के कुछ बेहतरीन और किफायती विकल्प दिए गए हैं। GPT-5-Codex वास्तव में महंगा है (अक्सर $20-50 इनपुट / $60-150 आउटपुट प्रति मिलियन टोकन के दायरे में, प्रदाता के आधार पर), इसलिए ये सुझाव मजबूत कोडिंग परफॉर्मेंस वाले किफायती विकल्पों पर केंद्रित हैं। OpenRouter का पे-पर-यूज़ मॉडल का मतलब है कि आप केवल प्रोसेस किए गए टोकन के लिए भुगतान करते हैं, और कई मॉडल्स में फ्री टियर या बहुत कम दरें (इनपुट/आउटपुट के लिए संयुक्त रूप से प्रति मिलियन टोकन $1 से कम) हैं।

मैंने SWE-Bench, HumanEval, या Aider जैसे कोडिंग बेंचमार्क पर उच्च स्कोर करने वाले मॉडल्स को प्राथमिकता दी है, जो सस्ते या मुफ्त हैं। मॉडल ID आपकी `config.toml` में आसान उपयोग के लिए फॉर्मेटेड हैं (जैसे, `model = "provider/model-name"`)। वर्तमान कीमतों के लिए, OpenRouter के मॉडल्स पेज को चेक करें, क्योंकि दरें थोड़ी बहुत बदल सकती हैं।

#### शीर्ष सिफारिशें:
- **Grok Code Fast (xAI)**
  मॉडल ID: `xai/grok-code-fast`
  क्यों: कोडिंग के लिए OpenRouter की LLM रैंकिंग में शीर्ष पर, स्पीड और एजेंटिक टास्क्स (जैसे, International Olympiad in Informatics में #1) में उत्कृष्ट। अक्सर बेसिक उपयोग के लिए मुफ्त, जिससे यह प्लेटफॉर्म पर सबसे अधिक इस्तेमाल किया जाने वाला मॉडल है। इटरेटिव कोडिंग वर्कफ़्लो के लिए बढ़िया।
  कीमत: मुफ्त या ~$0.50/$2.00 प्रति 1M टोकन (इनपुट/आउटपुट)। कॉन्टेक्स्ट: 128K टोकन।

- **Kat Coder Pro (KwaiPilot)**
  मॉडल ID: `kwaipilot/kat-coder-pro:free`
  क्यों: विशेष कोडिंग मॉडल जिसने SWE-Bench Verified पर 73.4% स्कोर किया, शीर्ष मालिकाना मॉडल्स के करीब। सीमित समय के लिए मुफ्त, कॉम्प्लेक्स रीजनिंग और कोड जनरेशन के लिए आदर्श।
  कीमत: मुफ्त (प्रोमो)। कॉन्टेक्स्ट: 256K टोकन, आउटपुट 32K तक।

- **DeepSeek Coder V3 (DeepSeek)**
  मॉडल ID: `deepseek/deepseek-coder-v3`
  क्यों: Aider कोडिंग स्कोर पर ~71% के साथ उत्कृष्ट मूल्य, इम्प्लीमेंटेशन और डीबगिंग के लिए मजबूत। फोरम्स में बजट कोडिंग के लिए अक्सर सुझाया जाता है।
  कीमत: बहुत सस्ता (~$0.14/$0.28 प्रति 1M)। कॉन्टेक्स्ट: 128K टोकन।

- **Llama 4 Maverick (Meta)**
  मॉडल ID: `meta/llama-4-maverick`
  क्यों: कोडिंग क्वालिटी और VS Code इंटीग्रेशन (जैसे, RooCode जैसे टूल्स के साथ) के लिए फ्री टियर में सर्वश्रेष्ठ। रियल-वर्ल्ड कोड टास्क्स पर अच्छा प्रदर्शन।
  कीमत: फ्री टियर उपलब्ध, या कम लागत (~$0.20/$0.80 प्रति 1M)। कॉन्टेक्स्ट: 128K टोकन।

- **Mistral Devstral Small (Mistral)**
  मॉडल ID: `mistral/devstral-small`
  क्यों: कीमत, फास्ट थ्रूपुट और कोड इम्प्लीमेंटेशन में अच्छा होने के लिए ऑप्टिमाइज़्ड। अक्सर हाइब्रिड वर्कफ़्लो के लिए बड़े मॉडल्स के साथ जोड़ा जाता है।
  कीमत: सस्ता (~$0.25/$1.00 प्रति 1M)। कॉन्टेक्स्ट: 128K टोकन।

- **Qwen3 235B (Qwen)**
  मॉडल ID: `qwen/qwen3-235b`
  क्यों: कोडिंग बेंचमार्क पर उच्च प्रदर्शन, लागत-अनुकूलित सेटअप के लिए सुझाया गया। बड़े पैमाने की कोड प्रोजेक्ट्स को अच्छी तरह से संभालता है।
  कीमत: किफायती (~$0.50/$2.00 प्रति 1M)। कॉन्टेक्स्ट: 128K टोकन।

- **Gemini 2.5 Flash (Google)**
  मॉडल ID: `google/gemini-2.5-flash`
  क्यों: रैंकिंग में #3, इटरेटिव कोडिंग के लिए तेज़ और कम लागत वाला। यदि आपके कोड में डेटा विज़ुअलाइज़ेशन शामिल है तो मल्टीमॉडल टास्क्स के लिए अच्छा।
  कीमत: सस्ता (~$0.35/$1.05 प्रति 1M)। कॉन्टेक्स्ट: 1M टोकन।

ये मॉडल OpenAI-संगत हैं, इसलिए प्रोवाइडर को "openrouter" और अपनी API key सेट करने के बाद ये Codex CLI में सीमलेस काम करेंगे। Grok Code Fast या Kat Coder जैसे मुफ्त मॉडल्स से टेस्ट करना शुरू करें। कोडिंग-विशिष्ट उपयोग के लिए, SWE-Bench स्कोर देखें—उच्च स्कोर का मतलब है रियल GitHub इश्यूज को सुलझाने में बेहतर। यदि आपको अधिक कॉन्टेक्स्ट या स्पीड चाहिए, तो सस्ते मॉडल्स पर ऑटो-फॉलबैक के लिए OpenRouter के रूटिंग के साथ जोड़ें।

एकीकृत करने के लिए: अपनी `config.toml` में, `[profiles cheap-coder]` जैसा प्रोफाइल जोड़ें जिसमें `model_provider = "openrouter"` और `model = "one-of-the-IDs-above"` हो।

[Top AI Models on OpenRouter 2025: Performance vs Cost Guide](https://www.teamday.ai/blog/top-ai-models-openrouter-2025)
[Best Budget Coding LLMs 2025: DeepSeek R1 vs Gemini vs GPT](https://llmx.de/blog/budget-coding-llms-2025/)
[What are the best LLMs available on OpenRouter to use for coding](https://medium.com/@okreitz/what-are-the-best-llms-available-on-openrouter-to-use-for-coding-with-kilo-ca04e75a84ee)
[Best Free AI Models You Can Use on OpenRouter](https://apidog.com/blog/free-ai-models/)
[Top AI Coding Models in 2025](https://www.veerotech.net/blog/top-ai-coding-models-in-2025-boost-your-development-workflow-with-these-game-changers/)
[LLM Rankings - OpenRouter](https://openrouter.ai/rankings)
[Top 5 AI Coding Models of March 2025](https://dev.to/apipie-ai/top-5-ai-coding-models-of-march-2025-5f04)
[Models - OpenRouter](https://openrouter.ai/models)
[whats the best coding model on openrouter? - Reddit](https://www.reddit.com/r/RooCode/comments/1kdu7we/whats_the_best_coding_model_on_openrouter/)