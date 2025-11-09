---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: دليل تهيئة واجهة برمجة التطبيقات REST في CodeIgniter
translated: true
type: note
---

فيما يلي دليل واضح ومفصل خطوة بخطوة لفهم واستخدام ملف تكوين REST API الخاص بـ CodeIgniter الذي شاركته (`application/config/rest.php`). يقوم هذا الملف بتكوين سلوك مكتبة REST_Controller (مكتبة PHP شائعة لبناء واجهات برمجة تطبيقات RESTful في CodeIgniter)، مثل مكتبة Phil Sturgeon's REST (التي يتم الآن صيانتها كجزء من إطار عمل CodeIgniter في بعض الإصدارات).

سأشرح:
- ما الذي تفعله المكتبة والمتطلبات الأساسية الرئيسية.
- كيفية إعداده واستخدامه.
- خيارات التكوين الرئيسية من ملفك (مع أمثلة).
- مثال بسيط للاستخدام.
- نصائح للأخطاء الشائعة والأمان.

إذا كان سؤالك يتعلق بجانب محدد (مثل المصادقة أو الحدود)، يرجى التوضيح للحصول على نصائح أكثر استهدافًا!

### 1. **المتطلبات الأساسية والإعداد**
   - **ما هي؟** هذه هي مكتبة REST_Controller لـ CodeIgniter (إطار عمل PHP). تتيح لك بناء واجهات برمجة تطبيقات RESTful (على سبيل المثال، نقاط النهاية التي تستجيب بـ JSON/XML على طلبات GET/POST) من خلال توسيع وحدات التحكم الخاصة بك من `REST_Controller`. يتحكم ملف التكوين الخاص بك في الإعدادات العامة مثل المصادقة، وتنسيقات الاستجابة، والحد من معدل الطلبات، والأمان.

   - **المتطلبات:**
     - CodeIgniter 3.x (أو إصدار متوافق؛ هذا التكوين مخصص للإصدارات الأقدم حول 3.x).
     - قم بتثبيت مكتبة REST_Controller إذا لم تكن موجودة بالفعل في تثبيت CodeIgniter الخاص بك (يمكنك تنزيلها من GitHub: `chriskacerguis/codeigniter-restserver`). ضع ملفات المكتبة في `application/libraries/` وقم بتحميلها تلقائيًا في `application/config/autoload.php`:
       ```php
       $autoload['libraries'] = ['rest_controller'];
       ```
     - إعداد قاعدة البيانات (اختياري؛ مطلوب لميزات مثل مفاتيح API، والتسجيل، أو الحدود). قم بتشغيل مخططات SQL المقدمة في تعليقات التكوين (على سبيل المثال، للجداول مثل `keys`, `logs`, `access`, `limits`).
     - تمكين عناوين URL المُنسقة في CodeIgniter (`application/config/routes.php`) لنقاط نهاية API نظيفة مثل `/api/users`.
     - يجب وضع ملف التكوين `rest.php` الخاص بك في `application/config/` وتحميله تلقائيًا في `application/config/autoload.php`:
       ```php
       $autoload['config'] = ['rest'];
       ```

   - **خطوات التثبيت الأساسية:**
     1. قم بتنزيل CodeIgniter وفك ضغطه.
     2. أضف ملفات مكتبة REST_Controller.
     3. انسخ ملف `rest.php` المقدم إلى `application/config/`.
     4. قم بإعداد المسارات في `routes.php` (على سبيل المثال، `$route['api/(:any)'] = 'api/$1';` لتعيين `/api/users` إلى وحدة تحكم).
     5. أنشئ وحدات تحكم API (انظر المثال أدناه).
     6. اختبر باستخدام أداة مثل Postman أو curl.

### 2. **خيارات التكوين الرئيسية**
سألخص الإعدادات الرئيسية من ملف التكوين الخاص بك، مجمعة حسب الغرض. تتحكم هذه في السلوك العام. يمكنك تعديلها لتناسب احتياجاتك (على سبيل المثال، تمكين HTTPS أو تغيير التنسيقات الافتراضية).

- **البروتوكول والإخراج:**
  - `$config['force_https'] = FALSE;`: يجبر جميع استدعاءات API على استخدام HTTPS. اضبط على `TRUE` لأمان بيئة الإنتاج.
  - `$config['rest_default_format'] = 'json';`: تنسيق الاستجابة الافتراضي (الخيارات: json, xml, csv، إلخ). يمكن للطلبات التجاوز عبر URL (على سبيل المثال، `/api/users.format=xml`).
  - `$config['rest_supported_formats']`: قائمة بالتنسيقات المسموح بها. قم بإزالة التنسيقات غير المرغوب فيها للأمان.
  - `$config['rest_ignore_http_accept'] = FALSE;`: تجاهل رؤوس HTTP Accept الخاصة بالعميل لتسريع الاستجابات (مفيد إذا كنت تستخدم دائمًا `$this->rest_format` في الكود).

- **المصادقة (الأمان):**
  - `$config['rest_auth'] = FALSE;`: وضع المصادقة الرئيسي. الخيارات:
    - `FALSE`: لا توجد مصادقة مطلوبة.
    - `'basic'`: HTTP Basic Auth (اسم المستخدم/كلمة المرور في رؤوس base64).
    - `'digest'`: مصادقة مشفرة أكثر أمانًا.
    - `'session'`: التحقق من متغير جلسة PHP.
  - `$config['auth_source'] = 'ldap';`: مكان التحقق من بيانات الاعتماد (على سبيل المثال، مصفوفة التكوين، LDAP، مكتبة مخصصة).
  - `$config['rest_valid_logins'] = ['admin' => '1234'];`: مصفوفة بسيطة لاسم المستخدم/كلمة المرور (يتم تجاهلها إذا كنت تستخدم LDAP).
  - `$config['auth_override_class_method']`: تجاوز المصادقة لوحدات تحكم أو طرق محددة (على سبيل المثال، `'users' => 'view' => 'basic'`).
  - `$config['auth_library_class/function']`: إذا كنت تستخدم مكتبة مخصصة، فحدد الفئة/الطريقة للتحقق.
  - ضوابط IP:
    - `$config['rest_ip_whitelist_enabled/blacklist_enabled']`: التصفية الأساسية لـ IP على API الخاص بك.
    - مفيد لتقييد الوصول (على سبيل المثال، قائمة IPs المسموح بها لتطبيقك).

- **مفاتيح API (طبقة أمان اختيارية):**
  - `$config['rest_enable_keys'] = FALSE;`: يمكّن التحقق من مفتاح API (المخزن في جدول قاعدة البيانات `keys`). يجب على العملاء إرسال المفاتيح في الرؤوس (على سبيل المثال، `X-API-KEY`).
  - `$config['rest_key_column/name/length']`: تخصيص حقول المفتاح واسم الرأس.
  - زوّد مع `$config['rest_enable_access']` لتقييد المفاتيح لوحدات تحكم أو طرق محددة.

- **التسجيل والحدود:**
  - `$config['rest_enable_logging/limits'] = FALSE;`: تمكين التسجيل في قاعدة البيانات للطلبات (URI، المعلمات، إلخ) أو الحد من معدل الطلبات (على سبيل المثال، X استدعاء في الساعة لكل مفتاح).
  - الجداول: `logs`, `limits` (شغّل SQL الموجود في التعليقات لإنشائها).
  - `$config['rest_limits_method']`: كيفية تطبيق الحدود (حسب مفتاح API، URL، إلخ).
  - تخصيص لكل طريقة في وحدات التحكم (على سبيل المثال، `$this->method['get']['limit'] = 100;`).

- **أخرى:**
  - `$config['rest_ajax_only'] = FALSE;`: تقييد على طلبات AJAX فقط (يعيد خطأ 505 بخلاف ذلك).
  - `$config['rest_language'] = 'english';`: اللغة لرسائل الخطأ.

للتعديل: قم بتحرير `rest.php` وأعد تشغيل تطبيقك. اختبر التغييرات بعناية!

### 3. **كيفية استخدامه: الاستخدام خطوة بخطوة**
بمجرد الإعداد، قم بإنشاء نقاط نهاية API عن طريق بناء وحدات تحكم تُوسع `REST_Controller`. فيما يلي عملية عالية المستوى:

1. **إنشاء وحدة تحكم:**
   - في `application/controllers/`، أنشئ `Api.php` (أو على سبيل المثال، `Users.php` لمورد محدد):
     ```php
     <?php
     defined('BASEPATH') OR exit('No direct script access allowed');
     require_once(APPPATH . 'libraries/REST_Controller.php');

     class Api extends REST_Controller {
         public function __construct() {
             parent::__construct();
             // اختياري: تعيين المصادقة، الحدود لكل طريقة
             $this->load->database();
             $this->method['index_get']['limit'] = 100; // 100 طلب/ساعة
         }

         // GET /api
         public function index_get() {
             $data = ['message' => 'مرحبًا بك في API', 'status' => 'success'];
             $this->response($data, REST_Controller::HTTP_OK);
         }

         // POST /api/users
         public function users_post() {
             $data = $this->input->post(); // الحصول على بيانات POST
             if (empty($data['name'])) {
                 $this->response(['error' => 'الاسم مطلوب'], REST_Controller::HTTP_BAD_REQUEST);
             }
             // المعالجة (على سبيل المثال، إدخال في قاعدة البيانات)
             $this->response(['message' => 'تم إنشاء المستخدم'], REST_Controller::HTTP_CREATED);
         }

         // PUT /api/users/{id}
         public function users_put($id) {
             $data = $this->put(); // الحصول على بيانات PUT
             // تحديث المستخدم بالمعرف $id
             $this->response(['message' => 'تم تحديث المستخدم'], REST_Controller::HTTP_OK);
         }

         // إلخ لـ DELETE
     }
     ```

2. **إرسال الطلبات:**
   - استخدم أي عميل HTTP:
     - GET: `curl http://yourdomain.com/api` → يُرجع JSON {"message": "مرحبًا بك في API", "status": "success"}
     - POST: `curl -X POST http://yourdomain.com/api/users -d "name=John"` → ينشئ مستخدمًا.
   - قم بتضمين الرؤوس إذا كنت تستخدم المصادقة/المفاتيح (على سبيل المثال، `Authorization: Basic base64(user:pass)` أو `X-API-KEY: yourkey`).

3. **الاختبار والتصحيح:**
   - تحقق من سجلات CodeIgniter للبحث عن الأخطاء.
   - إذا فشلت المصادقة، تأكد من تعيين بيانات الاعتماد بشكل صحيح.
   - للحدود/التسجيل، استعلم عن جداول قاعدة البيانات الخاصة بك.

### 4. **نصائح شائعة وأفضل الممارسات**
- **الأمان:** استخدم دائمًا HTTPS في بيئة الإنتاج (`force_https = TRUE`). مكّن المفاتيح إذا كنت تعرضها للعملاء الخارجيين. قم بتنقية المدخلات لمنع حقن SQL.
- **الأخطاء:** تتضمن الاستجابات حقول `status` و `error` (قابلة للتخصيص في التكوين). استخدم أداة Profiler الخاصة بـ CodeIgniter للتصحيح.
- **الأداء:** إذا تم تمكين التسجيل/الحدود، ستتعامل قاعدة البيانات مع الاستعلامات — راقب الأداء البطيء.
- **الترقية:** هذا التكوين مخصص لإصدارات CodeIgniter الأقدم. بالنسبة لـ CI 4، استخدم موارد API المدمجة (قد يحتاج هذا الإعداد إلى تعديلات).
- **استكشاف الأخطاء وإصلاحها:**
  - "لا توجد استجابة"؟ تحقق من المسارات، والتحميل التلقائي، ومسارات المكتبة.
  - مشاكل في المصادقة؟ تحقق من `$auth_source` وبيانات الاعتماد.
  - أخطاء في التنسيق؟ تأكد من أن تنسيقك موجود في `rest_supported_formats`.
- **الموارد:** المستندات على codeigniter-restserver.org. للترقية إلى CI4، راجع المستندات الرسمية.

إذا لم يُجب هذا على سؤالك بالضبط أو كنت بحاجة إلى كود لحالة استخدام محددة (على سبيل المثال، تمكين OAuth)، قدم المزيد من التفاصيل!