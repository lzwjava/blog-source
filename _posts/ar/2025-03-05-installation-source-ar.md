---
audio: false
generated: true
lang: ar
layout: post
title: مصدر التثبيت لمجموعات npm
translated: true
---

للتغيير مصدر التثبيت لـ `@ngx-formly/bootstrap` من ملف `.tgz` محلي إلى سجل npm، اتبع هذه الخطوات:

### 1. إلغاء تثبيت الحزمة المحللة
لأنك قد قمت بتثبيت `@ngx-formly/bootstrap` من ملف `.tgz` محلي، فهو حاليًا في مجلد `node_modules` لمشروعك. لإزالةه، قم بتشغيل الأمر التالي في شريط الأوامر:

```bash
npm uninstall @ngx-formly/bootstrap
```

يؤدي هذا الأمر إلى إزالة الحزمة من `node_modules`. إذا كان الحزمة قد أضيفت يدويًا إلى ملف `package.json` تحت `dependencies` أو `devDependencies`، فسيؤدي ذلك أيضًا إلى إزالتها من هناك. إذا لم يكن مدرجًا في `package.json` (شائع عند تثبيت من ملف `.tgz` دون حفظ)، فإنه سيظل مرفوعًا من مشروعك.

### 2. تثبيت الحزمة من سجل npm
الآن، قم بتثبيت الحزمة من سجل npm عن طريق تشغيل:

```bash
npm install @ngx-formly/bootstrap
```

يؤدي هذا الأمر إلى جلب أحدث إصدار لـ `@ngx-formly/bootstrap` من سجل npm (عادةً `https://registry.npmjs.org/` ما لم تقم بتكوين سجل آخر) وتثبيته في مجلد `node_modules`. وسيضيف الحزمة أيضًا إلى ملف `package.json` تحت `dependencies` بشكل افتراضي (في إصدارات npm الأخيرة)، مما يضمن تتبعها كجزء من مشروعك.

### اختياري: التحقق من السجل (إذا لزم الأمر)
إذا قمت سابقًا بتغيير سجل npm وريديك التأكد من أنه مقسم إلى سجل npm الافتراضي، يمكنك التحقق منه باستخدام:

```bash
npm config get registry
```

إذا كان الإخراج هو `https://registry.npmjs.org/`, فأنت تستخدم السجل الافتراضي، وسيعمل الأمر `npm install` كما هو متوقع. إذا كان مقسمًا إلى سجل آخر وريديك العودة إلى السجل الافتراضي، قم بتشغيل:

```bash
npm config set registry https://registry.npmjs.org/
```

ومع ذلك، نظرًا لأنك ذكرت أنك قمت بالفعل بتكوين سجلك، قد لا يكون هذا الخطو ضروريًا.

### ملاحظات
- **التحكم في الإصدار**: إذا كنت تحتاج إلى نفس الإصدار الذي في ملف `.tgz`, تحقق من رقم الإصدار في `node_modules/@ngx-formly/bootstrap/package.json` قبل إلغاء التثبيت. ثم قم بتثبيت ذلك الإصدار المحدد باستخدام:
  ```bash
  npm install @ngx-formly/bootstrap@<version>
  ```
  إذا لم تقم بتحديد إصدار، فسيتم تثبيت أحدث إصدار من السجل.
- **نوع التبعية**: إذا كنت تريد الحزمة كتعليمة تطويرية بدلاً من تعليمة عادية، استخدم:
  ```bash
  npm install @ngx-formly/bootstrap --save-dev
  ```

بالتتبع لهذه الخطوات، ستنجح في تغيير `@ngx-formly/bootstrap` من التثبيت من ملف `.tgz` محلي إلى التثبيت من سجل npm.