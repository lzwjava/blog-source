---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: استخدام hf-mirror.com في الصين
translated: true
type: note
---

### فهم hf-mirror.com
hf-mirror.com هو مرآة مجتمعية للنسخة الرسمية من Hugging Face Hub (huggingface.co)، مصمم خصيصًا لمساعدة المستخدمين في الصين (بما في ذلك قوانغتشو) على تجاوز قيود الشبكة وتنزيل نماذج/مجموعات البيانات الخاصة بالذكاء الاصطناعي بشكل أسرع. يقوم بتكرار هيكل المستودع بالكامل، لذا يمكنك الوصول إلى نماذج مثل GPT-2 أو مجموعات بيانات مثل WikiText دون الوصول المباشر إلى الموقع الأصلي، الذي غالبًا ما يكون بطيئًا أو محظورًا. نظرًا لأنك تستخدم وكيل Clash غالبًا، لاحظ أن hf-mirror.com مستضاف محليًا ولا يتطلب عادةً استخدام وكيل للوصول – فهو مُحسّن للاستخدام المباشر في الصين. إذا كنت تقوم بالفعل بتوجيه حركة المرور عبر Clash، فيمكنك إما توجيه حركة مرور hf-mirror.com مباشرة (لتجنب القفزات غير الضرورية) أو الإبقاء عليها عبر الوكيل إذا كنت تفضل ذلك.

### الإعداد الأساسي: استخدام المرآة
المفتاح هو تعيين متغير البيئة `HF_ENDPOINT` للإشارة إلى المرآة. هذا يعمل عالميًا لأدوات Hugging Face مثل مكتبة `transformers`، أو `huggingface-cli`، أو `hfd` (أداة تنزيل أسرع). افعل هذا **قبل** استيراد المكتبات أو تشغيل عمليات التنزيل.

#### 1. تعيين متغير البيئة
- **على Linux/macOS (دائم)**: أضف إلى ملف `~/.bashrc` أو `~/.zshrc`:
  ```
  echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.bashrc
  source ~/.bashrc
  ```
- **على Windows (PowerShell، دائم)**: شغّل مرة واحدة:
  ```
  [System.Environment]::SetEnvironmentVariable('HF_ENDPOINT', 'https://hf-mirror.com', 'User')
  ```
  ثم أعد تشغيل الطرفية.
- **مؤقت (أي نظام تشغيل)**: أضف البادئة للأوامر مثل:
  ```
  HF_ENDPOINT=https://hf-mirror.com your_command_here
  ```

هذا يوجه جميع تنزيلات Hugging Face إلى المرآة دون تغيير الكود الخاص بك.

#### 2. تثبيت الأدوات المطلوبة
- ثبّت واجهة سطر أوامر Hugging Face Hub (لعمليات التنزيل):
  ```
  pip install -U huggingface_hub
  ```
- لتنزيلات أسرع، احصل على `hfd` (Hugging Face Downloader، يستخدم aria2 للسرعات متعددة الخيوط):
  ```
  wget https://hf-mirror.com/hfd/hfd.sh  # أو نزّل عبر المتصفح
  chmod +x hfd.sh
  ```

#### 3. تنزيل النماذج أو مجموعات البيانات
- **باستخدام huggingface-cli** (يدعم الاستئناف عند المقاطعة):
  ```
  # تنزيل نموذج (مثلاً، GPT-2)
  huggingface-cli download gpt2 --resume-download --local-dir ./gpt2

  # تنزيل مجموعة بيانات (مثلاً، WikiText)
  huggingface-cli download --repo-type dataset wikitext --resume-download --local-dir ./wikitext
  ```
- **باستخدام hfd** (أسرع، خاصة للملفات الكبيرة):
  ```
  # نموذج
  ./hfd.sh gpt2

  # مجموعة بيانات
  ./hfd.sh wikitext --dataset
  ```
- **في كود Python** (مثلاً، مع مكتبة transformers):
  ```python
  import os
  os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'  # عيّن قبل عمليات الاستيراد

  from transformers import AutoModel, AutoTokenizer
  model = AutoModel.from_pretrained('gpt2')  # سيتنزّل من المرآة تلقائيًا
  tokenizer = AutoTokenizer.from_pretrained('gpt2')
  ```
  شغّل باستخدام: `HF_ENDPOINT=https://hf-mirror.com python your_script.py`

#### 4. التعامل مع النماذج المقيدة/التي تتطلب تسجيل الدخول
بعض النماذج (مثل Llama-2) تتطلب حساب Hugging Face ورمز وصول:
- سجّل الدخول على huggingface.co (استخدم وكيل Clash الخاص بك إذا كان الموقع محظورًا).
- أنشئ رمز وصول من https://huggingface.co/settings/tokens.
- نزّل باستخدام:
  ```
  huggingface-cli download --token hf_YourTokenHere meta-llama/Llama-2-7b-hf --resume-download --local-dir ./Llama-2-7b-hf
  ```
  أو بالنسبة لـ hfd:
  ```
  ./hfd.sh meta-llama/Llama-2-7b-hf --hf_username your_username --hf_token hf_YourTokenHere
  ```

### التكامل مع وكيل Clash
نظرًا لأن hf-mirror.com هو مرآة صينية، يجب أن يكون الوصول إليه ممكنًا دون Clash (الاتصال المباشر أسرع). ومع ذلك، إذا كنت تريد استخدام الوكيل له (مثلاً للاتساق أو إذا واجهت أي مشاكل)، فاضبط Clash لتوجيه حركة المرور إلى hf-mirror.com عبر مجموعة الوكيل المفضلة لديك. لا يحتاج Clash إلى إعداد خاص لـ "HF" – فهو يعمل على مستوى النظام.

#### نصائح سريعة لإعداد Clash
- تأكد من أن Clash يعمل وتم تعيينه كوكيل النظام الخاص بك (في Clash: اذهب إلى "General" > فعّل "System Proxy").
- **توجيه hf-mirror.com مباشرة (مُوصى به للسرعة)**: حرّر ملف الإعدادات YAML لـ Clash (عادة `config.yaml` في مجلد Clash). أضف قاعدة لتجاوز الوكيل للمرآة:
  ```
  rules:
    # ... القواعد الحالية الخاصة بك ...
    - DOMAIN-SUFFIX,hf-mirror.com,DIRECT  # يتجاوز الوكيل، يذهب مباشرة
    # ... بقية القواعد ...
  ```
  أعد تحميل الإعدادات في Clash (Profiles > Reload).
- **استخدم الوكيل إذا لزم الأمر**: إذا كنت تفضل التوجيه عبر Clash، لا تضيف قاعدة خاصة – سوف يتبع الإعداد الافتراضي الخاص بك (مثلاً، `MATCH,Proxy`). اختبر ذلك عن طريق اختبار ping لـ hf-mirror.com في متصفح مع تشغيل/إيقاف Clash.
- للتنزيلات: شغّل الأوامر في طرفية حيث يكون وكيل النظام نشطًا (يتعامل Clash مع ذلك). إذا كنت تستخدم Python، فإن المكتبات مثل `requests` (المستخدمة من قبل transformers) تحترم متغيرات البيئة `HTTP_PROXY`/`HTTPS_PROXY` التي يعينها Clash (مثلاً، `http://127.0.0.1:7890` لمنفذ HTTP).
- الاختبار: جرّب تنزيل نموذج صغير مثل `distilbert-base-uncased`. إذا كان بطيئًا، فعّطِل Clash لحركة مرور hf-mirror.com.

### استكشاف الأخطاء وإصلاحها
- **هل لا تزال التنزيلات تصل إلى huggingface.co؟** تأكد من تعيين `HF_ENDPOINT` **قبل** استيراد أي مكتبات من HF (أعد تشغيل notebook/الطرفية الخاصة بك).
- **سرعات بطيئة؟** استخدم `hfd` مع aria2 (يدعم اتصالات متعددة). أو تحقق من شبكتك – غالبًا ما يحصل مستخدمو قوانغتشو على سرعات 10-50 ميجابايت/ثانية على hf-mirror.com.
- **أخطاء مع مجموعات البيانات؟** بعضها يحتوي على نصوص برمجية مخصصة؛ حرّرها لاستخدام `https://hf-mirror.com` كعنوان URL أساسي.
- **خاص بـ Windows**: إذا كنت تستخدم Anaconda، عيّن متغير البيئة في البيئة الأساسية.
- لاستضافة مرآة محلية متقدمة (إذا كنت تريد تحكمًا كاملاً)، اطّلع على أدوات مفتوحة المصدر مثل Olah أو hf-mirror-site على GitHub، لكن ابدأ بالمرآة العامة.

هذا الإعداد يجب أن يمكنك من التنزيل بموثوقية. إذا واجهت أخطاء محددة، شارك الناتج لمزيد من المساعدة!

### المراجع
- [الدليل الرسمي لـ HF-Mirror](https://hf-mirror.com/)
- [وثائق Hugging Face Hub حول نقاط النهاية](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables#huggingface_hub_constants.HF_ENDPOINT)
- [أداة التنزيل hfd](https://hf-mirror.com/hfd/hfd.sh)
- [قواعد إعداد Clash](https://github.com/Dreamacro/clash/wiki/Configuration#rules)
- [Stack Overflow: التنزيل في الصين](https://stackoverflow.com/questions/77388822/how-to-download-huggingface-bert-base-uncased-in-china)