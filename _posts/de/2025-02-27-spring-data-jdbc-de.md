---
audio: false
generated: true
lang: de
layout: post
title: Spring Data JDBC
translated: true
type: note
---

Spring Data JDBC ist eine leistungsstarke Bibliothek, die Datenbankinteraktionen in einer Spring-Anwendung vereinfacht, indem sie einen leichtgewichtigen, annotierungsgesteuerten Ansatz für die Arbeit mit relationalen Datenbanken bietet. Es ist weniger vorgeprägt als Spring Data JPA und konzentriert sich auf eine einfachere, explizitere Art der Abbildung von Objekten auf Datenbanktabellen. Im Folgenden werde ich Sie durch die Grundlagen der Verwendung führen.

### 1. **Richten Sie Ihr Projekt ein**
Um zu beginnen, müssen Sie Spring Data JDBC in Ihr Projekt einbinden. Wenn Sie Maven verwenden, fügen Sie die folgende Abhängigkeit zu Ihrer `pom.xml` hinzu:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jdbc</artifactId>
</dependency>
```

Sie benötigen außerdem einen JDBC-Treiber für Ihre Datenbank (z.B. H2, MySQL, PostgreSQL). Zum Beispiel für H2:

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

Wenn Sie Gradle verwenden, wären die Entsprechungen:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-data-jdbc'
runtimeOnly 'com.h2database:h2'
```

### 2. **Konfigurieren Sie Ihre Datenbank**
Konfigurieren Sie die Datenbankverbindung in Ihrer `application.properties` oder `application.yml`. Für eine H2-In-Memory-Datenbank könnte das so aussehen:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.h2.console.enabled=true
```

Für eine echte Datenbank wie PostgreSQL passen Sie die URL, den Benutzernamen und das Passwort entsprechend an.

### 3. **Definieren Sie Ihr Domänenmodell**
Erstellen Sie eine einfache Entitätsklasse, um eine Tabelle in Ihrer Datenbank darzustellen. Spring Data JDBC verwendet Konventionen, bei denen der Klassenname auf den Tabellennamen abgebildet wird (standardmäßig in Kleinbuchstaben) und Felder auf Spalten.

```java
import org.springframework.data.annotation.Id;

public class Person {
    @Id
    private Long id;
    private String firstName;
    private String lastName;

    // Standardkonstruktor (von Spring Data JDBC benötigt)
    public Person() {}

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // Getter und Setter
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getFirstName() { return firstName; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public String getLastName() { return lastName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
}
```

- `@Id` kennzeichnet den Primärschlüssel.
- Spring Data JDBC erwartet einen parameterlosen Konstruktor.
- Die Tabelle wird standardmäßig `person` genannt, sofern nicht überschrieben.

### 4. **Erstellen Sie ein Repository**
Definieren Sie ein Interface, das `CrudRepository` erweitert, um grundlegende CRUD-Operationen zu handhaben:

```java
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, Long> {
}
```

Das war's! Sie müssen es nicht implementieren – Spring Data JDBC generiert die Implementierung zur Laufzeit.

### 5. **Verwenden Sie das Repository**
Injecten Sie das Repository in einen Service oder Controller und verwenden Sie es:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class PersonService {
    private final PersonRepository repository;

    @Autowired
    public PersonService(PersonRepository repository) {
        this.repository = repository;
    }

    public void savePerson() {
        Person person = new Person("John", "Doe");
        repository.save(person);
        System.out.println("Saved person with ID: " + person.getId());
    }

    public void listPeople() {
        Iterable<Person> people = repository.findAll();
        people.forEach(p -> System.out.println(p.getFirstName() + " " + p.getLastName()));
    }
}
```

### 6. **Starten Sie Ihre Anwendung**
Wenn Sie Spring Boot verwenden, erstellen Sie eine Hauptklasse mit `@SpringBootApplication` und führen Sie sie aus:

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

Spring Boot konfiguriert die Datenquelle und Spring Data JDBC automatisch.

### 7. **Optional: Benutzerdefinierte Abfragen**
Wenn Sie benutzerdefinierte Abfragen benötigen, können Sie Ihrem Repository Methoden mit `@Query` hinzufügen:

```java
import org.springframework.data.jdbc.repository.query.Query;
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, Long> {
    @Query("SELECT * FROM person WHERE first_name = :name")
    List<Person> findByFirstName(String name);
}
```

### Wichtige Punkte zu beachten
- **Kein Lazy Loading:** Im Gegensatz zu JPA unterstützt Spring Data JDBC kein Lazy Loading. Beziehungen (z.B. One-to-Many) müssen explizit mit Aggregate Roots modelliert werden.
- **Aggregate Root:** Jede Entität ist Teil eines Aggregats, und nur die Wurzel wird direkt gespeichert oder abgerufen.
- **Schema-Erstellung:** Spring Data JDBC erstellt Tabellen nicht automatisch. Sie müssen das Schema bereitstellen (z.B. über `schema.sql` in `src/main/resources`):

```sql
CREATE TABLE person (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);
```

### Beispielhafter Workflow
1. Starten Sie Ihre App.
2. Speichern Sie ein `Person`-Objekt mit `repository.save()`.
3. Rufen Sie es mit `repository.findById()` oder `findAll()` ab.

Das sind die Grundlagen! Wenn Sie tiefer in Beziehungen, benutzerdefinierte Abbildungen oder etwas Spezifisches eintauchen möchten, lassen Sie mich wissen, was Sie anstreben, und ich passe die Erklärung entsprechend an. Wie funktioniert das soweit für Sie?