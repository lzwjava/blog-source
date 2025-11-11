---
audio: false
lang: hi
layout: post
title: एनएलपी कार्य
translated: true
type: note
---

बेसिक NLP (नेचुरल लैंग्वेज प्रोसेसिंग) टास्क मानव भाषा को समझने, प्रोसेस करने और जनरेट करने की आधारशिला हैं। यहाँ NLP के कुछ मुख्य टास्क दिए गए हैं:

### 1. **टोकननाइजेशन (Tokenization)**
   - टेक्स्ट को छोटी इकाइयों जैसे शब्दों, वाक्यों, या सब-वर्ड्स में विभाजित करना।
   - उदाहरण:
     - इनपुट: "Natural Language Processing is fun!"
     - आउटपुट: ["Natural", "Language", "Processing", "is", "fun", "!"]

### 2. **पार्ट-ऑफ-स्पीच (POS) टैगिंग**
   - वाक्य के शब्दों को व्याकरणिक टैग (जैसे संज्ञा, क्रिया, विशेषण) देना।
   - उदाहरण:
     - इनपुट: "I love NLP."
     - आउटपुट: [("I", "PRP"), ("love", "VBP"), ("NLP", "NN")]

### 3. **नामित इकाई पहचान (Named Entity Recognition - NER)**
   - टेक्स्ट में इकाइयों (जैसे व्यक्ति, संगठन, स्थान) की पहचान करना और उन्हें वर्गीकृत करना।
   - उदाहरण:
     - इनपुट: "Barack Obama was born in Hawaii."
     - आउटपुट: [("Barack Obama", "PERSON"), ("Hawaii", "LOCATION")]

### 4. **सेंटीमेंट एनालिसिस (Sentiment Analysis)**
   - टेक्स्ट में व्यक्त भावना या इमोशन (जैसे सकारात्मक, नकारात्मक, तटस्थ) का निर्धारण करना।
   - उदाहरण:
     - इनपुट: "I love this movie!"
     - आउटपुट: "Positive"

### 5. **लेम्माटाइजेशन और स्टेमिंग (Lemmatization and Stemming)**
   - शब्दों को उनके मूल रूप में लाना।
   - उदाहरण:
     - इनपुट: "running", "ran", "runs"
     - आउटपुट (लेम्माटाइजेशन): "run"
     - आउटपुट (स्टेमिंग): "run"

### 6. **स्टॉप वर्ड रिमूवल (Stop Word Removal)**
   - आम शब्दों (जैसे "and", "is", "the") को हटाना जो महत्वपूर्ण अर्थ नहीं रखते।
   - उदाहरण:
     - इनपुट: "The cat is on the mat."
     - आउटपुट: ["cat", "mat"]

### 7. **टेक्स्ट क्लासिफिकेशन (Text Classification)**
   - टेक्स्ट को पूर्वनिर्धारित श्रेणियों या लेबल्स में वर्गीकृत करना।
   - उदाहरण:
     - इनपुट: "This is a sports article."
     - आउटपुट: "Sports"

### 8. **लैंग्वेज मॉडलिंग (Language Modeling)**
   - किसी अनुक्रम में अगले शब्द की भविष्यवाणी करना या शब्दों के अनुक्रमों को संभावनाएं देना।
   - उदाहरण:
     - इनपुट: "The cat sat on the ___"
     - आउटपुट: ["mat" (0.8), "chair" (0.1), "floor" (0.1)]

### 9. **मशीन ट्रांसलेशन (Machine Translation)**
   - टेक्स्ट का एक भाषा से दूसरी भाषा में अनुवाद करना।
   - उदाहरण:
     - इनपुट: "Hello, how are you?"
     - आउटपुट: "Hola, ¿cómo estás?"

### 10. **टेक्स्ट सारांशन (Text Summarization)**
   - लंबे टेक्स्ट से संक्षिप्त सारांश तैयार करना।
   - उदाहरण:
     - इनपुट: "Natural language processing is a subfield of AI. It involves understanding and generating human language."
     - आउटपुट: "NLP is a subfield of AI for understanding and generating language."

### 11. **कोरफेरेंस रेजोल्यूशन (Coreference Resolution)**
   - यह पहचानना कि विभिन्न शब्द एक ही इकाई को संदर्भित करते हैं।
   - उदाहरण:
     - इनपुट: "Alice said she would come."
     - आउटपुट: "Alice" -> "she"

### 12. **प्रश्नोत्तर (Question Answering)**
   - दिए गए संदर्भ या ज्ञान के आधार पर प्रश्नों के उत्तर देना।
   - उदाहरण:
     - इनपुट: संदर्भ: "Paris is the capital of France."
       प्रश्न: "What is the capital of France?"
     - आउटपुट: "Paris"

### 13. **वर्ड एम्बेडिंग (Word Embeddings)**
   - शब्दों को उच्च-आयामी स्थान में सतत वैक्टर के रूप में प्रस्तुत करना।
   - उदाहरण:
     - इनपुट: "king", "queen", "man", "woman"
     - आउटपुट: "king - man + woman ≈ queen" जैसे संबंध

### 14. **स्पेल चेकिंग और टेक्स्ट नॉर्मलाइजेशन (Spell Checking and Text Normalization)**
   - गलत वर्तनियों को सही करना और टेक्स्ट को मानक रूप देना (जैसे, "u r" -> "you are")।
   - उदाहरण:
     - इनपुट: "I luv NLP!"
     - आउटपुट: "I love NLP!"

### 15. **टेक्स्ट जनरेशन (Text Generation)**
   - किसी मॉडल या इनपुट प्रॉम्प्ट से सुसंगत टेक्स्ट जनरेट करना।
   - उदाहरण:
     - इनपुट: "Once upon a time,"
     - आउटपुट: "Once upon a time, there lived a brave knight in a faraway kingdom."

ये टास्क अधिक जटिल NLP सिस्टम और एप्लिकेशन जैसे चैटबॉट्स, वर्चुअल असिस्टेंट्स और रिकमेंडेशन सिस्टम के लिए बिल्डिंग ब्लॉक्स का काम करते हैं।