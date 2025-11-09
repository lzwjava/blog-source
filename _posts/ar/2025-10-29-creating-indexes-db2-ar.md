---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إنشاء الفهارس في آي بي إم دي بي ٢
translated: true
type: note
---

### إنشاء الفهارس في IBM DB2

يدعم IBM DB2 الفهارس لتحسين أداء الاستعلامات من خلال السماح باسترجاع البيانات بسرعة أكبر. يمكن إنشاء الفهارس على عمود واحد أو أكثر من الجدول. أدناه، سأغطي الأساسيات، بما في ذلك الفهارس الفريدة والفهارس المركبة (متعددة الأعمدة). لاحظ أن مصطلح "فهرس الاتحاد" ليس مصطلحًا قياسيًا في وثائق DB2 — قد يشير إلى فهرس مركب (يغطي مفاتيح متعددة) أو إلى سوء فهم لعمليات الاتحاد في الاستعلامات. إذا كنت تقصد شيئًا آخر، قدم المزيد من التفاصيل!

#### إنشاء الفهرس الأساسي
استخدم عبارة `CREATE INDEX` لبناء فهرس بسيط على عمود واحد. هذا يسرع عمليات البحث والفرز والربط على ذلك العمود.

**البنية:**
```sql
CREATE INDEX index_name
ON table_name (column_name [ASC | DESC]);
```

**مثال:**
```sql
CREATE INDEX idx_employee_id
ON employees (employee_id ASC);
```

- `ASC` يرتب تصاعديًا (الافتراضي)؛ استخدم `DESC` للترتيب التنازلي.
- الفهارس غير فريدة بشكل افتراضي، مما يسمح بقيم مكررة.

#### الفهرس الفريد (فرض المفاتيح الفريدة)
يضمن الفهرس الفريد عدم وجود قيم مكورة في العمود (الأعمدة) المفهرس، شبيهًا بقيد التفرد. ينشئ DB2 فهرسًا فريدًا تلقائيًا عند تعريف مفتاح أساسي أو قيد تفرد.

**البنية:**
```sql
CREATE UNIQUE INDEX index_name
ON table_name (column_name [ASC | DESC]);
```

**مثال:**
```sql
CREATE UNIQUE INDEX uidx_email
ON users (email ASC);
```

- هذا يمنع إدخال عناوين بريد إلكتروني مكررة.
- للتفرد الجزئي (مثلًا، تجاهل قيم NULL)، أضف `WHERE NOT NULL`:  
  ```sql
  CREATE UNIQUE WHERE NOT NULL INDEX uidx_email
  ON users (email ASC);
  ```
- يمكنك تضمين أعمدة غير مفتاحية لتغطية الاستعلام:  
  ```sql
  CREATE UNIQUE INDEX uidx_email
  ON users (email ASC) INCLUDE (first_name, last_name);
  ```

#### الفهرس المركب (مفاتيح متعددة، مثل عمودين أو أكثر)
يغطي الفهرس المركب (أو متعدد الأعمدة) مفاتيح متعددة، وهو مفيد للاستعلامات التي تقوم بالتصفية/الربط على مجموعات من الأعمدة. ترتيب الأعمدة مهم — ضع العمود الأكثر انتقائية أولاً.

**البنية:**
```sql
CREATE INDEX index_name
ON table_name (column1 [ASC | DESC], column2 [ASC | DESC], ...);
```

**مثال (مفتاحان):**
```sql
CREATE INDEX idx_order_date_customer
ON orders (order_date ASC, customer_id DESC);
```

- هذا يحسن أداء استعلامات مثل `SELECT * FROM orders WHERE order_date > '2023-01-01' AND customer_id = 123;`.
- للفهرس المركب الفريد: أضف `UNIQUE` (مثل `CREATE UNIQUE INDEX ...`).

#### نصائح إضافية
- **التحقق من الفهرس:** استخدم `SELECT * FROM SYSCAT.INDEXES WHERE TABSCHEMA = 'YOUR_SCHEMA' AND TABNAME = 'YOUR_TABLE';`.
- **حذف الفهرس:** `DROP INDEX index_name;`.
- تستهلك الفهارس مساحة تخزين وتبطئ عمليات الإدخال/التحديث — استخدمها بحكمة.
- للجداول المقسمة أو الخيارات المتقدمة (مثل التجميع)، راجع وثائق DB2.

[Db2 CREATE INDEX Statement](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=statements-create-index)  
[Db2 Unique Indexes](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=attributes-unique-indexes)  
[Db2 Composite Indexes Example](https://stackoverflow.com/questions/21597015/composite-index-creation-in-db2)  
[Db2 Unique Index Tutorial](https://www.db2tutorial.com/db2-index/db2-unique-index/)