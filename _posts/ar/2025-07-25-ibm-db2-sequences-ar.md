---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast:free
title: دليل استخدام التسلسل في آي بي إم دي بي ٢
translated: true
type: note
---

### استخدام التسلسل في IBM DB2 مع NEXT VALUE FOR

في IBM DB2، يُستخدم `NEXT VALUE FOR` لاسترداد القيمة التالية من التسلسل، والذي يُولّد أرقامًا فريدة ومتزايدة. تُعد التسلسلات مفيدة لتوليد المفاتيح الأساسية أو معرّفات فريدة أخرى.

#### مثال: إنشاء تسلسل واستخدامه
1. **إنشاء التسلسل** (نفّذ هذا مرة واحدة في بيئة DB2 الخاصة بك):
   ```sql
   CREATE SEQUENCE my_sequence
   START WITH 1
   INCREMENT BY 1
   NO CYCLE;
   ```
   - ينشئ هذا تسلسلاً باسم `my_sequence` يبدأ بالرقم 1 ويزيد بمقدار 1 في كل مرة.

2. **استخدم التسلسل في عبارة INSERT** للحصول على القيمة التالية:
   ```sql
   INSERT INTO employees (id, name, department)
   VALUES (NEXT VALUE FOR my_sequence, 'Alice Johnson', 'Engineering');
   ```
   - يُدخل هذا صفًا جديدًا حيث يكون `id` هو قيمة التسلسل التالية (مثال: 1 عند الاستخدام الأول، 2 عند الاستخدام التالي، إلخ).

#### ملاحظات رئيسية
- يمكنك أيضًا استخدامه في استعلامات SELECT: `SELECT NEXT VALUE FOR my_sequence FROM SYSIBM.SYSDUMMY1;`
- التسلسلات منفصلة عن الجداول ويمكن مشاركتها عبر جداول متعددة إذا لزم الأمر.
- لمزيد من التفاصيل، راجع وثائق IBM DB2 حول التسلسلات. إذا كنت بحاجة إلى أمثلة لوظائف التسلسل الأخرى مثل `PREVIOUS VALUE FOR`، فأعلمني!