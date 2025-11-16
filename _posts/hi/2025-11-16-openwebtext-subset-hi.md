---
audio: false
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: ओपनवेबटेक्स्ट का एक हिस्सा डाउनलोड करना
translated: true
type: note
---

आह, समझ गया — आप **Hugging Face CLI** के साथ ही रहना चाहते हैं लेकिन फिर भी केवल एक छोटा हिस्सा प्राप्त करना चाहते हैं। समस्या यह है: CLI को **पूरी फाइलें** डाउनलोड करने के लिए डिज़ाइन किया गया है, टुकड़े नहीं। OpenWebText 21 `.tar` सबसेट फाइलों में विभाजित है; यदि आप CLI का उपयोग करते हैं, तो यह पूरी टारबॉल डाउनलोड करेगा, इसलिए आप बड़े हिस्से डाउनलोड किए बिना ठीक "1%" प्राप्त नहीं कर सकते।

यहाँ एक व्यावहारिक तरीका है:

---

### 1. केवल फाइलों का एक सबसेट डाउनलोड करें

सभी 21 फाइलों के बजाय, केवल कुछ टारबॉल चुनें:

```bash
huggingface-cli download \
  --repo-type dataset openwebtext/subsets/urlsf_subset00.tar \
  --local-dir ./openwebtext
huggingface-cli download \
  --repo-type dataset openwebtext/subsets/urlsf_subset01.tar \
  --local-dir ./openwebtext
```

* प्रत्येक टारबॉल ~625MB है, इसलिए यदि आप इनमें से 1–2 डाउनलोड करते हैं, तो यह डेटासेट का लगभग 1–2% है।
* आप जो सबसेट चुनते हैं उसे समायोजित कर सकते हैं; HF क्रमिक क्रम लागू नहीं करता है।

---

### 2. केवल वही निकालें जिसकी आपको आवश्यकता है

डाउनलोड के बाद:

```bash
cd ./openwebtext
tar -xvf urlsf_subset00.tar
tar -xvf urlsf_subset01.tar
```

फिर आप इन सबसेट से केवल कुछ दस्तावेज़ों को प्रोसेस कर सकते हैं।

---

### 3. वैकल्पिक: HF Transfer के साथ संयोजित करें

CLI डाउनलोड की गति बढ़ाने के लिए:

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

फिर CLI कमांड्स को दोबारा आज़माएं — डाउनलोड बहुत तेज़ हो जाएगा।

---

यदि आप चाहें, तो मैं एक **छोटा कमांड स्निपेट बना सकता हूं जो केवल CLI का उपयोग करके OpenWebText का ~1% स्वचालित रूप से चुनता है**, ताकि आपको मैन्युअल रूप से टारबॉल चुनने की आवश्यकता न पड़े। क्या आप चाहते हैं कि मैं ऐसा करूं?