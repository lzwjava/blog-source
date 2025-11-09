---
audio: false
date: 2025-09-13
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: नवीनतम एआई मॉडल और उनके अनुप्रयोग
translated: true
type: note
---

यहाँ हमारे पास ज्ञात जानकारी (सितंबर 2025 के मध्य तक) का सारांश है कि GPT-5, Gemini 2.5 Pro, GPT-5 mini के बारे में क्या पता है, और उनका उपयोग कैसे किया जा रहा है, जिसमें Copilot / प्रीमियम मॉडल शामिल हैं:

---

## GPT-5 (OpenAI)

* **रिलीज़ तिथि**: 7 अगस्त, 2025. ([OpenAI][1])
* **यह क्या है**: एक एकीकृत LLM जिसमें बेहतर रीजनिंग, कम हेलुसिनेशन, कोडिंग, गणित, लेखन, स्वास्थ्य, विजुअल परसेप्शन आदि में बेहतर प्रदर्शन शामिल है। इसमें अधिक मांग वाले कार्यों के लिए "GPT-5 pro" संस्करण शामिल है। ([OpenAI][1])
* **रीजनिंग / सोच**: GPT-5 में एक आंतरिक तंत्र ("फास्ट" बनाम "डीपर रीजनिंग") है और उपयोगकर्ता अधिक गहन रीजनिंग के लिए "GPT-5 thinking" चुन सकते हैं या "think hard about this" जैसे प्रॉम्प्ट दे सकते हैं। ([OpenAI][1])
* **एक्सेस टियर / सीमाएँ**:

  * सभी ChatGPT उपयोगकर्ताओं (फ्री + पेड) की पहुंच है। ([OpenAI][1])
  * फ्री उपयोगकर्ताओं की उपयोग सीमा अधिक सीमित है, और एक निश्चित उपयोग के बाद उन्हें एक हल्के संस्करण ("GPT-5 mini") पर स्विच किया जा सकता है। ([OpenAI][1])
  * पेड (Plus, Pro, Team, Enterprise, EDU) उपयोगकर्ताओं को उच्च उपयोग सीमा मिलती है; Pro उपयोगकर्ताओं को "GPT-5 pro" मिलता है। ([OpenAI][1])

---

## Gemini 2.5 Pro (Google)

* **रिलीज़ / उपलब्धता**:

  * Gemini 2.5 Pro (प्रायोगिक) की पहली घोषणा 25 मार्च, 2025 को की गई थी। ([blog.google][2])
  * स्थिर ("सामान्य उपलब्धता") Gemini 2.5 Pro 17 जून, 2025 को रिलीज़ किया गया था। ([Google Cloud][3])
* **क्षमताएँ**: यह Gemini 2.5 परिवार में Google का सबसे उन्नत मॉडल है। इसमें बड़ी कॉन्टेक्स्ट विंडो (1 मिलियन टोकन), मजबूत रीजनिंग, कोडिंग, बहुभाषी समर्थन आदि विशेषताएँ शामिल हैं। ([blog.google][2])

---

## GPT-5 mini

* **क्या है / कब**: GPT-5 mini, GPT-5 का एक हल्का/तेज़ संस्करण है जो मध्य अगस्त 2025 में GitHub Copilot (पब्लिक प्रीव्यू) में उपलब्ध हुआ। ([The GitHub Blog][4])
* **कहाँ और कैसे**: यह GitHub Copilot Chat (github.com पर), VS Code में, GitHub Mobile (iOS/Android) पर उपलब्ध है। यह उपयोगकर्ताओं के लिए मॉडल पिकर में भी दिखाई देगा। ([The GitHub Blog][4])
* **प्रीमियम अनुरोध / लागत**: यह GitHub Copilot के पेड प्लान में "प्रीमियम अनुरोध" का उपयोग *नहीं* करता है। यानी, GPT-5 mini का उपयोग करने से "प्रीमियम अनुरोध" कोटा खत्म नहीं होता। ([The GitHub Blog][4])

---

## इनका उपयोग **Copilot / Premium / Microsoft / GitHub** में कैसे किया जाता है

* **GitHub Copilot**:

  * सभी Copilot प्लान (फ्री सहित) के पास अब GPT-5 mini तक पहुंच है। ([The GitHub Blog][4])
  * GPT-5 (पूर्ण संस्करण) केवल पेड Copilot प्लान पर उपलब्ध है। ([The GitHub Blog][5])
  * मॉडल पिकर उपयोगकर्ताओं को उनकी प्लान और संगठन सेटिंग्स के आधार पर GPT-5, GPT-5 mini आदि के बीच चयन करने देता है। ([The GitHub Blog][4])

* **Microsoft Copilot / Copilot Studio / 365 Copilot**:

  * Microsoft अपने Copilot उत्पादों में GPT-5 के उपयोग का समर्थन करता है। उदाहरण के लिए, Copilot Studio का उपयोग करने वाले निर्माता GPT-5 चुन सकते हैं, और विभिन्न GPT-5 वेरिएंट (चैट बनाम रीजनिंग) के बीच ऑटो-रूटिंग आदि है। ([Microsoft Developer][6])
  * प्रीमियम सुविधाओं के लिए आमतौर पर पेड सब्सक्रिप्शन की आवश्यकता होती है। GPT-5 का उपयोग, या उच्च-क्षमता वाले मॉडल, या अधिक रीजनिंग वाले मॉडल अक्सर भुगतान करने वाले उपयोगकर्ताओं या एंटरप्राइज़ टियर तक सीमित होते हैं। ([OpenAI][1])

---

यदि आप चाहें, तो मैं **प्रदर्शन तुलना** (GPT-5 बनाम Gemini 2.5 Pro आदि), या **भविष्य/अफवाह वाली सुविधाओं** के बारे में भी जानकारी दे सकता हूँ। क्या आप ऐसा चाहेंगे?

[1]: https://openai.com/index/introducing-gpt-5/?utm_source=chatgpt.com "Introducing GPT-5"
[2]: https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/?utm_source=chatgpt.com "Gemini 2.5: Our most intelligent AI model"
[3]: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions?utm_source=chatgpt.com "Model versions and lifecycle | Generative AI on Vertex AI"
[4]: https://github.blog/changelog/2025-08-13-gpt-5-mini-now-available-in-github-copilot-in-public-preview/?utm_source=chatgpt.com "GPT-5 mini now available in GitHub Copilot in public preview"
[5]: https://github.blog/changelog/2025-09-09-openai-gpt-5-and-gpt-5-mini-are-now-generally-available-in-github-copilot/?utm_source=chatgpt.com "OpenAI GPT-5 and GPT-5 mini are now generally available ..."
[6]: https://developer.microsoft.com/blog/gpt-5-for-microsoft-developers?utm_source=chatgpt.com "GPT-5 for Microsoft Developers"