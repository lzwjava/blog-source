---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: تهيئة وكيل Hugging Face XetHub
translated: true
type: note
---

نعم — **Rust reqwest يدعم بشكل مطلق تكوين البروكسي الصريح**، وعميل Hugging Face's XetHub (المكتوب بلغة Rust) يسمح بهذا أيضًا.
ولكن: Hugging Face **لا تعرض** واجهة برمجة تطبيقات (API) بلغة Python تسمح لك بتمرير إعدادات البروكسي مباشرة.
بدلاً من ذلك، تعتمد XetHub على **متغيرات البيئة** التي يقرأها reqwest تلقائيًا.

لذا فإن تكوين البروكسي الصريح لـ reqwest يبدو كالتالي:

---

# ✔ كيف يكتشف reqwest البروكسيات (رسمي)

يستخدم Reqwest تلقائيًا **متغيرات البيئة** التالية:

* `https_proxy`
* `http_proxy`
* `all_proxy`

استخدام الأحرف الصغيرة هو الجزء المهم.
يتجاهل Reqwest المتغيرات بالأحرف الكبيرة (`HTTPS_PROXY`) إلا إذا تم تمكين علم ميزة معين في وقت الترجمة.

**Hugging Face XetHub يستخدم الإعداد الافتراضي لـ reqwest → الأحرف الصغيرة فقط.**

هذا يعني:

```
export https_proxy="http://127.0.0.1:7890"
export http_proxy="http://127.0.0.1:7890"
```

هو تكوين البروكسي الصريح الوحيد المضمون العمل مع XetHub.

---

# ✔ كيف تتحمّل HuggingFace XetHub تكوين البروكسي

عند تشغيل `load_dataset` في Python، يتم تشغيل ملف ثنائي (binary) مكتوب بلغة Rust يقوم بما يلي:

1. البحث عن متغيرات بيئة البروكسي بالأحرف الصغيرة
2. إعادة كتابة عناوين URL
3. فتح الاتصالات عبر reqwest
4. تنزيل أجزاء الملف من `https://transfer.xethub.hf.co`

إذا لم يتم تعيين هذه المتغيرات البيئية، أو لم يكن يمكن الوصول إليها → سيتم رفض الاتصال.

---

# ✔ إجبار reqwest يدويًا على استخدام البروكسي (كود مرجعي)

فقط لإظهار ما سيفعله reqwest داخليًا:

```rust
let proxy = reqwest::Proxy::https("http://127.0.0.1:7890")?;
let client = reqwest::Client::builder()
    .proxy(proxy)
    .build()?;
```

عميل Hugging Face's XetHub *يفعل شيئًا مكافئًا*، ولكن يتم تشغيله بواسطة متغيرات البيئة.

---

# ✔ تكوين بروكسي صريح كامل يعمل دائمًا مع reqwest (متوافق مع HF)

شغِّل **كل** هذه الأوامر:

```bash
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
export all_proxy="http://127.0.0.1:7890"
```

استخدم بروكسي `http`، وليس `socks5`، لأن:

* دعم reqwest لـ socks هو اختياري
* الملف الثنائي لعملاء XetHub لم يُترجم مع هذه الميزة من أجل HF

لذا قد يفشل اتصال socks بصمت.

---

# ✔ التحقق من أن بروكسيك قيد الاستخدام

جرب:

```bash
env | grep proxy
```

إذا رأيت أحرفًا صغيرة → هذا جيد.

ثم:

```bash
curl -I https://transfer.xethub.hf.co --proxy http://127.0.0.1:7890
```

إذا نجح curl → سينجح reqwest.

---

# الملخص

* Hugging Face datasets أحيانًا يتم تنزيلها عبر **XetHub** (عميل Rust reqwest)
* Reqwest يحترم متغيرات البروكسي **بأحرف صغيرة** فقط بشكل افتراضي
* يجب عليك تعيينها بشكل صريح
* استخدم بروكسي **HTTP**، وليس SOCKS
* `HF_HUB_DISABLE_XETHUB=1` يمكنه تجاوز reqwest تمامًا إذا لزم الأمر

---

إذا أردت، يمكنني إعداد:

* سكريبت "إصلاح بروكسي HF" بأمر واحد
* تكوين دائم لملف `.bashrc` الخاص بك
* كشف تلقائي للتأكد مما إذا كان reqwest يستخدم البروكسي

فقط أعلمني.