---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: نظرة عامة على مجموعة بيانات FineWeb وكيفية استخدامها
translated: true
type: note
---

### نظرة عامة على مجموعة بيانات FineWeb
مجموعة بيانات FineWeb هي مجموعة نصوص ويب إنجليزية واسعة النطاق وعالية الجودة تم تطويرها من قبل Hugging Face، ومستمدة من لقطات CommonCrawl (2013–2024). تحتوي على أكثر من 15 تريليون رمز بعد التصفية وإزالة التكرارات، مما يجعلها مناسبة للتدريب المسبق لنماذج اللغة الكبيرة (LLMs). تم إصدارها بموجب ترخيص Open Data Commons Attribution License (ODC-By) وهي مستضافة على Hugging Face Datasets.

هناك متغيرات مثل FineWeb-Edu (مصفاة للمحتوى التعليمي) و FineWeb2 (امتداد متعدد اللغات). لتدريب نماذج اللغة الكبيرة، فإن النواة `HuggingFaceFW/fineweb` هي نقطة البداية.

### المتطلبات الأساسية
- **بيئة Python**: Python 3.8+ مع مكتبة `datasets` من Hugging Face.
- **التخزين**: مجموعة البيانات كاملة ضخمة الحجم (~16 تيرابايت مضغوطة). استخدم الوضع المتدفق للمعالجة الفورية أثناء التدريب.
- **اختياري للسرعة**: قم بتثبيت `huggingface_hub` مع دعم HF Transfer:  
  ```
  pip install huggingface_hub[hf_transfer]
  ```
  ثم عيّن متغير البيئة:  
  ```
  export HF_HUB_ENABLE_HF_TRANSFER=1
  ```
- **حساب Hugging Face**: اختياري ولكنه موصى به للوصول المقيد أو التنزيلات الأسرع (أنشئ حسابًا مجانيًا وسجل الدخول عبر `huggingface-cli login`).

### كيفية تحميل مجموعة البيانات
استخدم مكتبة `datasets` للوصول إليها مباشرة. إليك دليل خطوة بخطوة مع أمثلة على الكود.

#### 1. تثبيت التبعيات
```bash
pip install datasets
```

#### 2. تحميل مجموعة البيانات الكاملة (الوضع المتدفق للتدريب)
يتجنب الوضع المتدفق تنزيل مجموعة البيانات بالكامل مقدمًا — مثالي للتدريب على سعة تخزين محدودة. يقوم بإرجاع البيانات على شكل دفعات.

```python
from datasets import load_dataset

# تحميل مجموعة بيانات FineWeb الكاملة في الوضع المتدفق
dataset = load_dataset("HuggingFaceFW/fineweb", split="train", streaming=True)

# مثال: التكرار على الأمثلة القليلة الأولى
for example in dataset.take(5):
    print(example)  # كل مثال يحتوي على حقول مثل 'text', 'url', 'date'، إلخ.
```

- **التقسيمات**: في المقام الأول `train` (جميع البيانات). يتم توفير تفريغات CommonCrawl الفردية كتكوينات مثل `CC-MAIN-2015-11` (يمكن تحميلها عبر `load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2015-11", split="train")`).
- **تنسيق البيانات**: ملفات Parquet تحتوي على أعمدة تشمل `text` (المحتوى المنظف)، `url`، `date`، `quality_score`، إلخ. النص جاهز للتجزئة.

#### 3. تحميل مجموعة فرعية أو تكوين محدد
لأغراض الاختبار أو التدريب على نطاق أصغر:
```python
# تحميل تفريغ CommonCrawl محدد (مثلاً، بيانات 2023)
dataset = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2023-50", split="train")

# أو تحميل المجموعة الفرعية التعليمية (FineWeb-Edu، ~0.5 تريليون رمز)
edu_dataset = load_dataset("HuggingFaceFW/fineweb-edu", split="train", streaming=True)
```

#### 4. التكامل مع خطوط أنابيب التدريب
لتدريب نماذج اللغة الكبيرة (مثلاً، مع Transformers أو حلقات مخصصة)، استخدم المكرر المتدفق مباشرة في محمل البيانات الخاص بك:
```python
from transformers import DataCollatorForLanguageModeling, Trainer, TrainingArguments

# بافتراض أن لديك أداة تجزئة ونموذج
tokenizer = ...  # مثلاً، AutoTokenizer.from_pretrained("gpt2")

def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, max_length=512)

# إجراء التجزئة على الفور (في دالة map مع batched=True للكفاءة)
tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=dataset.column_names)

# المتابعة إلى Trainer أو حلقة مخصصة
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
# ... (إعداد Trainer مع tokenized_dataset)
```

- **نصيحة للكفاءة**: قم بالمعالجة على شكل دفعات باستخدام `batched=True` في `.map()`. للتدريب الموزع، استخدم Hugging Face Accelerate.

#### 5. تنزيل مجموعة البيانات الكاملة (غير متدفق)
إذا كنت بحاجة إلى تخزين محلي (غير موصى به للحجم الكامل):
```python
dataset = load_dataset("HuggingFaceFW/fineweb", split="train")  # يقوم بالتنزيل إلى ~/.cache/huggingface/datasets
```
استخدم `dataset.save_to_disk("/path/to/save")` بعد ذلك.

### نصائح إضافية للتدريب
- **إزالة التكرارات**: تمت بالفعل إزالة التكرارات من FineWeb، ولكن تحقق من البيانات الوصفية مثل `minhash_cluster_size` للزيادة العشوائية للعينة إذا لزم الأمر.
- **تصفية الجودة**: استخدم `quality_score` المدمج (مع عتبة >0.5) لأخذ عينات فرعية عالية الجودة.
- **المتغيرات**:
  - **FineWeb-Edu**: للتدريب المركّز على المحتوى التعليمي. قم بالتحميل كما هو مذكور أعلاه.
  - **FineWeb2**: للبيانات متعددة اللغات (1000+ لغة). قم بالتحميل عبر `load_dataset("HuggingFaceFW/fineweb-2", name="eng_Latn", split="train", streaming=True)`.
- **التقييم**: تقدم Hugging Face نماذج اختزال ومعايير تقييمية؛ قم بتدريب نماذج صغيرة (مثلاً، 1.8 مليار معامل) على مجموعات فرعية للمقارنة.
- **الموارد**: تفاصيل كاملة في [ورقة البحث](https://arxiv.org/abs/2402.06645). الكود الخاص بالتصفية المخصصة موجود على [GitHub](https://github.com/huggingface/fineweb).

للحصول على المساعدة في المشكلات، راجع [وثائق Hugging Face Datasets](https://huggingface.co/docs/datasets/loading). إذا كنت تستخدم إطار عمل محدد (مثلاً، PyTorch Lightning)، قم بتكييف المكرر وفقًا لذلك.