---
audio: false
generated: true
lang: ar
layout: post
title: استخدام ffmpeg في PHP
translated: true
---

### النقاط الرئيسية
- يبدو أن استخدام "php-ffmpeg/php-ffmpeg" الإصدار ~0.5 يتطلب أولاً تثبيت FFMpeg على نظامك، ثم استخدام Composer لتثبيت مكتبة PHP.
- تشير الأبحاث إلى تضمين ملف التحميل التلقائي وإنتاج مثال من `FFMpeg\FFMpeg` للتحكم في الوسائط، مع خيارات تحديد مسارات الثنائي إذا لزم الأمر.
- يشير الدليل إلى استخدام طرق مثل `open()`, `save()`, و `frame()` للعمليات الأساسية، ولكن تحقق من وثائق GitHub للحصول على التفاصيل الكاملة بسبب الاختلافات التي قد تكون محددة بالنسخة.

---

### التثبيت
أكد أولاً على تثبيت FFMpeg على نظامك:
- على Ubuntu، استخدم `sudo apt-get install ffmpeg`.
- على macOS، استخدم `brew install ffmpeg`.
- على Windows، قم بتنزيل من [هذا الموقع](https://www.gyan.dev/ffmpeg/builds/) واتبع التعليمات.

ثم، قم بتثبيت مكتبة php-FFMpeg عبر Composer باستخدام:
```
composer require php-FFMpeg/php-FFMpeg:~0.5
```

### الإعداد والاستخدام
أدخل ملف التحميل التلقائي في نصك PHP:
```php
require_once 'vendor/autoload.php';
```

إنتاج مثال من `FFMpeg\FFMpeg`، مع تحديد المسارات اختياريًا إذا لم تكن الثوابت FFMpeg في مسار النظام:
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'binary' => '/path/to/FFMpeg',
    'ffprobe' => '/path/to/FFprobe'
));
```

افتح ملف وسائط واكمل العمليات مثل:
- تحويل: `$video->save('output.mp4', new FFMpeg\Format\Video\X264());`
- استخراج إطار: `$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5)); $frame->save('frame.jpg');`
- تقطيع: `$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20)); $clip->save('clip.mp4');`

للحصول على مزيد من التفاصيل، راجع وثائق المكتبة على [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg).

---

### ملاحظة الاستطلاع: دليل شامل لاستخدام php-FFMpeg/php-FFMpeg الإصدار ~0.5

تقدم هذه الملاحظة استكشافًا شاملًا لاستخدام مكتبة "php-FFMpeg/php-FFMpeg"، بشكل خاص الإصدار حوالي 0.5، بناءً على المعلومات المتاحة. توسع على الإجابة المباشرة من خلال تضمين جميع التفاصيل ذات الصلة من البحث، مما يضمن فهمًا شاملًا للمستخدمين الذين يبحثون عن تنفيذ هذه مكتبة PHP للتحكم في الوسائط.

#### الخلفية والسياق
مكتبة "php-FFMpeg/php-FFMpeg" هي غلاف PHP للثوابت FFMpeg، مما يتيح التحكم في الوسائط بشكل موضوعي. تدعم مهام مثل تحويل الوسائط، استخراج الإطارات، تقطيع، وغيرها، مما يجعلها قيمة للمطورين الذين يعملون على تطبيقات ذات صلة بالوسائط. يشير التحديد "~0.5" إلى أي إصدار أكبر من أو يساوي 0.5 و أصغر من 1.0، مما يشير إلى التوافق مع إصدارات PHP القديمة، التي يمكن العثور عليها في فرع 0.x من المستودع.

بناءً على التاريخ الحالي، 3 مارس 2025، وتطور المكتبة، قد يكون الإصدار 0.5 جزءًا من الدعم التراثي، مع أن الفرع الرئيسي الآن يتطلب PHP 8.0 أو أعلى. توقع هذه الملاحظة أن المستخدم يعمل ضمن قيود هذه النسخة، معترفًا باحتمالية الاختلافات في الوظائف مقارنة بالإصدارات الجديدة.

#### عملية التثبيت
يجب أولاً تثبيت FFMpeg على النظام، حيث تعتمد المكتبة على ثوابتها للعمليات. تختلف طرق التثبيت حسب نظام التشغيل:
- **Ubuntu**: استخدم الأمر `sudo apt-get install ffmpeg` لتثبيته عبر مدير الحزم.
- **macOS**: استخدم Homebrew مع `brew install ffmpeg` لتثبيته بسهولة.
- **Windows**: قم بتنزيل ثوابت FFMpeg من [هذا الموقع](https://www.gyan.dev/ffmpeg/builds/) واتبع التعليمات المقدمة، مع التأكد من أن الملفات التنفيذية متاحة في مسار النظام أو تحديدها يدويًا.

بعد تثبيت FFMpeg، يتم تثبيت مكتبة php-FFMpeg عبر Composer، مدير حزم PHP. يضمن الأمر `composer require php-FFMpeg/php-FFMpeg:~0.5` استخراج النسخة الصحيحة. يخلق هذا عملية إنشاء مجلد `vendor` في المشروع، يحتوي على المكتبة وجميع الاعتماديات، مع إدارة Composer لتحميل التلقائي لضمان التكامل السلس.

#### الإعداد والتشغيل
بعد التثبيت، أدخل ملف التحميل التلقائي في نصك PHP لتسهيل الوصول إلى فئات المكتبة:
```php
require_once 'vendor/autoload.php';
```

إنتاج مثال من `FFMpeg\FFMpeg` لبدء استخدام المكتبة. تسمح طريقة الإنتاج بتكوين، خاصة إذا لم تكن ثوابت FFMpeg في مسار النظام:
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'timeout' => 0,
    'thread_count' => 12,
    'binary' => '/path/to/your/own/FFMpeg',
    'ffprobe' => '/path/to/your/own/FFprobe'
));
```
يتيح هذا التكوين تعيين أوقات الانتظار، عدد الخيوط، ومسارات الثوابت، مما يوفر مرونة أكبر للبيئات المختلفة. يبحث الإعداد الافتراضي عن الثوابت في المسار، ولكن تحديدها يدويًا يضمن التوافق، خاصة في البيئات المخصصة.

#### الاستخدام الأساسي والعمليات
توفر المكتبة واجهة موضوعية مريحة للتحكم في الوسائط. ابدأ بإفتح ملف وسائط:
```php
$video = $ff->open('input.mp4');
```
يدعم هذا المسارات المحلية للنظام، الموارد HTTP، وجميع البروتوكولات التي يدعمها FFMpeg، مع قائمة من أنواع الدعم المتاحة عبر الأمر `ffmpeg -protocols`.

##### تحويل الوسائط
يتضمن تحويل الوسائط تحويل الوسائط إلى صيغ مختلفة. استخدم طريقة `save` مع مثال صيغة:
```php
$format = new FFMpeg\Format\Video\X264();
$video->save('output.mp4', $format);
```
صيغة `X264` هي مثال واحد؛ تدعم المكتبة صيغ الفيديو والصوت المختلفة، يمكن تنفيذها عبر `FFMpeg\Format\FormatInterface`، مع واجهات محددة مثل `VideoInterface` و `AudioInterface` للوسائط respective.

##### استخراج الإطارات
يمكن أن يكون استخراج الإطارات مفيدًا لإنتاج الصور التوضيحية أو التحليل. يوضح الكود التالي استخراج إطار في الثانية الخامسة:
```php
$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5));
$frame->save('frame.jpg');
```
تضمن فئة `TimeCode`، جزء من `FFMpeg\Coordinate`، دقة الوقت، مع خيارات الدقة في استخراج الصور.

##### تقطيع
لتقطيع جزء من الفيديو، حدد أوقات البدء والنهاية:
```php
$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20));
$clip->save('clip.mp4');
```
يخلق هذا مقطع فيديو جديد، يحتفظ بالجودة والنمط الأصلي، مع القدرة على تطبيق فلاتر إضافية إذا لزم الأمر.

#### الميزات المتقدمة والتفاصيل
تدعم المكتبة ميزات إضافية، كما هو موضح في الوثائق:
- **تحكم في الصوت**: مثل الفيديو، يمكن تحويل الصوت باستخدام `FFMpeg\Media\Audio::save`، تطبيق الفلاتر، إضافة البيانات الوصفية، وإعادة العينة.
- **إنشاء GIF**: يمكن حفظ GIF متحركة باستخدام `FFMpeg\Media\Gif::save`، مع خيارات مدة اختيارية.
- **التجميع**: قم بدمج ملفات الوسائط متعددة باستخدام `FFMpeg\Media\Concatenate::saveFromSameCodecs` للرموز نفسها أو `saveFromDifferentCodecs` للرموز المختلفة، مع الموارد للقراءة المتقدمة في [هذا الرابط](https://trac.ffmpeg.org/wiki/Concatenate)، [هذا الرابط](https://ffmpeg.org/ffmpeg-formats.html#concat-1)، و [هذا الرابط](https://ffmpeg.org/ffmpeg.html#Stream-copy).
- **تحكم متقدم في الوسائط**: يدعم إدخالات/خروجات متعددة مع `-filter_complex`، مفيد للفلاتر والتحليل المعقد، مع دعم الفلاتر المدمج.
- **استخراج البيانات الوصفية**: استخدم `FFMpeg\FFProbe::create` للحصول على البيانات الوصفية، مع التحقق من صحة الملفات باستخدام `FFMpeg\FFProbe::isValid` (متاح منذ v0.10.0، مع العلم أن الإصدار 0.5 قد لا يحتوي على هذا).

توفر الإحداثيات مثل `FFMpeg\Coordinate\AspectRatio`، `Dimension`، `FrameRate`، `Point` (متحرك منذ v0.10.0)، و `TimeCode`، التحكم الدقيق في خصائص الوسائط، مع العلم أن بعض الميزات مثل النقاط الديناميكية قد لا تكون متاحة في الإصدار 0.5.

#### ملاحظات محددة بالنسخة
بناءً على التحديد "~0.5"، قد تتوافق المكتبة مع فرع 0.x، تدعم إصدارات PHP القديمة. يشير المستودع GitHub إلى PHP 8.0 أو أعلى للفرع الرئيسي، مع 0.x لدعم التراثي. ومع ذلك، لم يتم العثور على تفاصيل الإصدار 0.5 بشكل صريح في الإصدارات، مما يشير إلى أنه قد يكون جزءًا من تاريخ التزامات أو التزامات الفرع. يجب على المستخدمين التحقق من التوافق، حيث قد تتطلب الميزات الجديدة مثل أنواع الإحداثيات معينة (مثل النقاط الديناميكية) إصدارات بعد 0.5.

#### الوثائق والمزيد من القراءة
بينما كانت صفحة Read the Docs ([Read the Docs](https://FFMpeg-PHP.readthedocs.io/en/latest/)) فارغة، يحتوي المستودع GitHub ([GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)) على وثائق شاملة داخل README، تغطي استخدام API، الصيغ، والأمثلة. هذا هو المصدر الرئيسي للنسخة 0.5، مع غياب الوثائق المحددة على الإنترنت لهذه النسخة التراثية.

#### جدول: ملخص العمليات الرئيسية والمethods

| العملية               | مثال طريقة                                      | الوصف                                      |
|-------------------------|----------------------------------------------------|-------------------------------------------------|
| فتح ملف الوسائط         | `$ff->open('input.mp4')`                           | يفتح ملف الوسائط للتحكم فيه             |
| تحويل الفيديو         | `$video->save('output.mp4', new X264())`           | يحول إلى الصيغة المحددة                    |
| استخراج إطار           | `$video->frame(TimeCode::fromSeconds(5))->save('frame.jpg')` | يستخرج إطار في الوقت المحدد، يحفظه كصورة |
| تقطيع الفيديو              | `$video->clip(TimeCode::fromSeconds(10), TimeCode::fromSeconds(20))->save('clip.mp4')` | يخلق مقطع بين الأوقات، يحفظه كملف جديد   |
| تكوين المثال      | `FFMpeg::create(array('binary' => '/path/to/FFMpeg'))` | يحدد المسارات الثنائية والخيارات المخصصة            |

يحتوي هذا الجدول على الوظائف الأساسية، مما يساعد المستخدمين في الاستشارة السريعة أثناء تنفيذ المكتبة.

#### تفاصيل غير متوقعة: Implications of Legacy Version
جوانب غير متوقعة هي إمكانية قيود الإصدار 0.5، مع وضعه في فرع 0.x لدعم PHP القديم. قد يقيّد هذا الوصول إلى الميزات الحديثة مثل النقاط الديناميكية التي تم تقديمها في v0.10.0، مما يتطلب من المستخدمين التحقق من التزامات الفرع للحصول على القدرات الدقيقة، مما يضيف طبقة من التعقيد لا تظهر بشكل واضح في الإصدارات الحديثة.

#### الخاتمة
استخدام "php-FFMpeg/php-FFMpeg" الإصدار ~0.5 يتضمن تثبيت FFMpeg، الإعداد عبر Composer، واستخدام واجهة API موضوعية للتحكم في الوسائط. بينما تكون العمليات الأساسية مثل تحويل الوسائط واستخراج الإطارات بسيطة، قد تتطلب الاختلافات المحددة بالنسخة التحقق من وثائق فرع 0.x على [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg). يضمن هذا النهج الشامل أن المستخدمين يمكنهم استخدام المكتبة بشكل فعال، مع الاعتراف بقدراتها وقيداتها التراثية.

---

### المراجع الرئيسية
- [FFMpeg PHP Object Oriented Library Packagist](https://packagist.org/products/php-FFMpeg/php-FFMpeg)
- [PHP-FFMpeg GitHub Repository Documentation](https://github.com/PHP-FFMpeg/PHP-FFMpeg)
- [FFMpeg PHP Read the Docs Documentation](https://FFMpeg-PHP.readthedocs.io/en/latest/)
- [FFMpeg Download and Builds Website](https://www.gyan.dev/ffmpeg/builds/)
- [FFMpeg Concatenation Wiki Page](https://trac.ffmpeg.org/wiki/Concatenate)
- [FFMpeg Formats Documentation Page](https://ffmpeg.org/ffmpeg-formats.html#concat-1)
- [FFMpeg Command Line Tool Documentation](https://ffmpeg.org/ffmpeg.html#Stream-copy)