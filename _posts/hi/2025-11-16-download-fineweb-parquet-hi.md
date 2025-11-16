---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: विशिष्ट फाइनवेब पार्केट फ़ाइलें डाउनलोड करें
translated: true
type: note
---

आप सिर्फ एक Common Crawl डंप (जैसे CC-MAIN-2013-20) से कुछ parquet फाइलें डाउनलोड और उपयोग करना चाहते हैं, पूरे 15T-टोकन वाले FineWeb मॉन्स्टर की नहीं — बिल्कुल समझदारी भरी बात! 2025 में ऐसा करने के सबसे आसान तरीके यहां दिए गए हैं।

### विधि 1: huggingface_hub के साथ सीधा डाउनलोड (सुझाया गया, सबसे तेज़)
यह सिर्फ वही parquet फाइलें डाउनलोड करता है जो आप चाहते हैं, पूरी गति से (~GB/s अगर आप hf-transfer सक्षम करते हैं)।

```bash
# 1. इंस्टॉल/अपग्रेड करें
pip install -U "huggingface_hub[hf_transfer]"

# 2. तेज़ डाउनलोड सक्षम करें (बहुत ज़रूरी!)
export HF_HUB_ENABLE_HF_TRANSFER=1   # Linux/macOS
# या Windows PowerShell पर:
# $env:HF_HUB_ENABLE_HF_TRANSFER = "1"

# 3. सिर्फ वे कुछ parquet फाइलें डाउनलोड करें जो आप चाहते हैं
huggingface-cli download HuggingFaceFW/fineweb \
    data/CC-MAIN-2013-20/000_00000.parquet \
    data/CC-MAIN-2013-20/000_00001.parquet \
    data/CC-MAIN-2013-20/000_00002.parquet \
    --repo-type dataset --local-dir fineweb-2013-20
```

बस हो गया — अब आपके पास `fineweb-2013-20/` फोल्डर में तीन ~2.15 GB की parquet फाइलें हैं।

### विधि 2: विशिष्ट फाइलें डाउनलोड करने के लिए वन-लाइनर Python स्क्रिप्ट
```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="HuggingFaceFW/fineweb",
    repo_type="dataset",
    allow_patterns=[
        "data/CC-MAIN-2013-20/000_00000.parquet",
        "data/CC-MAIN-2013-20/000_00001.parquet",
        # और चाहें तो जोड़ें
    ],
    local_dir="fineweb-2013-20"
)
```

### Parquet फाइलों को लोकल रीड करने का तरीका
```python
import pandas as pd
# या स्पीड + कम मेमोरी के लिए pyarrow का उपयोग करें
import pyarrow.parquet as pq
import pyarrow.dataset as ds

# सबसे तेज़ तरीका (बिना सब कुछ RAM में लोड किए स्ट्रीम करता है)
dataset = ds.dataset("fineweb-2013-20/data/CC-MAIN-2013-20/", format="parquet")

for batch in dataset.to_batches(batch_size=1024):
    df = batch.to_pandas()
    for text in df["text"]:
        # जो चाहें करें: tokenize, filter, jsonl में लिखें, आदि।
        print(text[:200])  # उदाहरण
```

या बस pandas के साथ (कुछ फाइलों के लिए ठीक है):
```python
df = pd.read_parquet("fineweb-2013-20/data/CC-MAIN-2013-20/000_00000.parquet")
print(df.columns)  # ['text', 'id', 'dump', 'url', 'date', 'file_path', 'language', 'language_score', 'token_count']
print(df.iloc[0]["text"])
```

### CC-MAIN-2013-20 के लिए त्वरित आँकड़े
- ~207 parquet फाइलें × ~2.15 GB ≈ 422 GB कुल
- ~44 बिलियन टोकन (छोटे-से-मध्यम प्रयोगों के लिए अच्छा आकार)
- पहले से ही Hugging Face द्वारा साफ़ की गई, डीडुप्लिकेट की गई और फ़िल्टर की गई

बस आपको यही चाहिए। बस जितनी चाहें `_0000XX.parquet` फाइलें चुनें (वे फेंटी हुई/shuffled हैं), सिर्फ उन्हें डाउनलोड करें, और तुरंत ट्रेनिंग या फ़िल्टरिंग शुरू कर दें।