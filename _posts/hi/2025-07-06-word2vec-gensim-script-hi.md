---
audio: false
generated: true
lang: hi
layout: post
title: जेनसिम के साथ वर्डटूवेक स्क्रिप्ट
translated: true
type: note
---

आपको Word2Vec के लिए एक Python स्क्रिप्ट प्रदान करने के लिए, मुझे कुछ धारणाएं बनाने की आवश्यकता है क्योंकि "Word2Vec के बारे में एक स्क्रिप्ट" काफी व्यापक हो सकती है। मैं दो सामान्य परिदृश्य प्रदान करूंगा:

1.  **प्रशिक्षण और बुनियादी उपयोग के लिए `gensim` का उपयोग करने वाली एक सरल स्क्रिप्ट:** यह Python में Word2Vec का उपयोग करने का सबसे आम और व्यावहारिक तरीका है।
2.  **स्क्रैच से एक बहुत ही बुनियादी, वैचारिक कार्यान्वयन:** यह मुख्य एल्गोरिदम को समझने के लिए अधिक है, लेकिन जटिलता और अनुकूलन के कारण वास्तविक दुनिया में उपयोग के लिए कम व्यावहारिक है।

आपके अनुरोध को देखते हुए, मैं `gensim` दृष्टिकोण को प्राथमिकता दूंगा क्योंकि यही अधिकांश लोग उपयोग करते हैं।

-----

### `gensim` का उपयोग करके Word2Vec के लिए Python स्क्रिप्ट

यह स्क्रिप्ट प्रदर्शित करेगी:

  * नमूना पाठ डेटा तैयार करना।
  * एक Word2Vec मॉडल को प्रशिक्षित करना।
  * सबसे समान शब्द ढूंढना।
  * शब्द सादृश्य (analogies) करना।
  * मॉडल को सहेजना और लोड करना।

**पूर्वापेक्षाएँ:**

आपको `gensim` लाइब्रेरी इंस्टॉल करनी होगी:

```bash
pip install gensim
```

**Python स्क्रिप्ट (`word2vec_gensim_example.py`):**

```python
import gensim
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import logging

# प्रशिक्षण प्रगति देखने के लिए लॉगिंग कॉन्फ़िगर करें
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# --- 1. नमूना पाठ डेटा तैयार करें ---
# वास्तविक दुनिया के परिदृश्य में, आप फ़ाइलों से अपना पाठ डेटा लोड करेंगे।
# यहां, हम वाक्यों की एक साधारण सूची का उपयोग करते हैं।
raw_sentences = [
    "I love natural language processing.",
    "Word embeddings are a fascinating topic.",
    "Machine learning revolutionizes many industries.",
    "Deep learning is a subset of machine learning.",
    "Natural language processing uses various techniques.",
    "Computers understand human language better with word vectors.",
    "The quick brown fox jumps over the lazy dog.",
    "Dog and cat are common pets.",
    "King is to Queen as Man is to Woman."
]

# वाक्यों को प्रीप्रोसेस करें: टोकनाइज़ करें और लोअरकेस में बदलें
# इसके लिए gensim का simple_preprocess सुविधाजनक है
tokenized_sentences = [simple_preprocess(sentence) for sentence in raw_sentences]

print("\n--- Tokenized Sentences ---")
for sentence in tokenized_sentences:
    print(sentence)

# --- 2. Word2Vec मॉडल को प्रशिक्षित करें ---
# समझाए गए पैरामीटर:
#   vector_size: शब्द वैक्टर की आयामीता।
#   window: एक वाक्य के भीतर वर्तमान और अनुमानित शब्द के बीच की अधिकतम दूरी।
#   min_count: कुल आवृत्ति इससे कम वाले सभी शब्दों को नज़रअंदाज़ करता है।
#   sg: प्रशिक्षण एल्गोरिदम: CBOW के लिए 0, Skip-gram के लिए 1। Skip-gram आम तौर पर दुर्लभ शब्दों के लिए बेहतर होता है।
#   workers: मॉडल को प्रशिक्षित करने के लिए इतने वर्कर थ्रेड्स का उपयोग करें (=तेज़ प्रशिक्षण)।
#   epochs: कॉर्पस पर पुनरावृत्तियों (epochs) की संख्या।
model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=100,      # उदाहरण: 100-आयामी वैक्टर
    window=5,             # प्रत्येक तरफ 5 शब्दों की संदर्भ विंडो
    min_count=1,          # सभी शब्दों को शामिल करें (इस छोटे उदाहरण के लिए)
    sg=1,                 # Skip-gram (sg=1) का उपयोग करें
    workers=4,            # प्रशिक्षण के लिए 4 CPU कोर का उपयोग करें
    epochs=10             # 10 epochs के लिए प्रशिक्षण दें
)

print("\n--- Model Training Complete ---")

# --- 3. मॉडल का पता लगाएं ---

# किसी विशिष्ट शब्द के लिए वेक्टर प्राप्त करें
try:
    word_vector = model.wv['machine']
    print(f"\nVector for 'machine' (first 10 dimensions): {word_vector[:10]}")
    print(f"Vector for 'machine' shape: {word_vector.shape}")
except KeyError:
    print("\n'machine' not found in vocabulary.")

# सबसे समान शब्द ढूंढें
print("\n--- Most Similar Words to 'machine' ---")
try:
    similar_words = model.wv.most_similar('machine')
    for word, similarity in similar_words:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n'machine' not found in vocabulary.")

print("\n--- Most Similar Words to 'dog' ---")
try:
    similar_words_dog = model.wv.most_similar('dog')
    for word, similarity in similar_words_dog:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n'dog' not found in vocabulary.")


# शब्द सादृश्य करें (जैसे, King - Man + Woman = Queen)
# यह बहुत छोटे डेटासेट के साथ पूरी तरह से काम नहीं कर सकता है, लेकिन अवधारणा को प्रदर्शित करता है।
print("\n--- Word Analogies (King - Man + Woman = ?) ---")
try:
    result = model.wv.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
    if result:
        print(f"King - Man + Woman is similar to: {result[0][0]} (similarity: {result[0][1]:.4f})")
    else:
        print("No result for analogy. Vocabulary might be too small.")
except KeyError as e:
    print(f"One or more words for analogy not found in vocabulary: {e}")
except Exception as e:
    print(f"An error occurred during analogy: {e}")

# दो शब्दों के बीच समानता की जांच करें
print("\n--- Similarity between 'machine' and 'learning' ---")
try:
    similarity = model.wv.similarity('machine', 'learning')
    print(f"Similarity: {similarity:.4f}")
except KeyError:
    print("One or both words not found in vocabulary.")

print("\n--- Similarity between 'dog' and 'cat' ---")
try:
    similarity_pets = model.wv.similarity('dog', 'cat')
    print(f"Similarity: {similarity_pets:.4f}")
except KeyError:
    print("One or both words not found in vocabulary.")

print("\n--- Similarity between 'dog' and 'computer' ---")
try:
    similarity_diff = model.wv.similarity('dog', 'computer')
    print(f"Similarity: {similarity_diff:.4f}")
except KeyError:
    print("One or both words not found in vocabulary.")

# --- 4. मॉडल को सहेजें और लोड करें ---
model_path = "word2vec_model.bin"
model.save(model_path)
print(f"\nModel saved to {model_path}")

# मॉडल को वापस लोड करें
loaded_model = Word2Vec.load(model_path)
print(f"Model loaded from {model_path}")

# लोड किए गए मॉडल को सत्यापित करें
print("\n--- Verify Loaded Model (Most Similar Words to 'machine' using loaded model) ---")
try:
    similar_words_loaded = loaded_model.wv.most_similar('machine')
    for word, similarity in similar_words_loaded:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n'machine' not found in vocabulary in loaded model.")

print("\nScript execution complete.")
```

**स्क्रिप्ट कैसे चलाएं:**

1.  ऊपर दिए गए कोड को एक Python फ़ाइल के रूप में सहेजें (जैसे, `word2vec_gensim_example.py`)।
2.  अपना टर्मिनल या कमांड प्रॉम्प्ट खोलें।
3.  उस डायरेक्टरी पर नेविगेट करें जहां आपने फ़ाइल सहेजी है।
4.  स्क्रिप्ट को इस प्रकार चलाएं: `python word2vec_gensim_example.py`

-----

### Word2Vec में मुख्य अवधारणाएं (`gensim` कार्यान्वयन)

  * **`gensim.models.Word2Vec`**: प्रशिक्षण के लिए मुख्य वर्ग।
  * **`sentences`**: इटरेबल्स का एक इटरेबल, जहां बाहरी इटरेबल कॉर्पस है और आंतरिक इटरेबल शब्दों की सूची (टोकनाइज़्ड वाक्य) हैं।
  * **`vector_size`**: शब्द वैक्टर के लिए आयामों की संख्या। उच्च आयाम अधिक बारीकियों को पकड़ सकते हैं लेकिन अधिक डेटा और गणना की आवश्यकता होती है।
  * **`window`**: एक वाक्य में वर्तमान शब्द और उसके आस-पास के शब्दों के बीच की अधिकतम दूरी।
  * **`min_count`**: जो शब्द `min_count` से कम बार आते हैं, उन्हें नज़रअंदाज़ कर दिया जाता है। यह उन बहुत दुर्लभ शब्दों को फ़िल्टर करने में मदद करता है जिनके सार्थक एम्बेडिंग नहीं हो सकते हैं।
  * **`sg` (Skip-gram बनाम CBOW)**:
      * `sg=0` (CBOW - Continuous Bag of Words): संदर्भ के आधार पर वर्तमान शब्द की भविष्यवाणी करता है। प्रशिक्षित करने में तेज़।
      * `sg=1` (Skip-gram): वर्तमान शब्द को देखते हुए आस-पास के शब्दों की भविष्यवाणी करता है। आम तौर पर दुर्लभ शब्दों के लिए बेहतर प्रदर्शन करता है।
  * **`workers`**: प्रशिक्षण के लिए उपयोग किए जाने वाले CPU कोर की संख्या, प्रक्रिया को गति देती है।
  * **`epochs`**: एल्गोरिदम द्वारा पूरे डेटासेट पर पुनरावृत्तियों की संख्या। अधिक epochs बेहतर गुणवत्ता वाले एम्बेडिंग की ओर ले जा सकते हैं लेकिन अधिक समय भी लेते हैं।
  * **`model.wv`**: "शब्द वैक्टर" ऑब्जेक्ट (`KeyedVectors`) जिसमें प्रशिक्षित शब्द एम्बेडिंग और `most_similar`, `similarity` आदि जैसी विधियाँ शामिल हैं। आप सीधे `model.wv['word']` की तरह वैक्टर तक भी पहुंच सकते हैं।

-----

यह `gensim` स्क्रिप्ट Word2Vec के साथ काम करने के लिए एक ठोस आधार प्रदान करती है। वास्तविक दुनिया के अनुप्रयोगों के लिए, आप आम तौर पर एक बहुत बड़े कॉर्पस (जैसे, विकिपीडिया, Common Crawl) का उपयोग करेंगे और इष्टतम प्रदर्शन के लिए हाइपरपैरामीटर को ट्यून करेंगे।