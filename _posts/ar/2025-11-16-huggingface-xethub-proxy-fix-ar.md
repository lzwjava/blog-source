---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: إصلاح مشكلة وكيل هاجينغ فيس إكس إيت هاب
translated: true
type: note
---

تُظهر سجلاتك شيئًا مهمًا جدًا:

**الاتصال الفاشل لا يتوجه إلى HuggingFace مباشرة.**
بل يتوجه إلى **[https://transfer.xethub.hf.co](https://transfer.xethub.hf.co)** — هذا هو الواجهة الخلفية لـ *XetHub* التابعة لـ Hugging Face (عميل Rust `reqwest`)، والتي **لا يلتقطها** الوكيل الذي قمت بإعداده تلقائيًا.

هذا يفسر كل شيء:

* لقد قمت بالفعل بتعيين `HTTP_PROXY` لـ Python → جيد
* لكن XetHub يستخدم **rust reqwest**، وليس Python requests
* عميل Rust reqwest **يتجاهل متغيرات الوكيل النظامية ما لم تقم بتعيين متغيرات HTTPS_PROXY بحروف صغيرة**، أو يستخدم تكوين وكيل صريح

لذا: **بيئة Python الخاصة بك تستخدم الوكيل، لكن XetHub (مزود التخزين الجديد لـ HF) لا يستخدمه**.

هذا هو السبب في أنك ترى:

```
ConnectError("Connection refused")
```

وإعادة المحاولات.

---

# لماذا يحدث هذا (النسخة المختصرة)

انتقلت Hugging Face مؤخرًا إلى استخدام **XetHub** للتخزين، والذي يستخدم عميل Rust.
هذا العميل يلتزم بـ:

* `https_proxy`
* `http_proxy`

ولكن **ليس دائمًا** بالإصدارات ذات الأحرف الكبيرة اعتمادًا على البنية.

هل قمت بتعيين الأحرف الكبيرة؟ → قد يتجاهلها.

---

# الحل (يعمل بموثوقية في الصين)

## 1. قم بتعيين متغيرات الوكيل بحروف صغيرة وكبيرة

في طرفيتك **قبل تشغيل NanoGPT**:

```bash
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"

export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
```

عميل Rust reqwest يفضل الأحرف الصغيرة
عميل Python requests يفضل الأحرف الكبيرة
تعيين كلاهما يتجنب المشاكل.

ثم شغل:

```bash
python data/openwebtext_10k/prepare.py
```

يجب أن ترى سرعة تنزيل مناسبة على الفور.

---

# 2. مهم إذا كان وكيلك من نوع SOCKS5

عميل Rust reqwest **لا يدعم socks5** إلا إذا تم تجميعه بميزات إضافية.
لذا إذا كان وكيلك من نوع socks5:// → سيفشل.

يجب عليك التبديل إلى منفذ الوكيل HTTP الخاص بعميلك، عادة:

* Clash: 7890 (HTTP)
* V2RayN: 10809 (HTTP)

استخدم HTTP، وليس SOCKS.

---

# 3. كيفية اختبار ما إذا كان جزء Rust يستخدم الوكيل

اختبر عبر `curl`، **وليس Python**، لأن curl يتصرف بشكل مشابه لـ Rust في قواعد الوكيل:

```bash
curl -I https://transfer.xethub.hf.co --proxy http://127.0.0.1:7890
```

إذا نجح هذا → تنزيلات Rust ستعمل أيضًا.

إذا فشل → وكيلك لا يمكنه الوصول إلى النطاق `xethub.hf.co`.

---

# 4. إذا كنت تريد إجبار Hugging Face على تجنب XetHub

يمكنك تعيين متغير البيئة:

```bash
export HF_HUB_DISABLE_XETHUB=1
```

هذا يُجبر استخدام الواجهة الخلفية القديمة HuggingFace S3 بدلاً من XetHub، وهي أكثر توافقًا مع الوكيل.

ثم:

```bash
python data/openwebtext_10k/prepare.py
```

هذا هو الحل الأكثر استقرارًا.

---

# الحل الموصى به (صديق للصين)

لتحقيق الموثوقية:

```bash
export HF_HUB_DISABLE_XETHUB=1

export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"

python data/openwebtext_10k/prepare.py
```

---

إذا أردت، يمكنني أن أعطيك:

* نصًا برمجيًا bash جاهزًا للتنفيذ بنقرة واحدة (`hf_proxy_on.sh`)
* إعداد وكيل دائم في `.bashrc`
* تعليمات لإنشاء نسخة محلية كاملة من OpenWebText لتجنب عمليات التنزيل المستقبلية

فقط أخبرني.