---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح أداة إنهاء الذاكرة في سكريبت فاين ويب
translated: true
type: note
---

رسالة "Killed" بدون أي تتبع مكدس (traceback) لبايثون تعني أن قاتل الذاكرة (OOM) في لينكس هو الذي أنهى العملية. هذا يحدث في سكريبت `data/fineweb/prepare.py` لأنه يحاول تحميل ملفك النصي الموحد بالكامل (~15 جيجابايت) (`train_fineweb.txt`) إلى الذاكرة العشوائية (RAM) دفعة واحدة باستخدام أمر مثل `open(...).read()` قبل البدء في الترميز (tokenizing).

على الرغم من أن FineWeb-Edu مصمم للتدفق (التحميل التسلسلي) (أداة التحميل الرسمية تستخدم `datasets` من Hugging Face وتعالج البيانات جزءًا تلو الآخر في أجزاء بحجم ~100 مليون رمز (token) دون تحميل كل شيء في الذاكرة مرة واحدة)، فإن مجلد nanoGPT المخصص لـ fineweb له مسار ملف محلي غير فعال في استخدام الذاكرة للملفات الكبيرة.

### إصلاحات سريعة (اختر واحدة)

1.  **الأفضل والمُوصى به: استخدم أداة التحميل الرسمية لـ FineWeb-Edu التي تعمل بالتدفق بدلاً من الملفات المحلية**  
    لا تستخدم `data/fineweb/prepare.py` الخاص بـ nanoGPT على الإطلاق.  
    استخدم السكريبت الأحدث من Karpathy المصنوع خصيصًا لـ FineWeb-Edu بحجم 10 مليار رمز (أو أكثر):

    ```bash
    # من المجلد الرئيسي لـ nanoGPT (أو من أي مكان)
    wget https://raw.githubusercontent.com/karpathy/build-nanogpt/master/fineweb.py
    python fineweb.py
    ```

    يقوم هذا السكريبت بتحميل وترميز عينة FineWeb-Edu sample-10BT (10 مليار رمز، ~15-20 جيجابايت نص خام) بطريقة تدفقية باستخدام `datasets.load_dataset(..., streaming=True)` ومعالجة متعددة (multiprocessing). إنه لا يحمل مجموعة البيانات الكاملة في الذاكرة العشوائية أبدًا وينتج نفس أجزاء `.bin` التي يتوقعها nanoGPT في مجلد مثل `edu_fineweb10B/`.  
    يعمل بشكل جيد على أجهزة تحتوي على ذاكرة عشوائية بسعة 32-64 جيجابايت (أو حتى أقل إذا قمت بتقليل `num_proc_load_dataset` و `num_proc` في السكريبت).

    للإصدارات الكاملة 100B أو 1T، ما عليك سوى تغيير `remote_name = "sample-10BT"` إلى `"100BT"` أو أي إصدار تحتاجه.

2.  **إذا كنت ترغب حقًا في الاحتفاظ بملف parquet → txt المحلي الخاص بك (بحجم 10)**  
    قم بتعديل `data/fineweb/prepare.py` لمعالجة النص على شكل قطع (chunks) بدلاً من تحميله كله:

    افتح السكريبت واستبدل كتلة `with open(local_file, 'r', encoding='utf-8') as f: data = f.read()` الكبيرة بشيء مشابه لهذا:

    ```python
    from tqdm import tqdm
    import tiktoken
    enc = tiktoken.get_encoding("gpt2")

    chunk_size = 1_000_000  # عدد الأحرف في كل قطعة، يمكنك تعديلها إذا لزم الأمر
    tokens = []
    with open(local_file, "r", encoding="utf-8") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            tokens.extend(enc.encode_ordinary(chunk))  # أو enc.encode(chunk)
            print(f"Tokenized so far: {len(tokens)/1e6:.1f}M tokens")
    tokens = np.array(tokens, dtype=np.uint16)
    ```

    هذا يبقي ذروة استخدام الذاكرة العشوائية عند حوالي ~10-15 جيجابايت حتى لملفك البالغ 15 جيجابايت.

3.  **حلول متعلقة بالعتاد (مؤقتة، غير مثالية)**  
    - إضافة مساحة مبادلة (swap) كبيرة (مثلاً، ملف مبادلة بسعة 64-128 جيجابايت). سيكون الأمر بطيئًا للغاية بمجرد أن يبدأ استخدام المبادلة، لكنه قد ينتهي.  
      ```bash
      sudo fallocate -l 64G /swapfile
      sudo chmod 600 /swapfile
      sudo mkswap /swapfile
      sudo swapon /swapfile
      ```
    - التشغيل على جهاز أو instance يحتوي على ذاكرة عشوائية ≥64 جيجابايت (مثلاً، AWS r6i.4xlarge أو أكبر).

### ملخص
ما عليك سوى تشغيل السكريبت الرسمي `fineweb.py` من build-nanogpt — إنه الحل الأنظف وهو ما يستخدمه الجميع الآن لـ FineWeb. ملفك النصي الموحد البالغ 15 جيجابايت هو المشكلة، وليس FineWeb بحد ذاته.

[سكريبت تحميل FineWeb-Edu الرسمي](https://raw.githubusercontent.com/karpathy/build-nanogpt/master/fineweb.py)  
[صفحة مجموعة بيانات FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)