---
audio: false
generated: true
image: false
lang: hi
layout: post
title: वास स्प्रिंग जेडीबीसी टाइमआउट ट्राइएज गाइड
translated: true
type: note
---

यहाँ मेंटल मॉडल और एक क्विक ट्राएज प्लेबुक दिया गया है।

# यह कैसे काम करता है (WAS + Spring + JDBC)

1.  **DataSource, WAS में रहती है**

    *   आप WAS एडमिन कंसोल में एक JDBC Provider और एक **DataSource** (आमतौर पर ग्लोबल ट्रांजैक्शन के लिए `XA`, या गैर-XA) डिफाइन करते हैं।
    *   WAS **JCA कनेक्शन पूल** को मैनेज करता है और JDBC कनेक्शन देता है।

2.  **Spring, DataSource को JNDI के जरिए प्राप्त करता है**

    *   आपका Spring ऐप सर्वर की DataSource को लुकअप करता है (जैसे, `java:comp/env/jdbc/MyDS`) और उसे रैप करता है:

        *   प्लेन JDBC: `JdbcTemplate` उस DataSource का उपयोग करता है।
        *   JPA/Hibernate: `EntityManagerFactory` इसका उपयोग करती है।
    *   ट्रांजैक्शन आमतौर पर **कंटेनर JTA** (`WebSphereUowTransactionManager` या स्टैंडर्ड JTA) होते हैं। Spring का `@Transactional` कंटेनर ट्रांजैक्शन में शामिल हो जाता है।

3.  **कॉल पाथ**

    *   वेब रिक्वेस्ट → WebContainer थ्रेड → Spring सर्विस → tx शुरू होता है (JTA) → **WAS पूल** से `DataSource.getConnection()` → ड्राइवर के जरिए SQL → DB.
    *   टाइमआउट कई लेयर्स पर हो सकते हैं (Spring, JPA, WAS पूल, JTA tx, JDBC ड्राइवर/DB, नेटवर्क)।

# जब कोई टाइमआउट होता है — पहचानें कि किस प्रकार का है

चार बकेट में सोचें। संदेश/स्टैक आमतौर पर आपको बताता है कि कौन सा है।

1.  **कनेक्शन एक्विजिशन टाइमआउट**
    लक्षण: पूल्ड कनेक्शन की प्रतीक्षा करना।
    पूल एक्जॉशन या `J2CA0086W / J2CA0030E` के बारे में संदेश देखें।
    टाइपिकल नॉब्स: *Maximum Connections*, *Connection Timeout*, *Aged Timeout*, *Purge Policy*.

2.  **ट्रांजैक्शन टाइमआउट (JTA)**
    लक्षण: `WTRN`/`Transaction` संदेश; एक्सेप्शन जैसे *"Transaction timed out after xxx seconds"*।
    टाइपिकल नॉब: **Total transaction lifetime timeout**। लंबे DB ऑप्स को किल कर सकता है भले ही DB अभी भी काम कर रहा हो।

3.  **क्वेरी/स्टेटमेंट टाइमआउट**
    लक्षण: `java.sql.SQLTimeoutException`, Hibernate/JPA "query timeout", या Spring `QueryTimeoutException`।
    नॉब्स:

    *   Spring: `JdbcTemplate.setQueryTimeout(...)`, Hibernate `javax.persistence.query.timeout` / `hibernate.jdbc.timeout`.
    *   WAS DataSource कस्टम प्रॉपर्टीज़ (DB2 उदाहरण): `queryTimeout`, `queryTimeoutInterruptProcessingMode`.
    *   ड्राइवर/DB-साइड स्टेटमेंट टाइमआउट।

4.  **सॉकेट/रीड टाइमआउट / नेटवर्क**
    लक्षण: लंबे फ़ेच के दौरान कुछ आइडल टाइम के बाद; लो-लेवल `SocketTimeoutException` या वेंडर कोड।
    नॉब्स: ड्राइवर `loginTimeout`/`socketTimeout`, फ़ायरवॉल/NAT आइडल्स, DB कीपअलाइव्स।

# कहाँ चेक करें (लेयर के अनुसार)

**WAS एडमिन कंसोल पाथ (ट्रेडिशनल WAS)**

*   JDBC Provider / DataSource:
    Resources → JDBC → Data sources → *YourDS* →

    *   *Connection pool properties*: **Connection timeout**, **Maximum connections**, **Reap time**, **Unused timeout**, **Aged timeout**, **Purge policy**.
    *   *Custom properties*: वेंडर-स्पेसिफिक (जैसे, DB2 `queryTimeout`, `currentSQLID`, `blockingReadConnectionTimeout`, `queryTimeoutInterruptProcessingMode`).
    *   *JAAS – J2C* अगर ऑथ अलायसिस मैटर करते हैं।
*   Transactions:
    Application servers → *server1* → Container Settings → **Container Services → Transaction Service** → **Total transaction lifetime timeout**, **Maximum transaction timeout**.
*   WebContainer:
    थ्रेड पूल साइज (अगर रिक्वेस्ट्स जमा हो जाती हैं)।

**लॉग्स और ट्रेसेस**

*   ट्रेडिशनल WAS: `<profile_root>/logs/<server>/SystemOut.log` और `SystemErr.log`।
    की कंपोनेंट्स: `RRA` (रिसोर्स एडाप्टर), `JDBC`, `ConnectionPool`, `WTRN` (ट्रांजैक्शन)।
    ट्रेस एनेबल करें (संक्षिप्त स्टार्टर):

    ```
    RRA=all:WTRN=all:Transaction=all:JDBC=all:ConnectionPool=all
    ```

    इन्हें देखें:

    *   `J2CA0086W`, `J2CA0114W` (पूल/कनेक्शन इशूज़)
    *   `WTRN0037W`, `WTRN0124I` (tx टाइमआउट/रोलबैक)
    *   `DSRA`/`SQL` एक्सेप्शन वेंडर SQL कोड के साथ।
*   Liberty: `messages.log` `wlp/usr/servers/<server>/logs/` के अंदर।

**PMI / मॉनिटरिंग**

*   JDBC Connection Pools और Transaction मेट्रिक्स के लिए **PMI** एनेबल करें। इन पर नजर रखें:

    *   पूल साइज, इन-यूज़ काउंट, वेटर्स, वेट टाइम, टाइमआउट।
    *   ट्रांजैक्शन टाइमआउट/रोलबैक काउंट्स।

**Spring/JPA ऐप लॉग्स**

*   अपने ऐप में SQL + टाइमिंग चालू करें (`org.hibernate.SQL`, `org.hibernate.type`, Spring JDBC डीबग) टाइमआउट बनाम ड्यूरेशन को करिलेट करने के लिए।

**डेटाबेस और ड्राइवर**

*   DB2: `db2diag.log`, `MON_GET_PKG_CACHE_STMT`, एक्टिविटी इवेंट मॉनिटर्स, स्टेटमेंट-लेवल टाइमआउट।
*   ड्राइवर प्रॉपर्टीज़ WAS DataSource में या `DriverManager` में अगर आप कंटेनर DS का उपयोग नहीं कर रहे हैं (WAS पर टाइपिकल नहीं)।

**नेटवर्क**

*   आइडल टाइमआउट वाले मिडलबॉक्सेस। OS कीपअलाइव / ड्राइवर कीपअलाइव सेटिंग्स।

# क्विक ट्राएज फ्लो

1.  **टाइमआउट को क्लासिफाई करें**

    *   *कनेक्शन वेट?* `J2CA` पूल वॉर्निंग देखें। अगर हां, तो **Maximum connections** बढ़ाएं, लीक फिक्स करें, पूल ट्यून करें, पॉइजन इवेंट्स के लिए **Purge Policy = EntirePool** सेट करें।
    *   *Tx टाइमआउट?* `WTRN` संदेश। **Total transaction lifetime timeout** बढ़ाएं या प्रति tx काम कम करें; बड़े बैच जॉब्स को एक tx में रैप करने से बचें।
    *   *क्वेरी टाइमआउट?* `SQLTimeoutException` या Spring/Hibernate `QueryTimeout`। **Spring/Hibernate** टाइमआउट को **WAS DS** और **DB** टाइमआउट के साथ अलाइन करें; कॉन्फ्लिक्टिंग सेटिंग्स से बचें।
    *   *सॉकेट/रीड टाइमआउट?* नेटवर्क/ड्राइवर संदेश। ड्राइवर की `socketTimeout`/`loginTimeout`, DB कीपअलाइव्स, और फ़ायरवॉल चेक करें।

2.  **टाइमिंग्स को करिलेट करें**

    *   फेल होने वाले ड्यूरेशन की तुलना कॉन्फ़िगर थ्रेशोल्ड से करें (जैसे, "~30s पर फेल होता है" → कोई 30s सेटिंग ढूंढें: Spring क्वेरी टाइमआउट 30s? tx लाइफटाइम 30s? पूल वेट 30s?)।

3.  **पूलिंग हेल्थ चेक करें**

    *   PMI: क्या **waiters** > 0? क्या **in-use**, **max** के करीब है? लंबे समय तक चलने वाले होल्डर्स? **कनेक्शन लीक डिटेक्शन** एनेबल करने पर विचार करें (RRA ट्रेस दिखाता है कि कनेक्शन किसने लिया)।

4.  **DB विजिबिलिटी**

    *   DB पर कन्फर्म करें: क्या स्टेटमेंट अभी भी चल रहा था? क्या इसे कैंसल किया गया था? कोई लॉक वेट्स? अगर लॉक्स → लॉक टाइमआउट बनाम स्टेटमेंट टाइमआउट पर विचार करें।

# उपयोगी नॉब्स और गोटचाज (WAS + DB2 उदाहरण)

*   **Total transaction lifetime timeout** (सर्वर लेवल) लंबी क्वेरीज़ को किल कर देगा भले ही आपने कोई हायर Spring/Hibernate टाइमआउट सेट किया हो। इन्हें कंसिस्टेंट रखें।
*   **queryTimeoutInterruptProcessingMode** (DB2 के लिए DataSource कस्टम प्रॉपर्टी): कंट्रोल करती है कि DB2 को टाइमआउट वाली क्वेरी को कैसे इंटरप्ट करना चाहिए (कोऑपरेटिव/फोर्सफुल)। टाइमआउट के बाद फंसे थ्रेड्स से बचने में मदद करती है।
*   **Purge policy**: `EntirePool` फेटल SQL स्टेट्स (जैसे, DB रीस्टार्ट) से तेजी से रिकवर कर सकता है, लेकिन इसकी कीमत एक ब्लिप है।
*   **Aged/Unused timeout**: फ़ायरवॉल/NAT आइडल्स से बचने के लिए स्टेल कनेक्शन्स को रिटायर करें।
*   **Validation**: **validation by SQL** या **validation timeout** एनेबल करें ताकि डेड कनेक्शन उपयोग से पहले डिटेक्ट हो जाएं।
*   **थ्रेड पूल्स**: अगर WebContainer थ्रेड्स सैचुरेटेड हैं, तो *लक्षण टाइमआउट जैसे दिखते हैं*। सुनिश्चित करें कि WebContainer और Default थ्रेड पूल्स का आकार उचित है।

# मिनिमल Spring वायरिंग उदाहरण

**JNDI DataSource (XML)**

```xml
<jee:jndi-lookup id="dataSource" jndi-name="java:comp/env/jdbc/MyDS" expected-type="javax.sql.DataSource"/>
<bean id="txManager" class="org.springframework.transaction.jta.JtaTransactionManager"/>
<tx:annotation-driven transaction-manager="txManager"/>
```

**JdbcTemplate क्वेरी टाइमआउट (Java)**

```java
@Bean JdbcTemplate jdbcTemplate(DataSource ds) {
  JdbcTemplate jt = new JdbcTemplate(ds);
  jt.setQueryTimeout(60); // सेकंड्स
  return jt;
}
```

**Hibernate/JPA टाइमआउट**

```properties
javax.persistence.query.timeout=60000  # ms
hibernate.jdbc.timeout=60              # सेकंड्स
```

# जब आप एस्केलेट करते हैं तो क्या कैप्चर करें

*   एक्जैक्ट एक्सेप्शन टेक्स्ट + स्टैक ट्रेस।
*   टाइमस्टैम्प्स: रिक्वेस्ट स्टार्ट, tx बिगिन, क्वेरी स्टार्ट, एरर टाइम।
*   WAS DS पूल कॉन्फिग (स्क्रीनशॉट या वैल्यूज़), Transaction Service टाइमआउट।
*   PMI स्नैपशॉट (पूल वेटर्स, इन-यूज़, टाइमआउट काउंट्स)।
*   फेलियर टाइम पर सेशन/स्टेटमेंट का DB व्यू।
*   नेटवर्क टोपोलॉजी नोट्स (फ़ायरवॉल, प्रॉक्सी, आइडल टाइमर्स)।

अगर आप कोई स्पेसिफिक एक्सेप्शन स्निपेट (J2CA/WTRN/SQL स्टेट) पेस्ट करते हैं, तो मैं सटीक लेयर और एडजस्ट करने के लिए मैचिंग सेटिंग पहचान सकता हूं।