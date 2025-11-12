---
audio: false
generated: true
lang: ja
layout: post
title: Oracle DBでデータが存在するテーブルの特定
translated: true
type: note
---

Oracle Databaseでスキーマを探索中に、テーブルをクリックした際（SQL DeveloperやToadなどのGUIツールを使用している場合など）に「空」のように見える場合でも、必ずしもデータが存在しないわけではありません。権限、フィルター、あるいは単に間違ったテーブルを参照している可能性があります。スキーマ内のどのテーブルにデータが含まれているかを体系的に確認するには、データベースのメタデータをクエリするか、テーブルを直接検査します。以下に方法を示します：

#### 1. **権限を確認する**
   - テーブルが空に見える場合、データを表示する権限がない可能性があります。スキーマ内のテーブルに対する `SELECT` 権限があることを確認してください。
   - 特定のテーブルに対する権限を確認するには、以下を実行します：
     ```sql
     SELECT privilege
     FROM dba_tab_privs
     WHERE grantee = UPPER('your_username')
     AND table_name = UPPER('table_name');
     ```
     `'your_username'` と `'table_name'` を適切に置き換えてください。何も表示されない場合は、スキーマ所有者またはDBAにアクセス権の付与を依頼してください。

#### 2. **テーブルの行数をクエリする**
   - Oracleは、`USER_TABLES`、`ALL_TABLES`、または `DBA_TABLES` ビュー（アクセスレベルに依存）に、行数を含むテーブルに関する統計情報を保持しています。
   - 現在のスキーマでデータが存在するテーブルを確認するには：
     ```sql
     SELECT table_name, num_rows
     FROM user_tables
     WHERE num_rows > 0
     ORDER BY num_rows DESC;
     ```
     - `USER_TABLES`：現在のユーザーが所有するテーブルを表示します。
     - `NUM_ROWS`：おおよその行数（最終統計更新に基づく）。

   - 他のスキーマにアクセスできる場合（例：`ALL_TABLES` 経由）：
     ```sql
     SELECT owner, table_name, num_rows
     FROM all_tables
     WHERE num_rows > 0
     AND owner = UPPER('schema_name')
     ORDER BY num_rows DESC;
     ```
     `'schema_name'` を調査対象のスキーマ名に置き換えてください。

   **注意**：統計が最近収集されていない場合、`NUM_ROWS` は古い可能性があります。ステップ5を参照して統計を更新してください。

#### 3. **特定のテーブルを手動で確認する**
   - `NUM_ROWS` が信頼できない場合や確認したい場合は、個々のテーブルで `COUNT(*)` を実行します：
     ```sql
     SELECT table_name
     FROM user_tables;
     ```
     これにより、スキーマ内のすべてのテーブルがリストされます。その後、各テーブルに対して：
     ```sql
     SELECT COUNT(*) FROM table_name;
     ```
     カウントが0より大きい場合、テーブルにはデータが存在します。大規模なテーブルでは `COUNT(*)` が遅くなる可能性があるため注意してください。

#### 4. **スクリプトを使用して自動的に確認する**
   - 各テーブルを手動でクエリすることを避けるために、PL/SQLスクリプトを使用してスキーマ内のすべてのテーブルの行数を確認します：
     ```sql
     BEGIN
         FOR t IN (SELECT table_name FROM user_tables)
         LOOP
             EXECUTE IMMEDIATE 'SELECT COUNT(*) FROM ' || t.table_name INTO v_count;
             IF v_count > 0 THEN
                 DBMS_OUTPUT.PUT_LINE(t.table_name || ' has ' || v_count || ' rows');
             END IF;
         END LOOP;
     EXCEPTION
         WHEN OTHERS THEN
             DBMS_OUTPUT.PUT_LINE('Error on table ' || t.table_name || ': ' || SQLERRM);
     END;
     /
     ```
     - ツールで出力を有効にしてください（例：SQL*PlusまたはSQL Developerで `SET SERVEROUTPUT ON`）。
     - これにより、データが存在するテーブルのみが出力されます。他のスキーマを確認する場合は、`user_tables` を `all_tables` に調整し、`owner` フィルタを追加してください。

#### 5. **テーブル統計を更新する（必要に応じて）**
   - `USER_TABLES` または `ALL_TABLES` の `NUM_ROWS` が0を示すか、間違っているように見える場合、統計が古い可能性があります。更新するには：
     ```sql
     EXEC DBMS_STATS.GATHER_SCHEMA_STATS(ownname => 'schema_name');
     ```
     `'schema_name'` をスキーマ名に置き換えてください（自身のスキーマの場合はユーザー名を使用）。その後、ステップ2の `USER_TABLES` クエリを再実行してください。

#### 6. **パーティションテーブルを確認する**
   - スキーマがパーティションテーブルを使用している場合、データはパーティション間に分散している可能性があり、単純なクエリではこれを反映しないことがあります。パーティションを確認します：
     ```sql
     SELECT table_name, partition_name, num_rows
     FROM user_tab_partitions
     WHERE num_rows > 0
     ORDER BY table_name, partition_name;
     ```
     これにより、データが含まれているパーティションが表示されます。

#### 7. **GUIツールのヒント（例：SQL Developer）**
   - Oracle SQL DeveloperなどのGUIを使用している場合：
     1. 接続ペインでスキーマを右クリックします。
     2. 「テーブル」ノードを展開します。
     3. テーブルを右クリックし、「行数をカウント」を選択するか、「データ」タブを開いて内容をプレビューします（権限がある場合）。
     - 「データ」タブが空の場合、権限の問題であるか、テーブルに実際に行が存在しないかのどちらかです。

---

### 実践例
スキーマ `HR` にいる場合：
1. 以下を実行します：
   ```sql
   SELECT table_name, num_rows
   FROM user_tables
   WHERE num_rows > 0;
   ```
   出力例：
   ```
   TABLE_NAME   NUM_ROWS
   ----------   --------
   EMPLOYEES    107
   DEPARTMENTS  27
   ```
   これにより、`EMPLOYEES` と `DEPARTMENTS` にデータが存在することがわかります。

2. 統計が古い可能性がある場合は、更新します：
   ```sql
   EXEC DBMS_STATS.GATHER_SCHEMA_STATS('HR');
   ```
3. 同じクエリで再確認します。

---

### テーブルが空に見える理由
- **データが存在しない**：テーブルに実際に行が存在しない。
- **権限**：テーブル構造は表示できるが、データは表示できない。
- **フィルター**：GUIツールに行を非表示にするフィルターが設定されている（例：`WHERE` 句）。
- **データの切り捨て/削除**：データが最近削除された可能性がある。
- **シノニム/ビュー**：空またはアクセス不能なテーブルを指すシノニムまたはビューを参照している可能性がある。

まだ問題が解決しない場合は、具体的な設定（例：スキーマ名、使用ツール）を教えてください。さらに具体的なアドバイスを提供します！