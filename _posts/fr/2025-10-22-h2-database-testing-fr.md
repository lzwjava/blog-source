---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Test avec la base de données H2 dans Spring Boot
translated: true
type: note
---

### Utilisation de H2 Database dans les tests JUnit avec Spring Boot

H2 est une base de données légère en mémoire, idéale pour les tests unitaires et d'intégration dans les applications Java, particulièrement avec Spring Boot. Elle permet d'exécuter les tests rapidement sans avoir besoin de configurer une base de données externe. Voici un guide étape par étape en supposant un projet Spring Boot avec JPA/Hibernate. Si vous n'utilisez pas Spring, vous pouvez utiliser H2 via JDBC standard (voir les notes à la fin).

#### Étape 1 : Ajouter la dépendance H2
Incluez la dépendance H2 dans votre `pom.xml` (Maven) ou `build.gradle` (Gradle). Définissez son scope sur `test` pour éviter son inclusion en production.

**Maven (`pom.xml`) :**
```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>test</scope>
</dependency>
```

**Gradle (`build.gradle`) :**
```gradle
testImplementation 'com.h2database:h2'
```

Cela récupère le JAR H2 uniquement pour l'exécution des tests.

#### Étape 2 : Configurer H2 dans les propriétés de test
Créez ou mettez à jour `src/test/resources/application.properties` (ou `application-test.yml`) pour pointer vers H2. Cela remplace les paramètres de la base de données de production.

**application.properties :**
```
# Configuration de la base de données H2
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# Console H2 (optionnelle, pour le débogage)
spring.h2.console.enabled=true

# Paramètres JPA/Hibernate
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.show-sql=true
```

- `mem:testdb` : Base de données en mémoire nommée "testdb".
- `create-drop` : Crée automatiquement les tables au démarrage et les supprime à l'arrêt.
- Activez la console H2 à l'adresse `http://localhost:8080/h2-console` pendant les tests pour inspection (utilisez l'URL JDBC : `jdbc:h2:mem:testdb`).

Si vous utilisez des profils, activez-les avec `@ActiveProfiles("test")` dans votre classe de test.

#### Étape 3 : Écrire un test JUnit
Utilisez `@SpringBootTest` pour un contexte complet ou `@DataJpaTest` pour des tests centrés sur le repository. Annotez avec `@Test` et utilisez JUnit 5 (`@ExtendWith(SpringExtension.class)`).

**Exemple : Tester un JPA Repository**
Supposons que vous ayez une `Entity` comme `User` et un `UserRepository` étendant `JpaRepository`.

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.ActiveProfiles;

import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest  // Charge uniquement les beans liés à JPA pour des tests plus rapides
@ActiveProfiles("test")  // Active le profil de test
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

- `@DataJpaTest` : Auto-configure H2 et annule les transactions après chaque test.
- Utilisez les assertions `AssertJ` ou `JUnit` pour la vérification.
- Pour les tests de couche service, utilisez `@SpringBootTest` et injectez les services/repositories.

Exécutez avec `mvn test` ou le lanceur de tests de votre IDE. Chaque test démarre avec une base de données vierge.

#### Étape 4 : Conseils avancés
- **Migration Flyway/Liquibase** : Si vous utilisez des migrations de schéma, ajoutez-les dans `src/test/resources` et H2 les appliquera.
- **Test réaliste** : H2 imite la plupart des dialectes SQL mais peut différer de la production (par exemple, PostgreSQL). Pour des correspondances plus proches, considérez Testcontainers avec un conteneur de base de données réelle.
- **Exclure la configuration de production** : Dans `pom.xml`, utilisez des profils pour exclure les pilotes de base de données réelle dans les tests :
  ```xml
  <profile>
      <id>test</id>
      <dependencies>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-data-jpa</artifactId>
              <exclusions>
                  <exclusion>
                      <groupId>mysql</groupId>  <!-- Ou votre base de données de production -->
                      <artifactId>mysql-connector-java</artifactId>
                  </exclusion>
              </exclusions>
          </dependency>
      </dependencies>
  </profile>
  ```
- **Dépannage** : Si les tests utilisent la base de données de production, assurez-vous que `spring.profiles.active=test` ou utilisez `@TestPropertySource`.

#### JUnit autonome (sans Spring)
Pour JDBC standard sans Spring :
1. Ajoutez la dépendance H2 (comme ci-dessus).
2. Dans votre test :
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
Cela crée une base de données en mémoire par test.

Pour plus de détails, consultez les références ci-dessous.

[Setting Up H2 for Testing in Spring Boot](https://medium.com/@paulkunda/setting-up-h2-for-testing-in-spring-boot-245d3a98e405)  
[Self-Contained Testing Using an In-Memory Database | Baeldung](https://www.baeldung.com/spring-jpa-test-in-memory-database)  
[Setting Up H2 for Testing in Spring Boot application](https://medium.com/@akshatakanaje08/setting-up-h2-for-testing-in-spring-boot-application-7f016220a475)  
[Test Spring Data Repositories with H2 in-memory database](https://www.geekyhacker.com/test-spring-data-repositories-with-h2-in-memory-database/)