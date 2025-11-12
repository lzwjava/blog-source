---
audio: false
generated: true
lang: ar
layout: post
title: استخدام رابيت إم كيو في بي إتش بي
translated: true
type: note
---

### النقاط الرئيسية
- يبدو أنه لاستخدام الإصدار 2.6.* من "php-amqplib/php-amqplib"، تحتاج إلى تثبيته عبر Composer واتباع الخطوات الأساسية لإرسال واستقبال الرسائل مع RabbitMQ.
- تتضمن العملية إعداد اتصال، وتصريح قائمة انتظار، واستخدام طرق مثل `basic_publish` للإرسال و `basic_consume` مع حلقة للاستقبال، والتي قد تختلف قليلاً عن الإصدارات الأحدث.
- تشير الأبحاث إلى أنه بالنسبة للإصدار 2.6.*، تتطلب عملية الاستهلاك حلقة يدوية باستخدام `wait()`، على عكس الإصدارات الأحدث التي قد تستخدم طريقة `consume()`.

---

### التثبيت والإعداد
للبدء مع الإصدار 2.6.* من "php-amqplib/php-amqplib"، قم أولاً بتثبيته باستخدام Composer عن طريق تشغيل:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

تأكد من تثبيت RabbitMQ وتشغيله على نظامك، عادةً ما يمكن الوصول إليه على `localhost:5672` باستخدام بيانات الاعتماد الافتراضية (`guest/guest`). قم بتعديل هذه الإعدادات إذا كان إعدادك مختلفاً.

### إرسال الرسائل
لإرسال رسالة، قم بتضمين ملفات PHP الضرورية وإنشاء اتصال:

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
```

قم بتصريح قائمة انتظار ونشر رسالتك:

```php
$channel->queue_declare('hello', false, false, false, false);
$msg = new AMQPMessage('Hello World!');
$channel->basic_publish($msg, '', 'hello');
echo " [x] Sent 'Hello World!'\n";
```

أخيراً، أغلق الاتصال:

```php
$channel->close();
$connection->close();
```

### استقبال الرسائل
للاستقبال، قم بالإعداد بشكل مشابه ولكن قم بتعريف رد اتصال لمعالجة الرسائل:

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

لاحظ أنه بالنسبة للإصدار 2.6.*، تحتاج إلى الحلقة مع `wait()` لمواصلة الاستهلاك، وهو تفصيل غير متوقع مقارنة بالإصدارات الأحدث التي قد تستخدم طريقة `consume()` أبسط.

---

### ملاحظة المسح: الاستخدام التفصيلي للإصدار 2.6.* من "php-amqplib/php-amqplib"

يقدم هذا القسم دليلاً شاملاً لاستخدام مكتبة "php-amqplib/php-amqplib"، تحديداً الإصدار 2.6.*، للتفاعل مع RabbitMQ، نظام قوائم انتظار الرسائل الشهير. تم استخلاص المعلومات من الوثائق الرسمية، والدروس التعليمية، والتفاصيل الخاصة بالإصدار، مما يضمن فهماً شاملاً للمطورين.

#### الخلفية والسياق
"php-amqplib/php-amqplib" هي مكتبة PHP للتواصل مع RabbitMQ، وتنفذ بروتوكول AMQP 0.9.1. الإصدار 2.6.* هو إصدار قديم، وبينما تطورت المكتبة إلى الإصدار 3.x.x بحلول مارس 2025، فإن فهم استخدامها في هذا الإصدار المحدد أمر بالغ الأهمية للأنظمة القديمة أو متطلبات المشاريع المحددة. يتم الحفاظ على المكتبة من قبل مساهمين بما في ذلك Ramūnas Dronga و Luke Bakken، بمشاركة كبيرة من مهندسي VMware العاملين على RabbitMQ ([GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib)).

الدروس التعليمية لـ RabbitMQ، مثل تلك الموجودة على الموقع الرسمي لـ RabbitMQ، تقدم أمثلة قابلة للتطبيق بشكل عام ولكنها قد تعكس إصدارات أحدث. بالنسبة للإصدار 2.6.*، من الضروري إجراء تعديلات، خاصة في عملية الاستهلاك، كما هو مفصل أدناه.

#### عملية التثبيت
للبدء، قم بتثبيت المكتبة باستخدام Composer، مدير تبعيات PHP. قم بتشغيل الأمر التالي في دليل مشروعك:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

يضمن هذا الأمر تنزيل المكتبة وتكوينها للاستخدام، مع إدارة Composer للتبعيات. تأكد من تثبيت وتشغيل RabbitMQ، عادةً ما يمكن الوصول إليه على `localhost:5672` باستخدام بيانات الاعتماد الافتراضية (`guest/guest`). للإنتاج، قم بتعديل المضيف، والمنفذ، وبيانات الاعتماد حسب الحاجة، واستشر [CloudAMQP PHP Documentation](https://www.cloudamqp.com/docs/php.html) لإعدادات الوسيط المدار.

#### إرسال الرسائل: خطوة بخطوة
يتضمن إرسال الرسائل إنشاء اتصال والنشر إلى قائمة انتظار. إليك العملية:

1. **تضمين الملفات المطلوبة:**
   استخدم أداة التحميل التلقائي لـ Composer لتضمين المكتبة:

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   use PhpAmqpLib\Message\AMQPMessage;
   ```

2. **إنشاء اتصال وقناة:**
   قم بتهيئة اتصال بـ RabbitMQ وافتح قناة:

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

   المعلمات هي المضيف، المنفذ، اسم المستخدم، وكلمة المرور، مع القيم الافتراضية كما هو موضح. لتكوينات SSL أو غيرها، راجع [RabbitMQ PHP Tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-php).

3. **تصريح قائمة الانتظار والنشر:**
   قم بتصريح قائمة انتظار لضمان وجودها، ثم انشر رسالة:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   $msg = new AMQPMessage('Hello World!');
   $channel->basic_publish($msg, '', 'hello');
   echo " [x] Sent 'Hello World!'\n";
   ```

   هنا، ينشئ `queue_declare` قائمة انتظار باسم 'hello' مع الإعدادات الافتراضية (غير دائمة، غير حصرية، حذف تلقائي). يرسل `basic_publish` الرسالة إلى قائمة الانتظار.

4. **إغلاق الاتصال:**
   بعد الإرسال، أغلق القناة والاتصال لتحرير الموارد:

   ```php
   $channel->close();
   $connection->close();
   ```

هذه العملية قياسية عبر الإصدارات، مع عدم ملاحظة تغييرات كبيرة في سجل التغييرات للإصدار 2.6.* مقارنة بالإصدارات اللاحقة.

#### استقبال الرسائل: تفاصيل خاصة بالإصدار
يتطلب استقبال الرسائل في الإصدار 2.6.* اهتماماً دقيقاً، حيث أن آلية الاستهلاك تختلف عن الإصدارات الأحدث. إليك العملية التفصيلية:

1. **تضمين الملفات المطلوبة:**
   مشابه للإرسال، قم بتضمين أداة التحميل التلقائي والفئات الضرورية:

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   ```

2. **إنشاء اتصال وقناة:**
   أنشئ الاتصال والقناة كما كان من قبل:

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

3. **تصريح قائمة الانتظار:**
   تأكد من وجود قائمة الانتظار، مطابقة لتصريح المرسل:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   ```

4. **تعريف رد الاتصال:**
   أنشئ دالة رد اتصال للتعامل مع الرسائل المستلمة:

   ```php
   $callback = function ($msg) {
       echo ' [x] Received ', $msg->body, "\n";
   };
   ```

   سيتم استدعاء هذه الدالة لكل رسالة، وطباعة المحتوى في هذا المثال.

5. **استهلاك الرسائل:**
   للإصدار 2.6.*، استخدم `basic_consume` لتسجيل رد الاتصال، ثم ادخل في حلقة لمواصلة الاستهلاك:

   ```php
   $channel->basic_consume('hello', '', false, true, false, false, $callback);
   while (count($channel->callbacks)) {
       $channel->wait();
   }
   ```

   تأخذ طريقة `basic_consume` معلمات لاسم قائمة الانتظار، ووسم المستهلك، و no-local، و no-ack، والحصرية، و no-wait، ورد الاتصال. تحافظ الحلقة مع `wait()` على تشغيل المستهلك، والتحقق من وجود الرسائل. هذه تفصيلة مهمة، حيث أن الإصدارات الأحدث (مثل 3.2) قد تستخدم طريقة `consume()`، والتي لم تكن متاحة في 2.6.* بناءً على مراجعة وثائق API.

6. **إغلاق الاتصال:**
   بعد الاستهلاك، أغلق الموارد:

   ```php
   $channel->close();
   $connection->close();
   ```

التفصيل غير المتوقع هو الحاجة إلى الحلقة اليدوية في الإصدار 2.6.*، والتي قد تتطلب معالجة أخطاء إضافية للاستخدام في الإنتاج، مثل التقاط الاستثناءات لمشكلات الاتصال.

#### اعتبارات خاصة بالإصدار
الإصدار 2.6.* هو جزء من الإصدارات الأقدم، وبينما لا يسجله سجل التغييرات صراحةً، فإن الإصدارات حول 2.5 إلى 2.7 تظهر تحسينات مثل دعم نبضات القلب والتوافق مع PHP 5.3. للرسائل الكبيرة، يدعم الإصدار 2.6.* `setBodySizeLimit` على القناة للتعامل مع حدود الذاكرة، وقطع الرسائل إذا لزم الأمر، مع تفاصيل في [GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib).

بالمقارنة مع الإصدار 3.2، تشمل التغييرات دعم PHP 8 وطرق جديدة مثل `consume()`، لكن الوظيفة الأساسية للإرسال والاستهلاك الأساسي تظل متشابهة. يجب على المستخدمين الاختبار للتأكد من التوافق، خاصة مع إصدارات PHP، حيث من المحتمل أن يدعم 2.6.* إصدارات PHP من 5.3 إلى 7.x، حسب إدخالات سجل التغييرات.

#### استكشاف الأخطاء وإصلاحها وأفضل الممارسات
- إذا فشل الإرسال، تحقق من سجلات RabbitMQ بحثاً عن إنذارات الموارد، مثل مساحة القرص أقل من 50 ميجابايت، وضبط الإعدادات عبر [RabbitMQ Configuration Guide](https://www.rabbitmq.com/configure.html#config-items).
- للاستهلاك، تأكد من تشغيل المستهلك باستمرار؛ استخدم أدوات مثل Supervisor للتشغيل كبرنامج خفي في الإنتاج.
- اذكر قوائم الانتظار باستخدام `rabbitmqctl list_queues` على Linux أو `rabbitmqctl.bat list_queues` على Windows كمستخدم مميز، حسب [RabbitMQ Command Line Tools](https://www.rabbitmq.com/cli.html).

#### الجدول: مقارنة الإصدارات للطرق الرئيسية

| الطريقة             | سلوك الإصدار 2.6.*                          | سلوك الإصدار 3.2                          |
|--------------------|------------------------------------------------|----------------------------------------------|
| `basic_publish`    | قياسي، ينشر إلى قائمة الانتظار                    | بدون تغيير، نفس الاستخدام                        |
| `basic_consume`    | يتطلب حلقة مع `wait()` للاستهلاك       | مشابه، لكن طريقة `consume()` متاحة     |
| `setBodySizeLimit` | مدعوم للرسائل الكبيرة، يقطع إذا تم الضبط | مدعوم، نفس الوظيفة                |
| التوافق مع PHP  | على الأرجح من 5.3 إلى 7.x                               | يدعم إصدارات PHP 7.x و 8.x                     |

يسلط هذا الجدول الضوء على الاختلاف الرئيسي في الاستهلاك، وهو أمر بالغ الأهمية لمستخدمي الإصدار 2.6.*.

#### الخلاصة
يتضمن استخدام الإصدار 2.6.* من "php-amqplib/php-amqplib" التثبيت القياسي عبر Composer، مع إرسال الرسائل عبر `basic_publish` والاستقبال عبر `basic_consume` مع حلقة يدوية. بينما يشبه الإصدارات الأحدث، فإن عملية الاستهلاك تتطلب اهتماماً إضافياً، مما يجعل من الضروري للمطورين الاختبار والتعديل للأنظمة القديمة. لمزيد من التفاصيل، استشر دروس RabbitMQ التعليمية الرسمية ومستودع GitHub.

---

### الاقتباسات الرئيسية
- [GitHub - php-amqplib/php-amqplib The most widely used PHP client for RabbitMQ](https://github.com/php-amqplib/php-amqplib)
- [RabbitMQ tutorial - "Hello World!" PHP example](https://www.rabbitmq.com/tutorials/tutorial-one-php)
- [CloudAMQP PHP Documentation Get started with CloudAMQP and PHP](https://www.cloudamqp.com/docs/php.html)
- [php-amqplib/php-amqplib Packagist Formerly videlalvaro/php-amqplib](https://packagist.org/packages/php-amqplib/php-amqplib)
- [GitHub - php-amqplib/php-amqplib CHANGELOG file](https://github.com/php-amqplib/php-amqplib/blob/master/CHANGELOG.md)
- [RabbitMQ Configuration Guide Config items and settings](https://www.rabbitmq.com/configure.html#config-items)
- [RabbitMQ Command Line Tools CLI reference and usage](https://www.rabbitmq.com/cli.html)