---
audio: false
generated: true
lang: ar
layout: post
title: مكتبة سحابية Pili للتدفق PHP
translated: true
---

### النقاط الرئيسية
- يبدو أن استخدام "pili-engineering/pili-sdk-php": "dev-master" يتطلب تثبيته عبر Composer وإعداد بيانات اعتماد Qiniu.
- تشير الأبحاث إلى أن الحزمة تتطلب PHP 5.3.0 أو أعلى، وهي لمستخدمي Pili Streaming Cloud، المرتبطة بـ Qiniu.
- يشير الدليل إلى إنشاء كائن Hub واستخدام عمليات التدفق مثل إنشاء URLs RTMP، ولكن قد تختلف الأساليب الدقيقة.

### التثبيت
أولا، تأكد من أن Composer مثبّت. أضف الحزمة إلى ملف `composer.json` الخاص بك مع:
```json
"require": {
    "pili-engineering/pili-sdk-php": "dev-master"
}
```
ثم، قم بتشغيل `composer install` أو `composer update`. في سكربت PHP الخاص بك، أضف:
```php
require 'vendor/autoload.php';
```

### الإعداد والاستخدام
ستمحتك حساب Qiniu وحساب Pili Hub. قم بإعداد مفتاح الوصول، المفتاح السري، وإسم الحوب، ثم قم بإنشاء كائن Hub:
```php
use Qiniu\Credentials;
use Pili\Hub;

$credentials = new Credentials('your_access_key', 'your_secret_key');
$hub = new Hub($credentials, 'your_hub_name');
```
إنشاء أو الحصول على تدفق، مثل `$stream = $hub->createStream('your_stream_key');`، واستخدم أساليب مثل `$stream->rtmpPublishUrl(60)` للعمليات.

### تفاصيل غير متوقعة
لاحظ أن "dev-master" هو إصدار تطويري، قد يكون غير مستقر، مع إصدارات مخصصة مثل 1.5.5 متاحة للاستخدام الإنتاجي.

---

### دليل شامل لاستخدام "pili-engineering/pili-sdk-php": "dev-master"

يقدم هذا الدليل استكشافًا مفصلًا لكيفية استخدام حزمة "pili-engineering/pili-sdk-php" مع الإصدار "dev-master" بناءً على الوثائق والمثالات المتاحة. يغطي التثبيت والإعداد والاستخدام والتفاصيل الإضافية، مما يضمن فهمًا شاملًا للمطورين الذين يعملون مع خدمات Pili Streaming Cloud.

#### الخلفية والسياق
حزمة "pili-engineering/pili-sdk-php" هي مكتبة خادمية لـ PHP، مصممة لتفاعل مع Pili Streaming Cloud، خدمة مرتبطة بـ Qiniu، مزود تخزين السحاب وCDN. يشير "dev-master" إلى الفروع التطويرية الأخيرة، والتي قد تحتوي على ميزات حديثة ولكن قد تكون أقل استقرارًا من الإصدارات المخصصة. تتطلب الحزمة PHP 5.3.0 أو أعلى، مما يجعلها متاحة لمجتمعات PHP العديد.

#### عملية التثبيت
لبدء العمل، يجب أن يكون Composer مثبّتًا، وهو مدير اعتمادات لـ PHP. يتضمن التثبيت إضافة الحزمة إلى ملف `composer.json` لمشروعك وتشغيل أمر Composer لتنزيلها. بشكل محدد:

- أضف التالي إلى ملف `composer.json` تحت القسم "require":
  ```json
  "require": {
      "pili-engineering/pili-sdk-php": "dev-master"
  }
  ```
- قم بتشغيل `composer install` أو `composer update` في المصفح الخاص بك لتنزيل الحزمة ومتطلباتها. هذا سيخلق مجلد `vendor` مع الملفات اللازمة.
- في سكربت PHP الخاص بك، أضف المحمل التلقائي للوصول إلى فئات الحزمة:
  ```php
  require 'vendor/autoload.php';
  ```

تضمن هذه العملية أن الحزمة متكاملة في مشروعك، مستفيدًا من تحميل Composer التلقائي للوصول السهل إلى الفئات.

#### المتطلبات والإعداد
قبل استخدام SDK، تحتاج إلى حساب Qiniu ويجب إعداد Pili Hub، حيث يتفاعل SDK مع خدمات Pili Streaming Cloud. يتضمن ذلك الحصول على مفتاح الوصول ومفتاح السري من Qiniu وإعداد حوب في منصة Qiniu. تشير الوثائق إلى أن هذه البيانات ضرورية للمصادقة.

لإعداد، حدد بيانات اعتمادك في سكربت PHP الخاص بك:
- مفتاح الوصول: مفتاح الوصول الخاص بك لـ Qiniu.
- المفتاح السري: المفتاح السري الخاص بك لـ Qiniu.
- اسم الحوب: اسم Pili Hub الخاص بك، يجب أن يكون موجودًا مسبقًا.

يبدو الإعداد مثل:
```php
$accessKey = 'your_access_key';
$secretKey = 'your_secret_key';
$hubName = 'your_hub_name';
```

#### إنشاء واستخدام كائن Hub
يشكل كائن Hub قلب SDK، مما يسهل إدارة التدفق. أولاً، قم بإنشاء كائن Credentials باستخدام مفاتيح Qiniu:
```php
use Qiniu\Credentials;

$credentials = new Credentials($accessKey, $secretKey);
```
ثم، قم بإنشاء كائن Hub بهذه البيانات والمفتاح:
```php
use Pili\Hub;

$hub = new Hub($credentials, $hubName);
```
يتيح لك هذا كائن Hub تنفيذ عمليات مختلفة مرتبطة بالتدفق، مثل إنشاء، الحصول على، أو قائمة التدفقات.

#### العمل مع التدفقات
تدفقات مركزية لـ Pili Streaming Cloud، وتوفر SDK أساليب لإدارةها عبر كائن Hub. لإنشاء تدفق جديد:
```php
$streamKey = 'your_stream_key'; // يجب أن يكون فريدًا في الحوب
$stream = $hub->createStream($streamKey);
```
لحصول على تدفق موجود:
```php
$stream = $hub->getStream($streamKey);
```
ثم يقدم كائن التدفق أساليب مختلفة للعمليات، مفصولة في الجدول التالي بناءً على الوثائق المتاحة:

| **العملية**          | **الطريقة**                     | **الوصف**                                      |
|-------------------------|--------------------------------|------------------------------------------------------|
| إنشاء تدفق          | `$hub->createStream($key)`     | إنشاء تدفق جديد مع المفتاح المحدد.             |
| الحصول على تدفق             | `$hub->getStream($key)`        | الحصول على تدفق موجود من خلال المفتاح.                 |
| قائمة التدفقات           | `$hub->listStreams($marker, $limit, $prefix)` | قائمة التدفقات مع خيارات التصفح.               |
| URL نشر RTMP       | `$stream->rtmpPublishUrl($expire)` | إنشاء URL نشر RTMP مع وقت انتهاء الصلاحية.  |
| URL تشغيل RTMP          | `$stream->rtmpPlayUrl()`       | إنشاء URL تشغيل RTMP للتدفق.           |
| URL تشغيل HLS           | `$stream->hlsPlayUrl()`        | إنشاء URL تشغيل HLS للتدفق.             |
| تعطيل التدفق         | `$stream->disable()`           | تعطيل التدفق.                                 |
| تفعيل التدفق          | `$stream->enable()`            | تفعيل التدفق.                                  |
| حالة التدفق      | `$stream->status()`            | الحصول على حالة التدفق الحالية.          |

على سبيل المثال، لإنشاء URL نشر RTMP مع وقت انتهاء الصلاحية 60 ثانية:
```php
$expire = 60;
$url = $stream->rtmpPublishUrl($expire);
echo $url;
```
يمكن استخدام هذا URL لنشر التدفقات إلى Pili Streaming Cloud، مع انتهاء الصلاحية يضمن الوصول المؤقت.

#### تفاصيل إضافية
- **استقرار الإصدار**: "dev-master" هو فرع التطوير، قد يكون غير مستقر. للاستخدام الإنتاجي، اعتبر استخدام إصدار مخصص، مثل 1.5.5، متاح على Packagist [pili-engineering/pili-sdk-php versions](https://packagist.org/p/pili-engineering/pili-sdk-php). تشير السجلات إلى تحديثات مثل إضافة API وتهذيب الأساليب، مع إصدارات تعود إلى عام 2016.
- **معالجة الأخطاء**: تشير الوثائق إلى استخدام كتل try-catch للعمليات، كما في أمثلة إنشاء واكتساب التدفقات، لمعالجة الاستثناءات المحتملة.
- **وثائق ومثالات**: على الرغم من عدم توضيح الأمثلة بشكل واسع، فإن مستودع GitHub [Pili Streaming Cloud server-side library for PHP](https://github.com/pili-engineering/pili-sdk-php) يقدم تعليمات التثبيت وLists الميزات، ومقارنة مع SDKs لغات أخرى (مثل Python) تشير إلى وظائف مماثلة، مثل إنشاء URLs.

#### رؤى مقارنة
مقارنة مع SDKs Pili الأخرى، مثل الإصدار Python، تظهر أنماط مماثلة: كلاهما يتطلب بيانات اعتماد، إعداد Hub، وعمليات التدفق. ومع ذلك، يستخدم الإصدار PHP نهجًا موجهًا للأوبجكت مع فئات Hub وStream، في مقابل أسلوب Python الوظيفي. وهذا يتوافق مع الممارسات التطويرية النموذجية لـ PHP، يقدم أمان النوع ودعم IDE.

#### الخاتمة
استخدام "pili-engineering/pili-sdk-php": "dev-master" يتضمن تثبيته عبر Composer، إعداد بيانات اعتماد Qiniu، إنشاء كائن Hub، وإدارة التدفقات باستخدام أساليب مثل `rtmpPublishUrl`. تأكد من أن بيئتك تتوافق مع متطلبات PHP 5.3.0+ واستخدم استقرارًا للإنتاج. يقدم هذا الدليل نقطة بداية شاملة، مع تفاصيل إضافية متاحة في الوثائق الرسمية ومستودع GitHub.

### الإشارات الرئيسية
- [Pili Streaming Cloud server-side library for PHP GitHub](https://github.com/pili-engineering/pili-sdk-php)
- [pili-engineering/pili-sdk-php versions Packagist](https://packagist.org/p/pili-engineering/pili-sdk-php)