---
audio: false
generated: true
lang: de
layout: post
title: Frühlingsinterne Abläufe
translated: true
type: note
---

Lassen Sie uns über Spring und seine internen Abläufe eintauchen. Spring ist ein robustes Framework zum Erstellen von Java-Anwendungen, und ich werde jeden Teil Ihrer Frage Schritt für Schritt mit klaren Erklärungen behandeln.

### Wie funktioniert Spring?
Spring arbeitet nach dem Prinzip der **Inversion of Control (IoC)**. Das bedeutet, dass nicht Ihr Anwendungscode die Erstellung und Verwaltung von Objekten steuert, sondern Spring diese Aufgabe übernimmt. Dies geschieht durch eine Komponente namens **IoC-Container**. Der IoC-Container ist verantwortlich für:

- **Instanziieren** von Objekten (genannt Beans in Spring).
- **Konfigurieren** dieser Objekte basierend auf Ihren Vorgaben.
- **Zusammenbauen** der Objekte durch Verwalten ihrer Abhängigkeiten.

Dieser Ansatz reduziert die enge Kopplung in Ihrem Code, macht ihn modularer und einfacher zu warten.

### Wie verwaltet Spring Beans?
In Spring sind **Beans** die Objekte, die vom IoC-Container verwaltet werden. So geht Spring mit ihnen um:

1.  **Definition**: Sie definieren Beans entweder in:
    - **XML-Konfigurationsdateien**.
    - **Java-basierter Konfiguration** unter Verwendung von Annotationen wie `@Bean`, `@Component`, `@Service`, usw.
2.  **Erstellung**: Wenn die Anwendung startet, liest der IoC-Container diese Definitionen und erstellt die Beans.
3.  **Dependency Injection (DI)**: Spring injiziert automatisch Abhängigkeiten (andere Beans) in eine Bean, wo sie benötigt werden, und verwendet dabei:
    - **Konstruktor-Injection**.
    - **Setter-Injection**.
    - **Feld-Injection** (via `@Autowired`).

Der Container verwaltet den gesamten Lebenszyklus dieser Beans – von der Erstellung bis zur Zerstörung – und stellt sicher, dass sie bei Bedarf verfügbar sind.

### Unterschied zwischen einem Service und einem Controller
Im Kontext von **Spring MVC** (Springs Web-Framework) haben diese beiden Komponenten unterschiedliche Zwecke:

-   **Controller**:
    - Verarbeitet **HTTP-Anfragen** von Benutzern.
    - Verarbeitet Eingaben, ruft Geschäftslogik auf und entscheidet, welche **View** (z.B. eine Webseite) zurückgegeben werden soll.
    - Wird mit `@Controller` oder `@RestController` annotiert.
    - Befindet sich in der **Web-Schicht**.

-   **Service**:
    - Kapselt die **Geschäftslogik** der Anwendung.
    - Führt Aufgaben wie Berechnungen, Datenverarbeitung oder Interaktion mit Datenbanken durch.
    - Wird mit `@Service` annotiert.
    - Befindet sich in der **Business-Schicht**.

**Beispiel**:
- Ein Controller könnte eine Anfrage zum Anzeigen eines Benutzerprofils erhalten und einen Service aufrufen, um die Benutzerdaten abzurufen.
- Der Service holt die Daten aus einer Datenbank und gibt sie an den Controller zurück, der sie dann an die View sendet.

Kurz gesagt: **Controller verwalten Web-Interaktionen**, während **Services die Kernfunktionalität handhaben**.

### Was bietet Spring?
Spring ist ein umfassendes Framework, das eine breite Palette von Tools für Enterprise-Anwendungen bietet. Wichtige Funktionen sind:

- **Dependency Injection**: Vereinfacht die Verwaltung von Objektabhängigkeiten.
- **Aspect-Oriented Programming (AOP)**: Fügt übergreifende Belange wie Logging oder Sicherheit hinzu.
- **Transaktionsverwaltung**: Stellt Datenkonsistenz über Operationen hinweg sicher.
- **Spring MVC**: Ermöglicht das Erstellen robuster Webanwendungen.
- **Spring Boot**: Vereinfacht das Setup mit vorkonfigurierten Standardeinstellungen und eingebetteten Servern.
- **Spring Data**: Vereinfacht den Datenbankzugriff.
- **Sicherheit**: Bietet Tools für Authentifizierung und Autorisierung.

Springs modulares Design ermöglicht es Ihnen, nur die benötigten Funktionen auszuwählen.

### Wie sucht Spring nach Objekten oder Beans?
Wenn eine Spring-Anwendung startet:

1.  Der **IoC-Container** initialisiert.
2.  Er scannt nach **Bean-Definitionen** in:
    - XML-Dateien.
    - Annotierten Klassen (z.B. `@Component`, `@Bean`).
3.  Der Container erstellt die Beans und speichert sie in einer **Map**, indiziert nach Name oder Typ.
4.  Wenn eine Bean benötigt wird (z.B. für Injection oder direkten Abruf), stellt sie der Container bereit, indem er verwendet:
    - **Lookup nach Namen**.
    - **Lookup nach Typ** (z.B. via `@Autowired`).

Dieser Prozess stellt sicher, dass Beans throughout der Anwendung leicht verfügbar sind.

### Wie verwendet man Tomcat oder Netty als Server?
Spring Boot, eine Erweiterung von Spring, vereinfacht die Server-Einrichtung, indem es Server direkt in Ihre Anwendung einbettet. So funktioniert es mit **Tomcat** und **Netty**:

-   **Tomcat** (Servlet-basiert):
    - Standard-Server in Spring Boots `spring-boot-starter-web` Dependency.
    - Fügen Sie dies zu Ihrer `pom.xml` hinzu:
      ```xml
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-web</artifactId>
      </dependency>
      ```
    - Spring Boot bettet Tomcat ein, und Ihre App läuft als eigenständige ausführbare JAR-Datei.

-   **Netty** (Nicht-Servlet-basiert):
    - Wird für reaktive Webanwendungen verwendet (z.B. mit Spring WebFlux).
    - Ersetzen Sie Tomcat, indem Sie es ausschließen und Netty hinzufügen:
      ```xml
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-webflux</artifactId>
      </dependency>
      ```
    - Spring Boot bettet stattdessen Netty ein und unterstützt asynchrone, nicht-blockierende E/A.

Sie konfigurieren den Server über `application.properties` (z.B. Setzen des Ports mit `server.port=8080`). Es ist keine Bereitstellung auf einem externen Server erforderlich – Spring Boot erledigt alles.

### Zusammenfassung
-   **Springs Kern**: Verwendet einen IoC-Container für die Objektverwaltung.
-   **Bean-Verwaltung**: Wird via XML oder Annotationen definiert, mit automatisch injizierten Abhängigkeiten.
-   **Service vs. Controller**: Services handhaben Geschäftslogik; Controller verwalten Web-Anfragen.
-   **Funktionen**: Bietet DI, AOP, Web-Unterstützung und mehr.
-   **Bean-Lookup**: Container findet und stellt Beans aus Konfigurationen bereit.
-   **Server**: Spring Boot bettet Tomcat oder Netty mit einfachen Dependency-Änderungen ein.