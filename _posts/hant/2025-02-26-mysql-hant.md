---
audio: false
generated: false
lang: hant
layout: post
title: 使用 MySQL
translated: true
---

這是一個使用 MySQL 的逐步指南，MySQL 是一個流行的開源關聯式資料庫管理系統：

---

### 1. **安裝**
- **Windows**：從 [mysql.com/downloads](https://dev.mysql.com/downloads/installer/) 下載 MySQL 安裝程序
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
  sudo mysql_secure_installation  # 運行安全設置
  ```

---

### 2. **連接到 MySQL**
- **預設 root 登錄**：
  ```bash
  mysql -u root -p  # 提示輸入密碼
  ```
- **連接到遠程伺服器**：
  ```bash
  mysql -u username -p -h hostname -P 3306
  ```

---

### 3. **基本資料庫操作**
- **創建用戶**：
  ```sql
  CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
  ```
- **創建資料庫**：
  ```sql
  CREATE DATABASE mydb;
  GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'localhost';
  FLUSH PRIVILEGES;
  ```
- **基本 SQL 命令**：
  ```sql
  -- 創建表
  CREATE TABLE users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(50),
      email VARCHAR(100) UNIQUE
  );

  -- 插入數據
  INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com');

  -- 查詢數據
  SELECT * FROM users WHERE name LIKE 'B%';

  -- 更新數據
  UPDATE users SET email = 'new@email.com' WHERE id = 1;

  -- 刪除數據
  DELETE FROM users WHERE id = 2;
  ```

---

### 4. **高級功能**
- **連接**：
  ```sql
  SELECT orders.id, users.name
  FROM orders
  JOIN users ON orders.user_id = users.id;
  ```
- **存儲過程**：
  ```sql
  DELIMITER //
  CREATE PROCEDURE GetUsers()
  BEGIN
    SELECT * FROM users;
  END //
  DELIMITER ;

  CALL GetUsers();
  ```
- **JSON 支持** (MySQL 5.7+)：
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
- **優化表**：
  ```sql
  ANALYZE TABLE users;
  OPTIMIZE TABLE users;
  ```

---

### 6. **安全性**
- **創建只讀用戶**：
  ```sql
  CREATE USER 'reader'@'localhost' IDENTIFIED BY 'readpass';
  GRANT SELECT ON mydb.* TO 'reader'@'localhost';
  FLUSH PRIVILEGES;
  ```

---

### 7. **有用的 MySQL 命令**
- 列出資料庫：`SHOW DATABASES;`
- 使用資料庫：`USE mydb;`
- 列出表：`SHOW TABLES;`
- 描述表：`DESCRIBE users;`
- 顯示用戶：`SELECT user FROM mysql.user;`
- 退出 MySQL：`EXIT;` 或 `QUIT;`

---

### 8. **GUI 工具**
- **MySQL Workbench**：官方 GUI 工具
- **phpMyAdmin**：基於網頁的介面
- **DBeaver**：跨平台資料庫工具
- **HeidiSQL**：輕量級 Windows 客戶端

---

### 9. **學習資源**
- 官方文檔：[dev.mysql.com/doc](https://dev.mysql.com/doc/)
- 互動教程：[mysqltutorial.org](https://www.mysqltutorial.org/)
- 練習：[sqlzoo.net](https://sqlzoo.net/) 或 [leetcode.com](https://leetcode.com/)

---

**與 PostgreSQL 的關鍵差異**：
1. 使用 `AUTO_INCREMENT` 而不是 `SERIAL`
2. 預設情況下表名不區分大小寫
3. 使用 `mysqldump` 而不是 `pg_dump`
4. 預設端口：**3306** (與 PostgreSQL 的 5432)
5. 不同的驗證系統和用戶管理

**提示**：在進行重大變更之前，始終備份資料庫。對於關鍵操作，使用交易 (`START TRANSACTION`/`COMMIT`)。