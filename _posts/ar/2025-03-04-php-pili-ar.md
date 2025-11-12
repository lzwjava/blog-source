---
audio: false
generated: true
lang: ar
layout: post
title: مكتبة بيلي للبث السحابي لـ PHP
translated: true
type: note
---

### النقاط الرئيسية
- يبدو أنه لاستخدام "pili-engineering/pili-sdk-php": "dev-master"، تحتاج إلى تثبيته عبر Composer وإعداد بيانات اعتماد Qiniu.
- تشير الأبحاث إلى أن الحزمة تتطلب PHP 5.3.0 أو إصدار أحدث وهي مخصصة لخدمة Pili Streaming Cloud، المرتبطة بـ Qiniu.
- تميل الأدلة إلى إنشاء كائن Hub واستخدام عمليات البث مثل إنشاء عناوين URL لـ RTMP، ولكن الطرق الدقيقة قد تختلف.

### التثبيت
أولاً، تأكد من تثبيت Composer. أضف الحزمة إلى ملف `composer.json` الخاص بك باستخدام:
```json
"require": {
    "pili-engineering/pili-sdk-php": "dev-master"
}
```
ثم، قم بتشغيل `composer install` أو `composer update`. في سيناريو PHP الخاص بك، قم بالتضمين:
```php
require 'vendor/autoload.php';
```

### الإعداد والاستخدام
ستحتاج إلى حساب Qiniu و Pili Hub. قم بتعيين مفتاح الوصول، والمفتاح السري، واسم الـ Hub، ثم أنشئ كائن Hub:
```php
use Qiniu\Credentials;
use Pili\Hub;

$credentials = new Credentials('your_access_key', 'your_secret_key');
$hub = new Hub($credentials, 'your_hub_name');
```
قم بإنشاء أو الحصول على دفق، على سبيل المثال، `$stream = $hub->createStream('your_stream_key');`، واستخدم طرقًا مثل `$stream->rtmpPublishUrl(60)` للعمليات.

### تفصيل غير متوقع
لاحظ أن "dev-master" هو إصدار تطوير، قد يكون غير مستقر، مع وجود إصدارات معنونة مثل 1.5.5 متاحة للاستخدام في الإنتاج.

---

### دليل شامل حول استخدام "pili-engineering/pili-sdk-php": "dev-master"

يقدم هذا الدليل استكشافًا مفصلاً لكيفية استخدام حزمة "pili-engineering/pili-sdk-php" مع إصدار "dev-master"، بناءً على الوثائق والأمثلة المتاحة. يغطي الدليل التثبيت، والإعداد، والاستخدام، والاعتبارات الإضافية، مما يضمن فهماً شاملاً للمطورين العاملين مع خدمات Pili Streaming Cloud.

#### الخلفية والسياق
حزمة "pili-engineering/pili-sdk-php" هي مكتبة للخادم مكتوبة بلغة PHP، مصممة للتفاعل مع Pili Streaming Cloud، وهي خدمة مرتبطة بـ Qiniu، مزج تخزين سحابي وشبكة توصيل محتوى. يشير إصدار "dev-master" إلى فرع التطوير الأحدث، والذي قد يتضمن ميزات حديثة ولكنه قد يكون أقل استقرارًا من الإصدارات المعنونة. تتطلب الحزمة PHP 5.3.0 أو إصدار أحدث، مما يجعلها في متناول العديد من بيئات PHP اعتبارًا من 3 مارس 2025.

#### عملية التثبيت
للبدء، يجب أن يكون لديك Composer مثبتًا، وهو مدير تبعيات لـ PHP. يتضمن التثبيت إضافة الحزمة إلى ملف المشروع `composer.json` وتشغيل أمر Composer لتنزيلها. على وجه التحديد:

- أضف ما يلي إلى `composer.json` الخاص بك في قسم "require":
  ```json
  "require": {
      "pili-engineering/pili-sdk-php": "dev-master"
  }
  ```
- نفذ `composer install` أو `composer update` في طرفيتك لجلب الحزمة وتبعياتها. سيؤدي هذا إلى إنشاء دليل `vendor` بالملفات اللازمة.
- في سيناريو PHP الخاص بك، قم بتضمين أداة التحميل التلقائي للوصول إلى فئات الحزمة:
  ```php
  require 'vendor/autoload.php';
  ```

 تضمن هذه العملية دمج الحزمة في مشروعك، والاستفادة من التحميل التلقائي لـ Composer لسهولة الوصول إلى الفئات.

#### المتطلبات الأساسية والإعداد
قبل استخدام SDK، تحتاج إلى حساب Qiniu ويجب عليك إعداد Pili Hub، حيث يتفاعل SDK مع خدمات Pili Streaming Cloud. يتضمن ذلك الحصول على مفتاح وصول ومفتاح سري من Qiniu وإنشاء hub ضمن منصتهم. تشير الوثائق إلى أن بيانات الاعتماد هذه ضرورية للمصادقة.

للإعداد، حدد بيانات الاعتماد الخاصة بك في سيناريو PHP:
- مفتاح الوصول: مفتاح الوصول لـ Qiniu الخاص بك.
- المفتاح السري: المفتاح السري لـ Qiniu الخاص بك.
- اسم الـ Hub: اسم Pili Hub الخاص بك، والذي يجب أن يكون موجودًا مسبقًا قبل الاستخدام.

يبدو مثال الإعداد كالتالي:
```php
$accessKey = 'your_access_key';
$secretKey = 'your_secret_key';
$hubName = 'your_hub_name';
```

#### إنشاء واستخدام كائن Hub
جوهر SDK هو كائن Hub، الذي يسهل إدارة البث. أولاً، أنشئ كائن Credentials باستخدام مفاتيح Qiniu الخاصة بك:
```php
use Qiniu\Credentials;

$credentials = new Credentials($accessKey, $secretKey);
```
ثم، أنشئ كائن Hub باستخدام بيانات الاعتماد هذه واسم الـ hub الخاص بك:
```php
use Pili\Hub;

$hub = new Hub($credentials, $hubName);
```
يسمح لك كائن Hub هذا بتنفيذ عمليات متنوعة متعلقة بالبث، مثل إنشاء واسترجاع أو سرد الدفق.

#### العمل مع الدفق
تعد الدفق مركزية في Pili Streaming Cloud، وتوفر SDK طرقًا لإدارتها من خلال كائن Hub. لإنشاء دفق جديد:
```php
$streamKey = 'your_stream_key'; // يجب أن يكون فريدًا داخل الـ hub
$stream = $hub->createStream($streamKey);
```
لاسترجاع دفق موجود:
```php
$stream = $hub->getStream($streamKey);
```
يقدم كائن الدفق بعد ذلك طرقًا متنوعة للعمليات، موضحة في الجدول التالي بناءً على الوثائق المتاحة:

| **العملية**          | **الطريقة**                     | **الوصف**                                      |
|-------------------------|--------------------------------|------------------------------------------------------|
| إنشاء دفق          | `$hub->createStream($key)`     | ينشئ دفقًا جديدًا بالمفتاح المعطى.             |
| الحصول على دفق             | `$hub->getStream($key)`        | يسترجع دفقًا موجودًا بالمفتاح.                 |
| سرد الدفق           | `$hub->listStreams($marker, $limit, $prefix)` | يسرد الدفق مع خيارات ترقيم الصفحات.               |
| عنوان URL لنشر RTMP       | `$stream->rtmpPublishUrl($expire)` | يولد عنوان URL لنشر RTMP مع وقت انتهاء.  |
| عنوان URL لتشغيل RTMP          | `$stream->rtmpPlayUrl()`       | يولد عنوان URL لتشغيل RTMP للدفق.           |
| عنوان URL لتشغيل HLS           | `$stream->hlsPlayUrl()`        | يولد عنوان URL لتشغيل HLS للبث.             |
| تعطيل الدفق         | `$stream->disable()`           | يعطل الدفق.                                 |
| تمكين الدفق          | `$stream->enable()`            | يمكّن الدفق.                                  |
| الحصول على حالة الدفق      | `$stream->status()`            | يسترجع الحالة الحالية للدفق.          |

على سبيل المثال، لإنشاء عنوان URL لنشر RTMP بانتهاء صلاحية 60 ثانية:
```php
$expire = 60;
$url = $stream->rtmpPublishUrl($expire);
echo $url;
```
يمكن استخدام هذا العنوان URL لنشر الدفق إلى Pili Streaming Cloud، مع ضمان الوصول المؤقت بفضل انتهاء الصلاحية.

#### اعتبارات إضافية
- **استقرار الإصدار**: إصدار "dev-master" هو فرع التطوير، وقد يكون غير مستقر. للإنتاج، فكر في استخدام إصدار معنون، مثل 1.5.5، المتاح على Packagist [إصدارات pili-engineering/pili-sdk-php](https://packagist.org/p/pili-engineering/pili-sdk-php). يظهر التاريخ تحديثات مثل إضافات API وتحسينات الطرق، مع إصدارات تعود إلى 2016.
- **معالجة الأخطاء**: تشير الوثائق إلى استخدام كتل try-catch للعمليات، كما يُرى في أمثلة إنشاء واسترجاع الدفق، للتعامل مع الاستثناءات المحتملة.
- **الوثائق والأمثلة**: بينما لم يتم تفصيل أمثلة محددة على نطاق واسع، فإن مستودع GitHub [مكتبة Pili Streaming Cloud للخادم بلغة PHP](https://github.com/pili-engineering/pili-sdk-php) يوفر تعليمات التثبيت وقوائم الميزات، وتشير المقارنات مع SDKs للغات أخرى (مثل Python) إلى وظائف مماثلة، مثل إنشاء عنوان URL.

#### رؤى مقارنة
تكشف المقارنة مع Pili SDKs الأخرى، مثل إصدار Python، عن أنماط متشابهة: كلاهما يتطلب بيانات اعتماد، وإعداد hub، وعمليات دفق. ومع ذلك، يستخدم إصدار PHP نهجًا كائني التوجه مع فئات Hub و Stream، على النقيض من النمط الوظيفي الأكثر في Python. يتوافق هذا مع ممارسات التطوير النموذجية في PHP، مما يوفر سلامة النوع ودعم IDE.

#### الخلاصة
يتضمن استخدام "pili-engineering/pili-sdk-php": "dev-master" التثبيت عبر Composer، وإعداد بيانات اعتماد Qiniu، وإنشاء كائن Hub، وإدارة الدفق بطرق مثل `rtmpPublishUrl`. تأكد من أن بيئتك تفي بمتطلبات PHP 5.3.0+ وفكر في الاستقرار للاستخدام في الإنتاج. يوفر هذا الدليل نقطة بداية شاملة، مع تفاصيل إضافية متاحة في الوثائق الرسمية والمستودع.

### الاقتباسات الرئيسية
- [مستودع GitHub لمكتبة Pili Streaming Cloud للخادم بلغة PHP](https://github.com/pili-engineering/pili-sdk-php)
- [إصدارات pili-engineering/pili-sdk-php على Packagist](https://packagist.org/p/pili-engineering/pili-sdk-php)