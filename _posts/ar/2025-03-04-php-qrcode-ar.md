---
audio: false
generated: true
lang: ar
layout: post
title: أداة PHP لتوليد رموز QR
translated: true
type: note
---

### النقاط الرئيسية
- يبدو أنه لاستخدام "endroid/qr-code" الإصدار 2.2.2، تحتاج إلى تثبيته عبر Composer والتأكد من تمكين امتداد GD.
- تشير الأبحاث إلى أنه يمكنك إنشاء رموز QR باستخدام فئة Builder، مع تعيين معاملات مثل البيانات، الحجم، والكاتب، ثم حفظ النتيجة أو إخراجها.
- تميل الأدلة إلى أن المكتبة تدعم تنسيقات PNG و SVG وغيرها، مع خيارات لإضافة الشعارات والتسميات، ولكن يجب التحقق من ذلك للإصدار 2.2.2.

### التثبيت
أولاً، قم بتثبيت المكتبة باستخدام Composer بالأمر:
```
composer require endroid/qr-code:2.2.2
```
تأكد من أن إعداد PHP الخاص بك يحتوي على امتداد GD مفعل، لأنه مطلوب لإنشاء الصور.

### مثال للاستخدام
إليك مثالاً أساسياً باستخدام فئة Builder، والذي من المحتمل أن يكون متوافقاً مع الإصدار 2.2.2:
```php
use Endroid\QrCode\Builder\Builder;
use Endroid\QrCode\Encoding\Encoding;
use Endroid\QrCode\ErrorCorrectionLevel\ErrorCorrectionLevelHigh;
use Endroid\QrCode\Writer\PngWriter;

$url = 'https://example.com';
$qrCode = Builder::create()
    ->writer(new PngWriter())
    ->data($url)
    ->encoding(new Encoding('ISO-8859-1'))
    ->errorCorrectionLevel(new ErrorCorrectionLevelHigh())
    ->build();
$qrCode->saveToFile('qr_code.png');
```
هذا ينشئ رمز استجابة سريعة (QR) لرابط ويب ويحفظه كملف PNG. يمكنك أيضاً إخراجه كـ data URI للعرض على الويب.

### ملاحظات إضافية
المكتبة تدعم كتاباً مختلفين (مثل PNG، SVG) وتسمح بالتخصيص مثل إضافة الشعارات أو التسميات. ومع ذلك، نظراً لأن الإصدار 2.2.2 أقدم، فقد لا تكون بعض الميزات الموجودة في الوثائق الحالية (مثل خيارات الشعار المتقدمة) متاحة، لذا تحقق من وثائق ذلك الإصدار المحدد على [GitHub](https://github.com/endroid/qr-code).

---

### ملاحظة المسح: دليل مفصل لاستخدام "endroid/qr-code" الإصدار 2.2.2

توفر هذه الملاحظة دليلاً شاملاً لاستخدام مكتبة "endroid/qr-code"، الإصدار 2.2.2، لإنشاء رموز QR في تطبيقات PHP. إنها توسع نطاق الإجابة المباشرة من خلال تضمين جميع التفاصيل ذات الصلة من البحث، مما يضمن فهماً شاملاً للمطورين، خاصة أولئك الجدد على المكتبة. يتم تنظيم المحتوى لمحاكاة مقال احترافي، مع جداول للتوضيح وروابط داخلية للمرجعية الإضافية.

#### المقدمة
مكتبة "endroid/qr-code" هي أداة PHP لإنشاء رموز QR، تُستخدم على نطاق واسع لتطبيقات مثل تتبع المنتجات وإدارة المستندات والتسويق. الإصدار 2.2.2، المحدد في الاستعلام، هو إصدار أقدم، وعلى الرغم من الإشارة إلى أن المكتبة مهجورة على [Packagist](https://packagist.org/packages/endroid/qr-code)، إلا أنها تظل وظيفية لإنشاء رموز QR الأساسية. يوضح هذا الدليل التثبيت والاستخدام، مع التركيز على ضمان التوافق مع الإصدار 2.2.2، مع الإقرار بالاختلافات المحتملة عن الإصدارات الأحدث.

#### عملية التثبيت
للبدء، يجب عليك تثبيت المكتبة عبر Composer، مدير حزم PHP. الأمر هو:
```
composer require endroid/qr-code:2.2.2
```
هذا يضمن حصولك على الإصدار 2.2.2 بالضبط. المتطلب الحرج هو امتداد GD لـ PHP، والذي يجب تمكينه وتهيئته، لأنه أساسي لإنشاء الصور. بدونه، لا يمكن للمكتبة إنتاج رموز QR بصرية.

| الخطوة                  | التفاصيل                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| أمر التثبيت            | `composer require endroid/qr-code:2.2.2`                                |
| متطلب PHP              | تأكد من تمكين امتداد GD (تحقق من `phpinfo()` للتأكيد)                    |

تشير الأبحاث إلى أن مستودع GitHub الخاص بالمكتبة ([GitHub](https://github.com/endroid/qr-code)) وصفحات [Packagist](https://packagist.org/packages/endroid/qr-code) تؤكد طريقة التثبيت هذه، مع عدم العثور على وثائق محددة للإصدار 2.2.2، مما يشير إلى الاعتماد على أنماط الاستخدام العامة.

#### تفاصيل الاستخدام
تقدم المكتبة طريقتين أساسيتين لإنشاء رموز QR: استخدام فئة Builder أو مباشرة مع فئة QrCode. نظراً لتركيز الاستعلام على الاستخدام، يُوصى بطريقة Builder لبساطتها، على الرغم من تفصيل كلاهما هنا للاكتمال.

##### استخدام فئة Builder
توفر فئة Builder واجهة سلسة (fluent interface) لتهيئة رموز QR. استناداً إلى أمثلة من الوثائق الحديثة، فإن التطبيق الأساسي هو:
```php
use Endroid\QrCode\Builder\Builder;
use Endroid\QrCode\Encoding\Encoding;
use Endroid\QrCode\ErrorCorrectionLevel\ErrorCorrectionLevelHigh;
use Endroid\QrCode\Writer\PngWriter;

$url = 'https://example.com';
$qrCode = Builder::create()
    ->writer(new PngWriter())
    ->data($url)
    ->encoding(new Encoding('ISO-8859-1'))
    ->errorCorrectionLevel(new ErrorCorrectionLevelHigh())
    ->build();
$qrCode->saveToFile('qr_code.png');
```
ينشئ هذا الكود رمز استجابة سريعة (QR) للرابط، باستخدام تنسيق PNG، مع ترميز ISO-8859-1 لتوافق أفضل مع الماسحات الضوئية وتصحيح أخطاء عالي. يمكنك أيضاً إخراجه كـ data URI:
```php
$qrCodeDataUri = $qrCode->getDataUri();
```
هذا مفيد للتضمين في HTML، على سبيل المثال: `<img src="<?php echo $qrCodeDataUri; ?>">`.

ومع ذلك، نظراً لقدم الإصدار 2.2.2، قد تكون أسماء بعض الفئات مثل `ErrorCorrectionLevelHigh` مختلفة (مثل `ErrorCorrectionLevel::HIGH` في الإصدارات الأقدم). يشير البحث من منشورات Stack Overflow ([Stack Overflow](https://stackoverflow.com/questions/40777377/endroid-qr-code)) إلى أن الإصدارات الأقدم استخدمت طرقاً مثل `setErrorCorrection('high')`، لذا تحقق من API للإصدار 2.2.2.

##### استخدام فئة QrCode مباشرة
لمزيد من التحكم، يمكنك استخدام فئة QrCode، كما هو موضح في الأمثلة:
```php
use Endroid\QrCode\QrCode;
use Endroid\QrCode\Writer\PngWriter;

$qrCode = new QrCode('Life is too short to be generating QR codes');
$qrCode->setSize(300);
$qrCode->setMargin(10);
$writer = new PngWriter();
$result = $writer->write($qrCode);
$result->saveToFile('qrcode.png');
```
هذه الطريقة أكثر تفصيلاً ولكنها تسمح بالضبط الدقيق، مثل تعيين ألوان المقدمة والخلفية، والتي قد تكون ذات صلة بالإصدار 2.2.2. مرة أخرى، تحقق من توفر الطريقة في الوثائق.

#### خيارات التهيئة
تدعم المكتبة كتاباً مختلفين لتنسيقات الإخراج المختلفة، كما هو مفصل في الجدول أدناه، استناداً إلى الوثائق الحالية، مع ملاحظة للتحقق من ذلك للإصدار 2.2.2:

| فئة الكاتب             | التنسيق   | ملاحظات                                                                 |
|-----------------------|----------|----------------------------------------------------------------------|
| PngWriter             | PNG      | مستوى الضغط قابل للتكوين، الافتراضي -1                                |
| SvgWriter             | SVG      | مناسب للرسومات المتجهة، لا توجد خيارات ضغط                           |
| WebPWriter            | WebP     | الجودة 0-100، الافتراضي 80، جيد للاستخدام على الويب                  |
| PdfWriter             | PDF      | الوحدة بالملم، الافتراضي، جيد للطباعة                                |

تشمل خيارات الترميز UTF-8 (الافتراضي) و ISO-8859-1، مع التوصية بالأخير لتوافق أفضل مع قارئات الباركود. يمكن أن تحسن أوضاع حجم الكتلة المستديرة (الهامش، التكبير، التصغير، لا شيء) من إمكانية القراءة، ولكن يجب التأكد من توفرها في الإصدار 2.2.2.

#### الميزات المتقدمة والاعتبارات
للاستخدام المتقدم، مثل تضمين الشعارات، تدعم فئة Builder طرقاً مثل `logoPath()` و `logoResizeToWidth()`، كما ورد في مقال على Medium ([Medium](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)). ومع ذلك، قد تكون هذه الإضافات لاحقة للإصدار 2.2.2، لذا اختبر من أجل التوافق. التحقق من صحة رموز QR المُنشأة ممكن ولكنه يؤثر على الأداء ومعطل افتراضياً، وهي تفصيلة من [GitHub](https://github.com/endroid/qr-code).

نظراً لملاحظة هجر المكتبة على [Packagist](https://packagist.org/packages/endroid/qr-code)، تجدر الإشارة إلى المخاوف المحتملة المتعلقة بالأمان أو الصيانة، على الرغم من أنها تظل قابلة للتطبيق للاستخدام الأساسي. لمستخدمي Symfony، هناك حزمة (bundle) ([GitHub](https://github.com/endroid/qr-code-bundle))، ولكن هذا خارج نطاق استخدام PHP العام.

#### ملاحظات خاصة بالإصدار
أظهر البحث عدم وجود وثائق مباشرة للإصدار 2.2.2، مع عدم إدراج علامات (tags) له على GitHub، مما يشير إلى أنه قد يكون إصداراً أقدم أو خطأ مطبعي. يظهر المستودع الحالي إصدارات تصل إلى 6.0.0، ويشير [Packagist](https://packagist.org/packages/endroid/qr-code) إلى أنه مهجور، ويوصي بـ endroid/qr-code، وهو أمر محير لأنها نفس الحزمة. يشير هذا إلى مشاكل محتملة في إعادة التسمية أو إدارة الإصدارات، لذا يجب على المستخدمين قفل التبعيات واختبار التحديثات.

#### الخلاصة
يتضمن استخدام "endroid/qr-code" الإصدار 2.2.2 التثبيت عبر Composer، وضمان تمكين امتداد GD، وإنشاء رموز QR باستخدام فئة Builder أو QrCode. بينما تستند الأمثلة إلى الوثائق الحالية، تحقق من اختلافات API للإصدار 2.2.2، خاصة للميزات المتقدمة. لمزيد من التفاصيل، استشر صفحة GitHub الخاصة بالمكتبة ومناقشات Stack Overflow ذات الصلة.

#### الاقتباسات الرئيسية
- [مستودع GitHub لمنشئ رموز QR](https://github.com/endroid/qr-code)
- [صفحة Packagist لـ endroid/qr-code](https://packagist.org/packages/endroid/qr-code)
- [مقال Medium عن إنشاء رموز QR مع الصور المضمنة](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)
- [مناقشة Stack Overflow حول Endroid QR Code](https://stackoverflow.com/questions/40777377/endroid-qr-code)