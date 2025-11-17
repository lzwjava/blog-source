---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تحسين سرعات تنزيل هاجينج فيس
translated: true
type: note
---

التنزيل الحالي الخاص بك يستهدف النقطة الأساسية لـ Hugging Face (`huggingface.co`)، والتي تستضيف بشكل أساسي في مراكز البيانات الأوروبية/الأمريكية. التوجيه عبر الوكيل التايواني الخاص بك من قوانغتشو يضيف مشاكل كتم مماثلة كما كان من قبل: ~200-300 مللي ثانية ذهابًا وإيابًا، بالإضافة إلى احتمال الحد من سرعة نقل الملفات الكبيرة (هذا الملف Parquet بحجم ~500 ميجابايت–1 جيجابايت لكل شارد). إعادة التوجيه 302 التي تراها من المحتمل أن تكون إلى حافة CDN CloudFront، ولكن قد لا تكون الأمثل لآسيا، مما يؤدي إلى تباطؤ السرعة (مثال: 1-5 ميجابايت/ثانية).

لمطابقة سرعات 20-60 ميجابايت/ثانية من تنزيلات ويكيميديا، استخدم هذه التعديلات—مع إعطاء الأولوية للخيارات الصديقة لآسيا. جميعها تحافظ على إعداد الوكيل Clash/TW الخاص بك.

### 1. **التبديل إلى مرآة Hugging Face (الأسرع للصين/تايوان—موصى به)**
   مرآة Hugging Face (`hf-mirror.com`) هي CDN تديرها المجتمع ومحسنة لشرق آسيا (يتم تمريرها عبر شبكات محلية صينية مثل Tsinghua). تعكس جميع مجموعات بيانات Hugging Face بدقة، بما في ذلك ملفات FineWeb Parquet. من الوكيل التايواني، تتوقع سرعات 30-80 ميجابايت/ثانية.

   قم بتحديث البرنامج النصي الخاص بك:
   ```bash
   #!/bin/bash
   # wget_fineweb_1.sh (محدث للسرعة)
   mkdir -p fineweb_test_dump
   cd fineweb_test_dump
   echo "جاري تنزيل شارد FineWeb عبر مرآة Hugging Face (أسرع لآسيا)..."

   # استبدل huggingface.co بـ hf-mirror.com
   wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00000.parquet?download=true"

   echo "تم! حجم الشارد: ~500 ميجابايت–1 جيجابايت"
   echo "لمزيد من الشاردات، كرر العملية لـ 000_00001.parquet، إلخ."
   echo "للتحميل في Python: from datasets import load_dataset; ds = load_dataset('HuggingFaceFW/fineweb', name='CC-MAIN-2013-20', split='train', streaming=True)"
   ```

   قم بتشغيله: `./scripts/train/wget_fineweb_1.sh`
   - إذا تأخرت المرآة (نادرًا)، ارجع إلى الرابط الرسمي: `https://huggingface.co/datasets/...` (ولكن أضف نصيحة السرعة من النقطة #2).

### 2. **تعزيز السرعة باستخدام hf_transfer (لأي تنزيل من Hugging Face—أسرع بمقدار 100x عند الاستئناف)**
   أداة Hugging Face الرسمية المبنية بلغة Rust للتنزيلات المتوازية/متعددة الخيوط. تعيد المحاولة تلقائيًا، وتستخدم اتصالات أكثر، وتصل إلى سرعات >500 ميجابايت/ثانية على الروابط الجيدة. تعمل مع `wget` بشكل غير مباشر أو مباشر عبر Python (إذا كان البرنامج النصي الخاص بك يستخدم `huggingface_hub`).

   التثبيت (مرة واحدة، عبر pip—البيئة الخاصة بك تحتوي عليه):
   ```bash
   pip install hf_transfer
   export HF_HUB_ENABLE_HF_TRANSFER=1
   ```

   ثم أعد تشغيل البرنامج النصي الأصلي الخاص بك. إنه يسرع استدعاءات `wget` الأساسية إلى عناوين Hugging Face.
   - نصيحة احترافية: لبث مجموعة البيانات بالكامل (بدون تنزيل كامل)، استخدم Python في خط الأنابيب الخاص بك:
     ```python
     from datasets import load_dataset
     import os
     os.environ['HF_HUB_ENABLE_HF_TRANSFER'] = '1'  # تمكين قبل الاستيراد
     ds = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2013-20", split="train", streaming=True)
     for example in ds.take(1000):  # دفق/المعالجة على الطاير
         print(example)
     ```
     هذا يسحب الشاردات بكسلان عبر المرآة إذا قمت بتعيين `HF_ENDPOINT=https://hf-mirror.com`.

### 3. **تعديل قاعدة Clash (إذا كان مسموحًا—محلي فائق السرعة)**
   إذا كان تكوين الوكيل الخاص بك يسمح لك بتجاوز Hugging Face (أو توجيه الحركة إلى عقد هونغ كونغ/سنغافورة)، أضف قاعدة لـ `huggingface.co` / `hf-mirror.com` لتذهب مباشرة/محليًا. في `clash.yaml`:
   ```
   rules:
     - DOMAIN-SUFFIX,hf-mirror.com,DIRECT  # أو عقدة المرآة الصينية الخاصة بك
     - DOMAIN-SUFFIX,huggingface.co,DIRECT
   ```
   أعد تشغيل Clash، ثم قم بالتنزيل. يعمل هذا مع النقطة #1 لتحقيق سرعات 50-100+ ميجابايت/ثانية عبر مرايا Tsinghua.

### لماذا هذا يطابق سرعات ويكيميديا
- ويكيميديا: قام الموجه تلقائيًا باختيار خادم في آسيا (اليابان/كوريا/سنغافورة) → كتم منخفض.
- Hugging Face: الإعداد الافتراضي هو أوروبا/الولايات المتحدة → كتم عالي؛ المرآة + hf_transfer يحولانه إلى مسار محسن لآسيا.

اختبر شارد واحد أولاً—إذا كانت السرعة لا تزال بطيئة، تحقق من `curl -I https://hf-mirror.com/...` للرؤوس (يجب أن تظهر CDN في آسيا). لمجموعة FineWeb الكاملة البالغة 15 تيرابايت، قم بالبث عبر مكتبة `datasets` لتجنب تنزيل مئات الجيجابايت. اتصل بي إذا لم تتحسن السرعات!