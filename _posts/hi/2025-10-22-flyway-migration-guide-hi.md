---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: फ्लाईवे डेटाबेस माइग्रेशन गाइड
translated: true
type: note
---

### Flyway का परिचय
Flyway डेटाबेस स्कीमा माइग्रेशन को वर्जन-नियंत्रित तरीके से प्रबंधित करने के लिए एक लोकप्रिय ओपन-सोर्स टूल है। यह आपको डेटाबेस में वृद्धिशील परिवर्तन (जैसे टेबल बनाना, कॉलम बदलना, या डेटा इन्सर्ट करना) दोहराए जाने योग्य और सुरक्षित तरीके से लागू करने की अनुमति देता है। Java एप्लिकेशन में, Flyway को इसके API के माध्यम से एकीकृत किया जा सकता है, अक्सर एप्लिकेशन स्टार्टअप पर चलाया जाता है ताकि यह सुनिश्चित किया जा सके कि आपका कोड डेटाबेस के साथ इंटरैक्ट करने से पहले डेटाबेस स्कीमा अप-टू-डेट है। यह JDBC (जैसे, PostgreSQL, MySQL, Oracle) के माध्यम से अधिकांश डेटाबेस के साथ काम करता है।

### चरण 1: Flyway डिपेंडेंसी जोड़ें
अपनी बिल्ड फाइल में Flyway जोड़ें। जब तक आपको एंटरप्राइज़ फीचर्स की आवश्यकता न हो, ओपन-सोर्स एडिशन का उपयोग करें।

**Maven (`pom.xml`)**:
```xml
<dependencies>
    <dependency>
        <groupId>org.flywaydb</groupId>
        <artifactId>flyway-core</artifactId>
        <version>11.14.1</version> <!-- नवीनतम वर्जन के लिए जाँच करें -->
    </dependency>
    <!-- अपने डेटाबेस के लिए JDBC ड्राइवर जोड़ें, उदाहरण के लिए, PostgreSQL के लिए -->
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
        <version>42.7.3</version>
    </dependency>
</dependencies>
```

**Gradle (`build.gradle`)**:
```groovy
dependencies {
    implementation 'org.flywaydb:flyway-core:11.14.1'
    // अपने डेटाबेस के लिए JDBC ड्राइवर जोड़ें
    implementation 'org.postgresql:postgresql:42.7.3'
}
```

आपको अपने टार्गेट डेटाबेस के लिए JDBC ड्राइवर की भी आवश्यकता होगी।

### चरण 2: Flyway कॉन्फ़िगर करें
Flyway कॉन्फ़िगरेशन के लिए एक फ्लुएंट API का उपयोग करता है। मुख्य सेटिंग्स में डेटाबेस कनेक्शन विवरण, माइग्रेशन स्क्रिप्ट्स के लिए लोकेशन, और वैकल्पिक कॉलबैक शामिल हैं।

अपने Java कोड में, एक `Flyway` इंस्टेंस बनाएँ:
```java
import org.flywaydb.core.Flyway;

public class DatabaseMigration {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb";
        String user = "username";
        String password = "password";

        Flyway flyway = Flyway.configure()
                .dataSource(url, user, password)
                .locations("classpath:db/migration")  // SQL स्क्रिप्ट्स के लिए फोल्डर (डिफ़ॉल्ट: db/migration)
                .load();
    }
}
```
- `locations`: आपकी माइग्रेशन फाइलों के स्थान को इंगित करता है (उदाहरण के लिए, क्लासपाथ के लिए `src/main/resources/db/migration`)।
- अन्य सामान्य कॉन्फ़िग: मौजूदा स्कीमा को बेसलाइन करने के लिए `.baselineOnMigrate(true)`, या हिस्ट्री टेबल को कस्टमाइज़ करने के लिए `.table("flyway_schema_history")`।

### चरण 3: माइग्रेशन स्क्रिप्ट्स लिखें
माइग्रेशन स्क्रिप्ट्स SQL फाइलें होती हैं जिन्हें कॉन्फ़िगर की गई लोकेशन (जैसे `src/main/resources/db/migration`) में रखा जाता है। Flyway उन्हें क्रम में लागू करता है।

#### नामकरण परंपराएँ
- **वर्जन माइग्रेशन** (एक-बार की स्कीमा परिवर्तनों के लिए): `V<version>__<description>.sql` (उदाहरण के लिए, `V1__Create_person_table.sql`, `V2__Add_age_column.sql`)।
  - वर्जन फॉर्मेट: सेगमेंट के लिए अंडरस्कोर का उपयोग करें (उदाहरण के लिए, `V1_1__Initial.sql`)।
- **रिपीटेबल माइग्रेशन** (चल रहे कार्यों जैसे व्यूज़ के लिए): `R__<description>.sql` (उदाहरण के लिए, `R__Update_view.sql`)। यदि ये बदल गए हों तो ये हर बार चलते हैं।
- फाइलें लेक्सिकोग्राफिकल क्रम में लागू की जाती हैं।

#### उदाहरण स्क्रिप्ट्स
इन फाइलों को `src/main/resources/db/migration` में बनाएँ।

**V1__Create_person_table.sql**:
```sql
CREATE TABLE person (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO person (id, name) VALUES (1, 'John Doe');
```

**V2__Add_age_column.sql**:
```sql
ALTER TABLE person ADD COLUMN age INT;
```

**R__Populate_names.sql** (रिपीटेबल):
```sql
UPDATE person SET name = CONCAT(name, ' (Updated)') WHERE id = 1;
```

Flyway लागू किए गए माइग्रेशन को एक `flyway_schema_history` टेबल में ट्रैक करता है।

जटिल लॉजिक के लिए जो SQL के लिए उपयुक्त नहीं है, Java-आधारित माइग्रेशन का उपयोग करें (`org.flywaydb.core.api.migration.java.JavaMigration` इम्प्लीमेंट करें)।

### चरण 4: माइग्रेशन प्रोग्रामेटिकली रन करें
लंबित माइग्रेशन लागू करने के लिए `migrate()` को कॉल करें। इसे अपने ऐप के स्टार्टअप में एकीकृत करें (उदाहरण के लिए, `main()` में या एक Spring `@PostConstruct` में)।

```java
import org.flywaydb.core.Flyway;
import org.flywaydb.core.api.FlywayException;

public class DatabaseMigration {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb";
        String user = "username";
        String password = "password";

        Flyway flyway = Flyway.configure()
                .dataSource(url, user, password)
                .locations("classpath:db/migration")
                .load();

        try {
            flyway.migrate();  // सभी लंबित माइग्रेशन लागू करता है
            System.out.println("Database migrated successfully!");
        } catch (FlywayException e) {
            System.err.println("Migration failed: " + e.getMessage());
            // त्रुटि को हैंडल करें (उदाहरण के लिए, बाहर निकलें या रोलबैक करें)
        }

        // अब अपने एप्लिकेशन का बाकी हिस्सा शुरू करें
    }
}
```

- `migrate()`: वर्जन माइग्रेशन को क्रम में लागू करता है, फिर रिपीटेबल्स को।
- अन्य कमांड: स्टेटस के लिए `flyway.info()`, समस्याओं को ठीक करने के लिए `flyway.repair()`, स्थिरता जाँचने के लिए `flyway.validate()`।
- स्कीमा संगतता सुनिश्चित करने के लिए किसी भी डेटाबेस ऑपरेशन से पहले इसे रन करें।

### बेस्ट प्रैक्टिसेज़
- माइग्रेशन को इडेम्पोटेंट रखें (दोबारा रन करने के लिए सुरक्षित)।
- प्रोडक्शन डेटा की एक कॉपी पर माइग्रेशन का टेस्ट करें।
- माइग्रेशन फाइलों के लिए वर्जन कंट्रोल का उपयोग करें।
- Spring Boot के लिए, `spring-boot-starter-jdbc` जोड़ें और ऑटो-कॉन्फ़िगरेशन के लिए `application.properties` में `spring.flyway.enabled=true` सेट करें।

### संदर्भ
- [Flyway API (Java) Documentation](https://documentation.red-gate.com/fd/api-java-277579358.html)
- [Flyway Migrations Documentation](https://documentation.red-gate.com/fd/migrations-271585107.html)
- [Flyway Getting Started](https://documentation.red-gate.com/fd/getting-started-with-flyway-184127223.html)