---
audio: false
generated: true
lang: ar
layout: post
title: عبارات SQL SELECT
translated: true
type: note
---

للإجابة على استفسارك حول كيفية استخدام `SELECT`، و`LEFT JOIN`، و`RIGHT JOIN`، و`SELECT` المعقد، و`FROM`، و`GROUP BY`، و`WHERE NOT IN`، و`IN` في SQL، سأشرح كل مكون بوضوح وأقدم أمثلة عملية. هذه عمليات SQL أساسية تُستخدم لاسترداد البيانات ومعالجتها من قواعد البيانات. دعونا نفككها خطوة بخطوة، باستخدام مخطط قاعدة بيانات بسيط للاتساق:

- **الجداول:**
  - `employees` (الأعمدة: `employee_id`, `employee_name`, `department_id`, `salary`)
  - `departments` (الأعمدة: `department_id`, `department_name`)
  - `projects` (الأعمدة: `project_id`, `project_name`, `employee_id`)

---

### 1. SELECT
يُستخدم بند `SELECT` لتحديد الأعمدة التي تريد استردادها من جدول قاعدة البيانات. وهو يشكل الأساس لأي استعلام SQL.

- **الغرض:** اختيار البيانات المراد عرضها.
- **مثال:**
  ```sql
  SELECT employee_name, salary
  FROM employees;
  ```
  يسترد هذا الأعمدة `employee_name` و `salary` من جدول `employees`.

---

### 2. FROM
يحدد بند `FROM` الجدول (أو الجداول) الذي سيتم سحب البيانات منه. يُستخدم دائمًا مع `SELECT`.

- **الغرض:** تحديد مصدر البيانات.
- **مثال:**
  ```sql
  SELECT employee_name
  FROM employees;
  ```
  هنا، `employees` هو الجدول الذي يتم الاستعلام عنه.

---

### 3. LEFT JOIN
يجمع `LEFT JOIN` (أو `LEFT OUTER JOIN`) بين صفوف جدولين. حيث يعيد جميع السجلات من الجدول الأيسر والسجلات المطابقة من الجدول الأيمن. إذا لم يكن هناك تطابق، تتضمن النتيجة قيم `NULL` لأعمدة الجدول الأيمن.

- **الغرض:** تضمين جميع الصفوف من الجدول الأيسر، بغض النظر عن وجود تطابقات في الجدول الأيمن.
- **مثال:**
  ```sql
  SELECT e.employee_name, d.department_name
  FROM employees e
  LEFT JOIN departments d
  ON e.department_id = d.department_id;
  ```
  يسرد هذا جميع الموظفين وأسماء أقسامهم. إذا لم يكن الموظف معينًا لقسم، فسيكون `department_name` هو `NULL`.

---

### 4. RIGHT JOIN
يشبه `RIGHT JOIN` (أو `RIGHT OUTER JOIN`) `LEFT JOIN`، لكنه يعيد جميع السجلات من الجدول الأيمن والسجلات المطابقة من الجدول الأيسر. تؤدي الصفوف غير المطابقة في الجدول الأيسر إلى قيم `NULL`.

- **الغرض:** تضمين جميع الصفوف من الجدول الأيمن، بغض النظر عن وجود تطابقات في الجدول الأيسر.
- **مثال:**
  ```sql
  SELECT e.employee_name, d.department_name
  FROM employees e
  RIGHT JOIN departments d
  ON e.department_id = d.department_id;
  ```
  يظهر هذا جميع الأقسام وموظفيها. الأقسام التي لا يوجد بها موظفون سيكون لها `NULL` في `employee_name`.

---

### 5. SELECT المعقد
"`SELECT` المعقد" ليس مصطلحًا رسميًا في SQL، لكنه يشير عادةً إلى عبارة `SELECT` التي تجمع بين عدة بنود، وعمليات ربط، واستعلامات فرعية، أو دوال تجميعية لتنفيذ استرداد بيانات متقدم.

- **الغرض:** التعامل مع الاستعلامات المعقدة التي تتضمن عمليات متعددة.
- **مثال:**
  ```sql
  SELECT d.department_name, COUNT(e.employee_id) AS employee_count
  FROM departments d
  LEFT JOIN employees e
  ON d.department_id = e.department_id
  GROUP BY d.department_name
  HAVING COUNT(e.employee_id) > 5;
  ```
  يجد هذا الأقسام التي لديها أكثر من 5 موظفين، عن طريق حساب عدد الموظفين في كل قسم وتصفية النتائج.

---

### 6. GROUP BY
يُجمع بند `GROUP BY` الصفوف التي لها نفس القيم في أعمدة محددة في صفوف ملخصة، وغالبًا ما يُستخدم مع دوال التجميع مثل `COUNT` أو `SUM` أو `AVG`.

- **الغرض:** تجميع البيانات بناءً على قيم العمود.
- **مثال:**
  ```sql
  SELECT department_id, COUNT(employee_id) AS employee_count
  FROM employees
  GROUP BY department_id;
  ```
  يحسب هذا عدد الموظفين في كل قسم.

---

### 7. WHERE NOT IN
يصفّي بند `WHERE NOT IN` الصفوف التي لا توجد قيمة العمود الخاص بها في قائمة محددة أو نتيجة استعلام فرعي. كن حذرًا: إذا احتوت القائمة/الاستعلام الفرعي على `NULL`، فقد لا تُعيد أي صفوف.

- **الغرض:** استبعاد الصفوف بناءً على مجموعة من القيم.
- **مثال:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id NOT IN (1, 2);
  ```
  يسترد هذا الموظفين غير الموجودين في القسمين 1 أو 2.

- **مع الاستعلام الفرعي:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id NOT IN (SELECT department_id FROM departments WHERE department_name = 'Inactive');
  ```
  يجد هذا الموظفين غير الموجودين في الأقسام المُعلَمة باسم 'Inactive'.

---

### 8. IN
يصفّي بند `IN` الصفوف التي تطابق قيمة العمود الخاص بها أي قيمة في قائمة أو استعلام فرعي. إنه اختصار لشروط `OR` المتعددة.

- **الغرض:** تضمين الصفوف بناءً على مجموعة من القيم.
- **مثال:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id IN (3, 4);
  ```
  يسترد هذا الموظفين الموجودين في القسمين 3 أو 4.

- **مع الاستعلام الفرعي:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id IN (
      SELECT department_id
      FROM employees
      GROUP BY department_id
      HAVING COUNT(employee_id) > 5
  );
  ```
  يجد هذا الموظفين في الأقسام التي بها أكثر من 5 موظفين.

---

### جمع كل شيء معًا
إليك مثالاً يجمع بين عدة من هذه العمليات:
```sql
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
WHERE e.department_id NOT IN (1, 2)
GROUP BY d.department_name;
```
- **الشرح:**
  - `FROM departments d`: يبدأ بجدول `departments`.
  - `LEFT JOIN employees e`: يتضمن جميع الأقسام، حتى تلك التي لا تحتوي على موظفين.
  - `WHERE NOT IN (1, 2)`: يستبعد الموظفين من القسمين 1 و 2.
  - `GROUP BY d.department_name`: يُجمع النتائج حسب اسم القسم.
  - `SELECT ... COUNT`: يحسب عدد الموظفين في كل قسم.

---

### نصائح رئيسية
- **عمليات الربط (Joins):** اختر `LEFT JOIN` أو `RIGHT JOIN` بناءً على الصفوف التي تريد الاحتفاظ بها بالكامل (اليسار أو اليمين).
- **قيم NULL مع NOT IN:** إذا أعاد استعلام فرعي `NULL`، فقد يستبعد `NOT IN` جميع الصفوف بشكل غير متوقع. فكّر في استخدام `NOT EXISTS` كبديل.
- **الاستعلامات المعقدة:** قسّمها إلى أجزاء (على سبيل المثال، اختبر عمليات الربط بشكل منفصل) لضمان صحتها.
- **ترتيب البنود:** ضع `WHERE` قبل `GROUP BY`، واستخدم `HAVING` بعد `GROUP BY` لتصفية مستوى المجموعة.

من خلال فهم ومزج هذه المكونات في SQL—`SELECT`، و`FROM`، و`LEFT JOIN`، و`RIGHT JOIN`، و`GROUP BY`، و`WHERE NOT IN`، و`IN`—يمكنك صياغة استعلامات لاسترداد البيانات وتحليلها بفعالية من أي قاعدة بيانات علائقية.