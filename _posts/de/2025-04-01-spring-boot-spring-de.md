---
audio: false
generated: true
lang: de
layout: post
title: Spring Boot vs Spring Framework
translated: true
type: note
---

Lassen Sie uns die Unterschiede zwischen **Spring Boot** und **Spring** (oft als Spring Framework bezeichnet) näher betrachten. Obwohl sie eng miteinander verbunden sind, erfüllen sie unterschiedliche Zwecke im Java-Ökosystem. Ich werde die Unterschiede in Schlüsseldimensionen wie Zweck, Konfiguration, Entwicklungsgeschwindigkeit und Anwendungsfälle aufschlüsseln.

### 1. **Überblick und Zweck**
- **Spring Framework**: Das ursprüngliche, grundlegende Framework für Java-Anwendungen. Es wurde 2002 eingeführt und bietet ein umfassendes Programmier- und Konfigurationsmodell zur Vereinfachung der Enterprise-Java-Entwicklung. Es ist ein breites Ökosystem mit Modulen wie Spring MVC, Spring Security und Spring Data, das sich auf Dependency Injection und Modularität konzentriert.
- **Spring Boot**: Eine Schicht, die auf dem Spring Framework aufbaut und 2014 eingeführt wurde. Es wurde entwickelt, um die Spring-Entwicklung durch eine "einfach ausführen"-Erfahrung mit minimaler Konfiguration zu vereinfachen. Man kann es sich als Spring mit integrierten "Batterien" vorstellen – optimiert für schnelle Anwendungsentwicklung und Produktionsreife.

### 2. **Konfiguration**
- **Spring**: Erfordert manuelle Konfiguration. Sie definieren Beans, richten Abhängigkeiten ein und konfigurieren Komponenten (z.B. über XML-Dateien oder Java-Annotationen). Dies gibt Ihnen feinkörnige Kontrolle, kann aber zeitaufwändig und fehleranfällig sein, besonders für Anfänger.
- **Spring Boot**: Betont **Auto-Konfiguration**. Es verwendet sinnvolle Standardeinstellungen basierend auf den von Ihnen eingebundenen Abhängigkeiten (z.B. richtet das Hinzufügen von Spring Web automatisch einen Webserver wie Tomcat ein). Sie können diese Standardeinstellungen bei Bedarf überschreiben, aber das Ziel ist die Minimierung des Setups.

### 3. **Entwicklungsgeschwindigkeit**
- **Spring**: Langsamer im Start, weil Sie alles manuell verdrahten müssen – Abhängigkeiten, Server, Datenbankverbindungen usw. Es ist leistungsstark, erfordert aber mehr Aufwand, um eine einfache App zum Laufen zu bringen.
- **Spring Boot**: Schnellere Entwicklung dank seiner "Konvention vor Konfiguration"-Philosophie. Beispielsweise kann eine einfache REST-API in wenigen Minuten mit ein paar Codezeilen erstellt werden, dank eingebetteter Server und Starter-Abhängigkeiten.

### 4. **Abhängigkeitsverwaltung**
- **Spring**: Basiert darauf, dass Sie Abhängigkeiten manuell über Maven oder Gradle verwalten. Sie wählen die Spring-Module (z.B. Spring Core, Spring MVC) und Bibliotheken von Drittanbietern aus, was zu Versionskonflikten führen kann, wenn nicht sorgfältig vorgegangen wird.
- **Spring Boot**: Bietet **Starter-Abhängigkeiten** (z.B. `spring-boot-starter-web`, `spring-boot-starter-data-jpa`), die kompatible Versionen von Bibliotheken bündeln. Dies reduziert den Aufwand für die Abhängigkeitsverwaltung und gewährleistet Konsistenz.

### 5. **Eingebetteter Server**
- **Spring**: Beinhaltet keinen eingebetteten Server. Sie deployen Spring-Anwendungen typischerweise auf einem externen Server wie Tomcat, JBoss oder WebSphere, was zusätzliches Setup erfordert.
- **Spring Boot**: Wird standardmäßig mit eingebetteten Servern (Tomcat, Jetty oder Undertow) ausgeliefert. Sie können Ihre App als eigenständige JAR-Datei mit `java -jar` ausführen, was das Deployment einfacher und portabler macht (z.B. für Docker).

### 6. **Produktionsreife**
- **Spring**: Bietet Werkzeuge wie Spring Security und Spring Transaction Management, aber Sie müssen Monitoring, Health Checks und Metriken selbst konfigurieren.
- **Spring Boot**: Beinhaltet **Spring Boot Actuator**, der sofort einsatzbereite, produktionsreife Funktionen hinzufügt – Health-Endpoints, Metriken, Logging und mehr. Es ist so konzipiert, dass es mit minimalen Anpassungen deployment-bereit ist.

### 7. **Flexibilität vs. Einfachheit**
- **Spring**: Sehr flexibel und anpassbar. Ideal, wenn Sie volle Kontrolle über jeden Aspekt Ihrer Anwendung benötigen, aber dies geht auf Kosten der Komplexität.
- **Spring Boot**: Tauscht etwas Flexibilität gegen Einfachheit ein. Es ist opiniert, was bedeutet, dass es Konventionen (z.B. Projektstruktur, Standardeinstellungen) durchsetzt, um die Entwicklung zu optimieren, obwohl Sie es dennoch anpassen können.

### 8. **Anwendungsfälle**
- **Spring**: Am besten für komplexe, groß angelegte Enterprise-Anwendungen geeignet, bei denen Sie verschiedene Komponenten oder Legacy-Systeme integrieren müssen und der Setup-Aufwand in Kauf genommen wird.
- **Spring Boot**: Perfekt für moderne, schnelle Entwicklungsszenarien – Microservices, REST-APIs, eigenständige Apps oder Prototypen, bei denen Geschwindigkeit und Einfachheit wichtig sind.

### Beispielvergleich
- **Spring (Grundlegendes Setup)**:
  ```java
  // Manuelle Konfiguration mit Spring MVC
  @Configuration
  @EnableWebMvc
  public class WebConfig implements WebMvcConfigurer {
      @Bean
      public ViewResolver viewResolver() {
          InternalResourceViewResolver resolver = new InternalResourceViewResolver();
          resolver.setPrefix("/WEB-INF/views/");
          resolver.setSuffix(".jsp");
          return resolver;
      }
  }
  ```
  Zusätzlich müssten Sie eine `web.xml` oder einen Servlet-Initialisierer konfigurieren und auf einem externen Server deployen.

- **Spring Boot (Äquivalent)**:
  ```java
  @RestController
  public class HelloController {
      @GetMapping("/hello")
      public String sayHello() {
          return "Hello, World!";
      }
  }
  ```
  Fügen Sie `spring-boot-starter-web` zu Ihrer `pom.xml` hinzu, und Sie sind fertig – führen Sie es mit einem eingebetteten Server aus.

### Zusammenfassungstabelle

| Aspekt              | Spring Framework            | Spring Boot                 |
|---------------------|-----------------------------|-----------------------------|
| **Zweck**           | Kern-Framework für Java     | Vereinfachte Spring-Nutzung |
| **Konfiguration**   | Manuell (XML/Annotationen)  | Auto-konfiguriert           |
| **Server**          | Extern (z.B. Tomcat)        | Eingebettet (Tomcat, Jetty) |
| **Abhängigkeiten**  | Manuelle Verwaltung         | Starter vereinfachen es     |
| **Geschwindigkeit** | Langsamer im Start          | Schnelles Setup & Prototyping |
| **Flexibilität**    | Hoch, voll anpassbar        | Opiniert, weniger flexibel  |
| **Am besten für**   | Komplexe Enterprise-Apps    | Microservices, schnelle Apps|

### Fazit
- **Spring** ist die Grundlage – leistungsstark, flexibel und geeignet für Szenarien, in denen Sie totale Kontrolle benötigen oder mit Legacy-Systemen arbeiten.
- **Spring Boot** ist Spring made easy – ideal für moderne, schnelle Entwicklung mit Fokus auf Microservices und eigenständige Apps.

Wenn Sie ein neues Projekt starten und Geschwindigkeit schätzen, wählen Sie Spring Boot. Wenn Sie ein komplexes System warten oder tiefgehende Anpassungen benötigen, könnte Spring die bessere Basis sein. Soll ich irgendeinen Teil näher beleuchten?