---
audio: false
generated: false
lang: hi
layout: post
title: 'PostgreSQL: डेटाबेस प्रबंधन गाइड'
translated: true
---

यह PostgreSQL, एक शक्तिशाली ओपन-सोर्स रिलेशनल डेटाबेस मैनेजमेंट सिस्टम का उपयोग करने के लिए एक चरण-दर-चरण गाइड है:

### 1. **इंस्टॉलेशन**
- **Windows**: [postgresql.org/download](https://www.postgresql.org/download/) से डाउनलोड करें (pgAdmin GUI शामिल है)
- **macOS**: Homebrew का उपयोग करें (`brew install postgresql`) या इंस्टॉलर डाउनलोड करें
- **Linux** (Debian/Ubuntu):
  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  sudo systemctl start postgresql.service
  ```

### 2. **PostgreSQL से कनेक्ट करें**
- डिफ़ॉल्ट एडमिन यूजर: `postgres`
  ```bash
  sudo -u postgres psql  # Linux/macOS
  psql -U postgres       # Windows (via PSQL command line)
  ```
- एक विशेष डेटाबेस से कनेक्ट करें:
  ```bash
  psql -U username -d dbname -h localhost -p 5432
  ```

### 3. **बेसिक डेटाबेस ऑपरेशंस**
- **यूजर/रोल बनाएं**:
  ```sql
  CREATE USER myuser WITH PASSWORD 'mypassword';
  ALTER ROLE myuser WITH CREATEDB;
  ```
- **डेटाबेस बनाएं**:
  ```sql
  CREATE DATABASE mydb;
  GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
  ```
- **बेसिक SQL कमांड्स**:
  ```sql
  -- टेबल बनाएं
  CREATE TABLE users (
      id SERIAL PRIMARY KEY,
      name VARCHAR(50),
      email VARCHAR(100) UNIQUE
  );

  -- डेटा इंसर्ट करें
  INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

  -- डेटा क्वेरी करें
  SELECT * FROM users WHERE name LIKE 'A%';

  -- डेटा अपडेट करें
  UPDATE users SET email = 'new@email.com' WHERE id = 1;

  -- डेटा डिलीट करें
  DELETE FROM users WHERE id = 2;
  ```

### 4. **एडवांस्ड फीचर्स**
- **जॉइन्स**:
  ```sql
  SELECT orders.id, users.name
  FROM orders
  INNER JOIN users ON orders.user_id = users.id;
  ```
- **JSON समर्थन**:
  ```sql
  CREATE TABLE products (
      id SERIAL PRIMARY KEY,
      details JSONB
  );
  ```
- **फुल-टेक्स्ट सर्च**:
  ```sql
  SELECT * FROM documents
  WHERE to_tsvector('english', content) @@ to_tsquery('search & term');
  ```

### 5. **मेनटेनेंस**
- **बैकअप**:
  ```bash
  pg_dump mydb > backup.sql
  pg_dumpall > all_databases.sql
  ```
- **रिस्टोर**:
  ```bash
  psql -U username -d mydb -f backup.sql
  ```
- **वैक्यूम** (स्टोरेज वापस लेना):
  ```sql
  VACUUM ANALYZE;
  ```

### 6. **सिक्योरिटी**
- रीड-ऑनली यूजर बनाएं:
  ```sql
  CREATE USER readonly WITH PASSWORD 'readpass';
  GRANT CONNECT ON DATABASE mydb TO readonly;
  GRANT USAGE ON SCHEMA public TO readonly;
  GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
  ```

### 7. **उपयोगी कमांड्स**
- डेटाबेस सूची: `\l`
- डेटाबेस स्विच करें: `\c dbname`
- टेबल सूची: `\dt`
- टेबल वर्णन करें: `\d tablename`
- यूजर दिखाएं: `\du`
- psql से बाहर निकलें: `\q`

### 8. **GUI टूल्स**
- **pgAdmin**: Windows इंस्टॉलर के साथ शामिल है
- **DBeaver**: लोकप्रिय क्रॉस-प्लेटफॉर्म GUI
- **TablePlus**: नेटिव फील के साथ आधुनिक इंटरफ़ेस

### 9. **लर्निंग रिसोर्सेस**
- आधिकारिक डॉक्यूमेंटेशन: [postgresql.org/docs](https://www.postgresql.org/docs/)
- इंटरैक्टिव ट्यूटोरियल: [postgresqltutorial.com](https://www.postgresqltutorial.com/)
- प्रैक्टिस: [pgexercises.com](https://pgexercises.com/)

**टिप**: हमेशा परिवर्तन को डेवलपमेंट एनवायरमेंट में टेस्ट करें, पहले प्रोडक्शन में लागू करें। क्रिटिकल ऑपरेशंस के लिए ट्रांजैक्शंस (`BEGIN`/`COMMIT`) का उपयोग करें।