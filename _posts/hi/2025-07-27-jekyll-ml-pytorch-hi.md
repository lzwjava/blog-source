---
audio: false
generated: true
image: false
lang: hi
layout: post
title: जेकिल ब्लॉग को पाइटॉर्च के साथ उन्नत बनाना
translated: true
type: note
---

### PyTorch का उपयोग करके अपने Jekyll ब्लॉग में ML/AI सुविधाएँ जोड़ना

चूंकि आप एक Jekyll ब्लॉग (एक स्टैटिक साइट जनरेटर) चला रहे हैं, इसलिए सिफारिशें या वर्गीकरण जैसी ML/AI सुविधाओं को एकीकृत करने के लिए कुछ रचनात्मकता की आवश्यकता होती है। Jekyll स्टैटिक HTML बनाता है, इसलिए डायनामिक एलिमेंट्स (जैसे, रीयल-टाइम सिफारिशें) के लिए क्लाइंट-साइड JavaScript या बिल्ड प्रक्रिया के दौरान पूर्व-गणना की आवश्यकता हो सकती है, जो Jekyll प्लगइन्स या स्क्रिप्ट्स के माध्यम से की जा सकती है। आपने LLM API से बचने और PyTorch के साथ अपने खुद के न्यूरल नेटवर्क पर ध्यान केंद्रित करने का उल्लेख किया है—बढ़िया, क्योंकि यह सब कुछ लोकल और कस्टमाइजेबल रखता है। मैं व्यावहारिक विचारों की रूपरेखा प्रस्तुत करूंगा, जो PyTorch इम्प्लीमेंटेशन पर केंद्रित हैं। यह मानता है कि आपके पास NumPy (डेटा हैंडलिंग के लिए) जैसी बेसिक लाइब्रेरीज़ तक पहुंच है और आप टेक्स्ट प्रीप्रोसेसिंग को मैन्युअल रूप से या सरल टोकननाइजेशन के साथ संभाल सकते हैं (क्योंकि उन्नत NLP लाइब्रेरीज़ जैसे Hugging Face का आपके सेटअप में उल्लेख नहीं किया गया है, लेकिन आप उन्हें स्थानीय रूप से आवश्यकतानुसार जोड़ सकते हैं)।

आप संभवतः Python स्क्रिप्ट्स (जैसे, अपनी `scripts/` डायरेक्टरी में) बनाएंगे जो Jekyll की बिल्ड प्रक्रिया के दौरान चलती हैं (Makefile हुक या GitHub Actions के माध्यम से, यदि डिप्लॉय किया गया है)। उदाहरण के लिए, `_posts/` में Markdown पोस्ट को प्रोसेस करें, JSON डेटा जनरेट करें, और इसे Liquid टेम्पलेट्स के माध्यम से अपनी साइट में इंजेक्ट करें।

#### 1. PyTorch क्लासिफायर के साथ आर्टिकल वर्गीकरण
पोस्ट्स को स्वचालित रूप से वर्गीकृत करें (उदाहरण के लिए, "ML", "Notes", "Latex" जैसे विषयों में) एक सरल न्यूरल नेटवर्क क्लासिफायर को प्रशिक्षित करके। यह सुपरवाइज्ड लर्निंग है: आपको प्रशिक्षण डेटा के रूप में अपनी पोस्ट्स के एक सबसेट को मैन्युअल रूप से लेबल करने की आवश्यकता होगी। यदि आपके पास लेबल नहीं हैं, तो अनसुपरवाइज्ड क्लस्टरिंग के साथ शुरुआत करें (नीचे देखें)।

**चरण:**
- **डेटा तैयारी:** `_posts/` में अपनी Markdown फाइलों को पार्स करें। टेक्स्ट कंटेंट निकालें (फ्रंटमैटर को छोड़ दें)। एक डेटासेट बनाएं: (टेक्स्ट, लेबल) जोड़ियों की सूची। शुरुआत में ~50-100 लेबल किए गए उदाहरणों के लिए एक CSV या सूची का उपयोग करें।
- **प्रीप्रोसेसिंग:** टेक्स्ट को टोकननाइज़ करें (स्पेस/व्हाइटस्पेस पर सरल विभाजन), एक शब्दावली बनाएं, संख्यात्मक इंडेक्स में कनवर्ट करें। वन-हॉट एन्कोडिंग या बेसिक एम्बेडिंग का उपयोग करें।
- **मॉडल:** मल्टी-क्लास क्लासिफिकेशन के लिए PyTorch में एक बुनियादी फीडफॉरवर्ड न्यूरल नेटवर्क।
- **प्रशिक्षण:** अपने लोकल मशीन पर प्रशिक्षित करें। क्रॉस-एन्ट्रॉपी लॉस और Adam ऑप्टिमाइज़र का उपयोग करें।
- **एकीकरण:** सभी पोस्ट्स को वर्गीकृत करने के लिए बिल्ड के दौरान स्क्रिप्ट चलाएं, एक `categories.json` फाइल जनरेट करें, और इसे Jekyll में पेजों को टैग करने या श्रेणी इंडेक्स बनाने के लिए उपयोग करें।

**उदाहरण PyTorch कोड स्निपेट (एक स्क्रिप्ट में जैसे `scripts/categorize_posts.py`):**
```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import os
from collections import Counter

# चरण 1: डेटा लोड और प्रीप्रोसेस करें (सरलीकृत)
def load_posts(posts_dir='_posts'):
    texts = []
    labels = []  # मैनुअल लेबल मानें: 0=ML, 1=Notes, आदि।
    for file in os.listdir(posts_dir):
        if file.endswith('.md'):
            with open(os.path.join(posts_dir, file), 'r') as f:
                content = f.read().split('---')[2].strip()  # फ्रंटमैटर छोड़ें
                texts.append(content)
                # प्लेसहोल्डर: एक dict या CSV से लेबल लोड करें
                labels.append(0)  # वास्तविक लेबल के साथ बदलें
    return texts, labels

texts, labels = load_posts()
# शब्दावली बनाएं (शीर्ष 1000 शब्द)
all_words = ' '.join(texts).lower().split()
vocab = {word: idx for idx, word in enumerate(Counter(all_words).most_common(1000))}
vocab_size = len(vocab)

# टेक्स्ट को वैक्टर में बदलें (बैग-ऑफ-वर्ड्स)
def text_to_vec(text):
    vec = np.zeros(vocab_size)
    for word in text.lower().split():
        if word in vocab:
            vec[vocab[word]] += 1
    return vec

X = np.array([text_to_vec(t) for t in texts])
y = torch.tensor(labels, dtype=torch.long)

# चरण 2: मॉडल परिभाषित करें
class Classifier(nn.Module):
    def __init__(self, input_size, num_classes):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, num_classes)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = Classifier(vocab_size, num_classes=3)  # num_classes समायोजित करें

# चरण 3: प्रशिक्षण
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()
X_tensor = torch.tensor(X, dtype=torch.float32)

for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X_tensor)
    loss = loss_fn(outputs, y)
    loss.backward()
    optimizer.step()
    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# चरण 4: नई पोस्ट पर अनुमान
def classify_post(text):
    vec = torch.tensor(text_to_vec(text), dtype=torch.float32).unsqueeze(0)
    with torch.no_grad():
        pred = model(vec).argmax(1).item()
    return pred  # श्रेणी नाम पर मैप वापस करें

# मॉडल सेव करें: torch.save(model.state_dict(), 'classifier.pth')
# बिल्ड स्क्रिप्ट में: सभी पोस्ट्स को वर्गीकृत करें और JSON में लिखें
```

**सुधार:** बेहतर सटीकता के लिए, वर्ड एम्बेडिंग (PyTorch में एक सरल Embedding लेयर प्रशिक्षित करें) का उपयोग करें या अधिक लेयर्स जोड़ें। यदि अनलेबल्ड है, तो क्लस्टरिंग पर स्विच करें (जैसे, एम्बेडिंग पर KMeans—अगला भाग देखें)। इस स्क्रिप्ट को अपनी Makefile में चलाएं: `jekyll build && python scripts/categorize_posts.py`.

#### 2. PyTorch एम्बेडिंग के साथ सिफारिश प्रणाली
पाठकों को समान लेखों की सिफारिश करें (जैसे, "आपको यह भी पसंद आ सकता है...")। कंटेंट-आधारित सिफारिश का उपयोग करें: प्रत्येक पोस्ट के लिए एम्बेडिंग सीखें, फिर समानता (कोसाइन दूरी) की गणना करें। उपयोगकर्ता डेटा की आवश्यकता नहीं—बस पोस्ट सामग्री।

**चरण:**
- **डेटा:** ऊपर के समान—पोस्ट से टेक्स्ट निकालें।
- **मॉडल:** टेक्स्ट को लो-डायमेंशनल एम्बेडिंग (जैसे, 64-डिम वैक्टर) में संपीड़ित करने के लिए PyTorch में एक ऑटोएनकोडर प्रशिक्षित करें।
- **प्रशिक्षण:** सार्थक प्रतिनिधित्व सीखने के लिए पुनर्निर्माण हानि को कम करें।
- **सिफारिशें:** किसी दी गई पोस्ट के लिए, एम्बेडिंग स्पेस में निकटतम पड़ोसियों को खोजें।
- **एकीकरण:** बिल्ड के दौरान एम्बेडिंग की प्री-कंप्यूट करें, JSON में स्टोर करें। सिफारिशें दिखाने के लिए साइट पर JS (या स्टैटिक सूचियों के लिए Liquid) का उपयोग करें।

**उदाहरण PyTorch कोड स्निपेट (`scripts/recommend_posts.py` में):**
```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
# ऊपर से load_posts और text_to_vec का पुन: उपयोग करें

texts, _ = load_posts()  # लेबल्स को नजरअंदाज करें
X = np.array([text_to_vec(t) for t in texts])
X_tensor = torch.tensor(X, dtype=torch.float32)

# ऑटोएनकोडर मॉडल
class Autoencoder(nn.Module):
    def __init__(self, input_size, embedding_size=64):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_size, 256),
            nn.ReLU(),
            nn.Linear(256, embedding_size)
        )
        self.decoder = nn.Sequential(
            nn.Linear(embedding_size, 256),
            nn.ReLU(),
            nn.Linear(256, input_size)
        )
    
    def forward(self, x):
        emb = self.encoder(x)
        return self.decoder(emb)

model = Autoencoder(vocab_size)
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.MSELoss()

for epoch in range(200):
    optimizer.zero_grad()
    reconstructed = model(X_tensor)
    loss = loss_fn(reconstructed, X_tensor)
    loss.backward()
    optimizer.step()
    if epoch % 20 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# एम्बेडिंग प्राप्त करें
with torch.no_grad():
    embeddings = model.encoder(X_tensor).numpy()

# सिफारिश करें: पोस्ट i के लिए, शीर्ष 3 समान खोजें
similarities = cosine_similarity(embeddings)
for i in range(len(texts)):
    rec_indices = similarities[i].argsort()[-4:-1][::-1]  # स्वयं को छोड़कर शीर्ष 3
    print(f'Recs for post {i}: {rec_indices}')

# Jekyll के लिए एम्बेडिंग को JSON में सेव करें
import json
with open('embeddings.json', 'w') as f:
    json.dump({'embeddings': embeddings.tolist(), 'posts': [f'post_{i}' for i in range(len(texts))]}, f)
```

**सुधार:** बेहतर एम्बेडिंग के लिए एक variational ऑटोएनकोडर का उपयोग करें। यदि आपके पास उपयोगकर्ता दृश्य (एनालिटिक्स के माध्यम से) हैं, तो PyTorch में मैट्रिक्स फैक्टराइजेशन मॉडल के साथ सहयोगात्मक फ़िल्टरिंग जोड़ें। क्लाइंट-साइड: JSON को JS में लोड करें और व्यक्तिगतकरण के लिए ऑन-द-फ्लाई समानताएं गणना करें।

#### 3. PyTorch के साथ अन्य विचार
- **ऑटो-टैगिंग के लिए अनसुपरवाइज्ड क्लस्टरिंग:** यदि लेबलिंग थकाऊ है, तो पोस्ट्स को विषयों में समूहित करने के लिए एम्बेडिंग (ऊपर ऑटोएनकोडर से) + KMeans क्लस्टरिंग का उपयोग करें। एम्बेडिंग के लिए PyTorch, क्लस्टरिंग के लिए NumPy/SciPy।
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=5)
  clusters = kmeans.fit_predict(embeddings)
  # क्लस्टर के आधार पर टैग असाइन करें
  ```
  एकीकृत करें: स्क्रिप्ट के माध्यम से फ्रंटमैटर में टैग जनरेट करें।

- **सिमेंटिक सर्च एन्हांसमेंट:** क्वेरी और पोस्ट्स को समान रूप से एम्बेड करें, फिर सर्च बार के लिए कोसाइन समानता का उपयोग करें। पोस्ट एम्बेडिंग प्रीकंप्यूट करें; क्वेरी एम्बेडिंग के लिए JS का उपयोग करें (लेकिन चूंकि PyTorch Python है, JS इनफेरेंस के लिए मॉडल को ONNX में एक्सपोर्ट करें ONNX.js के माध्यम से, या सर्च को स्टैटिक रखें)।

- **पोस्ट सारांशीकरण:** जोड़े (पूर्ण पाठ, मैनुअल सारांश) डेटा पर एक seq2seq मॉडल (PyTorch में RNN/LSTM) प्रशिक्षित करें। बड़े डेटासेट के बिना चुनौतीपूर्ण, लेकिन अपनी पोस्ट्स के साथ छोटे स्तर पर शुरुआत करें। एक्सर्प्ट जनरेट करने के लिए उपयोग करें।

**सामान्य सुझाव:**
- **स्केलेबिलिटी:** एक छोटे ब्लॉग के लिए, CPU पर प्रशिक्षित करें; PyTorch इसे ठीक से संभालता है। मॉडल को `torch.save` के साथ सेव करें और इनफेरेंस के लिए लोड करें।
- **बिल्ड एकीकरण:** Makefile में जोड़ें: `train: python scripts/train_models.py` फिर `build: jekyll build && python scripts/generate_features.py`।
- **सीमाएँ:** उन्नत NLP (जैसे, transformers) के बिना, परिणाम बुनियादी होते हैं—स्थानीय रूप से `torchtext` या मैनुअल GloVe एम्बेडिंग जोड़ने पर विचार करें। अपनी `ml/` या `notes/` डायरेक्टरीज़ पर परीक्षण करें।
- **डिप्लॉयमेंट:** यदि GitHub Pages पर है, तो CI में स्क्रिप्ट्स चलाएं। डायनामिक सामग्री के लिए, एक हल्का Flask बैकएंड जोड़ने पर विचार करें, लेकिन यह स्टैटिक Jekyll से अलग हो जाता है।

यदि आप अधिक विवरण साझा करते हैं (जैसे, पोस्ट गिनती, विषय), तो मैं इन्हें परिष्कृत कर सकता हूं!