---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: नैनोजीपीटी के साथ कस्टम डेटासेट का प्रशिक्षण
translated: true
type: note
---

### nanoGPT के साथ कस्टम टेक्स्ट डेटासेट तैयार करना और ट्रेनिंग देना

nanoGPT को टेक्स्ट डेटा, जिसमें कस्टम डेटासेट भी शामिल हैं, पर आसानी से ट्रेनिंग देने के लिए डिज़ाइन किया गया है। इस प्रक्रिया में आपके टेक्स्ट को बाइनरी टोकन फाइलों में तैयार करना, ट्रेनिंग पैरामीटर कॉन्फ़िगर करना और ट्रेनिंग स्क्रिप्ट चलाना शामिल है। नीचे, मैं रिपॉजिटरी के उदाहरणों (जैसे Shakespeare या OpenWebText) के आधार पर चरणों की रूपरेखा दूंगा। आपको कुशल ट्रेनिंग (CPU भी काम करता है लेकिन धीमा है) के लिए Python 3.8+ और एक GPU की आवश्यकता होगी।

#### 1. निर्भरताएँ इंस्टॉल करें
सबसे पहले, वातावरण सेट अप करें:
```
pip install torch numpy transformers datasets tiktoken wandb tqdm
```
- `torch`: PyTorch के लिए (GPU का उपयोग कर रहे हैं तो CUDA के साथ इंस्टॉल करें: उदा. `pip install torch --index-url https://download.pytorch.org/whl/cu118`)।
- अन्य टोकननाइजेशन, डेटा लोडिंग और लॉगिंग संभालते हैं।

#### 2. अपना कस्टम डेटासेट तैयार करें
nanoGPT आपके डेटा को बाइनरी फाइलों (`train.bin` और `val.bin`) के रूप में अपेक्षित करता है जिनमें टोकनयुक्त पूर्णांक होते हैं। आपको अपने रॉ टेक्स्ट को प्रोसेस करने के लिए एक सरल तैयारी स्क्रिप्ट लिखनी होगी।

- **अपनी टेक्स्ट फाइल रखें**: अपना रॉ टेक्स्ट (जैसे `input.txt`) `data/` के अंतर्गत एक नए फोल्डर में रखें, जैसे `data/my_dataset/`।

- **एक तैयारी स्क्रिप्ट बनाएँ**: रिपो से एक उदाहरण कॉपी करें और उसे एडाप्ट करें (जैसे कैरेक्टर-लेवल के लिए `data/shakespeare_char/prepare.py` या GPT-2 BPE टोकन-लेवल के लिए `data/openwebtext/prepare.py`)।

  **कैरेक्टर-लेवल टोकननाइजेशन के लिए उदाहरण** (छोटे डेटासेट के लिए सरल; प्रत्येक कैरेक्टर को एक टोकन मानता है):
  ```python
  # इसे data/my_dataset/prepare.py के रूप में सेव करें
  import os
  import requests
  import numpy as np
  from torch.utils.data import Dataset, random_split

  # अपना टेक्स्ट लोड करें (अपनी फाइल पथ से बदलें)
  with open('data/my_dataset/input.txt', 'r', encoding='utf-8') as f:
      text = f.read()

  # कैरेक्टर्स के रूप में एनकोड करें
  chars = sorted(list(set(text)))
  vocab_size = len(chars)
  stoi = {ch: i for i, ch in enumerate(chars)}
  itos = {i: ch for i, ch in enumerate(chars)}
  def encode(s): return [stoi[c] for c in s]
  def decode(l): return ''.join([itos[i] for i in l])

  # पूरे टेक्स्ट को टोकनाइज़ करें
  data = torch.tensor(encode(text), dtype=torch.long)

  # ट्रेन/वैल में विभाजित करें (90/10)
  n = int(0.9 * len(data))
  train_data = data[:n]
  val_data = data[n:]

  # .bin फाइलों के रूप में सेव करें
  train_data = train_data.numpy()
  val_data = val_data.numpy()
  train_data.tofile('data/my_dataset/train.bin')
  val_data.tofile('data/my_dataset/val.bin')

  # स्टैट्स प्रिंट करें
  print(f"डेटासेट की लंबाई कैरेक्टर्स में: {len(data)}")
  print(f"शब्दावली आकार: {vocab_size}")
  ```
  इसे रन करें:
  ```
  python data/my_dataset/prepare.py
  ```
  यह `train.bin` और `val.bin` बनाता है।

- **GPT-2 BPE टोकननाइजेशन के लिए** (बड़े डेटासेट के लिए बेहतर; सबवर्ड्स का उपयोग करता है):
  `data/openwebtext/prepare.py` को एडाप्ट करें। आपको `tiktoken` इंस्टॉल करने की आवश्यकता होगी (पहले से ही निर्भरताओं में है) और अपने टेक्स्ट को इसी तरह हैंडल करना होगा, लेकिन कैरेक्टर एनकोडिंग के बजाय `tiktoken.get_encoding("gpt2").encode()` का उपयोग करें। अपने टेक्स्ट को ट्रेन/वैल चंक्स में विभाजित करें (जैसे 90/10), फिर NumPy ऐरे के रूप में `.bin` में सेव करें।

- **सुझाव**:
  - अपना डेटासेट साफ रखें (जैसे, यदि आवश्यक हो तो विशेष वर्ण हटा दें)।
  - बहुत बड़ी फाइलों के लिए, मेमोरी समस्याओं से बचने के लिए चंक्स में प्रोसेस करें।
  - शब्दावली आकार: कैरेक्टर्स के लिए ~65 (Shakespeare); BPE के लिए ~50k।

#### 3. ट्रेनिंग कॉन्फ़िगर करें
एक उदाहरण को कॉपी करके (जैसे `config/train_shakespeare_char.py`) एक कॉन्फ़िग फाइल बनाएं और उसे `config/train_my_dataset.py` के रूप में सेव करें और उसे एडिट करें।

ट्वीक करने के लिए मुख्य पैरामीटर:
```python
# उदाहरण कॉन्फ़िग स्निपेट
out_dir = 'out-my_dataset'  # चेकपॉइंट के लिए आउटपुट फोल्डर
dataset = 'my_dataset'      # आपके डेटा फोल्डर नाम से मेल खाता है
batch_size = 64             # GPU मेमोरी के आधार पर एडजस्ट करें (जैसे, छोटे GPU के लिए 12)
block_size = 256            # संदर्भ लंबाई (उदाहरण प्रति टोकन)
n_layer = 6                 # ट्रांसफॉर्मर लेयर्स
n_head = 6                  # अटेंशन हेड्स
n_embd = 384                # एम्बेडिंग डायमेंशन
max_iters = 5000            # ट्रेनिंग स्टेप्स
lr = 6e-4                   # लर्निंग रेट
dropout = 0.2               # ड्रॉपआउट रेट
init_from = 'scratch'       # नए मॉडल के लिए 'scratch'; प्रीट्रेंड लोड करने के लिए 'gpt2'
```
- फाइन-ट्यूनिंग के लिए (प्रीट्रेंड GPT-2 से शुरू करें): `init_from = 'gpt2'` (या 'gpt2-medium') सेट करें।
- Apple Silicon के लिए: `device = 'mps'` जोड़ें।
- डिफ़ॉल्ट रूप से प्रत्येक 500 इटरेशन पर चेकपॉइंट सेव करें।

#### 4. ट्रेनिंग रन करें
स्क्रैच से या फाइन-ट्यून करें:
```
python train.py config/train_my_dataset.py
```
- मल्टी-GPU के लिए (जैसे, 8 GPU): `torchrun --standalone --nproc_per_node=8 train.py config/train_my_dataset.py`।
- WandB के साथ मॉनिटर करें (लॉस, सैंपल लॉग करता है; कॉन्फ़िग में `wandb_log = True` से इनेबल करें)।
- ट्रेनिंग समय: GPU पर छोटे मॉडल के लिए मिनटों में; बड़े मॉडल के लिए घंटों/दिनों में।

#### 5. सैंपल जनरेट करें (मॉडल टेस्ट करें)
ट्रेनिंग के बाद, टेक्स्ट सैंपल करें:
```
python sample.py --out_dir=out-my_dataset --start="आपका प्रॉम्प्ट यहाँ"
```
यह लेटेस्ट चेकपॉइंट लोड करता है और टेक्स्ट जनरेट करता है।

#### सामान्य समस्याएँ
- **मेमोरी एरर्स**: `batch_size` या `block_size` कम करें।
- **GPU नहीं है**: कमांड्स में `--device=cpu --compile=False` जोड़ें।
- **बड़े डेटासेट**: स्केलिंग के लिए डिस्ट्रिब्यूटेड ट्रेनिंग का उपयोग करें।

अधिक विवरण के लिए, रिपो का README और डेटा/कॉन्फ़िग उदाहरण देखें।

[nanoGitHub GitHub](https://github.com/karpathy/nanoGPT)