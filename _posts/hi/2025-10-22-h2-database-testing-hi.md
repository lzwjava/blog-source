---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: स्प्रिंग बूट में एच२ डेटाबेस के साथ परीक्षण
translated: true
type: note
---

### स्प्रिंग बूट के साथ JUnit टेस्ट में H2 डेटाबेस का उपयोग

H2 एक लाइटवेट, इन-मेमोरी डेटाबेस है जो जावा एप्लिकेशन, विशेष रूप से स्प्रिंग बूट के साथ, यूनिट और इंटीग्रेशन टेस्टिंग के लिए आदर्श है। यह आपको बाहरी डेटाबेस सेटअप की आवश्यकता के बिना तेजी से टेस्ट चलाने की अनुमति देता है। नीचे एक चरण-दर-चरण मार्गदर्शिका दी गई है जो स्प्रिंग बूट प्रोजेक्ट के साथ JPA/Hibernate का उपयोग करने की मान्यता पर आधारित है। यदि आप स्प्रिंग का उपयोग नहीं कर रहे हैं, तो आप सादे JDBC के माध्यम से H2 का उपयोग कर सकते हैं (अंत में दिए गए नोट्स देखें)।

#### चरण 1: H2 डिपेंडेंसी जोड़ें
अपने `pom.xml` (Maven) या `build.gradle` (Gradle) में H2 डिपेंडेंसी शामिल करें। इसे `test` स्कोप में रखें ताकि यह प्रोडक्शन में शामिल न हो।

**Maven (`pom.xml`):**
```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>test</scope>
</dependency>
```

**Gradle (`build.gradle`):**
```gradle
testImplementation 'com.h2database:h2'
```

यह टेस्ट एक्जिक्यूशन के लिए केवल H2 JAR को इन्क्लूड करता है।

#### चरण 2: टेस्ट प्रॉपर्टीज में H2 कॉन्फ़िगर करें
H2 को पॉइंट करने के लिए `src/test/resources/application.properties` (या `application-test.yml`) बनाएं या अपडेट करें। यह प्रोडक्शन DB सेटिंग्स को ओवरराइड करता है।

**application.properties:**
```
# H2 डेटाबेस कॉन्फ़िगरेशन
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# H2 कंसोल (वैकल्पिक, डीबगिंग के लिए)
spring.h2.console.enabled=true

# JPA/Hibernate सेटिंग्स
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.show-sql=true
```

- `mem:testdb`: "testdb" नाम का इन-मेमोरी डेटाबेस।
- `create-drop`: स्टार्टअप पर टेबल्स ऑटो-क्रिएट करता है और शटडाउन पर ड्रॉप कर देता है।
- इंस्पेक्शन के लिए टेस्ट के दौरान H2 कंसोल को `http://localhost:8080/h2-console` पर एनेबल करें (JDBC URL: `jdbc:h2:mem:testdb` का उपयोग करें)।

यदि प्रोफाइल्स का उपयोग कर रहे हैं, तो अपनी टेस्ट क्लास में `@ActiveProfiles("test")` के साथ एक्टिवेट करें।

#### चरण 3: एक JUnit टेस्ट लिखें
पूर्ण कॉन्टेक्स्ट के लिए `@SpringBootTest` का उपयोग करें या रिपॉजिटरी-फोकस्ड टेस्ट के लिए `@DataJpaTest` का उपयोग करें। `@Test` के साथ एनोटेट करें और JUnit 5 (`@ExtendWith(SpringExtension.class)`) का उपयोग करें।

**उदाहरण: एक JPA रिपॉजिटरी को टेस्ट करना**
मान लें कि आपके पास `User` जैसी एक `Entity` और `JpaRepository` को एक्सटेंड करने वाला एक `UserRepository` है।

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.ActiveProfiles;

import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest  // केवल JPA-संबंधित बीन्स को लोड करता है, तेज टेस्ट के लिए
@ActiveProfiles("test")  // टेस्ट प्रोफाइल को एक्टिवेट करता है
public class UserRepositoryTest {

    @Autowired
    private UserRepository userRepository;

    @Test
    public void shouldSaveAndFindUser() {
        // दिया गया
        User user = new User("John Doe", "john@example.com");
        userRepository.save(user);

        // जब
        User foundUser = userRepository.findByEmail("john@example.com").orElse(null);

        // तब
        assertThat(foundUser).isNotNull();
        assertThat(foundUser.getName()).isEqualTo("John Doe");
    }
}
```

- `@DataJpaTest`: H2 को ऑटो-कॉन्फ़िगर करता है और प्रत्येक टेस्ट के बाद ट्रांजैक्शन रोल बैक करता है।
- वेरिफिकेशन के लिए `AssertJ` या `JUnit` असेर्शन का उपयोग करें।
- सर्विस-लेयर टेस्ट के लिए, `@SpringBootTest` का उपयोग करें और सर्विसेज/रिपॉजिटरीज को इंजेक्ट करें।

`mvn test` या अपने IDE के टेस्ट रनर के साथ रन करें। प्रत्येक टेस्ट एक फ्रेश DB के साथ शुरू होता है।

#### चरण 4: उन्नत टिप्स
- **Flyway/Liquibase माइग्रेशन**: यदि स्कीमा माइग्रेशन का उपयोग कर रहे हैं, तो उन्हें `src/test/resources` में जोड़ें और H2 उन्हें एप्लाई करेगा।
- **यथार्थवादी टेस्टिंग**: H2 अधिकांश SQL डायलेक्ट्स की नकल करता है लेकिन प्रोडक्शन (जैसे, PostgreSQL) से भिन्न हो सकता है। करीबी मिलान के लिए, वास्तविक DB कंटेनर के साथ Testcontainers पर विचार करें।
- **प्रोडक्शन कॉन्फ़िग को बाहर करें**: `pom.xml` में, टेस्ट में रियल DB ड्राइवरों को बाहर करने के लिए प्रोफाइल्स का उपयोग करें:
  ```xml
  <profile>
      <id>test</id>
      <dependencies>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-data-jpa</artifactId>
              <exclusions>
                  <exclusion>
                      <groupId>mysql</groupId>  <!-- या आपका prod DB -->
                      <artifactId>mysql-connector-java</artifactId>
                  </exclusion>
              </exclusions>
          </dependency>
      </dependencies>
  </profile>
  ```
- **समस्या निवारण**: यदि टेस्ट प्रोडक्शन DB का उपयोग करते हैं, तो सुनिश्चित करें कि `spring.profiles.active=test` है या `@TestPropertySource` का उपयोग करें।

#### स्टैंडअलोन JUnit (बिना स्प्रिंग के)
स्प्रिंग के बिना सादे JDBC के लिए:
1. H2 डिपेंडेंसी जोड़ें (जैसा ऊपर बताया गया है)।
2. अपने टेस्ट में:
```java
import org.h2.jdbcx.JdbcDataSource;
import org.junit.jupiter.api.Test;

public class StandaloneH2Test {
    @Test
    public void testH2Connection() throws Exception {
        JdbcDataSource ds = new JdbcDataSource();
        ds.setURL("jdbc:h2:mem:test;DB_CLOSE_DELAY=-1");
        ds.setUser("sa");
        ds.setPassword("");

        try (Connection conn = ds.getConnection();
             Statement stmt = conn.createStatement()) {
            stmt.execute("CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255))");
            stmt.execute("INSERT INTO users VALUES (1, 'Test User')");
            ResultSet rs = stmt.executeQuery("SELECT * FROM users");
            assertTrue(rs.next());
        }
    }
}
```
यह प्रति टेस्ट एक इन-मेमोरी DB बनाता है।

अधिक जानकारी के लिए, नीचे दिए गए संदर्भ देखें।

[Setting Up H2 for Testing in Spring Boot](https://medium.com/@paulkunda/setting-up-h2-for-testing-in-spring-boot-245d3a98e405)  
[Self-Contained Testing Using an In-Memory Database | Baeldung](https://www.baeldung.com/spring-jpa-test-in-memory-database)  
[Setting Up H2 for Testing in Spring Boot application](https://medium.com/@akshatakanaje08/setting-up-h2-for-testing-in-spring-boot-application-7f016220a475)  
[Test Spring Data Repositories with H2 in-memory database](https://www.geekyhacker.com/test-spring-data-repositories-with-h2-in-memory-database/)