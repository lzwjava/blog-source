---
audio: false
date: 2025-09-07
generated: true
image: false
lang: ar
layout: post
title: إصلاح طلبات خطوط جوجل المحظورة
translated: true
type: note
---

هذا الطلب هو محاولة صفحتك لتحميل ورقة أنماط خطوط ويب من Google Fonts:

* **ما هو:** `https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap` هو CSS الذي يعرّف وجوه خط **Open Sans**. سمة موقعك أو CSS المخصص يضمّنه حتى يتمكن الموقع من العرض باستخدام Open Sans.
* **لماذا ترى "الحالة: — / 0 بايت / لا توجد رؤوس":** تظهر DevTools ذلك عندما يتم **حظر الطلب أو إلغاؤه** (على سبيل المثال، بواسطة مانع إعلانات/خصوصية، أو سياسة أمان محتوى صارمة، أو شبكة غير مستقرة، أو حظر على مستوى الدولة). الصفحة لا تزال *تحاول* طلبه، ومن هنا يأتي السطر في الشبكة.

### من أين يأتي على الأرجح في مدونة Jekyll

عادةً ما يكون أحد هذه الخيارات صحيحًا:

1. **السمة تضمنه في `<head>`**
   ابحث عن سطر مثل
   `<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap" rel="stylesheet">`
   في `_layouts/default.html` أو `_includes/head.html` (أو ما يعادلها في السمة إذا كنت تستخدم `remote_theme`).

2. **SCSS تستورده**
   افحص `/assets/css/*.scss` أو `/_sass/**` بحثًا عن
   `@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap");`

3. **السمة البعيدة** (مثل jekyll-theme-cayman) تدرج خطوط Google Fonts مباشرة في ملف الرأس الخاص بها. سيسمح لك تجاوز ملف الرأس/التخطيط للسمة في مستودعك بإزالته.

### كيفية العثور عليه بسرعة

من جذر مستودع موقعك، جرب أيًا من:

```
rg -n "fonts.googleapis.com"
rg -n "Open Sans"
rg -n "display=swap"
```

### خيارات لإصلاحه أو تغييره

**أ) إزالة خطوط Google واستخدام مجموعة خطوط نظام (الأسرع والأكثر احترامًا للخصوصية)**

1. احذف الوسم `<link>` (أو قاعدة `@import` في SCSS) الذي يجلب خطوط Google.
2. في ورقة الأنماط الرئيسية الخاصة بك، عيّن مجموعة خطوط نظام:

   ```css
   html, body {
     font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu,
                  "Helvetica Neue", Arial, "Noto Sans", sans-serif,
                  "Apple Color Emoji", "Segoe UI Emoji";
   }
   ```

   (في Jekyll، ضع هذا في `assets/css/style.scss` مع وجود سطور front-matter `---` في الأعلى.)

**ب) الاحتفاظ بـ Open Sans ولكن استضافته ذاتيًا**

1. حمّل ملفات WOFF2 لـ Open Sans (400 و 700) وضعها في `assets/fonts/`.
2. أضف إلى CSS الخاص بك:

   ```css
   @font-face {
     font-family: "Open Sans";
     font-style: normal;
     font-weight: 400;
     font-display: swap;
     src: url("/assets/fonts/OpenSans-400.woff2") format("woff2");
   }
   @font-face {
     font-family: "Open Sans";
     font-style: normal;
     font-weight: 700;
     font-display: swap;
     src: url("/assets/fonts/OpenSans-700.woff2") format("woff2");
   }
   body { font-family: "Open Sans", system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; }
   ```
3. احذف الوسم `<link>`/`@import` الخاص بـ Google Fonts.

**ج) اتركه كما هو ولكن أوقف فشل الطلب**

* عطّل إضافة الحظر لموقعك، أو خفّض سياسة أمان المحتوى للسماح بـ `https://fonts.googleapis.com` و `https://fonts.gstatic.com`.
* إذا كنت في منطقة يتم فيها حظر هذه النطاقات، فافضل الخيار أ أو ب.

### نصائح تجاوز محددة لـ Jekyll

* **السمة البعيدة:** انسخ `/_includes/head.html` أو `/_layouts/default.html` من السمة إلى مستودعك بنفس المسار، احذف سطر Google Fonts، وسيستخدم Jekyll النسخة المتجاوزة الخاصة بك.
* **ملف رأس مضغوط:** أحيانًا تقوم السمة بحقن الخطوط عبر متغير. إذا كان الأمر كذلك، عيّن هذا المتغير ليصبح فارغًا أو تجاوز الملف المضمن لاستبعاد الخطوط.

إذا قمت بلصق اسم سمتك (أو `theme` / `remote_theme` من ملف `_config.yml` الخاص بك) يمكنني إظهار الملف المحدد الذي يجب تجاوزه وفرق التغييرات الأدنى.