---
audio: false
generated: true
image: false
lang: ar
layout: post
title: تحميل متجهات GloVe بطريقتين
translated: true
type: note
---

لديك طريقتان سهلتان للحصول على متجهات GloVe لكلمات مثل `the`، `to`، `U.S.` ولنصك الخاص:

---

## الخيار أ — تنزيل Stanford GloVe والبحث باستخدام `gensim`

هذا هو المسار الأكثر شيوعًا ويعمل دون اتصال بالإنترنت تمامًا بعد التنزيل.

```python
# 1) التنزيل وفك الضغط (للمرة الأولى فقط)
import os, zipfile, urllib.request
url = "https://nlp.stanford.edu/data/glove.6B.zip"
zip_path = "glove.6B.zip"
if not os.path.exists(zip_path):
    urllib.request.urlretrieve(url, zip_path)
with zipfile.ZipFile(zip_path) as zf:
    zf.extract("glove.6B.300d.txt")  # مجموعة 300 بعد

# 2) تحويل تنسيق GloVe -> تنسيق نص word2vec ثم التحميل
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors

glove_path = "glove.6B.300d.txt"
w2v_path   = "glove.6B.300d.w2v.txt"
if not os.path.exists(w2v_path):
    glove2word2vec(glove_path, w2v_path)

vectors = KeyedVectors.load_word2vec_format(w2v_path, binary=False)
print(vectors.vector_size)  # 300

# 3) عمليات البحث عن كلمة مفردة
print(vectors['the'][:5])   # أول 5 أبعاد
print(vectors['to'][:5])

# ملاحظة: المفردات في glove.6B كلها أحرف صغيرة.
# 'U.S.' -> 'u.s.' في هذه المفردات (إذا كانت موجودة). الطريقة الأكثر أمانًا: تحويل كلماتك إلى أحرف صغيرة.
print(vectors['u.s.'][:5])
```

الآن يمكنك تضمين نصك الخاص:

```python
import re, numpy as np

# أداة تجزئة نصية بسيطة تحتفط بالنقاط في كلمات مثل u.s.
TOKEN_RE = re.compile(r"[A-Za-z0-9\.\-']+")

def tokenize(text: str):
    return TOKEN_RE.findall(text.lower())

def embed_tokens(tokens, kv: KeyedVectors):
    vecs = [kv[w] for w in tokens if w in kv.key_to_index]
    return np.stack(vecs) if vecs else np.zeros((0, kv.vector_size))

def embed_sentence_avg(text: str, kv: KeyedVectors):
    V = embed_tokens(tokenize(text), kv)
    return V.mean(axis=0) if V.size else np.zeros(kv.vector_size)

# أمثلة
print(embed_sentence_avg("The quick brown fox jumps over the lazy dog.", vectors)[:10])
print(embed_tokens(tokenize("U.S. interest rates rose today."), vectors).shape)  # (عدد_الكلمات, 300)
```

**نصائح**

* `glove.6B.300d.txt` ≈ 1.1 جيجابايت في الذاكرة. إذا كان ذلك ثقيلًا، جرب `100d` بدلاً من ذلك.
* مجموعة 6B **كلها أحرف صغيرة**؛ قم دائمًا بتحويل نصك إلى أحرف صغيرة، أو استخدم مجموعة **840B** الأكبر إذا كنت تحتاج إلى تغطية أوسع (وهي أيضًا غالبًا بدون حالة أحرف في التطبيق العملي).
* الكلمات غير الموجودة في المفردات لا تُرجع أي شيء؛ يمكنك تخطيها أو استخدام طرق احتياطية تعتمد على أجزاء الكلمات.

---

## الخيار ب — دع `torchtext` يقوم بتنزيل وتقديم GloVe لك

هذا يتجنب التنزيل والتحويل اليدوي.

```python
import torch
from torchtext.vocab import GloVe
import re

glove = GloVe(name="6B", dim=300)  # التنزيل التلقائي إلى ~/.vector_cache
stoi = glove.stoi    # كلمة -> فهرس
vecs = glove.vectors # موتر [المفردات, 300]

def get_word_vec(word: str):
    idx = stoi.get(word.lower())
    return vecs[idx] if idx is not None else None

print(get_word_vec("the")[:5])
print(get_word_vec("to")[:5])
print(get_word_vec("U.S.")[:5])     # تصبح None في العديد من البناءات؛ جرب "u.s.":
print(get_word_vec("u.s.")[:5])

# تضمين الجملة (المتوسط)
TOKEN_RE = re.compile(r"[A-Za-z0-9\.\-']+")
def embed_sentence_avg(text: str):
    toks = TOKEN_RE.findall(text.lower())
    xs = [get_word_vec(t) for t in toks]
    xs = [x for x in xs if x is not None]
    return torch.stack(xs, dim=0).mean(0) if xs else torch.zeros(glove.dim)

print(embed_sentence_avg("The quick brown fox...")[:10])
```

---

## ما سألت عنه بخصوص الصفوف المحددة

تلك الصفوف مثل:

```
the  0.418 0.24968 -0.41242 0.1217 ... 0.34527  # إجمالي 300 عدد عشري عائم
to   0.68047 -0.039263 -0.67412 0.056051 ... -0.067549
U.S. 0.3459  0.21513  -0.09982 0.25344 ... 0.024118
```

هي بالضبط ما ستراه في ملفات النص العادي `.txt`: كل سطر هو `رمز` متبوعًا بـ `300` عدد عشري عائم. مع `gensim` أو `torchtext`، لا تحتاج إلى تحليل الأسطر بنفسك — فهي تتولى ذلك وتعطيك إمكانية البحث المباشر عن المتجهات.

---

## الأخطاء الشائعة (والإصلاحات)

* **“KeyError: ‘U.S.’”** → استخدم `u.s.` مع مجموعة 6B، أو اختر مجموعة أكبر بتغطية أفضل، وقم دائمًا بتحويل الأحرف إلى صغيرة قبل البحث.
* **ذاكرة/وقت هائل** → استخدم `100d` أو `200d` بدلاً من `300d`، أو حمّل فقط الكلمات المطلوبة عن طريق فحص الملف وبناء مفردات أصغر.
* **متجهات الجملة/المستند** → قم بحساب المتوسط أو المجموع لمتجهات الكلمات؛ لمتوسط مرجح، جرب أوزان TF-IDF.

إذا أردت، أخبرني عن هدفك المحدد في معالجة النص (تصنيف، تشابه، تجميع، إلخ) وسأرسم لك خط أنابيب بسيطًا من البداية إلى النهاية باستخدام GloVe.