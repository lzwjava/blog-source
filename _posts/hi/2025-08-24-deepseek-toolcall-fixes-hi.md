---
audio: false
generated: true
image: false
lang: hi
layout: post
title: डीपसीक टूल कॉल संघर्षों को ठीक करें
translated: true
type: note
---

आप एक **टूल-कॉल वैलिडेशन एरर** का सामना कर रहे हैं। DeepSeek (OpenAI-स्टाइल) का उपयोग एक Claude Code फ्लो में किया जा रहा है जो Anthropic-स्टाइल टूल मैसेजेस की अपेक्षा करता है। दो सुरक्षित ठीक करने के तरीके:

*   **सभी Claude Code कार्य को Anthropic (प्रॉक्सी के माध्यम से) पर रूट करें**।
*   **जब आप DeepSeek का उपयोग *करें*, तो टूल्स बंद कर दें** (ताकि यह केवल सादा टेक्स्ट लौटाए) और रीजनिंग स्ट्रीम्स को दबा दें।

यहां एक अपडेटेड सिंगल-फाइल कॉन्फ़िग है जो दोनों करती है। इसे ज्यों का त्यों पेस्ट करें:

```json
{
  "PROXY_URL": "http://127.0.0.1:7890",
  "LOG": true,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "",
      "models": [
        "moonshotai/kimi-k2",
        "anthropic/claude-sonnet-4",
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.7-sonnet:thinking",
        "anthropic/claude-opus-4",
        "google/gemini-2.5-flash",
        "google/gemini-2.5-pro",
        "deepseek/deepseek-chat-v3-0324",
        "deepseek/deepseek-chat-v3.1",
        "deepseek/deepseek-r1",
        "mistralai/mistral-medium-3.1",
        "qwen/qwen3-coder",
        "openai/gpt-oss-120b",
        "openai/gpt-5",
        "openai/gpt-5-mini",
        "x-ai/grok-3-mini"
      ],
      "transformer": {
        "use": ["openrouter"]
      },
      "params": {
        "deepseek/deepseek-chat-v3.1": {
          "tool_choice": "none",
          "reasoning": { "exclude": true }
        },
        "deepseek/deepseek-r1": {
          "tool_choice": "none",
          "reasoning": { "exclude": true }
        }
      }
    },
    {
      "name": "anthropic-proxy",
      "api_base_url": "http://127.0.0.1:3000/v1/messages",
      "api_key": "",
      "models": [
        "anthropic/claude-sonnet-4",
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.7-sonnet:thinking",
        "anthropic/claude-opus-4"
      ]
    }
  ],
  "Router": {
    "default": "anthropic-proxy,anthropic/claude-sonnet-4",
    "background": "anthropic-proxy,anthropic/claude-sonnet-4",
    "think": "anthropic-proxy,anthropic/claude-sonnet-4",
    "longContext": "openrouter,moonshotai/kimi-k2",
    "longContextThreshold": 2000,
    "webSearch": "openrouter,mistralai/mistral-medium-3.1",
    "overrides": {
      "deepseek/deepseek-chat-v3.1": "openrouter,deepseek/deepseek-chat-v3.1",
      "deepseek/deepseek-r1": "openrouter,deepseek/deepseek-r1",
      "google/gemini-2.5-flash": "openrouter,google/gemini-2.5-flash",
      "google/gemini-2.5-pro": "openrouter,google/gemini-2.5-pro",
      "qwen/qwen3-coder": "openrouter,qwen/qwen3-coder",
      "openai/gpt-5-mini": "openrouter,openai/gpt-5-mini"
    }
  }
}
```

यह क्या करता है:

*   Claude Code पाथ (`default/background/think`) **Anthropic को `anthropic-proxy` के माध्यम से** जाते हैं, इसलिए टूल यूज़ काम करता है।
*   DeepSeek उपलब्ध रहता है, लेकिन `"tool_choice":"none"` और `"reasoning.exclude": true` के साथ, इसलिए यह टूल कॉल या थिंकिंग चंक्स उत्पन्न नहीं करेगा जो आपके IDE एजेंट को तोड़ते हैं।
*   आप अभी भी स्पष्ट रूप से DeepSeek चुन सकते हैं (उदाहरण के लिए, सादी चैट या ड्राफ्टिंग के लिए), और यह OpenRouter के माध्यम से साफ-सुथरे ढंग से रूट हो जाएगा।

यदि आपको अभी भी "Invalid tool parameters" दिखाई देता है, तो इसका मतलब है कि कोई न कोई लेयर *अभी भी* DeepSeek को टूल कॉल उत्पन्न करने दे रहा है। उस स्थिति में, सुनिश्चित करें कि आपका रनर वास्तव में प्रति-मॉडल `params` का सम्मान करता है। यदि यह नहीं करता है, तो अपने DeepSeek उपयोग को केवल उन्हीं संदर्भों में सेट करें जहां टूल्स अक्षम हैं, या `default` को वापस `openai/gpt-5-mini` पर सेट करें और DeepSeek को मैन्युअल "no-tools" प्रोफाइल के लिए आरक्षित कर दें।