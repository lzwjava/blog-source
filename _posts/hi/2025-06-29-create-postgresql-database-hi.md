---
audio: false
generated: true
lang: hi
layout: post
title: पोस्टग्रेएसक्यूएल डेटाबेस बनाएँ
translated: true
type: note
---

आप पहले से ही PostgreSQL इंटरैक्टिव टर्मिनल (`psql`) में `postgres` यूजर के रूप में हैं, जो बहुत अच्छा है! PostgreSQL में एक डेटाबेस बनाने के लिए, आप `CREATE DATABASE` कमांड का उपयोग कर सकते हैं। यहां एक चरण-दर-चरण गाइड दी गई है:

1.  **सुनिश्चित करें कि आप `psql` में हैं**:
    आप पहले से हैं, जैसा कि `postgres=#` प्रॉम्प्ट दिखा रहा है।

2.  **एक डेटाबेस बनाएं**:
    एक नया डेटाबेस बनाने के लिए निम्नलिखित कमांड का उपयोग करें। `mydatabase` को अपने इच्छित डेटाबेस नाम से बदलें:

    ```sql
    CREATE DATABASE mydatabase;
    ```

    यह `mydatabase` नाम का एक डेटाबेस बनाता है।

3.  **पुष्टि करें कि डेटाबेस बन गया है**:
    सभी डेटाबेस की सूची देखने के लिए:

    ```sql
    \l
    ```

    यह `mydatabase` सहित सभी डेटाबेस की एक तालिका प्रदर्शित करेगा।

4.  **नए डेटाबेस से कनेक्ट करें**:
    नए डेटाबेस में काम शुरू करने के लिए, इससे कनेक्ट करें:

    ```sql
    \c mydatabase
    ```

    यह आपके सत्र को `mydatabase` पर स्विच कर देता है।

5.  **वैकल्पिक: एक यूजर बनाएं और अनुमतियां दें**:
    यदि आप चाहते हैं कि कोई विशिष्ट यूजर इस डेटाबेस को प्रबंधित करे, तो एक बनाएं और विशेषाधिकार प्रदान करें:

    ```sql
    CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
    GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
    ```

    `myuser` और `mypassword` को अपने इच्छित यूजरनेम और पासवर्ड से बदलें।

6.  **`psql` से बाहर निकलें**:
    काम पूरा होने पर, इसके साथ बाहर निकलें:

    ```sql
    \q
    ```

### नोट्स:
- आपके द्वारा देखी गई `Permission denied` त्रुटि (`could not change directory to "/home/lzw/projects/lzwjava.github.io"`) इसलिए है क्योंकि `postgres` यूजर के पास आपके होम डायरेक्टरी तक पहुंच नहीं है। यह डेटाबेस निर्माण को प्रभावित नहीं करती है लेकिन एक प्रतिबंधित डायरेक्टरी से `psql` चलाते समय दिखाई दे सकती है। आप इसे `psql` को उस डायरेक्टरी से चलाकर टाल सकते हैं जिस तक `postgres` यूजर की पहुंच है या डायरेक्टरी बदले बिना (उदाहरण के लिए, `/tmp` से `sudo -u postgres psql` चलाएं)।
- `psql` में आपके द्वारा आजमाया गया `ls` कमांड वैध नहीं है। डेटाबेस की सूची देखने के लिए `\l` या किसी डेटाबेस के भीतर टेबल्स की सूची देखने के लिए `\dt` का उपयोग करें।
- सुनिश्चित करें कि PostgreSQL सेवा चल रही है (`sudo systemctl start postgresql.service`), जो आपने पहले ही कर लिया है।

### उदाहरण सत्र:
```sql
postgres=# CREATE DATABASE mydatabase;
CREATE DATABASE
postgres=# \l
                                  List of databases
   Name      |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-------------+----------+----------+-------------+-------------+-----------------------
 mydatabase  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
 template1   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
(4 rows)

postgres=# \c mydatabase
You are now connected to database "mydatabase" as user "postgres".
mydatabase=# \q
```

यदि आपको और सहायता की आवश्यकता है (उदाहरण के लिए, टेबल सेटअप करना, यूजर बनाना, या किसी एप्लिकेशन से कनेक्ट करना), तो मुझे बताएं!