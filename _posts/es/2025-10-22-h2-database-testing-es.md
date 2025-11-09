---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Pruebas con Base de Datos H2 en Spring Boot
translated: true
type: note
---

### Uso de H2 Database en Pruebas JUnit con Spring Boot

H2 es una base de datos ligera en memoria ideal para pruebas unitarias y de integración en aplicaciones Java, especialmente con Spring Boot. Permite ejecutar pruebas rápidamente sin necesidad de configurar una base de datos externa. A continuación se muestra una guía paso a paso que asume un proyecto Spring Boot con JPA/Hibernate. Si no estás usando Spring, puedes usar H2 mediante JDBC simple (ver notas al final).

#### Paso 1: Agregar la Dependencia de H2
Incluye la dependencia de H2 en tu `pom.xml` (Maven) o `build.gradle` (Gradle). Define su alcance como `test` para evitar su inclusión en producción.

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

Esto descarga el JAR de H2 solo para la ejecución de pruebas.

#### Paso 2: Configurar H2 en las Propiedades de Prueba
Crea o actualiza `src/test/resources/application.properties` (o `application-test.yml`) para apuntar a H2. Esto sobrescribe la configuración de la base de datos de producción.

**application.properties:**
```
# Configuración de H2 Database
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# Consola H2 (opcional, para depuración)
spring.h2.console.enabled=true

# Configuración JPA/Hibernate
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.show-sql=true
```

- `mem:testdb`: Base de datos en memoria llamada "testdb".
- `create-drop`: Crea las tablas automáticamente al iniciar y las elimina al finalizar.
- Habilita la consola H2 en `http://localhost:8080/h2-console` durante las pruebas para inspección (usa JDBC URL: `jdbc:h2:mem:testdb`).

Si usas perfiles, actívalos con `@ActiveProfiles("test")` en tu clase de prueba.

#### Paso 3: Escribir una Prueba JUnit
Usa `@SpringBootTest` para un contexto completo o `@DataJpaTest` para pruebas centradas en repositorios. Anota con `@Test` y usa JUnit 5 (`@ExtendWith(SpringExtension.class)`).

**Ejemplo: Probando un JPA Repository**
Asume que tienes una `Entity` como `User` y un `UserRepository` que extiende `JpaRepository`.

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.ActiveProfiles;

import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest  // Carga solo los beans relacionados con JPA para pruebas más rápidas
@ActiveProfiles("test")  // Activa el perfil de prueba
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

- `@DataJpaTest`: Auto-configura H2 y revierte las transacciones después de cada prueba.
- Usa aserciones de `AssertJ` o `JUnit` para la verificación.
- Para pruebas a nivel de servicio, usa `@SpringBootTest` e inyecta los servicios/repositorios.

Ejecuta con `mvn test` o el ejecutor de pruebas de tu IDE. Cada prueba comienza con una base de datos nueva.

#### Paso 4: Consejos Avanzados
- **Migración con Flyway/Liquibase**: Si usas migraciones de esquema, agrégalas a `src/test/resources` y H2 las aplicará.
- **Pruebas Realistas**: H2 imita la mayoría de los dialectos SQL pero puede diferir de la base de datos de producción (por ejemplo, PostgreSQL). Para mayor similitud, considera usar Testcontainers con un contenedor de base de datos real.
- **Excluir Configuración de Producción**: En `pom.xml`, usa perfiles para excluir los controladores de la base de datos real en las pruebas:
  ```xml
  <profile>
      <id>test</id>
      <dependencies>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-data-jpa</artifactId>
              <exclusions>
                  <exclusion>
                      <groupId>mysql</groupId>  <!-- O tu DB de prod -->
                      <artifactId>mysql-connector-java</artifactId>
                  </exclusion>
              </exclusions>
          </dependency>
      </dependencies>
  </profile>
  ```
- **Solución de Problemas**: Si las pruebas usan la base de datos de producción, asegúrate de que `spring.profiles.active=test` o usa `@TestPropertySource`.

#### JUnit Independiente (Sin Spring)
Para JDBC simple sin Spring:
1. Agrega la dependencia de H2 (como arriba).
2. En tu prueba:
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
Esto crea una base de datos en memoria por prueba.

Para más detalles, consulta las referencias a continuación.

[Setting Up H2 for Testing in Spring Boot](https://medium.com/@paulkunda/setting-up-h2-for-testing-in-spring-boot-245d3a98e405)  
[Self-Contained Testing Using an In-Memory Database | Baeldung](https://www.baeldung.com/spring-jpa-test-in-memory-database)  
[Setting Up H2 for Testing in Spring Boot application](https://medium.com/@akshatakanaje08/setting-up-h2-for-testing-in-spring-boot-application-7f016220a475)  
[Test Spring Data Repositories with H2 in-memory database](https://www.geekyhacker.com/test-spring-data-repositories-with-h2-in-memory-database/)