---
audio: false
generated: true
lang: hi
layout: post
title: पोस्टग्रेएसक्यूएल डेटाबेस पहुंच प्रदान करें
translated: true
type: note
---

PostgreSQL में किसी user को database तक पहुंच प्रदान करने के लिए, आपको इन steps का पालन करना होगा। मैं आपको psql command-line interface में SQL commands का उपयोग करके process के माध्यम से मार्गदर्शन करूंगा।

PostgreSQL से कनेक्ट करें: आप पहले ही postgres user का उपयोग करके PostgreSQL से कनेक्ट हो चुके हैं, जिसमें आमतौर पर superuser privileges होती हैं।

User बनाएँ (यदि पहले से मौजूद नहीं है): यदि user मौजूद नहीं है, तो आप निम्न command का उपयोग करके एक बना सकते हैं। username और password को वांछित username और password से बदलें।

```
CREATE USER username WITH PASSWORD 'password';
```

Database बनाएँ (यदि पहले से मौजूद नहीं है): यदि database मौजूद नहीं है, तो आप निम्न command का उपयोग करके इसे बना सकते हैं। database_name को वांछित database name से बदलें।

```
CREATE DATABASE database_name;
```

Database पर Privileges प्रदान करें: किसी specific database पर सभी privileges एक user को प्रदान करने के लिए, निम्न command का उपयोग करें। database_name और username को appropriate names से बदलें।

```
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
```

Schema पर Usage प्रदान करें: यदि आप चाहते हैं कि user को database के भीतर एक specific schema तक पहुंच हो, तो आप schema पर usage प्रदान कर सकते हैं। schema_name और username को appropriate names से बदलें।

```
GRANT USAGE ON SCHEMA schema_name TO username;
```

Tables पर Privileges प्रदान करें: किसी schema के भीतर tables पर specific privileges प्रदान करने के लिए, आप निम्न command का उपयोग कर सकते हैं। schema_name, table_name, और username को appropriate names से बदलें।

```
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA schema_name TO username;
```

Privileges को Effective बनाएँ: यदि आपने tables पर privileges प्रदान की हैं, तो आपको future tables के लिए भी default privileges सेट करने की आवश्यकता हो सकती है।

```
ALTER DEFAULT PRIVILEGES IN SCHEMA schema_name GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO username;
```

यहाँ एक example है कि commands कैसी दिख सकती हैं:

```
CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE DATABASE mydatabase;
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
\c mydatabase
GRANT USAGE ON SCHEMA public TO myuser;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO myuser;
```

ये commands एक user को एक specific database और उसकी tables तक full access के साथ सेट अप कर देंगी। अपनी specific needs और security policies के अनुसार commands को adjust करें।