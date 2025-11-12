---
audio: false
generated: true
lang: de
layout: post
title: Spring Boot Ausnahmen
translated: true
type: note
---

Bei der Arbeit mit Spring Boot oder dem umfassenderen Spring Framework sehen sich Entwickler häufig Ausnahmen aufgrund von Konfigurationsproblemen, Laufzeitfehlern oder unsachgemäßer Verwendung von APIs gegenüber. Nachfolgend finden Sie eine Liste häufiger Ausnahmen, auf die Sie stoßen könnten, zusammen mit ihren typischen Ursachen und möglichen Lösungen. Diese Ausnahmen sind der Übersichtlichkeit halber nach Kategorien gruppiert.

---

### **1. Konfigurationsbezogene Ausnahmen**

- **`org.springframework.beans.factory.BeanCreationException`**:
  - **Ursache**: Eine Bean konnte aufgrund fehlender Abhängigkeiten, Fehlkonfiguration oder Instanziierungsfehlern nicht erstellt werden.
  - **Beispiel**: Fehlende `@Component`, `@Service` oder `@Autowired`-Abhängigkeit nicht gefunden.
  - **Lösung**: Bean-Definitionen prüfen, sicherstellen, dass Abhängigkeiten verfügbar sind, und Annotationen überprüfen.

- **`org.springframework.beans.factory.NoSuchBeanDefinitionException`**:
  - **Ursache**: Spring kann eine Bean des angeforderten Typs oder Namens im Application Context nicht finden.
  - **Beispiel**: Versuch, eine nicht definierte oder gescannte Bean mit `@Autowired` zu injecten.
  - **Lösung**: Sicherstellen, dass die Bean annotiert ist (z.B. mit `@Component`) und sich im Pfad des Component-Scans befindet.

- **`org.springframework.context.ApplicationContextException`**:
  - **Ursache**: Allgemeiner Fehler bei der Initialisierung des Spring Application Context.
  - **Beispiel**: Ungültige Konfiguration in `application.properties` oder ein Syntaxfehler in einer `@Configuration`-Klasse.
  - **Lösung**: Stacktrace auf die Grundursache überprüfen (z.B. ungültige Property oder fehlende Ressource).

- **`org.springframework.beans.factory.UnsatisfiedDependencyException`**:
  - **Ursache**: Eine für eine Bean erforderliche Abhängigkeit kann nicht erfüllt werden.
  - **Beispiel**: Zirkuläre Abhängigkeit oder fehlende Implementierung für ein Interface.
  - **Lösung**: Zirkuläre Abhängigkeiten auflösen (z.B. mit `@Lazy`) oder die fehlende Abhängigkeit bereitstellen.

---

### **2. Web- und REST-bezogene Ausnahmen**

- **`org.springframework.web.bind.MissingServletRequestParameterException`**:
  - **Ursache**: Ein erforderlicher Request-Parameter fehlt in einer HTTP-Anfrage.
  - **Beispiel**: `@RequestParam("id")` ist angegeben, aber der Client hat keine `id` gesendet.
  - **Lösung**: Den Parameter optional machen (`required = false`) oder sicherstellen, dass der Client ihn mitsendet.

- **`org.springframework.http.converter.HttpMessageNotReadableException`**:
  - **Ursache**: Der Request-Body kann nicht deserialisiert werden (z.B. fehlerhaftes JSON).
  - **Beispiel**: Senden von ungültigem JSON an einen `@RequestBody`-Endpunkt.
  - **Lösung**: Die Request-Payload validieren und sicherstellen, dass sie zur Struktur des Zielobjekts passt.

- **`org.springframework.web.method.annotation.MethodArgumentTypeMismatchException`**:
  - **Ursache**: Ein Methodenargument kann nicht in den erwarteten Typ konvertiert werden.
  - **Beispiel**: Übergabe eines Strings wie `"abc"` an einen Parameter, der einen `int` erwartet.
  - **Lösung**: Eingabe validieren oder benutzerdefinierte Konverter verwenden.

- **`org.springframework.web.servlet.NoHandlerFoundException`**:
  - **Ursache**: Es existiert kein Controller-Mapping für die angeforderte URL.
  - **Beispiel**: Tippfehler in `@RequestMapping` oder fehlender Controller.
  - **Lösung**: Endpunkt-Mappings überprüfen und sicherstellen, dass Controller gescannt werden.

---

### **3. Datenzugriffsausnahmen (Spring Data/JPA/Hibernate)**

- **`org.springframework.dao.DataIntegrityViolationException`**:
  - **Ursache**: Ein Datenbankvorgang verletzt eine Constraint (z.B. Unique Key oder Foreign Key).
  - **Beispiel**: Einfügen eines doppelten Primärschlüsselwerts.
  - **Lösung**: Daten auf Eindeutigkeit prüfen oder die Ausnahme abfangen.

- **`org.springframework.orm.jpa.JpaSystemException`**:
  - **Ursache**: Allgemeiner JPA-bezogener Laufzeitfehler, oft als Wrapper für eine Hibernate-Exception.
  - **Beispiel**: Constraint-Verletzung oder Verbindungsproblem.
  - **Lösung**: Die verschachtelte Ausnahme (z.B. `SQLException`) auf Details untersuchen.

- **`org.hibernate.LazyInitializationException`**:
  - **Ursache**: Versuch, auf eine lazy-geladene Entität außerhalb einer aktiven Session zuzugreifen.
  - **Beispiel**: Zugriff auf eine `@OneToMany`-Beziehung nach Ende der Transaktion.
  - **Lösung**: Eager Fetching verwenden, im Query fetchen (z.B. `JOIN FETCH`) oder eine offene Session sicherstellen.

- **`org.springframework.dao.InvalidDataAccessApiUsageException`**:
  - **Ursache**: Falsche Verwendung der Spring Data- oder JDBC-APIs.
  - **Beispiel**: Übergeben eines null-Parameters an eine Query, die einen Wert erwartet.
  - **Lösung**: Query-Parameter und API-Nutzung validieren.

---

### **4. Sicherheitsbezogene Ausnahmen**

- **`org.springframework.security.access.AccessDeniedException`**:
  - **Ursache**: Der authentifizierte Benutzer hat keine Berechtigung für eine Ressource.
  - **Beispiel**: Zugriff auf einen gesicherten Endpunkt ohne die erforderliche Rolle.
  - **Lösung**: `@PreAuthorize` oder Sicherheitskonfiguration prüfen und Rollen/Berechtigungen anpassen.

- **`org.springframework.security.authentication.BadCredentialsException`**:
  - **Ursache**: Authentifizierung aufgrund falschen Benutzernamens oder Passworts fehlgeschlagen.
  - **Beispiel**: Benutzer gibt falsche Anmeldedaten in einem Login-Formular ein.
  - **Lösung**: Sicherstellen, dass die Anmeldedaten korrekt sind; Fehlerbehandlung für Benutzerfeedback anpassen.

- **`org.springframework.security.authentication.DisabledException`**:
  - **Ursache**: Das Benutzerkonto ist deaktiviert.
  - **Beispiel**: Eine `UserDetails`-Implementierung gibt `isEnabled() == false` zurück.
  - **Lösung**: Konto aktivieren oder Benutzerstatus aktualisieren.

---

### **5. Verschiedene Laufzeitausnahmen**

- **`java.lang.IllegalStateException`**:
  - **Ursache**: Spring stößt während der Ausführung auf einen ungültigen Zustand.
  - **Beispiel**: Aufruf einer Methode auf einer Bean, die nicht vollständig initialisiert wurde.
  - **Lösung**: Lebenszyklus-Methoden oder die Initialisierungsreihenfolge der Beans prüfen.

- **`org.springframework.transaction.TransactionException`**:
  - **Ursache**: Ein Problem ist während der Transaktionsverwaltung aufgetreten.
  - **Beispiel**: Transaktion-Rollback aufgrund einer nicht behandelten Ausnahme.
  - **Lösung**: Richtige Verwendung von `@Transactional` sicherstellen und Ausnahmen innerhalb der Transaktion behandeln.

- **`java.lang.NullPointerException`**:
  - **Ursache**: Versuch, auf eine null-Objektreferenz zuzugreifen.
  - **Beispiel**: Eine `@Autowired`-Abhängigkeit wurde aufgrund einer Fehlkonfiguration nicht injiziert.
  - **Lösung**: Null-Checks hinzufügen oder debuggen, warum die Abhängigkeit fehlt.

---

### **6. Spring Boot-spezifische Ausnahmen**

- **`org.springframework.boot.context.embedded.EmbeddedServletContainerException`** (ältere Versionen) oder **`org.springframework.boot.web.server.WebServerException`** (neuere Versionen):
  - **Ursache**: Fehler beim Starten des eingebetteten Web-Servers (z.B. Tomcat, Jetty).
  - **Beispiel**: Port bereits in Verwendung (z.B. `8080`).
  - **Lösung**: Port in `application.properties` ändern (`server.port=8081`) oder den belegten Port freigeben.

- **`org.springframework.boot.autoconfigure.jdbc.DataSourceProperties$DataSourceBeanCreationException`**:
  - **Ursache**: Fehler beim Konfigurieren der DataSource.
  - **Beispiel**: Fehlende oder falsche `spring.datasource.url/username/password`.
  - **Lösung**: DataSource-Properties in `application.properties` oder `application.yml` überprüfen.

- **`org.springframework.boot.SpringApplication - Application run failed`**:
  - **Ursache**: Allgemeiner Fehler während des Spring Boot-Starts.
  - **Beispiel**: Fehlkonfiguration, fehlende Beans oder Abhängigkeitskonflikte.
  - **Lösung**: Den vollständigen Stacktrace auf die Grundursache überprüfen.

---

### **Best Practices zur Ausnahmebehandlung**

1. **Globale Ausnahmebehandlung**:
   - Verwenden Sie `@ControllerAdvice` mit `@ExceptionHandler`, um Ausnahmen konsistent über Ihre Anwendung hinweg abzufangen und zu behandeln.
   - Beispiel:
     ```java
     @ControllerAdvice
     public class GlobalExceptionHandler {
         @ExceptionHandler(DataIntegrityViolationException.class)
         public ResponseEntity<String> handleDataIntegrityViolation() {
             return ResponseEntity.status(HttpStatus.CONFLICT).body("Data integrity violation occurred.");
         }
     }
     ```

2. **Logging**:
   - Loggen Sie Ausnahmen mit einem Framework wie SLF4J/Logback, um die Fehlersuche zu erleichtern.

3. **Benutzerdefinierte Ausnahmen**:
   - Definieren Sie anwendungsspezifische Ausnahmen und ordnen Sie sie geeigneten HTTP-Statuscodes zu.

4. **Validierung**:
   - Verwenden Sie `@Valid` und Bean Validation (z.B. `@NotNull`), um Fehler frühzeitig abzufangen und Laufzeitausnahmen zu vermeiden.

5. **Debugging**:
   - Aktivieren Sie detailliertes Logging (`logging.level.org.springframework=DEBUG`) in `application.properties`, um Probleme nachzuverfolgen.

---

### **Schlussfolgerung**

Diese Ausnahmen gehören zu den häufigsten, auf die Sie bei der Verwendung von Spring Boot oder dem Spring Framework stoßen werden. Das Verständnis ihrer Ursachen und Lösungen kann die Entwicklung und Fehlersuche erheblich beschleunigen. Wenn Sie auf eine bestimmte Ausnahme stoßen und eine tiefergehende Erklärung benötigen, teilen Sie mir bitte die Details mit, und ich werde eine maßgeschneiderte Erklärung liefern!