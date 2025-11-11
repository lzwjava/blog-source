---
audio: false
generated: true
lang: ja
layout: post
title: DBeaverでOracle DBテーブルのデータを確認する手順
translated: true
type: note
---

前回のOracle Databaseでデータが含まれるテーブルを探す方法についての質問に基づき、DBeaverを使用してOracle Databaseのどのテーブルにデータが含まれているかを確認する方法について尋ねていると想定します。DBeaverは、Oracleや他のデータベースでうまく動作する人気の無料マルチプラットフォームデータベースツールです。以下では、DBeaverを使用してOracleスキーマを調査し、データが含まれるテーブルを特定する方法を説明します。

---

#### 1. **Oracle Databaseへの接続を設定**
   - **DBeaverのインストール**: まだの場合、[dbeaver.io](https://dbeaver.io/)からDBeaver（Community Editionで可）をダウンロードしてインストールします。
   - **新しい接続の作成**:
     1. DBeaverを開き、メニューで **Database** > **New Database Connection** をクリックします。
     2. リストから **Oracle** を選択し、**Next** をクリックします。
     3. 接続詳細を入力します：
        - **Host**: Oracleサーバーのホスト名またはIPアドレス。
        - **Port**: 通常は1521（Oracleのデフォルト）。
        - **Database/SID or Service Name**: 設定に応じて（例：Express Editionの場合はSID = `XE`、またはサービス名）。
        - **Username** と **Password**: Oracleの資格情報。
     4. **Test Connection** をクリックして動作を確認します。プロンプトが表示された場合は、Oracle JDBCドライバをダウンロードする必要があります（DBeaverはこれを自動的に行えます）。
     5. **Finish** をクリックして接続を保存します。

#### 2. **データベースナビゲーターでスキーマを探索**
   - **Database Navigator**（左側のペイン）で、Oracle接続を展開します。
   - スキーマのリスト（例：ユーザー名やアクセス可能な他のスキーマ）が表示されます。調査したいスキーマを展開します。
   - 各スキーマの下で、**Tables** ノードを展開してすべてのテーブルを表示します。

#### 3. **GUIを使用してテーブルのデータを確認**
   - **テーブルデータの表示**:
     1. テーブル名をダブルクリックするか、右クリックして **Edit Table** を選択します。
     2. 開いたエディターで **Data** タブに切り替えます。
     3. テーブルにデータが含まれている場合、行が表示されます。空の場合、行は表示されません（または「No data」のようなメッセージが表示されます）。
     - デフォルトでは、DBeaverは最大200行を取得します。すべての行を取得するには、Dataタブの下部ツールバーにある **Fetch All Rows** ボタン（小さな矢印アイコン）をクリックします。
   - **行数の迅速なカウント**:
     1. Database Navigatorでテーブルを右クリックします。
     2. **Navigate** > **Row Count** を選択します。
     3. DBeaverは `SELECT COUNT(*)` クエリを実行し、結果をポップアップで表示します。0の場合、テーブルは空です。

#### 4. **SQLクエリを実行して複数のテーブルを確認**
   - 一度に多くのテーブルを確認したい場合（各テーブルをクリックするよりも効率的）、SQL Editorを使用します：
     1. **SQL Editor** > **New SQL Script** をクリックします（または `Ctrl + [` を押します）。
     2. スキーマコンテキストを設定します：
        - SQL Editorの上部にあるドロップダウンを使用してスキーマを選択するか、以下を実行します：
          ```sql
          ALTER SESSION SET CURRENT_SCHEMA = schema_name;
          ```
          `schema_name` を対象のスキーマ（例：`HR`）に置き換えます。
     3. すべてのテーブルの行数をクエリします：
        - データが含まれるテーブルをリストするために、このSQLを使用します（前回の回答と同様）：
          ```sql
          SELECT table_name, num_rows
          FROM user_tables
          WHERE num_rows > 0
          ORDER BY num_rows DESC;
          ```
        - `Ctrl + Enter` を押して実行します。結果は下部の **Results** タブに表示されます。
        - `USER_TABLES` はあなたのスキーマ内のテーブルを表示します。他のスキーマにまたがってアクセス可能なテーブルには `ALL_TABLES` を使用します：
          ```sql
          SELECT owner, table_name, num_rows
          FROM all_tables
          WHERE num_rows > 0
          AND owner = UPPER('schema_name');
          ```
     4. **注意**: `NUM_ROWS` は最後の統計更新からの推定値です。不正確な場合は、以下で統計を更新します：
        ```sql
        EXEC DBMS_STATS.GATHER_SCHEMA_STATS('schema_name');
        ```