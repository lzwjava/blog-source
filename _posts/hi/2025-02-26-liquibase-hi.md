---
audio: false
generated: true
lang: hi
layout: post
title: 'लिक्विबेस: डेटाबेस स्कीम प्रबंधन'
translated: true
type: note
---

यहाँ **Liquibase का उपयोग कैसे करें** पर एक व्यापक गाइड है, जो आपके Spring Boot एप्लिकेशन में डेटाबेस स्कीमा परिवर्तनों को प्रभावी ढंग से प्रबंधित करने में मदद करेगी:

---

### 1. Liquibase डिपेंडेंसी जोड़ें
शुरुआत करने के लिए, आपको अपने प्रोजेक्ट में Liquibase डिपेंडेंसी शामिल करनी होगी। यदि आप **Maven** का उपयोग कर रहे हैं, तो इसे अपने `pom.xml` में जोड़ें:

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
```

**Gradle** के लिए, इसे अपने `build.gradle` में जोड़ें:

```groovy
implementation 'org.liquibase:liquibase-core'
```

यह आपके प्रोजेक्ट में Liquibase core लाइब्रेरी ले आएगा।

---

### 2. Liquibase कॉन्फ़िगर करें
Liquibase डेटाबेस स्कीमा परिवर्तनों को प्रबंधित करने के लिए एक **चेंजलॉग फ़ाइल** का उपयोग करता है। डिफ़ॉल्ट रूप से, Spring Boot क्लासपाथ में `db/changelog/db.changelog-master.yaml`, `db/changelog/db.changelog-master.xml`, या `db/changelog/db.changelog-master.sql` नाम की फ़ाइल ढूंढता है। आप अपने `application.properties` (या `application.yml`) में एक प्रॉपर्टी जोड़कर इस लोकेशन को कस्टमाइज़ कर सकते हैं:

```properties
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

यह Spring Boot को बताता है कि आपकी चेंजलॉग फ़ाइल कहाँ मिलेगी।

---

### 3. एक चेंजलॉग फ़ाइल बनाएँ
चेंजलॉग फ़ाइल उन परिवर्तनों को परिभाषित करती है जिन्हें आप अपने डेटाबेस पर लागू करना चाहते हैं। आप इसे XML, YAML, या SQL जैसे फॉर्मेट में लिख सकते हैं। यहाँ `src/main/resources/db/changelog/db.changelog-master.xml` पर स्थित एक **XML चेंजलॉग** फ़ाइल का उदाहरण दिया गया है:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.8.xsd">

    <changeSet id="1" author="your-name">
        <createTable tableName="users">
            <column name="id" type="int">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="username" type="varchar(255)"/>
            <column name="email" type="varchar(255)"/>
        </createTable>
    </changeSet>

</databaseChangeLog>
```

यह उदाहरण तीन कॉलम (`id`, `username`, और `email`) के साथ एक `users` टेबल बनाता है। प्रत्येक `<changeSet>` लागू करने के लिए परिवर्तनों के एक सेट का प्रतिनिधित्व करता है।

---

### 4. अपना Spring Boot एप्लिकेशन रन करें
जब आप अपना Spring Boot एप्लिकेशन शुरू करते हैं, तो Liquibase स्वचालित रूप से:
- चेंजलॉग फ़ाइल को पढ़ता है।
- जांचता है कि कौन से चेंजसेट पहले ही लागू हो चुके हैं (एक `DATABASECHANGELOG` नामक टेबल में ट्रैक किए गए)।
- आपके डेटाबेस पर किसी भी नए चेंजसेट को निष्पादित करता है।

किसी अतिरिक्त कोड की आवश्यकता नहीं है—Spring Boot की ऑटो-कॉन्फ़िगरेशन यह आपके लिए संभाल लेती है।

---

### 5. Liquibase को कस्टमाइज़ करें (वैकल्पिक)
आप `application.properties` में प्रॉपर्टीज़ का उपयोग करके Liquibase के व्यवहार को ट्वीक कर सकते हैं। यहाँ कुछ सामान्य विकल्प दिए गए हैं:

```properties
spring.liquibase.enabled=true          # Liquibase को सक्षम या अक्षम करें
spring.liquibase.drop-first=false      # परिवर्तन लागू करने से पहले डेटाबेस ड्रॉप करें (सावधानी से उपयोग करें)
spring.liquibase.contexts=dev,prod     # विशिष्ट संदर्भों में ही चेंजसेट चलाएं
```

ये सेटिंग्स आपको Liquibase को अपने वातावरण या वर्कफ़्लो के अनुकूल बनाने की अनुमति देती हैं।

---

### 6. उन्नत सुविधाओं का लाभ उठाएं
Liquibase स्कीमा प्रबंधन को बेहतर बनाने के लिए शक्तिशाली सुविधाएँ प्रदान करता है:
- **संदर्भ और लेबल**: नियंत्रित करें कि कौन से चेंजसेट विशिष्ट वातावरण (जैसे, `dev` बनाम `prod`) में चलें।
- **पूर्वशर्त**: सुनिश्चित करें कि चेंजसेट लागू करने से पहले कुछ शर्तें (जैसे, कोई टेबल मौजूद हो) पूरी होती हैं।
- **रोलबैक**: परिभाषित करें कि यदि आवश्यक हो तो किसी चेंजसेट को पूर्ववत कैसे करें।
- **रिफैक्टरिंग**: जटिल डेटाबेस परिवर्तनों (जैसे, कॉलम का नाम बदलना) के लिए अंतर्निहित सपोर्ट का उपयोग करें।

उदाहरण के लिए, किसी चेंजसेट में एक संदर्भ जोड़ना:

```xml
<changeSet id="2" author="your-name" context="dev">
    <addColumn tableName="users">
        <column name="created_at" type="timestamp"/>
    </addColumn>
</changeSet>
```

यह चेंजसेट केवल `dev` संदर्भ में चलेगा।

---

### 7. इन-मेमोरी डेटाबेस के साथ टेस्ट करें
टेस्टिंग के लिए, Liquibase को H2 जैसे इन-मेमोरी डेटाबेस के साथ जोड़ें। H2 डिपेंडेंसी जोड़ें:

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

फिर टेस्टिंग के लिए अपनी `application.properties` कॉन्फ़िगर करें:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

टेस्ट के दौरान Liquibase आपके परिवर्तनों को इन-मेमोरी डेटाबेस पर लागू कर देगा।

---

### 8. अपनी चेंजलॉग को वर्जन कंट्रोल में रखें
अपनी चेंजलॉग फ़ाइलों को अपने एप्लिकेशन कोड के साथ वर्जन कंट्रोल (जैसे, Git) में स्टोर करें। यह सुनिश्चित करता है कि आपकी डेटाबेस स्कीमा आपके कोडबेस के साथ तालमेल बिठाकर विकसित हो, जिससे डिप्लॉयमेंट और रोलबैक अधिक अनुमानित हो जाते हैं।

---

### सारांश
Spring Boot एप्लिकेशन में Liquibase का उपयोग करने के लिए:
1. Liquibase डिपेंडेंसी जोड़ें।
2. चेंजलॉग फ़ाइल लोकेशन कॉन्फ़िगर करें।
3. अपने डेटाबेस परिवर्तनों के साथ एक चेंजलॉग फ़ाइल बनाएँ।
4. अपना एप्लिकेशन रन करें—बाकी काम Liquibase संभाल लेता है।

Liquibase एक मजबूत टूल है जो डेटाबेस स्कीमा परिवर्तनों को एक संरचित, वर्जन-नियंत्रित तरीके से प्रबंधित करने के लिए है, जो Spring Boot के साथ सहजता से एकीकृत होता है।