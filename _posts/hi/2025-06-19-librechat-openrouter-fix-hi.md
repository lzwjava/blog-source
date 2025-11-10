---
audio: false
generated: true
image: false
lang: hi
layout: post
model: mistralai/mistral-medium-3.1
title: लिब्रेचैट ओपनराउटर मॉडल त्रुटि को ठीक करना
translated: true
type: note
---

यह त्रुटि तब होती है जब **LibreChat** को **OpenRouter** के साथ बैकेंड के रूप में उपयोग करते हैं, और चुना गया मॉडल (`gpt-5-chat` या इसी तरह का) उपलब्ध नहीं है या ठीक से रूट नहीं हुआ है। यहां मुद्दे और उसे हल करने के तरीके का विवरण दिया गया है:

---

## **यह त्रुटि क्यों होती है**
- **OpenRouter** विभिन्न AI मॉडल्स के लिए एक प्रॉक्सी का काम करता है, लेकिन सभी मॉडल डिफ़ॉल्ट रूप से उपलब्ध या सक्षम नहीं होते हैं।
- `404 No endpoints found that support tool use` त्रुटि का मतलब है कि आपके द्वारा चुना गया मॉडल (`gpt-5-chat`) या तो:
  - OpenRouter द्वारा समर्थित नहीं है।
  - आपके LibreChat सेटअप में कॉन्फ़िगर नहीं है।
  - किसी अलग प्रदाता या API कुंजी की आवश्यकता है।

---

## **इसे कैसे ठीक करें**

### 1. **OpenRouter में उपलब्ध मॉडल्स की जांच करें**
- उपलब्ध मॉडल्स को देखने के लिए [OpenRouter की मॉडल सूची](https://openrouter.ai/models) पर जाएँ।
- अभी के लिए, `gpt-5-chat` कोई आधिकारिक OpenAI मॉडल नहीं है (नवीनतम GPT-4o है)। यदि आपका मतलब GPT-4 था, तो `openai/gpt-4` या इसी तरह के मॉडल का उपयोग करें।

### 2. **LibreChat कॉन्फ़िगरेशन अपडेट करें**
- LibreChat में, **Settings** > **Model Selection** पर जाएं।
- एक ऐसा मॉडल चुनें जो **OpenRouter द्वारा समर्थित** हो (जैसे `openai/gpt-4`, `mistralai/mistral-7b`, आदि)।
- यदि आप सीधे OpenAI का उपयोग करना चाहते हैं, तो **API Provider** को OpenRouter के बजाय **OpenAI** पर स्विच करें।

### 3. **API कुंजियाँ सत्यापित करें**
- सुनिश्चित करें कि आपके पास एक वैध **OpenRouter API key** (यदि OpenRouter उपयोग कर रहे हैं) या **OpenAI API key** (यदि OpenAI उपयोग कर रहे हैं) है।
- कुंजी को LibreChat के **Settings** > **API Keys** में जोड़ें।

### 4. **LibreChat को पुनरारंभ करें**
- सेटिंग्स बदलने के बाद, परिवर्तनों को लागू करने के लिए LibreChat को पुनरारंभ करें।

### 5. **LibreChat दस्तावेज़ीकरण देखें**
- विस्तृत निर्देशों के लिए [LibreChat की OpenRouter सेटअप गाइड](https://github.com/danny-avila/LibreChat#openrouter) देखें।

---

## **वैकल्पिक समाधान**
- यदि आप OpenAI के मॉडल्स का उपयोग करना चाहते हैं, तो प्रदाता को **OpenAI** पर सेट करें और `gpt-4`, `gpt-4o`, या `gpt-3.5-turbo` चुनें।
- यदि आप OpenRouter का उपयोग करना चाहते हैं, तो उनकी [समर्थित सूची](https://openrouter.ai/models) से एक मॉडल चुनें।

---