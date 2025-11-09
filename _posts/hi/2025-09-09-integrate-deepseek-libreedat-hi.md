---
audio: false
date: 2025-09-09
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: लिब्रेचैट के साथ डीपसीक एकीकरण गाइड
translated: true
type: note
---

यहाँ **LibreChat में DeepSeek को चलाने का सबसे तेज़ तरीका** है। मैं दो विकल्प दिखाऊंगा—**आधिकारिक DeepSeek API** (सुझाया गया) का उपयोग करें, या **OpenRouter** के माध्यम से जाएं।

---

## विकल्प A — DeepSeek के आधिकारिक API का उपयोग करें (सुझाया गया)

1.  **DeepSeek API key प्राप्त करें**
    अपने DeepSeek अकाउंट में एक बनाएं, फिर base URL नोट करें:
    `https://api.deepseek.com` (या OpenAI-संगत `https://api.deepseek.com/v1`). ([DeepSeek API Docs][1], [deepseek.apidog.io][2])

2.  **`librechat.yaml` में एक DeepSeek endpoint जोड़ें**
    इसे `endpoints:` → `custom:` के अंतर्गत रखें:

```yaml
- name: deepseek
  apiKey: ${DEEPSEEK_API_KEY}
  baseURL: https://api.deepseek.com/v1
  models:
    default: deepseek-chat
    fetch: true
    list:
      - deepseek-chat        # V3 (general)
      - deepseek-coder       # code-centric
      - deepseek-reasoner    # R1 reasoning
  titleConvo: true
  dropParams: null
```

LibreChat एक **DeepSeek** config guide प्रदान करता है और model names (`deepseek-chat`, `deepseek-coder`, `deepseek-reasoner`) की पुष्टि करता है और R1 के अपने "thought process" को stream करने के बारे में नोट्स देता है। ([LibreChat][3])

3.  **`.env` के माध्यम से API key एक्सपोज़ करें**
    आपकी LibreChat `.env` फ़ाइल में:

```
DEEPSEEK_API_KEY=sk-...
```

LibreChat `librechat.yaml` + `.env` के माध्यम से custom OpenAI-संगत प्रदाताओं का समर्थन करता है। ([LibreChat][4])

4.  **अपना stack restart करें**
    अपने LibreChat फ़ोल्डर से:

```bash
docker compose down
docker compose up -d --build
```

(जरूरी है ताकि API container `librechat.yaml` और `.env` को फिर से लोड करे।) यदि आपके custom endpoints दिखाई नहीं देते हैं, तो config errors के लिए `api` container logs जांचें। ([GitHub][5])

---

## विकल्प B — OpenRouter के माध्यम से DeepSeek का उपयोग करें

यदि आप पहले से ही OpenRouter का उपयोग करते हैं, तो बस DeepSeek models को एक OpenRouter endpoint block में पंजीकृत करें।

`librechat.yaml`:

```yaml
- name: openrouter
  apiKey: ${OPENROUTER_KEY}
  baseURL: https://openrouter.ai/api/v1
  models:
    default: deepseek/deepseek-chat
    list:
      - deepseek/deepseek-chat
      - deepseek/deepseek-coder
      - deepseek/deepseek-reasoner
```

LibreChat docs से दो महत्वपूर्ण नोट्स:
• `OPENROUTER_API_KEY` env var name सेट न करें (एक अलग नाम जैसे `OPENROUTER_KEY` का उपयोग करें) नहीं तो आप गलती से OpenAI endpoint को ओवरराइड कर देंगे।
• OpenRouter, LibreChat की custom endpoints सूची में first-class है। ([LibreChat][6])

OpenRouter, DeepSeek models को एक OpenAI-संगत सतह के साथ एक्सपोज़ करता है। ([OpenRouter][7])

---

## सुझाव और सावधानियां

*   **R1 / `deepseek-reasoner`**: यह अपनी chain-of-thought ("thought process") को stream कर सकता है। कुछ OpenAI parameters लागू नहीं हो सकते हैं। यदि आपको अजीब आउटपुट दिखाई देता है, तो पहले `deepseek-chat` के साथ परीक्षण करें। ([LibreChat][3])
*   **Model fetching**: `fetch: true` सेट करने से LibreChat को नवीनतम model list प्राप्त करने की अनुमति मिलती है जब समर्थित हो; अन्यथा आपके द्वारा निर्दिष्ट `list:` का उपयोग किया जाता है। ([LibreChat][8])
*   **ये सेटिंग्स कहां स्थित हैं**: `librechat.yaml` custom endpoints फ़ाइल है; `.env` keys और proxy settings रखती है। ([LibreChat][8])

यदि आप चाहें, तो अपनी वर्तमान `librechat.yaml` पेस्ट करें और मैं इसे साफ-सुथरे तरीके से DeepSeek जोड़ने के लिए पैच कर दूंगा (कोई टेबल नहीं, वादा है)।

[1]: https://api-docs.deepseek.com/?utm_source=chatgpt.com "DeepSeek API Docs: Your First API Call"
[2]: https://deepseek.apidog.io/your-first-api-call-835227m0?utm_source=chatgpt.com "DeepSeek API: Your First API Call"
[3]: https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/deepseek?utm_source=chatgpt.com "Deepseek"
[4]: https://www.librechat.ai/docs/quick_start/custom_endpoints?utm_source=chatgpt.com "Custom Endpoints"
[5]: https://github.com/danny-avila/LibreChat/discussions/2487?utm_source=chatgpt.com "Fix the librechat.yaml file in the main repository. #2487"
[6]: https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/openrouter?utm_source=chatgpt.com "Openrouter"
[7]: https://openrouter.ai/deepseek/deepseek-v3-base%3Afree/api?utm_source=chatgpt.com "DeepSeek V3 Base – Run with an API"
[8]: https://www.librechat.ai/docs/configuration/librechat_yaml?utm_source=chatgpt.com "librechat.yaml config file"