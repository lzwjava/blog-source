---
audio: false
generated: true
lang: de
layout: post
title: Swagger-Annotationen
translated: true
type: note
---

Um das `swagger-annotations`-Paket in Ihrem Java-Projekt zu verwenden, insbesondere für die Dokumentation einer mit Spring Boot erstellten REST-API, befolgen Sie diese Schritte. Diese Anleitung setzt voraus, dass Sie Swagger 2.0 verwenden, das häufig mit der `springfox`-Bibliothek integriert wird. Das `swagger-annotations`-Paket bietet Annotations, um Metadaten zu Ihren API-Endpunkten hinzuzufügen und ermöglicht so die automatische Generierung von API-Dokumentation.

---

### Schritt 1: Fügen Sie die erforderlichen Abhängigkeiten hinzu

Sie müssen das `swagger-annotations`-Paket und eine Swagger-Integrationsbibliothek (z.B. `springfox`) in Ihr Projekt einbinden. Wenn Sie Maven verwenden, fügen Sie die folgenden Abhängigkeiten zu Ihrer `pom.xml` hinzu:

```xml
<!-- Swagger Annotations -->
<dependency>
    <groupId>io.swagger</groupId>
    <artifactId>swagger-annotations</artifactId>
    <version>1.6.2</version>
</dependency>

<!-- Springfox Swagger 2 für Swagger-Integration -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
</dependency>

<!-- Springfox Swagger UI für interaktive Dokumentation -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.9.2</version>
</dependency>
```

- **`io.swagger:swagger-annotations`**: Bietet die Annotations für Swagger 2.0.
- **`springfox-swagger2`**: Integriert Swagger mit Spring Boot und verarbeitet die Annotations.
- **`springfox-swagger-ui`**: Fügt eine Weboberfläche hinzu, um die generierte Dokumentation anzuzeigen.

> **Hinweis**: Prüfen Sie die neuesten Versionen auf [Maven Repository](https://mvnrepository.com/), da diese Versionen (1.6.2 für `swagger-annotations` und 2.9.2 für `springfox`) möglicherweise Updates haben.

---

### Schritt 2: Konfigurieren Sie Swagger in Ihrer Anwendung

Um Swagger zu aktivieren und das Scannen Ihrer API nach Annotations zu ermöglichen, erstellen Sie eine Konfigurationsklasse mit einer `Docket`-Bean. Fügen Sie diese Ihrer Spring Boot-Anwendung hinzu:

```java
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@EnableSwagger2
public class SwaggerConfig {
    @Bean
    public Docket api() {
        return new Docket(DocumentationType.SWAGGER_2)
                .select()
                .apis(RequestHandlerSelectors.any()) // Scant alle Controller
                .paths(PathSelectors.any())          // Schließt alle Pfade ein
                .build();
    }
}
```

- **`@EnableSwagger2`**: Aktiviert die Swagger 2.0-Unterstützung.
- **`Docket`**: Konfiguriert, welche Endpunkte dokumentiert werden sollen. Das obige Setup scannt alle Controller und Pfade, aber Sie können es anpassen (z.B. `RequestHandlerSelectors.basePackage("com.example.controllers")`), um den Umfang einzuschränken.

---

### Schritt 3: Verwenden Sie Swagger-Annotations in Ihrem Code

Das `swagger-annotations`-Paket bietet Annotations, um Ihre API zu beschreiben. Wenden Sie diese auf Ihre Controller-Klassen, Methoden, Parameter und Modelle an. Nachfolgend finden Sie gängige Annotations mit Beispielen:

#### Einen Controller annotieren

Verwenden Sie `@Api`, um den Controller zu beschreiben:

```java
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "User Controller", description = "Operationen bezüglich Benutzern")
@RestController
@RequestMapping("/users")
public class UserController {
    // Methoden kommen hier hin
}
```

- **`value`**: Ein Kurzname für die API.
- **`description`**: Eine kurze Erklärung, was der Controller macht.

#### API-Operationen annotieren

Verwenden Sie `@ApiOperation`, um einzelne Endpunkte zu beschreiben:

```java
import io.swagger.annotations.ApiOperation;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Einen Benutzer anhand der ID abrufen", response = User.class)
@GetMapping("/{id}")
public ResponseEntity<User> getUserById(@PathVariable Long id) {
    // Implementierung
    return ResponseEntity.ok(new User(id, "John Doe"));
}
```

- **`value`**: Eine Zusammenfassung der Operation.
- **`response`**: Der erwartete Rückgabetyp.

#### Parameter beschreiben

Verwenden Sie `@ApiParam` für Methodenparameter:

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@ApiOperation(value = "Einen neuen Benutzer erstellen")
@PostMapping
public ResponseEntity<User> createUser(
        @ApiParam(value = "User-Objekt, das erstellt werden soll", required = true) 
        @RequestBody User user) {
    // Implementierung
    return ResponseEntity.ok(user);
}
```

- **`value`**: Beschreibt den Parameter.
- **`required`**: Zeigt an, ob der Parameter obligatorisch ist.

#### Antworten spezifizieren

Verwenden Sie `@ApiResponses` und `@ApiResponse`, um mögliche HTTP-Antworten zu dokumentieren:

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.ApiResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Einen Benutzer löschen")
@ApiResponses(value = {
    @ApiResponse(code = 200, message = "Benutzer erfolgreich gelöscht"),
    @ApiResponse(code = 404, message = "Benutzer nicht gefunden")
})
@DeleteMapping("/{id}")
public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
    // Implementierung
    return ResponseEntity.ok().build();
}
```

- **`code`**: HTTP-Statuscode.
- **`message`**: Beschreibung der Antwort.

#### Modelle beschreiben

Für Data Transfer Objects (DTOs) verwenden Sie `@ApiModel` und `@ApiModelProperty`:

```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(description = "User Data Transfer Object")
public class User {
    @ApiModelProperty(notes = "Der eindeutige Identifikator des Benutzers", example = "1")
    private Long id;

    @ApiModelProperty(notes = "Der Name des Benutzers", example = "John Doe")
    private String name;

    // Getter und Setter
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public User(Long id, String name) {
        this.id = id;
        this.name = name;
    }
}
```

- **`@ApiModel`**: Beschreibt das Modell.
- **`@ApiModelProperty`**: Detailliert jedes Feld mit optionalen Beispielen.

---

### Schritt 4: Führen Sie die Anwendung aus und greifen Sie auf die Dokumentation zu

1. Starten Sie Ihre Spring Boot-Anwendung.
2. Öffnen Sie einen Browser und navigieren Sie zu:  
   **http://localhost:8080/swagger-ui.html**  
   Diese URL zeigt die Swagger UI, eine interaktive Oberfläche, die Ihre API-Dokumentation basierend auf den Annotations anzeigt.

---

### Zusammenfassung zur Verwendung von `swagger-annotations`

1. **Abhängigkeiten hinzufügen**: Binden Sie `swagger-annotations` und `springfox` in Ihre `pom.xml` ein.
2. **Swagger konfigurieren**: Richten Sie eine `Docket`-Bean ein, um das Swagger-Scanning zu aktivieren.
3. **Ihren Code annotieren**:
   - `@Api` für Controller.
   - `@ApiOperation` für Methoden.
   - `@ApiParam` für Parameter.
   - `@ApiResponses` und `@ApiResponse` für Antwortdetails.
   - `@ApiModel` und `@ApiModelProperty` für DTOs.
4. **Dokumentation anzeigen**: Greifen Sie auf die Swagger UI unter `/swagger-ui.html` zu.

---

### Zusätzliche Hinweise

- **Swagger 2.0 vs. OpenAPI 3.0**: Diese Anleitung verwendet Swagger 2.0 mit `io.swagger:swagger-annotations`. Für OpenAPI 3.0 verwenden Sie `io.swagger.core.v3:swagger-annotations` und eine Bibliothek wie `springdoc-openapi`, was einige Annotationsnamen ändert (z.B. `@Tag` statt `@Api`).
- **Anpassung**: Passen Sie die `Docket`-Konfiguration an, um bestimmte Pakete oder Pfade zu filtern, für eine fokussiertere Dokumentation.
- **Qualität**: Geben Sie klare, detaillierte Beschreibungen in den Annotations an, um die Nützlichkeit der generierten Dokumentation zu verbessern.

Indem Sie diese Schritte befolgen, können Sie das `swagger-annotations`-Paket effektiv nutzen, um Ihre REST-API zu dokumentieren, was es Entwicklern und Konsumenten erleichtert, Ihre Endpunkte zu verstehen und mit ihnen zu interagieren.