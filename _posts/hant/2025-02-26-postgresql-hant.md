---
audio: false
generated: true
lang: hant
layout: post
title: 'PostgreSQL: 資料庫管理指南'
translated: true
---

以下是使用 PostgreSQL 的逐步指南，這是一個強大的開源關聯式資料庫管理系統：

### 1. **安裝**
- **Windows**：從 [postgresql.org/download](https://www.postgresql.org/download/) 下載（包括 pgAdmin GUI）
- **macOS**：使用 Homebrew (`brew install postgresql`) 或下載安裝程式
- **Linux** (Debian/Ubuntu)：
  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  sudo systemctl start postgresql.service
  ```

### 2. **連接到 PostgreSQL**
- 默認管理員用戶：`postgres`
  ```bash
  sudo -u postgres psql  # Linux/macOS
  psql -U postgres       # Windows (via PSQL 命令行)
  ```
- 連接到特定資料庫：
  ```bash
  psql -U username -d dbname -h localhost -p 5432
  ```

### 3. **基本資料庫操作**
- **創建用戶/角色**：
  ```sql
  CREATE USER myuser WITH PASSWORD 'mypassword';
  ALTER ROLE myuser WITH CREATEDB;
  ```
- **創建資料庫**：
  ```sql
  CREATE DATABASE mydb;
  GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
  ```
- **基本 SQL 命令**：
  ```sql
  -- 創建表
  CREATE TABLE users (
      id SERIAL PRIMARY KEY,
      name VARCHAR(50),
      email VARCHAR(100) UNIQUE
  );

  -- 插入數據
  INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

  -- 查詢數據
  SELECT * FROM users WHERE name LIKE 'A%';

  -- 更新數據
  UPDATE users SET email = 'new@email.com' WHERE id = 1;

  -- 刪除數據
  DELETE FROM users WHERE id = 2;
  ```

### 4. **高級功能**
- **連接**：
  ```sql
  SELECT orders.id, users.name
  FROM orders
  INNER JOIN users ON orders.user_id = users.id;
  ```
- **JSON 支持**：
  ```sql
  CREATE TABLE products (
      id SERIAL PRIMARY KEY,
      details JSONB
  );
  ```
- **全文搜索**：
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
- **恢復**：
  ```bash
  psql -U username -d mydb -f backup.sql
  ```
- **Vacuum** (回收儲存空間)：
  ```sql
  VACUUM ANALYZE;
  ```

### 6. **安全**
- 創建只讀用戶：
  ```sql
  CREATE USER readonly WITH PASSWORD 'readpass';
  GRANT CONNECT ON DATABASE mydb TO readonly;
  GRANT USAGE ON SCHEMA public TO readonly;
  GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
  ```

### 7. **有用的命令**
- 列出資料庫：`\l`
- 切換資料庫：`\c dbname`
- 列出表：`\dt`
- 描述表：`\d tablename`
- 顯示用戶：`\du`
- 退出 psql：`\q`

### 8. **圖形用戶界面工具**
- **pgAdmin**：隨 Windows 安裝程式附帶
- **DBeaver**：流行的跨平台 GUI
- **TablePlus**：現代界面，具有本地感覺

### 9. **學習資源**
- 官方文檔：[postgresql.org/docs](https://www.postgresql.org/docs/)
- 互動教程：[postgresqltutorial.com](https://www.postgresqltutorial.com/)
- 練習：[pgexercises.com](https://pgexercises.com/)

**提示**：在應用到生產環境之前，請在開發環境中測試更改。對於關鍵操作，使用事務（`BEGIN`/`COMMIT`）。