---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: आईबीएम डीबी२ में सूचकांक बनाना
translated: true
type: note
---

### IBM DB2 में इंडेक्स बनाना

IBM DB2 क्वेरी परफॉर्मेंस को ऑप्टिमाइज़ करने के लिए इंडेक्स का समर्थन करता है, जिससे डेटा रिट्रीवल तेज़ होता है। इंडेक्स टेबल के एक या अधिक कॉलम पर बनाए जा सकते हैं। नीचे, मैं बुनियादी बातों को कवर करूंगा, जिसमें यूनिक इंडेक्स और मल्टी-कॉलम (कम्पोजिट) इंडेक्स शामिल हैं। ध्यान दें कि "यूनियन इंडेक्स" DB2 डॉक्यूमेंटेशन में एक मानक शब्द नहीं है— इसका मतलब कम्पोजिट इंडेक्स (एक से अधिक की को कवर करना) या क्वेरीज़ में यूनियन ऑपरेशंस की गलतफहमी हो सकती है। यदि आपका कुछ और मतलब है, तो कृपया अधिक जानकारी दें!

#### बेसिक इंडेक्स क्रिएशन
सिंगल कॉलम पर एक साधारण इंडेक्स बनाने के लिए `CREATE INDEX` स्टेटमेंट का उपयोग करें। इससे उस कॉलम पर सर्च, सॉर्ट और जॉइन की स्पीड बढ़ती है।

**सिंटैक्स:**
```sql
CREATE INDEX index_name
ON table_name (column_name [ASC | DESC]);
```

**उदाहरण:**
```sql
CREATE INDEX idx_employee_id
ON employees (employee_id ASC);
```

- `ASC` आरोही क्रम में सॉर्ट करता है (डिफॉल्ट); अवरोही के लिए `DESC` का उपयोग करें।
- इंडेक्स डिफॉल्ट रूप से नॉन-यूनिक होते हैं, जो डुप्लिकेट वैल्यूज़ की अनुमति देते हैं।

#### यूनिक इंडेक्स (यूनिक कीज़ लागू करना)
एक यूनिक इंडेक्स यह सुनिश्चित करता है कि इंडेक्स किए गए कॉलम(s) में कोई डुप्लिकेट वैल्यू न हो, यह एक यूनिक कंस्ट्रेंट की तरह ही है। जब आप प्राइमरी की या यूनिक कंस्ट्रेंट डिफाइन करते हैं, तो DB2 स्वचालित रूप से एक यूनिक इंडेक्स बना देता है।

**सिंटैक्स:**
```sql
CREATE UNIQUE INDEX index_name
ON table_name (column_name [ASC | DESC]);
```

**उदाहरण:**
```sql
CREATE UNIQUE INDEX uidx_email
ON users (email ASC);
```

- यह डुप्लिकेट ईमेल डालने से रोकता है।
- आंशिक यूनिकनेस के लिए (जैसे, NULL को नज़रअंदाज करना), `WHERE NOT NULL` जोड़ें:  
  ```sql
  CREATE UNIQUE WHERE NOT NULL INDEX uidx_email
  ON users (email ASC);
  ```
- आप क्वेरी कवरेज के लिए नॉन-की कॉलम्स को शामिल कर सकते हैं:  
  ```sql
  CREATE UNIQUE INDEX uidx_email
  ON users (email ASC) INCLUDE (first_name, last_name);
  ```

#### कम्पोजिट इंडेक्स (मल्टीपल कीज़, जैसे दो या अधिक कॉलम)
एक कम्पोजिट (या मल्टी-कॉलम) इंडेक्स एक से अधिक कीज़ को कवर करता है, यह कॉलम्स के कॉम्बिनेशन पर फिल्टर/जॉइन करने वाली क्वेरीज़ के लिए उपयोगी होता है। कॉलम्स का क्रम मायने रखता है—सबसे सेलेक्टिव कॉलम को पहले रखें।

**सिंटैक्स:**
```sql
CREATE INDEX index_name
ON table_name (column1 [ASC | DESC], column2 [ASC | DESC], ...);
```

**उदाहरण (दो कीज़):**
```sql
CREATE INDEX idx_order_date_customer
ON orders (order_date ASC, customer_id DESC);
```

- यह ऐसी क्वेरीज़ को ऑप्टिमाइज़ करता है जैसे `SELECT * FROM orders WHERE order_date > '2023-01-01' AND customer_id = 123;`।
- यूनिक कम्पोजिट के लिए: `UNIQUE` जोड़ें (जैसे, `CREATE UNIQUE INDEX ...`)।

#### अतिरिक्त सुझाव
- **इंडेक्स वेरिफाई करें:** `SELECT * FROM SYSCAT.INDEXES WHERE TABSCHEMA = 'YOUR_SCHEMA' AND TABNAME = 'YOUR_TABLE';` का उपयोग करें।
- **इंडेक्स ड्रॉप करें:** `DROP INDEX index_name;`।
- इंडेक्स स्टोरेज का उपभोग करते हैं और इंसर्ट/अपडेट को धीमा करते हैं—उनका विवेकपूर्ण उपयोग करें।
- पार्टीशन्ड टेबल्स या एडवांस्ड ऑप्शन्स (जैसे, क्लस्टरिंग) के लिए, DB2 डॉक्स देखें।

[Db2 CREATE INDEX Statement](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=statements-create-index)  
[Db2 Unique Indexes](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=attributes-unique-indexes)  
[Db2 Composite Indexes Example](https://stackoverflow.com/questions/21597015/composite-index-creation-in-db2)  
[Db2 Unique Index Tutorial](https://www.db2tutorial.com/db2-index/db2-unique-index/)