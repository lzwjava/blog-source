---
audio: false
generated: true
lang: ja
layout: post
title: PostgreSQLデータベースアクセス権限の付与
translated: true
type: note
---

PostgreSQLでユーザーにデータベースへのアクセス権を付与するには、以下の手順に従う必要があります。psqlコマンドラインインターフェースでSQLコマンドを使用する方法をご案内します。

PostgreSQLへの接続: postgresユーザーを使用してPostgreSQLに接続済みです。このユーザーは通常スーパーユーザー権限を持っています。

ユーザーの作成（存在しない場合）: ユーザーが存在しない場合は、以下のコマンドで作成できます。usernameとpasswordを希望のユーザー名とパスワードに置き換えてください。

```
CREATE USER username WITH PASSWORD 'password';
```

データベースの作成（存在しない場合）: データベースが存在しない場合は、以下のコマンドで作成できます。database_nameを希望のデータベース名に置き換えてください。

```
CREATE DATABASE database_name;
```

データベースへの権限付与: 特定のデータベースに対する全ての権限をユーザーに付与するには、以下のコマンドを使用します。database_nameとusernameを適切な名前に置き換えてください。

```
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
```

スキーマへの使用権限付与: ユーザーがデータベース内の特定のスキーマにアクセスできるようにするには、スキーマの使用権限を付与します。schema_nameとusernameを適切な名前に置き換えてください。

```
GRANT USAGE ON SCHEMA schema_name TO username;
```

テーブルへの権限付与: スキーマ内のテーブルに対する特定の権限を付与するには、以下のコマンドを使用します。schema_name、table_name、usernameを適切な名前に置き換えてください。

```
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA schema_name TO username;
```

権限の有効化: テーブルへの権限を付与した場合、将来作成されるテーブルに対してもデフォルトの権限を設定する必要があるかもしれません。

```
ALTER DEFAULT PRIVILEGES IN SCHEMA schema_name GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO username;
```

以下はコマンドの使用例です：

```
CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE DATABASE mydatabase;
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
\c mydatabase
GRANT USAGE ON SCHEMA public TO myuser;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO myuser;
```

これらのコマンドは、特定のデータベースとそのテーブルへの完全なアクセス権を持つユーザーを設定します。特定のニーズとセキュリティポリシーに応じてコマンドを調整してください。