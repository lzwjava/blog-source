---
audio: false
generated: true
lang: hant
layout: post
title: 使用 MySQL
translated: true
type: note
---

以下是一份使用 MySQL（熱門的開源關聯式資料庫管理系統）的逐步指南：

---

### 1. **安裝**
- **Windows**：從 [mysql.com/downloads](https://dev.mysql.com/downloads/installer/) 下載 MySQL Installer
- **macOS**：
  ```bash
  brew install mysql
  brew services start mysql
  ```
- **Linux** (Debian/Ubuntu)：
  ```bash
  sudo apt update
  sudo apt install mysql-server mysql-client
  sudo systemctl start mysql
  sudo mysql_secure_installation  # 執行安全設定
  ```

---

### 2. **連接 MySQL**
- **預設 root 登入**：
  ```bash
  mysql -u root -p  # 輸入密碼
  ```
- **連接遠端伺服器**：
  ```bash
  mysql -u username -p -h hostname -P 3306
  ```

---

### 3. **基本資料庫操作**
- **建立使用者**：
  ```sql
  CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
  ```
- **建立資料庫**：
  ```sql
  CREATE DATABASE mydb;
  GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'localhost';
  FLUSH PRIVILEGES;
  ```
- **基本 SQL 指令**：
  ```sql
  -- 建立表格
  CREATE TABLE users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(50),
      email VARCHAR(100) UNIQUE
  );

  -- 插入資料
  INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com');

  -- 查詢資料
  SELECT * FROM users WHERE name LIKE 'B%';

  -- 更新資料
  UPDATE users SET email = 'new@email.com' WHERE id = 1;

  -- 刪除資料
  DELETE FROM users WHERE id = 2;
  ```

---

### 4. **進階功能**
- **合併查詢**：
  ```sql
  SELECT orders.id, users.name 
  FROM orders
  JOIN users ON orders.user_id = users.id;
  ```
- **預存程序**：
  ```sql
  DELIMITER //
  CREATE PROCEDURE GetUsers()
  BEGIN
    SELECT * FROM users;
  END //
  DELIMITER ;
  
  CALL GetUsers();
  ```
- **JSON 支援** (MySQL 5.7+)：
  ```sql
  CREATE TABLE products (
      id INT PRIMARY KEY,
      details JSON
  );
  ```

---

### 5. **維護**
- **備份**：
  ```bash
  mysqldump -u root -p mydb > backup.sql
  ```
- **還原**：
  ```bash
  mysql -u root -p mydb < backup.sql
  ```
- **最佳化表格**：
  ```sql
  ANALYZE TABLE users;
  OPTIMIZE TABLE users;
  ```

---

### 6. **安全性**
- **建立唯讀使用者**：
  ```sql
  CREATE USER 'reader'@'localhost' IDENTIFIED BY 'readpass';
  GRANT SELECT ON mydb.* TO 'reader'@'localhost';
  FLUSH PRIVILEGES;
  ```

---

### 7. **實用 MySQL 指令**
- 列出資料庫：`SHOW DATABASES;`
- 使用資料庫：`USE mydb;`
- 列出表格：`SHOW TABLES;`
- 描述表格結構：`DESCRIBE users;`
- 顯示使用者：`SELECT user FROM mysql.user;`
- 離開 MySQL：`EXIT;` 或 `QUIT;`

---

### 8. **GUI 工具**
- **MySQL Workbench**：官方 GUI 工具
- **phpMyAdmin**：網頁版介面
- **DBeaver**：跨平台資料庫工具
- **HeidiSQL**：輕量級 Windows 客戶端

---

### 9. **學習資源**
- 官方文件：[dev.mysql.com/doc](https://dev.mysql.com/doc/)
- 互動教學：[mysqltutorial.org](https://www.mysqltutorial.org/)
- 練習平台：[sqlzoo.net](https://sqlzoo.net/) 或 [leetcode.com](https://leetcode.com/)

---

**與 PostgreSQL 的主要差異**：
1. 使用 `AUTO_INCREMENT` 而非 `SERIAL`
2. 預設表格名稱不分大小寫
3. 使用 `mysqldump` 而非 `pg_dump`
4. 預設連接埠：**3306**（PostgreSQL 為 5432）
5. 不同的認證系統與使用者管理

**提示**：進行重大變更前務必備份資料庫。關鍵操作請使用交易（`START TRANSACTION`/`COMMIT`）。