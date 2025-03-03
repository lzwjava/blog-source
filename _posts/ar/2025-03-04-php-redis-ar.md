---
audio: false
generated: true
lang: ar
layout: post
title: عامل Redis لـ PHP
translated: true
---

لاستخدام مكتبة `"predis/predis": "1.1"` في PHP، فإنك تتحدث عن عميل Redis لـ PHP يمكن تثبيته عبر Composer. إليك دليل خطوة بخطوة لتثبيته واستخدامه في مشروع PHP الخاص بك:

---

### 1. **تثبيت Composer (إذا لم يكن مثبتًا بالفعل)**
إذا لم يكن لديك Composer مثبتًا، قم بتنزيله وتثبيته من [getcomposer.org](https://getcomposer.org/). إنه مدير اعتمادات لـ PHP.

---

### 2. **إعداد مشروعك**
إذا لم يكن لديك مشروع، قم بإنشاء مجلد له:
```bash
mkdir my-redis-project
cd my-redis-project
```

---

### 3. **إضافة Predis إلى مشروعك**
قم بتنفيد الأمر التالي لـ Composer لتثبيت الإصدار 1.1 من Predis:
```bash
composer require predis/predis:1.1
```
سيقوم هذا الأمر بتنزيل Predis الإصدار 1.1 ويولّد ملف `composer.json` (و مجلد `vendor` مع المكتبة).

بدلاً من ذلك، إذا كان لديك ملف `composer.json` بالفعل، يمكنك إضافة السطر التالي إليه:
```json
{
    "require": {
        "predis/predis": "1.1"
    }
}
```
ثم قم بتنفيد الأمر التالي:
```bash
composer install
```

---

### 4. **تضمين ملف Autoloader**
في سكربت PHP الخاص بك، قم بتضمين ملف Autoloader لـ Composer لتحميل Predis:
```php
require 'vendor/autoload.php';
```

---

### 5. **مثال استخدام أساسي**
إليك مثال بسيط على كيفية الاتصال بخدمة Redis واستخدام Predis:

```php
<?php
require 'vendor/autoload.php';

use Predis\Client;

// إنشاء مثيل جديد لـ Redis
$redis = new Client([
    'scheme' => 'tcp',
    'host'   => '127.0.0.1', // استبدل بعنوان خادم Redis الخاص بك
    'port'   => 6379,        // الميناء الافتراضي لـ Redis
]);

// تعيين زوج مفتاح-قيمة
$redis->set('mykey', 'مرحبًا، Redis!');

// استرجاع القيمة
$value = $redis->get('mykey');
echo $value; // يخرج: مرحبا، Redis!

// مثال مع قائمة
$redis->lpush('mylist', 'item1');
$redis->lpush('mylist', 'item2');
$list = $redis->lrange('mylist', 0, -1);
print_r($list); // يخرج: Array ( [0] => item2 [1] => item1 )
?>
```

---

### 6. **خيارات التكوين**
يمكنك تخصيص الاتصال عن طريق تمرير مصفوفة من الخيارات إلى مصنع `Client`. على سبيل المثال:
```php
$redis = new Client([
    'scheme' => 'tcp',
    'host'   => 'redis.example.com',
    'port'   => 6379,
    'password' => 'yourpassword', // إذا كان مطلوبًا التحقق من الهوية
    'database' => 0,              // اختيار قاعدة بيانات Redis محددة
]);
```

---

### 7. **الأوامر الشائعة**
Predis يدعم معظم أوامر Redis مباشرة كطرق. إليك بعض الأمثلة:
- **السلاسل**: `set`, `get`, `incr`, `decr`
- **القوائم**: `lpush`, `rpush`, `lpop`, `rpop`, `lrange`
- **المجموعات**: `sadd`, `smembers`, `srem`
- **الهاشات**: `hset`, `hget`, `hgetall`

لجدول كامل، راجع [وثائق Predis](https://github.com/predis/predis) أو مرجع أوامر Redis.

---

### 8. **معالجة الأخطاء**
قم بتضمين استدعاءات Redis في كتلة try-catch لتعامل مع الأخطاء المحتملة للاتصال أو التشغيل:
```php
try {
    $redis->set('test', 'value');
    echo $redis->get('test');
} catch (Exception $e) {
    echo "خطأ: " . $e->getMessage();
}
```

---

### 9. **المتطلبات الأساسية**
- تأكد من تشغيل خادم Redis (على سبيل المثال، محليًا عبر `redis-server` أو على خادم بعيد).
- PHP 5.3.0 أو أعلى (Predis 1.1 متوافق مع إصدارات PHP القديمة، ولكن تحقق من بيئتك).

---

هذا هو كل شيء! الآن أنت مستعد لاستخدام Predis 1.1 في مشروع PHP الخاص بك. أخبرني إذا كنت تحتاج إلى مساعدة في عمليات Redis محددة أو حل مشاكل!