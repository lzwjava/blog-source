---
audio: false
date: 2025-09-10
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: استراتيجية اختبار تفرد وثبات واجهة برمجة التطبيقات
translated: true
type: note
---

سؤال رائع. دعنا نأخذ نظرة عامة أولاً، ثم نتعامل بشكل عملي مع "التميز" في اختبارات API/الدمج.

# ما هو ما (تذكير سريع)

*   **URL (المسار + الاستعلام)**
    *   المسار عادةً ما يكون **هوية المورد**: `/orders/123`.
    *   معاملات الاستعلام هي **مرشحات/معدِّلات**: `/orders?status=PAID&page=2`.

*   **الطريقة**
    *   `GET/HEAD` آمنتان.
    *   `PUT` **مُعاد** (نفس الاستدعاء، نفس النتيجة).
    *   `POST` **ليس** مُعادًا ما لم تضيف آلية **مفتاح الإعادة**.
    *   `PATCH` غير مضمون الإعادة.

*   **الرؤوس**
    *   `Content-Type`: كيفية ترميز **الجسم**.
        *   `application/json` → جسم JSON.
        *   `application/x-www-form-urlencoded` → جسم `a=1&b=2`.
        *   `multipart/form-data; boundary=----abcd` → ملفات/مرفعات وأجزاء مختلطة.
    *   `Content-Disposition` يظهر **داخل أجزاء multipart**، وليس في رأس الطلب الأساسي. جزء نموذجي:
        ```
        --Boundary123
        Content-Disposition: form-data; name="file"; filename="x.png"
        Content-Type: image/png

        <binary bytes>
        --Boundary123--
        ```
    *   رؤوس مخصصة مفيدة:
        *   **Idempotency-Key**: لإزالة التكرار من استدعاءات POST ذات التأثيرات الجانبية.
        *   **X-Request-ID / Correlation-ID**: لتتبع/تسجيل طلب واحد عبر الخدمات.

*   **الجسم**
    *   JSON: وثيقة مُسلسلة.
    *   `form-urlencoded`: أزواج مفتاح-قيمة مثل سلسلة الاستعلام ولكن في الجسم.
    *   `multipart/form-data`: أجزاء متعددة مفصولة بمحدد `boundary` (`----WebKitFormBoundary...` هو سلسلة شائعة من المتصفحات).

# أين يجب أن توجد الهوية؟

*   **هوية المورد** → في **مسار URL** (`/users/{id}`)، لأنها ثابتة ويمكن وضع إشارة عليها.
*   **معدِّلات العملية** → استعلام أو رؤوس.
*   **التمثيل/الحالة للكتابة** → الجسم.

محاولة ترميز تميز الطلب فقط في URL غالبًا ما تفشل في عمليات الكتابة (مثل POST مع JSON كبير). بدلاً من ذلك، فكر في **طبقتين**:

1.  **هوية الطلب (البصمة)**:
    تجزئة حتمية لـ:
    *   **طريقة** HTTP
    *   **المسار المُهيأ** (النموذج + القيم الملموسة)
    *   **الاستعلام المُهيأ** (مرتب)
    *   **الرؤوس المحددة** (فقط تلك التي تؤثر على الدلالات، مثل `Accept`، `Content-Language`، و *ليس* `Date`)
    *   **الجسم** (JSON مُهيأ أو تجزئة لكل جزء في multipart)

2.  **هوية العملية (الإعادة على مستوى الأعمال)**:
    للعمليات ذات التأثير الجانبي (إنشاء/شحن/تحويل)، استخدم **مفتاح الإعادة** (UUID لكل *نية عمل*). يخزن الخادم النتيجة الأولى تحت ذلك المفتاح ويعيدها عند إعادة المحاولة.

هذه تحل مشاكل مختلفة: البصمات تساعد في **اختباراتك** و **إمكانية المراقبة**؛ مفاتيح الإعادة تحمي **بيئة الإنتاج** من التأثيرات المكررة.

# استراتيجية الاختبار لـ "التميز"

1.  **عرّف دالة بصمة للطلب** (جهة العميل/الاختبار). منطق مثالِي:
    *   أحرف صغيرة لأسماء الرؤوس؛ اشمل فقط قائمة السماح الآمنة.
    *   رتب معاملات الاستعلام؛ استقرّ سلسلة JSON للجسم (أزل المسافات البيضاء، رتب المفاتيح).
    *   SHA-256 على `METHOD\nPATH\nQUERY\nHEADERS\nBODY`.

2.  **امنح كل اختبار معرّف ارتباط**
    *   أنشئ UUID لكل حالة اختبار: `X-Request-ID: test-<suite>-<uuid>`.
    *   سجله على الخادم حتى تتمكن من ربط السجلات باختبار واحد.

3.  **استخدم مفتاح الإعادة حيثما دعت الحاجة**
    *   لطلبات POST التي تنشئ مواردًا أو تشحن أموالاً:
        *   `Idempotency-Key: <uuid>`
        *   يجب على الخادم إعادة نفس 200/201 ونفس الجسم لإعادة المحاولة بنفس المفتاح خلال نافذة الاحتفاظ.

4.  **احتفظ ببيانات الاختبار فريدة ولكن بالحد الأدنى**
    *   استخدم معرفات حتمية مُهيأة مسبقًا (مثل البريد الإلكتروني `user+T001@example.com`) أو أضف لاحقة تحتوي على UUID الخاص بالاختبار.
    *   نظف البيانات، أو الأفضل، صمم الاختبارات لتكون **مُعادَة** باستخدام PUT/DELETE ضد المعرفات المُهيأة مسبقًا حيثما أمكن.

5.  **تحقق من الصحة بالمستوى الصحيح**
    *   للعمليات **المُعادَة**: تحقق من **الحالة**، **التمثيل**، و **التأثيرات الجانبية** (مثل عدم تغير عدد السجلات عند التكرار).
    *   لطلبات **POST غير المُعادَة** مع مفتاح الإعادة: تحقق من أن أول استدعاء يعطي 201، واستدعاء إعادة المحاولة اللاحق يعطي 200 بنفس الجسم (أو 201 مكرر مع نفس المورد).

# مقاطع عملية

**أمثلة cURL**

*   POST بـ JSON:
    ```bash
    curl -X POST https://api.example.com/orders \
      -H 'Content-Type: application/json' \
      -H 'Idempotency-Key: 4b6f2d1a-...' \
      -H 'X-Request-ID: test-orders-create-...' \
      -d '{"customerId":"C123","items":[{"sku":"ABC","qty":1}]}'
    ```
*   رفع multipart:
    ```bash
    curl -X POST https://api.example.com/uploads \
      -H 'X-Request-ID: test-upload-...' \
      -F 'file=@/path/pic.png' \
      -F 'meta={"purpose":"avatar"};type=application/json'
    ```
    (يقوم curl بتعيين `Content-Type: multipart/form-data; boundary=----...` ولكل جزء `Content-Disposition` الخاص به.)

**بصمة طلب من جهة الاختبار في Python (توضيحية):**

```python
import hashlib, json, urllib.parse

def canonical_json(obj):
    return json.dumps(obj, separators=(',', ':'), sort_keys=True)

def normalize_query(url):
    parsed = urllib.parse.urlsplit(url)
    q = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    q.sort()
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urllib.parse.urlencode(q), '')), q

def request_fingerprint(method, url, headers=None, body_bytes=b''):
    headers = headers or {}
    # allowlist headers that affect semantics
    allow = {'accept', 'content-type', 'content-language'}
    norm_headers = {k.lower(): v.strip() for k, v in headers.items() if k.lower() in allow}
    header_line = '\n'.join(f'{k}:{norm_headers[k]}' for k in sorted(norm_headers))
    url_no_query, q_pairs = normalize_query(url)
    query_line = '&'.join(f'{k}={v}' for k, v in q_pairs)
    h = hashlib.sha256()
    h.update((method.upper() + '\n').encode())
    h.update((url_no_query + '\n').encode())
    h.update((query_line + '\n').encode())
    h.update((header_line + '\n').encode())
    h.update(body_bytes or b'')
    return h.hexdigest()
```

*   لأجسام JSON، مرر `body_bytes=canonical_json(payload).encode()`.
*   لـ multipart، قم بتجزئة كل جزء ثم تجزئة التسلسل لتجنب ضوضاء الحدود.

# الإجابة على فكرتك الأساسية

> "إذا كان URL فريدًا فإن الطلبات فريدة؛ معاملات/جسم الطلب لا تزال تساهم كثيرًا — كيف أفكر في التميز لاختبارات API/الدمج؟"

*   اعامل **URL بمفرده** على أنه **غير كافٍ** للتميز في الاختبارات، لأن الرؤوس والجسم يغيران الدلالات بشكل مادي.
*   ابني **بصمة طلب** كما هو موضح أعلاه لإزالة التكرار/التتبع في الاختبارات.
*   لإزالة التكرار على **مستوى الأعمال** لطلبات **POST**، اعتمد على **مفتاح الإعادة**، وليس URL.
*   احتفظ **بهوية المورد** في المسار للوضوح وحتمية أفضل في الاختبار.

# قائمة مراجعة صغيرة يمكنك اعتمادها اليوم

*   [ ] أضف `X-Request-ID` (UUID) إلى كل طلب اختبار.
*   [ ] أضف `Idempotency-Key` إلى طلبات POST التي تنشئ/تشحن.
*   [ ] نفّذ أداة مساعدة للاختبار تحسب بصمة الطلب وتسجلها مع كل تحقق.
*   [ ] هيّئ JSON قبل التجزئة؛ رتب معاملات الاستعلام؛ استخدم قائمة سماح للرؤوس الدلالية.
*   [ ] فضّل PUT للعمليات الإدراج/التحديث لجعل الاختبارات مُعادَة؛ احتفظ بـ POST للعمليات الإنشائية الحقيقية.
*   [ ] لـ multipart، تحقق من **الأجزاء التي قام الخادم بتحليلها** (الأسماء، أسماء الملفات، أنواع المحتوى) بدلاً من بايتات الحدود الخام.

إذا شاركت مكدس الاختبار الحالي الخاص بك (pytest/unittest + requests/httpx، أو Java/Kotlin)، يمكنني إدراج أداة مساعدة جاهزة للاستخدام مخصصة له.