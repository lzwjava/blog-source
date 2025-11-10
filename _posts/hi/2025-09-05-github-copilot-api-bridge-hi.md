---
audio: false
generated: true
image: false
lang: hi
layout: post
title: GitHub Copilot API ब्रिज
translated: true
type: note
---

आप **ericc-ch/copilot-api** पर पहुंचे हैं, यह एक GitHub प्रोजेक्ट है जो **GitHub Copilot** को एक लोकल API सर्वर में बदल देता है जो **OpenAI** और **Anthropic** (जैसे, Claude) APIs के साथ संगत है।

यहां एक स्पष्ट विवरण दिया गया है—कोई टेबल नहीं, सीधी बात:

---

### यह क्या है?

* यह एक **रिवर्स-इंजीनियर्ड प्रॉक्सी** है जो आपको GitHub Copilot के साथ परिचित OpenAI-स्टाइल एंडपॉइंट्स जैसे `/v1/chat/completions`, `/v1/models`, और `/v1/embeddings` का उपयोग करके इंटरैक्ट करने देता है। आप Anthropic-संगत एंडपॉइंट्स जैसे `/v1/messages` का भी उपयोग कर सकते हैं ([GitHub][1])।

* अनिवार्य रूप से, यह उन टूल्स को, जो OpenAI या Anthropic APIs का सपोर्ट करते हैं—जैसे Claude Code—GitHub Copilot को उनके बैकएंड के रूप में उपयोग करने देता है ([GitHub][1])।

---

### मुख्य विशेषताएं

* **OpenAI & Anthropic संगतता**: असली OpenAI या Anthropic API की तरह काम करता है ([GitHub][1])।
* **Claude Code इंटीग्रेशन**: एक `--claude-code` फ्लैग के साथ Claude Code में प्लग इन करने के लिए तैयार ([GitHub][1])।
* **उपयोग डैशबोर्ड**: एक बिल्ट-इन वेब इंटरफेस के माध्यम से अपने Copilot API उपयोग और कोटा की निगरानी करें ([GitHub][1])।
* **दर सीमा और स्वीकृति नियंत्रण**: दर-सीमित करने (`--rate-limit`), ऑटो-वेट (`--wait`), मैन्युअल स्वीकृति (`--manual`), और डीबगिंग (टोकन दिखाना) के विकल्प शामिल हैं—GitHub के दुरुपयोग सिस्टम से बचने के लिए बढ़िया ([GitHub][1])।
* **विभिन्न Copilot प्लान्स को सपोर्ट करता है**: व्यक्तिगत, व्यवसाय, या एंटरप्राइज खाते सभी काम करते हैं ([GitHub][1])।

---

### सेटअप और उपयोग

* **आवश्यक शर्तें**: आपको Bun (≥ 1.2.x) और एक GitHub Copilot सब्सक्रिप्शन की आवश्यकता होगी ([GitHub][1])।
* **इंस्टालेशन विकल्प**:

  * **Docker**:

    ```bash
    docker build -t copilot-api .
    docker run -p 4141:4141 -v $(pwd)/copilot-data:/root/.local/share/copilot-api copilot-api
    ```

    या सीधे `GH_TOKEN` के माध्यम से अपना GitHub टोकन पास करें ([GitHub][1])।
  * **npx**:

    ```bash
    npx copilot-api@latest start --port 8080
    ```

    या सिर्फ ऑथेंटिकेट करने के लिए `npx copilot-api@latest auth` ([GitHub][1])।
* **कमांड स्ट्रक्चर**:

  * `start`: API सर्वर लॉन्च करता है (जरूरत पड़ने पर ऑथेंटिकेशन संभालता है)।
  * `auth`: सर्वर चलाए बिना GitHub लॉगिन ट्रिगर करता है।
  * `check-usage`: आपके टर्मिनल में वर्तमान Copilot उपयोग आउटपुट करता है।
  * `debug`: डायग्नोस्टिक जानकारी दिखाता है (वर्जन, ऑथ स्टेटस, आदि), वैकल्पिक `--json` आउटपुट के साथ ([GitHub][1])।

---

### वास्तविक दुनिया की प्रतिक्रिया

Reddit उपयोगकर्ताओं ने अपनी राय दी है:

> "यह प्रोजेक्ट आपको कॉपिलॉट को एक ओपनएआई संगत एंडपॉइंट में बदलने देता है।" ([Reddit][2])
> "यह आपका ... बनाने के लिए एक अद्भुत प्रोजेक्ट है" ([Reddit][3])

---

### महत्वपूर्ण चेतावनियां

* **अनौपचारिक और अनसपोर्टेड**: यह **कोई** आधिकारिक GitHub उत्पाद नहीं है और कभी भी काम करना बंद कर सकता है ([GitHub][1])।
* **दुरुपयोग पहचान का जोखिम**: भारी या स्वचालित उपयोग GitHub की दुरुपयोग सुरक्षा को ट्रिगर कर सकता है और आपकी Copilot एक्सेस को निलंबित कर सकता है ([GitHub][1])।
* **संभावित दर-सीमा समस्याएं**: कुछ उपयोगकर्ताओं ने `421 Misdirected Request` जैसी त्रुटियों की रिपोर्ट की है, और मेंटेनर ने जांच करते समय विकास रोक दिया है ([GitHub][4])।

---

### सारांश (कोई टेबल की जरूरत नहीं)

* **यह क्या करता है**: GitHub Copilot को एक OpenAI/Anthropic API की तरह एक्सपोज करता है।
* **यह क्यों मायने रखता है**: Copilot को उन टूल्स में उपयोगी बनाता है जो उन APIs की अपेक्षा करते हैं—जैसे Claude Code।
* **इसे कैसे उपयोग करें**: Docker या npx के माध्यम से इंस्टॉल करें; स्टार्ट करने, ऑथेंटिकेट करने, या उपयोग की निगरानी के लिए कमांड्स चलाएं।
* **सावधानी के साथ आगे बढ़ें**: यह उपयोगी है, लेकिन अनौपचारिक है, और GitHub की दर-सीमा या सुरक्षा सुरक्षा उपाय भारी उपयोग में बाधा डाल सकते हैं।

---

मुझे बताएं अगर आप इसे सेटअप करने में मदद चाहते हैं, या किसी विशिष्ट प्रोजेक्ट या टूल में इंटीग्रेट करने के बारे में उत्सुक हैं!

[1]: https://github.com/ericc-ch/copilot-api?utm_source=chatgpt.com "ericc-ch/copilot-api"
[2]: https://www.reddit.com/r/ChatGPTCoding/comments/1m6cqac/how_to_use_your_github_copilot_subscription_with/?utm_source=chatgpt.com "How to use your GitHub Copilot subscription with Claude ..."
[3]: https://www.reddit.com/r/ClaudeAI/comments/1lc21gk/using_github_copilot_as_a_provider_for_claude_code/?utm_source=chatgpt.com "Using GitHub Copilot as a provider for Claude Code"
[4]: https://github.com/ericc-ch/copilot-api/issues/7?utm_source=chatgpt.com "Issue #7 · ericc-ch/copilot-api - 421 Misdirected Request"