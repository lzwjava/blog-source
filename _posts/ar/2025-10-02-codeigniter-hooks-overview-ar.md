---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: نظرة عامة على خطافات كود إيجنايتر
translated: true
type: note
---

### ما هي الـ Hooks في CodeIgniter؟

الـ Hooks في CodeIgniter هي وسيلة لتمديد وظائف الإطار دون تعديل ملفاته الأساسية. تسمح لك بتشغيل كود مخصص في نقاط محددة خلال دورة التنفيذ، مثل قبل أو بعد تحميل المتحكمات، أو تجاوز الإخراج، أو التخزين المؤقت. هذا يحافظ على قابلية التحديث من خلال فصل الكود الخاص بك عن قاعدة الكود الرسمية.

يتم تعريف الـ Hooks في `application/config/hooks.php` وتمكينها في `application/config/config.php` عن طريق تعيين `$config['enable_hooks'] = TRUE;`.

### تمكين الـ Hooks

1. افتح ملف `application/config/config.php`.
2. عيّن متغير الإعدادات:
   ```php
   $config['enable_hooks'] = TRUE;
   ```
   هذا يخبر CodeIgniter بالتحقق من ملف الـ Hooks وتنفيذه.

### تعريف الـ Hooks

يتم تكوين الـ Hooks كمصفوفة من المصفوفات في `application/config/hooks.php`. كل مصفوفة خطاف تحدد:
- `class`: (مطلوب) اسم الفئة (يجب أن يطابق اسم الملف).
- `function`: (مطلوب) اسم الدالة في الفئة.
- `filename`: (مطلوب) اسم ملف الفئة (بدون .php).
- `filepath`: (اختياري) مسار المجلد إلى الملف، الافتراضي هو `application/hooks/`.
- `params`: (اختياري) مصفوفة من المعاملات لتمريرها إلى الدالة.

ضع فئات الـ Hooks الخاصة بك في `application/hooks/`.

### نقاط الـ Hook

يوفر CodeIgniter هذه النقاط المحددة مسبقًا حيث يمكن للخطافات التنفيذ:
- **pre_system**: يعمل قبل تحميل النظام (لم ينفذ أي شيء آخر بعد).
- **pre_controller**: يعمل مباشرة قبل استدعاء المتحكم.
- **post_controller_constructor**: يعمل بعد إنشاء نسخة من المتحكم ولكن قبل تنفيذ دوالها.
- **post_controller**: يعمل بعد انتهاء المتحكم.
- **display_override**: يعمل بدلاً من إخراج المحتوى إلى المتصفح (يتجاوز _display create/exit controller file).
- **cache_override**: يعمل بدلاً من تحميل ذاكرة التخزين المؤقت (يتجاوز _display the cache).
- **post_system**: يعمل بعد إرسال صفحة الويب بالكامل إلى المتصفح.

### مثال للاستخدام

لنفترض أنك تريد تسجيل كل طلب قبل تشغيل المتحكم. أنشئ خطافًا لـ `pre_controller`.

1. أنشئ الملف `application/hooks/my_hook.php`:
   ```php
   <?php
   class My_hook {
       public function log_request() {
           // مثال: التسجيل في ملف أو قاعدة بيانات
           log_message('info', 'Controller about to be called: ' . $this->uri->uri_string());
       }
   }
   ```

2. في `application/config/hooks.php`، أضف:
   ```php
   $hook['pre_controller'] = array(
       'class' => 'My_hook',
       'function' => 'log_request',
       'filename' => 'my_hook.php',
       'filepath' => 'hooks', // اختياري، الافتراضي هو application/hooks/
       'params' => array() // معاملات اختيارية
   );
   ```

الآن، في كل مرة يكون المتحكم على وشك التشغيل، سيتم تنفيذ `log_request`.

### أفضل الممارسات
- استخدم الـ Hooks باعتدال؛ إذا أمكن، قم بتمديد المتحكمات أو استخدام المكتبات بدلاً من ذلك.
- اختبر الـ Hooks دائمًا في بيئة تطوير للتأكد من أنها لا تتعارض مع المنطق الأساسي.
- لمزيد من التفاصيل، راجع الدليل الرسمي لمستخدم CodeIgniter حول الـ Hooks.