---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Db2での外部キーの作成
translated: true
type: note
---

### IBM Db2での外部キーの作成

Db2における外部キーは、あるテーブル（子テーブル）の列（または列のセット）を別のテーブル（親テーブル）の主キーまたは一意キーにリンクすることで、参照整合性を強制します。これにより、子テーブルの値が親テーブルの既存の値と一致することが保証され、孤立したレコードが防止されます。

外部キーは、`CREATE TABLE`を使用したテーブル作成時、または`ALTER TABLE`を使用して既存のテーブルに追加することで定義できます。構文は標準SQLであり、Db2のプラットフォーム（例: LUW, z/OS）全体で動作します。

#### 1. テーブル作成時における外部キーの定義 (`CREATE TABLE`)
列定義内またはテーブル定義の最後で`FOREIGN KEY`句を使用します。

**基本構文:**
```
CREATE TABLE child_table (
    child_column1 datatype,
    foreign_key_column datatype,
    -- 他の列...
    CONSTRAINT constraint_name
    FOREIGN KEY (foreign_key_column) 
    REFERENCES parent_table (parent_key_column)
);
```

**例:**
主キー`dept_id`を持つ`departments`テーブルがあると仮定します:
```
CREATE TABLE departments (
    dept_id INTEGER NOT NULL PRIMARY KEY,
    dept_name VARCHAR(50)
);
```

次に、`dept_id`を参照する外部キーを持つ`employees`テーブルを作成します:
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

これにより、`employees`テーブルの`dept_id`に`fk_emp_dept`という名前の外部キーが作成されます。

#### 2. 既存のテーブルへの外部キーの追加 (`ALTER TABLE`)
テーブルが存在した後で制約を追加するには`ALTER TABLE`を使用します。親キーは既に存在している必要があります。

**基本構文:**
```
ALTER TABLE child_table 
ADD CONSTRAINT constraint_name 
FOREIGN KEY (foreign_key_column) 
REFERENCES parent_table (parent_key_column);
```

**例:**
既存の`employees`テーブルに同じ外部キーを追加するには:
```
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) 
REFERENCES departments (dept_id);
```

#### 追加オプション
親行が更新または削除されたときの動作を指定できます:
- `ON DELETE CASCADE`: 親が削除されると子行も削除します。
- `ON DELETE SET NULL`: 親が削除されると子行の外部キーをNULLに設定します。
- `ON UPDATE CASCADE`: 親キーが変更されると子キーも更新します。
- `ON UPDATE SET NULL`: 親キーが更新されると子キーをNULLに設定します。

**オプション付きの例:**
```
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) 
REFERENCES departments (dept_id)
ON DELETE CASCADE
ON UPDATE RESTRICT;
```

#### 主なルールと考慮事項
- 外部キー列は、親キー列のデータ型および長さと一致する必要があります。
- 外部キーを作成する前に、親テーブルに主キーまたは一意キーが定義されている必要があります。
- 外部キーは同じテーブルを参照できます（自己参照）。
- 複数の列で複合外部キーを形成できます: `FOREIGN KEY (col1, col2) REFERENCES parent (pk1, pk2)`。
- 外部キーを削除するには: `ALTER TABLE child_table DROP CONSTRAINT constraint_name;`。
- パフォーマンス向上のため、外部キー列にインデックスを作成することが推奨されます。

既存のデータが制約に違反している場合（例: 孤立した行）は、制約の追加が失敗する可能性があるため、開発環境でテストしてください。

#### 参考文献
- [Foreign key (referential) constraints - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=constraints-foreign-key-referential)
- [CREATE TABLE statement - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=statements-create-table)
- [ALTER TABLE statement - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=statements-alter-table)
- [Adding a foreign key with Db2 - Stack Overflow](https://stackoverflow.com/questions/59370149/adding-a-foreign-key-with-db2-of-ibm)