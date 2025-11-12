---
audio: false
generated: true
lang: ja
layout: post
title: SQL SELECT文
translated: true
type: note
---

SQLにおける`SELECT`、`LEFT JOIN`、`RIGHT JOIN`、複雑な`SELECT`、`FROM`、`GROUP BY`、`WHERE NOT IN`、`IN`の使用方法について、各要素を明確に説明し実践的な例を提供します。これらはデータベースからデータを取得および操作するための基本的なSQL操作です。一貫性のために単純なデータベーススキーマを使用して、段階的に説明していきます：

- **テーブル:**
  - `employees` (カラム: `employee_id`, `employee_name`, `department_id`, `salary`)
  - `departments` (カラム: `department_id`, `department_name`)
  - `projects` (カラム: `project_id`, `project_name`, `employee_id`)

---

### 1. SELECT
`SELECT`句は、データベーステーブルから取得したいカラムを指定するために使用します。あらゆるSQLクエリの基礎を形成します。

- **目的:** 表示するデータを選択する。
- **例:**
  ```sql
  SELECT employee_name, salary
  FROM employees;
  ```
  これは`employees`テーブルから`employee_name`と`salary`カラムを取得します。

---

### 2. FROM
`FROM`句は、データを取得する元のテーブル（または複数のテーブル）を特定します。常に`SELECT`とともに使用されます。

- **目的:** データソースを指定する。
- **例:**
  ```sql
  SELECT employee_name
  FROM employees;
  ```
  ここでは、`employees`がクエリ対象のテーブルです。

---

### 3. LEFT JOIN
`LEFT JOIN`（または`LEFT OUTER JOIN`）は、2つのテーブルの行を結合します。左テーブルのすべてのレコードと、右テーブルの一致するレコードを返します。一致がない場合、結果には右テーブルのカラムに`NULL`値が含まれます。

- **目的:** 右テーブルでの一致に関係なく、左テーブルのすべての行を含める。
- **例:**
  ```sql
  SELECT e.employee_name, d.department_name
  FROM employees e
  LEFT JOIN departments d
  ON e.department_id = d.department_id;
  ```
  これはすべての従業員とその部門名をリストします。従業員が部門に割り当てられていない場合、`department_name`は`NULL`になります。

---

### 4. RIGHT JOIN
`RIGHT JOIN`（または`RIGHT OUTER JOIN`）は`LEFT JOIN`と似ていますが、右テーブルのすべてのレコードと左テーブルの一致するレコードを返します。一致しない左テーブルの行は`NULL`値になります。

- **目的:** 左テーブルでの一致に関係なく、右テーブルのすべての行を含める。
- **例:**
  ```sql
  SELECT e.employee_name, d.department_name
  FROM employees e
  RIGHT JOIN departments d
  ON e.department_id = d.department_id;
  ```
  これはすべての部門とその従業員を表示します。従業員がいない部門は`employee_name`が`NULL`になります。

---

### 5. 複雑なSELECT
「複雑な`SELECT`」は正式なSQL用語ではありませんが、通常、高度なデータ取得を実行するために、複数の句、結合、サブクエリ、または集計関数を組み合わせた`SELECT`ステートメントを指します。

- **目的:** 複数の操作を含む複雑なクエリを扱う。
- **例:**
  ```sql
  SELECT d.department_name, COUNT(e.employee_id) AS employee_count
  FROM departments d
  LEFT JOIN employees e
  ON d.department_id = e.department_id
  GROUP BY d.department_name
  HAVING COUNT(e.employee_id) > 5;
  ```
  これは従業員が5人より多い部門を見つけ、部門ごとの従業員を数えて結果をフィルタリングします。

---

### 6. GROUP BY
`GROUP BY`句は、指定されたカラムで同じ値を持つ行を要約行にグループ化します。`COUNT`、`SUM`、`AVG`などの集計関数とよく一緒に使用されます。

- **目的:** カラムの値に基づいてデータを集計する。
- **例:**
  ```sql
  SELECT department_id, COUNT(employee_id) AS employee_count
  FROM employees
  GROUP BY department_id;
  ```
  これは各部門の従業員数を数えます。

---

### 7. WHERE NOT IN
`WHERE NOT IN`句は、カラムの値が指定されたリストまたはサブクエリの結果内に存在しない行をフィルタリングします。注意：リスト/サブクエリに`NULL`が含まれている場合、行が返されない可能性があります。

- **目的:** 値のセットに基づいて行を除外する。
- **例:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id NOT IN (1, 2);
  ```
  これは部門1または2にいない従業員を取得します。

- **サブクエリを使用した例:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id NOT IN (SELECT department_id FROM departments WHERE department_name = 'Inactive');
  ```
  これは「Inactive」とマークされた部門にいない従業員を見つけます。

---

### 8. IN
`IN`句は、カラムの値がリストまたはサブクエリ内の任意の値と一致する行をフィルタリングします。これは複数の`OR`条件の短縮形です。

- **目的:** 値のセットに基づいて行を含める。
- **例:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id IN (3, 4);
  ```
  これは部門3または4にいる従業員を取得します。

- **サブクエリを使用した例:**
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
  これは従業員が5人より多い部門にいる従業員を見つけます。

---

### すべてを組み合わせた例
これらの操作のいくつかを組み合わせた例を以下に示します：
```sql
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
WHERE e.department_id NOT IN (1, 2)
GROUP BY d.department_name;
```
- **説明:**
  - `FROM departments d`: `departments`テーブルから開始します。
  - `LEFT JOIN employees e`: 従業員がいない部門も含め、すべての部門を含みます。
  - `WHERE NOT IN (1, 2)`: 部門1および2からの従業員を除外します。
  - `GROUP BY d.department_name`: 結果を部門名でグループ化します。
  - `SELECT ... COUNT`: 部門ごとの従業員を数えます。

---

### 主なヒント
- **結合:** 完全に保持したい行がどちらのテーブル（左または右）にあるかに基づいて、`LEFT JOIN`または`RIGHT JOIN`を選択します。
- **NOT IN と NULL:** サブクエリが`NULL`を返す場合、`NOT IN`は予期せずすべての行を除外する可能性があります。代替として`NOT EXISTS`を検討してください。
- **複雑なクエリ:** 正確性を確保するために、クエリを部分に分割します（例：結合を個別にテストする）。
- **順序の重要性:** `WHERE`を`GROUP BY`の前に配置し、グループレベルのフィルターには`GROUP BY`の後に`HAVING`を使用します。

これらのSQLコンポーネント—`SELECT`、`FROM`、`LEFT JOIN`、`RIGHT JOIN`、`GROUP BY`、`WHERE NOT IN`、`IN`—を理解し組み合わせることで、リレーショナルデータベースからデータを効果的に取得および分析するクエリを作成できます。