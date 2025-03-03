---
audio: false
generated: true
lang: ar
layout: post
title: استخدام مومنت.جاي في جافاسكريبت
translated: true
---

سأريك كيفية استخدام مكتبات `moment` و `moment-timezone` في JavaScript. هذه المكتبات شائعة في معالجة التواريخ والأوقات.

1. أولاً، قم بتثبيت الحزم إذا لم تفعل ذلك بالفعل:
```bash
npm install moment moment-timezone
```

2. أمثلة استخدام أساسي:

```javascript
// استيراد المكتبات
const moment = require('moment');
const momentTimezone = require('moment-timezone');

// استخدام Moment.js الأساسي
// التاريخ الحالي والوقت الحالي
const now = moment();
console.log(now.format('YYYY-MM-DD HH:mm:ss')); // مثلا، "2025-03-03 14:30:45"

// تحليل تاريخ محدد
const date = moment('2025-12-25');
console.log(date.format('MMMM Do YYYY')); // "December 25th 2025"

// تعديل التواريخ
const tomorrow = moment().add(1, 'days');
console.log(tomorrow.format('ddd, MMM D')); // مثلا، "Tue, Mar 4"

// استخدام Moment-Timezone
// الحصول على الوقت في منطقة زمنية محددة
const nyTime = momentTimezone.tz('America/New_York');
console.log(nyTime.format('YYYY-MM-DD HH:mm:ss z')); // يتضمن اختصار المنطقة الزمنية

// تحويل الوقت بين المناطق الزمنية
const localTime = moment();
const tokyoTime = localTime.clone().tz('Asia/Tokyo');
console.log(`Local: ${localTime.format('HH:mm')}`);
console.log(`Tokyo: ${tokyoTime.format('HH:mm')}`);

// قائمة جميع المناطق الزمنية المتاحة
const timezones = momentTimezone.tz.names();
console.log(timezones); // مصفوفة أسماء المناطق الزمنية
```

خيارات التنسيق الشائعة:
- `YYYY`: سنة 4 أرقام (2025)
- `MM`: شهر 2 أرقام (03)
- `DD`: يوم 2 أرقام (03)
- `HH`: ساعة 24 (14)
- `hh`: ساعة 12 (02)
- `mm`: دقائق (30)
- `ss`: ثوان (45)
- `z`: اختصار المنطقة الزمنية

أدوات مفيدة:
```javascript
// تعديل التاريخ
moment().add(7, 'days');     // إضافة زمن
moment().subtract(2, 'hours'); // استخراج زمن
moment().startOf('month');   // بداية الفترة
moment().endOf('month');     // نهاية الفترة

// مقارنة التواريخ
moment().isBefore(date);
moment().isAfter(date);
moment().isSame(date);

// عمليات المنطقة الزمنية
momentTimezone.tz('2025-03-03', 'America/Los_Angeles');
momentTimezone.tz.guess(); // تخمين منطقة زمنية المستخدم
```

ملاحظات:
1. هذه الإصدارات (^2.14.1 و ^0.5.7) قديمة جدًا (من حوالي 2016). افترض استخدام أحدث الإصدارات ما لم يكن لديك متطلبات توافق محددة.
2. الآن يُعتبر Moment.js مشروعًا قديمًا في وضع الصيانة. بالنسبة للمشاريع الجديدة، قد ترغب في النظر في البدائل مثل `date-fns` أو `luxon`.