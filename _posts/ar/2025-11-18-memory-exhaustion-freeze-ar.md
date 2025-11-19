---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: أسباب استنفاد الذاكرة تؤدي إلى تجمد النظام
translated: true
type: note
---

مشكلتك **ليست** في وحدة معالجة الرسومات (الـ 4070 Ti بالكاد يتم استخدامها هنا). هذا النص البرمجي **يعمل بالكامل على المعالج والذاكرة العشوائية**، والتوقف المؤقت + تجمد واجهة المستخدم بعد حوالي 140 مليون رمز (token) يكون almost certainly بسبب **نفاد الذاكرة العشوائية** ويبدأ النظام في استخدام الذاكرة الافتراضية (swap) بشكل مكثف على القرص، مما يؤدي إلى تجمد كل شيء لدقائق أو ساعات.

### لماذا يحدث هذا عند حوالي 140–200 مليون رمز

كل رمز → يُخزن كـ uint16 → 2 بايت.

*   140 مليون رمز ≈ 280 ميجابايت
*   1 مليار رمز ≈ 2 جيجابايت
*   10 مليار رمز (FineWeb-10B كامل) ≈ 20 جيجابايت
*   100+ مليار رمز (مثل العديد من تنزيلات FineWeb/Edu) ≈ 200+ جيجابايت

لكن انظر إلى قائمة `all_tokens = []` في Python: لقوائم Python حشوة (overhead) هائلة. كل كائن integer يأخذ حوالي 28–32 بايت على Python 64-bit (حتى لو كانت القيمة تتسع في uint16).

استخدام الذاكرة الفعلي أثناء بناء القائمة:
*   ~150 مليون رمز في قائمة Python → ~150 مليون × 28–32 بايت ≈ **4–5 جيجابايت** فقط لكائنات القائمة
*   ثم تقوم بـ `np.array(..., dtype=np.uint16)` → ~300 ميجابايت أخرى للـ array المضغوط
*   إجمالي ذروة استخدام الذاكرة العشوائية أثناء التحويل ≈ 5–6 جيجابايت + نظام التشغيل + حشوة سطح المكتب

لديك 62.6 جيجابايت ذاكرة عشوائية، فلماذا يتجمد عند 140 مليون رمز فقط؟

لأن ملفك المدخل `train_fineweb.txt` هو على الأرجح **أكبر بكثير** مما تظن.

غالبًا ما يقوم الأشخاص بتنزيل عينات FineWeb-100B أو حتى 1T ويسمونها "train_fineweb.txt". إذا كان ملفك، على سبيل المثال، العينة الشهيرة FineWeb-Edu ذات 100 مليار رمز (~200–300 جيجابايت ملف نصي)، فسيستمر النص البرمجي في القراءة إلى ما لا نهاية، وستنمو قائمة `all_tokens` إلى عشرات أو مئات المليارات من الرموز → مئات الجيجابايت من الذاكرة العشوائية → نفاد الذاكرة (OOM) → إجهاد الذاكرة الافتراضية (swap thrashing) → تجمد كامل لسطح المكتب. مراوح وحدة معالجة الرسومات تدور لأن النص البرمجي لا يزال حيًا (بالكاد)، وPython عالق في دالة `extend()` أو في تحويل `np.array()` النهائي.

### الحلول (اختر واحدًا)

#### أفضل حل: Stream مباشرة إلى .bin دون الاحتفاظ بجميع الرموز في الذاكرة العشوائية أبدًا
هذه النسخة تستخدم ذاكرة عشوائية ضئيلة جدًا (الذروة < 1 جيجابايت حتى لملفات النصوص بحجم التيرابايت):

```python
# stream_tokenize_to_bin.py
import os
import numpy as np
import tiktoken

enc = tiktoken.get_encoding("gpt2")
CHUNK_SIZE = 1_000_000  # characters per chunk, adjust if needed

def process_file(input_path: str, train_bin: str, val_bin: str, val_ratio=0.0005):
    temp_train = train_bin + '.tmp'
    temp_val = val_bin + '.tmp'

    total_tokens = 0
    val_tokens_written = 0
    val_target = None  # we decide it after first pass or approximate

    with open(input_path, "r", encoding="utf-8", errors='ignore') as f, \
         open(temp_train, "wb") as train_f, \
         open(temp_val, "wb") as val_f:

        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            tokens = enc.encode_ordinary(chunk)
            tokens_u16 = np.array(tokens, dtype=np.uint16)

            total_tokens += len(tokens_u16)

            # Approximate validation split on-the-fly (good enough)
            if val_target is None and total_tokens > 10_000_000:
                val_target = int(total_tokens * val_ratio / (1 - val_ratio))

            if val_tokens_written < val_target:
                split_point = min(len(tokens_u16), val_target - val_tokens_written)
                val_f.write(tokens_u16[:split_point].tobytes())
                train_f.write(tokens_u16[split_point:].tobytes())
                val_tokens_written += split_point
            else:
                train_f.write(tokens_u16.tobytes())

            if total_tokens % 50_000_000 == 0:
                print(f"Processed {total_tokens/1e6:.1f}M tokens")

    # Rename temp files
    os.rename(temp_train, train_bin)
    os.rename(temp_val, val_bin)
    print(f"Done! Total ≈ {total_tokens/1e9:.2f}B tokens")
    print(f"train.bin and val.bin ready (no RAM explosion)")

if __name__ == "__main__":
    txt_file = "train_fineweb.txt"
    process_file(txt_file, "train.bin", "val.bin")
```

هذا يقوم بالـ Stream مباشرة إلى القرص، ولا يحتفظ أبدًا بأكثر من جزء (chunk) واحد في الذاكرة.

#### إذا كنت تريد حقًا نمط النص البرمجي الأصلي ولكن بشكل آمن
أضف مراقبة للذاMemory وقم بتقسيم المخرجات:

```python
# add this instead of one giant list
MAX_TOKENS_PER_SHARD = 500_000_000  # ~1 GB per shard

shard_idx = 0
all_tokens = []

for chunk in iter(lambda: f.read(chunk_size), ""):
    if not chunk:
        break
    tokens = enc.encode_ordinary(chunk)
    all_tokens.extend(tokens)

    if len(all_tokens) >= MAX_TOKENS_PER_SHARD:
        arr = np.array(all_tokens, dtype=np.uint16)
        arr.tofile(f"train_shard_{shard_idx:04d}.bin")
        print(f"Saved shard {shard_idx} - {len(arr)/1e6:.1f}M tokens")
        all_tokens.clear()
        shard_idx += 1
```

لاحقًا، ما عليك سوى دمج الأجزاء باستخدام: `cat train_shard_*.bin > train.bin`

### فحص سريع لحجم ملفك الحقيقي
شغّل هذه الأوامر في الطرفية:

```bash
du -h train_fineweb.txt          # human size
wc -c train_fineweb.txt          # bytes
ls -lh train_fineweb.txt
```

FineWeb-10B نصي يكون حوالي 20–25 جيجابايت، و 100B يكون حوالي 200–250 جيجابايت، إلخ.

### الملخص
نصك البرمجي يتوقف لأن قوائم Python تستهلك ذاكرة عشوائية أكثر بـ 15–20 مرة من الـ numpy array النهائي. مع ملفات FineWeb الكبيرة، تتجاوز بسرعة 50+ جيجابايت → ذاكرة افتراضية (swap) → تجمد سطح المكتب.

استخدم نسخة الـ streaming أعلاه — فهي تعمل على ملفات نصية بحجم 1 تيرابايت+ بأقل من 2 جيجابايت ذاكرة عشوائية وتنتهي في بضع ساعات على نواة معالج واحدة.

الـ 4070 Ti الخاصة بك بريئة هنا؛ إنها تنتظر بيانات لن تأتي أبدًا لأن الذاكرة العشوائية معطلة.