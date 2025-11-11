---
audio: false
generated: true
lang: ar
layout: post
title: استخدام Bootstrap لبناء مواقع ويب متجاوبة
translated: true
type: note
---

لاستخدام Bootstrap في تطوير الواجهات الأمامية، اتبع هذه الخطوات لدمج واستغلال هذا الإطار العمل الشعبي بفعالية لبناء مواقع ويب مستجيبة ومصممة:

### 1. **افهم ما هو Bootstrap**
Bootstrap هو إطار عمل front-end واسع الانتشار مصمم لتبسيط إنشاء مواقع ويب مستجيبة وموجهة للهواتف المحمولة أولاً. يقدم:
- **مكونات مصممة مسبقًا**: أزرار، أشرطة تنقل، نماذج، بطاقات، نوافذ مشروحة، والمزيد.
- **نظام شبكي**: لإنشاء تخطيطات مرنة تتكيف مع أحجام الشاشات المختلفة.
- **CSS و JavaScript**: لوظائف التصميم والتفاعل.

بإدراج Bootstrap في مشروعك، يمكنك بناء واجهات المستخدم بسرعة دون الحاجة لكتابة CSS أو JavaScript مخصصة موسعة.

---

### 2. **أضف Bootstrap إلى HTML الخاص بك**
لبدء استخدام Bootstrap، تحتاج إلى إضافة ملفات الـ CSS والـ JavaScript الخاصة به إلى HTML الخاص بك. هناك طريقتان رئيسيتان:

#### **الخيار 1: استخدام CDN (موصى به للبدء السريع)**
أضف الروابط التالية إلى ملف HTML الخاص بك:
- **CSS**: ضع هذا في قسم `<head>` لتحميل أنماط Bootstrap.
  ```html
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  ```
- **JavaScript**: ضع هذا قبل وسم إغلاق `</body>` لتمكين المكونات التفاعلية (مثل النوافذ المشروحة، القوائم المنسدلة).
  ```html
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  ```

**ملاحظة**: ملف `.bundle.min.js` يتضمن Popper.js، وهو مطلوب لبعض مكونات Bootstrap مثل التلميحات والنوافذ المنبثقة. تحقق دائمًا من [توثيق Bootstrap الرسمي](https://getbootstrap.com/) للحصول على أحدث روابط CDN.

#### **الخيار 2: استضافة الملفات محليًا**
إذا كنت تفضل العمل دون اتصال بالإنترنت أو تحتاج إلى تخصيص Bootstrap:
- حمل ملفات Bootstrap من [الموقع الرسمي](https://getbootstrap.com/docs/5.3/getting-started/download/).
- استخرج ملفات CSS و JS إلى دليل مشروعك.
- اربطها في HTML الخاص بك:
  ```html
  <link rel="stylesheet" href="path/to/bootstrap.min.css">
  <script src="path/to/bootstrap.bundle.min.js"></script>
  ```

عادةً ما يكون استخدام CDN أكثر ملاءمة للمشاريع الصغيرة أو النماذج الأولية السريعة.

---

### 3. **استخدم فئات ومكونات Bootstrap**
بمجرد إدراج Bootstrap، يمكنك استخدام فئاته لتصميم وهيكلة HTML الخاص بك.

#### **النظام الشبكي**
يساعد نظام الأعمدة الـ 12 في Bootstrap على إنشاء تخطيطات مستجيبة:
- استخدم `.container` للحصول على تخطيط مركزي.
- استخدم `.row` لتحديد الصفوف و `.col` (مع نقاط التوقف مثل `col-md-4`) للأعمدة.
مثال:
```html
<div class="container">
  <div class="row">
    <div class="col-md-4">العمود 1</div>
    <div class="col-md-4">العمود 2</div>
    <div class="col-md-4">العمود 3</div>
  </div>
</div>
```
- على الشاشات المتوسطة (`md`) وما فوق، يأخذ كل عمود 4 وحدات من أصل 12 (ثلث العرض).
- على الشاشات الأصغر، تتراكم الأعمدة رأسيًا افتراضيًا. استخدم نقاط التوقف مثل `col-sm-`، `col-lg-`، إلخ. لمزيد من التحكم.

#### **المكونات**
يوفر Bootstrap عناصر واجهة مستخدم جاهزة للاستخدام. أمثلة:
- **زر**: أضف `.btn` ومعدل مثل `.btn-primary`.
  ```html
  <button class="btn btn-primary">انقر هنا</button>
  ```
- **شريط التنقل**: أنشئ شريط تنقل مستجيب.
  ```html
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">العلامة</a>
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
استكشف المزيد من المكونات (البطاقات، النماذج، النوافذ المشروحة، إلخ.) في التوثيق.

---

### 4. **خصص Bootstrap**
يمكن تخصيص الأنماط الافتراضية لـ Bootstrap لتتناسب مع تصميمك:
- **CSS مخصص**: تجاوز الأنماط بإضافة ملف CSS الخاص بك بعد رابط CSS الخاص بـ Bootstrap.
  ```html
  <link rel="stylesheet" href="custom.css">
  ```
  مثال:
  ```css
  .btn-primary {
    background-color: #ff5733; /* لون برتقالي مخصص */
  }
  ```
- **متغيرات CSS (Bootstrap 5)**: عدل السمات باستخدام متغيرات CSS.
  ```css
  :root {
    --bs-primary: #ff5733;
    --bs-primary-rgb: 255, 87, 51;
  }
  ```
- **تخصيص Sass**: لإجراء تغييرات متقدمة، حمل ملفات مصدر Bootstrap، وقم بتعديل متغيرات Sass (مثل `$primary`)، وأعد تجميع CSS.

لمعظم المشاريع، إضافة CSS مخصص يكون كافيًا.

---

### 5. **تأكد من إمكانية الوصول والأداء**
- **إمكانية الوصول**: يتضمن Bootstrap بعض ميزات إمكانية الوصول (مثل سمات ARIA)، لكن استخدم HTML الدلالي (مثل `<nav>`، `<main>`) واختبر باستخدام قارئات الشاشة لضمان الامتثال.
- **الأداء**: يمكن أن تكون ملفات CSS و JS الكاملة لـ Bootstrap كبيرة. لتحسين الأداء:
  - استخدم فقط المكونات التي تحتاجها عن طريق إنشاء بناء مخصص باستخدام ملفات Sass الخاصة بـ Bootstrap أو واجهة برمجة التطبيقات المساعدة.
  - أزل الأنماط غير المستخدمة بأدوات مثل PurgeCSS.

---

### 6. **راجع التوثيق**
[توثيق Bootstrap الرسمي](https://getbootstrap.com/docs/5.3/getting-started/introduction/) هو مصدرك الأساسي. يوفر:
- شروحات مفصلة لجميع المكونات.
- أمثلة كود للتنفيذ السريع.
- تحديثات حول أحدث الميزات وأفضل الممارسات.

---

### مثال: صفحة Bootstrap بسيطة
إليك ملف HTML أساسي يستخدم Bootstrap:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bootstrap Example</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
  <div class="container">
    <h1 class="mt-4">مرحبًا، Bootstrap!</h1>
    <button class="btn btn-primary">انقر هنا</button>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```
- فئة `mt-4` تضيف تباعد هامش علوي.
- فئة `.btn.btn-primary` تصمم الزر.

---

باتباع هذه الخطوات — إضافة Bootstrap إلى مشروعك، واستخدام فئاته، وتخصيصه حسب الحاجة، وتحسين الأداء — يمكنك بناء واجهات أمامية حديثة ومستجيبة بكفاءة. ابدأ بطريقة CDN واستكشف التوثيق لتحرير الإمكانات الكاملة لـ Bootstrap!