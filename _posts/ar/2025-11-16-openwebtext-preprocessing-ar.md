---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: سكربت معالجة مجموعة بيانات أوبن ويب تكست
translated: true
type: note
---

### نظرة عامة
هذا النص البرمجي بلغة Python يعالج ملف نصي كبير يحتوي على مجموعة بيانات OpenWebText (مجموعة نصوص مجمعة من الويب مشابهة لما يُستخدم لتدريب نماذج مثل GPT-2). الهدف هو:
- تقسيم النص الخام إلى "مستندات" (قطع نصية) يمكن إدارتها.
- إنشاء كائن `Dataset` من Hugging Face لسهولة التعامل.
- تحويل النص إلى رموز باستخدام برنامج الترميز GPT-2 Byte Pair Encoding (BPE) من TikToken (بتجاهل الرموز الخاصة وإضافة علامة نهاية النص).
- تقسيم مجموعة البيانات إلى مجموعتي تدريب (%99.95) وتحقق (%0.05).
- حفظ البيانات المرمزة كملفات ثنائية مضغوطة (`train.bin` و `val.bin`) باستخدام مصفوفات الذاكرة المعنونة (memory-mapped arrays) من NumPy. تخزن هذه الملفات تسلسلات لمعرفات الرموز (كأعداد صحيحة 16-بت) لتحميل فعال أثناء تدريب تعلم الآلة.

تم تصميم النص البرمجي للكفاءة على الأنظمة متعددة النوى، باستخدام المعالجة المتعددة (multiprocessing) لتحويل النص إلى رموز. وهو مستلهم من وحدة تحميل البيانات من مستودع Flash Attention (المشار إليه في الكود)، والتي تتعامل مع معالجة أولية مماثلة لتدريب نماذج اللغة. ملاحظة: مجموعة OpenWebText ضخمة (~40 جيجابايت غير مضغوطة)، لكن هذا النص البرمجي يفترض وجود ملف محلي مسبق التحميل باسم `openwebtext.txt`. الملفات الناتجة أصغر بكثير: `train.bin` ~17 جيجابايت (9 مليار رمز) و `val.bin` ~8.5 ميجابايت (4 مليون رمز).

يطبع النص البرمجي إعدادات الوكيل (proxy) في البداية (على الأرجح لتصحيح مشاكل الشبكة أثناء أي عمليات تنزيل ضمنية، رغم عدم وجود أي منها هنا بشكل صريح). ويستخدم 8 عمليات عاملة (worker processes) لتحويل النص إلى رموز افتراضيًا.

### تفصيل خطوة بخطوة

#### 1. الاستيراد والإعداد الأولي
```python
import os
import tarfile
from tqdm import tqdm
import numpy as np
import tiktoken
from huggingface_hub import hf_hub_download
from datasets import load_dataset # huggingface datasets
import datasets

print("HTTP_PROXY:", os.getenv("HTTP_PROXY"))
print("HTTPS_PROXY:", os.getenv("HTTPS_PROXY"))

# number of workers in .map() call
# good number to use is ~order number of cpu cores // 2
num_proc = 8

# number of workers in load_dataset() call
# best number might be different from num_proc above as it also depends on NW speed.
# it is better than 1 usually though
num_proc_load_dataset = num_proc

enc = tiktoken.get_encoding("gpt2")

datasets.logging.set_verbosity_info()
```
- **الغرض**: يستورد مكتبات للتعامل مع الملفات (`os`, `tarfile`)، أشرطة التقدم (`tqdm`)، العمليات العددية (`numpy`)، تحويل النص إلى رموز (`tiktoken`)، وأدوات Hugging Face (`huggingface_hub`, `datasets`).
- **طباعة إعدادات الوكيل**: يسجل متغيرات البيئة لوكلاء HTTP/HTTPS، مفيد إذا واجه النص البرمجي قيودًا على الشبكة (مثل تنزيل نماذج برنامج الترميز، رغم أن TikToken يتعامل مع هذا داخليًا).
- **العمال**: يضبط `num_proc=8` للمعالجة المتوازية في تحويل النص إلى رموز (تقريبًا نصف نوى المعالج للتوازن). `num_proc_load_dataset` يطابقه لكنه غير مستخدم هنا (متبقي من الكود الأصلي المستلهم، الذي يحمل البيانات من Hugging Face).
- **المرمِّز**: يحمل برنامج الترميز GPT-2 BPE (`enc`). يحول هذا النص إلى معرفات رموز عددية (مدى 0–50,256).
- **التسجيل**: يضبط تسجيل Hugging Face datasets إلى مستوى "info" لإخراج مفصل أثناء المعالجة.

حارس `if __name__ == '__main__':` يضمن أن المنطق الرئيسي يعمل فقط عند تنفيذ النص البرمجي مباشرة (وليس عند استيراده).

#### 2. قراءة وتقسيم ملف النص
```python
if __name__ == '__main__':
    # Read the local openwebtext.txt file
    txt_file = os.path.join(os.path.dirname(__file__), 'openwebtext.txt')
    print(f"Reading from local file: {txt_file}")

    # Read the text content
    texts = []
    with open(txt_file, 'r', encoding='utf-8', errors='ignore') as f:
        # Read the entire file
        full_text = f.read().strip()

        # Try to split into documents by double newlines first
        documents = full_text.split('\n\n')

        # If we only got one document, split by single newlines
        if len(documents) <= 1:
            documents = full_text.split('\n')

        # If we still only have one document, split by period followed by space
        if len(documents) <= 1:
            # Split on period followed by space, then join back sentences
            sentences = full_text.split('. ')
            # Group sentences into chunks of ~100 sentences per document
            chunk_size = 100
            for i in range(0, len(sentences), chunk_size):
                chunk = '. '.join(sentences[i:i+chunk_size])
                if chunk.strip():
                    texts.append(chunk.strip() + '.')
        else:
            # Process documents from double/single newline splits
            for doc in documents:
                doc = doc.strip()
                if doc:  # Only add non-empty documents
                    texts.append(doc)

        print(f"Created {len(texts)} documents from the text file")
```
- **قراءة الملف**: يفتح `openwebtext.txt` (يفترض وجوده في نفس دليل النص البرمجي) بوضع UTF-8، متجاهلاً أخطاء الترميز. يقرأ المحتوى كاملاً في `full_text` ويقلم المسافات البيضاء.
- **منطق التقسيم**: يحاول تقسيم النص إلى "مستندات" (قطع منطقية مثل الفقرات أو المقالات):
  - **الأولي**: التقسيم بمسافتين جديدتين (`\n\n`)، شائع لفصل المستندات في المجموعات النصية.
  - **البديل 1**: إذا أنتج ذلك ≤1 قطعة (مثل عدم وجود مسافتين جديدتين)، يقسم بمسافة جديدة واحدة (`\n`) للنص القائم على الأسطر.
  - **البديل 2**: إذا كان لا يزال ≤1 قطعة (مثل كتلة نصية واحدة)، يقسم إلى جمل بواسطة `. ` (نقطة + مسافة)، ثم يجمع كل 100 جملة في قطعة "مستند". هذا يمنع وجود مدخلات طويلة جدًا. يضيف نقطة في نهاية كل قطعة للاكتمال.
- **الإخراج**: يخزن المستندات غير الفارغة والمقلمة في قائمة `texts`. يطبع العدد الإجمالي الذي تم إنشاؤه (مثل 10 آلاف مثال لمجموعة فرعية).
- **لماذا بهذه الطريقة؟** مجموعة OpenWebText هي سلسلة من صفحات الويب، لذا فإن التقسيم ينشئ أمثلة تدريب ليست مجرد تفريغ خام. هذا يحاكي كيفية معالجة مجموعات البيانات مثل BookCorpus.

#### 3. إنشاء وتقسيم مجموعة البيانات
```python
    # Create dataset from texts
    dataset = datasets.Dataset.from_dict({'text': texts})

    # create train/val split from the 10k examples
    split_dataset = dataset.train_test_split(test_size=0.0005, seed=2357, shuffle=True)
    split_dataset['val'] = split_dataset.pop('test') # rename the test split to val
```
- **إنشاء مجموعة البيانات**: يغلف قائمة `texts` في `Dataset` من Hugging Face بعمود واحد `'text'`. هذا يمكن من عمليات متوازية فعالة مثل التعيين (mapping).
- **التقسيم**: يستخدم `train_test_split` للتقسيم إلى مجموعتي تدريب (%99.95) واختبار (%0.05). حجم مجموعة التحقق الصغير مقصود لمجموعات البيانات الضخمة — كافٍ للتقييم دون إهدار للحوسبة.
  - `test_size=0.0005`: %0.05 للتحقق (مثل ~50 مثال من 100 ألف).
  - `seed=2357`: بذرة عشوائية ثابتة لإمكانية إعادة الإنتاج.
  - `shuffle=True**: يخلط قبل التقسيم.
- **إعادة التسمية**: يزيل `'test'` ويعيد تسميته إلى `'val'`. الآن `split_dataset` هو قاموس بمفاتيح `'train'` و `'val'`، كل منهما كائن `Dataset`.

#### 4. دالة تحويل النص إلى رموز
```python
    # we now want to tokenize the dataset. first define the encoding function (gpt2 bpe)
    def process(example):
        ids = enc.encode_ordinary(example['text']) # encode_ordinary ignores any special tokens
        ids.append(enc.eot_token) # add the end of text token, e.g. 50256 for gpt2 bpe
        # note: I think eot should be prepended not appended... hmm. it's called "eot" though...
        out = {'ids': ids, 'len': len(ids)}
        return out
```
- **الغرض**: يحول النص إلى معرفات رموز لإدخال النموذج.
- **`encode_ordinary`**: يحول سلسلة النص إلى قائمة أعداد صحيحة (مفردات GPT-2). يتجاهل أي رموز غير قياسية في النص.
- **إضافة EOT**: يضيف رمز نهاية النص (ID 50256 لـ GPT-2) في النهاية. يشير هذا إلى حدود التسلسل أثناء التدريب. (تذكر الملاحظة نقاشًا محتملاً حول الإضافة في البداية مقابل النهاية، لكن الإضافة في النهاية شائعة في إعدادات نماذج LM السببية مثل GPT).
- **الإخراج**: يُرجع قاموسًا يحتوي على `'ids'` (قائمة معرفات الرموز) و `'len'` (طول التسلسل، للتجميع لاحقًا).

#### 5. تطبيق تحويل النص إلى رموز
```python
    # tokenize the dataset
    tokenized = split_dataset.map(
        process,
        remove_columns=['text'],
        desc="tokenizing the splits",
        num_proc=num_proc,
    )
```
- **التعيين**: يطبق `process` على كل مثال في مجموعتي التدريب/التحقق باستخدام عمال متوازيين (`num_proc=8`).
- **`remove_columns=['text']`**: يحذف النص الأصلي لتوفير الذاكرة (نحتاج فقط إلى الرموز الآن).
- **التقدم**: يظهر شريط تقدم عبر `desc`. يمكن أن تستغرق هذه الخطوة وقتًا لمجموعات البيانات الكبيرة بسبب الترميز.

#### 6. حفظ البيانات المرمزة في ملفات ثنائية
```python
    # concatenate all the ids in each dataset into one large file we can use for training
    for split, dset in tokenized.items():
        arr_len = np.sum(dset['len'], dtype=np.uint64)
        filename = os.path.join(os.path.dirname(__file__), f'{split}.bin')
        dtype = np.uint16 # (can do since enc.max_token_value == 50256 is < 2**16)
        arr = np.memmap(filename, dtype=dtype, mode='w+', shape=(arr_len,))

        # Use adaptive batch size based on dataset size
        total_batches = min(1024, len(dset))
        if total_batches < 1024:
            print(f"Using {total_batches} batches for {split} dataset (size: {len(dset)})")

        idx = 0
        for batch_idx in tqdm(range(total_batches), desc=f'writing {filename}'):
            # Only process if this batch index is valid for the dataset size
            if batch_idx < len(dset):
                # Batch together samples for faster write
                batch = dset.shard(num_shards=total_batches, index=batch_idx, contiguous=True).with_format('numpy')
                arr_batch = np.concatenate(batch['ids'])
                # Write into mmap
                arr[idx : idx + len(arr_batch)] = arr_batch
                idx += len(arr_batch)
        arr.flush()
```
- **حلقة على المجموعات**: لكل من `'train'` و `'val'`، يحسب العدد الإجمالي للرموز (`arr_len`) بجمع حقول `'len'`.
- **مصفوفة الذاكرة المعنونة**: ينشئ ملف memmap من NumPy (`train.bin` أو `val.bin`) كمصفوفة قابلة للكتابة من أعداد صحيحة uint16 (تناسب قيمة الرمز القصوى لـ GPT-2 وهي 50,256؛ توفر ~50% مساحة مقارنة بـ int32). الشكل أحادي البعد: `(total_tokens,)`.
- **التجميع للكفاءة**: يقسم مجموعة البيانات إلى ما يصل إلى 1024 شريحة (`total_batches`) لتجنب تحميل كل شيء في الذاكرة العشوائية مرة واحدة. لمجموعات البيانات الصغيرة (<1024 مثال)، يستخدم العدد الدقيق.
  - **`shard`**: يقسم مجموعة البيانات إلى دفعات متتالية (لا يوجد خلط هنا).
  - **`with_format('numpy')`**: يحول الدفعة إلى مصفوفات NumPy للتسلسل السريع.
- **الكتابة**: يسلسل معرفات الرموز من كل دفعة وينسخها بشكل تسلسلي في مصفوفة memmap بدءًا من `idx`. يتتبع التقدم بـ `tqdm`.
- **`flush()`**: يضمن كتابة جميع البيانات إلى القرص.
- **لماذا ثنائي/memmap؟** هذه الملفات ضخمة لكن يمكن دفقها. أثناء التدريب، يمكنك تحميلها باستخدام `np.memmap('train.bin', dtype=np.uint16, mode='r')` دون تحميل كل شيء في الذاكرة.

#### 7. ملاحظات على الإخراج والاستخدام
```python
    # train.bin is ~17GB, val.bin ~8.5MB
    # train has ~9B tokens (9,035,582,198)
    # val has ~4M tokens (4,434,897)

    # to read the bin files later, e.g. with numpy:
    # m = np.memmap('train.bin', dtype=np.uint16, mode='r')
```
- هذه أحجام مثال لمجموعة OpenWebText الكاملة (قد يختلف ملفك المحلي).
- **نصيحة القراءة**: استخدم memmap للوصول للقراءة فقط. في حلقات التدريب، يمكنك أخذ عينات من مؤشرات بداية عشوائية وقراءة تسلسلات ذات طول ثابت (مثل 1024 رمز) من المصفوفة المسطحة.

### مشاكل محتملة وملاحظات
- **استخدام الذاكرة**: قراءة ملف `openwebtext.txt` الكامل في الذاكرة العشوائية قد يفشل للملفات الكبيرة جدًا (40+ جيجابايت). فكر في القراءة المتدفقة إذا لزم الأمر.
- **موضع EOT**: تسأل الملاحظة عن الإضافة في النهاية مقابل البداية؛ عمليًا، الإضافة في النهاية تعمل للنماذج الانحدارية (تشير إلى النهاية بعد المحتوى).
- **التخصيص**: يفترض ملف محلي؛ الكود الأصلي المستلهم يحمل من Hugging Face، لكن هذه النسخة تقرأ محليًا (أسرع، لا حاجة لمصادقة).
- **التبعيات**: يتطلب `tiktoken`, `datasets`, `numpy`, `tqdm`. قم بالتثبيت عبر pip إذا كانت مفقودة.
- **القابلية للتوسع**: لمجموعة OpenWebText الحقيقية، شغّل على جهاز بذاكرة عشوائية 64+ جيجابايت وتخزين سريع (SSD). تقسيم 10 آلاف مثال يشير إلى أن هذا قد يكون لمجموعة فرعية.

يحول هذا النص البرمجي النص الخام إلى تنسيق جاهز للتدريب، مُحسَّن لنماذج اللغة مثل GPT. إذا كانت لديك أسئلة حول تعديله (مثل برنامج ترميز مختلف أو حجم قطعة مختلف)، دعني أعلم!