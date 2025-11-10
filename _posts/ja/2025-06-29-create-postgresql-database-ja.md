---
audio: false
generated: true
lang: ja
layout: post
title: PostgreSQLデータベースの作成
translated: true
type: note
---

あなたはすでにPostgreSQLの対話型ターミナル（`psql`）に`postgres`ユーザーとしてログインしています。これは素晴らしいことです！PostgreSQLでデータベースを作成するには、`CREATE DATABASE`コマンドを使用します。以下にステップバイステップのガイドを示します：

1. **`psql`にいることを確認**：
   `postgres=#`プロンプトが表示されているので、すでにログインしています。

2. **データベースを作成**：
   以下のコマンドを使用して新しいデータベースを作成します。`mydatabase`を希望のデータベース名に置き換えてください：

   ```sql
   CREATE DATABASE mydatabase;
   ```

   これにより`mydatabase`という名前のデータベースが作成されます。

3. **データベースが作成されたことを確認**：
   すべてのデータベースをリスト表示して確認します：

   ```sql
   \l
   ```

   これにより`mydatabase`を含むすべてのデータベースのテーブルが表示されます。

4. **新しいデータベースに接続**：
   新しいデータベースで作業を開始するには、以下のコマンドで接続します：

   ```sql
   \c mydatabase
   ```

   これによりセッションが`mydatabase`に切り替わります。

5. **オプション：ユーザーを作成して権限を付与**：
   特定のユーザーにこのデータベースを管理させたい場合は、ユーザーを作成して権限を付与します：

   ```sql
   CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
   GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
   ```

   `myuser`と`mypassword`を希望のユーザー名とパスワードに置き換えてください。

6. **`psql`を終了**：
   完了したら、以下のコマンドで終了します：

   ```sql
   \q
   ```

### 注意点：
- 表示された`Permission denied`エラー（`could not change directory to "/home/lzw/projects/lzwjava.github.io"`）は、`postgres`ユーザーがあなたのホームディレクトリにアクセスできないためです。これはデータベース作成には影響しませんが、制限されたディレクトリから`psql`を実行すると表示される可能性があります。このエラーを避けるには、`postgres`ユーザーがアクセスできるディレクトリから`psql`を実行するか、ディレクトリを変更しないでください（例：`/tmp`から`sudo -u postgres psql`を実行）。
- `psql`で試した`ls`コマンドは有効ではありません。データベースをリスト表示するには`\l`を、データベース内のテーブルをリスト表示するには`\dt`を使用してください。
- PostgreSQLサービスが実行されていることを確認してください（`sudo systemctl start postgresql.service`）。これはすでに行われています。

### 実行例：
```sql
postgres=# CREATE DATABASE mydatabase;
CREATE DATABASE
postgres=# \l
                                  データベース一覧
    名前     |  所有者  | エンコーディング |  照合順序   |   キャラクタ型    |   アクセス権利   
-------------+----------+------------------+-------------+------------------+-------------------
 mydatabase  | postgres | UTF8             | en_US.UTF-8 | en_US.UTF-8      | 
 postgres    | postgres | UTF8             | en_US.UTF-8 | en_US.UTF-8      | 
 template0   | postgres | UTF8             | en_US.UTF-8 | en_US.UTF-8      | =c/postgres      +
             |          |                  |             |                  | postgres=CTc/postgres
 template1   | postgres | UTF8             | en_US.UTF-8 | en_US.UTF-8      | =c/postgres      +
             |          |                  |             |                  | postgres=CTc/postgres
(4行)

postgres=# \c mydatabase
データベース"mydatabase"にユーザ"postgres"として接続しました。
mydatabase=# \q
```

さらにヘルプが必要な場合（例：テーブルの設定、ユーザーの設定、アプリケーションからの接続など）、お知らせください！