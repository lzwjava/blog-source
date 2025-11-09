---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: دليل تهيئة مُنقّح CodeIgniter
translated: true
type: note
---

### فهم تكوين أداة Profiler في CodeIgniter

المقتطف الذي قدمته يبدو أنه الرأس والتعليقات من ملف `config/profiler.php` في CodeIgniter (يوجد عادةً في `application/config/profiler.php`). يُستخدم هذا الملف لتكوين **أداة Profiler**، وهي أداة مدمجة في CodeIgniter لتصحيح الأخطاء وقياس أداء تطبيقك. تتيح لك عرض (أو إخفاء) أقسام مختلفة من البيانات في نهاية تحميل الصفحة، مثل أوقات التنفيذ واستعلامات قاعدة البيانات والفئات التي تم تحميلها.

المقتطف الذي شاركته هو مجرد الرأس—وهو قياسي لجميع ملفات التكوين في CodeIgniter—مع رابط لدليل المستخدم الرسمي (على الرغم من ملاحظة أن وثائق CodeIgniter 3 قد تكون أكثر صلة إذا كنت تستخدم ذلك الإصدار، حيث أن CI 4 لديه بعض الاختلافات). أدناه، سأشرح **كيفية استخدام وتكوين أداة Profiler** في CodeIgniter خطوة بخطوة، بما في ذلك مثال كامل لملف التكوين الكامل.

#### الخطوة 1: المتطلبات الأساسية
- **إصدار CodeIgniter**: ينطبق هذا على إصدارات CI 2.x و 3.x. إذا كنت تستخدم CI 4، يتم الوصول إلى أداة Profiler بشكل مختلف عبر شريط أدوات Debug في `application/Config/Toolbar.php`.
- **البيئة**: أداة Profiler مخصصة **للتطوير فقط** (وليس للإنتاج، لأنها تعرض بيانات حساسة). قم بتمكينها عبر ملف التكوين.
- **كيفية عملها**: بمجرد التمكين، تُلحق أداة Profiler لوحة تصحيح أخطاء قابلة للطي في أسفل صفحاتك، تعرض مقاييس مثل المعايير المرجعية والاستعلامات وبيانات POST. لا تتطلب تشغيل كود مخصص—فهي تلقائية بعد الإعداد.

#### الخطوة 2: كيفية تمكين أداة Profiler
1. **تحديد موقع ملف التكوين**:
   - في مشروعك، انتقل إلى `application/config/profiler.php`.
   - إذا كان الملف غير موجود، قم بإنشائه بناءً على القالب الافتراضي.

2. **التمكين بشكل عام**:
   - افتح `application/config/profiler.php` وعيّن `$config['enable_profiler'] = TRUE;`.
   - سيؤدي هذا إلى تمكين أداة Profiler لجميع الطلبات (يمكنك تمكينها/تعطيلها بشكل شرطي لاحقًا في المتحكمات).

3. **مثال كامل لملف التكوين**:
   بناءً على بنية CI القياسية، إليك الشكل النموذجي الكامل لملف `config/profiler.php` (يمكنك نسخ هذا ولصقه في ملفك إذا كان مفقودًا). المقتطف الذي قدمته هو الجزء العلوي فقط؛ يليه مصفوفة التكوين.

   ```php
   <?php
   defined('BASEPATH') OR exit('No direct script access allowed');

   /*
   | -------------------------------------------------------------------------
   | Profiler Sections
   | -------------------------------------------------------------------------
   | This file lets you determine whether or not various sections of Profiler
   | data are displayed when the Profiler is enabled.
   | Please see the user guide for info:
   |
   |    http://codeigniter.com/user_guide/general/profiling.html
   |
   */

   $config['enable_profiler'] = TRUE;  // Set to TRUE to enable, FALSE to disable globally

   // Configurable sections (set to TRUE to show, FALSE to hide)
   $config['config']         = TRUE;   // Displays all config variables
   $config['queries']        = TRUE;   // Displays all executed database queries and their execution time
   $config['get']            = TRUE;   // Displays all GET data passed to controllers
   $config['post']           = TRUE;   // Displays all POST data passed to controllers
   $config['uri_string']     = TRUE;   // Displays the requested URI string
   $config['controller_info'] = TRUE;  // Displays controller and method information
   $config['models']         = TRUE;   // Displays details about loaded models
   $config['libraries']      = TRUE;   // Displays details about loaded libraries
   $config['helpers']        = TRUE;   // Displays details about loaded helpers
   $config['memory_usage']   = TRUE;   // Shows memory usage
   $config['elapsed_time']   = TRUE;   // Shows total execution time
   $config['benchmarks']     = TRUE;   // Shows benchmark data
   $config['http_headers']   = TRUE;   // Displays HTTP headers
   $config['session_data']   = TRUE;   // Displays session data

   /* End of file profiler.php */
   /* Location: ./application/config/profiler.php */
   ```

   - **الإعدادات الرئيسية**:
     - `$config['enable_profiler']`: المفتاح الرئيسي.
     - كل قسم (مثل `config['queries']`) يتحكم في الرؤية. عيّن القيمة إلى `TRUE`/`FALSE` بناءً على ما تريد تصحيحه.

4. **التمكين الشرطي (اختياري)**:
   - ليس عليك تمكينه بشكل عام. في المتحكم، يمكنك استخدام:
     ```php
     $this->output->enable_profiler(TRUE);  // Enable for this specific method/request
     $this->output->enable_profiler(FALSE); // Disable
     ```
   - يتجاوز هذا التكوين العام لتلك الصفحة.

#### الخطوة 3: كيفية استخدام أداة Profiler عمليًا
1. **الوصول إلى المخرجات**:
   - قم بتحميل أي صفحة في تطبيقك (مثل طريقة في المتحكم).
   - انتقل إلى الأسفل—ستظهر أداة Profiler كصندوق قابل للطي يحتوي على أقسام مثل "Elapsed Time," و "Database Queries," إلخ.
   - انقر على "Close" أو "Open" للتبديل بين إظهارها وإخفائها.

2. **ما يظهره كل قسم**:
   - **Benchmarks**: أوقات وحدة المعالجة المركزية لأجزاء مختلفة من الكود الخاص بك (مفيد للتحسين).
   - **Queries**: جميع استعلامات SQL التي تم تنفيذها، بما في ذلك أوقات التنفيذ والأخطاء (رائع لتصحيح أخطاء قاعدة البيانات).
   - **POST/GET**: بيانات النموذج المُرسلة، مفيدة للتحقق من صحة النماذج.
   - **Memory Usage**: مقدار ذاكرة الوصول العشوائي التي استخدمها السكريبت (مراقبة التسريبات).
   - مثال: إذا كانت الصفحة بطيئة، قم بتمكين `benchmarks` و `queries` لتحديد الاختناقات.

3. **المعايير المرجعية المخصصة**:
   - أضف علامات مخصصة في الكود الخاص بك لتوقيت كتل محددة:
     ```php
     $this->benchmark->mark('query_start');  // Start timer
     // Your code here (e.g., a foreach loop or DB query)
     $this->benchmark->mark('query_end');    // End timer
     ```
   - سيظهر هذا في قسم "Benchmarks" تلقائيًا.

4. **مثال للاستخدام في المتحكم**:
   لنفترض أن لديك طريقة في المتحكم بطيئة—يمكنك تمكين Profiler هناك للتصحيح:
   ```php
   class Example extends CI_Controller {
       public function index() {
           $this->load->database();
           $this->output->enable_profiler(TRUE);  // Enable for this page only

           // Your logic here, e.g., fetching data
           $data['results'] = $this->db->get('users')->result();
           $this->load->view('example_view', $data);
       }
   }
   ```
   - بعد تحميل هذه الصفحة، تحقق من الأسفل لبيانات Profiler.

#### الخطوة 4: نصائح واستكشاف الأخطاء وإصلاحها
- **ملاحظة أمنية**: لا تقم أبدًا بالتمكين في بيئة الإنتاج—عطّل عبر `$config['enable_profiler'] = FALSE;` أو باستخدام متغيرات البيئة (مثلًا، عبر Hooks لبيئات التطوير DEV).
- **المشاكل الشائعة**:
  - لا تظهر؟ تأكد من أن `$config['enable_profiler']` هي TRUE وأنك لست على خادم إنتاج.
  - أخطاء؟ تحقق مما إذا كانت ملفات `view` الخاصة بك تحتوي على وسوم إغلاق صحيحة (مثل `</html>`).
- **متقدم**: لمزيد من التحكم، استخدم **Hooks** في `config/hooks.php` لتمكينها شرطيًا بناءً على عنوان IP أو البيئة.
- **الموارد**:
  - الوثائق الرسمية: [CodeIgniter 3 Profiling](https://codeigniter.com/user_guide/general/profiling.html) أو [CI 4 Debugging](https://codeigniter.com/user_guide/testing/debugging.html).
  - إذا كنت تستخدم CI 4، انتقل إلى شريط أدوات Debug بدلاً من ذلك (يتم تمكينه في `Toolbar.php`).

إذا كان هذا لا يتطابق مع ما تقصده (مثلًا، إذا كان لديك تكوين أو خطأ مختلف)، فقدم المزيد من السياق مثل الكود الكامل أو إصدار CI الخاص بك، وسأقوم بتعديل الإجابة!