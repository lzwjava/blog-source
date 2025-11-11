---
audio: false
generated: true
lang: hant
layout: post
title: SQL SELECT 語句
translated: true
type: note
---

針對您關於如何在 SQL 中使用 `SELECT`、`LEFT JOIN`、`RIGHT JOIN`、複雜 `SELECT`、`FROM`、`GROUP BY`、`WHERE NOT IN` 及 `IN` 的查詢，我將清晰解釋每個部分並提供實用範例。這些是從資料庫檢索和操作資料的基本 SQL 操作。讓我們逐步分解，並使用統一的簡單資料庫結構來說明：

- **資料表：**
  - `employees` (欄位：`employee_id`, `employee_name`, `department_id`, `salary`)
  - `departments` (欄位：`department_id`, `department_name`)
  - `projects` (欄位：`project_id`, `project_name`, `employee_id`)

---

### 1. SELECT
`SELECT` 子句用於指定要從資料庫資料表中檢索的欄位。它是所有 SQL 查詢的基礎。

- **用途：** 選擇要顯示的資料。
- **範例：**
  ```sql
  SELECT employee_name, salary
  FROM employees;
  ```
  這會從 `employees` 資料表中檢索 `employee_name` 和 `salary` 欄位。

---

### 2. FROM
`FROM` 子句標識要從中提取資料的資料表（或多個資料表）。它總是與 `SELECT` 一起使用。

- **用途：** 指定資料來源。
- **範例：**
  ```sql
  SELECT employee_name
  FROM employees;
  ```
  這裡，`employees` 是被查詢的資料表。

---

### 3. LEFT JOIN
`LEFT JOIN`（或 `LEFT OUTER JOIN`）合併兩個資料表的列。它返回左側資料表的所有記錄，以及右側資料表中匹配的記錄。如果沒有匹配項，結果中右側資料表的欄位將包含 `NULL` 值。

- **用途：** 包含左側資料表的所有列，無論右側資料表是否有匹配項。
- **範例：**
  ```sql
  SELECT e.employee_name, d.department_name
  FROM employees e
  LEFT JOIN departments d
  ON e.department_id = d.department_id;
  ```
  這會列出所有員工及其部門名稱。如果員工未分配至部門，`department_name` 將為 `NULL`。

---

### 4. RIGHT JOIN
`RIGHT JOIN`（或 `RIGHT OUTER JOIN`）與 `LEFT JOIN` 類似，但它返回右側資料表的所有記錄，以及左側資料表中匹配的記錄。不匹配的左側資料表列將導致 `NULL` 值。

- **用途：** 包含右側資料表的所有列，無論左側資料表是否有匹配項。
- **範例：**
  ```sql
  SELECT e.employee_name, d.department_name
  FROM employees e
  RIGHT JOIN departments d
  ON e.department_id = d.department_id;
  ```
  這會顯示所有部門及其員工。沒有員工的部門將在 `employee_name` 欄位中顯示 `NULL`。

---

### 5. 複雜 SELECT
「複雜 `SELECT`」並非正式的 SQL 術語，但通常指結合了多個子句、JOIN、子查詢或聚合函數來執行進階資料檢索的 `SELECT` 語句。

- **用途：** 處理涉及多個操作的複雜查詢。
- **範例：**
  ```sql
  SELECT d.department_name, COUNT(e.employee_id) AS employee_count
  FROM departments d
  LEFT JOIN employees e
  ON d.department_id = e.department_id
  GROUP BY d.department_name
  HAVING COUNT(e.employee_id) > 5;
  ```
  這會找出員工人數超過 5 人的部門，計算每個部門的員工人數並過濾結果。

---

### 6. GROUP BY
`GROUP BY` 子句將具有指定欄位相同值的列分組為摘要列，通常與聚合函數如 `COUNT`、`SUM` 或 `AVG` 一起使用。

- **用途：** 根據欄位值聚合資料。
- **範例：**
  ```sql
  SELECT department_id, COUNT(employee_id) AS employee_count
  FROM employees
  GROUP BY department_id;
  ```
  這會計算每個部門的員工人數。

---

### 7. WHERE NOT IN
`WHERE NOT IN` 子句過濾掉欄位值不在指定清單或子查詢結果中的列。請注意：如果清單/子查詢包含 `NULL`，則可能不會返回任何列。

- **用途：** 根據一組值排除列。
- **範例：**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id NOT IN (1, 2);
  ```
  這會檢索不在部門 1 或 2 的員工。

- **使用子查詢：**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id NOT IN (SELECT department_id FROM departments WHERE department_name = 'Inactive');
  ```
  這會找出不在標記為 'Inactive' 的部門中的員工。

---

### 8. IN
`IN` 子句過濾欄位值匹配清單或子查詢中任何值的列。它是多個 `OR` 條件的簡寫形式。

- **用途：** 根據一組值包含列。
- **範例：**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id IN (3, 4);
  ```
  這會檢索在部門 3 或 4 的員工。

- **使用子查詢：**
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
  這會找出在員工人數超過 5 人的部門中的員工。

---

### 綜合應用範例
以下是一個結合了上述多個操作的範例：
```sql
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
WHERE e.department_id NOT IN (1, 2)
GROUP BY d.department_name;
```
- **解釋：**
  - `FROM departments d`：從 `departments` 資料表開始。
  - `LEFT JOIN employees e`：包含所有部門，即使該部門沒有員工。
  - `WHERE NOT IN (1, 2)`：排除來自部門 1 和 2 的員工。
  - `GROUP BY d.department_name`：按部門名稱對結果進行分組。
  - `SELECT ... COUNT`：計算每個部門的員工人數。

---

### 關鍵提示
- **JOIN：** 根據您想完全保留哪個資料表的列（左側或右側）來選擇 `LEFT JOIN` 或 `RIGHT JOIN`。
- **NOT IN 與 NULL：** 如果子查詢返回 `NULL`，`NOT IN` 可能會意外地排除所有列。可以考慮使用 `NOT EXISTS` 作為替代方案。
- **複雜查詢：** 將其分解為多個部分（例如，單獨測試 JOIN）以確保正確性。
- **順序很重要：** 將 `WHERE` 放在 `GROUP BY` 之前，並在 `GROUP BY` 之後使用 `HAVING` 來進行群組層級的過濾。

通過理解並結合這些 SQL 元件——`SELECT`、`FROM`、`LEFT JOIN`、`RIGHT JOIN`、`GROUP BY`、`WHERE NOT IN` 和 `IN`——您便可以有效地構建查詢，從任何關聯式資料庫中檢索和分析資料。