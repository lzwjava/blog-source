---
audio: false
generated: true
lang: ar
layout: post
title: استخدام مكتبة مومنت.جي إس في جافا سكريبت
translated: true
type: note
---

سأوضح لك كيفية استخدام مكتبتي `moment` و `moment-timezone` في JavaScript. هذه مكتبات شائعة للتعامل مع التواريخ والأوقات.

1. أولاً، قم بتثبيت الحزم إذا لم تكن قد قمت بذلك بالفعل:
```bash
npm install moment moment-timezone
```

2. أمثلة على الاستخدام الأساسي:

```javascript
// استيراد المكتبات
const moment = require('moment');
const momentTimezone = require('moment-timezone');

// الاستخدام الأساسي لـ Moment.js
// التاريخ والوقت الحاليان
const now = moment();
console.log(now.format('YYYY-MM-DD HH:mm:ss')); // على سبيل المثال، "2025-03-03 14:30:45"

// تحليل تاريخ محدد
const date = moment('2025-12-25');
console.log(date.format('MMMM Do YYYY')); // "December 25th 2025"

// معالجة التواريخ
const tomorrow = moment().add(1, 'days');
console.log(tomorrow.format('ddd, MMM D')); // على سبيل المثال، "Tue, Mar 4"

// استخدام Moment-Timezone
// الحصول على الوقت في منطقة زمنية محددة
const nyTime = momentTimezone.tz('America/New_York');
console.log(nyTime.format('YYYY-MM-DD HH:mm:ss z')); // يتضمن اختصار المنطقة الزمنية

// تحويل الوقت بين المناطق الزمنية
const localTime = moment();
const tokyoTime = localTime.clone().tz('Asia/Tokyo');
console.log(`Local: ${localTime.format('HH:mm')}`);
console.log(`Tokyo: ${tokyoTime.format('HH:mm')}`);

// سرد جميع المناطق الزمنية المتاحة
const timezones = momentTimezone.tz.names();
console.log(timezones); // مصفوفة بأسماء المناطق الزمنية
```

خيارات التنسيق الشائعة:
- `YYYY`: سنة مكونة من 4 أرقام (2025)
- `MM`: شهر مكون من رقمين (03)
- `DD`: يوم مكون من رقمين (03)
- `HH`: توقيت 24 ساعة (14)
- `hh`: توقيت 12 ساعة (02)
- `mm`: دقائق (30)
- `ss`: ثواني (45)
- `z`: اختصار المنطقة الزمنية

طرق مفيدة:
```javascript
// معالجة التاريخ
moment().add(7, 'days');     // إضافة وقت
moment().subtract(2, 'hours'); // طرح وقت
moment().startOf('month');   // بداية الفترة
moment().endOf('month');     // نهاية الفترة

// مقارنة التواريخ
moment().isBefore(date);
moment().isAfter(date);
moment().isSame(date);

// عمليات المنطقة الزمنية
momentTimezone.tz('2025-03-03', 'America/Los_Angeles');
momentTimezone.tz.guess(); // تخمين المنطقة الزمنية للمستخدم
```

ملاحظات:
1. هذه الإصدارات (^2.14.1 و ^0.5.7) قديمة جداً (من حوالي عام 2016). فكر في استخدام أحدث الإصدارات ما لم تكن لديك متطلبات توافق محددة.
2. Moment.js تعتبر الآن مشروعاً قديماً في وضع الصيانة. للمشاريع الجديدة، قد ترغب في النظر في بدائل مثل `date-fns` أو `luxon`.