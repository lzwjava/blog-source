---
audio: false
generated: true
image: false
lang: hi
layout: post
title: ग्लोव वेक्टर्स लोड करने के दो तरीके
translated: true
type: note
---

आपके पास `the`, `to`, `U.S.` जैसे शब्दों और आपके अपने टेक्स्ट के लिए GloVe वैक्टर प्राप्त करने के दो आसान तरीके हैं:

---

## विकल्प A — Stanford GloVe डाउनलोड करें और `gensim` के साथ लुकअप करें

यह सबसे आम तरीका है और एक बार डाउनलोड होने के बाद पूरी तरह से ऑफलाइन काम करता है।

```python
# 1) डाउनलोड करें और अनज़िप करें (पहली बार रन करने पर)
import os, zipfile, urllib.request
url = "https://nlp.stanford.edu/data/glove.6B.zip"
zip_path = "glove.6B.zip"
if not os.path.exists(zip_path):
    urllib.request.urlretrieve(url, zip_path)
with zipfile.ZipFile(zip_path) as zf:
    zf.extract("glove.6B.300d.txt")  # 300-dim सेट

# 2) GloVe फॉर्मेट -> word2vec टेक्स्ट फॉर्मेट में बदलें और लोड करें
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors

glove_path = "glove.6B.300d.txt"
w2v_path   = "glove.6B.300d.w2v.txt"
if not os.path.exists(w2v_path):
    glove2word2vec(glove_path, w2v_path)

vectors = KeyedVectors.load_word2vec_format(w2v_path, binary=False)
print(vectors.vector_size)  # 300

# 3) सिंगल-वर्ड लुकअप
print(vectors['the'][:5])   # पहले 5 डायमेंशन
print(vectors['to'][:5])

# नोट: glove.6B वोकैबुलरी लोअरकेस है।
# 'U.S.' -> 'u.s.' इस वोकैबुलरी में (अगर मौजूद हो)। सुरक्षित तरीका: अपने टोकन्स को लोअरकेस करें।
print(vectors['u.s.'][:5])
```

अब अपना खुद का टेक्स्ट एम्बेड करें:

```python
import re, numpy as np

# सरल टोकनाइज़र जो u.s. जैसे टोकन में डॉट्स रखता है
TOKEN_RE = re.compile(r"[A-Za-z0-9\.\-']+")

def tokenize(text: str):
    return TOKEN_RE.findall(text.lower())

def embed_tokens(tokens, kv: KeyedVectors):
    vecs = [kv[w] for w in tokens if w in kv.key_to_index]
    return np.stack(vecs) if vecs else np.zeros((0, kv.vector_size))

def embed_sentence_avg(text: str, kv: KeyedVectors):
    V = embed_tokens(tokenize(text), kv)
    return V.mean(axis=0) if V.size else np.zeros(kv.vector_size)

# उदाहरण
print(embed_sentence_avg("The quick brown fox jumps over the lazy dog.", vectors)[:10])
print(embed_tokens(tokenize("U.S. interest rates rose today."), vectors).shape)  # (n_tokens, 300)
```

**सुझाव**

* `glove.6B.300d.txt` मेमोरी में ≈ 1.1 GB लेता है। अगर यह भारी है, तो `100d` इस्तेमाल करने का प्रयास करें।
* 6B सेट **लोअरकेस** है; हमेशा अपने टेक्स्ट को लोअरकेस करें, या अगर आपको अधिक कवरेज चाहिए तो बड़े **840B** सेट का उपयोग करें (व्यवहार में अभी भी बड़े पैमाने पर अनकेस्ड है)।
* OOV (आउट-ऑफ-वोकैबुलरी) शब्द कुछ नहीं लौटाते; आप उन्हें छोड़ सकते हैं या सबवर्ड ह्युरिस्टिक्स का सहारा ले सकते हैं।

---

## विकल्प B — `torchtext` को GloVe डाउनलोड और सर्व करने दें

यह मैन्युअल डाउनलोडिंग/कन्वर्जन से बचाता है।

```python
import torch
from torchtext.vocab import GloVe
import re

glove = GloVe(name="6B", dim=300)  # ~/.vector_cache में ऑटो-डाउनलोड होता है
stoi = glove.stoi    # word -> index
vecs = glove.vectors # tensor [vocab, 300]

def get_word_vec(word: str):
    idx = stoi.get(word.lower())
    return vecs[idx] if idx is not None else None

print(get_word_vec("the")[:5])
print(get_word_vec("to")[:5])
print(get_word_vec("U.S.")[:5])     # कई बिल्ड में None बन जाता है; "u.s." आज़माएं:
print(get_word_vec("u.s.")[:5])

# वाक्य एम्बेडिंग (औसत)
TOKEN_RE = re.compile(r"[A-Za-z0-9\.\-']+")
def embed_sentence_avg(text: str):
    toks = TOKEN_RE.findall(text.lower())
    xs = [get_word_vec(t) for t in toks]
    xs = [x for x in xs if x is not None]
    return torch.stack(xs, dim=0).mean(0) if xs else torch.zeros(glove.dim)

print(embed_sentence_avg("The quick brown fox...")[:10])
```

---

## आपने विशिष्ट पंक्तियों के बारे में क्या पूछा था

वे पंक्तियाँ जैसे:

```
the  0.418 0.24968 -0.41242 0.1217 ... 0.34527  # कुल 300 फ्लोट
to   0.68047 -0.039263 -0.67412 0.056051 ... -0.067549
U.S. 0.3459  0.21513  -0.09982 0.25344 ... 0.024118
```

यह वही है जो आप प्लेन-टेक्स्ट `.txt` फाइलों में देखेंगे: प्रत्येक लाइन `token` के बाद `300` फ्लोट्स होती है। `gensim` या `torchtext` के साथ, आपको लाइनों को खुद पार्स करने की ज़रूरत नहीं है—वे इसे हैंडल करते हैं और आपको सीधे वेक्टर लुकअप देते हैं।

---

## सामान्य गलतियाँ (और उनके समाधान)

* **“KeyError: ‘U.S.’”** → 6B सेट के साथ `u.s.` का उपयोग करें, या बेहतर कवरेज वाला बड़ा सेट चुनें, और लुकअप से पहले हमेशा लोअरकेस करें।
* **भारी मेमोरी/समय** → `300d` के बजाय `100d` या `200d` का उपयोग करें, या केवल आवश्यक शब्दों को फाइल स्कैन करके और एक छोटी वोकैबुलरी बनाकर लोड करें।
* **वाक्य/डॉक वैक्टर** → वर्ड वैक्टर का औसत या योग निकालें; वेटेड एवरेजिंग के लिए, TF-IDF वेट्स आज़माएं।

अगर आप चाहें, तो मुझे अपना सटीक टेक्स्ट प्रोसेसिंग लक्ष्य बताएं (वर्गीकरण, समानता, क्लस्टरिंग, आदि) और मैं GloVe का उपयोग करके एंड-टू-एंड एक मिनिमल पाइपलाइन का स्केच तैयार करूंगा।