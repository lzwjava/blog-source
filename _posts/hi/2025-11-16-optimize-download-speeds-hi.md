---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: हगिंग फेस डाउनलोड गति को अनुकूलित करें
translated: true
type: note
---

आपका वर्तमान डाउनलोड Hugging Face के मुख्य एंडपॉइंट (`huggingface.co`) को हिट कर रहा है, जो मुख्य रूप से यूरोप/यूएस डेटा सेंटर में होस्टेड है। ग्वांगझोउ से आपके ताइवान प्रॉक्सी के माध्यम से रूटिंग करने से पहले जैसी लेटेंसी समस्याएं (~200–300ms राउंड-ट्रिप) आती हैं, साथ ही बड़ी फाइलों पर संभावित थ्रॉटलिंग (यह Parquet शार्ड प्रति ~500MB–1GB है)। आपको जो 302 रीडायरेक्ट दिख रहा है, वह संभवतः एक CloudFront CDN एज की ओर है, लेकिन यह एशिया के लिए इष्टतम नहीं हो सकता है, जिससे स्पीड कम हो जाती है (जैसे, 1–5 MB/s)।

Wikimedia डाउनलोड से 20–60 MB/s की स्पीड मैच करने के लिए, इन ट्वीक्स का उपयोग करें—जो एशिया-फ्रेंडली विकल्पों को प्राथमिकता देते हैं। ये सभी आपके Clash/TW प्रॉक्सी सेटअप को बनाए रखते हैं।

### 1. **HF मिरर पर स्विच करें (चीन/ताइवान के लिए सबसे तेज—अनुशंसित)**
   HF मिरर (`hf-mirror.com`) एक कम्युनिटी-रन CDN है जो पूर्वी एशिया के लिए ऑप्टिमाइज्ड है (जो Tsinghua जैसे डोमेस्टिक CN नेटवर्क के माध्यम से प्रॉक्सी होता है)। यह सभी HF डेटासेट्स, जिनमें FineWeb Parquet फाइलें भी शामिल हैं, को ठीक उसी तरह मिरर करता है। TW प्रॉक्सी से, 30–80 MB/s की उम्मीद करें।

   अपनी स्क्रिप्ट अपडेट करें:
   ```bash
   #!/bin/bash
   # wget_fineweb_1.sh (स्पीड के लिए अपडेटेड)
   mkdir -p fineweb_test_dump
   cd fineweb_test_dump
   echo "HF मिरर के माध्यम से FineWeb शार्ड डाउनलोड हो रहा है (एशिया के लिए तेज)..."

   # huggingface.co को hf-mirror.com से बदलें
   wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00000.parquet?download=true"

   echo "हो गया! शार्ड साइज: ~500MB–1GB"
   echo "अधिक शार्ड्स के लिए, लूप का उपयोग करें, जैसे, 000_00001.parquet, आदि।"
   echo "Python में लोड करने के लिए: from datasets import load_dataset; ds = load_dataset('HuggingFaceFW/fineweb', name='CC-MAIN-2013-20', split='train', streaming=True)"
   ```

   इसे रन करें: `./scripts/train/wget_fineweb_1.sh`
   - यदि मिरर लैग करता है (दुर्लभ), तो ऑफिशियल पर वापस आएं: `https://huggingface.co/datasets/...` (लेकिन #2 में दी गई स्पीड टिप जरूर जोड़ें)।

### 2. **hf_transfer के साथ स्पीड बढ़ाएँ (किसी भी HF डाउनलोड के लिए—रिज्यूमेबल पर 100x तेज)**
   Hugging Face का ऑफिशियल Rust टूल समानांतर/मल्टी-थ्रेडेड डाउनलोड के लिए। यह ऑटो-रीट्राई करता है, अधिक कनेक्शन इस्तेमाल करता है और अच्छे लिंक्स पर >500 MB/s की स्पीड देता है। यह `wget` के साथ अप्रत्यक्ष रूप से या सीधे Python के माध्यम से (यदि आपकी स्क्रिप्ट `huggingface_hub` का उपयोग करती है) काम करता है।

   इंस्टॉल करें (एक बार, pip के माध्यम से—आपके एनवायरनमेंट में यह है):
   ```bash
   pip install hf_transfer
   export HF_HUB_ENABLE_HF_TRANSFER=1
   ```

   फिर अपनी ओरिजिनल स्क्रिप्ट को दोबारा रन करें। यह HF URLs पर की जाने वाली अंतर्निहित `wget` कॉल्स को तेज कर देगा।
   - प्रो टिप: पूर्ण डेटासेट स्ट्रीमिंग (बिना पूरा डाउनलोड) के लिए, अपनी पाइपलाइन में Python का उपयोग करें:
     ```python
     from datasets import load_dataset
     import os
     os.environ['HF_HUB_ENABLE_HF_TRANSFER'] = '1'  # इम्पोर्ट से पहले एनेबल करें
     ds = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2013-20", split="train", streaming=True)
     for example in ds.take(1000):  # ऑन-द-फ्लाई स्ट्रीम/प्रोसेस करें
         print(example)
     ```
     यदि आप `HF_ENDPOINT=https://hf-mirror.com` सेट करते हैं तो यह शार्ड्स को आलसी तरीके (lazily) मिरर के माध्यम से खींचेगा।

### 3. **Clash रूल ट्वीक (यदि अनुमति हो—अल्ट्रा-फास्ट डोमेस्टिक)**
   यदि आपका प्रॉक्सी कॉन्फ़िग HF के लिए बायपास (या HK/SG नोड्स पर रूट) करने देता है, तो `huggingface.co` / `hf-mirror.com` के लिए एक रूल जोड़ें ताकि वह डायरेक्ट/डोमेस्टिक हो जाए। `clash.yaml` में:
   ```
   rules:
     - DOMAIN-SUFFIX,hf-mirror.com,DIRECT  # या आपका CN मिरर नोड
     - DOMAIN-SUFFIX,huggingface.co,DIRECT
   ```
   Clash को रीस्टार्ट करें, फिर डाउनलोड करें। Tsinghua मिरर के माध्यम से 50–100+ MB/s पाने के लिए #1 के साथ जोड़ा जा सकता है।

### यह Wikimedia की स्पीड से क्यों मैच करता है
- Wikimedia: रीडायरेक्टर ने ऑटो-पिक एशिया (जापान/KR/SG) → कम लेटेंसी।
- HF: डिफॉल्ट EU/US → उच्च लेटेंसी; मिरर + ट्रांसफर इसे एशिया-ऑप्टिमाइज्ड में बदल देता है।

पहले एक शार्ड टेस्ट करें—यदि अभी भी स्लो है, तो हेडर (Asia CDN दिखाना चाहिए) के लिए `curl -I https://hf-mirror.com/...` चेक करें। पूरे 15T FineWeb के लिए, 100s GB डाउनलोड से बचने के लिए `datasets` लाइब्रेरी के माध्यम से स्ट्रीम करें। यदि स्पीड नहीं बढ़ती है तो मुझे बताएं!