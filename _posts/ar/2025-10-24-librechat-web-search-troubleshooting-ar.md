---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: استكشاف أخطاء البحث على الويب في LibreChat
translated: true
type: note
---

لنستكشف الأخطاء وإصلاحها بعناية — عندما **لا يعمل البحث على الويب في LibreChat** حتى بعد إضافة مفاتيح **Firecrawl** و **SerpApi** و **Jina API**، فإن المشكلة تكاد تكون دائمًا واحدة مما يلي: أخطاء في التهيئة، أو أعلام تمكين مفقودة في الخلفية، أو سوء تفسير لواجهة المستخدم.

إليك تحليلاً واضحًا يمكنك اتباعه (بدون جداول، فقط تفسيرات):

---

### 1. **تحقق مما إذا كان "البحث على الويب" مفعلًا في تهيئة الخلفية**

افتح ملف تهيئة خادم LibreChat (عادةً `.env` أو `api/config.yaml` اعتمادًا على إعدادك) وتأكد من أن لديك شيء مثل:

```
# لملف .env
SEARCH_ENABLED=true
```

أو، إذا كنت تستخدم YAML:

```yaml
features:
  search: true
```

إذا لم يتم تعيين `SEARCH_ENABLED` أو `search` صراحةً إلى `true`، فقد تظهر زر واجهة المستخدم ولكنه لن ينفذ عمليات البحث فعليًا.

---

### 2. **تأكد من أن أسماء مفاتيح API صحيحة**

كل موفر يتوقع أسماء متغيرات بيئة محددة. على سبيل المثال:

* لـ **SerpApi**:

  ```
  SERPAPI_API_KEY=your_key_here
  ```
* لـ **Firecrawl**:

  ```
  FIRECRAWL_API_KEY=your_key_here
  ```
* لـ **Jina**:

  ```
  JINA_API_KEY=your_key_here
  ```

تأكد أيضًا من تصدير هذه المتغيرات أو تحميلها في نفس بيئة عملية `backend` قيد التشغيل.

للتحقق:

```bash
echo $SERPAPI_API_KEY
```

إذا لم يُرجع شيء، فهذا يعني أن الخلفية لا تراه.

---

### 3. **أعد تشغيل LibreChat بعد تعديل المفاتيح**

لا تعيد LibreChat تحميل متغيرات البيئة تلقائيًا. شغّل:

```bash
docker compose down
docker compose up -d
```

(أو `npm run start` مرة أخرى إذا كنت لا تستخدم Docker).

---

### 4. **تحقق من موفر البحث الذي تستخدمه LibreChat فعليًا**

تختار LibreChat خلفية افتراضية واحدة للبحث على الويب اعتمادًا على ترتيب التهيئة.

إذا أردت منها استخدام SerpApi، على سبيل المثال، يجب أن تحدد:

```
SEARCH_PROVIDER=serpapi
```

بدلاً من ذلك، إذا أردت Jina:

```
SEARCH_PROVIDER=jina
```

إذا قمت فقط بتعيين المفاتيح ولكن لم تحدد أي موفر يجب استخدامه، فقد تفترض LibreChat عدم وجود موفر افتراضي.

---

### 5. **اطلع على سجلات الخلفية**

شغّل:

```bash
docker logs librechat-backend
```

أو

```bash
npm run start:debug
```

ابحث عن رسائل مثل:

```
[Search] SerpApi key missing or invalid
```

أو

```
Search provider not configured
```

هذه هي أفضل الأدلة.

---

### 6. **اختبر واجهات البرمجة مباشرة**

للتأكد من أن مفاتيحك تعمل فعليًا:

**اختبار SerpApi:**

```bash
curl "https://serpapi.com/search.json?q=chatgpt&api_key=YOUR_KEY"
```

**اختبار Firecrawl:**

```bash
curl "https://api.firecrawl.dev/v1/search?q=chatgpt" -H "Authorization: Bearer YOUR_KEY"
```

**اختبار Jina:**

```bash
curl "https://r.jina.ai/chatgpt" -H "Authorization: Bearer YOUR_KEY"
```

إذا فشلت هذه الاختبارات، فهذا يعني أن المفاتيح نفسها غير صالحة أو أنك تجاوزت الحد المسموح به.

---

### 7. **عدم تطابق إصدار واجهة المستخدم**

إذا قمت مؤخرًا بتحديث LibreChat (خاصة من الإصدار v0.7 السابق إلى v0.8+)، فقد يكون مفتاح تبديل `Web Search` في واجهة المستخدم موجودًا حتى لو كان إصدار الخلفية لديك لا يدوح وحدة البحث المدمجة Firecrawl/Jina بعد.
شغّل:

```bash
git pull
```

وأعد البناء:

```bash
docker compose build --no-cache
docker compose up -d
```

---

### 8. **التحقق النهائي — تأكد من واجهة المستخدم على الويب**

افتح واجهة المستخدم، وانتقل إلى **الإعدادات → الميزات**، وتأكد من:

* مفتاح تبديل "البحث على الويب" في وضع التشغيل
* موفرك المختار مدرج في القائمة (SerpApi أو Firecrawl أو Jina)

إذا كانت العبارة *"لا يوجد موفر متاح"*، فهذا يعني أن الخلفية لا تقرأ مفاتيحك.

---

إذا أردت، يمكنك لصق الجزء ذي الصلة من ملف `.env` الخاص بك (مع إخفاء المفاتيح) وسأحدد بالضبط أي سطر مفقود أو اسمه خاطئ.

هل ترغب في عرض ذلك المقتطف لي؟