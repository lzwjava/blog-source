---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: लिक्विबेस को स्प्रिंग बूट के साथ एकीकृत करना
translated: true
type: note
---

## Liquibase को Spring Boot के साथ एकीकृत करना

Liquibase डेटाबेस स्कीमा परिवर्तनों (माइग्रेशन) को वर्जन-नियंत्रित तरीके से प्रबंधित करने के लिए एक लोकप्रिय ओपन-सोर्स टूल है। Spring Boot, Liquibase के लिए उत्कृष्ट ऑटो-कॉन्फ़िगरेशन सपोर्ट प्रदान करता है, जिससे इसे एकीकृत करना आसान हो जाता है। यह गाइड मानती है कि आप Spring Boot 3.x (2025 तक नवीनतम) के साथ Maven का उपयोग कर रहे हैं, लेकिन अवधारणाएँ Gradle पर भी लागू होती हैं। हम बुनियादी बातों को चरण दर चरण कवर करेंगे।

### आवश्यक शर्तें
- एक Spring Boot प्रोजेक्ट सेट अप (उदाहरण के लिए, Spring Initializr के माध्यम से)।
- एक डेटाबेस (उदाहरण के लिए, टेस्टिंग के लिए H2, प्रोडक्शन के लिए PostgreSQL/MySQL) जो `application.properties` में कॉन्फ़िगर किया गया हो।

### चरण 1: Liquibase डिपेंडेंसी जोड़ें
अपने `pom.xml` में Liquibase Spring Boot स्टार्टर शामिल करें। यह Liquibase को आसानी से एकीकृत करता है।

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId> <!-- डेटाबेस कनेक्टिविटी के लिए -->
</dependency>
```

Gradle के लिए, `build.gradle` में जोड़ें:
```groovy
implementation 'org.liquibase:liquibase-core'
implementation 'org.springframework.boot:spring-boot-starter-jdbc'
```

डिपेंडेंसी प्राप्त करने के लिए `mvn clean install` (या `./gradlew build`) चलाएँ।

### चरण 2: Liquibase कॉन्फ़िगर करें
यदि आप चेंजलॉग फ़ाइलों को डिफ़ॉल्ट लोकेशन में रखते हैं तो Spring Boot स्वचालित रूप से Liquibase का पता लगा लेता है। `application.properties` (या `.yml` समकक्ष) के माध्यम से कस्टमाइज़ करें।

उदाहरण `application.properties`:
```properties
# डेटाबेस सेटअप (अपने डीबी के लिए एडजस्ट करें)
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driver-class-name=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# Liquibase कॉन्फ़िगरेशन
spring.liquibase.change-log=classpath:db/changelog/db.changelog-master.xml
spring.liquibase.enabled=true  # डिफ़ॉल्ट true है
spring.liquibase.drop-first=false  # डेव के लिए स्टार्टअप पर स्कीमा ड्रॉप करने के लिए true सेट करें
```

- `change-log`: आपकी मास्टर चेंजलॉग फ़ाइल का पथ (डिफ़ॉल्ट: `db/changelog/db.changelog-master.xml`)।
- `spring.liquibase.enabled` के साथ सक्षम/अक्षम करें।
- कॉन्टेक्स्ट/प्रोफाइल के लिए, विशिष्ट परिवर्तन चलाने के लिए `spring.liquibase.contexts=dev` का उपयोग करें।

### चरण 3: चेंजलॉग फ़ाइलें बनाएँ
Liquibase स्कीमा परिवर्तनों को परिभाषित करने के लिए "चेंजलॉग्स" का उपयोग करता है। `src/main/resources` के अंतर्गत एक डायरेक्टरी स्ट्रक्चर बनाएँ:
```
src/main/resources/
└── db/
    └── changelog/
        ├── db.changelog-master.xml  # मास्टर फ़ाइल जो अन्य को शामिल करती है
        └── changes/
            ├── 001-create-users-table.xml  # व्यक्तिगत परिवर्तन
            └── 002-add-email-column.xml
```

#### मास्टर चेंजलॉग (`db.changelog-master.xml`)
यह अन्य चेंजलॉग्स को शामिल करती है:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.24.xsd">

    <include file="changes/001-create-users-table.xml"/>
    <include file="changes/002-add-email-column.xml"/>
</databaseChangeLog>
```

#### नमूना परिवर्तन (`001-create-users-table.xml`)
एक टेबल क्रिएशन को परिभाषित करें:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                                       http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.24.xsd">

    <changeSet id="001" author="yourname">
        <createTable tableName="users">
            <column name="id" type="bigint">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="name" type="varchar(255)">
                <constraints nullable="false"/>
            </column>
        </createTable>
    </changeSet>
</databaseChangeLog>
```

- चेंजलॉग्स के लिए XML, YAML, JSON, या SQL फॉर्मेट का उपयोग करें।
- प्रत्येक `<changeSet>` एक माइग्रेशन है जिसमें एक ID होती है (ट्रैकिंग के लिए)।
- ऐप को स्टार्ट करने के लिए `java -jar target/your-app.jar` चलाएँ—Liquibase बूटस्ट्रैप पर परिवर्तनों को स्वचालित रूप से लागू करता है।

### चरण 4: चलाना और टेस्टिंग करना
- **स्टार्टअप पर**: Spring Boot आपके ऐप के पूरी तरह से शुरू होने से पहले Liquibase को चलाता है।
- **रोलबैक**: टेस्टिंग के लिए `spring.liquibase.rollback-file` या CLI का उपयोग करें।
- **CLI एकीकरण**: मैन्युअल रन के लिए, Liquibase Maven प्लगइन जोड़ें:
  ```xml
  <plugin>
      <groupId>org.liquibase</groupId>
      <artifactId>liquibase-maven-plugin</artifactId>
      <version>4.24.0</version>
      <configuration>
          <changeLogFile>src/main/resources/db/changelog/db.changelog-master.xml</changeLogFile>
          <url>jdbc:h2:mem:testdb</url>
          <username>sa</username>
          <password></password>
      </configuration>
  </plugin>
  ```
  फिर `mvn liquibase:update` चलाएँ।

- **वैलिडेशन**: चेंजलॉग्स की जाँच करने के लिए `spring.liquibase.validate-on-migrate=true` सक्षम करें।

### सामान्य सुझाव
- **प्रोफाइल**: आवश्यकता होने पर बीन्स पर `@Profile("dev")` का उपयोग करें, लेकिन Liquibase फ़िल्टर किए जाने तक वैश्विक रूप से चलता है।
- **प्रीकंडीशन**: डीबी स्टेट की जाँच करने के लिए चेंजसेट में `<preConditions>` जोड़ें।
- **SQL फॉर्मेट**: रॉ SQL के लिए, `.sql` फ़ाइलें बनाएँ और उन्हें शामिल करें: `<sqlFile path="changes/create-users.sql" relativeToChangelogFile="true"/>`।
- **ट्रबलशूटिंग**: त्रुटियों के लिए लॉग्स जाँचें (उदाहरण के लिए, `liquibase` प्रीफिक्स वाले)। सुनिश्चित करें कि डीबी URL सही है।
- **प्रोडक्शन**: यदि आप पसंद करते हैं तो Flyway का उपयोग करें, लेकिन Liquibase जटिल परिवर्तनों और मल्टी-डीबी सपोर्ट में बेहतर है।

टैग किए गए रोलबैक या कस्टम एक्सटेंशन जैसी उन्नत सुविधाओं के लिए, डॉक्स देखें।

### संदर्भ
- [Spring Boot Liquibase Auto-Configuration](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#io.liquibase)
- [Liquibase Official Documentation](https://docs.liquibase.com/start/home.html)
- [Baeldung Spring Boot + Liquibase Tutorial](https://www.baeldung.com/liquibase-refactor-schema-of-jpa-entity-in-spring-boot)