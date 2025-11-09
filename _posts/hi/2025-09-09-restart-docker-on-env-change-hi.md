---
audio: false
date: 2025-09-09
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: पर्यावरण परिवर्तन के बाद डॉकर कंटेनरों को पुनः आरंभ करें
translated: true
type: note
---

जब आप `.env` को बदलते हैं, तो Docker स्वचालित रूप से उन environment variables को रीलोड नहीं करेगा। containers को नए values प्राप्त करने के लिए आपको उन्हें restart करना होगा। अपने LibreChat setup के लिए, आप इसे इस तरह कर सकते हैं:

1. सुनिश्चित करें कि आप `docker-compose.yml` फ़ाइल वाले उसी directory में हैं।
2. चलाएँ:

```bash
docker compose down
docker compose up -d
```

यह चल रहे containers को बंद करेगा और हटाएगा, फिर उन्हें नए `.env` values के साथ पुनः बनाएगा।

---

### विकल्प: केवल restart करें

यदि आप सब कुछ पूरी तरह से बंद नहीं करना चाहते हैं, तो आप containers को नए environment variables प्राप्त करने के लिए rebuild करने के लिए मजबूर कर सकते हैं:

```bash
docker compose up -d --force-recreate
```

या यदि आपने Dockerfiles या dependencies को भी बदला है, तो `--build` जोड़ें:

```bash
docker compose up -d --build
```

---

✅ संक्षेप में:

* `.env` को edit करने के बाद, हमेशा containers को **पुनः बनाएँ** (`down` + `up` या `up --force-recreate`)।
* एक साधारण `docker compose restart` नए environment values को रीलोड नहीं करेगा, यह केवल पुराने values के साथ restart करता है।

क्या आप चाहते हैं कि मैं आपको यह भी दिखाऊँ कि कैसे **verify** करें कि आपके LibreChat containers नए environment values का उपयोग कर रहे हैं (जैसे `docker inspect` या `docker exec env` के साथ)?