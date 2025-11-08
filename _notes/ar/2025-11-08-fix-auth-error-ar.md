---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح خطأ مصادقة واجهة برمجة تطبيقات الترجمة
translated: true
type: note
---

### تحليل سير العمل وسبب الخطأ

سير عمل GitHub Actions الخاص بـ "ترجمة الملاحظات الحديثة" يبدو منظمًا بشكل عام بشكل جيد—فهو يقوم باستخراج المستودع، وإعداد Python، وتثبيت التبعيات، وتشغيل سكريبت الترجمة على أحدث N منشور، وتثبيت التغييرات على `_notes/`. ومع ذلك، بناءً على السجلات التي شاركتها سابقًا (مع أخطاء 401 أثناء الترجمة إلى لغات مثل ar, de, fr، إلخ)، فإن المشكلة تكمن في المصادقة لطلبات API الترجمة داخل `scripts/translation/update_lang_notes.py`.

#### السبب الجذري
- الخطأ `"No cookie auth credentials found"` (HTTP 401) هو خطأ محدد لـ **OpenRouter API** (أو عميل/مكتبة Python تتفاعل معه، مثل LiteLLM أو SDK غير رسمي). يحدث هذا عندما يفتقر طلب API إلى رؤوس المصادقة الصحيحة.
- يتوقع OpenRouter `Authorization: Bearer <your_openrouter_api_key>` في الطلبات. إذا لم يتم تمرير المفتاح بشكل صحيح، فإن بعض العملاء يتراجعون إلى (أو يسيئون تفسير الحاجة إلى) المصادقة القائمة على الكوكيز، مما يؤدي إلى هذا الخطأ بالضبط.
- في سير العمل الخاص بك:
  - أنت تقوم بتعيين `OPENROUTER_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}`، مما يمرر قيمة سرية إلى بيئة السكريبت.
  - ولكن من المرجح أن السكريبت لا يقرأ/يستخدم متغير البيئة هذا بشكل صحيح. التباينات الشائعة:
    - يتوقع السكريبت `OPENAI_API_KEY` (لنقاط النهاية المتوافقة مع OpenAI مثل OpenRouter).
    - أو أنه يستخدم مكتبة (مثل `openai` Python SDK) دون تعيين عنوان URL الأساسي إلى `https://openrouter.ai/api/v1`.
    - قد يحتوي السر `DEEPSEEK_API_KEY` في الواقع على **مفتاح OpenRouter API** الخاص بك (الموجه إلى نماذج DeepSeek/Grok)، ولكن إذا كان مفتاح DeepSeek مباشرًا، فلن يعمل مع OpenRouter.
- من السجلات، يستخدم السكريبت النموذج `'x-ai/grok-4-fast'` (Grok 4 عبر OpenRouter)، وهو يعالج front matter/العناوين بنجاح لكنه يفشل في ترجمة المحتوى لكل لغة.
- هذه ليست مشكلة في GitHub Actions—بل هي في إعداد عميل API في سكريبت Python. يستمر سير العمل في خطوة commit (ومن هنا جاء سجل `git config user.name "github-actions[bot]"`)، ولكن بدون الترجمات، تتم إضافة الملفات الإنجليزية فقط.

#### الإصلاحات الموصى بها
1. **تحديث متغيرات البيئة في سير العمل**:
   - محاذاة مع إعدادات OpenRouter الشائعة (المتوافقة مع OpenAI). قم بتغيير كتلة `env` في خطوة "Translate posts" إلى:
     ```
     env:
       GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
       OPENAI_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}  # إعادة تسمية المتغير إلى ما يتوقعه السكريبت
       OPENAI_BASE_URL: https://openrouter.ai/api/v1   # مطلوب للتوجيه إلى OpenRouter
     ```
   - إذا كان `DEEPSEEK_API_KEY` هو مفتاح OpenRouter الخاص بك، فهذا جيد. إذا كان مفتاح DeepSeek مباشرًا، فقم بإنشاء سر جديد `OPENROUTER_API_KEY` في إعدادات المستودع باستخدام مفتاح OpenRouter الفعلي الخاص بك (احصل على واحد من [openrouter.ai/keys](https://openrouter.ai/keys)).
   - للاختبار: أضف `echo $OPENAI_API_KEY` (مخفى) إلى خطوة التشغيل لتصحيح الأخطاء في السجلات.

2. **إصلاح سكريبت Python (`update_lang_notes.py`)**:
   - تأكد من أنه يقوم بتهيئة عميل OpenAI بهذه الطريقة (بافتراض استخدام مكتبة `openai`):
     ```python
     import os
     from openai import OpenAI

     client = OpenAI(
         api_key=os.getenv("OPENAI_API_KEY"),
         base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")  # الإعداد الافتراضي لـ OpenAI إذا لم يتم التعيين
     )

     # ثم استخدم client.chat.completions.create(..., model="x-ai/grok-4-fast")
     ```
   - إذا كنت تستخدم LiteLLM (شائع لمزودي متعددين): قم بتثبيته إذا لم يكن في `requirements.txt`، واستدع `completion(model="openrouter/x-ai/grok-4-fast", api_key=os.getenv("OPENAI_API_KEY"), api_base="https://openrouter.ai/api/v1", ...)`.
   - لحلقة الترجمة: أضف معالجة الأخطاء لكل لغة (مثل `try/except` حول استدعاءات API، وتسجيل الإخفاقات، وتخطيها في حالة 401).
   - التعامل مع الكوكيز بشكل صريح؟ من غير المرجح الحاجة إليه—التزم بمفاتيح API. إذا كان السكريبت يحتوي على كود متصفح/Selenium، فقم بإزالته لموثوقية CI.

3. **تحسينات سير العمل**:
   - **التحقق من صحة الإدخال**: أضف فحصًا لـ N=0 أو `--n` غير صالح لتجنب عدم معالجة أي شيء.
   - **Commit مشروط**: `git diff --cached --quiet || git commit` الخاص بك جيد، ولكن قم بتحديث الرسالة لتعكس جميع اللغات: `-m "Add translated posts (ar, de, es, fr, hi, ja, zh, hant)"`.
   - **التخزين المؤقت**: أضف `actions/cache` لـ `pip` لتسريع عمليات التثبيت.
   - **وضع التصحيح**: أضف إدخالًا اختياريًا `debug: true` وعلم `--debug` إلى السكريبت لتسجيل مفصّل.
   - **الأذونات**: تأكد من أن بيئة `github-pages` لديها صلاحية قراءة/كتابة إذا لزم الأمر.
   - مقتطف YAML المحدث بالكامل لخطوة "Translate posts":
     ```
     - name: Translate posts
       run: |
         python scripts/translation/update_lang_notes.py --n ${{ inputs.n }}
       env:
         GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         OPENAI_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
         OPENAI_BASE_URL: https://openrouter.ai/api/v1
     ```

4. **خطوات الاختبار**:
   - **اختبار محلي**: قم بتشغيل `python scripts/translation/update_lang_notes.py --n 1` محليًا مع تصدير متغيرات البيئة (مثل `export OPENAI_API_KEY=your_key`).
   - **اختبار سير العمل**: قم بتشغيله باستخدام `workflow_dispatch` و N=1، وتحقق من السجلات لاستدعاءات API.
   - **التحقق من السر**: في إعدادات المستودع > Secrets، تأكد من أن `DEEPSEEK_API_KEY` يحتوي على مفتاح OpenRouter صالح (يبدأ بـ `sk-or-...`).
   - إذا كان لا يزال فاشلًا، أضف `--verbose` إلى السكريبت وافحص رؤوس الطلب (على سبيل المثال، عبر `print(client.api_key)`).

هذا يجب أن يحل مشاكل أخطاء 401 ويجعل الترجمات تتدفق. إذا قمت بمشاركة مقاطع من `update_lang_notes.py` (على سبيل المثال، تهيئة عميل API)، يمكنني تحديد الموقع بدقة أكبر.

#### المراجع
- [بدء سريع لـ OpenRouter (إعداد مصادقة API)](https://openrouter.ai/docs/quickstart)
- [تكامل LiteLLM مع OpenRouter](https://docs.litellm.ai/docs/providers/openrouter) (إذا كنت تستخدمه)
- [مشكلة على GitHub حول خطأ مصادقة مشابه في OpenRouter](https://github.com/mendableai/firecrawl/issues/1352)
- [مناقشة على Reddit حول أخطاء 401 في OpenRouter](https://www.reddit.com/r/openrouter/comments/1oqiaol/error_401_no_cookie_auth_credentials_found/)