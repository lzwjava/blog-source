---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: IBM DB2でのインデックス作成
translated: true
type: note
---

### IBM DB2でのインデックス作成

IBM DB2は、より高速なデータ取得を可能にすることでクエリパフォーマンスを最適化するためのインデックスをサポートしています。インデックスは、テーブルの1つ以上のカラムに対して作成できます。以下では、ユニークインデックスと複数列（複合）インデックスの基本を説明します。「ユニオンインデックス」はDB2の標準的な用語ではありません。これは、複数のキーをカバーする複合インデックスを指すか、クエリ内のユニオン操作の誤解である可能性があります。別の意味を意図していた場合は、詳細を提供してください！

#### 基本のインデックス作成
単一のカラムに対して単純なインデックスを構築するには、`CREATE INDEX`ステートメントを使用します。これにより、そのカラムに対する検索、ソート、結合が高速化されます。

**構文:**
```sql
CREATE INDEX index_name
ON table_name (column_name [ASC | DESC]);
```

**例:**
```sql
CREATE INDEX idx_employee_id
ON employees (employee_id ASC);
```

- `ASC`は昇順でソート（デフォルト）。降順の場合は`DESC`を使用。
- インデックスはデフォルトで非ユニークであり、重複する値を許可します。

#### ユニークインデックス（ユニークキーの強制）
ユニークインデックスは、インデックスが付けられたカラムに重複する値が存在しないことを保証します。これはユニーク制約と同様です。DB2は、主キーまたはユニーク制約を定義すると自動的にユニークインデックスを作成します。

**構文:**
```sql
CREATE UNIQUE INDEX index_name
ON table_name (column_name [ASC | DESC]);
```

**例:**
```sql
CREATE UNIQUE INDEX uidx_email
ON users (email ASC);
```

- これにより、重複するメールアドレスの挿入が防止されます。
- 部分的な一意性（例: NULLを無視）の場合、`WHERE NOT NULL`を追加:  
  ```sql
  CREATE UNIQUE WHERE NOT NULL INDEX uidx_email
  ON users (email ASC);
  ```
- クエリカバレッジのために非キーカラムを含めることができます:  
  ```sql
  CREATE UNIQUE INDEX uidx_email
  ON users (email ASC) INCLUDE (first_name, last_name);
  ```

#### 複合インデックス（複数キー、例: 2つ以上のカラム）
複合（または複数列）インデックスは複数のキーをカバーし、列の組み合わせでフィルタリング/結合するクエリに有用です。カラムの順序が重要です。選択性が最も高いカラムを先頭に配置します。

**構文:**
```sql
CREATE INDEX index_name
ON table_name (column1 [ASC | DESC], column2 [ASC | DESC], ...);
```

**例（2つのキー）:**
```sql
CREATE INDEX idx_order_date_customer
ON orders (order_date ASC, customer_id DESC);
```

- これは、`SELECT * FROM orders WHERE order_date > '2023-01-01' AND customer_id = 123;`のようなクエリを最適化します。
- ユニークな複合インデックスの場合: `UNIQUE`を追加（例: `CREATE UNIQUE INDEX ...`）。

#### 追加のヒント
- **インデックスの確認:** `SELECT * FROM SYSCAT.INDEXES WHERE TABSCHEMA = 'YOUR_SCHEMA' AND TABNAME = 'YOUR_TABLE';`を使用。
- **インデックスの削除:** `DROP INDEX index_name;`。
- インデックスはストレージを消費し、挿入/更新を遅くします。注意して使用してください。
- パーティションテーブルや高度なオプション（例: クラスタリング）については、DB2のドキュメントを参照してください。

[Db2 CREATE INDEX Statement](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=statements-create-index)  
[Db2 Unique Indexes](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=attributes-unique-indexes)  
[Db2 Composite Indexes Example](https://stackoverflow.com/questions/21597015/composite-index-creation-in-db2)  
[Db2 Unique Index Tutorial](https://www.db2tutorial.com/db2-index/db2-unique-index/)