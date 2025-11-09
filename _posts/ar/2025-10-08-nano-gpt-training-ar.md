---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تدريب مجموعات البيانات المخصصة باستخدام نانو جي بي تي
translated: true
type: note
---

### إعداد وتدريب مجموعة بيانات نصية مخصصة باستخدام nanoGPT

تم تصميم nanoGPT ليكون سهل التدريب على البيانات النصية، بما في ذلك مجموعات البيانات المخصصة. تتضمن العملية تحضير النص الخاص بك إلى ملفات ثنائية للرموز (tokens)، وضبط معاملات التدريب، وتشغيل سكريبت التدريب. أدناه، سأوضح الخطوات بناءً على الأمثلة الموجودة في المستودع (مثل Shakespeare أو OpenWebText). ستحتاج إلى Python 3.8+ ووحدة معالجة رسومية (GPU) للتدريب الكفء (وحدة المعالجة المركزية تعمل ولكنها أبطأ).

#### 1. تثبيت التبعيات
أولاً، قم بإعداد البيئة:
```
pip install torch numpy transformers datasets tiktoken wandb tqdm
```
- `torch`: لـ PyTorch (قم بتثبيتها مع CUDA إذا كنت تستخدم GPU: مثلاً `pip install torch --index-url https://download.pytorch.org/whl/cu118`).
- الباقي يتعامل مع توليد الرموز (tokenization)، تحميل البيانات، والتسجيل.

#### 2. إعداد مجموعة البيانات المخصصة الخاصة بك
يتوقع nanoGPT بياناتك كملفات ثنائية (`train.bin` و `val.bin`) تحتوي على أعداد صحيحة ممثلة للرموز. ستحتاج إلى كتابة سكريبت إعداد بسيط لمعالجة النص الخام الخاص بك.

- **ضع ملف النص الخاص بك**: ضع النص الخام الخاص بك (مثلاً `input.txt`) في مجلد جديد تحت `data/`، مثل `data/my_dataset/`.

- **أنشئ سكريبت إعداد**: انسخ وقم بتعديل مثال من المستودع (مثلاً `data/shakespeare_char/prepare.py` للمستوى الحرفي أو `data/openwebtext/prepare.py` لمستوى رموز GPT-2 BPE).

  **مثال للتشفير على مستوى الحرف** (بسيط لمجموعات البيانات الصغيرة؛ يعامل كل حرف كرمز):
  ```python
  # احفظ كـ data/my_dataset/prepare.py
  import os
  import requests
  import numpy as np
  from torch.utils.data import Dataset, random_split

  # قم بتحميل النص الخاص بك (استبدل بمسار ملفك)
  with open('data/my_dataset/input.txt', 'r', encoding='utf-8') as f:
      text = f.read()

  # قم بتشفير النص كحروف
  chars = sorted(list(set(text)))
  vocab_size = len(chars)
  stoi = {ch: i for i, ch in enumerate(chars)}
  itos = {i: ch for i, ch in enumerate(chars)}
  def encode(s): return [stoi[c] for c in s]
  def decode(l): return ''.join([itos[i] for i in l])

  # قم بتحويل النص كله إلى رموز
  data = torch.tensor(encode(text), dtype=torch.long)

  # قسم إلى بيانات تدريب/تحقق (90/10)
  n = int(0.9 * len(data))
  train_data = data[:n]
  val_data = data[n:]

  # احفظ كملفات .bin
  train_data = train_data.numpy()
  val_data = val_data.numpy()
  train_data.tofile('data/my_dataset/train.bin')
  val_data.tofile('data/my_dataset/val.bin')

  # اطبع الإحصائيات
  print(f"Length of dataset in characters: {len(data)}")
  print(f"Vocab size: {vocab_size}")
  ```
  قم بتشغيله:
  ```
  python data/my_dataset/prepare.py
  ```
  هذا ينشئ `train.bin` و `val.bin`.

- **لتشفير GPT-2 BPE** (أفضل لمجموعات البيانات الأكبر حجمًا؛ يستخدم وحدات فرعية للكلمات):
  قم بتعديل `data/openwebtext/prepare.py`. ستحتاج إلى تثبيت `tiktoken` (موجود بالفعل في التبعيات) والتعامل مع النص الخاص بك بطريقة مشابهة، ولكن استخدم `tiktoken.get_encoding("gpt2").encode()` بدلاً من التشفير الحرفي. قسم النص الخاص بك إلى أجزاء تدريب/تحقق (مثلاً 90/10)، ثم احفظها كمصفوفات NumPy في ملفات `.bin`.

- **نصائح**:
  - حافظ على مجموعة بياناتك نظيفة (مثلاً، أزل الأحرف الخاصة إذا لزم الأمر).
  - للملفات كبيرة الحجم جدًا، قم بالمعالجة على دفعات لتجنب مشاكل الذاكرة.
  - حجم المفردات: ~65 للحروف (Shakespeare)؛ ~50k لـ BPE.

#### 3. ضبط التدريب
أنشئ ملف ضبط عن طريق نسخ مثال (مثلاً `config/train_shakespeare_char.py`) إلى `config/train_my_dataset.py` وقم بتعديله.

معاملات رئيسية للتعديل:
```python
# مقتطف مثال لملف الضبط
out_dir = 'out-my_dataset'  # مجلد الإخراج لنقاط التفتيش
dataset = 'my_dataset'      # يطابق اسم مجلد البيانات الخاص بك
batch_size = 64             # اضبط بناءً على ذاكرة GPU (مثلاً 12 لـ GPU صغير)
block_size = 256            # طول السياق (عدد الرموز لكل مثال)
n_layer = 6                 # طبقات المحول (Transformer)
n_head = 6                  # رؤوس الانتباه (Attention)
n_embd = 384                # بُعد التضمين (Embedding)
max_iters = 5000            # خطوات التدريب
lr = 6e-4                   # معدل التعلم
dropout = 0.2               # معدل الإسقاط (Dropout)
init_from = 'scratch'       # 'scratch' لنموذج جديد؛ 'gpt2' لتحميل نموذج مدرب مسبقًا
```
- للضبط الدقيق (البدء من GPT-2 المدرب مسبقًا): عيّن `init_from = 'gpt2'` (أو 'gpt2-medium').
- لـ Apple Silicon: أضف `device = 'mps'`.
- يتم حفظ نقاط التفتيش كل 500 دورة تدريبية افتراضيًا.

#### 4. تشغيل التدريب
قم بالتدريب من الصفر أو بالضبط الدقيق:
```
python train.py config/train_my_dataset.py
```
- لـ multi-GPU (مثلاً 8 وحدات GPU): `torchrun --standalone --nproc_per_node=8 train.py config/train_my_dataset.py`.
- راقب باستخدام WandB (يسجل الخسائر، عينات؛ فعّله في الإعدادات بـ `wandb_log = True`).
- وقت التدريب: دقائق للنماذج الصغيرة على GPU؛ ساعات/أيام للنماذج الأكبر.

#### 5. توليد عينات (اختبار النموذج)
بعد التدريب، قم بتوليد نص:
```
python sample.py --out_dir=out-my_dataset --start="النص المحفز الخاص بك هنا"
```
هذا يحمل أحدث نقطة تفتيش ويقوم بالتوليد.

#### مشاكل شائعة
- **أخطاء في الذاكرة**: قلل `batch_size` أو `block_size`.
- **لا يوجد GPU**: أضف `--device=cpu --compile=False` للأوامر.
- **مجموعات بيانات كبيرة**: استخدم التدريب الموزع للتوسع.

لمزيد من التفاصيل، راجع ملف README في المستودع وأمثلة البيانات/الإعدادات.

[nanoGPT GitHub](https://github.com/karpathy/nanoGPT)