---
audio: false
generated: true
image: false
lang: ar
layout: post
model: mistralai/mistral-medium-3.1
title: إصلاح خطأ نموذج LibreChat في OpenRouter
translated: true
type: note
---

يحدث هذا الخطأ عند استخدام **LibreChat** مع **OpenRouter** كخلفية، عندما لا يكون النموذج المحدد (`gpt-5-chat` أو ما شابه) متاحًا أو لا يتم توجيهه بشكل صحيح. إليك تحليلًا للمشكلة وكيفية حلها:

---

## **لماذا يحدث هذا الخطأ**
- يعمل **OpenRouter** كوسيط للوصول إلى نماذج الذكاء الاصطناعي المختلفة، ولكن ليس جميع النماذج متاحة أو مفعلة افتراضيًا.
- يعني الخطأ `404 No endpoints found that support tool use` أن النموذج الذي حددته (`gpt-5-chat`) إما:
  - غير مدعوم من قبل OpenRouter.
  - غير مضبوط في إعدادات LibreChat الخاصة بك.
  - يتطلب موفرًا مختلفًا أو مفتاح واجهة برمجة تطبيقات (API Key) مختلفًا.

---

## **كيفية إصلاح المشكلة**

### 1. **تحقق من النماذج المتاحة في OpenRouter**
- قم بزيارة [قائمة نماذج OpenRouter](https://openrouter.ai/models) لمعرفة النماذج المتاحة.
- حتى الآن، `gpt-5-chat` ليس نموذجًا رسميًا من OpenAI (أحدث نموذج هو GPT-4o). إذا كنت تقصد GPT-4، فاستخدم `openai/gpt-4` أو ما شابه.

### 2. **تحديث تكوين LibreChat**
- في LibreChat، انتقل إلى **الإعدادات (Settings)** > **اختيار النموذج (Model Selection)**.
- اختر نموذجًا **مدعومًا من OpenRouter** (مثل `openai/gpt-4`، `mistralai/mistral-7b`، إلخ).
- إذا كنت ترغب في استخدام OpenAI مباشرة، قم بتحويل **موفر واجهة برمجة التطبيقات (API Provider)** إلى **OpenAI** بدلاً من OpenRouter.

### 3. **التحقق من مفاتيح واجهة برمجة التطبيقات (API Keys)**
- تأكد من أن لديك **مفتاح OpenRouter API صالح** (إذا كنت تستخدم OpenRouter) أو **مفتاح OpenAI API صالح** (إذا كنت تستخدم OpenAI).
- أضف المفتاح في **الإعدادات (Settings)** > **مفاتيح واجهة برمجة التطبيقات (API Keys)** في LibreChat.

### 4. **إعادة تشغيل LibreChat**
- بعد تغيير الإعدادات، أعد تشغيل LibreChat لتطبيق التغييرات.

### 5. **التحقق من وثائق LibreChat**
- راجع [دليل إعداد OpenRouter لـ LibreChat](https://github.com/danny-avila/LibreChat#openrouter) للحصول على تعليمات مفصلة.

---

## **حلول بديلة**
- إذا كنت ترغب في استخدام نماذج OpenAI، اضبط الموفر على **OpenAI** واختر `gpt-4` أو `gpt-4o` أو `gpt-3.5-turbo`.
- إذا كنت ترغب في استخدام OpenRouter، اختر نموذجًا من [قائمته المدعومة](https://openrouter.ai/models).

---