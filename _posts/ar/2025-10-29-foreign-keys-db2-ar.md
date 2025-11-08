---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إنشاء المفاتيح الخارجية في Db2
translated: true
type: note
---

### إنشاء المفاتيح الخارجية في IBM Db2

تفرض المفاتيح الخارجية في Db2 تكامل المرجعية من خلال ربط عمود (أو مجموعة أعمدة) في جدول واحد (الجدول الفرعي) بالمفتاح الأساسي أو المفتاح الفريد في جدول آخر (الجدول الأصلي). وهذا يضمن أن القيم في الجدول الفرعي تتطابق مع القيم الموجودة في الجدول الأصلي، مما يمنع السجلات اليتيمة.

يمكنك تعريف المفاتيح الخارجية إما أثناء إنشاء الجدول باستخدام `CREATE TABLE` أو بإضافتها إلى جدول موجود باستخدام `ALTER TABLE`. بناء الجملة هو SQL قياسي ويعمل عبر منصات Db2 (مثل LUW, z/OS).

#### 1. تعريف مفتاح خارجي أثناء إنشاء الجدول (`CREATE TABLE`)
استخدم بند `FOREIGN KEY` ضمن تعريفات الأعمدة أو في نهاية تعريف الجدول.

**بناء الجملة الأساسي:**
```
CREATE TABLE child_table (
    child_column1 datatype,
    foreign_key_column datatype,
    -- أعمدة أخرى...
    CONSTRAINT constraint_name
    FOREIGN KEY (foreign_key_column) 
    REFERENCES parent_table (parent_key_column)
);
```

**مثال:**
افترض أن لديك جدول `departments` بمفتاح أساسي `dept_id`:
```
CREATE TABLE departments (
    dept_id INTEGER NOT NULL PRIMARY KEY,
    dept_name VARCHAR(50)
);
```

الآن قم بإنشاء جدول `employees` بمفتاح خارجي يشير إلى `dept_id`:
```
CREATE TABLE employees (
    emp_id INTEGER NOT NULL PRIMARY KEY,
    emp_name VARCHAR(100),
    dept_id INTEGER,
    CONSTRAINT fk_emp_dept 
    FOREIGN KEY (dept_id) 
    REFERENCES departments (dept_id)
);
```

هذا ينشئ مفتاحًا خارجيًا باسم `fk_emp_dept` على `dept_id` في `employees`.

#### 2. إضافة مفتاح خارجي إلى جدول موجود (`ALTER TABLE`)
استخدم `ALTER TABLE` لإضافة القيد بعد وجود الجدول. يجب أن يكون المفتاح الأصلي موجودًا مسبقًا.

**بناء الجملة الأساسي:**
```
ALTER TABLE child_table 
ADD CONSTRAINT constraint_name 
FOREIGN KEY (foreign_key_column) 
REFERENCES parent_table (parent_key_column);
```

**مثال:**
لإضافة نفس المفتاح الخارجي إلى جدول `employees` موجود:
```
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) 
REFERENCES departments (dept_id);
```

#### خيارات إضافية
يمكنك تحديد الإجراءات لما يحدث عند تحديث أو حذف صف أصلي:
- `ON DELETE CASCADE`: يحذف الصفوف الفرعية عند حذف الصف الأصلي.
- `ON DELETE SET NULL`: يضبط المفتاح الخارجي على NULL في الصفوف الفرعية.
- `ON UPDATE CASCADE`: يقوم بتحديث المفاتيح الفرعية عند تغيير المفتاح الأصلي.
- `ON UPDATE SET NULL`: يضبط على NULL عند تحديث المفتاح الأصلي.

**مثال مع الخيارات:**
```
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) 
REFERENCES departments (dept_id)
ON DELETE CASCADE
ON UPDATE RESTRICT;
```

#### القواعد والاعتبارات الرئيسية
- يجب أن تتطابق أعمدة المفتاح الخارجي مع نوع البيانات وطول أعمدة المفتاح الأصلي.
- يجب أن يكون للجدول الأصلي مفتاح أساسي أو فريد محدد قبل إنشاء المفتاح الخارجي.
- يمكن أن تشير المفاتيح الخارجية إلى نفس الجدول (مرجعية ذاتية).
- يمكن أن تشكل أعمدة متعددة مفتاحًا خارجيًا مركبًا: `FOREIGN KEY (col1, col2) REFERENCES parent (pk1, pk2)`.
- لحذف مفتاح خارجي: `ALTER TABLE child_table DROP CONSTRAINT constraint_name;`.
- يُوصى بإنشاء فهرس على أعمدة المفتاح الخارجي لتحسين الأداء.

اختبر في بيئة تطوير، حيث قد تفشل إضافة القيود إذا كانت البيانات الموجودة تنتهكها (مثل الصفوف اليتيمة).

#### المراجع
- [Foreign key (referential) constraints - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=constraints-foreign-key-referential)
- [CREATE TABLE statement - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=statements-create-table)
- [ALTER TABLE statement - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=statements-alter-table)
- [Adding a foreign key with Db2 - Stack Overflow](https://stackoverflow.com/questions/59370149/adding-a-foreign-key-with-db2-of-ibm)