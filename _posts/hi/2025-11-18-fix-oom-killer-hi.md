---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: फाइनवेब स्क्रिप्ट में ओओएम किलर को ठीक करें
translated: true
type: note
---

बिना किसी Python ट्रेसबैक के "Killed" संदेश का मतलब है कि Linux OOM (आउट-ऑफ-मेमोरी) किलर ने प्रक्रिया को समाप्त कर दिया। यह `data/fineweb/prepare.py` स्क्रिप्ट में होता है क्योंकि यह टोकनाइज़ करने से पहले आपकी पूरी ~15 GB संयुक्त टेक्स्ट फ़ाइल (`train_fineweb.txt`) को एक बार में RAM में लोड करने की कोशिश करती है, जैसे `open(...).read()` के साथ।

भले ही FineWeb-Edu स्ट्रीमिंग के लिए डिज़ाइन किया गया है (आधिकारिक डाउनलोडर Hugging Face `datasets` का उपयोग करता है और शार्ड-बाय-शार्ड ~100M टोकन चंक्स में प्रोसेस करता है बिना कभी सब कुछ मेमोरी में लोड किए), nanoGPT फाइनवेब फोल्डर में एक कस्टम लोकल-फ़ाइल पथ है जो बड़ी फाइलों के लिए मेमोरी-एफिशिएंट नहीं है।

### त्वरित समाधान (एक चुनें)

1.  **सबसे अच्छा और सुझाया गया: अपनी लोकल फाइलों के बजाय आधिकारिक स्ट्रीमिंग FineWeb-Edu डाउनलोडर का उपयोग करें**
    nanoGPT `data/fineweb/prepare.py` का बिल्कुल भी उपयोग न करें।
    Karpathy के नए स्क्रिप्ट का उपयोग करें जो विशेष रूप से FineWeb-Edu 10B टोकन (या बड़े) के लिए बनाया गया है:

    ```bash
    # nanoGPT रूट से (या कहीं से भी)
    wget https://raw.githubusercontent.com/karpathy/build-nanogpt/master/fineweb.py
    python fineweb.py
    ```

    यह `datasets.load_dataset(..., streaming=True)` और मल्टीप्रोसेसिंग का उपयोग करके FineWeb-Edu sample-10BT (10 बिलियन टोकन, ~15-20 GB रॉ) को स्ट्रीमिंग फैशन में डाउनलोड और टोकनाइज़ करता है। यह पूरे डेटासेट को कभी भी RAM में लोड नहीं करता है और nanoGPT द्वारा अपेक्षित ठीक वैसी ही `.bin` शार्ड्स `edu_fineweb10B/` जैसे फोल्डर में तैयार करता है।
    यह 32-64 GB RAM वाली मशीनों पर (या इससे भी कम अगर आप स्क्रिप्ट में `num_proc_load_dataset` और `num_proc` कम करते हैं) ठीक चलता है।

    पूर्ण 100B या 1T वर्जन के लिए, बस `remote_name = "sample-10BT"` को `"100BT"` या जो आपको चाहिए उसमें बदल दें।

2.  **यदि आप वास्तव में अपनी 10 लोकल parquet → txt फाइल रखना चाहते हैं**
    `data/fineweb/prepare.py` को पूरी फाइल को लोड करने के बजाय चंक्स में प्रोसेस करने के लिए संशोधित करें:

    स्क्रिप्ट को खोलें और बड़े `with open(local_file, 'r', encoding='utf-8') as f: data = f.read()` ब्लॉक को कुछ इस तरह बदलें:

    ```python
    from tqdm import tqdm
    import tiktoken
    enc = tiktoken.get_encoding("gpt2")

    chunk_size = 1_000_000  # characters per chunk, adjust if needed
    tokens = []
    with open(local_file, "r", encoding="utf-8") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            tokens.extend(enc.encode_ordinary(chunk))  # or enc.encode(chunk)
            print(f"Tokenized so far: {len(tokens)/1e6:.1f}M tokens")
    tokens = np.array(tokens, dtype=np.uint16)
    ```

    यह आपकी 15 GB फाइल के लिए भी पीक RAM को ~10-15 GB से कम रखता है।

3.  **हार्डवेयर वर्कअराउंड (अस्थायी, आदर्श नहीं)**
    - बहुत सारी स्वैप जोड़ें (जैसे, 64-128 GB स्वैप फाइल)। एक बार स्वैपिंग शुरू होने पर यह बेहद धीमा हो जाएगा, लेकिन यह पूरा हो सकता है।
      ```bash
      sudo fallocate -l 64G /swapfile
      sudo chmod 600 /swapfile
      sudo mkswap /swapfile
      sudo swapon /swapfile
      ```
    - ≥64 GB RAM वाली मशीन/इंस्टेंस पर चलाएं (जैसे, AWS r6i.4xlarge या बड़ा)।

### सारांश
बस build-nanogpt से आधिकारिक `fineweb.py` चलाएं — यह सबसे साफ-सुथरा समाधान है और अब FineWeb के लिए हर कोई इसी का उपयोग करता है। आपकी संयुक्त 15 GB txt फाइल समस्या है, FineWeb स्वयं नहीं।

[आधिकारिक FineWeb-Edu डाउनलोडर स्क्रिप्ट](https://raw.githubusercontent.com/karpathy/build-nanogpt/master/fineweb.py)
[FineWeb-Edu डेटासेट पेज](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)