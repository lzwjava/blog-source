---
audio: false
generated: true
lang: ar
layout: post
title: نص وورد تو فِك باستخدام جنسيم
translated: true
type: note
---

لتزويدك بنص برمجي Python لـ Word2Vec، أحتاج إلى وضع بعض الافتراضات حول ما تبحث عنه، لأن "نصًا برمجيًا حول Word2Vec" يمكن أن يكون واسعًا جدًا. سأقدم سيناريوهين شائعين:

1.  **نص برمجي بسيط باستخدام `gensim` للتدريب والاستخدام الأساسي:** هذه هي الطريقة الأكثر شيوعًا وعملية لاستخدام Word2Vec في Python.
2.  **تنفيذ أساسي جدًا ومفاهيمي من الصفر:** هذا أكثر لفهم الخوارزميات الأساسية، ولكنه أقل عملية للاستخدام في العالم الحقيقي بسبب التعقيد والتحسين.

بناءً على طلبك، سأعطي الأولوية لنهج `gensim` لأنه ما يستخدمه معظم الناس.

-----

### نص برمجي Python لـ Word2Vec باستخدام `gensim`

سيوضح هذا النص البرمجي:

  * إعداد بيانات نصية عينة.
  * تدريب نموذج Word2Vec.
  * إيجاد الكلمات الأكثر تشابهًا.
  * إجراء القياسات التناظرية للكلمات.
  * حفظ وتحميل النموذج.

**المتطلبات الأساسية:**

ستحتاج إلى تثبيت مكتبة `gensim`:

```bash
pip install gensim
```

**النص البرمجي Python (`word2vec_gensim_example.py`):**

```python
import gensim
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import logging

# تكوين التسجيل لرؤية تقدم التدريب
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# --- 1. إعداد بيانات النص العينة ---
# في سيناريو حقيقي، ستقوم بتحميل بيانات النص الخاصة بك من الملفات.
# هنا، نستخدم قائمة بسيطة من الجمل.
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

# معالجة الجمل مسبقًا: تقسيم إلى وحدات وتحويل إلى أحرف صغيرة
# simple_preprocess من gensim ملائمة لهذا
tokenized_sentences = [simple_preprocess(sentence) for sentence in raw_sentences]

print("\n--- الجمل المقسمة إلى وحدات ---")
for sentence in tokenized_sentences:
    print(sentence)

# --- 2. تدريب نموذج Word2Vec ---
# المعلمات موضحة:
#   vector_size: أبعاد متجهات الكلمات.
#   window: أقصى مسافة بين الكلمة الحالية والكلمة المتوقعة داخل الجملة.
#   min_count: يتجاهل جميع الكلمات ذات التكرار الإجمالي الأقل من هذا.
#   sg: خوارزمية التدريب: 0 لـ CBOW، 1 لـ Skip-gram. Skip-gram بشكل عام أفضل للكلمات النادرة.
#   workers: استخدم هذا العدد من مؤشرات الترابط العاملة لتدريب النموذج (= تدريب أسرع).
#   epochs: عدد التكرارات (epochs) فوق مجموعة النصوص.
model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=100,      # مثال: متجهات ذات 100 بُعد
    window=5,             # نطاق سياقي مقداره 5 كلمات على كلا الجانبين
    min_count=1,          # تضمين جميع الكلمات (لهذا المثال الصغير)
    sg=1,                 # استخدام Skip-gram (sg=1)
    workers=4,            # استخدام 4 نوى معالجة للتدريب
    epochs=10             # التدريب لمدة 10 epochs
)

print("\n--- اكتمل تدريب النموذج ---")

# --- 3. استكشاف النموذج ---

# الحصول على المتجه لكلمة محددة
try:
    word_vector = model.wv['machine']
    print(f"\nالمتجه لكلمة 'machine' (أول 10 أبعاد): {word_vector[:10]}")
    print(f"شكل المتجه لكلمة 'machine': {word_vector.shape}")
except KeyError:
    print("\nكلمة 'machine' غير موجودة في المفردات.")

# العثور على الكلمات الأكثر تشابهًا
print("\n--- الكلمات الأكثر تشابهًا مع 'machine' ---")
try:
    similar_words = model.wv.most_similar('machine')
    for word, similarity in similar_words:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\nكلمة 'machine' غير موجودة في المفردات.")

print("\n--- الكلمات الأكثر تشابهًا مع 'dog' ---")
try:
    similar_words_dog = model.wv.most_similar('dog')
    for word, similarity in similar_words_dog:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\nكلمة 'dog' غير موجودة في المفردات.")


# إجراء القياسات التناظرية للكلمات (مثلًا، King - Man + Woman = Queen)
# قد لا يعمل هذا بشكل مثالي مع مجموعات البيانات الصغيرة جدًا، لكنه يوضح الفكرة.
print("\n--- القياس التناظري للكلمات (King - Man + Woman = ?) ---")
try:
    result = model.wv.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
    if result:
        print(f"King - Man + Woman يشبه: {result[0][0]} (التشابه: {result[0][1]:.4f})")
    else:
        print("لا توجد نتيجة للقياس. قد تكون المفردات صغيرة جدًا.")
except KeyError as e:
    print(f"واحدة أو أكثر من كلمات القياس غير موجودة في المفردات: {e}")
except Exception as e:
    print(f"حدث خطأ أثناء القياس: {e}")

# التحقق من التشابه بين كلمتين
print("\n--- التشابه بين 'machine' و 'learning' ---")
try:
    similarity = model.wv.similarity('machine', 'learning')
    print(f"التشابه: {similarity:.4f}")
except KeyError:
    print("واحدة أو كلتا الكلمتين غير موجودة في المفردات.")

print("\n--- التشابه بين 'dog' و 'cat' ---")
try:
    similarity_pets = model.wv.similarity('dog', 'cat')
    print(f"التشابه: {similarity_pets:.4f}")
except KeyError:
    print("واحدة أو كلتا الكلمتين غير موجودة في المفردات.")

print("\n--- التشابه بين 'dog' و 'computer' ---")
try:
    similarity_diff = model.wv.similarity('dog', 'computer')
    print(f"التشابه: {similarity_diff:.4f}")
except KeyError:
    print("واحدة أو كلتا الكلمتين غير موجودة في المفردات.")

# --- 4. حفظ وتحميل النموذج ---
model_path = "word2vec_model.bin"
model.save(model_path)
print(f"\nتم حفظ النموذج في {model_path}")

# تحميل النموذج مرة أخرى
loaded_model = Word2Vec.load(model_path)
print(f"تم تحميل النموذج من {model_path}")

# التحقق من النموذج المحمل
print("\n--- التحقق من النموذج المحمل (الكلمات الأكثر تشابهًا مع 'machine' باستخدام النموذج المحمل) ---")
try:
    similar_words_loaded = loaded_model.wv.most_similar('machine')
    for word, similarity in similar_words_loaded:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\nكلمة 'machine' غير موجودة في المفردات في النموذج المحمل.")

print("\nاكتمل تنفيذ النص البرمجي.")
```

**كيفية تشغيل النص البرمجي:**

1.  احفظ الكود أعلاه كملف Python (مثل `word2vec_gensim_example.py`).
2.  افتح طرفيتك أو موجه الأوامر.
3.  انتقل إلى الدليل حيث حفظت الملف.
4.  شغل النص البرمجي باستخدام: `python word2vec_gensim_example.py`

-----

### المفاهيم الأساسية في Word2Vec (تنفيذ `gensim`)

  * **`gensim.models.Word2Vec`**: الفئة الرئيسية للتدريب.
  * **`sentences`**: كائن قابل للتكرار من كائنات قابلة للتكرار، حيث التكرار الخارجي هو مجموعة النصوص والتكرارات الداخلية هي قوائم الكلمات (الجمل المقسمة إلى وحدات).
  * **`vector_size`**: عدد الأبعاد لمتجهات الكلمات. الأبعاد الأعلى يمكنها التقاط المزيد من الفروق الدقيقة ولكنها تتطلب المزيد من البيانات والحساب.
  * **`window`**: أقصى مسافة بين الكلمة الحالية والكلمات المحيطة بها في الجملة.
  * **`min_count`**: الكلمات التي تظهر مرات أقل من `min_count` يتم تجاهلها. هذا يساعد في تصفية الكلمات النادرة جدًا التي قد لا تحتوي على تضمينات ذات معنى.
  * **`sg` (Skip-gram مقابل CBOW)**:
      * `sg=0` (CBOW - Continuous Bag of Words): يتنبأ بالكلمة الحالية بناءً على سياقها. أسرع في التدريب.
      * `sg=1` (Skip-gram): يتنبأ بالكلمات المحيطة بمعلومية الكلمة الحالية. بشكل عام يعمل بشكل أفضل للكلمات النادرة.
  * **`workers`**: عدد نوى المعالج لاستخدامها في التدريب، مما يسرع العملية.
  * **`epochs`**: عدد المرات التي تمر فيها الخوارزمية على مجموعة البيانات بأكملها. المزيد من الـ epochs يمكن أن يؤدي إلى تضمينات أفضل جودة ولكنه يستغرق وقتًا أطول أيضًا.
  * **`model.wv`**: كائن "متجهات الكلمات" (`KeyedVectors`) الذي يحتوي على تضمينات الكلمات المدربة وطرق مثل `most_similar`، `similarity`، إلخ. يمكنك أيضًا الوصول إلى المتجهات مباشرة مثل `model.wv['word']`.

-----

يوفر نص `gensim` البرمجي هذا أساسًا متينًا للعمل مع Word2Vec. للتطبيقات الواقعية، سوف تستخدم عادة مجموعة نصوص أكبر بكثير (مثل Wikipedia، Common Crawl) وضبط المعلمات الفائقة للحصول على أفضل أداء.