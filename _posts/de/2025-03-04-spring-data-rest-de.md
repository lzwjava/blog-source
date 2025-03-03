---
audio: false
generated: true
lang: de
layout: post
title: Spring Data REST Modul
translated: true
---

Um **spring-data-rest-core** zu verwenden, können Sie das Spring Data REST-Modul nutzen, um Ihre Spring Data-Repositories als RESTful-Endpunkte in Ihrer Anwendung freizugeben. Hier ist eine vollständige Schritt-für-Schritt-Anleitung, um Ihnen den Einstieg zu erleichtern:

---

### 1. Spring Data REST-Abhängigkeit hinzufügen
Um Spring Data REST zu verwenden, müssen Sie dessen Abhängigkeit in Ihrem Projekt einbinden. Wenn Sie **Spring Boot** verwenden (ein häufiger Fall), fügen Sie die folgende Abhängigkeit zu Ihrer Build-Datei hinzu:

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

Dieser Starter bringt `spring-data-rest-core` zusammen mit anderen notwendigen Komponenten mit. Für Nicht-Spring-Boot-Projekte können Sie `spring-data-rest-core` direkt einbinden, aber der Spring Boot Starter wird aus Gründen der Einfachheit empfohlen.

---

### 2. Ihre Entitäten definieren
Erstellen Sie Ihr Domänenmodell, indem Sie Entitätsklassen mit einer Persistenztechnologie wie JPA (Java Persistence API) definieren. Zum Beispiel:

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

Diese `User`-Entität stellt eine einfache Tabelle in Ihrer Datenbank mit einer `id` und `name` dar.

---

### 3. Repository-Schnittstellen erstellen
Definieren Sie eine Repository-Schnittstelle für Ihre Entität, indem Sie eine der Spring Data-Repository-Schnittstellen erweitern, wie z.B. `JpaRepository`. Zum Beispiel:

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
```

Durch die Erweiterung von `JpaRepository` erhalten Sie grundlegende CRUD-Operationen (Erstellen, Lesen, Aktualisieren, Löschen) kostenlos. Spring Data REST wird dieses Repository automatisch als RESTful-Endpunkt freigeben.

---

### 4. Ihre Anwendung starten
Mit der hinzugefügten Abhängigkeit und Ihren definierten Entitäten und Repositories starten Sie Ihre Spring Boot-Anwendung. Spring Data REST wird automatisch REST-Endpunkte basierend auf Ihrem Repository generieren. Für das obige `UserRepository` können Sie auf Folgendes zugreifen:

- **GET /users**: Abrufen einer Liste aller Benutzer.
- **GET /users/{id}**: Abrufen eines bestimmten Benutzers anhand der ID.
- **POST /users**: Erstellen eines neuen Benutzers (mit einem JSON-Payload, z.B. `{"name": "Alice"}`).
- **PUT /users/{id}**: Aktualisieren eines bestehenden Benutzers.
- **DELETE /users/{id}**: Löschen eines Benutzers.

Zum Beispiel, wenn Ihre Anwendung auf `localhost:8080` läuft, können Sie ein Tool wie `curl` oder einen Browser verwenden, um zu testen:

```bash
curl http://localhost:8080/users
```

Die Antwort wird HATEOAS-Links enthalten, die es den Clients ermöglichen, dynamisch auf verwandte Ressourcen zuzugreifen.

---

### 5. (Optional) REST-Endpunkte anpassen
Sie können anpassen, wie Ihre Repositories freigegeben werden, indem Sie Annotationen oder Konfigurationen verwenden:

- **Endpunkt-Pfad ändern**:
  Verwenden Sie die `@RepositoryRestResource`-Annotation, um einen benutzerdefinierten Pfad anzugeben:
  ```java
  import org.springframework.data.rest.core.annotation.RepositoryRestResource;

  @RepositoryRestResource(path = "people")
  public interface UserRepository extends JpaRepository<User, Long> {
  }
  ```
  Jetzt wird der Endpunkt `/people` anstelle von `/users` sein.

- **Globale Einstellungen konfigurieren**:
  Passen Sie den Basis-Pfad oder andere Einstellungen an, indem Sie `RepositoryRestConfigurer` implementieren:
  ```java
  import org.springframework.data.rest.webmvc.config.RepositoryRestConfigurer;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.data.rest.core.config.RepositoryRestConfiguration;

  @Configuration
  public class RestConfig implements RepositoryRestConfigurer {
      @Override
      public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config) {
          config.setBasePath("/api"); // Alle Endpunkte beginnen mit /api
      }
  }
  ```
  Mit dieser Konfiguration sind Ihre Benutzer unter `/api/users` erreichbar.

---

### Wichtige Funktionen von Spring Data REST
- **HATEOAS-Unterstützung**: Antworten enthalten Hypermedia-Links zu verwandten Ressourcen.
- **Seitenweise Darstellung und Sortierung**: Verwenden Sie Abfrageparameter wie `?page=0&size=10&sort=name,asc`, um Ergebnisse zu paginieren und zu sortieren.
- **Filtern**: Fügen Sie benutzerdefinierte Abfrage-Methoden zu Ihrem Repository hinzu (z.B. `findByName(String name)`), um zusätzliche Endpunkte freizugeben.

---

### Zusammenfassung
Um `spring-data-rest-core` zu verwenden:
1. Fügen Sie die Spring Data REST-Abhängigkeit hinzu (z.B. `spring-boot-starter-data-rest` für Spring Boot).
2. Definieren Sie Ihre Entitäten mit den entsprechenden Annotationen (z.B. `@Entity` für JPA).
3. Erstellen Sie Repository-Schnittstellen, die Spring Data-Schnittstellen erweitern (z.B. `JpaRepository`).
4. Starten Sie Ihre Anwendung, um automatisch generierte REST-Endpunkte zu nutzen.
5. Passen Sie bei Bedarf Endpunkt-Pfade oder -Verhalten an.

Diese Vorgehensweise ermöglicht es Ihnen, schnell eine RESTful-API mit minimalem Code zu erstellen, indem Sie die Kernfunktionen von Spring Data REST nutzen.