---
audio: false
generated: true
lang: ar
layout: post
title: 'دليل إدارة قواعد البيانات: PostgreSQL'
translated: true
type: note
---

إليك دليلًا خطوة بخطوة لاستخدام PostgreSQL، نظام إدارة قواعد البيانات العلائقية مفتوح المصدر القوي:

### 1. **التثبيت**
- **Windows**: حمّل من [postgresql.org/download](https://www.postgresql.org/download/) (يتضمن واجهة pgAdmin الرسومية)
- **macOS**: استخدم Homebrew (`brew install postgresql`) أو حمّل المثبِّت
- **Linux** (Debian/Ubuntu):
  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  sudo systemctl start postgresql.service
  ```

### 2. **الاتصال بـ PostgreSQL**
- مستخدم المدير الافتراضي: `postgres`
  ```bash
  sudo -u postgres psql  # Linux/macOS
  psql -U postgres       # Windows (عبر سطر أوامر PSQL)
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
      id SERIAL