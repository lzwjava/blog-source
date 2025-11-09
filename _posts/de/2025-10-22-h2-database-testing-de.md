---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Testen mit H2-Datenbank in Spring Boot
translated: true
type: note
---

### Verwendung der H2-Datenbank in JUnit-Tests mit Spring Boot

H2 ist eine schlanke In-Memory-Datenbank, die sich ideal für Unit- und Integration-Tests in Java-Anwendungen, insbesondere mit Spring Boot, eignet. Sie ermöglicht das schnelle Ausführen von Tests, ohne dass eine externe Datenbank eingerichtet werden muss. Nachfolgend finden Sie eine Schritt-für-Schritt-Anleitung, die von einem Spring-Boot-Projekt mit JPA/Hibernate ausgeht. Falls Sie Spring nicht verwenden, können Sie H2 auch über plain JDBC nutzen (siehe Hinweise am Ende).

#### Schritt 1: H2-Abhängigkeit hinzufügen
Fügen Sie die H2-Abhängigkeit in Ihre `pom.xml` (Maven) oder `build.gradle` (Gradle) ein. Weisen Sie ihr den Scope `test` zu, um eine Einbindung in der Produktivumgebung zu vermeiden.

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

Dies lädt das H2-JAR nur für die Testausführung.

#### Schritt 2: H2 in den Test-Properties konfigurieren
Erstellen oder aktualisieren Sie `src/test/resources/application.properties` (oder `application-test.yml`), um auf H2 zu verweisen. Dies überschreibt die Produktiv-DB-Einstellungen.

**application.properties:**
```
# H2-Datenbankkonfiguration
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# H2-Konsole (optional, für Debugging)
spring.h2.console.enabled=true

# JPA/Hibernate-Einstellungen
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.show-sql=true
```

- `mem:testdb`: In-Memory-Datenbank mit dem Namen "testdb".
- `create-drop`: Erstellt Tabellen beim Start automatisch und löscht sie beim Herunterfahren.
- Aktivieren Sie die H2-Konsole unter `http://localhost:8080/h2-console` während der Tests zur Inspektion (verwenden Sie die JDBC-URL: `jdbc:h2:mem:testdb`).

Falls Sie Profile verwenden, aktivieren Sie diese mit `@ActiveProfiles("test")` in Ihrer Testklasse.

#### Schritt 3: Einen JUnit-Test schreiben
Verwenden Sie `@SpringBootTest` für den vollständigen Context oder `@DataJpaTest` für Repository-fokussierte Tests. Kommentieren Sie mit `@Test` und verwenden Sie JUnit 5 (`@ExtendWith(SpringExtension.class)`).

**Beispiel: Testen eines JPA-Repositorys**
Angenommen, Sie haben eine `Entity` wie `User` und ein `UserRepository`, das `JpaRepository` erweitert.

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.ActiveProfiles;

import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest  // Lädt nur JPA-bezogene Beans für schnellere Tests
@ActiveProfiles("test")  // Aktiviert das Test-Profil
public class UserRepositoryTest {

    @Autowired
    private UserRepository userRepository;

    @Test
    public void shouldSaveAndFindUser() {
        // Given
        User user = new User("John Doe", "john@example.com");
        userRepository.save(user);

        // When
        User foundUser = userRepository.findByEmail("john@example.com").orElse(null);

        // Then
        assertThat(foundUser).isNotNull();
        assertThat(foundUser.getName()).isEqualTo("John Doe");
    }
}
```

- `@DataJpaTest`: Konfiguriert H2 automatisch und macht Transaktionen nach jedem Test rückgängig.
- Verwenden Sie `AssertJ` oder `JUnit` Assertions zur Verifikation.
- Für Service-Layer-Tests verwenden Sie `@SpringBootTest` und injizieren Sie Services/Repositories.

Führen Sie die Tests mit `mvn test` oder dem Test-Runner Ihrer IDE aus. Jeder Test startet mit einer frischen DB.

#### Schritt 4: Erweiterte Tipps
- **Flyway/Liquibase Migration**: Falls Sie Schema-Migrationen verwenden, fügen Sie diese zu `src/test/resources` hinzu und H2 wird sie anwenden.
- **Realistischeres Testen**: H2 ahmt die meisten SQL-Dialekte nach, kann sich aber von der Produktivumgebung (z.B. PostgreSQL) unterscheiden. Für genauere Übereinstimmungen sollten Sie Testcontainers mit einem echten DB-Container in Betracht ziehen.
- **Produktionskonfiguration ausschließen**: In `pom.xml` können Sie Profile verwenden, um echte DB-Treiber in Tests auszuschließen:
  ```xml
  <profile>
      <id>test</id>
      <dependencies>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-data-jpa</artifactId>
              <exclusions>
                  <exclusion>
                      <groupId>mysql</groupId>  <!-- Oder Ihre Prod-DB -->
                      <artifactId>mysql-connector-java</artifactId>
                  </exclusion>
              </exclusions>
          </dependency>
      </dependencies>
  </profile>
  ```
- **Fehlerbehebung**: Falls Tests die Produktions-DB verwenden, stellen Sie sicher, dass `spring.profiles.active=test` gesetzt ist oder verwenden Sie `@TestPropertySource`.

#### Eigenständiges JUnit (Ohne Spring)
Für plain JDBC ohne Spring:
1. Fügen Sie die H2-Abhängigkeit hinzu (wie oben).
2. In Ihrem Test:
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
Dies erzeugt eine In-Memory-DB pro Test.

Weitere Details finden Sie in den folgenden Referenzen.

[Setting Up H2 for Testing in Spring Boot](https://medium.com/@paulkunda/setting-up-h2-for-testing-in-spring-boot-245d3a98e405)  
[Self-Contained Testing Using an In-Memory Database | Baeldung](https://www.baeldung.com/spring-jpa-test-in-memory-database)  
[Setting Up H2 for Testing in Spring Boot application](https://medium.com/@akshatakanaje08/setting-up-h2-for-testing-in-spring-boot-application-7f016220a475)  
[Test Spring Data Repositories with H2 in-memory database](https://www.geekyhacker.com/test-spring-data-repositories-with-h2-in-memory-database/)