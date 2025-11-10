---
audio: false
generated: true
image: false
lang: ar
layout: post
title: تعزيز مدونة جيكل باستخدام باي تورش
translated: true
type: note
---

### تحسين مدونتك التي تعمل بـ Jekyll باستخدام التعلم الآلي/الذكاء الاصطناعي عبر PyTorch

بما أنك تستخدم مدونة Jekyll (مولد مواقع ثابت)، فإن دمج ميزات التعلم الآلي/الذكاء الاصطناعي مثل نظام التوصيات أو التصنيف يتطلب بعض الإبداع. تقوم Jekyll ببناء HTML ثابت، لذا فإن العناصر الديناميكية (مثل التوصيات الفورية) قد تحتاج إلى JavaScript يعمل على جانب العميل أو حساب مسبق أثناء عملية البناء عبر إضافات Jekyll أو البرامج النصية. لقد ذكرت أنك تريد تجنب واجهات برمجة تطبيقات النماذج اللغوية الكبيرة والتركيز على شبكاتك العصبية الخاصة باستخدام PyTorch — هذا رائع، لأن هذا يبقي كل شيء محليًا وقابلاً للتخصيص. سأقدم أفكارًا عملية، مع التركيز على تنفيذات PyTorch. تفترض هذه الأفكار أن لديك إمكانية الوصول إلى المكتبات الأساسية مثل NumPy (للتلاعب بالبيانات) ويمكنك التعامل مع المعالجة المسبقة للنصوص يدويًا أو باستخدام تجزئة بسيطة (نظرًا لأن المكتبات المتقدمة مثل Hugging Face لم تُذكر في إعدادك، ولكن يمكنك إضافتها محليًا إذا لزم الأمر).

من المحتمل أن تقوم بإنشاء برامج نصية بلغة Python (على سبيل المثال، في الدليل `scripts/`) تعمل أثناء عملية بناء Jekyll (عبر خطاف Makefile أو GitHub Actions في حالة النشر). على سبيل المثال، معالجة منشورات Markdown في `_posts/`، وإنشاء بيانات JSON، وحقنها في موقعك عبر قوالب Liquid.

#### 1. تصنيف المقالات باستخدام مصنف PyTorch
قم بتصنيف المنشورات تلقائيًا (على سبيل المثال، إلى مواضيع مثل "ML"، "Notes"، "Latex") من خلال تدريب شبكة عصبية بسيطة للمصنف. هذا تعلم خاضع للإشراف: ستحتاج إلى وضع تسميات يدويًا لمجموعة فرعية من منشوراتك كبيانات تدريب. إذا لم يكن لديك تسميات، ابدأ بالتجميع غير الخاضع للإشراف (انظر أدناه).

**الخطوات:**
- **إعداد البيانات:** تحليل ملفات Markdown الخاصة بك في `_posts/`. استخراج محتوى النص (تخطي frontmatter). إنشاء مجموعة بيانات: قائمة بأزواج (النص، التسمية). استخدم CSV أو قائمة لحوالي 50-100 مثال موسوم في البداية.
- **المعالجة المسبقة:** تجزئة النص (تقسيم بسيط على المسافات/المسافات البيضاء)، بناء مفردات، التحويل إلى مؤشرات رقمية. استخدم الترميز one-hot أو التضمينات الأساسية.
- **النموذج:** شبكة عصبية انتشارية أمامية أساسية في PyTorch للتصنيف متعدد الفئات.
- **التدريب:** التدريب على جهازك المحلي. استخدم دالة الخسارة cross-entropy ومحسن Adam.
- **التكامل:** تشغيل البرنامج النصي أثناء البناء لتصنيف جميع المنشورات، وإنشاء ملف `categories.json`، واستخدامه في Jeklio لوضع علامات على الصفحات أو إنشاء فهارس للفئات.

**مقتطف كود PyTorch مثال (في برنامج نصي مثل `scripts/categorize_posts.py`):**
```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import os
from collections import Counter

# الخطوة 1: تحميل البيانات والمعالجة المسبقة (مبسط)
def load_posts(posts_dir='_posts'):
    texts = []
    labels = []  # نفترض تسميات يدوية: 0=ML, 1=Notes, إلخ.
    for file in os.listdir(posts_dir):
        if file.endswith('.md'):
            with open(os.path.join(posts_dir, file), 'r') as f:
                content = f.read().split('---')[2].strip()  # تخطي frontmatter
                texts.append(content)
                # عنصر نائب: تحميل التسمية من قاموس أو CSV
                labels.append(0)  # استبدل بالتسميات الفعلية
    return texts, labels

texts, labels = load_posts()
# بناء المفردات (أهم 1000 كلمة)
all_words = ' '.join(texts).lower().split()
vocab = {word: idx for idx, word in enumerate(Counter(all_words).most_common(1000))}
vocab_size = len(vocab)

# تحويل النص إلى متجهات (كيس الكلمات)
def text_to_vec(text):
    vec = np.zeros(vocab_size)
    for word in text.lower().split():
        if word in vocab:
            vec[vocab[word]] += 1
    return vec

X = np.array([text_to_vec(t) for t in texts])
y = torch.tensor(labels, dtype=torch.long)

# الخطوة 2: تعريف النموذج
class Classifier(nn.Module):
    def __init__(self, input_size, num_classes):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, num_classes)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = Classifier(vocab_size, num_classes=3)  # اضبط num_classes

# الخطوة 3: التدريب
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

# الخطوة 4: الاستدلال على منشور جديد
def classify_post(text):
    vec = torch.tensor(text_to_vec(text), dtype=torch.float32).unsqueeze(0)
    with torch.no_grad():
        pred = model(vec).argmax(1).item()
    return pred  # قم بتعيين القيمة مرة أخرى إلى اسم الفئة

# حفظ النموذج: torch.save(model.state_dict(), 'classifier.pth')
# في برنامج البناء: صنف جميع المنشورات واكتب في JSON
```

**التحسينات:** للحصول على دقة أفضل، استخدم التضمينات الكلامية (قم بتدريب طبقة Embedding بسيطة في PyTorch) أو أضف المزيد من الطبقات. إذا لم تكن هناك تسميات، انتقل إلى التجميع (على سبيل المثال، KMeans على التضمينات — انظر القسم التالي). قم بتشغيل هذا البرنامج النصي في ملف Makefile الخاص بك: `jekyll build && python scripts/categorize_posts.py`.

#### 2. نظام التوصيات باستخدام PyTorch Embeddings
قم بالتوصية بمقالات مشابهة للقراء (على سبيل المثال، "قد يعجبك أيضًا..."). استخدم التوصية القائمة على المحتوى: تعلم تضمينات لكل منشور، ثم احسب التشابه (مسافة جيب التمام). لا حاجة لبيانات المستخدم — فقط محتوى المنشور.

**الخطوات:**
- **البيانات:** نفس ما ورد أعلاه — استخراج النص من المنشورات.
- **النموذج:** تدريب autoencoder في PyTorch لضغط النص في تضمينات منخفضة الأبعاد (على سبيل المثال، متجهات 64-dim).
- **التدريب:** قلل خسارة إعادة البناء لتعلم تمثيلات ذات معنى.
- **التوصيات:** لمنشور معين، ابحث عن أقرب الجيران في فضاء التضمين.
- **التكامل:** احسب التضمينات مسبقًا أثناء البناء، وقم بتخزينها في JSON. استخدم JS على الموقع لإظهار التوصيات (أو Liquid للقوائم الثابتة).

**مقتطف كود PyTorch مثال (في `scripts/recommend_posts.py`):**
```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
# إعادة استخدام load_posts و text_to_vec من الأعلى

texts, _ = load_posts()  # تجاهل التسميات
X = np.array([text_to_vec(t) for t in texts])
X_tensor = torch.tensor(X, dtype=torch.float32)

# نموذج Autoencoder
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

# الحصول على التضمينات
with torch.no_grad():
    embeddings = model.encoder(X_tensor).numpy()

# التوصية: للمنشور i، ابحث عن أعلى 3 مشابه
similarities = cosine_similarity(embeddings)
for i in range(len(texts)):
    rec_indices = similarities[i].argsort()[-4:-1][::-1]  # أعلى 3 باستثناء نفسه
    print(f'Recs for post {i}: {rec_indices}')

# حفظ التضمينات في JSON لـ Jekyll
import json
with open('embeddings.json', 'w') as f:
    json.dump({'embeddings': embeddings.tolist(), 'posts': [f'post_{i}' for i in range(len(texts))]}, f)
```

**التحسينات:** استخدم variational autoencoder للحصول على تضمينات أفضل. إذا كان لديك مشاهدات المستخدم (عبر التحليلات)، أضف تصفية تعاونية مع نموذج matrix factorization في PyTorch. جانب العميل: قم بتحميل JSON في JS واحسب التشابه على الطاير للتخصيص.

#### 3. أفكار أخرى باستخدام PyTorch
- **التجميع غير الخاضع للإشراف لوضع العلامات التلقائية:** إذا كانت وضع العلامات شاقة، استخدم التضمينات (من الـ autoencoder أعلاه) + تجميع KMeins لتجميع المنشورات في مواضيع. PyTorch للتضمينات، NumPy/SciPy للتجميع.
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=5)
  clusters = kmeans.fit_predict(embeddings)
  # تعيين علامات بناءً على المجموعات
  ```
  التكامل: إنشاء علامات في frontmatter عبر برنامج نصي.

- **تحسين البحث الدلالي:** تضمين الاستعلامات والمنشورات بشكل مشابه، ثم استخدم تشابه جيب التمام لشريط البحث. احسب تضمينات المنشورات مسبقًا؛ استخدم JS لتضمين الاستعلام (ولكن بما أن PyTorch يعمل بـ Python، قم بتصدير النموذج إلى ONNX للاستدلال عبر ONNX.js، أو حافظ على البحث ثابتًا).

- **تلخيص المنشورات:** تدريب نموذج seq2seq (RNN/LSTM في PyTorch) على بيانات مقترنة (النص الكامل، الملخص اليدوي). هذا صعب بدون مجموعات بيانات كبيرة، ولكن ابدأ صغيرًا بمنشوراتك. استخدم لتوليد مقتطفات.

**نصائح عامة:**
- **القابلية للتوسع:** بالنسبة لمدونة صغيرة، قم بالتدريب على وحدة المعالجة المركزية؛ PyTorch يتعامل مع ذلك بشكل جيد. احفظ النماذج باستخدام `torch.save` وقم بتحميلها للاستدلال.
- **تكامل البناء:** أضف إلى Makefile: `train: python scripts/train_models.py` ثم `build: jekyll build && python scripts/generate_features.py`.
- **القيود:** بدون معالجة اللغة الطبيعية المتقدمة (مثل المحولات transformers)، تكون النتائج أساسية — فكر في إضافة `torchtext` أو تضمينات GloVe اليدوية محليًا. اختبر على أدلة `ml/` أو `notes/` الخاصة بك.
- **النشر:** إذا كنت تستخدم GitHub Pages، فشغل البرامج النصية في CI. بالنسبة للأشياء الديناميكية، فكر في إضافة خادم خفيف الوزن Flask، ولكن هذا ينحرف عن Jekyll الثابت.

إذا شاركت المزيد من التفاصيل (مثل عدد المنشورات، المواضيع)، يمكنني تحسين هذه الأفكار!