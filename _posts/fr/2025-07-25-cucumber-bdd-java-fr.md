---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide BDD Cucumber pour les Développeurs Java
translated: true
type: note
---

Voici une introduction pratique et complète à **Cucumber** : ce que c'est, pourquoi les équipes l'utilisent et comment devenir productif avec celui-ci en Java (avec des notes rapides pour les utilisateurs JS/Python).

---

# Qu'est-ce que Cucumber (et ce qu'il n'est pas)

*   **Cucumber** est un framework de test **BDD (Behavior-Driven Development)**. Il vous permet de décrire un comportement en langage clair (Gherkin) et de lier ces phrases à du code exécutable (définitions d'étapes).
*   C'est idéal lorsque vous voulez une **compréhension partagée** entre le produit, les QA et l'ingénierie, et une **documentation vivante** qui fait aussi office de tests.
*   Ce **n'est pas** un remplacement pour les frameworks de tests unitaires (JUnit/TestNG/Jest/PyTest). Il les complète en se concentrant sur les **tests d'acceptation au niveau métier**.

---

# Éléments principaux

**1) Gherkin (spécifications en texte clair)**

*   Écrit dans des fichiers `.feature`.
*   Mots-clés : `Feature`, `Scenario`, `Given/When/Then/And/But`, `Background`, `Scenario Outline` + `Examples`, `@tags`, (et optionnellement `Rule` dans les versions récentes de Gherkin).
*   Style langage naturel ; supporte de nombreuses locales.

**2) Définitions d'étapes (code)**

*   Lie les étapes Gherkin au code via **Cucumber Expressions** (ou regex).
*   Peut appeler des Page Objects, des clients API, des services, des helpers de base de données, etc.

**3) Runner**

*   Démarre Cucumber, découvre les features/étapes par les chemins de glue, la configuration et les tags.
*   Sur la JVM, vous exécutez typiquement via **JUnit** (4 ou 5) ou **TestNG**.

**4) Rapports**

*   Génère du HTML/JSON/XML JUnit ; s'intègre avec les tableaux de bord CI et des outils comme **Allure**.

---

# Exemple minimal (Java, Maven)

**pom.xml (parties clés)**

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
        <!-- exécuter par tag, en parallèle, etc., si besoin -->
      </configuration>
    </plugin>
  </plugins>
</build>
```

**Structure du projet**

```
src
 └─ test
     ├─ java
     │   └─ com/example/steps/...
     └─ resources
         └─ features/...
```

**Un fichier feature (`src/test/resources/features/login.feature`)**

```gherkin
Feature: Connexion
  En tant qu'utilisateur enregistré
  Je veux me connecter
  Afin de pouvoir accéder à mon compte

  Background:
    Étant donné que l'application est en cours d'exécution

  @smoke
  Scenario: Connexion réussie
    Étant donné que je suis sur la page de connexion
    Quand je me connecte avec le nom d'utilisateur "alice" et le mot de passe "secret"
    Alors je devrais voir "Bienvenue, alice"

  Scenario Outline: Échec de connexion
    Étant donné que je suis sur la page de connexion
    Quand je me connecte avec le nom d'utilisateur "<user>" et le mot de passe "<pass>"
    Alors je devrais voir "Identifiants invalides"
    Examples:
      | user  | pass     |
      | alice | wrong    |
      | bob   | invalid  |
```

**Définitions d'étapes (Java, Cucumber Expressions)**

```java
package com.example.steps;

import io.cucumber.java.en.*;
import static org.junit.jupiter.api.Assertions.*;

public class LoginSteps {
  private String page;
  private String message;

  @Given("the application is running")
  public void app_running() {
    // initialiser l'application de test / démarrer le serveur / réinitialiser l'état
  }

  @Given("I am on the login page")
  public void i_am_on_the_login_page() {
    page = "login";
  }

  @When("I sign in with username {string} and password {string}")
  public void i_sign_in(String user, String pass) {
    // appeler l'UI ou l'API ; ici on simule :
    if ("alice".equals(user) && "secret".equals(pass)) {
      message = "Bienvenue, alice";
    } else {
      message = "Identifiants invalides";
    }
  }

  @Then("I should see {string}")
  public void i_should_see(String expected) {
    assertEquals(expected, message);
  }
}
```

**Runner JUnit 5 (découverte par le moteur)**

```java
// Aucune classe de runner explicite nécessaire avec JUnit Platform.
// Créez une suite de tests si vous voulez du filtrage par tag :
import org.junit.platform.suite.api.*;

@Suite
@IncludeEngines("cucumber")
@SelectClasspathResource("features")
@ConfigurationParameter(key = "cucumber.glue", value = "com.example.steps")
@ConfigurationParameter(key = "cucumber.plugin", value = "pretty, html:target/cucumber.html, json:target/cucumber.json")
@ExcludeTags("wip") // exemple
public class RunCucumberTest {}
```

Exécution :

```bash
mvn -q -Dtest=RunCucumberTest test
```

---

# Les essentiels de Gherkin que vous utiliserez quotidiennement

*   **Background** : configuration commune une fois par scénario (ex: "Étant donné que je suis connecté").
*   **Scenario Outline + Examples** : tests pilotés par les données sans copier-coller les étapes.
*   **Doc Strings** : charges utiles multilignes (ex: corps JSON) dans les étapes.
*   **Data Tables** : transformer un tableau d'une étape en objets ou maps.
*   **Tags** : découper la suite (`@smoke`, `@api`, `@slow`) pour les pipelines CI.
*   **Rule** (optionnel) : grouper les scénarios par règle métier pour la lisibilité.

---

# Cucumber Expressions (plus conviviales que les regex)

*   Placeholders comme `{string}`, `{int}`, `{word}`, `{float}`.
*   Les **types de paramètres personnalisés** vous permettent d'analyser des objets du domaine :

```java
import io.cucumber.java.ParameterType;

public class ParameterTypes {
  @ParameterType("USD|CNY|EUR")
  public Currency currency(String code) { return Currency.getInstance(code); }
}
```

Puis utilisez : `When I pay 100 {currency}`.

---

# Hooks & cycle de vie des tests

*   `@Before`, `@After`, `@BeforeStep`, `@AfterStep` dans les variantes JVM/JS/Ruby.
*   Utilisez les hooks pour une **configuration/nettoyage propres**, des captures d'écran en cas d'échec, des réinitialisations de base de données, etc.
*   Pour l'injection de dépendances, utilisez **Spring** (cucumber-spring) ou **PicoContainer** pour partager l'état :
    *   Avec Spring Boot, annotez les classes d'étapes comme des beans ; utilisez `@SpringBootTest` pour le wiring et les test slices si nécessaire.

---

# Intégrations que vous voudrez probablement

*   **Web UI** : Selenium/WebDriver, Playwright. Encapsulez dans des **Page Objects** et appelez depuis les étapes.
*   **API** : REST Assured/clients HTTP ; validez avec des assertions JSON.
*   **DB** : Flyway/Liquibase pour le schéma, chargeurs de données de test, bases de données embarquées.
*   **Mocking** : WireMock/Testcontainers pour les systèmes externes.
*   **Reporting** : HTML/JSON intégrés ; **Allure** pour des chronologies riches et des pièces jointes.
*   **Parallélisme** : JUnit Platform (ou le `cucumber-jvm-parallel-plugin` avec TestNG dans les stacks plus anciennes). Gardez les scénarios isolés ; évitez l'état mutable partagé.

---

# CI/CD & mise à l'échelle

*   **Pipelines basés sur les tags** : exécutez `@smoke` sur les PRs, `@regression` quotidien, `@slow` en cron.
*   **Répartissez par fichier ou tag** entre les agents pour la vitesse.
*   **Artifacts** : publiez HTML/JSON/Allure et les captures d'écran/vidéos (UI).
*   **Tests instables** : trouvez leur cause racine—ne comptez pas sur les "nouvelles tentatives pour passer au vert".

---

# Bonnes pratiques (éprouvées)

*   **Une seule voix** dans Gherkin : gardez une phraséologie d'étape cohérente ; évitez le bavardage UI ("cliquer sur le bouton bleu")—concentrez-vous sur **l'intention** ("soumettre les identifiants").
*   **Étapes légères, helpers épais** : le code d'étape doit déléguer aux page objects/services ; gardez la logique hors des étapes.
*   **Données de test stables** : initialisez via APIs/fixtures de base de données ; évitez le couplage avec un aléatoire de type production.
*   **Scénarios rapides et indépendants** : pas de présupposé d'ordre ; état propre par scénario.
*   **Limitez la taille de la suite** : réservez Cucumber pour le **comportement métier** ; gardez les tests unitaires dans JUnit/TestNG/Jest pour les détails de bas niveau.

---

# Anti-patterns à éviter

*   Traiter Cucumber comme un runner de tests unitaires plus joli.
*   Abuser de `And` avec de longues séquences procédurales (impératif, fragile).
*   Coupler aux sélecteurs CSS ou aux détails UI volatils dans la formulation des étapes.
*   Les Backgrounds géants qui cachent ce dont chaque scénario a réellement besoin.

---

# Notes rapides pour les autres langages

**JavaScript/TypeScript**

*   Utilisez **`@cucumber/cucumber`**.
*   Scripts typiques :

  ```bash
  npm i -D @cucumber/cucumber
  npx cucumber-js --require steps/**/*.ts --publish-quiet
  ```
*   Fonctionne bien avec **Playwright** et **Allure**.

**Python**

*   Utilisez **behave** (similaire à Cucumber) ou **pytest-bdd**.
*   La structure et les concepts sont les mêmes : features + steps + fixtures.

**Ruby**

*   Implémentation originale de Cucumber ; les idiomes reflètent les versions JVM et JS.

---

# Quand choisir Cucumber

*   Vous voulez une **documentation vivante** lisible par des non-ingénieurs.
*   Les critères d'acceptation doivent être **exécutables** et **traçables** jusqu'aux releases.
*   Les équipes cross-fonctionnelles s'accordent sur le comportement **avant** l'implémentation (triades BDD).

Évitez-le (ou utilisez-le avec parcimonie) si l'équipe ne maintiendra pas le Gherkin, ou si les tests sont purement techniques là où les tests unitaires/d'intégration apportent déjà de la clarté.

---

Si vous me dites votre stack (Spring/Quarkus ? REST/UI ? comment vous déployez/CI ?), je peux esquisser un squelette Cucumber prêt à l'exécution avec Maven/Gradle, les plugins recommandés et un exemple de pipeline qui correspond à votre configuration.