---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: Db2 में विदेशी कुंजियाँ बनाना
translated: true
type: note
---

### IBM Db2 में फॉरेन की बनाना

Db2 में फॉरेन की, एक टेबल (चाइल्ड टेबल) के कॉलम (या कॉलम के सेट) को दूसरी टेबल (पैरेंट टेबल) की प्राइमरी की या यूनिक की से जोड़कर रेफेरेंशियल इंटीग्रिटी को एनफोर्स करती है। यह सुनिश्चित करती है कि चाइल्ड टेबल में मान पैरेंट टेबल में मौजूदा मानों से मेल खाते हैं, जिससे ओर्फन रिकॉर्ड बनने से रोका जा सके।

आप फॉरेन की को या तो `CREATE TABLE` का उपयोग करके टेबल क्रिएशन के दौरान डिफाइन कर सकते हैं या मौजूदा टेबल में `ALTER TABLE` का उपयोग करके जोड़ सकते हैं। सिंटैक्स स्टैंडर्ड SQL है और Db2 के सभी प्लेटफॉर्म (जैसे, LUW, z/OS) पर काम करता है।

#### 1. टेबल क्रिएशन के दौरान फॉरेन की डिफाइन करना (`CREATE TABLE`)
कॉलम डेफिनिशन के अंदर या टेबल डेफिनिशन के अंत में `FOREIGN KEY` क्लॉज का उपयोग करें।

**बेसिक सिंटैक्स:**
```
CREATE TABLE child_table (
    child_column1 datatype,
    foreign_key_column datatype,
    -- अन्य कॉलम...
    CONSTRAINT constraint_name
    FOREIGN KEY (foreign_key_column) 
    REFERENCES parent_table (parent_key_column)
);
```

**उदाहरण:**
मान लीजिए आपके पास `departments` नाम की एक टेबल है जिसकी प्राइमरी की `dept_id` है:
```
CREATE TABLE departments (
    dept_id INTEGER NOT NULL PRIMARY KEY,
    dept_name VARCHAR(50)
);
```

अब एक `employees` टेबल बनाएं जिसमें `dept_id` को रेफरेंस करती हुई एक फॉरेन की हो:
```
CREATE TABLE employees (
    emp_id INTEGER NOT NULL PRIMARY KEY,
    emp_name VARCHAR(100),
    dept_id INTEGER,
    CONSTRAINT fk_emp_dept 
    FOREIGN KEY (dept_id) 
    REFERENCES departments (dept_id)
);
```

यह `employees` टेबल में `dept_id` पर `fk_emp_dept` नाम की एक फॉरेन की बनाता है।

#### 2. मौजूदा टेबल में फॉरेन की जोड़ना (`ALTER TABLE`)
टेबल के बन जाने के बाद कंस्ट्रेंट जोड़ने के लिए `ALTER TABLE` का उपयोग करें। पैरेंट की पहले से मौजूद होनी चाहिए।

**बेसिक सिंटैक्स:**
```
ALTER TABLE child_table 
ADD CONSTRAINT constraint_name 
FOREIGN KEY (foreign_key_column) 
REFERENCES parent_table (parent_key_column);
```

**उदाहरण:**
मौजूदा `employees` टेबल में वही फॉरेन की जोड़ने के लिए:
```
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) 
REFERENCES departments (dept_id);
```

#### अतिरिक्त ऑप्शन
आप यह स्पेसिफाई कर सकते हैं कि जब किसी पैरेंट रो को अपडेट या डिलीट किया जाता है तो क्या एक्शन होगा:
- `ON DELETE CASCADE`: पैरेंट के डिलीट होने पर चाइल्ड रो को भी डिलीट कर देता है।
- `ON DELETE SET NULL`: पैरेंट के डिलीट होने पर चाइल्ड रो में फॉरेन की को NULL सेट कर देता है।
- `ON UPDATE CASCADE`: पैरेंट की के बदलने पर चाइल्ड की को अपडेट कर देता है।
- `ON UPDATE SET NULL`: पैरेंट की के अपडेट होने पर चाइल्ड की को NULL सेट कर देता है।

**ऑप्शन के साथ उदाहरण:**
```
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) 
REFERENCES departments (dept_id)
ON DELETE CASCADE
ON UPDATE RESTRICT;
```

#### मुख्य नियम और विचारणीय बातें
- फॉरेन की कॉलम का डेटा टाइप और लंबाई पैरेंट की कॉलम से मेल खानी चाहिए।
- फॉरेन की बनाने से पहले पैरेंट टेबल में प्राइमरी या यूनिक की डिफाइन होनी चाहिए।
- फॉरेन की उसी टेबल को रेफरेंस कर सकती हैं (सेल्फ-रेफरेंशियल)।
- एक से अधिक कॉलम मिलकर एक कंपोजिट फॉरेन की बना सकते हैं: `FOREIGN KEY (col1, col2) REFERENCES parent (pk1, pk2)`।
- फॉरेन की ड्रॉप करने के लिए: `ALTER TABLE child_table DROP CONSTRAINT constraint_name;`।
- परफॉर्मेंस के लिए फॉरेन की कॉलम पर एक इंडेक्स बनाने की सिफारिश की जाती है।

डेवलपमेंट एनवायरनमेंट में टेस्ट करें, क्योंकि अगर मौजूदा डेटा उनका उल्लंघन करता है (जैसे, ओर्फन रो) तो कंस्ट्रेंट जोड़ने में फेल हो सकता है।

#### संदर्भ
- [Foreign key (referential) constraints - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=constraints-foreign-key-referential)
- [CREATE TABLE statement - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=statements-create-table)
- [ALTER TABLE statement - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=statements-alter-table)
- [Adding a foreign key with Db2 - Stack Overflow](https://stackoverflow.com/questions/59370149/adding-a-foreign-key-with-db2-of-ibm)