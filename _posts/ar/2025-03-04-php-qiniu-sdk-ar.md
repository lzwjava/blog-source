---
audio: false
generated: true
lang: ar
layout: post
title: SDK Qiniu بـ PHP
translated: true
type: note
---

لاستخدام `"qiniu/php-sdk": "^7.0"` في PHP، ستحتاج إلى دمج Qiniu PHP SDK في مشروعك. يتيح لك هذا SDK التفاعل مع خدمات تخزين سحابة Qiniu، مثل رفع الملفات وإدارة الـ Buckets والمزيد. فيما يلي دليل خطوة بخطوة لمساعدتك على البدء:

---

### 1. تثبيت Qiniu PHP SDK
الطريقة الموصى بها لتثبيت SDK هي عبر Composer، مدير الاعتماديات (Dependencies) لـ PHP. تأكد من تثبيت Composer على نظامك.

#### الخطوات:
- افتح الطرفية (Terminal) وانتقل إلى دليل مشروعك.
- شغِّل الأمر التالي لإضافة Qiniu PHP SDK (الإصدار 7.x) إلى مشروعك:
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- سيقوم Composer بتنزيل SDK والاعتماديات الخاصة به في دليل `vendor/` وتوليد ملف التحميل التلقائي (autoload).

إذا لم يكن Composer مثبتًا لديك، يمكنك تنزيله من [getcomposer.org](https://getcomposer.org/).

---

### 2. إعداد مشروعك
بعد التثبيت، تحتاج إلى تضمين أداة التحميل التلقائي (autoloader) في سكريبت PHP الخاص بك لاستخدام فئات SDK.

#### مثال:
أنشئ ملف PHP (مثل `index.php`) في دليل مشروعك وأضف السطر التالي في الأعلى:
```php
require_once 'vendor/autoload.php';
```

هذا يضمن تحميل فئات SDK تلقائيًا عند الحاجة.

---

### 3. تكوين المصادقة (Authentication)
لاستخدام Qiniu SDK، ستحتاج إلى `AccessKey` و `SecretKey` الخاصين بـ Qiniu، ويمكنك الحصول عليهما من لوحة تحكم حساب Qiniu الخاص بك.

#### مثال:
```php
use Qiniu\Auth;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

استبدل `'YOUR_ACCESS_KEY'` و `'YOUR_SECRET_KEY'` ببيانات الاعتماد الفعلية الخاصة بك.

---

### 4. الاستخدام الأساسي: رفع ملف
إحدى المهام الشائعة مع Qiniu SDK هي رفع الملفات إلى الـ Bucket. إليك مثالاً لكيفية رفع ملف محلي.

#### مثال:
```php
use Qiniu\Storage\UploadManager;

$bucket = 'YOUR_BUCKET_NAME'; // استبدل باسم الـ Bucket الخاص بك في Qiniu
$filePath = '/path/to/your/file.txt'; // المسار إلى الملف الذي تريد رفعه
$key = 'file.txt'; // اسم الملف في تخزين Qiniu (يمكن أن يكون null لاستخدام اسم الملف الأصلي)

$token = $auth->uploadToken($bucket); // توليد رمز الرفع (Upload Token)
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "Upload failed: " . $error->message();
} else {
    echo "Upload successful! File hash: " . $ret['hash'];
}
```

- `$bucket`: اسم الـ Bucket الخاص بك في Qiniu.
- `$filePath`: المسار المحلي للملف الذي تريد رفعه.
- `$key`: مفتاح الملف (الاسم) الذي سيخزن به في Qiniu. إذا تم تعيينه إلى `null`، سيقوم Qiniu بتوليد مفتاح بناءً على الـ Hash الخاص بالملف.
- `$token`: رمز رفع يتم توليده باستخدام بيانات اعتمادك واسم الـ Bucket.
- ترجع الدالة `putFile` مصفوفة: `$ret` (معلومات النجاح) و `$error` (معلومات الخطأ، إن وجدت).

---

### 5. ميزات إضافية
يوفر Qiniu PHP SDK العديد من الوظائف الأخرى، مثل:
- **إدارة الـ Buckets**: استخدم `Qiniu\Storage\BucketManager` لسرد الملفات أو حذفها أو إدارة إعدادات الـ Bucket.
- **عمليات الملفات**: نسخ أو نقل أو حذف الملفات في الـ Bucket الخاص بك.
- **معالجة الصور**: توليد عناوين URL للصور المعاد تحجيمها أو المُنسقة.

#### مثال: سرد الملفات في الـ Bucket
```php
use Qiniu\Storage\BucketManager;

$bucketMgr = new BucketManager($auth);
list($ret, $error) = $bucketMgr->listFiles($bucket);

if ($error !== null) {
    echo "Error: " . $error->message();
} else {
    echo "Files in bucket:\n";
    foreach ($ret['items'] as $item) {
        echo $item['key'] . "\n";
    }
}
```

---

### 6. معالجة الأخطاء
تحقق دائمًا من المتغير `$error` بعد عمليات SDK. إذا فشلت العملية، سيحتوي `$error` على تفاصيل حول ما حدث من خطأ.

#### مثال:
```php
if ($error !== null) {
    var_dump($error);
} else {
    var_dump($ret);
}
```

---

### 7. المتطلبات
- إصدار PHP: يدعم إصدار SDK `^7.0` إصدار PHP 5.3.3 وما أعلى (حتى PHP 8.x في الإصدارات اللاحقة).
- الامتدادات (Extensions): تأكد من تمكين امتدادات PHP `cURL` و `xml`، لأن SDK يتطلبها.

يمكنك التحقق من إصدار PHP والامتدادات باستخدام:
```bash
php -v
php -m
```

---

### 8. أين تذهب بعد ذلك
- **التوثيق (Documentation)**: لمزيد من التفاصيل، راجع [توثيق Qiniu PHP SDK الرسمي](https://developer.qiniu.com/kodo/sdk/php) أو [مستودع GitHub](https://github.com/qiniu/php-sdk).
- **الأمثلة**: تحقق من دليل `examples/` في مستودع GitHub لمزيد من حالات الاستخدام.
- **الدعم**: إذا واجهت مشاكل، قدّم تذكرة إلى دعم Qiniu (<support@qiniu.com>) أو اسأل في منتديات مجتمعهم.

---

### مثال كامل للكود
إليك سكريبتًا كاملاً لرفع ملف:
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
    echo "Upload failed: " . $error->message();
} else {
    echo "Upload successful! File hash: " . $ret['hash'];
}
```

استبدل القيم النائبة (`YOUR_ACCESS_KEY`, `YOUR_SECRET_KEY`, `YOUR_BUCKET_NAME`, `/path/to/your/file.txt`) ببياناتك الفعلية، وستكون جاهزًا!

دعني أعلم إذا كنت بحاجة إلى مساعدة في ميزة محددة!