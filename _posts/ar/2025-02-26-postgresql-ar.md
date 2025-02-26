---
audio: false
lang: ar
layout: post
title: دليل إدارة قواعد البيانات PostgreSQL
translated: true
---

هنا دليل خطوة بخطوة لاستخدام PostgreSQL، نظام إدارة قواعد البيانات العلائقية المفتوحة المصدر القوي:

### 1. **التثبيت**
- **Windows**: تحميل من [postgresql.org/download](https://www.postgresql.org/download/) (يشمل pgAdmin GUI)
- **macOS**: استخدام Homebrew (`brew install postgresql`) أو تحميل المثبّت
- **Linux** (Debian/Ubuntu):
  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  sudo systemctl start postgresql.service
  ```

### 2. **الاتصال بPostgreSQL**
- المستخدم الإداري الافتراضي: `postgres`
  ```bash
  sudo -u postgres psql  # Linux/macOS
  psql -U postgres       # Windows (من خلال PSQL command line)
  ```
- الاتصال بقاعدة بيانات محددة:
  ```bash
  psql -U username -d dbname -h localhost -p 5432
  ```

### 3. **عمليات قاعدة البيانات الأساسية**
- **إنشاء مستخدم/دور**:
  ```sql
  CREATE USER myuser WITH PASSWORD 'mypassword';
  ALTER ROLE myuser WITH CREATEDB;
  ```
- **إنشاء قاعدة بيانات**:
  ```sql
  CREATE DATABASE mydb;
  GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
  ```
- **أوامر SQL الأساسية**:
  ```sql
  -- إنشاء جدول
  CREATE TABLE users (
      id SERIAL PRIMARY KEY,
      name VARCHAR(50),
      email VARCHAR(100) UNIQUE
  );

  -- إدخال البيانات
  INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

  -- استعلام البيانات
  SELECT * FROM users WHERE name LIKE 'A%';

  -- تحديث البيانات
  UPDATE users SET email = 'new@email.com' WHERE id = 1;

  -- حذف البيانات
  DELETE FROM users WHERE id = 2;
  ```

### 4. **الميزات المتقدمة**
- **الاندماجات**:
  ```sql
  SELECT orders.id, users.name
  FROM orders
  INNER JOIN users ON orders.user_id = users.id;
  ```
- **دعم JSON**:
  ```sql
  CREATE TABLE products (
      id SERIAL PRIMARY KEY,
      details JSONB
  );
  ```
- **البحث النصي الكامل**:
  ```sql
  SELECT * FROM documents
  WHERE to_tsvector('english', content) @@ to_tsquery('search & term');
  ```

### 5. **الصيانة**
- **النسخ الاحتياطي**:
  ```bash
  pg_dump mydb > backup.sql
  pg_dumpall > all_databases.sql
  ```
- **استعادة**:
  ```bash
  psql -U username -d mydb -f backup.sql
  ```
- **الفراغ** (استعادة التخزين):
  ```sql
  VACUUM ANALYZE;
  ```

### 6. **الأمن**
- إنشاء مستخدم فقط للقراءة:
  ```sql
  CREATE USER readonly WITH PASSWORD 'readpass';
  GRANT CONNECT ON DATABASE mydb TO readonly;
  GRANT USAGE ON SCHEMA public TO readonly;
  GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
  ```

### 7. **الأوامر المفيدة**
- قائمة قواعد البيانات: `\l`
- تبديل قاعدة البيانات: `\c dbname`
- قائمة الجداول: `\dt`
- وصف الجدول: `\d tablename`
- عرض المستخدمين: `\du`
- الخروج من psql: `\q`

### 8. **أدوات الواجهة الرسومية**
- **pgAdmin**: مرفق مع تثبيت Windows
- **DBeaver**: واجهة رسومية شائعة متعددة المنصات
- **TablePlus**: واجهة حديثة مع شعور محلي

### 9. **مصادر التعلم**
- الوثائق الرسمية: [postgresql.org/docs](https://www.postgresql.org/docs/)
- الدرس التفاعلي: [postgresqltutorial.com](https://www.postgresqltutorial.com/)
- الممارسة: [pgexercises.com](https://pgexercises.com/)

**نصيحه**: دائمًا اختبار التغييرات في بيئة تطوير قبل تطبيقها على الإنتاج. استخدم المعاملات (`BEGIN`/`COMMIT`) لأعمال حاسمة.