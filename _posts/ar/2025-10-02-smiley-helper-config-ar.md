---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: تهيئة مساعد الوجوه الضاحكة في كود إيجنتر
translated: true
type: note
---

### نظرة عامة
هذا ملف تكوين PHP من إطار عمل CodeIgniter لتطوير الويب، وتحديدًا لـ **مساعد الوجوه التعبيرية/الابتسامات**. CodeIgniter هو إطار عمل PHP من نوع MVC لبناء تطبيقات الويب. يحدد هذا文件 مجموعة من رموز الوجوه التعبيرية/الابتسامات التي يستخدمها `smiley_helper` التابع للإطار لاستبدال الوجوه التعبيرية النصية (مثل `:-)`) تلقائيًا بوسوم HTML `<img>` التي تعرض صور GIF المقابلة.

يضمن الم文件 منع الوصول المباشر عبر `defined('BASEPATH') OR exit('No direct script access allowed');`، وهي إجراء أمان في CodeIgniter لمنع تنفيذ السكريبت المباشر غير المصرح به.

### المكونات الرئيسية
- **الغرض**: تحويل الوجوه التعبيرية النصية العادية في المحتوى الذي ينشئه المستخدم (مثل مشاركات المنتدى أو التعليقات) إلى صور مرئية لتجربة مستخدم أفضل.
- **هيكل البيانات**: `$smileys` عبارة عن مصفوفة ارتباطية في PHP بهيكل رسمي:
  ```
  $smileys = array(
      'smiley_code' => array('image_file', 'width', 'height', 'alt_text'),
      // ...
  );
  ```
  - **smiley_code**: النمط النصي المطلوب مطابقته (مثل `:-)`, `:lol:`, `>:(`).
  - **image_file**: اسم صورة GIF في دليل الابتسامات (الإعداد الافتراضي هو `application/views/smileys/` في CodeIgniter).
  - **width/height**: الأبعاد بالبكسل لوسم `<img>` (جميعها `'19'` هنا، مما يشير إلى صور GIF مقاس 19x19 بكسل).
  - **alt_text**: النص البديل لإمكانية الوصول/قارئات الشاشة، يصف المشاعر.

- **الاستخدام في CodeIgniter**: قم بتحميل المساعد باستخدام `$this->load->helper('smiley');`، ثم استدع دوالاً مثل `parse_smileys($text)` على السلاسل النصية التي تحتوي على رموز الوجوه التعبيرية. يستبدل هذا الرموز بوسوم `<img>`، على سبيل المثال:
  - الإدخال: `I'm happy :)`
    الإخراج: `I'm happy <img src="http://example.com/smileys/smile.gif" width="19" height="19" alt="smile">`

### تفصيل المدخلات
تتضمن المصفوفة أكثر من 40 تعيينًا مجمعة حسب نوع المشاعر. معظم الصور هي صور GIF مقاس 19x19 بكسل. إليك نظرة ملخصة (مع أمثلة):

| رمز الوجه التعبيري | الصورة | النص البديل | ملاحظات |
|---------------|-------|----------|-------|
| `:-)`, `:)` | grin.gif, smile.gif | grin, smile | ابتسامات وضحكات إيجابية. |
| `:lol:`, `:cheese:` | lol.gif, cheese.gif | LOL, cheese | ضحك/إعجاب، ابتسامة جبنية. |
| `;-)`, `;)` | wink.gif | wink | غمزة. |
| `:smirk:`, `:roll:` | smirk.gif, rolleyes.gif | smirk, rolleyes | سخرية/إيماءة حكيمة. |
| `:-S`, `:wow:`, `:bug:` | confused.gif, surprise.gif, bigsurprise.gif | confused, surprised, big surprise | حيرة/دهشة. |
| `:-P`, `%-P`, `;-P`, `:P` | tongue_laugh.gif, إلخ. | tongue laugh, إلخ. | متغيرات إخراج اللسان (ضاحك، غمزة، استهزاء). |
| `:blank:`, `:long:`, `:ohh:`, `:grrr:`, `:gulp:`, `8-/` | متنوعة | blank stare, long face, ohh, grrr, gulp, oh oh | وجوه محايدة أو منزعجة. |
| `:down:`, `:red:`, `:sick:`, `:shut:` | متنوعة | downer, red face, sick, shut eye | حزين، محرج، مريض. |
| `:-/`, `>:(` (`:mad:`), `>:-(` (`:angry:`) | hmm.gif, mad.gif, angry.gif | hmmm, mad, angry | مرتبك، غاضب، غاضب جدًا. |
| `:zip:`, `:kiss:` | zip.gif, kiss.gif | zipper, kiss | إغلاق الفم، قبلة. |
| `:ahhh:`, `:coolsmile:`, `-:coolsmirk:`, `:coolgrin:`, `:coolhmm:`, `:coolmad:`, `:coolcheese:` | shock.gif, shade_smile.gif, إلخ. | shock, cool smile, cool smirk, cool grin, cool hmm, cool mad, cool cheese | متغيرات مصدومة أو "رائعة"/بنظارات شمسية. |
| `:vampire:`, `:snake:` | vampire.gif, snake.gif | vampire, snake | وجوه تعبيرية ذات طابع. |
| `:exclaim:`, `:question:` | exclaim.gif, question.gif | exclaim, question | ما يعادل علامات الترقيم (!, ?). |

### التوسيع والتخصيص
- **إضافة ابتسامات**: أضف مدخلات جديدة، على سبيل المثال: `':fire:' => array('fire.gif', '19', '19', 'fire');`.
- **تغيير الصور**: قم بتحديث أسماء الملفات إذا كنت تستبدل صور GIF بصور PNG أو JPG (اضبط العرض والارتفاع وفقًا لذلك).
- **الدليل**: تأكد من وجود الصور في مسار الابتسامات في CodeIgniter.
- **القيود**: جميع الصور هنا بنفس الحجم؛ قد تختلف التطبيقات الحقيقية. هذه المصفوفة تحدد التعيينات فقط—منطق الاستبدال موجود في المساعد نفسه.

إذا كان لديك سؤال محدد حول تخصيص أو استخدام هذا في CodeIgniter، قدم المزيد من التفاصيل!