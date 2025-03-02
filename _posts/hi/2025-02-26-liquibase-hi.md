---
audio: false
generated: true
lang: hi
layout: post
title: 'Liquibase: डेटाबेस स्कीमा प्रबंधन'
translated: true
---

यह एक व्यापक मार्गदर्शिका है **Liquibase** का उपयोग **Spring Boot** अनुप्रयोग में अपने डेटाबेस स्कीमा परिवर्तनों को प्रभावी ढंग से प्रबंधित करने के लिए:

---

### 1. Liquibase निर्भरता जोड़ें
शुरू करने के लिए, आपको अपने प्रोजेक्ट में Liquibase निर्भरता शामिल करनी होगी। अगर आप **Maven** का उपयोग कर रहे हैं, तो इसे अपने `pom.xml` में जोड़ें:

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

यह Liquibase कोर लाइब्रेरी को आपके प्रोजेक्ट में लाता है।

---

### 2. Liquibase को संरचना करें
Liquibase एक **चेंजलॉग फ़ाइल** का उपयोग करता है डेटाबेस स्कीमा परिवर्तनों को प्रबंधित करने के लिए। डिफ़ॉल्ट रूप से, Spring Boot एक फ़ाइल को खोजता है जिसका नाम `db/changelog/db.changelog-master.yaml`, `db/changelog/db.changelog-master.xml`, या `db/changelog/db.changelog-master.sql` है, क्लासपाथ में। आप इसे एक गुण को अपने `application.properties` (या `application.yml`) में जोड़कर अनुकूलित कर सकते हैं:

```properties
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

यह Spring Boot को बताता है कि आपकी चेंजलॉग फ़ाइल कहाँ मिलेगी।

---

### 3. एक चेंजलॉग फ़ाइल बनाएं
चेंजलॉग फ़ाइल आपने डेटाबेस में लागू करने के लिए परिवर्तनों को परिभाषित करती है। आप इसे XML, YAML, या SQL में लिख सकते हैं। यहाँ एक **XML चेंजलॉग** फ़ाइल का उदाहरण है जो `src/main/resources/db/changelog/db.changelog-master.xml` पर स्थित है:

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

इस उदाहरण में एक `users` टेबल बनाया गया है जिसमें तीन कॉलम हैं: `id`, `username`, और `email`. प्रत्येक `<changeSet>` एक परिवर्तन सेट को लागू करने के लिए है।

---

### 4. अपने Spring Boot अनुप्रयोग को चलाएं
जब आप अपने Spring Boot अनुप्रयोग को शुरू करते हैं, तो Liquibase स्वचालित रूप से:
- चेंजलॉग फ़ाइल को पढ़ता है।
- यह देखता है कि कौन से चेंजसेट पहले से लागू हो चुके हैं (एक टेबल में ट्रैक किया गया है जिसे `DATABASECHANGELOG` कहा जाता है).
- अपने डेटाबेस पर किसी भी नए चेंजसेट को लागू करता है।

किसी अतिरिक्त कोड की आवश्यकता नहीं है—Spring Boot की स्वचालित संरचना इस काम को आपके लिए संभालती है।

---

### 5. Liquibase को अनुकूलित करें (वैकल्पिक)
आप `application.properties` में गुणों का उपयोग करके Liquibase की व्यवहार को अनुकूलित कर सकते हैं। यहाँ कुछ आम विकल्प हैं:

```properties
spring.liquibase.enabled=true          # Liquibase को सक्षम या असक्षम करें
spring.liquibase.drop-first=false      # परिवर्तन लागू करने से पहले डेटाबेस को ड्रॉप करें (सावधानी से उपयोग करें)
spring.liquibase.contexts=dev,prod     # केवल विशिष्ट परिस्थितियों में चेंजसेट चलाएं
```

ये सेटिंग्स आपको Liquibase को अपने वातावरण या कार्यप्रणाली के अनुसार अनुकूलित करने की अनुमति देते हैं।

---

### 6. उन्नत विशेषताओं का लाभ उठाएं
Liquibase स्कीमा प्रबंधन को बढ़ाने के लिए शक्तिशाली विशेषताएँ प्रदान करता है:
- **परिस्थितियाँ और लेबल**: नियंत्रित करें कि कौन से चेंजसेट विशिष्ट वातावरणों में (जैसे `dev` vs. `prod`) चलें।
- **पूर्वशर्तें**: सुनिश्चित करें कि कुछ शर्तें (जैसे एक टेबल मौजूद है) एक चेंजसेट लागू करने से पहले पूरी हों।
- **रोलबैक**: अगर आवश्यक हो, तो एक चेंजसेट को वापस करने का तरीका परिभाषित करें।
- **पुनर्विन्यास**: जटिल डेटाबेस परिवर्तन (जैसे कॉलम नाम बदलना) के लिए बिल्ट-इन समर्थन का उपयोग करें।

उदाहरण के लिए, एक चेंजसेट में एक परिस्थिति जोड़ना:

```xml
<changeSet id="2" author="your-name" context="dev">
    <addColumn tableName="users">
        <column name="created_at" type="timestamp"/>
    </addColumn>
</changeSet>
```

यह चेंजसेट केवल `dev` परिस्थिति में चलता है।

---

### 7. एक इन-मेमोरी डेटाबेस के साथ परीक्षण करें
परीक्षण के लिए, Liquibase को एक इन-मेमोरी डेटाबेस जैसे H2 के साथ जोड़ें। H2 निर्भरता जोड़ें:

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

फिर अपने `application.properties` को परीक्षण के लिए संरचना करें:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

Liquibase आपके परिवर्तन को परीक्षण के दौरान इन-मेमोरी डेटाबेस में लागू करेगा।

---

### 8. अपने चेंजलॉग को संस्करण नियंत्रण में रखें
अपने चेंजलॉग फ़ाइलें को संस्करण नियंत्रण (जैसे Git) में अपने अनुप्रयोग कोड के साथ रखें। यह सुनिश्चित करता है कि आपका डेटाबेस स्कीमा आपके कोडबेस के साथ एक साथ विकसित होता है, जिससे डिप्लॉयमेंट और रोलबैक अधिक पूर्वानुमेय बन जाते हैं।

---

### सारांश
एक Spring Boot अनुप्रयोग में Liquibase का उपयोग करने के लिए:
1. Liquibase निर्भरता जोड़ें।
2. चेंजलॉग फ़ाइल स्थान को संरचना करें।
3. अपने डेटाबेस परिवर्तनों के साथ एक चेंजलॉग फ़ाइल बनाएं।
4. अपने अनुप्रयोग को चलाएं—Liquibase बाकी सब संभाल लेता है।

Liquibase एक मजबूत औजार है डेटाबेस स्कीमा परिवर्तनों को संरचित, संस्करण नियंत्रित तरीके से प्रबंधित करने के लिए, जो Spring Boot के साथ सिल्की-सम्‍बद्ध है।