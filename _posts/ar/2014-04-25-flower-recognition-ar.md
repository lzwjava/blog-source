---
audio: false
generated: false
image: false
lang: ar
layout: post
title: تطبيق التعرف على الزهور
translated: true
type: post
---

هذا هو README.md من مشروع GitHub [https://github.com/lzwjava/flower-recognition](https://github.com/lzwjava/flower-recognition).

---

### تطبيق التعرف على الزهور

هذا تطبيق Android للتعرف على الزهور مصمم لمساعدة المستخدمين في التعرف على الزهور من خلال التقاط الصور و رسم الدوائر لمساعدتهم في التعرف.

#### الميزات:
- **تقاط الصور**: يمكن للمستخدمين التقاط صور الزهور مباشرة داخل التطبيق.
- **وظيفة الرسم**: القدرة على رسم الدوائر و الملاحظات على صور الزهور لمساعدتهم في التعرف.
- **التحقق من الهوية**: التحقق من هوية المستخدم بشكل آمن مع شاشة تسجيل الدخول.
- **عرض النتائج**: عرض نتائج التعرف في واجهة مستخدم متعة.
- **تصميم المواد**: تطبيق مبادئ تصميم المواد للحصول على تجربة مستخدم حديثة ومفهومة.

#### بنية الملفات:
```
└── com
    └── lzw
        └── flower
            ├── activity
            │   ├── LoginActivity.java
            │   └── PhotoActivity.java
            ├── adapter
            │   └── PhotoAdapter.java
            ├── avobject
            │   └── Photo.java
            ├── base
            │   ├── App.java
            │   ├── ImageLoader.java
            │   └── SplashActivity.java
            ├── deprecated
            │   ├── CameraActivity.java
            │   └── Deprecated.java
            ├── draw
            │   ├── Draw.java
            │   ├── DrawActivity.java
            │   ├── DrawFragment.java
            │   ├── DrawView.java
            │   ├── HelpBtn.java
            │   ├── History.java
            │   ├── Tooltip.java
            │   └── ZoomImageView.java
            ├── fragment
            │   ├── RecogFragment.java
            │   └── WaitFragment.java
            ├── material
            │   └── MaterialActivity.java
            ├── result
            │   ├── FlowerAdapter.java
            │   ├── FlowerData.java
            │   ├── Image.java
            │   ├── ResultActivity.java
            │   └── ResultFragment.java
            ├── service
            │   └── PhotoService.java
            ├── utils
            │   ├── BitmapUtils.java
            │   ├── Crop.java
            │   ├── ImageListDialogBuilder.java
            │   ├── Logger.java
            │   ├── PathUtils.java
            │   └── Utils.java
            └── web
                ├── Upload.java
                ├── UploadImage.java
                └── Web.java
```

#### المكونات:
- **الأنشطة**: يحتوي على صفوف لتعامل مع الأنشطة المختلفة للحساب مثل تسجيل الدخول، التقاط الصور، و شاشة النقر.
- **المفوضات**: يدير عرض الصور و نتائج التعرف.
- **AVObject**: يمثل كائنات الصور مع البيانات الفرعية المرتبطة.
- **الرسوم**: صفوف مرتبطة بالرسوم الدوائر والملاحظات على صور الزهور.
- **القطع**: يوفر المكونات الواجهة المستخدمية لعرض نتائج التعرف و مؤشرات الانتظار.
- **المواد**: قد يكون مرتبطاً بتعليمات تصميم المواد.
- **الخدمات**: يدير المهام الخلفية و تعديل البيانات المتعلقة بالصور.
- **صادرات**: يحتوي على صفوف المساعدة لمهام مختلفة مثل معالجة الصور و التسجيل.

#### الاستخدام:
1. قم بتعليقات المراجع.
2. افتح المشروع في Android Studio.
3. قم ببناء وتنفيذ التطبيق على جهاز أندرويد أو جهاز محاكي.

#### الرخصة:
تم ترخيص هذا المشروع تحت [رخصة MIT](LICENSE).