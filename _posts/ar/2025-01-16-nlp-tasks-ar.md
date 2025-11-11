---
audio: false
lang: ar
layout: post
title: مهام معالجة اللغات الطبيعية
translated: true
type: note
---

المهام الأساسية لـ NLP (معالجة اللغة الطبيعية) تشكل أساسًا لفهم اللغة البشرية ومعالجتها وتوليدها. فيما يلي بعض المهام الأساسية في معالجة اللغة الطبيعية:

### 1. **التجزئة (Tokenization)**
   - تقسيم النص إلى وحدات أصغر مثل الكلمات أو الجمل أو الأجزاء الجزئية للكلمات.
   - مثال:
     - الإدخال: "!Natural Language Processing is fun"
     - الإخراج: ["Natural", "Language", "Processing", "is", "fun", "!"]

### 2. **وسم جزء الكلام (Part-of-Speech (POS) Tagging)**
   - تعيين وسوم نحوية (مثل الاسم، الفعل، الصفة) للكلمات في الجملة.
   - مثال:
     - الإدخال: "I love NLP."
     - الإخراج: [("I", "PRP"), ("love", "VBP"), ("NLP", "NN")]

### 3. **التعرف على الكيانات المسماة (Named Entity Recognition (NER))**
   - تحديد وتصنيف الكيانات (مثل الأشخاص، المنظمات، المواقع) في النص.
   - مثال:
     - الإدخال: "Barack Obama was born in Hawaii."
     - الإخراج: [("Barack Obama", "PERSON"), ("Hawaii", "LOCATION")]

### 4. **تحليل المشاعر (Sentiment Analysis)**
   - تحديد المشاعر أو العاطفة التي ينقلها النص (مثل إيجابي، سلبي، محايد).
   - مثال:
     - الإدخال: "!I love this movie"
     - الإخراج: "إيجابي"

### 5. **الاشتقاق والتجذير (Lemmatization and Stemming)**
   - اختزال الكلمات إلى أشكالها الجذرية.
   - مثال:
     - الإدخال: "running", "ran", "runs"
     - الإخراج (الاشتقاق): "run"
     - الإخراج (التجذير): "run"

### 6. **إزالة كلمات التوقف (Stop Word Removal)**
   - إزالة الكلمات الشائعة (مثل "and", "is", "the") التي لا تضيف معنى كبيرًا.
   - مثال:
     - الإدخال: "The cat is on the mat."
     - الإخراج: ["cat", "mat"]

### 7. **تصنيف النص (Text Classification)**
   - تصنيف النص إلى فئات أو تسميات محددة مسبقًا.
   - مثال:
     - الإدخال: "This is a sports article."
     - الإخراج: "الرياضة"

### 8. **نمذجة اللغة (Language Modeling)**
   - توقع الكلمة التالية في التسلسل أو تعيين احتمالات لتسلسلات الكلمات.
   - مثال:
     - الإدخال: "The cat sat on the ___"
     - الإخراج: ["mat" (0.8), "chair" (0.1), "floor" (0.1)]

### 9. **الترجمة الآلية (Machine Translation)**
   - ترجمة النص من لغة إلى أخرى.
   - مثال:
     - الإدخال: "Hello, how are you?"
     - الإخراج: "?Hola, ¿cómo estás"

### 10. **تلخيص النص (Text Summarization)**
   - إنشاء ملخص موجز من نص أطول.
   - مثال:
     - الإدخال: "Natural language processing is a subfield of AI. It involves understanding and generating human language."
     - الإخراج: "NLP is a subfield of AI for understanding and generating language."

### 11. **حل الإحالة (Coreference Resolution)**
   - تحديد متى تشير كلمات مختلفة إلى نفس الكيان.
   - مثال:
     - الإدخال: "Alice said she would come."
     - الإخراج: "Alice" -> "she"

### 12. **الإجابة على الأسئلة (Question Answering)**
   - الإجابة على الأسئلة بناءً على سياق معين أو معرفة.
   - مثال:
     - الإدخال: السياق: "Paris is the capital of France." السؤال: "What is the capital of France?"
     - الإخراج: "Paris"

### 13. **التضمينات الكلمية (Word Embeddings)**
   - تمثيل الكلمات كمتجهات مستمرة في فضاء متعدد الأبعاد.
   - مثال:
     - الإدخال: "king", "queen", "man", "woman"
     - الإخراج: علاقات مثل "king - man + woman ≈ queen"

### 14. **التدقيق الإملائي وتطبيع النص (Spell Checking and Text Normalization)**
   - تصحيح الأخطاء الإملائية وتوحيد النص (مثال: "u r" -> "you are").
   - مثال:
     - الإدخال: "!I luv NLP"
     - الإخراج: "!I love NLP"

### 15. **توليد النص (Text Generation)**
   - توليد نص متماسك من نموذج أو موجه إدخال.
   - مثال:
     - الإدخال: "Once upon a time,"
     - الإخراج: "Once upon a time, there lived a brave knight in a faraway kingdom."

هذه المهام تعمل كحجر أساس للأنظمة والتطبيقات الأكثر تعقيدًا في معالجة اللغة الطبيعية، مثل روبوتات الدردشة والمساعدات الافتراضية وأنظمة التوصية.