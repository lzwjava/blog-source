---
audio: false
generated: true
lang: ar
layout: post
title: استخدام أفمبغ في بي إتش بي
translated: true
type: note
---

### النقاط الرئيسية
- يبدو من المحتمل أنه لاستخدام الإصدار ~0.5 من "php-ffmpeg/php-ffmpeg"، تحتاج أولاً إلى تثبيت FFMpeg على نظامك ثم استخدام Composer لتثبيت مكتبة PHP.
- تشير الأبحاث إلى ضرورة تضمين ملف autoload وإنشاء نسخة من `FFMpeg\FFMpeg` لمعالجة الوسائط، مع خيارات لتحديد مسارات الملفات الثنائية إذا لزم الأمر.
- تميل الأدلة نحو استخدام طرق مثل `open()`، و`save()`، و`frame()` للعمليات الأساسية، ولكن تحقق من وثائق GitHub للحصول على التفاصيل الكاملة بسبب الاختلافات المحتملة الخاصة بالإصدار.

---

### التثبيت
أولاً، تأكد من تثبيت FFMpeg على نظامك:
- على Ubuntu، استخدم `sudo apt-get install ffmpeg`.
- على macOS، استخدم `brew install ffmpeg`.
- على Windows، قم بالتحميل من [هذا الموقع](https://www.gyan.dev/ffmpeg/builds/) واتبع التعليمات.

بعد ذلك، قم بتثبيت مكتبة php-FFMpeg عبر Composer باستخدام:
```
composer require php-FFMpeg/php-FFMpeg:~0.5
```

### الإعداد والاستخدام
قم بتضمين ملف autoload في سكريبت PHP الخاص بك:
```php
require_once 'vendor/autoload.php';
```

قم بإنشاء نسخة من `FFMpeg\FFMpeg`، مع تحديد المسارات اختيارياً إذا لم تكن الملفات الثنائية لـ FFMpeg موجودة في مسار النظام PATH:
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'binary' => '/path/to/FFMpeg',
    'ffprobe' => '/path/to/FFprobe'
));
```

افتح ملف وسائط وقم بإجراء العمليات، مثل:
- إعادة الترميز Transcoding: `$video->save('output.mp4', new FFMpeg\Format\Video\X264());`
- استخراج إطار: `$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5)); $frame->save('frame.jpg');`
- القص Clipping: `$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20)); $clip->save('clip.mp4');`

لمزيد من التفاصيل، راجع وثائق المكتبة على [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg).

---

### ملاحظة المسح: دليل شامل لاستخدام php-FFMpeg/php-FFMpeg الإصدار ~0.5

توفر هذه الملاحظة استكشافاً متعمقاً لاستخدام مكتبة "php-FFMpeg/php-FFMpeg"، تحديداً الإصدار التقريبي 0.5، استناداً إلى المعلومات المتاحة. وهي توسع نطاق الإجابة المباشرة من خلال تضمين جميع التفاصيل ذات الصلة من البحث، مما يضمن فهماً شاملاً للمستخدمين الذين يسعون لتنفيذ هذه المكتبة لمعالجة الوسائط.

#### الخلفية والسياق
مكتبة "php-FFMpeg/php-FFMpeg" هي غلاف wrapper لـ PHP للملف الثنائي FFMpeg، مما يتيح معالجة ملفات الفيديو والصوت بطريقة كائنية التوجه Object-Oriented. وهي تدعم مهاماً مثل إعادة الترميز Transcoding، واستخراج الإطارات، والقص، والمزيد، مما يجعلها ذات قيمة للمطورين العاملين على التطبيقات المتعلقة بالوسائط. يشير تحديد الإصدار "~0.5" إلى أي إصدار أكبر من أو يساوي 0.5 وأقل من 1.0، مما يشير إلى التوافق مع إصدارات PHP القديمة، والتي من المحتمل العثور عليها في الفرع 0.x من المستودع.

نظراً للتاريخ الحالي، 3 مارس 2025، وتطور المكتبة، قد يكون الإصدار 0.5 جزءاً من الدعم القديم Legacy support، حيث يتطلب الفرع الرئيسي الآن PHP 8.0 أو أعلى. تفترض هذه الملاحظة أن المستخدم يعمل ضمن قيود هذا الإصدار، مع الإقبال بالاختلافات المحتملة في الوظائف مقارنة بالإصدارات الأحدث.

#### عملية التثبيت
للبدء، يجب تثبيت FFMpeg على النظام، حيث تعتمد المكتبة على ملفاته الثنائية للعمليات. تختلف طرق التثبيت حسب نظام التشغيل:
- **Ubuntu**: استخدم الأمر `sudo apt-get install ffmpeg` للتثبيت عبر مدير الحزم.
- **macOS**: استخدم Homebrew مع `brew install ffmpeg` للحصول على تثبيت مباشر.
- **Windows**: قم بتنزيل الملفات الثنائية لـ FFMpeg من [هذا الموقع](https://www.gyan.dev/ffmpeg/builds/) واتبع التعليمات المقدمة، مع التأكد من إمكانية الوصول إلى الملفات التنفيذية في مسار النظام PATH أو تحديدها يدوياً.

بعد تثبيت FFMpeg، يتم تثبيت مكتبة php-FFMpeg عبر Composer، مدير حزم PHP. يضمن الأمر `composer require php-FFMpeg/php-FFMpeg:~0.5` جلب الإصدار الصحيح. تنشئ هذه العملية دليل `vendor` في المشروع، والذي يضم المكتبة وتبعياتها، حيث يدير Composer التحميل التلقائي autoloading للتكامل السلس.

#### الإعداد والتهيئة
بعد التثبيت، قم بتضمين ملف autoload في سكريبت PHP الخاص بك لتمكين الوصول إلى فئات المكتبة:
```php
require_once 'vendor/autoload.php';
```

قم بإنشاء نسخة من `FFMpeg\FFMpeg` للبدء في استخدام المكتبة. تتيح طريقة الإنشاء التكوين، وهو أمر مهم بشكل خاص إذا لم تكن الملفات الثنائية لـ FFMpeg في مسار النظام PATH:
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'timeout' => 0,
    'thread_count' => 12,
    'binary' => '/path/to/your/own/FFMpeg',
    'ffprobe' => '/path/to/your/own/FFprobe'
));
```
يدعم هذا التكوين ضبط مهلات الوقت timeouts، وأعداد الخيوط thread counts، ومسارات الملفات الثنائية الصريحة، مما يعزز المرونة لإعدادات النظام المختلفة. يبحث الإعداد الافتراضي عن الملفات الثنائية في PATH، لكن التحديد اليدوي يضمن التوافق، خاصة في البيئات المخصصة.

#### الاستخدام الأساسي والعمليات
توفر المكتبة واجهة كائنية التوجه سلسة لمعالجة الوسائط. ابدأ بفتح ملف وسائط:
```php
$video = $ff->open('input.mp4');
```
هذا يدعم مسارات نظام الملفات المحلي، وموارد HTTP، وبروتوكولات أخرى مدعومة من قبل FFMpeg، مع قائمة بالأنواع المدعومة المتاحة عبر الأمر `ffmpeg -protocols`.

##### إعادة الترميز Transcoding
تتضمن إعادة الترميز تحويل الوسائط إلى تنسيقات مختلفة. استخدم طريقة `save` مع نسخة من التنسيق Format:
```php
$format = new FFMpeg\Format\Video\X264();
$video->save('output.mp4', $format);
```
تنسيق `X264` هو مثال واحد؛ تدعم المكتبة تنسيقات فيديو وصوت متنوعة، يمكن تنفيذها عبر `FFMpeg\Format\FormatInterface`، مع واجهات محددة مثل `VideoInterface` و `AudioInterface` لأنواع الوسائط respective media types.

##### استخراج الإطارات
يعد استخراج الإطارات مفيداً للصور المصغرة thumbnails أو التحليل. يستخرج الكود التالي إطاراً عند 5 ثوانٍ:
```php
$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5));
$frame->save('frame.jpg');
```
تضمن فئة `TimeCode`، وهي جزء من `FFMpeg\Coordinate`، توقيتاً دقيقاً، مع خيارات للدقة في استخراج الصور.

##### القص Clipping
لقطع جزء من الفيديو، حدد أوقات البدء والانتهاء:
```php
$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20));
$clip->save('clip.mp4');
```
ينشئ هذا مقطع فيديو جديداً، مع الحفاظ على الجودة والتنسيق الأصليين، مع القدرة على تطبيق مرشحات filters إضافية إذا لزم الأمر.

#### الميزات المتقدمة والاعتبارات
تدعم المكتبة ميزات إضافية، كما هو موضح في الوثائق:
- **معالجة الصوت Audio Manipulation**: على غرار الفيديو، يمكن إعادة ترميز الصوت باستخدام `FFMpeg\Media\Audio::save`، وتطبيق المرشحات، وإضافة بيانات وصفية metadata، وإعادة أخذ العينات resampling.
- **إنشاء GIF**: يمكن حفظ صور GIF متحركة باستخدام `FFMpeg\Media\Gif::save`، مع معلمات مدة اختيارية.
- **الدمج Concatenation**: اجمع ملفات وسائط متعددة باستخدام `FFMpeg\Media\Concatenate::saveFromSameCodecs` لنفس الترميزات codecs أو `saveFromDifferentCodecs` للترميزات المتنوعة، مع موارد لمزيد من القراءة في [هذا الرابط](https://trac.ffmpeg.org/wiki/Concatenate)، و[هذا الرابط](https://ffmpeg.org/ffmpeg-formats.html#concat-1)، و[هذا الرابط](https://ffmpeg.org/ffmpeg.html#Stream-copy).
- **معالجة الوسائط المتقدمة Advanced Media Handling**: تدعم مدخلات/مخرجات متعددة مع `-filter_complex`، مفيدة للتصفية المعقدة complex filtering والتعيين mapping، مع دعم مدمج للمرشحات.
- **استخراج البيانات الوصفية Metadata Extraction**: استخدم `FFMpeg\FFProbe::create` للبيانات الوصفية، والتحقق من صحة الملفات باستخدام `FFMpeg\FFProbe::isValid` (متاح منذ v0.10.0، مع ملاحظة أن الإصدار 0.5 قد يفتقر إلى هذا).

توفر الإحداثيات Coordinates، مثل `FFMpeg\Coordinate\AspectRatio`، و`Dimension`، و`FrameRate`، و`Point` (ديناميكي منذ v0.10.0)، و`TimeCode`، تحكماً دقيقاً في خصائص الوسائط، على الرغم من أن بعض الميزات مثل النقاط الديناميكية قد لا تكون متاحة في الإصدار 0.5.

#### ملاحظات خاصة بالإصدار
نظراً لتحديد الإصدار "~0.5"، فمن المرجح أن المكتبة تتماشى مع الفرع 0.x، مما يدعم إصدارات PHP القديمة. يشير مستودع GitHub إلى PHP 8.0 أو أعلى للفرع الرئيسي، مع 0.x للدعم القديم. ومع ذلك، لم يتم العثور على تفاصيل الإصدار 0.5 بالضبط في الإصدارات Releases، مما يشير إلى أنه قد يكون جزءاً من سجل الالتزامات commit history أو التزامات الفرع. يجب على المستخدمين التحقق من التوافق، حيث قد تتطلب الميزات الأحدث مثل أنواع إحداثيات معينة (مثل النقاط الديناميكية) إصدارات تتجاوز 0.5.

#### الوثائق والقراءة الإضافية
بينما ظهرت صفحة Read the Docs ([Read the Docs](https://FFMpeg-PHP.readthedocs.io/en/latest/)) فارغة، يحتوي مستودع GitHub ([GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)) على وثائق شاملة داخل ملف README، تغطي استخدام API، والتنسيقات، والأمثلة. هذا هو المورد الأساسي للإصدار 0.5، نظراً لعدم وجود وثائق عبر إنترنت محددة لهذا الإصدار القديم.

#### الجدول: ملخص للعمليات والطرق الرئيسية

| العملية               | مثال الطريقة                                      | الوصف                                          |
|-----------------------|---------------------------------------------------|------------------------------------------------|
| فتح ملف وسائط         | `$ff->open('input.mp4')`                          | يحمل ملف وسائط للمعالجة                        |
| إعادة ترميز الفيديو   | `$video->save('output.mp4', new X264())`          | يحول إلى التنسيق المحدد                        |
| استخراج إطار          | `$video->frame(TimeCode::fromSeconds(5))->save('frame.jpg')` | يستخرج إطاراً في وقت محدد، يحفظ كصورة         |
| قص الفيديو            | `$video->clip(TimeCode::fromSeconds(10), TimeCode::fromSeconds(20))->save('clip.mp4')` | ينشئ مقطعاً بين وقتين، يحفظ كملف جديد         |
| تكوين النسخة          | `FFMpeg::create(array('binary' => '/path/to/FFMpeg'))` | يحدد مسارات الملفات الثنائية المخصصة والخيارات |

يلخص هذا الجدول الوظائف الأساسية، مما يساعد المستخدمين في الرجوع السريع أثناء تنفيذ المكتبة.

#### تفصيل غير متوقع: تداعيات الإصدار القديم
جانب غير متوقع هو القيد المحتمل للإصدار 0.5، نظراً لموقعه في الفرع 0.x لدعم PHP الأقدم. قد يقيد هذا الوصول إلى الميزات الحديثة، مثل نقاط الإحداثيات الديناميكية التي تم تقديمها في v0.10.0، مما يتطلب من المستخدمين التحقق من التزامات الفرع للحصول على الإمكانيات الدقيقة، مما يضيف طبقة من التعقيد غير الواضحة فوراً في الإصدارات الأحدث.

#### الخلاصة
يتضمن استخدام الإصدار ~0.5 من "php-FFMpeg/php-FFMpeg" تثبيت FFMpeg، والإعداد عبر Composer، والاستفادة من واجهة برمجة تطبيقات API كائنية التوجه لمهام الوسائط. بينما تكون العمليات الأساسية مثل إعادة الترميز واستخراج الإطارات واضحة، قد تستلزم الاختلافات الخاصة بالإصدار الرجوع إلى وثائق الفرع 0.x على [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg). يضمن هذا النهج الشامل أن يتمكن المستخدمون من استخدام المكتبة بفعالية، مع الإقرار بقوتها وقيودها المحتملة كإصدار قديم.

---

### الاقتباسات الرئيسية
- [FFMpeg PHP Object Oriented Library Packagist](https://packagist.org/products/php-FFMpeg/php-FFMpeg)
- [PHP-FFMpeg GitHub Repository Documentation](https://github.com/PHP-FFMpeg/PHP-FFMpeg)
- [FFMpeg PHP Read the Docs Documentation](https://FFMpeg-PHP.readthedocs.io/en/latest/)
- [FFMpeg Download and Builds Website](https://www.gyan.dev/ffmpeg/builds/)
- [FFMpeg Concatenation Wiki Page](https://trac.ffmpeg.org/wiki/Concatenate)
- [FFMpeg Formats Documentation Page](https://ffmpeg.org/ffmpeg-formats.html#concat-1)
- [FFMpeg Command Line Tool Documentation](https://ffmpeg.org/ffmpeg.html#Stream-copy)