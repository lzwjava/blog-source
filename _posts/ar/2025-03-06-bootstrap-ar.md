---
audio: false
generated: true
lang: ar
layout: post
title: استخدام بوتستراب لبناء مواقع ويب متجاوبة
translated: true
---

لاستخدام Bootstrap في تطوير واجهات المستخدم، اتبع هذه الخطوات لتكامله واستخدامه بشكل فعال في بناء مواقع الويب الاستجابة والمصممة:

### 1. **فهم ما هو Bootstrap**
Bootstrap هو إطار عمل شائعة الاستخدام في واجهات المستخدم، مصمم لتسهيل إنشاء مواقع الويب الاستجابة، المتجهة نحو الهواتف أولاً. يوفر:
- **مكونات مسبقة التصميم**: أزرار، شريطات التنقل، استمارات، بطاقات، نافذة مودال، وغيرها.
- **نظام شبكة**: لإنشاء تصاميم مرنة تتكيف مع مختلف أحجام الشاشة.
- **CSS و JavaScript**: لتطبيق التسمية والتفاعل.

بإضافة Bootstrap إلى مشروعك، يمكنك بناء واجهات المستخدم بسرعة دون كتابة CSS أو JavaScript مخصص.

---

### 2. **إضافة Bootstrap إلى ملف HTML الخاص بك**
لبدء استخدام Bootstrap، يجب عليك إضافة ملفاته CSS و JavaScript إلى ملف HTML الخاص بك. هناك نهجين رئيسيين:

#### **الخيار 1: استخدام CDN (موصى به للبدء السريع)**
أضف الروابط التالية إلى ملف HTML الخاص بك:
- **CSS**: ضع هذا في قسم `<head>` لتحميل أنماط Bootstrap.
  ```html
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  ```
- **JavaScript**: ضع هذا قبل علامة `</body>` الخاتمة لتفعيل المكونات التفاعلية (مثل النوافذ المودال، القوائم المنسدلة).
  ```html
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  ```

**ملاحظة**: ملف `.bundle.min.js` يحتوي على Popper.js، الذي هو مطلوب لبعض مكونات Bootstrap مثل النصائح والتوضيحات. تأكد دائمًا من مراجعة [التوثيق الرسمي لBootstrap](https://getbootstrap.com/) للحصول على الروابط الأخيرة ل-CDN.

#### **الخيار 2: استضافة الملفات محليًا**
إذا كنت تفضل العمل دون اتصال بالإنترنت أو تحتاج إلى تعديل Bootstrap:
- قم بتنزيل ملفات Bootstrap من [الموقع الرسمي](https://getbootstrap.com/docs/5.3/getting-started/download/).
- استخرج ملفات CSS و JS إلى دليل مشروعك.
- ربطهم في ملف HTML الخاص بك:
  ```html
  <link rel="stylesheet" href="path/to/bootstrap.min.css">
  <script src="path/to/bootstrap.bundle.min.js"></script>
  ```

استخدام CDN غالبًا ما يكون أكثر راحة للمشاريع الصغيرة أو النموذج الأولي السريع.

---

### 3. **استخدام فئات و مكونات Bootstrap**
بعد إضافة Bootstrap، يمكنك استخدام فئاته لتسمية و تنظيم HTML الخاص بك.

#### **نظام الشبكة**
نظام الشبكة المكون من 12 عمودًا في Bootstrap يساعد في إنشاء تصاميم استجابة:
- استخدم `.container` لإنشاء تصاميم مركزية.
- استخدم `.row` لتحديد الصفوف و `.col` (مع نقاط التوقف مثل `col-md-4`) للعناصر.
مثال:
```html
<div class="container">
  <div class="row">
    <div class="col-md-4">عمود 1</div>
    <div class="col-md-4">عمود 2</div>
    <div class="col-md-4">عمود 3</div>
  </div>
</div>
```
- على الشاشات المتوسطة (`md`) و أكبر، يأخذ كل عمود 4 من 12 الوحدة (ثلث العرض).
- على الشاشات الصغيرة، يتم ترتيب العناصر عموديًا بشكل افتراضي. استخدم نقاط التوقف مثل `col-sm-`, `col-lg-`, إلخ. للحصول على مزيد من التحكم.

#### **المكونات**
Bootstrap يوفر عناصر واجهات المستخدم جاهزة للاستخدام. أمثلة:
- **زر**: أضف `.btn` و موديفاير مثل `.btn-primary`.
  ```html
  <button class="btn btn-primary">انقر علي</button>
  ```
- **شريط التنقل**: إنشاء شريط تنقل استجابة.
  ```html
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">العلامة التجارية</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="#">الرئيسية</a>
        </li>
      </ul>
    </div>
  </nav>
  ```
استكشف المزيد من المكونات (بطاقات، استمارات، نوافذ مودال، إلخ.) في التوثيق.

---

### 4. **تخصيص Bootstrap**
يمكن تعديل أنماط Bootstrap الافتراضية لتطابق تصميمك:
- **CSS مخصص**: غلب على الأنماط بإضافة ملف CSS خاص بك بعد رابط CSS لBootstrap.
  ```html
  <link rel="stylesheet" href="custom.css">
  ```
  مثال:
  ```css
  .btn-primary {
    background-color: #ff5733; /* لون برتقالي مخصص */
  }
  ```
- **متغيرات CSS (Bootstrap 5)**: قم بتعديل المواضيع باستخدام متغيرات CSS.
  ```css
  :root {
    --bs-primary: #ff5733;
    --bs-primary-rgb: 255, 87, 51;
  }
  ```
- **تخصيص Sass**: لمزيد من التغييرات المتقدمة، قم بتنزيل ملفات المصدر لBootstrap، قم بتحرير متغيرات Sass (مثل `$primary`), و إعادة تجميع CSS.

لأغلبية المشاريع، إضافة CSS مخصص يكون كافيًا.

---

### 5. **تأكد من الوصولية والأداء**
- **الوصولية**: Bootstrap يحتوي على بعض ميزات الوصولية (مثل معلمات ARIA)، ولكن استخدم HTML معاني (مثل `<nav>`, `<main>`) و اختبر باستخدام قراء الشاشة لضمان الالتزام.
- **الأداء**: يمكن أن تكون ملفات CSS و JS الكاملة لBootstrap كبيرة. لتفادي ذلك:
  - استخدم فقط المكونات التي تحتاجها بإنشاء بناء مخصص باستخدام ملفات Sass لBootstrap أو API المساعدة.
  - قم بإزالة الأنماط غير المستخدمة باستخدام أدوات مثل PurgeCSS.

---

### 6. **المرجع إلى التوثيق**
[التوثيق الرسمي لBootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) هو مصدرك الأساسي. يوفر:
- شرح تفصيلي لكل مكون.
- أمثلة رمزية للتمكن السريع.
- تحديثات حول أحدث الميزات وأفضل الممارسات.

---

### مثال: صفحة Bootstrap بسيطة
هنا ملف HTML أساسي باستخدام Bootstrap:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>مثال Bootstrap</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
  <div class="container">
    <h1 class="mt-4">مرحبًا، Bootstrap!</h1>
    <button class="btn btn-primary">انقر علي</button>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```
- فئة `mt-4` تضيف فراغًا في الأعلى.
- فئة `.btn.btn-primary` تحدد نمط الزر.

---

بالتتبع لهذه الخطوات - إضافة Bootstrap إلى مشروعك، استخدام فئاته، التخصيص حسب الحاجة، والتأكد من الأداء - يمكنك بناء واجهات المستخدم الحديثة الاستجابة بشكل فعال. ابدأ باستخدام طريقة CDN واستكشف التوثيق لتحرير كامل إمكانات Bootstrap!