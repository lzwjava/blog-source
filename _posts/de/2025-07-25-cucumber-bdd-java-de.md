---
audio: false
generated: true
image: false
lang: de
layout: post
title: BDD-Leitfaden für Java-Entwickler mit Gurken
translated: true
type: note
---

Hier ist eine praktische, umfassende Einführung in **Cucumber** – was es ist, warum Teams es verwenden und wie man damit in Java produktiv wird (plus kurze Hinweise für JS/Python-Nutzer).

---

# Was Cucumber ist (und was nicht)

*   **Cucumber** ist ein **BDD (Behavior-Driven Development)** Test-Framework. Es ermöglicht dir, Verhalten in einfacher Sprache (Gherkin) zu beschreiben und diese Sätze an ausführbaren Code (Schritt-Definitionen) zu binden.
*   Es ist ideal, wenn du ein **gemeinsames Verständnis** zwischen Produkt, QA und Entwicklung benötigst und **lebendige Dokumentation**, die gleichzeitig als Tests dient.
*   Es ist **kein** Ersatz für Unit-Testing-Frameworks (JUnit/TestNG/Jest/PyTest). Es ergänzt sie, indem es den Fokus auf **akzeptanzkriterienorientierte Tests auf Geschäftsebene** legt.

---

# Kernkomponenten

**1) Gherkin (Klartext-Spezifikationen)**

*   Geschrieben in `.feature`-Dateien.
*   Schlüsselwörter: `Feature`, `Scenario`, `Given/When/Then/And/But`, `Background`, `Scenario Outline` + `Examples`, `@tags`, (und optional `Rule` in neueren Gherkin-Versionen).
*   Natürliche Sprachstile; unterstützt viele Gebietsschemata.

**2) Schritt-Definitionen (Code)**

*   Binden Gherkin-Schritte via **Cucumber Expressions** (oder Regex) an Code.
*   Können Page Objects, API-Clients, Services, DB-Helper etc. aufrufen.

**3) Runner**

*   Startet Cucumber, entdeckt Features/Schritte über Glue-Pfade, Konfiguration und Tags.
*   Auf der JVM läuft man typischerweise über **JUnit** (4 oder 5) oder **TestNG**.

**4) Berichte**

*   Erzeuge HTML/JSON/JUnit-XML; integriere sie in CI-Dashboards und Tools wie **Allure**.

---

# Minimalbeispiel (Java, Maven)

**pom.xml (wichtige Teile)**

```xml
<dependencies>
  <!-- JUnit 5 -->
  <dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.10.2</version>
    <scope>test</scope>
  </dependency>

  <!-- Cucumber JVM + JUnit Platform -->
  <dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-java</artifactId>
    <version>7.18.1</version>
    <scope>test</scope>
  </dependency>
  <dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-junit-platform-engine</artifactId>
    <version>7.18.1</version>
    <scope>test</scope>
  </dependency>
</dependencies>

<build>
  <plugins>
    <plugin>
      <artifactId>maven-surefire-plugin</artifactId>
      <version>3.2.5</version>
      <configuration>
        <!-- run by tag, parallel, etc., if needed -->
      </configuration>
    </plugin>
  </plugins>
</build>
```

**Projektstruktur**

```
src
 └─ test
     ├─ java
     │   └─ com/example/steps/...
     └─ resources
         └─ features/...
```

**Eine Feature-Datei (`src/test/resources/features/login.feature`)**

```gherkin
Feature: Login
  As a registered user
  I want to sign in
  So that I can access my account

  Background:
    Given the application is running

  @smoke
  Scenario: Successful login
    Given I am on the login page
    When I sign in with username "alice" and password "secret"
    Then I should see "Welcome, alice"

  Scenario Outline: Failed login
    Given I am on the login page
    When I sign in with username "<user>" and password "<pass>"
    Then I should see "Invalid credentials"
    Examples:
      | user  | pass     |
      | alice | wrong    |
      | bob   | invalid  |
```

**Schritt-Definitionen (Java, Cucumber Expressions)**

```java
package com.example.steps;

import io.cucumber.java.en.*;
import static org.junit.jupiter.api.Assertions.*;

public class LoginSteps {
  private String page;
  private String message;

  @Given("the application is running")
  public void app_running() {
    // bootstrap test app / start server / reset state
  }

  @Given("I am on the login page")
  public void i_am_on_the_login_page() {
    page = "login";
  }

  @When("I sign in with username {string} and password {string}")
  public void i_sign_in(String user, String pass) {
    // call UI or API; here fake it:
    if ("alice".equals(user) && "secret".equals(pass)) {
      message = "Welcome, alice";
    } else {
      message = "Invalid credentials";
    }
  }

  @Then("I should see {string}")
  public void i_should_see(String expected) {
    assertEquals(expected, message);
  }
}
```

**JUnit 5 Runner (Discovery durch Engine)**

```java
// No explicit runner class needed with JUnit Platform.
// Create a test suite if you want tag filtering:
import org.junit.platform.suite.api.*;

@Suite
@IncludeEngines("cucumber")
@SelectClasspathResource("features")
@ConfigurationParameter(key = "cucumber.glue", value = "com.example.steps")
@ConfigurationParameter(key = "cucumber.plugin", value = "pretty, html:target/cucumber.html, json:target/cucumber.json")
@ExcludeTags("wip") // example
public class RunCucumberTest {}
```

Ausführen:

```bash
mvn -q -Dtest=RunCucumberTest test
```

---

# Gherkin-Grundlagen für den täglichen Gebrauch

*   **Background**: Gemeinsame Vorbereitung einmal pro Szenario (z.B. "Given I'm logged in").
*   **Scenario Outline + Examples**: Datengetriebene Tests ohne Schritt-Kopieren.
*   **Doc Strings**: Mehrzeilige Inhalte (z.B. JSON-Bodies) in Schritten.
*   **Data Tables**: Transformiere eine Tabelle eines Schritts in Objekte oder Maps.
*   **Tags**: Unterteile die Testsuite (`@smoke`, `@api`, `@slow`) für CI-Pipelines.
*   **Rule** (optional): Gruppiere Szenarien nach einer Geschäftsregel für bessere Lesbarkeit.

---

# Cucumber Expressions (benutzerfreundlicher als Regex)

*   Platzhalter wie `{string}`, `{int}`, `{word}`, `{float}`.
*   **Benutzerdefinierte Parametertypen** ermöglichen das Parsen von Domänenobjekten:

```java
import io.cucumber.java.ParameterType;

public class ParameterTypes {
  @ParameterType("USD|CNY|EUR")
  public Currency currency(String code) { return Currency.getInstance(code); }
}
```

Dann verwende: `When I pay 100 {currency}`.

---

# Hooks & Test-Lebenszyklus

*   `@Before`, `@After`, `@BeforeStep`, `@AfterStep` in JVM/JS/Ruby-Varianten.
*   Verwende Hooks für **saubere Setup/Teardown-Prozesse**, Screenshots bei Fehlern, DB-Resets etc.
*   Für Dependency Injection verwende **Spring** (cucumber-spring) oder **PicoContainer**, um Zustand zu teilen:
    *   Mit Spring Boot annotiere Step-Klassen als Beans; verwende `@SpringBootTest` für Wiring und Test Slices nach Bedarf.

---

# Integrationen, die du wahrscheinlich brauchst

*   **Web UI**: Selenium/WebDriver, Playwright. Kapsle sie in **Page Objects** und rufe sie aus Schritten auf.
*   **API**: REST Assured/HTTP-Clients; validiere mit JSON-Assertions.
*   **DB**: Flyway/Liquibase für das Schema, Test-Daten-Loader, eingebettete Datenbanken.
*   **Mocking**: WireMock/Testcontainers für externe Systeme.
*   **Reporting**: Integrierte HTML/JSON-Berichte; **Allure** für umfangreiche Timelines und Anhänge.
*   **Parallel**: JUnit Platform (oder das `cucumber-jvm-parallel-plugin` mit TestNG in älteren Stacks). Halte Szenarien isoliert; vermeide gemeinsamen veränderlichen Zustand.

---

# CI/CD & Skalierung

*   **Tag-basierte Pipelines**: Führe `@smoke` bei PRs aus, täglich `@regression`, Cron-Jobs für `@slow`.
*   **Sharding nach Datei oder Tag** über Agenten für Geschwindigkeit.
*   **Artefakte**: Veröffentliche HTML/JSON/Allure-Berichte und Screenshots/Videos (UI).
*   **Flaky Tests**: Finde die Ursache – löse sie nicht durch "Wiederholen bis es grün wird".

---

# Bewährte Praktiken (erprobt)

*   **Eine Stimme** in Gherkin: Halte die Schritt-Formulierung konsistent; vermeide UI-Geschwätz ("click the blue button") – konzentriere dich auf die **Absicht** ("submit credentials").
*   **Dünne Schritte, dicke Helfer**: Schritt-Code sollte an Page Objects/Services delegieren; halte Logik aus den Schritten heraus.
*   **Stabile Testdaten**: Erzeuge sie via APIs/DB-Fixtures; vermeide Kopplung an produktionsähnliche Zufälligkeit.
*   **Schnelle, unabhängige Szenarien**: Keine Annahmen über die Reihenfolge; sauberer Zustand pro Szenario.
*   **Begrenze die Suite-Größe**: Reserviere Cucumber für **Geschäftslogik**; behalte Unit-Tests in JUnit/TestNG/Jest für Low-Level-Details.

---

# Anti-Patterns, die du vermeiden solltest

*   Cucumber als hübscheren Unit-Test-Runner zu behandeln.
*   Übermäßige Verwendung von `And` mit langen prozeduralen Abfolgen (imperativ, anfällig).
*   Kopplung an CSS-Selektoren oder volatile UI-Details in der Schritt-Formulierung.
*   Riesen-`Backgrounds`, die verbergen, was jedes Szenario tatsächlich braucht.

---

# Kurze Hinweise für andere Sprachen

**JavaScript/TypeScript**

*   Verwende **`@cucumber/cucumber`**.
*   Typische Skripte:

  ```bash
  npm i -D @cucumber/cucumber
  npx cucumber-js --require steps/**/*.ts --publish-quiet
  ```
*   Funktioniert gut mit **Playwright** und **Allure**.

**Python**

*   Verwende **behave** (Cucumber-ähnlich) oder **pytest-bdd**.
*   Struktur und Konzepte sind gleich: Features + Schritte + Fixtures.

**Ruby**

*   Ursprüngliche Cucumber-Implementierung; Idiome spiegeln die JVM- und JS-Versionen wider.

---

# Wann du Cucumber wählen solltest

*   Du möchtest **lebendige Dokumentation**, die von Nicht-Entwicklern gelesen werden kann.
*   Akzeptanzkriterien müssen **ausführbar** und **rückverfolgbar** zu Releases sein.
*   Funktionsübergreifende Teams einigen sich **vor** der Implementierung auf das Verhalten (BDD-Triaden).

Überspringe es (oder verwende es sparsam), wenn das Team das Gherkin nicht pflegen wird oder wenn Tests rein technisch sind, wo Unit/Integration-Tests bereits Klarheit liefern.

---

Wenn du mir deinen Stack verrätst (Spring/Quarkus? REST/UI? Wie deployst du/CI?), kann ich dir ein lauffähiges Cucumber-Gerüst mit Maven/Gradle, empfohlenen Plugins und einer Beispiel-Pipeline skizzieren, die zu deinem Setup passt.