---
audio: true
generated: true
lang: de
layout: post
title: Swagger Annotationen
translated: true
---

Um das `swagger-annotations`-Paket in Ihrem Java-Projekt zu verwenden, insbesondere zur Dokumentation einer mit Spring Boot erstellten REST-API, befolgen Sie diese Schritte. Diese Anleitung geht davon aus, dass Sie Swagger 2.0 verwenden, das häufig mit der `springfox`-Bibliothek integriert wird. Das `swagger-annotations`-Paket bietet Annotationen, um Ihre API-Endpunkte mit Metadaten zu versehen und die automatische Erstellung von API-Dokumentation zu ermöglichen.

---

### Schritt 1: Fügen Sie die erforderlichen Abhängigkeiten hinzu

Sie müssen das `swagger-annotations`-Paket und eine Swagger-Integrationsbibliothek (z. B. `springfox`) in Ihr Projekt einbinden. Wenn Sie Maven verwenden, fügen Sie die folgenden Abhängigkeiten zu Ihrer `pom.xml` hinzu:

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

- **`io.swagger:swagger-annotations`**: Bietet die Annotationen für Swagger 2.0.
- **`springfox-swagger2`**: Integriert Swagger mit Spring Boot und verarbeitet die Annotationen.
- **`springfox-swagger-ui`**: Fügt eine Web-Oberfläche hinzu, um die generierte Dokumentation anzuzeigen.

> **Hinweis**: Überprüfen Sie die neuesten Versionen im [Maven Repository](https://mvnrepository.com/), da diese Versionen (1.6.2 für `swagger-annotations` und 2.9.2 für `springfox`) möglicherweise aktualisiert wurden.

---

### Schritt 2: Konfigurieren Sie Swagger in Ihrer Anwendung

Um Swagger zu aktivieren und es zu ermöglichen, Ihre API nach Annotationen zu durchsuchen, erstellen Sie eine Konfigurationsklasse mit einem `Docket`-Bean. Fügen Sie dies zu Ihrer Spring Boot-Anwendung hinzu:

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
                .apis(RequestHandlerSelectors.any()) // Scan all controllers
                .paths(PathSelectors.any())          // Include all paths
                .build();
    }
}
```

- **`@EnableSwagger2`**: Aktiviert die Unterstützung für Swagger 2.0.
- **`Docket`**: Konfiguriert, welche Endpunkte dokumentiert werden sollen. Die obige Konfiguration scannt alle Controller und Pfade, aber Sie können dies anpassen (z. B. `RequestHandlerSelectors.basePackage("com.example.controllers")`), um den Umfang zu begrenzen.

---

### Schritt 3: Verwenden Sie Swagger-Annotationen in Ihrem Code

Das `swagger-annotations`-Paket bietet Annotationen, um Ihre API zu beschreiben. Wenden Sie diese auf Ihre Controller-Klassen, Methoden, Parameter und Modelle an. Hier sind einige gängige Annotationen mit Beispielen:

#### Annotieren eines Controllers

Verwenden Sie `@Api`, um den Controller zu beschreiben:

```java
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "Benutzer-Controller", description = "Vorgänge, die Benutzer betreffen")
@RestController
@RequestMapping("/users")
public class UserController {
    // Methoden hier
}
```

- **`value`**: Ein kurzer Name für die API.
- **`description`**: Eine kurze Erklärung, was der Controller macht.

#### Annotieren von API-Vorgängen

Verwenden Sie `@ApiOperation`, um einzelne Endpunkte zu beschreiben:

```java
import io.swagger.annotations.ApiOperation;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Benutzer nach ID abrufen", response = User.class)
@GetMapping("/{id}")
public ResponseEntity<User> getUserById(@PathVariable Long id) {
    // Implementierung
    return ResponseEntity.ok(new User(id, "John Doe"));
}
```

- **`value`**: Eine Zusammenfassung des Vorgangs.
- **`response`**: Der erwartete Rückgabetyp.

#### Beschreiben von Parametern

Verwenden Sie `@ApiParam` für Methodenparameter:

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@ApiOperation(value = "Erstellen eines neuen Benutzers")
@PostMapping
public ResponseEntity<User> createUser(
        @ApiParam(value = "Zu erstellendes Benutzerobjekt", required = true)
        @RequestBody User user) {
    // Implementierung
    return ResponseEntity.ok(user);
}
```

- **`value`**: Beschreibt den Parameter.
- **`required`**: Gibt an, ob der Parameter obligatorisch ist.

#### Spezifizieren von Antworten

Verwenden Sie `@ApiResponses` und `@ApiResponse`, um mögliche HTTP-Antworten zu dokumentieren:

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.ApiResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Benutzer löschen")
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

#### Beschreiben von Modellen

Für Datenübertragungsobjekte (DTOs) verwenden Sie `@ApiModel` und `@ApiModelProperty`:

```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(description = "Benutzer-Datenübertragungsobjekt")
public class User {
    @ApiModelProperty(notes = "Die eindeutige Kennung des Benutzers", example = "1")
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
- **`@ApiModelProperty`**: Gibt Details zu jedem Feld an, optional mit Beispielen.

---

### Schritt 4: Starten und Zugriff auf die Dokumentation

1. Starten Sie Ihre Spring Boot-Anwendung.
2. Öffnen Sie einen Browser und navigieren Sie zu:
   **http://localhost:8080/swagger-ui.html**
   Diese URL zeigt die Swagger-UI an, eine interaktive Oberfläche, die Ihre API-Dokumentation basierend auf den Annotationen anzeigt.

---

### Zusammenfassung der Verwendung von `swagger-annotations`

1. **Abhängigkeiten hinzufügen**: Fügen Sie `swagger-annotations` und `springfox` zu Ihrer `pom.xml` hinzu.
2. **Swagger konfigurieren**: Richten Sie ein `Docket`-Bean ein, um das Scannen durch Swagger zu aktivieren.
3. **Code annotieren**:
   - `@Api` für Controller.
   - `@ApiOperation` für Methoden.
   - `@ApiParam` für Parameter.
   - `@ApiResponses` und `@ApiResponse` für Antwortdetails.
   - `@ApiModel` und `@ApiModelProperty` für DTOs.
4. **Dokumentation anzeigen**: Greifen Sie auf die Swagger-UI unter `/swagger-ui.html` zu.

---

### Zusätzliche Hinweise

- **Swagger 2.0 vs. OpenAPI 3.0**: Diese Anleitung verwendet Swagger 2.0 mit `io.swagger:swagger-annotations`. Für OpenAPI 3.0 verwenden Sie `io.swagger.core.v3:swagger-annotations` und eine Bibliothek wie `springdoc-openapi`, was einige Annotationsnamen ändert (z. B. `@Tag` anstelle von `@Api`).
- **Anpassung**: Passen Sie die `Docket`-Konfiguration an, um bestimmte Pakete oder Pfade zu filtern, um eine fokussiertere Dokumentation zu erhalten.
- **Qualität**: Geben Sie klare, detaillierte Beschreibungen in den Annotationen an, um die Nützlichkeit der generierten Dokumentation zu verbessern.

Durch die Befolgung dieser Schritte können Sie das `swagger-annotations`-Paket effektiv nutzen, um Ihre REST-API zu dokumentieren und es Entwicklern und Verbrauchern zu erleichtern, Ihre Endpunkte zu verstehen und damit zu interagieren.