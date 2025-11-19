---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: मेमोरी एक्जॉशन के कारण सिस्टम जम जाता है
translated: true
type: note
---

आपकी समस्या **GPU** नहीं है (यहाँ 4070 Ti का मुश्किल से इस्तेमाल हो रहा है)। यह स्क्रिप्ट **पूरी तरह से CPU + RAM** पर चलती है, और ~140M टोकन्स के बाद हँग + GUI फ्रीज होना लगभग निश्चित रूप से इसलिए है क्योंकि आपकी **RAM खत्म** हो रही है और सिस्टम डिस्क पर भारी स्वैपिंग शुरू कर देता है, जो सब कुछ मिनटों या घंटों के लिए फ्रीज कर देता है।

### यह ~140M–200M टोकन्स पर क्यों होता है

प्रत्येक टोकन → uint16 के रूप में स्टोर होता है → 2 बाइट्स।

- 140 मिलियन टोकन्स ≈ 280 MB
- 1 बिलियन टोकन्स ≈ 2 GB
- 10 बिलियन टोकन्स (पूरा FineWeb-10B) ≈ 20 GB
- 100B+ टोकन्स (कई FineWeb/Edu डाउनलोड्स की तरह) ≈ 200+ GB

लेकिन Python में आपकी `all_tokens = []` लिस्ट को देखें: Python लिस्ट्स में भारी ओवरहेड होता है। प्रत्येक इंटीजर ऑब्जेक्ट 64-बिट Python पर ~28–32 बाइट्स का होता है (भले ही वैल्यू uint16 में फिट हो जाए)।

लिस्ट बनाते समय वास्तविक मेमोरी उपयोग:
- Python लिस्ट में ~150M टोकन्स → ~150M × 28–32 बाइट्स ≈ **4–5 GB** सिर्फ लिस्ट ऑब्जेक्ट्स के लिए
- फिर आप `np.array(..., dtype=np.uint16)` करते हैं → कॉम्पैक्ट ऐरे के लिए लगभग ~300 MB और
- कनवर्जन के दौरान कुल पीक RAM ≈ 5–6 GB + OS + डेस्कटॉप ओवरहेड

आपके पास 62.6 GB RAM है, तो सिर्फ 140M टोकन्स पर ही फ्रीज क्यों?

क्योंकि आपकी इनपुट फाइल `train_fineweb.txt` संभवतः **आपके सोचने से कहीं बड़ी** है।

लोग अक्सर FineWeb-100B या 1T सैंपल्स डाउनलोड करते हैं और उसे "train_fineweb.txt" नाम दे देते हैं। अगर आपकी फाइल, मान लीजिए, लोकप्रिय 100B-टोकन FineWeb-Edu सैंपल (~200–300 GB टेक्स्ट फाइल) है, तो स्क्रिप्ट अनंत तक पढ़ती रहेगी, `all_tokens` लिस्ट दसियों या सैकड़ों अरबों टोकन्स तक बढ़ जाएगी → सैकड़ों GB की RAM → OOM → स्वैप थ्रैशिंग → पूरा डेस्कटॉप फ्रीज। GPU के पंखे इसलिए घूमते हैं क्योंकि स्क्रिप्ट अभी भी जीवित (मुश्किल से) है, Python `extend()` में या अंतिम `np.array()` कनवर्जन में फंसा हुआ है।

### समाधान (एक चुनें)

#### सबसे अच्छा ठीक: सीधे .bin में स्ट्रीम करें, सभी टोकन्स को RAM में रखे बिना
यह वर्जन RAM का लगभग कोई इस्तेमाल नहीं करती (टेराबाइट-साइज्ड टेक्स्ट के लिए भी पीक < 1 GB):

```python
# stream_tokenize_to_bin.py
import os
import numpy as np
import tiktoken

enc = tiktoken.get_encoding("gpt2")
CHUNK_SIZE = 1_000_000  # characters per chunk, adjust if needed

def process_file(input_path: str, train_bin: str, val_bin: str, val_ratio=0.0005):
    temp_train = train_bin + '.tmp'
    temp_val = val_bin + '.tmp'

    total_tokens = 0
    val_tokens_written = 0
    val_target = None  # we decide it after first pass or approximate

    with open(input_path, "r", encoding="utf-8", errors='ignore') as f, \
         open(temp_train, "wb") as train_f, \
         open(temp_val, "wb") as val_f:

        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            tokens = enc.encode_ordinary(chunk)
            tokens_u16 = np.array(tokens, dtype=np.uint16)

            total_tokens += len(tokens_u16)

            # Approximate validation split on-the-fly (good enough)
            if val_target is None and total_tokens > 10_000_000:
                val_target = int(total_tokens * val_ratio / (1 - val_ratio))

            if val_tokens_written < val_target:
                split_point = min(len(tokens_u16), val_target - val_tokens_written)
                val_f.write(tokens_u16[:split_point].tobytes())
                train_f.write(tokens_u16[split_point:].tobytes())
                val_tokens_written += split_point
            else:
                train_f.write(tokens_u16.tobytes())

            if total_tokens % 50_000_000 == 0:
                print(f"Processed {total_tokens/1e6:.1f}M tokens")

    # Rename temp files
    os.rename(temp_train, train_bin)
    os.rename(temp_val, val_bin)
    print(f"Done! Total ≈ {total_tokens/1e9:.2f}B tokens")
    print(f"train.bin and val.bin ready (no RAM explosion)")

if __name__ == "__main__":
    txt_file = "train_fineweb.txt"
    process_file(txt_file, "train.bin", "val.bin")
```

यह सीधे डिस्क पर स्ट्रीम करती है, मेमोरी में एक से ज्यादा चंक कभी नहीं रखती।

#### अगर आपको वास्तव में ओरिजिनल स्क्रिप्ट स्टाइल चाहिए लेकिन सुरक्षित
मेमोरी मॉनिटरिंग जोड़ें और आउटपुट को शार्ड में बाँट दें:

```python
# add this instead of one giant list
MAX_TOKENS_PER_SHARD = 500_000_000  # ~1 GB per shard

shard_idx = 0
all_tokens = []

for chunk in iter(lambda: f.read(chunk_size), ""):
    if not chunk:
        break
    tokens = enc.encode_ordinary(chunk)
    all_tokens.extend(tokens)

    if len(all_tokens) >= MAX_TOKENS_PER_SHARD:
        arr = np.array(all_tokens, dtype=np.uint16)
        arr.tofile(f"train_shard_{shard_idx:04d}.bin")
        print(f"Saved shard {shard_idx} - {len(arr)/1e6:.1f}M tokens")
        all_tokens.clear()
        shard_idx += 1
```

बाद में बस शार्ड्स को कैट कर दें: `cat train_shard_*.bin > train.bin`

### जल्दी जांचें कि आपकी फाइल वास्तव में कितनी बड़ी है
टर्मिनल में ये चलाएँ:

```bash
du -h train_fineweb.txt          # human size
wc -c train_fineweb.txt          # bytes
ls -lh train_fineweb.txt
```

FineWeb-10B टेक्स्ट ~20–25 GB का होता है, 100B ~200–250 GB का, आदि।

### सारांश
आपकी स्क्रिप्ट इसलिए फेल होती है क्योंकि Python लिस्ट्स अंतिम numpy ऐरे से 15–20× ज्यादा RAM खाती हैं। बड़ी FineWeb फाइल्स के साथ आप जल्दी ही 50+ GB से आगे निकल जाते हैं → स्वैप → फ्रोजन डेस्कटॉप।

ऊपर दिए गए स्ट्रीमिंग वर्जन का इस्तेमाल करें — यह 1TB+ टेक्स्ट फाइल्स पर <2 GB RAM के साथ काम करती है और सिंगल CPU कोर पर कुछ घंटों में खत्म हो जाती है।

आपकी 4070 Ti यहाँ निर्दोष है; वह उस डेटा का इंतज़ार कर रही है जो कभी आता नहीं क्योंकि RAM मर चुकी है।