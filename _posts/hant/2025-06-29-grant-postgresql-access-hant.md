---
audio: false
generated: true
lang: hant
layout: post
title: 授予 PostgreSQL 數據庫存取權限
translated: true
type: note
---

要授予使用者在 PostgreSQL 中存取資料庫的權限，您需要按照以下步驟操作。我將指導您透過 psql 命令列介面使用 SQL 指令來完成此過程。

連線到 PostgreSQL：您已使用 postgres 使用者連線到 PostgreSQL，該使用者通常具有超級使用者權限。

建立使用者（如果尚未建立）：如果使用者不存在，您可以使用以下指令建立。請將 username 和 password 替換為所需的使用者名稱和密碼。

```
CREATE USER username WITH PASSWORD 'password';
```

建立資料庫（如果尚未建立）：如果資料庫不存在，您可以使用以下指令建立。請將 database_name 替換為所需的資料庫名稱。

```
CREATE DATABASE database_name;
```

授予資料庫權限：要授予使用者對特定資料庫的所有權限，請使用以下指令。請將 database_name 和 username 替換為相應的名稱。

```
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
```

授予結構描述使用權限：如果您希望使用者能夠存取資料庫中的特定結構描述，可以授予該結構描述的使用權限。請將 schema_name 和 username 替換為相應的名稱。

```
GRANT USAGE ON SCHEMA schema_name TO username;
```

授予資料表權限：要授予對結構描述內資料表的特定權限，可以使用以下指令。請將 schema_name、table_name 和 username 替換為相應的名稱。

```
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA schema_name TO username;
```

使權限生效：如果您已授予資料表權限，可能還需要為未來的資料表設定預設權限。

```
ALTER DEFAULT PRIVILEGES IN SCHEMA schema_name GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO username;
```

以下是指令的範例：

```
CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE DATABASE mydatabase;
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
\c mydatabase
GRANT USAGE ON SCHEMA public TO myuser;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO myuser;
```

這些指令將設定一個對特定資料庫及其資料表具有完整存取權限的使用者。請根據您的具體需求和安全性政策調整這些指令。