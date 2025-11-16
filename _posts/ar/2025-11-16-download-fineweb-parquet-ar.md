---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تنزيل ملفات باركيه محددة من فاين ويب
translated: true
type: note
---

كل ما تريده هو تنزيل واستخدام بعض ملفات parquet من إحدى مجموعات Common Crawl (مثل CC-MAIN-2013-20) بدلاً من مجموعة FineWeb الضخمة البالغة 15 تريليون رمز — هذا أمر معقول تمامًا! إليك أسهل الطرق للقيام بذلك في عام 2025.

### الطريقة 1: التنزيل المباشر باستخدام huggingface_hub (موصى به، الأسرع)
يقوم هذا بتنزيل فقط ملفات parquet التي تريدها بأقصى سرعة (~جيجابايت/ثانية إذا قمت بتمكين hf-transfer).

```bash
# 1. التثبيت/التحديث
pip install -U "huggingface_hub[hf_transfer]"

# 2. تمكين التنزيل السريع (مهم جدًا!)
export HF_HUB_ENABLE_HF_TRANSFER=1   # Linux/macOS
# أو على Windows PowerShell:
# $env:HF_HUB_ENABLE_HF_TRANSFER = "1"

# 3. تنزيل فقط ملفات parquet القليلة التي تريدها
huggingface-cli download HuggingFaceFW/fineweb \
    data/CC-MAIN-2013-20/000_00000.parquet \
    data/CC-MAIN-2013-20/000_00001.parquet \
    data/CC-MAIN-2013-20/000_00002.parquet \
    --repo-type dataset --local-dir fineweb-2013-20
```

هذا كل شيء — لديك الآن ثلاثة ملفات parquet بحجم ~2.15 جيجابايت في المجلد `fineweb-2013-20/`.

### الطريقة 2: سكريبت Python من سطر واحد لتنزيل ملفات محددة
```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="HuggingFaceFW/fineweb",
    repo_type="dataset",
    allow_patterns=[
        "data/CC-MAIN-2013-20/000_00000.parquet",
        "data/CC-MAIN-2013-20/000_00001.parquet",
        # أضف المزيد إذا أردت
    ],
    local_dir="fineweb-2013-20"
)
```

### كيفية قراءة ملفات Parquet محليًا
```python
import pandas as pd
# أو استخدم pyarrow للسرعة + ذاكرة أقل
import pyarrow.parquet as pq
import pyarrow.dataset as ds

# أسرع طريقة (يدفق دون تحميل كل شيء في ذاكرة الوصول العشوائي)
dataset = ds.dataset("fineweb-2013-20/data/CC-MAIN-2013-20/", format="parquet")

for batch in dataset.to_batches(batch_size=1024):
    df = batch.to_pandas()
    for text in df["text"]:
        # افعل ما تريد: tokenize، فلتر، اكتب إلى jsonl، إلخ.
        print(text[:200])  # مثال
```

أو ببساطة باستخدام pandas (جيد لبضعة ملفات):
```python
df = pd.read_parquet("fineweb-2013-20/data/CC-MAIN-2013-20/000_00000.parquet")
print(df.columns)  # ['text', 'id', 'dump', 'url', 'date', 'file_path', 'language', 'language_score', 'token_count']
print(df.iloc[0]["text"])
```

### إحصائيات سريعة لـ CC-MAIN-2013-20
*   ~207 ملف parquet × ~2.15 جيجابايت ≈ 422 جيجابايت إجمالاً
*   ~44 مليار رمز (حجم جيد للتجارب الصغيرة والمتوسطة)
*   تم تنظيفها وإزالة التكرارات وترشيحها مسبقًا بواسطة Hugging Face

هذا كل ما تحتاجه. ما عليك سوى اختيار أي عدد تريده من ملفات `_0000XX.parquet` (يتم خلطها عشوائيًا)، وتنزيل تلك الملفات فقط، والبدء في التدريب أو التصفية على الفور.