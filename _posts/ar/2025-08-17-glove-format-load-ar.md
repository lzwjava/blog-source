---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دليل تنسيق وتحميل GloVe
translated: true
type: note
---

متجهات GloVe هي ملفات نصية عادية. كل سطر يمثل رمزًا واحدًا يتبعه قيم التضمين الخاصة به، وكلها مفصولة بمسافات. **لا يوجد رأس** (على عكس العديد من ملفات word2vec النصية).

مثال (GloVe بُعد 300):

```
the 0.418 0.24968 -0.41242 0.1217 ... 0.34527   # 300 رقم عائم إجمالاً
to   0.68047 -0.039263 -0.67412 0.056051 ... -0.067549
U.S. 0.3459  0.21513  -0.09982  0.244 ... 0.024118
```

بعض الملاحظات العملية:

* الإصدارات الشائعة:

  * `glove.6B.{50,100,200,300}d.txt` (ويكيبيديا + Gigaword؛ \~400k مفردات، أحرف صغيرة).
  * `glove.840B.300d.txt` (Common Crawl؛ \~2.2M مفردات).
  * `glove.twitter.27B.{25,50,100,200}d.txt` (تويتر؛ الكثير من الهاشتاغ والرموز التعبيرة).
* الرموز لا تحتوي أبدًا على مسافات (تستخدم العبارات شرطات سفلية)، لذا فإن `line.split()` البسيط كافٍ.
* الأرقام العائمة هي ASCII؛ ستشاهد أعداد عشرية عادية وأحيانًا الترميز العلمي.
* لا يوجد صف `<unk>` خاص؛ التعامل مع الكلمات غير الموجودة في المفردات متروك لك.

دالة التحميل الخاصة بك

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

تطابق هذا التنسيق. هناك تحسينان صغيران قد ترغب فيهما:

1. استخدم float32 لتقليل الذاكرة إلى النصف:

```python
vec = np.asarray(line[1:], dtype=np.float32)
```

2. تخطى أسطر "الرأس" العرضية أو الأسطر السيئة (بعض الملفات المعاد تجميعها تضيف واحدًا):

```python
parts = line.rstrip().split(' ')
if len(parts) < 2: 
    continue
if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
    # يبدو كرأس على نمط word2vec: "<vocab> <dim>"
    continue
word, *vals = parts
```

### بناء مصفوفة تضمين لمفرداتك

بعد إنشاء `dictionary: word -> id`، قم بتعيين صفوف GloVe في مصفوفة أوزان لـ `nn.Embedding` الخاصة بك:

```python
def build_embedding_matrix(dictionary, glove_path, dim=300, dtype=np.float32):
    _, glove = read_glove_vecs(glove_path)  # كما هو مذكور أعلاه، ولكن dtype=float32
    V = len(dictionary)
    W = np.random.uniform(-0.05, 0.05, (V, dim)).astype(dtype)
    for w, idx in dictionary.items():
        vec = glove.get(w)
        if vec is not None and vec.shape[0] == dim:
            W[idx] = vec
    return torch.tensor(W)

# الاستخدام
# emb_weight = build_embedding_matrix(dictionary, "glove.6B.300d.txt", dim=300)
# model.in_embeddings.weight.data.copy_(emb_weight)
```

### مقارنة سريعة مع word2vec نصي/ثنائي

* **GloVe نصي**: لا يوجد رأس، `كلمة رقم_عائم رقم_عائم ...`
* **word2vec نصي**: غالبًا ما يبدأ برأس `"<vocab> <dim>"`.
* **word2vec ثنائي**: رأس + أرقام عائمة ثنائية.

إذا احتجت في أي وقت لاستخدام أدوات تتوقع تنسيق word2vec، قم بالتحويل باستخدام `gensim.scripts.glove2word2vec`.