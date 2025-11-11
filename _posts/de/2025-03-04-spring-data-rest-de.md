---
audio: false
generated: true
lang: de
layout: post
title: Spring Data REST Modul
translated: true
type: note
---

Um **spring-data-rest-core** zu verwenden, können Sie das Spring Data REST-Modul nutzen, um Ihre Spring Data-Repositories als RESTful-Endpoints in Ihrer Anwendung verfügbar zu machen. Nachfolgend finden Sie eine vollständige, schrittweise Anleitung für den Einstieg:

---

### 1. Fügen Sie die Spring Data REST-Abhängigkeit hinzu
Um Spring Data REST zu verwenden, müssen Sie dessen Abhängigkeit in Ihr Projekt aufnehmen. Wenn Sie **Spring Boot** verwenden (ein gängiges Szenario), fügen Sie Ihren Build-Dateien die folgende Abhängigkeit hinzu:

- **Maven**:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-data-rest</artifactId>
  </dependency>
  ```

- **Gradle**:
  ```gradle
  implementation 'org.springframework.boot:spring-boot-starter-data-rest'
  ```

Dieses Starter-Paket bringt `spring-data-rest-core` zusammen mit anderen notwendigen Komponenten mit. Für Projekte ohne Spring Boot können Sie `spring-data-rest-core` direkt einbinden, aber das Spring Boot Starter-Paket wird der Einfachheit halber empfohlen.

---

### 2. Definieren Sie Ihre Entitäten
Erstellen Sie Ihr Domain-Modell, indem Sie Entitätsklassen mit einer Persistenztechnologie wie JPA (Java Persistence API) definieren. Zum Beispiel:

```java
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.GeneratedValue;

@Entity
public class User {
    @Id
    @GeneratedValue
    private Long id;
    private String name;

    // Konstruktoren
    public User() {}
    public User(String name) {
        this.name = name;
    }

    // Getter und Setter
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

Diese `User`-Entität repräsentiert eine einfache Tabelle in Ihrer Datenbank mit einer `id` und einem `name`.

---

### 3. Erstellen Sie Repository-Interfaces
Definieren Sie ein Repository-Interface für Ihre Entität, indem Sie eines der Spring Data-Repository-Interfaces erweitern, wie z.B. `JpaRepository`. Zum Beispiel:

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
```

Durch das Erweitern von `JpaRepository` erhalten Sie grundlegende CRUD-Operationen (Create, Read, Update, Delete) kostenlos. Spring Data REST wird dieses Repository automatisch als RESTful-Endpoint verfügbar machen.

---

### 4. Führen Sie Ihre Anwendung aus
Nachdem die Abhängigkeit hinzugefügt und Ihre Entitäten und Repositories definiert wurden, starten Sie Ihre Spring Boot-Anwendung. Spring Data REST generiert automatisch REST-Endpoints basierend auf Ihrem Repository. Für das oben genannte `UserRepository` können Sie darauf zugreifen:

- **GET /users**: Ruft eine Liste aller Benutzer ab.
- **GET /users/{id}**: Ruft einen bestimmten Benutzer anhand der ID ab.
- **POST /users**: Erstellt einen neuen Benutzer (mit einem JSON-Payload, z.B. `{"name": "Alice"}`).
- **PUT /users/{id}**: Aktualisiert einen bestehenden Benutzer.
- **DELETE /users/{id}**: Löscht einen Benutzer.

Wenn Ihre Anwendung beispielsweise auf `localhost:8080` läuft, können Sie ein Tool wie `curl` oder einen Browser zum Testen verwenden:

```bash
curl http://localhost:8080/users
```

Die Antwort enthält HATEOAS-Links, die es Clients ermöglichen, dynamisch zu verwandten Ressourcen zu navigieren.

---

### 5. (Optional) Passen Sie die REST-Endpoints an
Sie können anpassen, wie Ihre Repositories verfügbar gemacht werden, indem Sie Annotationen oder Konfigurationen verwenden:

- **Ändern Sie den Endpoint-Pfad**:
  Verwenden Sie die `@RepositoryRestResource`-Annotation, um einen benutzerdefinierten Pfad anzugeben:
  ```java
  import org.springframework.data.rest.core.annotation.RepositoryRestResource;

  @RepositoryRestResource(path = "people")
  public interface UserRepository extends JpaRepository<User, Long> {
  }
  ```
  Jetzt lautet der Endpoint `/people` anstelle von `/users`.

- **Globale Einstellungen konfigurieren**:
  Passen Sie den Basispfad oder andere Einstellungen an, indem Sie `RepositoryRestConfigurer` implementieren:
  ```java
  import org.springframework.data.rest.webmvc.config.RepositoryRestConfigurer;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.data.rest.core.config.RepositoryRestConfiguration;

  @Configuration
  public class RestConfig implements RepositoryRestConfigurer {
      @Override
      public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config) {
          config.setBasePath("/api"); // Alle Endpoints beginnen mit /api
      }
  }
  ```
  Damit wären Ihre Benutzer unter `/api/users` erreichbar.

---

### Wichtige Funktionen von Spring Data REST
- **HATEOAS-Unterstützung**: Antworten enthalten Hypermedia-Links zu verwandten Ressourcen.
- **Paginierung und Sortierung**: Verwenden Sie Abfrageparameter wie `?page=0&size=10&sort=name,asc`, um Ergebnisse zu paginieren und zu sortieren.
- **Filterung**: Fügen Sie Ihrem Repository benutzerdefinierte Abfragemethoden hinzu (z.B. `findByName(String name)`), um zusätzliche Endpoints verfügbar zu machen.

---

### Zusammenfassung
Um `spring-data-rest-core` zu verwenden:
1. Nehmen Sie die Spring Data REST-Abhängigkeit auf (z.B. `spring-boot-starter-data-rest` für Spring Boot).
2. Definieren Sie Ihre Entitäten mit entsprechenden Annotationen (z.B. `@Entity` für JPA).
3. Erstellen Sie Repository-Interfaces, die Spring Data-Interfaces erweitern (z.B. `JpaRepository`).
4. Führen Sie Ihre Anwendung aus, um auf automatisch generierte REST-Endpoints zuzugreifen.
5. Passen Sie optional Endpoint-Pfade oder das Verhalten nach Bedarf an.

Dieser Ansatz ermöglicht es Ihnen, schnell eine RESTful-API mit minimalem Code zu erstellen und dabei die Kernfunktionalität von Spring Data REST zu nutzen.