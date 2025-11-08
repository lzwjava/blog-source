---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在 Db2 中建立外來鍵
translated: true
type: note
---

### 在 IBM Db2 中建立外來鍵

外來鍵在 Db2 中透過將一個資料表（子資料表）中的欄位（或欄位組）連結到另一個資料表（父資料表）中的主鍵或唯一鍵，來強制執行參照完整性。這確保子資料表中的值與父資料表中的現有值相符，防止出現孤立的記錄。

您可以在建立資料表時使用 `CREATE TABLE`，或透過 `ALTER TABLE` 將其新增至現有資料表來定義外來鍵。語法是標準 SQL，並適用於所有 Db2 平台（例如 LUW、z/OS）。

#### 1. 在建立資料表時定義外來鍵 (`CREATE TABLE`)
在欄位定義內或資料表定義的結尾使用 `FOREIGN KEY` 子句。

**基本語法：**
```
CREATE TABLE child_table (
    child_column1 datatype,
    foreign_key_column datatype,
    -- 其他欄位...
    CONSTRAINT constraint_name
    FOREIGN KEY (foreign_key_column) 
    REFERENCES parent_table (parent_key_column)
);
```

**範例：**
假設您有一個具有主鍵 `dept_id` 的 `departments` 資料表：
```
CREATE TABLE departments (
    dept_id INTEGER NOT NULL PRIMARY KEY,
    dept_name VARCHAR(50)
);
```

現在建立一個具有參照 `dept_id` 的外來鍵的 `employees` 資料表：
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

這會在 `employees` 中的 `dept_id` 上建立一個名為 `fk_emp_dept` 的外來鍵。

#### 2. 將外來鍵新增至現有資料表 (`ALTER TABLE`)
使用 `ALTER TABLE` 在資料表存在後新增約束。父鍵必須已經存在。

**基本語法：**
```
ALTER TABLE child_table 
ADD CONSTRAINT constraint_name 
FOREIGN KEY (foreign_key_column) 
REFERENCES parent_table (parent_key_column);
```

**範例：**
將相同的外來鍵新增至現有的 `employees` 資料表：
```
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) 
REFERENCES departments (dept_id);
```

#### 其他選項
您可以指定在更新或刪除父列時發生的動作：
- `ON DELETE CASCADE`：在刪除父列時刪除子列。
- `ON DELETE SET NULL`：在子列中將外來鍵設為 NULL。
- `ON UPDATE CASCADE`：在父鍵變更時更新子鍵。
- `ON UPDATE SET NULL`：在父鍵更新時設為 NULL。

**帶選項的範例：**
```
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) 
REFERENCES departments (dept_id)
ON DELETE CASCADE
ON UPDATE RESTRICT;
```

#### 主要規則與注意事項
- 外來鍵欄位必須與父鍵欄位的資料類型和長度相符。
- 父資料表必須在建立外來鍵之前定義主鍵或唯一鍵。
- 外來鍵可以參照同一個資料表（自參照）。
- 多個欄位可以組成複合外來鍵：`FOREIGN KEY (col1, col2) REFERENCES parent (pk1, pk2)`。
- 要刪除外來鍵：`ALTER TABLE child_table DROP CONSTRAINT constraint_name;`。
- 建議在外來鍵欄位上建立索引以提升效能。

請在開發環境中測試，因為如果現有資料違反約束（例如孤立的列），新增約束可能會失敗。

#### 參考資料
- [外來鍵（參照）約束 - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=constraints-foreign-key-referential)
- [CREATE TABLE 語句 - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=statements-create-table)
- [ALTER TABLE 語句 - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=statements-alter-table)
- [在 Db2 中新增外來鍵 - Stack Overflow](https://stackoverflow.com/questions/59370149/adding-a-foreign-key-with-db2-of-ibm)