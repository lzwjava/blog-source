---
audio: false
date: 2025-09-06
generated: true
image: false
lang: hi
layout: post
title: लागत और प्रदर्शन के लिए इष्टतम मॉडल चयन
translated: true
type: note
---

आपके Claude Code कॉन्फ़िगरेशन को देखते हुए, आप लागत और प्रदर्शन दोनों के लिए ऑप्टिमाइज़ करना चाहते हैं। आपके राउटर सेटअप में "सस्ते और शक्तिशाली" मॉडल चुनने के लिए यहां कुछ सिफारिशें दी गई हैं:

## आपकी सूची से सर्वश्रेष्ठ लागत/प्रदर्शन वाले मॉडल:

**अधिकांश कार्यों के लिए (डिफ़ॉल्ट):**
- `deepseek/deepseek-chat-v3.1` - बहुत कम लागत पर उत्कृष्ट प्रदर्शन
- `deepseek/deepseek-r1` - शानदार रीजनिंग क्षमताएं, फिर भी लागत-प्रभावी

**बैकग्राउंड कार्यों के लिए:**
- `deepseek/deepseek-chat-v3.1` - पहले से ही एक अच्छा विकल्प
- `google/gemini-2.5-flash` - तेज़ और सस्ता

**सोचने/रीजनिंग के लिए:**
- `deepseek/deepseek-r1` - विशेष रूप से रीजनिंग कार्यों के लिए डिज़ाइन किया गया
- `z-ai/glm-4.5` - आपका वर्तमान विकल्प ठीक है

**अपडेटेड राउटर सुझाव:**
```json
"Router": {
  "default": "openrouter,deepseek/deepseek-chat-v3.1",
  "background": "openrouter,google/gemini-2.5-flash", 
  "think": "openrouter,deepseek/deepseek-r1",
  "longContext": "openrouter,moonshotai/kimi-k2",
  "webSearch": "openrouter,google/gemini-2.5-flash"
}
```

## मुख्य विचार:
- **DeepSeek मॉडल** वर्तमान में सबसे अच्छा मूल्य/प्रदर्शन अनुपात प्रदान करते हैं
- **Gemini 2.5 Flash** सरल कार्यों के लिए बहुत तेज़ और सस्ता है
- **Kimi** को लंबे कॉन्टेक्स्ट के लिए रखें क्योंकि यह 200k+ टोकन अच्छी तरह संभालता है
- **Gemini 2.5 Pro** यदि आपको Flash से अधिक क्षमता की आवश्यकता है

आप सटीक लागतों की तुलना करने के लिए OpenRouter की वेबसाइट पर वर्तमान मूल्य जांच सकते हैं, लेकिन DeepSeek मॉडल आमतौर पर GPT-4 स्तर के मॉडल की तुलना में 10-20x सस्ते होते हैं, जबकि प्रतिस्पर्धी प्रदर्शन प्रदान करते हैं।