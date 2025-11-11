---
audio: false
generated: true
lang: de
layout: post
title: Wie Eigenschaften in Spring Boot funktionieren
translated: true
type: note
---

Lassen Sie uns untersuchen, wie Properties in Spring Boot funktionieren, einschließlich der Verwendung von YAML- oder `.properties`-Dateien, wie man sie mit Command-Line-Argumenten wie `-D` überschreibt, die verschiedenen Möglichkeiten zur Initialisierung von Properties und wie man sie effektiv testet.

---

### **Wie Properties in Spring Boot funktionieren**
Spring Boot bietet ein flexibles System zur Verwaltung der Anwendungskonfiguration durch Properties, die als Schlüssel-Wert-Paare definiert sind. Diese Properties können in mehreren Quellen definiert werden, und Spring Boot löst sie basierend auf einer bestimmten Reihenfolge der Priorität auf. Dies ermöglicht es Ihnen, Ihre Anwendung für verschiedene Umgebungen oder Bereitstellungsszenarien anzupassen. Properties werden in die **Spring Environment** geladen, wodurch sie in Ihrer gesamten Anwendung zugänglich sind.

Die Hauptquellen für Properties umfassen:
- Konfigurationsdateien (z.B. `application.properties` oder `application.yml`)
- Command-Line-Argumente (z.B. `--server.port=8081`)
- Systemproperties (z.B. `-Dserver.port=8081`)
- Umgebungsvariablen
- Java-Code (z.B. via `@Value` oder `@ConfigurationProperties`)

---

### **Verwendung von YAML oder Properties-Dateien**
Spring Boot unterstützt zwei primäre Formate für Konfigurationsdateien, die typischerweise in `src/main/resources` abgelegt werden:

#### **1. `.properties`-Dateien**
Dies ist ein einfaches, flaches Schlüssel-Wert-Format:
```properties
server.port=8080
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
```

#### **2. `.yml`- oder `.yaml`-Dateien**
Dies ist ein strukturiertes, hierarchisches Format, das Einrückungen verwendet:
```yaml
server:
  port: 8080
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
```

**Wichtige Punkte:**
- Verwenden Sie `.properties` für einfache Konfigurationen und `.yml` für verschachtelte oder komplexe Setups.
- Profilspezifische Dateien (z.B. `application-dev.yml`) können für umgebungsspezifische Einstellungen verwendet werden.
- Beispiel: Das Setzen von `server.port=8080` ändert den Port, auf dem Ihre Spring Boot-Anwendung läuft.

---

### **Verwendung von Command-Line-Argumenten zum Überschreiben von Properties**
Sie können Properties, die in Konfigurationsdateien definiert sind, auf zwei Arten mit Command-Line-Argumenten überschreiben:

#### **1. Verwendung von `--` für Spring Boot Properties**
Übergeben Sie Properties direkt beim Ausführen der Anwendung:
```bash
java -jar myapp.jar --server.port=8081 --spring.datasource.url=jdbc:mysql://localhost:3306/testdb
```
Diese haben Vorrang vor Konfigurationsdateien.

#### **2. Verwendung von `-D` für Systemproperties**
Setzen Sie Systemproperties mit `-D`, die Spring Boot ebenfalls erkennt:
```bash
java -Dserver.port=8081 -Dspring.datasource.url=jdbc:mysql://localhost:3306/testdb -jar myapp.jar
```
Systemproperties überschreiben ebenfalls die Werte aus Konfigurationsdateien.

---

### **Verschiedene Möglichkeiten zur Initialisierung von Properties**
Spring Boot bietet mehrere Methoden, um Properties über Dateien und Command-Line-Argumente hinaus zu definieren oder zu initialisieren:

#### **1. Umgebungsvariablen**
Properties können über Umgebungsvariablen gesetzt werden. Zum Beispiel:
- Setzen Sie `SERVER_PORT=8081` in Ihrer Umgebung, und Spring Boot ordnet es `server.port` zu.
- **Namenskonvention:** Konvertieren Sie Property-Namen in Großbuchstaben und ersetzen Sie Punkte (`.`) durch Unterstriche (`_`), z.B. wird `spring.datasource.url` zu `SPRING_DATASOURCE_URL`.

#### **2. Java-Code**
Sie können Properties programmatisch initialisieren:
- **Verwendung von `@Value`**: Injizieren Sie eine bestimmte Property in ein Feld.
  ```java
  @Value("${server.port}")
  private int port;
  ```
- **Verwendung von `@ConfigurationProperties`**: Binden Sie eine Gruppe von Properties an ein Java-Objekt.
  ```java
  @Component
  @ConfigurationProperties(prefix = "app")
  public class AppProperties {
      private String name;
      // Getter und Setter
  }
  ```
  Dies bindet Properties wie `app.name` an das Feld `name`.

#### **3. Standardwerte**
Geben Sie Fallback-Werte an, wenn eine Property nicht definiert ist:
- In `@Value`: `@Value("${server.port:8080}")` verwendet `8080`, wenn `server.port` nicht gesetzt ist.
- In Konfigurationsdateien: Setzen Sie Standardwerte in `application.properties` oder YAML.

---

### **Property-Priorität**
Spring Boot löst Properties aus mehreren Quellen in dieser Reihenfolge auf (höhere Priorität überschreibt niedrigere):
1. Command-Line-Argumente (`--property=value`)
2. Systemproperties (`-Dproperty=value`)
3. Umgebungsvariablen
4. Konfigurationsdateien (`application.properties` oder `application.yml`)
5. Standardwerte im Code

**Beispiel:** Wenn `server.port=8080` in `application.properties` steht, Sie aber `java -jar myapp.jar --server.port=8081` ausführen, wird der Port `8081` sein.

---

### **Wie man Properties testet**
Das Testen von Properties stellt sicher, dass sich Ihre Anwendung wie erwartet verhält. Hier sind gängige Ansätze:

#### **1. Verwendung von `@TestPropertySource`**
Überschreiben Sie Properties in Unit-Tests:
```java
@SpringBootTest
@TestPropertySource(properties = {"server.port=9090"})
public class MyTest {
    // Testcode
}
```

#### **2. Verwendung von `application-test.properties`**
Legen Sie eine testspezifische Datei in `src/test/resources` ab:
```properties
server.port=9090
```
Spring Boot lädt diese automatisch während der Tests.

#### **3. Programmatische Überschreibungen**
Setzen Sie Properties im Test-Setup:
```java
@SpringBootTest
public class MyTest {
    @BeforeEach
    public void setup() {
        System.setProperty("server.port", "9090");
    }
}
```

#### **4. Verwendung von `@ActiveProfiles`**
Aktivieren Sie profilspezifische Properties:
- Definieren Sie `application-test.yml` mit Testeinstellungen.
- Verwenden Sie:
  ```java
  @SpringBootTest
  @ActiveProfiles("test")
  public class MyTest {
      // Testcode
  }
  ```

---

### **Zusammenfassung**
- **Konfigurationsdateien**: Verwenden Sie `application.properties` oder `application.yml` für Standardeinstellungen.
- **Command-Line-Argumente**: Überschreiben Sie mit `--property=value` oder `-Dproperty=value`.
- **Initialisierungsmethoden**: Nutzen Sie Umgebungsvariablen, Java-Code (`@Value`, `@ConfigurationProperties`) oder Standardwerte.
- **Testing**: Verwenden Sie `@TestPropertySource`, testspezifische Dateien, programmatische Überschreibungen oder Profile.

Dies deckt die Grundlagen der Arbeit mit Properties in Spring Boot ab. Lassen Sie mich wissen, wenn Sie weitere Details wünschen!