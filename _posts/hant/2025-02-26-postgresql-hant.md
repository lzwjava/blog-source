---
audio: false
generated: true
lang: hant
layout: post
title: PostgreSQL：數據庫管理指南
translated: true
type: note
---

以下是使用 PostgreSQL 的逐步指南，這是一個功能強大的開源關聯式資料庫管理系統：

### 1. **安裝**
- **Windows**：從 [postgresql.org/download](https://www.postgresql.org/download/) 下載（包含 pgAdmin 圖形介面）
- **macOS**：使用 Homebrew（`brew install postgresql`）或下載安裝程式
- **Linux**（Debian/Ubuntu）：
  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  sudo systemctl start postgresql.service
  ```

### 2. **連線到 PostgreSQL**
- 預設管理員使用者：`postgres`
  ```bash
  sudo -u postgres psql  # Linux/macOS
  psql -U postgres       # Windows（透過 PSQL 命令列）
  ```
- 連線到特定資料庫：
  ```bash
  psql -U username -d dbname -h localhost -p 5432
  ```

### 3. **基本資料庫操作**
- **建立使用者/角色**：
  ```sql
  CREATE USER myuser WITH PASSWORD 'mypassword';
  ALTER ROLE myuser WITH CREATEDB;
  ```
- **建立資料庫**：
  ```sql
  CREATE DATABASE mydb;
  GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
  ```
- **基本 SQL 指令**：
  ```sql
  -- 建立表格
  CREATE TABLE users (
      id SERIAL PRIMARY KEY,
      name VARCHAR(50),
      email VARCHAR(100) UNIQUE
  );

  -- 插入資料
  INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

  -- 查詢資料
  SELECT * FROM users WHERE name LIKE 'A%';

  -- 更新資料
  UPDATE users SET email = 'new@email.com' WHERE id = 1;

  -- 刪除資料
  DELETE FROM users WHERE id = 2;
  ```

### 4. **進階功能**
- **合併查詢**：
  ```sql
  SELECT orders.id, users.name 
  FROM orders
  INNER JOIN users ON orders.user_id = users.id;
  ```
- **JSON 支援**：
  ```sql
  CREATE TABLE products (
      id SERIAL PRIMARY KEY,
      details JSONB
  );
  ```
- **全文搜尋**：
  ```sql
  SELECT * FROM documents 
  WHERE to_tsvector('english', content) @@ to_tsquery('search & term');
  ```

### 5. **維護**
- **備份**：
  ```bash
  pg_dump mydb > backup.sql
  pg_dumpall > all_databases.sql
  ```
- **還原**：
  ```bash
  psql -U username -d mydb -f backup.sql
  ```
- **清理**（回收儲存空間）：
  ```sql
  VACUUM ANALYZE;
  ```

### 6. **安全性**
- 建立唯讀使用者：
  ```sql
  CREATE USER readonly WITH PASSWORD 'readpass';
  GRANT CONNECT ON DATABASE mydb TO readonly;
  GRANT USAGE ON SCHEMA public TO readonly;
  GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
  ```

### 7. **實用指令**
- 列出資料庫：`\l`
- 切換資料庫：`\c dbname`
- 列出表格：`\dt`
- 描述表格結構：`\d tablename`
- 顯示使用者：`\du`
- 退出 psql：`\q`

### 8. **圖形介面工具**
- **pgAdmin**：Windows 安裝程式內含
- **DBeaver**：流行的跨平台圖形介面
- **TablePlus**：具有原生感的現代介面

### 9. **學習資源**
- 官方文件：[postgresql.org/docs](https://www.postgresql.org/docs/)
- 互動式教學：[postgresqltutorial.com](https://www.postgresqltutorial.com/)
- 練習平台：[pgexercises.com](https://pgexercises.com/)

**提示**：在應用至生產環境前，請務必在開發環境中測試變更。對於關鍵操作，請使用交易（`BEGIN`/`COMMIT`）。