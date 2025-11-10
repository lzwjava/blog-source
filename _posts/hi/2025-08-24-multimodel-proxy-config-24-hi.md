---
audio: false
generated: true
image: false
lang: hi
layout: post
title: अद्यतन बहु-मॉडल प्रॉक्सी कॉन्फ़िग मार्गदर्शिका
translated: true
type: note
---

यहाँ आपके अपडेटेड कॉन्फ़िग के लिए है - इसे अपने कॉन्फ़िग में जोड़ दें:

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
    "default": "openrouter,openai/gpt-5-mini",
    "background": "openrouter,google/gemini-2.5-flash",
    "think": "openrouter,qwen/qwen3-coder",
    "longContext": "openrouter,moonshotai/kimi-k2",
    "longContextThreshold": 2000,
    "webSearch": "openrouter,mistralai/mistral-medium-3.1",
    "overrides": {
      "anthropic/claude-sonnet-4": "anthropic-proxy,anthropic/claude-sonnet-4",
      "anthropic/claude-3.5-sonnet": "anthropic-proxy,anthropic/claude-3.5-sonnet",
      "anthropic/claude-3.7-sonnet:thinking": "anthropic-proxy,anthropic/claude-3.7-sonnet:thinking",
      "anthropic/claude-opus-4": "anthropic-proxy,anthropic/claude-opus-4",
      "deepseek/deepseek-chat-v3.1": "openrouter,deepseek/deepseek-chat-v3.1"
    }
  }
}
```

यदि आपका रनर DeepSeek पर रीजनिंग स्ट्रीम्स को दबाने के लिए कोई फ़्लैग एक्सपोज़ करता है (जिसे कभी-कभी `reasoning.exclude` या इसी तरह का नाम दिया जाता है), तो `deepseek/deepseek-chat-v3.1` के लिए इसे सक्षम करें ताकि UI पार्सिंग में आने वाली दिक्कतों से बचा जा सके।