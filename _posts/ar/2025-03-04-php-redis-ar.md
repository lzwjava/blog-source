---
audio: false
generated: true
lang: ar
layout: post
title: عميل ريديس لـ PHP
translated: true
type: note
---

لاستخدام مكتبة `"predis/predis": "1.1"` في PHP، فأنت تشير إلى عميل Redis لـ PHP يمكن تثبيته عبر Composer. إليك دليل خطوة بخطوة لإعداده واستخدامه في مشروع PHP الخاص بك:

---

### 1. **تثبيت Composer (إذا لم يكن مثبتًا بالفعل)**
إذا لم يكن لديك Composer مثبتًا، قم بتنزيله وتثبيته من [getcomposer.org](https://getcomposer.org/). إنه مدير تبعيات لـ PHP.

---

### 2. **إعداد مشروعك**
إذا لم يكن لديك مشروع بالفعل، قم بإنشاء دليل له:
```bash
mkdir my-redis-project
cd my-redis-project
```

---

### 3. **إضافة Predis إلى مشروعك**
قم بتشغيل أمر Composer التالي لتثبيت الإصدار 1.1 من Predis:
```bash
composer require predis/predis:1.1
```
سيؤدي هذا إلى تنزيل Predis الإصدار 1.1 وإنشاء ملف `composer.json` (ودليل `vendor` يحتوي على المكتبة).

بدلاً من ذلك، إذا كان لديك ملف `composer.json` بالفعل، يمكنك إضافة هذا السطر إليه يدويًا:
```json
{
    "require": {
        "predis/predis": "1.1"
    }
}
```
ثم قم بتشغيل:
```bash
composer install
```

---

### 4. **تضمين Autoloader**
في سكريبت PHP الخاص بك، قم بتضمين autoloader الخاص بـ Composer لتحميل Predis:
```php
require 'vendor/autoload.php';
```

---

### 5. **مثال على الاستخدام الأساسي**
إليك مثالاً بسيطًا لكيفية الاتصال بخادم Redis واستخدام Predis:

```php
<?php
require 'vendor/autoload.php';

use Predis\Client;

// إنشاء مثيل جديد لعميل Redis
$redis = new Client([
    'scheme' => 'tcp',
    'host'   => '127.0.0.1', // استبدلها باسم مضيف خادم Redis الخاص بك
    'port'   => 6379,        // منفذ Redis الافتراضي
]);

// تعيين زوج مفتاح-قيمة
$redis->set('mykey', 'Hello, Redis!');

// استرجاع القيمة
$value = $redis->get('mykey');
echo $value; // الناتج: Hello, Redis!

// مثال مع قائمة
$redis->lpush('mylist', 'item1');
$redis->lpush('mylist', 'item2');
$list = $redis->lrange('mylist', 0, -1);
print_r($list); // الناتج: Array ( [0] => item2 [1] => item1 )
?>
```

---

### 6. **خيارات التهيئة**
يمكنك تخصيص الاتصال عن طريق تمرير مصفوفة من الخيارات إلى منشئ `Client`. على سبيل المثال:
```php
$redis = new Client([
    'scheme' => 'tcp',
    'host'   => 'redis.example.com',
    'port'   => 6379,
    'password' => 'yourpassword', // إذا كانت المصادقة مطلوبة
    'database' => 0,              // حدد قاعدة بيانات Redis محددة
]);
```

---

### 7. **الأوامر الشائعة**
يدعم Predis معظم أوامر Redis مباشرة كطرق. إليك بعض الأمثلة:
- **Strings**: `set`, `get`, `incr`, `decr`
- **Lists**: `lpush`, `rpush`, `lpop`, `rpop`, `lrange`
- **Sets**: `sadd`, `smembers`, `srem`
- **Hashes**: `hset`, `hget`, `hgetall`

للحصول على قائمة كاملة، راجع [توثيق Predis](https://github.com/predis/predis) أو مرجع أوامر Redis.

---

### 8. **معالجة الأخطاء**
قم بتغليف استدعاءات Redis الخاصة بك في كتلة try-catch للتعامل مع أخطاء الاتصال أو وقت التشغيل المحتملة:
```php
try {
    $redis->set('test', 'value');
    echo $redis->get('test');
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
```

---

### 9. **المتطلبات الأساسية**
- تأكد من تشغيل خادم Redis (على سبيل المثال، محليًا عبر `redis-server` أو على مضيف بعيد).
- PHP 5.3.0 أو إصدار أحدث (Predis 1.1 متوافق مع إصدارات PHP القديمة، ولكن تحقق من بيئتك).

---

هذا كل شيء! أنت الآن جاهز لاستخدام Predis 1.1 في مشروع PHP الخاص بك. أعلمني إذا كنت بحاجة إلى مساعدة في عمليات Redis محددة أو استكشاف الأخطاء وإصلاحها!