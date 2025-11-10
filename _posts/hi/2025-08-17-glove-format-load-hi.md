---
audio: false
generated: true
image: false
lang: hi
layout: post
title: ग्लोव प्रारूप और लोडिंग गाइड
translated: true
type: note
---

GloVe वैक्टर सादे-पाठ फ़ाइलें होती हैं। प्रत्येक पंक्ति एक टोकन और उसके एम्बेडिंग मान होते हैं, सभी स्पेस से अलग किए गए। इसमें **कोई हेडर नहीं** होता (कई word2vec टेक्स्ट फ़ाइलों के विपरीत)।

उदाहरण (300-d GloVe):

```
the 0.418 0.24968 -0.41242 0.1217 ... 0.34527   # कुल 300 फ्लोट
to   0.68047 -0.039263 -0.67412 0.056051 ... -0.067549
U.S. 0.3459  0.21513  -0.09982  0.25344 ... 0.024118
```

कुछ व्यावहारिक नोट्स:

* सामान्य रिलीज़:

  * `glove.6B.{50,100,200,300}d.txt` (विकिपीडिया + Gigaword; \~400k शब्दावली, लोअरकेस)।
  * `glove.840B.300d.txt` (Common Crawl; \~2.2M शब्दावली)।
  * `glove.twitter.27B.{25,50,100,200}d.txt` (ट्विटर; बहुत सारे हैशटैग/इमोटिकॉन)।
* टोकन में कभी भी स्पेस नहीं होते (वाक्यांश अंडरस्कोर का उपयोग करते हैं), इसलिए एक साधारण `line.split()` ठीक काम करता है।
* फ्लोट ASCII में होते हैं; आपको नियमित दशमलव और कभी-कभी वैज्ञानिक संकेतन दिखाई देगी।
* कोई विशेष `<unk>` पंक्ति नहीं होती; OOV हैंडलिंग आप पर निर्भर करती है।

आपका लोडर

```python
def read_glove_vecs(glove_file):
    with open(glove_file, 'r', encoding='utf-8') as f:
        words = set()
        word_to_vec_map = {}
        for line in f:
            line = line.strip().split()
            curr_word = line[0]
            words.add(curr_word)
            word_to_vec_map[curr_word] = np.array(line[1:], dtype=np.float64)
    return words, word_to_vec_map
```

इस फॉर्मेट से मेल खाता है। दो छोटे अपग्रेड जो आप चाह सकते हैं:

1. मेमोरी आधी करने के लिए float32 का उपयोग करें:

```python
vec = np.asarray(line[1:], dtype=np.float32)
```

2. आकस्मिक "हेडर" या खराब पंक्तियों को छोड़ दें (कुछ रीपैकेज्ड फ़ाइलें एक जोड़ देती हैं):

```python
parts = line.rstrip().split(' ')
if len(parts) < 2: 
    continue
if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
    # word2vec-स्टाइल हेडर जैसा दिखता है: "<vocab> <dim>"
    continue
word, *vals = parts
```

### अपनी शब्दावली के लिए एक एम्बेडिंग मैट्रिक्स बनाना

जब आप `dictionary: word -> id` बना लेते हैं, तो GloVe पंक्तियों को अपने `nn.Embedding` के लिए वेट मैट्रिक्स में मैप करें:

```python
def build_embedding_matrix(dictionary, glove_path, dim=300, dtype=np.float32):
    _, glove = read_glove_vecs(glove_path)  # ऊपर जैसा, लेकिन dtype=float32
    V = len(dictionary)
    W = np.random.uniform(-0.05, 0.05, (V, dim)).astype(dtype)
    for w, idx in dictionary.items():
        vec = glove.get(w)
        if vec is not None and vec.shape[0] == dim:
            W[idx] = vec
    return torch.tensor(W)

# usage
# emb_weight = build_embedding_matrix(dictionary, "glove.6B.300d.txt", dim=300)
# model.in_embeddings.weight.data.copy_(emb_weight)
```

### word2vec टेक्स्ट/बाइनरी के साथ त्वरित अंतर

* **GloVe टेक्स्ट**: कोई हेडर नहीं, `word float float ...`
* **word2vec टेक्स्ट**: अक्सर `"<vocab> <dim>"` हेडर से शुरू होता है।
* **word2vec बाइनरी**: हेडर + बाइनरी फ्लोट।

यदि आपको कभी word2vec फॉर्मेट की अपेक्षा करने वाले टूलिंग का उपयोग करने की आवश्यकता हो, तो `gensim.scripts.glove2word2vec` से कनवर्ट करें।