---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: फाइनवेब डेटा डाउनलोड और तैयारी
translated: true
type: note
---

### Parquet फ़ाइल डाउनलोड करना

आपके द्वारा प्रदान किया गया URL FineWeb डेटासेट (CommonCrawl डेटा का एक साफ़ किया गया सबसेट) की एक विशिष्ट Parquet फ़ाइल की ओर इशारा करता है। यह फ़ाइल (`CC-MAIN-2013-20` डंप से `000_00000.parquet`) अंग्रेजी वेब टेक्स्ट की ~1 मिलियन पंक्तियाँ शामिल करती है, जहाँ प्रत्येक पंक्ति में एक `text` कॉलम होता है जो पहले से ही भाषा मॉडल प्रशिक्षण के लिए प्रीप्रोसेस्ड है (HTML हटाया गया, डीडुप्लिकेट किया गया, Trafilatura जैसे टूल्स के माध्यम से क्वालिटी-फ़िल्टर किया गया)।

इसे डाउनलोड करने के लिए:
- Hugging Face CLI का उपयोग करें: `huggingface-cli download HuggingFaceFW/fineweb data/CC-MAIN-2013-20/000_00000.parquet --local-dir ./fineweb_data`
- या Python के साथ `huggingface_hub` के माध्यम से:
  ```python
  from huggingface_hub import hf_hub_download

  file_path = hf_hub_download(
      repo_id="HuggingFaceFW/fineweb",
      filename="data/CC-MAIN-2013-20/000_00000.parquet",
      local_dir="./fineweb_data"
  )
  print(f"Downloaded to: {file_path}")
  ```
यह ~500MB की फ़ाइल को स्थानीय रूप से सेव कर देता है (उदाहरण: `./fineweb_data/data/CC-MAIN-2013-20/000_00000.parquet`)।

पूरे डंप (सैकड़ों फ़ाइलें) के लिए, डेटासेट डॉक्स में दिखाए अनुसार `snapshot_download` का उपयोग करें, लेकिन टेस्टिंग के लिए इस सिंगल फ़ाइल से शुरुआत करें।

### टेक्स्ट निकालना

FineWeb का `text` कॉलम प्लेन टेक्स्ट है जो प्रशिक्षण के लिए तैयार है—HTML या raw HTML को पार्स करने की कोई आवश्यकता नहीं है। इसे कुशलतापूर्वक लोड करने के लिए `pandas` या `pyarrow` का उपयोग करें। यहाँ बताया गया है कैसे:

1.  **डिपेंडेंसी इंस्टॉल करें** (यदि आवश्यक हो): `pip install pandas pyarrow datasets` (यह मानते हुए कि आपके पास NanoGPT सेटअप के लिए ये पहले से हैं)।

2.  **Parquet फ़ाइल लोड करें और टेक्स्ट निकालें**:
    ```python
    import pandas as pd
    import os

    # आपकी डाउनलोड की गई फ़ाइल का पथ
    parquet_path = "./fineweb_data/data/CC-MAIN-2013-20/000_00000.parquet"

    # Parquet फ़ाइल लोड करें (बड़ी फ़ाइलों के लिए कुशल)
    df = pd.read_parquet(parquet_path, columns=['text'])  # मेमोरी बचाने के लिए केवल text कॉलम लोड करें

    # सभी टेक्स्ट को एक लिस्ट में निकालें (या मेमोरी कंस्ट्रेंड होने पर इटरेट करें)
    texts = df['text'].tolist()  # ~1M स्ट्रिंग्स की लिस्ट

    # ऑप्शनल: बेसिक क्लीनिंग (FineWeb पहले से ही साफ है, लेकिन व्हाइटस्पेस नॉर्मलाइज़ करें)
    import re
    def clean_text(text):
        if pd.isna(text):  # null को स्किप करें (FineWeb में दुर्लभ)
            return ''
        text = re.sub(r'\s+', ' ', text.strip())  # व्हाइटस्पेस को कॉलैप्स करें
        return text if len(text) > 10 else ''  # बहुत छोटे टेक्स्ट को फ़िल्टर करें

    cleaned_texts = [clean_text(t) for t in texts if t]  # फ़िल्टर लागू करें

    print(f"Extracted {len(cleaned_texts)} text samples")
    print("Sample:", cleaned_texts[0][:200] + "...")  # पहले टेक्स्ट का प्रिव्यू
    ```

    - **मेमोरी टिप**: इस फ़ाइल में ~1M पंक्तियाँ हैं, प्रत्येक टेक्स्ट ~1-5k करैक्टर का है। 16GB RAM वाले मशीन पर, यह ठीक से लोड हो जाती है। बड़े डंप के लिए, चंक्ड रीडिंग के लिए `pyarrow` का उपयोग करें:
      ```python
      import pyarrow.parquet as pq

      table = pq.read_table(parquet_path, columns=['text'])
      texts = table['text'].to_pylist()
      ```

    - **स्ट्रीमिंग विकल्प** (पूरी डाउनलोड की आवश्यकता नहीं): सब कुछ लोड किए बिना इटरेट करने के लिए `datasets` लाइब्रेरी का उपयोग करें:
      ```python
      from datasets import load_dataset

      # स्ट्रीमिंग मोड में विशिष्ट डंप लोड करें
      dataset = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2013-20", split="train", streaming=True)

      texts = []
      for i, sample in enumerate(dataset):
          if i >= 100000:  # टेस्टिंग के लिए लिमिट
              break
          texts.append(sample['text'])

      # ऊपर बताए अनुसार साफ करें
      ```

### NanoGPT प्रशिक्षण के लिए तैयार करना

NanoGPT एक सिंगल टेक्स्ट फ़ाइल (उदाहरण: `input.txt`) की अपेक्षा करता है जिसमें एक विशेष टोकन (जैसे `"<|endoftext|>"`) द्वारा अलग किए गए कॉन्कैटनेटेड डॉक्युमेंट्स होते हैं। निकाले गए टेक्स्ट को फॉर्मेट करने का तरीका यहाँ बताया गया है:

```python
# ऊपर से cleaned_texts निकालने के बाद
with open('input.txt', 'w', encoding='utf-8') as f:
    for text in cleaned_texts:
        f.write(text + "\n<|endoftext|>\n")  # NanoGPT का डिफ़ॉल्ट सेपरेटर

print("Saved to input.txt – ready for NanoGPT!")
```

- **यह फॉर्मेट क्यों?** NanoGPT का `data.py` स्क्रिप्ट `input.txt` को पढ़ेगा, इसे आपके टोकनाइज़र (उदाहरण: GPT-2) के साथ एनकोड करेगा, और train/val स्प्लिट्स बनाएगा। क्रॉस-डॉक्युमेंट कॉन्टेक्स्ट ब्लीड से बचने के लिए प्रत्येक डॉक्युमेंट `"<|endoftext|>"` के साथ समाप्त होता है।
- **कस्टमाइज़ेशन**:
  - लंबाई के आधार पर फ़िल्टर करें: मिड-साइज़्ड डॉक्स को रखने के लिए लिखने से पहले `if 100 < len(text.split()) < 10000:` जोड़ें।
  - टेस्टिंग के लिए सबसेट: क्विक 10k-सैंपल रन के लिए `cleaned_texts[:10000]` का उपयोग करें।
  - ट्रेन कमांड: एक बार `input.txt` तैयार हो जाने पर, NanoGPT में `python train.py` चलाएँ (यदि आवश्यक हो तो `--dataset=input.txt` एडजस्ट करें)।

यह सिंगल फ़ाइल ~5-10B टोकन देती है—फाइन-ट्यूनिंग के लिए बढ़िया। अधिक के लिए, अतिरिक्त Parquet फ़ाइलें डाउनलोड करें और कॉन्कैटनेट करें। यदि आपको मेमोरी संबंधी समस्याएँ आती हैं या NanoGPT कॉन्फ़िग में सहायता की आवश्यकता है, तो विवरण साझा करें!

**संदर्भ**: [FineWeb Dataset Card](https://huggingface.co/datasets/HuggingFaceFW/fineweb)