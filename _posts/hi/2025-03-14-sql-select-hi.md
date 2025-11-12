---
audio: false
generated: true
lang: hi
layout: post
title: एसक्यूएल सिलेक्ट स्टेटमेंट्स
translated: true
type: note
---

आपके SQL में `SELECT`, `LEFT JOIN`, `RIGHT JOIN`, कॉम्प्लेक्स `SELECT`, `FROM`, `GROUP BY`, `WHERE NOT IN`, और `IN` के उपयोग के बारे में प्रश्न का उत्तर देने के लिए, मैं प्रत्येक घटक को स्पष्ट रूप से समझाऊंगा और व्यावहारिक उदाहरण दूंगा। ये डेटाबेस से डेटा पुनर्प्राप्त करने और उसे परिवर्तित करने के लिए उपयोग की जाने वाली मौलिक SQL संचालन हैं। आइए इन्हें चरण दर चरण तोड़ते हैं, एक सरल डेटाबेस स्कीमा का उपयोग करते हुए:

- **टेबल:**
  - `employees` (कॉलम: `employee_id`, `employee_name`, `department_id`, `salary`)
  - `departments` (कॉलम: `department_id`, `department_name`)
  - `projects` (कॉलम: `project_id`, `project_name`, `employee_id`)

---

### 1. SELECT
`SELECT` क्लॉज़ का उपयोग उन कॉलम को निर्दिष्ट करने के लिए किया जाता है जिन्हें आप डेटाबेस टेबल से पुनर्प्राप्त करना चाहते हैं। यह किसी भी SQL क्वेरी की आधारशिला है।

- **उद्देश्य:** चुनना कि कौन सा डेटा प्रदर्शित करना है।
- **उदाहरण:**
  ```sql
  SELECT employee_name, salary
  FROM employees;
  ```
  यह `employees` टेबल से `employee_name` और `salary` कॉलम पुनर्प्राप्त करता है।

---

### 2. FROM
`FROM` क्लॉज़ उस टेबल (या टेबल्स) की पहचान करता है जहाँ से डेटा खींचना है। इसका उपयोग हमेशा `SELECT` के साथ किया जाता है।

- **उद्देश्य:** डेटा स्रोत निर्दिष्ट करना।
- **उदाहरण:**
  ```sql
  SELECT employee_name
  FROM employees;
  ```
  यहाँ, `employees` वह टेबल है जिसे क्वेरी किया जा रहा है।

---

### 3. LEFT JOIN
एक `LEFT JOIN` (या `LEFT OUTER JOIN`) दो टेबल्स की पंक्तियों को संयोजित करता है। यह बाईं टेबल की सभी रिकॉर्ड और दाईं टेबल की मेल खाने वाली रिकॉर्ड लौटाता है। यदि कोई मेल नहीं है, तो परिणाम में दाईं टेबल के कॉलम के लिए `NULL` मान शामिल होते हैं।

- **उद्देश्य:** बाईं टेबल की सभी पंक्तियों को शामिल करना, भले ही दाईं टेबल में मेल हों या न हों।
- **उदाहरण:**
  ```sql
  SELECT e.employee_name, d.department_name
  FROM employees e
  LEFT JOIN departments d
  ON e.department_id = d.department_id;
  ```
  यह सभी कर्मचारियों और उनके विभाग के नामों की सूची देता है। यदि कोई कर्मचारी किसी विभाग को नियत नहीं है, तो `department_name` `NULL` होगा।

---

### 4. RIGHT JOIN
एक `RIGHT JOIN` (या `RIGHT OUTER JOIN`) एक `LEFT JOIN` के समान है, लेकिन यह दाईं टेबल की सभी रिकॉर्ड और बाईं टेबल की मेल खाने वाली रिकॉर्ड लौटाता है। बाईं टेबल की मेल न खाने वाली पंक्तियों के परिणामस्वरूप `NULL` मान होते हैं।

- **उद्देश्य:** दाईं टेबल की सभी पंक्तियों को शामिल करना, भले ही बाईं टेबल में मेल हों या न हों।
- **उदाहरण:**
  ```sql
  SELECT e.employee_name, d.department_name
  FROM employees e
  RIGHT JOIN departments d
  ON e.department_id = d.department_id;
  ```
  यह सभी विभागों और उनके कर्मचारियों को दिखाता है। बिना कर्मचारियों वाले विभागों में `employee_name` में `NULL` होगा।

---

### 5. कॉम्प्लेक्स SELECT
"कॉम्प्लेक्स `SELECT`" एक औपचारिक SQL शब्द नहीं है, लेकिन आमतौर पर एक `SELECT` स्टेटमेंट को संदर्भित करता है जो उन्नत डेटा पुनर्प्राप्ति करने के लिए कई क्लॉज, जॉइन, सबक्वेरीज़, या एग्रीगेट फ़ंक्शन को जोड़ता है।

- **उद्देश्य:** कई संचालनों वाली जटिल क्वेरीज़ को संभालना।
- **उदाहरण:**
  ```sql
  SELECT d.department_name, COUNT(e.employee_id) AS employee_count
  FROM departments d
  LEFT JOIN employees e
  ON d.department_id = e.department_id
  GROUP BY d.department_name
  HAVING COUNT(e.employee_id) > 5;
  ```
  यह 5 से अधिक कर्मचारियों वाले विभाग ढूंढता है, प्रति विभाग कर्मचारियों की गिनती करता है और परिणामों को फ़िल्टर करता है।

---

### 6. GROUP BY
`GROUP BY` क्लॉज़ समान मानों वाली पंक्तियों को निर्दिष्ट कॉलम में सारांश पंक्तियों में समूहित करता है, जिनका उपयोग अक्सर `COUNT`, `SUM`, या `AVG` जैसे एग्रीगेट फ़ंक्शन के साथ किया जाता है।

- **उद्देश्य:** कॉलम मानों के आधार पर डेटा एकत्रित करना।
- **उदाहरण:**
  ```sql
  SELECT department_id, COUNT(employee_id) AS employee_count
  FROM employees
  GROUP BY department_id;
  ```
  यह प्रत्येक विभाग में कर्मचारियों की संख्या गिनता है।

---

### 7. WHERE NOT IN
`WHERE NOT IN` क्लॉज़ उन पंक्तियों को फ़िल्टर करता है जहाँ किसी कॉलम का मान किसी निर्दिष्ट सूची या सबक्वेरी परिणाम में मौजूद नहीं है। सावधान रहें: यदि सूची/सबक्वेरी में `NULL` शामिल है, तो कोई भी पंक्ति वापस नहीं आ सकती है।

- **उद्देश्य:** मानों के एक सेट के आधार पर पंक्तियों को बाहर करना।
- **उदाहरण:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id NOT IN (1, 2);
  ```
  यह उन कर्मचारियों को पुनर्प्राप्त करता है जो विभाग 1 या 2 में नहीं हैं।

- **सबक्वेरी के साथ:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id NOT IN (SELECT department_id FROM departments WHERE department_name = 'Inactive');
  ```
  यह उन कर्मचारियों को ढूंढता है जो 'Inactive' चिह्नित विभागों में नहीं हैं।

---

### 8. IN
`IN` क्लॉज़ उन पंक्तियों को फ़िल्टर करता है जहाँ किसी कॉलम का मान किसी सूची या सबक्वेरी में किसी भी मान से मेल खाता है। यह कई `OR` शर्तों के लिए एक शॉर्टहैंड है।

- **उद्देश्य:** मानों के एक सेट के आधार पर पंक्तियों को शामिल करना।
- **उदाहरण:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id IN (3, 4);
  ```
  यह विभाग 3 या 4 में कर्मचारियों को पुनर्प्राप्त करता है।

- **सबक्वेरी के साथ:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id IN (
      SELECT department_id
      FROM employees
      GROUP BY department_id
      HAVING COUNT(employee_id) > 5
  );
  ```
  यह उन कर्मचारियों को ढूंढता है जो 5 से अधिक कर्मचारियों वाले विभागों में हैं।

---

### सभी को एक साथ रखना
यहाँ इनमें से कई संचालनों को जोड़ने वाला एक उदाहरण दिया गया है:
```sql
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
WHERE e.department_id NOT IN (1, 2)
GROUP BY d.department_name;
```
- **स्पष्टीकरण:**
  - `FROM departments d`: `departments` टेबल से शुरू होता है।
  - `LEFT JOIN employees e`: सभी विभागों को शामिल करता है, चाहे उनमें कर्मचारी हों या न हों।
  - `WHERE NOT IN (1, 2)`: विभाग 1 और 2 के कर्मचारियों को बाहर करता है।
  - `GROUP BY d.department_name`: परिणामों को विभाग के नाम से समूहित करता है।
  - `SELECT ... COUNT`: प्रति विभाग कर्मचारियों की गिनती करता है।

---

### मुख्य सुझाव
- **जॉइन:** `LEFT JOIN` या `RIGHT JOIN` का चयन इस आधार पर करें कि आप किस टेबल की पंक्तियों को पूरी तरह से रखना चाहते हैं (बाएँ या दाएँ)।
- **NOT IN के साथ NULL:** यदि कोई सबक्वेरी `NULL` लौटाती है, तो `NOT IN` अप्रत्याशित रूप से सभी पंक्तियों को बाहर कर सकता है। एक विकल्प के रूप में `NOT EXISTS` पर विचार करें।
- **कॉम्प्लेक्स क्वेरीज़:** शुद्धता सुनिश्चित करने के लिए उन्हें भागों में तोड़ें (उदाहरण के लिए, जॉइन को अलग से परखें)।
- **क्रम मायने रखता है:** `GROUP BY` से पहले `WHERE` रखें, और समूह-स्तरीय फ़िल्टर के लिए `GROUP BY` के बाद `HAVING` का उपयोग करें।

इन SQL घटकों—`SELECT`, `FROM`, `LEFT JOIN`, `RIGHT JOIN`, `GROUP BY`, `WHERE NOT IN`, और `IN`—को समझकर और संयोजित करके, आप किसी भी रिलेशनल डेटाबेस से डेटा को प्रभावी ढंग से पुनर्प्राप्त करने और विश्लेषण करने के लिए क्वेरीज़ तैयार कर सकते हैं।