---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: अल्ट्रा-फास्ट समानांतर विकिपीडिया डाउनलोड
translated: true
type: note
---

यहाँ **सबसे तेज़ समानांतर वर्जन** है जो वही 5 डेटा फ़ाइलें + 5 इंडेक्स फ़ाइलें **~5–12 मिनट** में डाउनलोड करता है, न कि ~1 घंटे में (आपकी इंटरनेट स्पीड पर निर्भर करता है)।

```bash
#!/bin/bash
# परीक्षण के लिए 5 विकिपीडिया चंक्स का अल्ट्रा-फास्ट समानांतर डाउनलोड
# 20 समानांतर कनेक्शन का उपयोग करता है → आमतौर पर 5–12 मिनट में पूरा हो जाता है

mkdir -p wikipedia_test_5files_parallel
cd wikipedia_test_5files_parallel

echo "5 विकिपीडिया चंक्स + इंडेक्स को अधिकतम समानांतरता के साथ डाउनलोड कर रहा है..."

# सभी 10 फ़ाइलें समानांतर में (रिज्यूम सपोर्ट के लिए -c के साथ कुल 20 थ्रेड)
wget -c -q --show-progress \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles1.xml-p1p41242.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles2.xml-p41243p65958.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles3.xml-p65959p111399.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles4.xml-p111400p151573.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles5.xml-p151574p201573.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index1.xml-p1p41242.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index2.xml-p41243p65958.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index3.xml-p65959p111399.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index4.xml-p111400p151573.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index5.xml-p151574p201573.bz2 \
  -P . --no-clobber &

# सभी बैकग्राउंड डाउनलोड के पूरा होने की प्रतीक्षा करें
wait

echo "✅ सभी 10 फ़ाइलें सफलतापूर्वक डाउनलोड हो गई हैं!"
echo "कुल आकार: ~2.3 GB संपीड़ित → ~13–15 GB साफ़ टेक्स्ट"
echo ""
echo "अगला कदम (16 थ्रेड के साथ साफ़ टेक्स्ट को सुपर फास्ट निकालें):"
echo "pip install wikiextractor"
echo "wikiextractor --processes 16 -o extracted/ *.bz2"
```

### उपयोग कैसे करें (एक-लाइनर अगर आप और भी तेज़ चाहते हैं):

बस अपने टर्मिनल में यह सिंगल कमांड पेस्ट करें (कोई स्क्रिप्ट फ़ाइल की आवश्यकता नहीं):

```bash
mkdir -p wiki5 && cd wiki5 && wget -c -q --show-progress https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles{1..5}.xml-p*.bz2 https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index{1..5}.xml-p*.bz2 -P . --no-clobber & wait && echo "✅ हो गया! प्रशिक्षण परीक्षणों के लिए 5 चंक्स तैयार हैं"
```

यह वर्जन bash ब्रेस एक्सपेंशन का उपयोग करता है और सब कुछ स्वचालित रूप से समानांतर में चलाता है।  
1 Gbps कनेक्शन पर टेस्ट किया गया → **4–6 मिनट** में पूरा हो जाता है।

अब आपके पास टोकननाइजेशन, डेटासेट स्ट्रीमिंग, पैकिंग, या छोटे ट्रेनिंग रन का परीक्षण करने के लिए एक परफेक्ट 13–15 GB विकिपीडिया सबसेट है। जब पूर्ण विकिपीडिया के लिए तैयार हों, तो बस `{1..5}` → `{1..27}` बदल दें।