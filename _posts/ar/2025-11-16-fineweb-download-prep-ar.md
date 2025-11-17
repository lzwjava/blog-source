---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تنزيل وإعداد بيانات FineWeb
translated: true
type: note
---

### تنزيل ملف Parquet

الرابط الذي قدمته يشير إلى ملف Parquet محدد من مجموعة بيانات FineWeb (مجموعة فرعية مُنقَّحة من بيانات CommonCrawl). يحتوي هذا الملف (`000_00000.parquet` من إصدار `CC-MAIN-2013-20`) على حوالي مليون صف من النصوص الشبكية الإنجليزية، ويشتمل كل صف على عمود `text` تمت معالجته مسبقًا بالفعل لتدريب نماذج اللغة (تمت إزالة HTML، وإزالة التكرارات، والتصفية حسب الجودة باستخدام أدوات مثل Trafilatura).

لتنزيله:
- استخدم واجهة سطر أوامر Hugging Face: `huggingface-cli download HuggingFaceFW/fineweb data/CC-MAIN-2013-20/000_00000.parquet --local-dir ./fineweb_data`
- أو عبر Python باستخدام `huggingface_hub`:
  ```python
  from huggingface_hub import hf_hub_download

  file_path = hf_hub_download(
      repo_id="HuggingFaceFW/fineweb",
      filename="data/CC-MAIN-2013-20/000_00000.parquet",
      local_dir="./fineweb_data"
  )
  print(f"Downloaded to: {file_path}")
  ```
هذا يحفظ الملف الذي حجمه ~500 ميغابايت محليًا (مثال: `./fineweb_data/data/CC-MAIN-2013-20/000_00000.parquet`).

للحصول على الإصدار الكامل (مئات الملفات)، استخدم `snapshot_download` كما هو موضح في وثائق مجموعة البيانات، لكن ابدأ بهذا الملف الفردي للاختبار.

### استخراج النص

عمود `text` في FineWeb هو نص عادي جاهز للتدريب—لا حاجة لتحليل HTML أو HTML خام. استخدم `pandas` أو `pyarrow` لتحميله بكفاءة. إليك الطريقة:

1. **تثبيت التبعيات** (إذا لزم الأمر): `pip install pandas pyarrow datasets` (بافتراض أن لديهم إعداد NanoGPT).

2. **تحميل ملف Parquet واستخراج النص**:
   ```python
   import pandas as pd
   import os

   # المسار إلى الملف الذي تم تنزيله
   parquet_path = "./fineweb_data/data/CC-MAIN-2013-20/000_00000.parquet"

   # تحميل ملف Parquet (فعال للملفات الكبيرة)
   df = pd.read_parquet(parquet_path, columns=['text'])  # تحميل عمود النص فقط لتوفير الذاكرة

   # استخراج كل النصوص إلى قائمة (أو التكرار إذا كانت الذاكرة محدودة)
   texts = df['text'].tolist()  # قائمة تحتوي على ~1 مليون سلسلة نصية

   # اختياري: تنظيف أساسي (FineWeb نظيف بالفعل، لكن يمكن تطبيع المسافات البيضاء)
   import re
   def clean_text(text):
       if pd.isna(text):  # تخطي القيم الفارغة (نادرة في FineWeb)
           return ''
       text = re.sub(r'\s+', ' ', text.strip())  # ضغط المسافات البيضاء
       return text if len(text) > 10 else ''  # تصفية النصوص القصيرة جدًا

   cleaned_texts = [clean_text(t) for t in texts if t]  # تطبيق التصفية

   print(f"Extracted {len(cleaned_texts)} text samples")
   print("Sample:", cleaned_texts[0][:200] + "...")  # معاينة النص الأول
   ```

   - **نصيحة الذاكرة**: يحتوي هذا الملف على ~1 مليون صف، كل نص ~1-5 ألف حرف. على جهاز بذاكرة وصول عشوائي 16 جيجابايت، يتم التحميل بشكل جيد. للإصدارات الأكبر، استخدم `pyarrow` للقراءة المجزأة:
     ```python
     import pyarrow.parquet as pq

     table = pq.read_table(parquet_path, columns=['text'])
     texts = table['text'].to_pylist()
     ```

   - **بديل البث** (لا حاجة للتنزيل الكامل): استخدم مكتبة `datasets` للتكرار دون تحميل كل شيء:
     ```python
     from datasets import load_dataset

     # تحميل إصدار محدد في وضع البث
     dataset = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2013-20", split="train", streaming=True)

     texts = []
     for i, sample in enumerate(dataset):
         if i >= 100000:  # تحديد للاختبار
             break
         texts.append(sample['text'])

     # التنظيف كما ورد أعلاه
     ```

### التحضير لتدريب NanoGPT

يتوقع NanoGPT ملف نصي واحد (مثال: `input.txt`) يحتوي على مستندات مترابطة مفصولة برمز خاص (مثل `"<|endoftext|>"`). إليك كيفية تنسيق النص المستخرج:

```python
# بعد استخراج cleaned_texts كما ورد أعلاه
with open('input.txt', 'w', encoding='utf-8') as f:
    for text in cleaned_texts:
        f.write(text + "\n<|endoftext|>\n")  # الفاصل الافتراضي لـ NanoGPT

print("Saved to input.txt – ready for NanoGPT!")
```

- **لماذا هذا التنسيق؟** سيقوم برنامج `data.py` التابع لـ NanoGPT بقراءة `input.txt`، وتشفيره باستخدام أداة الترميز الخاصة بك (مثال: GPT-2)، وإنشاء تقسيمات تدريب/تحقق. ينتهي كل مستند بـ `"<|endoftext|>"` لتجنب تداخل السياق بين المستندات.
- **التخصيص**:
  - التصفية حسب الطول: أضف `if 100 < len(text.split()) < 10000:` قبل الكتابة للاحتفاظ بالمستندات متوسطة الحجم.
  - مجموعة فرعية للاختبار: استخدم `cleaned_texts[:10000]` لتشغيل سريع بعينة 10 آلاف.
  - أمر التدريب: بمجرد أن يصبح `input.txt` جاهزًا، شغِّل `python train.py` في NanoGPT (اضبط `--dataset=input.txt` إذا لزم الأمر).

يمنحك هذا الملف الفردي ~5-10 مليار رمز—ممتاز للضبط الدقيق. للمزيد، قم بتنزيل ملفات Parquet إضافية ووصلها. إذا واجهت مشاكل في الذاكرة أو تحتاج مساعدة في تكوين NanoGPT، شارك التفاصيل!

**المرجع**: [بطاقة مجموعة بيانات FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb)