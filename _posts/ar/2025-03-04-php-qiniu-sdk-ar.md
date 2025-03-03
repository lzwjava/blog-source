---
audio: false
generated: true
lang: ar
layout: post
title: Qiniu PHP SDK
translated: true
---

لاستخدام `"qiniu/php-sdk": "^7.0"` في PHP، عليك دمج SDK PHP لـ Qiniu في مشروعك. يسمح هذا SDK لك بالتواصل مع خدمات تخزين السحاب Qiniu، مثل تحميل الملفات، إدارة الحاويات، وغيرها. أدناه دليل خطوة بخطوة للحصول على البدء:

---

### 1. تثبيت SDK PHP لـ Qiniu
الطريقة الموصى بها لتثبيت SDK هي عبر Composer، وهو مدير الاعتماديات لـ PHP. تأكد من أن Composer مثبت على نظامك.

#### الخطوات:
- افتح مستخدم الطرفية وقلب إلى مجلد المشروع.
- انفذ الأمر التالي لإضافة SDK PHP لـ Qiniu (الإصدار 7.x) إلى مشروعك:
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- سيقوم Composer بتنزيل SDK واعتمادياته إلى مجلد `vendor/` ويولد ملف تحميل تلقائي.

إذا لم يكن Composer مثبتًا، يمكنك تنزيله من [getcomposer.org](https://getcomposer.org/).

---

### 2. إعداد المشروع
بعد التثبيت، عليك تضمين ملف التحميل التلقائي في ملف PHP الخاص بك لاستخدام فئات SDK.

#### المثال:
إنشاء ملف PHP (مثل `index.php`) في مجلد المشروع وأضف السطر التالي في الأعلى:
```php
require_once 'vendor/autoload.php';
```

هذا يضمن تحميل فئات SDK تلقائيًا عند الحاجة.

---

### 3. إعداد التوثيق
لاستخدام SDK لـ Qiniu، تحتاج إلى `AccessKey` و `SecretKey` الخاصين بك، والتي يمكنك الحصول عليها من لوحة تحكم حساب Qiniu الخاص بك.

#### المثال:
```php
use Qiniu\Auth;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

قم بإستبدال `'YOUR_ACCESS_KEY'` و `'YOUR_SECRET_KEY'` بمعلومات الاعتماد الخاصة بك.

---

### 4. الاستخدام الأساسي: تحميل ملف
من أكثر المهام الشائعة مع SDK لـ Qiniu تحميل الملفات إلى حاوية. إليك مثال على كيفية تحميل ملف محلي.

#### المثال:
```php
use Qiniu\Storage\UploadManager;

$bucket = 'YOUR_BUCKET_NAME'; // استبدل باسم حاوية Qiniu الخاص بك
$filePath = '/path/to/your/file.txt'; // مسار الملف الذي تريد تحميله
$key = 'file.txt'; // اسم الملف في تخزين Qiniu (يمكن أن يكون `null` لاستخدام اسم الملف الأصلي)

$token = $auth->uploadToken($bucket); // إنشاء رمز تحميل
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "فشل التحميل: " . $error->message();
} else {
    echo "تم التحميل بنجاح! رمز الملف: " . $ret['hash'];
}
```

- `$bucket`: اسم حاوية Qiniu.
- `$filePath`: مسار الملف المحلي الذي تريد تحميله.
- `$key`: مفتاح الملف (الاسم) الذي سيتم تخزينه في Qiniu. إذا تم تعيينه إلى `null`، سيقوم Qiniu بإنشاء مفتاح بناءً على هاش الملف.
- `$token`: رمز تحميل تم إنشاؤه باستخدام معلومات الاعتماد واسم الحاوية.
- يرجع طريقة `putFile` مصفوفة: `$ret` (معلومات النجاح) و `$error` (معلومات الخطأ، إذا كان هناك).

---

### 5. الميزات الإضافية
يوفر SDK PHP لـ Qiniu العديد من الوظائف الأخرى، مثل:
- **إدارة الحاويات**: استخدم `Qiniu\Storage\BucketManager` لتسجيل الملفات، حذف الملفات، أو إدارة إعدادات الحاوية.
- **عمليات الملفات**: نسخ، نقل، أو حذف الملفات في حاوية.
- **معالجة الصور**: إنشاء روابط لمصغرات الصور أو الصور المصفوفة.

#### المثال: تسجيل الملفات في حاوية
```php
use Qiniu\Storage\BucketManager;

$bucketMgr = new BucketManager($auth);
list($ret, $error) = $bucketMgr->listFiles($bucket);

if ($error !== null) {
    echo "خطأ: " . $error->message();
} else {
    echo "الملفات في الحاوية:\n";
    foreach ($ret['items'] as $item) {
        echo $item['key'] . "\n";
    }
}
```

---

### 6. معالجة الأخطاء
تأكد دائمًا من متغير `$error` بعد عمليات SDK. إذا فشلت عملية، سيحتوي `$error` على تفاصيل حول ما حدث.

#### المثال:
```php
if ($error !== null) {
    var_dump($error);
} else {
    var_dump($ret);
}
```

---

### 7. المتطلبات
- إصدار PHP: يدعم إصدار SDK `^7.0` PHP 5.3.3 و أعلى (حتى PHP 8.x في الإصدارات اللاحقة).
- الإضافات: تأكد من تمكين الإضافات `cURL` و `xml` لـ PHP، حيث أنها مطلوبة من SDK.

يمكنك التحقق من إصدار PHP و الإضافات باستخدام:
```bash
php -v
php -m
```

---

### 8. إلى أين الآن
- **التوثيق**: للحصول على مزيد من التفاصيل، راجع [التوثيق الرسمي لـ SDK PHP لـ Qiniu](https://developer.qiniu.com/kodo/sdk/php) أو [مستودع GitHub](https://github.com/qiniu/php-sdk).
- **الأمثلة**: تحقق من مجلد `examples/` في مستودع GitHub للحصول على المزيد من الحالات.
- **الدعم**: إذا واجهت مشاكل، قم بإرسال تذكرة إلى دعم Qiniu (<support@qiniu.com>) أو اسأل في منتداهم.

---

### الكود الكامل
هنا هو نص كامل لتحميل ملف:
```php
<?php
require_once 'vendor/autoload.php';

use Qiniu\Auth;
use Qiniu\Storage\UploadManager;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';
$bucket = 'YOUR_BUCKET_NAME';
$filePath = '/path/to/your/file.txt';
$key = 'file.txt';

$auth = new Auth($accessKey, $secretKey);
$token = $auth->uploadToken($bucket);
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "فشل التحميل: " . $error->message();
} else {
    echo "تم التحميل بنجاح! رمز الملف: " . $ret['hash'];
}
```

قم بإستبدال القيم المؤقتة (`YOUR_ACCESS_KEY`, `YOUR_SECRET_KEY`, `YOUR_BUCKET_NAME`, `/path/to/your/file.txt`) بمعلوماتك الفعلية، وسوف تكون جاهزًا!