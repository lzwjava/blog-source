---
audio: false
generated: true
lang: de
layout: post
title: Verwenden von Eclipse
translated: true
type: note
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass Eclipse effektiv mit IBM Websphere Liberty, Spring, Spring Boot und Maven verwendet werden kann, aber das Setup erfordert spezifische Konfigurationen.
- Recherchen legen nahe, Spring Tool Suite (STS) und IBM Liberty Developer Tools als Plug-ins in Eclipse zu installieren, um die Funktionalität zu erweitern.
- Die Hinweise deuten darauf hin, ein Spring Boot-Projekt mit STS oder Spring Initializr zu erstellen und es dann für den Einsatz auf Websphere Liberty zu konfigurieren.

### Einrichtung von Eclipse
Laden Sie zunächst die "Eclipse IDE for Enterprise Java and Web Developers" von [Eclipse Downloads](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) herunter und installieren Sie sie. Stellen Sie sicher, dass JDK 17 oder neuer installiert ist, was Sie überprüfen können, indem Sie `java -version` in Ihrem Terminal ausführen.

### Konfiguration für Spring und Spring Boot
Installieren Sie das Spring Tool Suite (STS) Plug-in, indem Sie in Eclipse zu Hilfe -> Eclipse Marketplace gehen, nach "Spring Tools" suchen und die entsprechende Version installieren. Dies verbessert die Spring- und Spring Boot-Entwicklung. Sie können direkt in Eclipse ein neues Spring Boot-Projekt über Datei -> Neu -> Spring Starter Project erstellen, Maven als Build-Tool auswählen und notwendige Abhängigkeiten wie Spring Web hinzufügen.

### Integration mit IBM Websphere Liberty
Installieren Sie die IBM Liberty Developer Tools aus dem Eclipse Marketplace, indem Sie nach "IBM Liberty Developer Tools" suchen und den Installationsanweisungen folgen. Richten Sie einen Websphere Liberty-Server ein, indem Sie zu Fenster -> Einstellungen -> Server -> Laufzeitumgebungen gehen, eine neue Websphere Liberty-Laufzeitumgebung hinzufügen und eine Serverinstanz über Datei -> Neu -> Andere -> Server erstellen. Stellen Sie sicher, dass die server.xml des Servers `<feature>springBoot-2.0</feature>` für Spring Boot-Unterstützung enthält, wie in den [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html) beschrieben.

### Bereitstellung Ihrer Anwendung
Modifizieren Sie Ihre Spring Boot-Anwendung so, dass sie `SpringBootServletInitializer` erweitert, anstatt eine Hauptmethode zu verwenden, die einen eingebetteten Server startet. Verpacken Sie sie als WAR-Datei, indem Sie `<packaging>war</packaging>` in Ihrer pom.xml setzen. Stellen Sie sie bereit, indem Sie mit der rechten Maustaste auf das Projekt klicken, "Run As -> Run on Server" auswählen und Ihren Liberty-Server wählen. Dies stellt sicher, dass die Anwendung im Web-Container von Liberty läuft.

---

### Umfragehinweis: Umfassende Anleitung zur Verwendung von Eclipse mit IBM Websphere Liberty, Spring, Spring Boot und Maven

Diese Anleitung bietet eine detaillierte Schritt-für-Schritt-Anleitung zur effektiven Verwendung von Eclipse in Verbindung mit IBM Websphere Liberty, Spring, Spring Boot und Maven, zugeschnitten auf Entwickler, die in diesen Ökosystemen arbeiten. Der Prozess umfasst die Einrichtung von Eclipse, die Installation notwendiger Plug-ins, die Erstellung und Konfiguration von Projekten sowie die Bereitstellung von Anwendungen, mit einem Fokus auf Integration und Best Practices Stand 27. Februar 2025.

#### Eclipse-Setup und Voraussetzungen
Eclipse dient als robuste IDE für die Java-Entwicklung, insbesondere für Enterprise-Anwendungen. Laden Sie für dieses Setup die Version 2024-06 der "Eclipse IDE for Enterprise Java and Web Developers" von [Eclipse Downloads](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) herunter. Stellen Sie sicher, dass Ihr System JDK 17 oder neuer hat, was Sie durch Ausführen von `java -version` im Terminal überprüfen können. Diese Version gewährleistet Kompatibilität mit modernen Spring- und Liberty-Funktionen.

#### Installation wesentlicher Plug-ins
Um Eclipse für die Spring- und Spring Boot-Entwicklung zu erweitern, installieren Sie die Spring Tool Suite (STS), die nächste Generation der Spring-Tooling. Greifen Sie darauf über Hilfe -> Eclipse Marketplace zu, suchen Sie nach "Spring Tools" und installieren Sie den Eintrag "Spring Tools (aka Spring IDE and Spring Tool Suite)". Dieses Plug-in, detailliert auf [Spring Tools](https://spring.io/tools/), bietet erstklassige Unterstützung für Spring-basierte Anwendungen und integriert sich nahtlos in Eclipse für Funktionen wie Projekterstellung und Debugging.

Für die IBM Websphere Liberty-Integration installieren Sie die IBM Liberty Developer Tools, ebenfalls erhältlich über den Eclipse Marketplace durch Suche nach "IBM Liberty Developer Tools". Dieses Plug-in, getestet für Eclipse 2024-06, wie in [IBM Liberty Developer Tools](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools) vermerkt, erleichtert das Erstellen und Bereitstellen von Java EE-Anwendungen für Liberty, mit Unterstützung für Versionen bis zurück zu 2019-12.

#### Erstellung eines Spring Boot-Projekts
Es gibt zwei primäre Methoden, um ein Spring Boot-Projekt in Eclipse mit installiertem STS zu erstellen:

1. **Verwendung von Spring Initializr**: Besuchen Sie [Spring Initializr](https://start.spring.io/), wählen Sie Maven als Build-Tool, wählen Sie Ihre Projektmetadaten (Group, Artifact, etc.) und fügen Sie Abhängigkeiten wie Spring Web hinzu. Generieren Sie das Projekt als ZIP-Datei, extrahieren Sie es und importieren Sie es in Eclipse über Datei -> Importieren -> Vorhandenes Maven-Projekt, wählen Sie den extrahierten Ordner aus.

2. **Direkte Verwendung von STS**: Öffnen Sie Eclipse, gehen Sie zu Datei -> Neu -> Andere, erweitern Sie Spring Boot und wählen Sie "Spring Starter Project". Folgen Sie dem Assistenten, stellen Sie sicher, dass Maven als Typ gewählt ist, und wählen Sie Abhängigkeiten. Diese Methode, beschrieben in [Creating Spring Boot Project with Eclipse and Maven](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven), wird aufgrund ihrer Integration in den Eclipse-Arbeitsbereich bevorzugt.

Beide Methoden stellen ein Maven-basiertes Projekt sicher, was für das Dependency Management mit Spring Boot entscheidend ist.

#### Konfiguration für die Bereitstellung auf Websphere Liberty
Um auf Websphere Liberty bereitzustellen, modifizieren Sie Ihre Spring Boot-Anwendung so, dass sie im Web-Container von Liberty läuft, anstatt einen eingebetteten Server zu starten. Dies beinhaltet:

- Sicherstellen, dass die Hauptanwendungsklasse `SpringBootServletInitializer` erweitert. Zum Beispiel:

  ```java
  @SpringBootApplication
  public class MyApplication extends SpringBootServletInitializer {
      // Keine Hauptmethode; Liberty übernimmt den Start
  }
  ```

- Aktualisieren der pom.xml, um als WAR-Datei zu verpacken, durch Hinzufügen von:

  ```xml
  <packaging>war</packaging>
  ```

  Dies ist für die traditionelle Bereitstellung in Servlet-Containern notwendig, wie in [Deploying Spring Boot Applications](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet) vermerkt.

Websphere Liberty, insbesondere seine Open-Source-Variante Open Liberty, unterstützt Spring Boot-Anwendungen mit spezifischen Features. Stellen Sie sicher, dass die server.xml des Liberty-Servers das `<feature>springBoot-2.0</feature>` für Spring Boot 2.x-Unterstützung enthält, wie in den [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html) detailliert beschrieben. Diese Konfiguration deaktiviert den eingebetteten Web-Container und nutzt stattdessen den von Liberty.

#### Einrichtung und Konfiguration des Websphere Liberty-Servers in Eclipse
Mit installierten IBM Liberty Developer Tools richten Sie einen Liberty-Server ein:

- Navigieren Sie zu Fenster -> Einstellungen -> Server -> Laufzeitumgebungen, klicken Sie auf "Hinzufügen" und wählen Sie "WebSphere Application Server Liberty". Folgen Sie dem Assistenten, um Ihre Liberty-Installation zu lokalisieren, typischerweise in einem Verzeichnis wie `<Liberty_Root>/wlp`, wie in [Liberty and Eclipse](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9) erwähnt.

- Erstellen Sie eine neue Serverinstanz über Datei -> Neu -> Andere -> Server, wählen Sie "WebSphere Application Server Liberty" und die von Ihnen konfigurierte Laufzeitumgebung. Benennen Sie den Server und passen Sie die Einstellungen nach Bedarf an.

- Bearbeiten Sie die server.xml des Servers, zugänglich über die Server-Ansicht, um notwendige Features einzubeziehen. Für Spring Boot fügen Sie hinzu:

  ```xml
  <featureManager>
      <feature>springBoot-2.0</feature>
      <!-- Andere Features wie servlet-3.1 für Web-Unterstützung -->
  </featureManager>
  ```

Dieses Setup, unterstützt von [IBM WebSphere Liberty](https://www.ibm.com/docs/en/was-liberty/base?topic=liberty-overview), gewährleistet Kompatibilität mit Spring Boot-Anwendungen.

#### Bereitstellen und Ausführen der Anwendung
Um bereitzustellen, klicken Sie mit der rechten Maustaste auf Ihr Projekt im Projekt-Explorer, wählen Sie "Run As -> Run on Server", wählen Sie Ihren Liberty-Server und klicken Sie auf Fertig. Eclipse wird die WAR-Datei auf dem Liberty-Server bereitstellen, und Sie können die Logs in der Konsolen-Ansicht überwachen. Stellen Sie sicher, dass der Anwendungskontext-Root in der server.xml korrekt gesetzt ist, typischerweise unter `<webApplication>`-Tags, um auf Ihre Anwendung über die entsprechende URL zuzugreifen, z.B. `http://localhost:9080/yourapp`.

Für das Debugging verwenden Sie die Debug-Perspektive, setzen Sie Breakpoints nach Bedarf und nutzen Sie die Unterstützung von Liberty für Remote-Debugging, wie in [Debugging with Eclipse and Liberty](https://stackoverflow.com/questions/41428156/how-to-debug-web-service-with-eclipse-websphere-liberty) diskutiert.

#### Zusätzliche Überlegungen
- **Verpackungsoptionen**: Während WAR für Servlet-Container Standard ist, unterstützt Open Liberty auch JAR-Bereitstellungen, wie in [Configure and Deploy Spring Boot to Open Liberty](https://openliberty.io/docs/latest/deploy-spring-boot.html) zu sehen. Für JAR stellen Sie sicher, dass die Anwendung so konfiguriert ist, dass sie keinen eingebetteten Server startet, was zusätzliche Liberty-Features oder Konfigurationen erfordern kann.
- **Maven-Integration**: Verwenden Sie Maven für das Dependency Management und stellen Sie sicher, dass das `liberty-maven-plugin` für die automatisierte Bereitstellung enthalten ist, wie in [IBM Liberty Maven Plugin](https://github.com/WASdev/ci.maven#liberty-maven-plugin) vermerkt.
- **Fehlerbehebung**: Wenn Probleme auftreten, überprüfen Sie die Server-Logs im `logs`-Verzeichnis unter Ihrer Liberty-Serverinstanz und stellen Sie die Kompatibilität zwischen der Liberty-Version und Spring Boot sicher, da Versionen wie Liberty 8.5.5.9 oder höher ausführbare JARs unterstützen, laut [Stack Overflow Discussion](https://stackoverflow.com/questions/36132791/how-to-use-websphere-liberty-in-spring-boot-application).

Dieses umfassende Setup gewährleistet die effektive Nutzung von Eclipse für die Entwicklung und Bereitstellung von Spring Boot-Anwendungen auf IBM Websphere Liberty unter Nutzung von Maven für das Build-Management.

#### Tabelle: Vergleich der Bereitstellungsoptionen

| Bereitstellungstyp | Vorteile                                      | Nachteile                                      | Konfigurationshinweise                          |
|-----------------|-------------------------------------------|-------------------------------------------|----------------------------------------------|
| WAR-Datei        | Standard für Servlet-Container, weitgehend unterstützt | Erfordert Erweiterung von `SpringBootServletInitializer` | Setze `<packaging>war</packaging>` in pom.xml  |
| JAR-Datei        | Einfacher für die Entwicklung, unterstützt von Open Liberty | Kann zusätzliche Liberty-Features erfordern   | Stelle sicher, dass kein eingebetteter Server startet, verwende springBoot-Feature |

Diese Tabelle, abgeleitet aus [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html), hilft bei der Auswahl der geeigneten Bereitstellungsstrategie basierend auf den Projektanforderungen.

### Wichtige Zitate
- [Creating Spring Boot Project with Eclipse and Maven, step-by-step guide](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)
- [IBM Liberty Developer Tools, Eclipse plugin for Java EE applications](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)
- [Open Liberty Docs, deploying Spring Boot applications](https://openliberty.io/docs/latest/deploy-spring-boot.html)
- [Spring Tools, next generation tooling for Spring development](https://spring.io/tools/)
- [Eclipse Downloads, packages for enterprise Java development](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers)
- [Liberty and Eclipse, installing development environment](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9)
- [Deploying Spring Boot Applications, Spring Boot reference](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet)