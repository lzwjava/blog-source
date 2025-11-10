---
audio: false
generated: true
lang: hant
layout: post
title: 建立 PostgreSQL 數據庫
translated: true
type: note
---

你已經成功進入 PostgreSQL 互動式終端機 (`psql`) 並以 `postgres` 用戶身份登入，這很好！要在 PostgreSQL 中建立資料庫，你可以使用 `CREATE DATABASE` 指令。以下是逐步操作指南：

1. **確認你正在使用 `psql`**：
   如 `postgres=#` 提示符所示，你已經處於 `psql` 環境中。

2. **建立資料庫**：
   使用以下指令建立新資料庫。請將 `mydatabase` 替換為你想要的資料庫名稱：

   ```sql
   CREATE DATABASE mydatabase;
   ```

   這將建立一個名為 `mydatabase` 的資料庫。

3. **驗證資料庫是否建立成功**：
   列出所有資料庫以確認：

   ```sql
   \l
   ```

   這將顯示包含 `mydatabase` 在內的所有資料庫列表。

4. **連線到新資料庫**：
   要開始在新資料庫中工作，請使用以下指令連線：

   ```sql
   \c mydatabase
   ```

   這會將你的工作階段切換到 `mydatabase`。

5. **可選：建立用戶並授予權限**：
   如果你想讓特定用戶管理此資料庫，請建立用戶並授予權限：

   ```sql
   CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
   GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
   ```

   請將 `myuser` 和 `mypassword` 替換為你想要的用戶名和密碼。

6. **退出 `psql`**：
   完成後，使用以下指令退出：

   ```sql
   \q
   ```

### 注意事項：
- 你之前看到的 `Permission denied` 錯誤（`could not change directory to "/home/lzw/projects/lzwjava.github.io"`）是因為 `postgres` 用戶無法存取你的家目錄。這不會影響資料庫建立，但當從受限制的目錄執行 `psql` 時可能會出現此訊息。你可以透過在 `postgres` 用戶可存取的目錄中執行 `psql`，或不切換目錄（例如從 `/tmp` 執行 `sudo -u postgres psql`）來避免此問題。
- 你在 `psql` 中嘗試的 `ls` 指令無效。請使用 `\l` 來列出資料庫，或使用 `\dt` 來列出資料庫中的表格。
- 請確保 PostgreSQL 服務正在運行（`sudo systemctl start postgresql.service`），這你已經完成了。

### 操作範例：
```sql
postgres=# CREATE DATABASE mydatabase;
CREATE DATABASE
postgres=# \l
                                  資料庫列表
   名稱     |  擁有者  | 字元編碼 |    校對規則    |     字元類型     |   存取權限   
------------+----------+----------+----------------+------------------+--------------
 mydatabase | postgres | UTF8     | en_US.UTF-8    | en_US.UTF-8      | 
 postgres   | postgres | UTF8     | en_US.UTF-8    | en_US.UTF-8      | 
 template0  | postgres | UTF8     | en_US.UTF-8    | en_US.UTF-8      | =c/postgres  +
            |          |          |                |                  | postgres=CTc/postgres
 template1  | postgres | UTF8     | en_US.UTF-8    | en_US.UTF-8      | =c/postgres  +
            |          |          |                |                  | postgres=CTc/postgres
(4 行)

postgres=# \c mydatabase
你現在已經連線到資料庫 "mydatabase"，使用者為 "postgres"。
mydatabase=# \q
```

如果你需要進一步協助（例如設定表格、用戶或從應用程式連線），請告訴我！