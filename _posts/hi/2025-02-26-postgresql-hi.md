---
audio: false
generated: true
lang: hi
layout: post
title: 'PostgreSQL: डेटाबेस प्रबंधन गाइड'
translated: true
type: note
---

PostgreSQL का उपयोग करने के लिए एक चरण-दर-चरण मार्गदर्शिका यहां दी गई है, जो एक शक्तिशाली ओपन-सोर्स रिलेशनल डेटाबेस मैनेजमेंट सिस्टम है:

### 1. **इंस्टालेशन**
- **Windows**: [postgresql.org/download](https://www.postgresql.org/download/) से डाउनलोड करें (इसमें pgAdmin GUI शामिल है)
- **macOS**: Homebrew (`brew install postgresql`) का उपयोग करें या इंस्टॉलर डाउनलोड करें
- **Linux** (Debian/Ubuntu):
  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  sudo systemctl start postgresql.service
  ```

### 2. **PostgreSQL से कनेक्ट करें**
- डिफ़ॉल्ट एडमिन यूज़र: `postgres`
  ```bash
  sudo -u postgres psql  # Linux/macOS
  psql -U postgres       # Windows (PSQL कमांड लाइन के माध्यम से)
  ```
- किसी विशिष्ट डेटाबेस से कनेक्ट करें:
  ```bash
  psql -U username -d dbname -h localhost -p 5432
  ```

### 3. **बेसिक डेटाबेस ऑपरेशन्स**
- **यूज़र/रोल बनाएँ**:
  ```sql
  CREATE USER myuser WITH PASSWORD 'mypassword';
  ALTER ROLE myuser WITH CREATEDB;
  ```
- **डेटाबेस बनाएँ**:
  ```sql
  CREATE DATABASE mydb;
  GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
  ```
- **बेसिक SQL कमांड्स**:
  ```sql
  -- टेबल बनाएँ
  CREATE TABLE users (
      id SERIAL PRIMARY KEY,
      name VARCHAR(50),
      email VARCHAR(100) UNIQUE
  );

  -- डेटा इन्सर्ट करें
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
- **JSON सपोर्ट**:
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

### 5. **मेंटेनेंस**
- **बैकअप**:
  ```bash
  pg_dump mydb > backup.sql
  pg_dumpall > all_databases.sql
  ```
- **रिस्टोर**:
  ```bash
  psql -U username -d mydb -f backup.sql
  ```
- **वैक्यूम** (स्टोरेज रिक्लेम करें):
  ```sql
  VACUUM ANALYZE;
  ```

### 6. **सिक्योरिटी**
- रीड-ओनली यूज़र बनाएँ:
  ```sql
  CREATE USER readonly WITH PASSWORD 'readpass';
  GRANT CONNECT ON DATABASE mydb TO readonly;
  GRANT USAGE ON SCHEMA public TO readonly;
  GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
  ```

### 7. **यूज़फुल कमांड्स**
- डेटाबेस लिस्ट करें: `\l`
- डेटाबेस स्विच करें: `\c dbname`
- टेबल्स लिस्ट करें: `\dt`
- टेबल डिस्क्राइब करें: `\d tablename`
- यूज़र्स दिखाएँ: `\du`
- psql से बाहर निकलें: `\q`

### 8. **GUI टूल्स**
- **pgAdmin**: Windows इंस्टॉलर के साथ शामिल
- **DBeaver**: पॉपुलर क्रॉस-प्लेटफ़ॉर्म GUI
- **TablePlus**: नेटिव फील के साथ मॉडर्न इंटरफेस

### 9. **लर्निंग रिसोर्सेज**
- ऑफिशियल डॉक्यूमेंटेशन: [postgresql.org/docs](https://www.postgresql.org/docs/)
- इंटरएक्टिव ट्यूटोरियल: [postgresqltutorial.com](https://www.postgresqltutorial.com/)
- प्रैक्टिस: [pgexercises.com](https://pgexercises.com/)

**टिप**: प्रोडक्शन में लागू करने से पहले हमेशा डेवलपमेंट एनवायरनमेंट में बदलावों का टेस्ट करें। क्रिटिकल ऑपरेशन्स के लिए ट्रांजैक्शन (`BEGIN`/`COMMIT`) का उपयोग करें।