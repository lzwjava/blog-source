---
audio: false
generated: true
lang: ar
layout: post
title: خطأ في بناء pycrypto
translated: true
type: note
---

يحدث الخطأ لأن حزمة `pycrypto` تتطلب ملف رأس Python المسمى `longintrepr.h`، وهو جزء من رؤوس تطوير Python. هذا الملف مفقود في بيئة Python 3.13 الخاصة بك. إليك كيفية حله:

### الحل:
1. **تثبيت رؤوس تطوير Python**  
   قم بتثبيت حزمة تطوير Python 3.13 لنظام التشغيل الخاص بك. على Ubuntu/Debian، قم بتشغيل:
   ```bash
   sudo apt-get install python3.13-dev
   ```

2. **إعادة تثبيت `pycrypto`**  
   بعد تثبيت الرؤوس، أعد محاولة التثبيت:
   ```bash
   pip install pycrypto
   ```

---

### توصيات بديلة:
**الخيار 1: استبدال `pycrypto` بـ `pycryptodome` (مفضل)**  
`pycrypto` أصبح قديماً وغير مدعوم. انتقل إلى النسخة المطورة والمستمرة `pycryptodome`، وهي متوافقة مع واجهة برمجة التطبيقات (API):
```bash
pip uninstall pycrypto
pip install pycryptodome
```

**الخيار 2: استخدام إصدار قديم من Python**  
إذا سمحت التوافقية، استخدم Python ≤3.9 (حيث من المعروف أن `pycrypto` يعمل):
```bash
# مثال باستخدام pyenv
pyenv install 3.9.18
pyenv local 3.9.18
pip install -r requirements.txt
```

---

### لماذا حدث هذا:
- `longintrepr.h` هو ملف رأس داخلي في Python يُستخدم لتمثيل الأعداد الصحيحة. يتم تضمينه في حزم تطوير Python ولكن ليس في التثبيتات القياسية.
- قد يحتوي Python 3.13 على تغييرات هيكلية تعطل الحزم القديمة مثل `pycrypto` (تم تحديثه آخر مرة في 2014).
- يشير تحذير التقادم إلى أن `pycrypto` يستخدم طرق بناء قديمة غير مدعومة في إصدارات `pip` الأحدث.

### الوقاية:
1. **تجنب `pycrypto`**: استخدم `pycryptodome` للاحتياجات التشفيرية.
2. **تثبيت إصدارات Python**: للمشاريع القديمة، استخدم Python ≤3.9 في بيئات مثل Docker/Venv.
3. **التحقق من التبعيات**: استخدم `pip check` لتحديد الحزم غير المتوافقة.

---

لا تعتمد أي من الحزم التي قمت بإدراجها (`aliyunsdkcore`, `aliyun-python-sdk-ecs`, `alibabacloud_vpc20160428`, إلخ) بشكل مباشر على **`pycrypto`**.

ومع ذلك، إذا كنت ترى أن `pycrypto` يتم تثبيته، فقد يكون ذلك تبعية **غير مباشرة** لإحدى هذه الحزم. للتحقق من الحزمة التي تتطلب `pycrypto`، قم بتشغيل:

```bash
pip show pycrypto
```
أو
```bash
pipdeptree | grep -i pycrypto
```

### المشتبه بهم المحتملون:
1. **الحزم الأمنية القديمة أو المهجورة** (على الرغم من عدم وجود أي منها في قائمتك تتطلب `pycrypto` بشكل صريح).
2. **تبعية قديمة** من حزمة مثل `paramiko` (SSH) أو `google-auth`، ولكنها عادة ما تنتقل إلى `pycryptodome`.

### الإجراء الموصى به:
1. **استبدل `pycrypto` بـ `pycryptodome`** (نسخة مطورة ومستمرة):
   ```bash
   pip uninstall pycrypto
   pip install pycryptodome
   ```
   تقبل بعض الحزم `pycryptodome` كبديل مباشر.

2. **أعد تثبيت التبعيات قسراً** لضمان عدم وجود روابط خفية:
   ```bash
   pip install --upgrade --force-reinstall -r requirements.txt
   ```

3. **إذا استمر وجود `pycrypto`**، قم بمراجعة بيئتك:
   ```bash
   pipdeptree --warn silence | grep -i crypto
   ```

### الاستنتاج الرئيسي:
الحزم المدرجة في قائمتك لا تعتمد مباشرة على `pycrypto`، ولكن تبعية أخرى مخفية قد تكون هي السبب. عزل التبعية باستخدام `pipdeptree` سيحدد الجاني. إذا لم تكن هناك حزمة حرجة تتطلبها، **قم بإزالة `pycrypto` نهائياً** — فهو قديم وقد يكون غير آمن.

---

بناءً على سجلاتك، لا تعتمد أي من **الحزم المدرجة بشكل صريح** بشكل مباشر على `pycrypto`. ومع ذلك، فإن إحدى تبعياتك لها **تبعية غير مباشرة** عليه. إليك كيفية تحديد ذلك وحله:

### 1. تحديد الحزمة المسببة للمشكلة
قم بتشغيل هذا الأمر للعثور على الحزمة عالية المستوى التي تتطلب `pycrypto`:
```bash
pipdeptree --warn silence | grep -i pycrypto
```

### 2. المشتبه بهم الشائعون في مجموعتك
بناءً على حزمك، إليك المرشحون الأكثر احتمالاً:
- **`paramiko`** (يستخدمه `hcloud`، `tigeropen`، أو حزم SDK للسحابة)
- **`google-auth`** (تستخدمه حزم Google Cloud)
- **`boto`** (مكتبات AWS القديمة)
- **`ansible`** (إذا تم استخدامه بشكل غير مباشر)

### 3. الحل الفوري: استبدال `pycrypto`
نظرًا لأن `pycrypto` قديم ومتعطل على Python 3.13، استبدله بالنسخة المطورة والمستمرة:
```bash
pip uninstall pycrypto
pip install pycryptodome
```

### 4. إذا استمرت التبعية
أعد تثبيت جميع الحزم قسراً مع فحوصات التبعية:
```bash
pip install --upgrade --force-reinstall -r requirements.txt
```

### 5. التحقق من التثبيت
تحقق مما إذا كانت `pycryptodome` تلبي التبعية:
```bash
python -c "from Crypto import Random; print('Success')"
```

### لماذا يحدث هذا
- `pycrypto` كان تبعية تشفير شائعة للحزم القديمة (آخر تحديث: 2014)
- أزال Python 3.13 الرؤوس الداخلية مثل `longintrepr.h` التي كانت `pycrypto` تعتمد عليها
- البدائل الحديثة مثل `cryptography` (التي تقوم بتثبيتها) لا تستخدم `pycrypto`

أسرع حل هو **الخطوة 3** – استبدال `pycrypto` بـ `pycryptodome` المتوافق مع واجهة برمجة التطبيقات (API). هذا يحل مشكلة التجميع مع الحفاظ على التوافقية.