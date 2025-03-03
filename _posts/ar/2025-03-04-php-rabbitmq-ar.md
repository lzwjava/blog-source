---
audio: false
generated: true
lang: ar
layout: post
title: استخدام RabbitMQ في PHP
translated: true
---

### النقاط الرئيسية
- يبدو أن استخدام "php-amqplib/php-amqplib" الإصدار 2.6.* يتطلب تثبيته عبر Composer وتتبع الخطوات الأساسية لإرسال واستقبال الرسائل مع RabbitMQ.
- يتضمن العملية إعداد اتصال، إعلان صف، واستخدام طرق مثل `basic_publish` لإرسال و `basic_consume` مع حلقة لاستقبال، والتي قد تختلف قليلاً عن الإصدارات الأحدث.
- تشير الأبحاث إلى أن عملية الاستهلاك في الإصدار 2.6.* تتطلب حلقة يدوية مع `wait()`، على عكس الإصدارات الأحدث التي قد تستخدم طريقة `consume()`.

---

### التثبيت والتكوين
لبدء العمل مع "php-amqplib/php-amqplib" الإصدار 2.6.*، قم بتثبيته أولاً باستخدام Composer من خلال تنفيذ:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

تأكد من تثبيت RabbitMQ وتفعيله على نظامك، عادةً ما يكون متاحًا في `localhost:5672` مع بيانات الدخول الافتراضية (`guest/guest`). قم بتعديل هذه الإعدادات إذا كان إعدادك مختلفًا.

### إرسال الرسائل
لإرسال رسالة، قم بإدراج الملفات PHP اللازمة وخلق اتصال:

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
```

أعلن صفًا ونشر رسالتك:

```php
$channel->queue_declare('hello', false, false, false, false);
$msg = new AMQPMessage('Hello World!');
$channel->basic_publish($msg, '', 'hello');
echo " [x] Sent 'Hello World!'\n";
```

أخيرًا، أغلق الاتصال:

```php
$channel->close();
$connection->close();
```

### استلام الرسائل
لاستلام الرسائل، قم بتكوينها بشكل مشابه ولكن حدد استدعاء للرسائل:

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
$channel->queue_declare('hello', false, false, false, false);

$callback = function ($msg) {
    echo ' [x] Received ', $msg->body, "\n";
};

$channel->basic_consume('hello', '', false, true, false, false, $callback);
while (count($channel->callbacks)) {
    $channel->wait();
}

$channel->close();
$connection->close();
```

لاحظ أن الإصدار 2.6.* يتطلب الحلقة مع `wait()` لاستمرار الاستهلاك، وهو تفصيل غير متوقع مقارنة بالإصدارات الأحدث التي قد تستخدم طريقة `consume()` أبسط.

---

### ملاحظة الاستطلاع: الاستخدام التفصيلي لـ "php-amqplib/php-amqplib" الإصدار 2.6.*

يوفر هذا القسم دليلًا شاملًا لاستخدام مكتبة "php-amqplib/php-amqplib"، بشكل خاص الإصدار 2.6.*، للتفاعل مع RabbitMQ، نظام صف الرسائل الشهير. تم استخلاص المعلومات من الوثائق الرسمية، الدروس التدريبية، والتفاصيل الخاصة بالإصدار، مما يضمن فهمًا شاملًا للمطورين.

#### الخلفية والسياق
"php-amqplib/php-amqplib" هي مكتبة PHP للتواصل مع RabbitMQ، تنفذ بروتوكول AMQP 0.9.1. الإصدار 2.6.* هو إصدار قديم، وقد تطورت المكتبة إلى الإصدار 3.x.x بحلول مارس 2025، ولكن فهم استخدامه في هذا الإصدار المحدد هو أمر حاسم للنظم القديمة أو متطلبات المشروع الخاصة. يتم الحفاظ على المكتبة من قبل المتطوعين بما في ذلك Ramūnas Dronga و Luke Bakken، مع مشاركة كبيرة من مهندسي VMware الذين يعملون على RabbitMQ ([GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib)).

تقدم دروس RabbitMQ، مثل تلك الموجودة على موقع RabbitMQ الرسمي، أمثلة يمكن تطبيقها بشكل عام ولكن قد تعكس الإصدارات الأحدث. بالنسبة للإصدار 2.6.*، يتطلب الأمر تعديلات، خاصة في عملية الاستهلاك، كما هو موضح أدناه.

#### عملية التثبيت
لبدء العمل، قم بتثبيت المكتبة باستخدام Composer، مدير التبعيات PHP. قم بتنفيد الأمر التالي في مجلد المشروع:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

يضمن هذا الأمر تحميل المكتبة وتكوينها للاستخدام، مع إدارة Composer للتبعيات. تأكد من تثبيت RabbitMQ وتفعيله، عادةً ما يكون متاحًا في `localhost:5672` مع بيانات الدخول الافتراضية (`guest/guest`). بالنسبة للإنتاج، قم بتعديل المضيف، الميناء، وبيانات الدخول حسب الحاجة، واستعرض [CloudAMQP PHP Documentation](https://www.cloudamqp.com/docs/php.html) لتكوين الموزع المحكم.

#### إرسال الرسائل: خطوة بخطوة
يشمل إرسال الرسائل إنشاء اتصال ونشر إلى صف. إليك العملية:

1. **إدراج الملفات المطلوبة:**
   استخدم Composer autoloader لإدراج المكتبة:

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   use PhpAmqpLib\Message\AMQPMessage;
   ```

2. **إنشاء اتصال وقناة:**
   قم بإنشاء اتصال إلى RabbitMQ وفتح قناة:

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

   تكون المعلمات المضيف، الميناء، اسم المستخدم، وكلمة المرور، مع الافتراضات كما هو موضح. بالنسبة للاتصالات SSL أو غيرها من الإعدادات، استعرض [RabbitMQ PHP Tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-php).

3. **إعلان صف ونشر:**
   اعلان صف لضمان وجوده، ثم نشر رسالة:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   $msg = new AMQPMessage('Hello World!');
   $channel->basic_publish($msg, '', 'hello');
   echo " [x] Sent 'Hello World!'\n";
   ```

   هنا، `queue_declare` يخلق صفًا باسم 'hello' مع الإعدادات الافتراضية (غير دائم، غير حصري، حذف تلقائي). `basic_publish` يرسل الرسالة إلى الصف.

4. **إغلاق الاتصال:**
   بعد إرسال، أغلق القناة والاتصال لتحرير الموارد:

   ```php
   $channel->close();
   $connection->close();
   ```

هذه العملية هي القياسية عبر الإصدارات، مع عدم وجود تغييرات كبيرة في سجل التغييرات للإصدار 2.6.* مقارنة بالإصدارات اللاحقة.

#### استلام الرسائل: التفاصيل الخاصة بالإصدار
يحتاج استلام الرسائل في الإصدار 2.6.* إلى انتباه خاص، حيث تختلف آلية الاستهلاك عن الإصدارات الأحدث. إليك العملية التفصيلية:

1. **إدراج الملفات المطلوبة:**
   مشابه لإرسال، إدراج autoloader والصفوف اللازمة:

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   ```

2. **إنشاء اتصال وقناة:**
   قم بإنشاء الاتصال والقناة كما سبق:

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

3. **إعلان صف:**
   تأكد من وجود الصف، متطابقًا مع إعلان المرسل:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   ```

4. **تعريف استدعاء:**
   قم بإنشاء استدعاء لتعامل مع الرسائل المستلمة:

   ```php
   $callback = function ($msg) {
       echo ' [x] Received ', $msg->body, "\n";
   };
   ```

   سيتم استدعاء هذه الوظيفة لكل رسالة، طباعة الجسم في هذا المثال.

5. **استهلاك الرسائل:**
   بالنسبة للإصدار 2.6.*، استخدم `basic_consume` لتسجيل الاستدعاء، ثم أدخل حلقة لاستمرار الاستهلاك:

   ```php
   $channel->basic_consume('hello', '', false, true, false, false, $callback);
   while (count($channel->callbacks)) {
       $channel->wait();
   }
   ```

   تأخذ طريقة `basic_consume` المعلمات لاسم الصف، علامة المستهلك، no-local، no-ack، exclusive، no-wait، والاستدعاء. تظل الحلقة مع `wait()` الاستهلاك يعمل، تحقق من الرسائل. هذا تفصيل مهم، حيث قد تستخدم الإصدارات الأحدث (مثل 3.2) طريقة `consume()`، والتي لم تكن متاحة في 2.6.* بناءً على مراجعة وثائق API.

6. **إغلاق الاتصال:**
   بعد الاستهلاك، أغلق الموارد:

   ```php
   $channel->close();
   $connection->close();
   ```

تفصيل غير متوقع هو الحاجة إلى الحلقة اليدوية في الإصدار 2.6.*، والتي قد تتطلب معالجة الأخطاء الإضافية للإنتاج، مثل استثناءات الاتصال.

#### استعراض الإصدارات
الإصدار 2.6.* جزء من الإصدارات القديمة، ولم يحدد سجل التغييرات ذلك بشكل صريح، ولكن الإصدارات من 2.5 إلى 2.7 تظهر تحسينات مثل دعم القلب وPHP 5.3. بالنسبة للرسائل الكبيرة، يدعم الإصدار 2.6.* `setBodySizeLimit` على القناة لتعامل مع حدود الذاكرة، تقطع الرسائل إذا لزم الأمر، مع التفاصيل في [GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib).

مقارنة بالإصدار 3.2، تشمل التغييرات دعم PHP 8 ووسائل جديدة مثل `consume()`، ولكن الوظيفة الأساسية لإرسال واستهلاك الأساسي تبقى مماثلة. يجب على المستخدمين اختبار التوافق، خاصة مع إصدارات PHP، حيث أن 2.6.* يدعم PHP 5.3 إلى 7.x، وفقًا لمدخلات سجل التغييرات.

#### حل المشاكل والتوصيات
- إذا فشل الإرسال، تحقق من سجلات RabbitMQ للحصول على إشعارات الموارد، مثل مساحة القرص أقل من 50 MB، وقم بتعديل الإعدادات عبر [RabbitMQ Configuration Guide](https://www.rabbitmq.com/configure.html#config-items).
- بالنسبة للاستهلاك، تأكد من تشغيل المستهلك بشكل مستمر؛ استخدم أدوات مثل Supervisor لتحويل إلى ديمون في الإنتاج.
- قم بتمرير الصفوف باستخدام `rabbitmqctl list_queues` في Linux أو `rabbitmqctl.bat list_queues` في Windows كمسؤول، وفقًا لـ [RabbitMQ Command Line Tools](https://www.rabbitmq.com/cli.html).

#### جدول: مقارنة الإصدارات للمethods الرئيسية

| Method             | سلوك الإصدار 2.6.*                          | سلوك الإصدار 3.2                          |
|--------------------|------------------------------------------------|----------------------------------------------|
| `basic_publish`    | قياسي، ينشر إلى الصف                          | غير متغير، نفس الاستخدام                        |
| `basic_consume`    | يتطلب حلقة مع `wait()` لاستهلاك         | مشابه، ولكن طريقة `consume()` متاحة     |
| `setBodySizeLimit` | مدعوم للرسائل الكبيرة، يقطع إذا تم تعيينه | مدعوم، نفس الوظيفة                |
| PHP Compatibility  | محتمل 5.3 إلى 7.x                               | يدعم PHP 7.x و 8.x                     |

يوضح هذا الجدول الفرق الرئيسي في الاستهلاك، وهو حاسم للمستخدمين في الإصدار 2.6.*.

#### الخاتمة
استخدام "php-amqplib/php-amqplib" الإصدار 2.6.* يتضمن تثبيت Composer القياسي، مع إرسال الرسائل عبر `basic_publish` واستقبالها عبر `basic_consume` مع حلقة يدوية. بينما مشابه للإصدارات الأحدث، تتطلب عملية الاستهلاك انتباهًا إضافيًا، مما يجعل من الضروري للمطورين اختبار وتعديل للنظم القديمة. للحصول على مزيد من التفاصيل، استعرض الدروس التدريبية الرسمية RabbitMQ ومخزن GitHub.