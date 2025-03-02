---
audio: false
generated: true
lang: de
layout: post
title: Eclipse verwenden
translated: true
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass Eclipse effektiv mit IBM Websphere Liberty, Spring, Spring Boot und Maven verwendet werden kann, aber die Einrichtung erfordert spezifische Konfigurationen.
- Forschungen deuten darauf hin, dass die Installation von Spring Tool Suite (STS) und IBM Liberty Developer Tools als Plug-ins in Eclipse für erweiterte Funktionalität vorteilhaft ist.
- Die Beweise sprechen dafür, ein Spring Boot-Projekt mit STS oder Spring Initializr zu erstellen und es dann für die Bereitstellung auf Websphere Liberty zu konfigurieren.

### Einrichtung von Eclipse
Um zu beginnen, laden Sie die "Eclipse IDE for Enterprise Java and Web Developers" von [Eclipse Downloads](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) herunter und installieren Sie sie. Stellen Sie sicher, dass JDK 17 oder neuer installiert ist, was Sie durch Ausführen von `java -version` in Ihrem Terminal überprüfen können.

### Konfiguration für Spring und Spring Boot
Installieren Sie das Spring Tool Suite (STS)-Plug-in, indem Sie in Eclipse zu Hilfe -> Eclipse Marketplace gehen, nach "Spring Tools" suchen und die entsprechende Version installieren. Dies verbessert die Entwicklung von Spring und Spring Boot. Sie können ein neues Spring Boot-Projekt direkt in Eclipse über Datei -> Neu -> Spring Starter Project erstellen, Maven als Build-Tool auswählen und notwendige Abhängigkeiten wie Spring Web hinzufügen.

### Integration mit IBM Websphere Liberty
Installieren Sie die IBM Liberty Developer Tools aus dem Eclipse Marketplace, indem Sie nach "IBM Liberty Developer Tools" suchen und den Installationsanweisungen folgen. Richten Sie einen Websphere Liberty-Server ein, indem Sie zu Fenster -> Einstellungen -> Server -> Laufzeitumgebungen gehen, eine neue Websphere Liberty-Laufzeit hinzufügen und eine Serverinstanz über Datei -> Neu -> Anderes -> Server erstellen. Stellen Sie sicher, dass die server.xml des Servers `<feature>springBoot-2.0</feature>` für die Unterstützung von Spring Boot enthält, wie in den [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html) beschrieben.

### Bereitstellung Ihrer Anwendung
Passen Sie Ihre Spring Boot-Anwendung so an, dass sie `SpringBootServletInitializer` erweitert, anstatt eine Hauptmethode zu verwenden, die einen eingebetteten Server startet, und packen Sie sie als WAR-Datei, indem Sie `<packaging>war</packaging>` in Ihrer pom.xml setzen. Bereitstellen Sie, indem Sie das Projekt mit der rechten Maustaste anklicken, "Als -> Auf Server ausführen" auswählen und Ihren Liberty-Server auswählen. Dies stellt sicher, dass die Anwendung im Web-Container von Liberty läuft.

---

### Umfragehinweis: Umfassender Leitfaden zur Verwendung von Eclipse mit IBM Websphere Liberty, Spring, Spring Boot und Maven

Dieser Leitfaden bietet eine detaillierte Anleitung zur effektiven Verwendung von Eclipse in Kombination mit IBM Websphere Liberty, Spring, Spring Boot und Maven, speziell für Entwickler, die in diesen Ökosystemen arbeiten. Der Prozess umfasst die Einrichtung von Eclipse, die Installation notwendiger Plug-ins, das Erstellen und Konfigurieren von Projekten sowie das Bereitstellen von Anwendungen, mit einem Fokus auf Integration und Best Practices bis zum 27. Februar 2025.

#### Eclipse-Einrichtung und Voraussetzungen
Eclipse dient als robuste IDE für die Java-Entwicklung, insbesondere für Unternehmensanwendungen. Für diese Einrichtung laden Sie die "Eclipse IDE for Enterprise Java and Web Developers" Version 2024-06 herunter, die unter [Eclipse Downloads](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) verfügbar ist. Stellen Sie sicher, dass Ihr System JDK 17 oder neuer hat, was Sie durch Ausführen von `java -version` im Terminal überprüfen können. Diese Version stellt die Kompatibilität mit modernen Spring- und Liberty-Funktionen sicher.

#### Installation wesentlicher Plug-ins
Um Eclipse für die Entwicklung von Spring und Spring Boot zu verbessern, installieren Sie die Spring Tool Suite (STS), das nächste Generationstooling für Spring. Dies erreichen Sie über Hilfe -> Eclipse Marketplace, suchen nach "Spring Tools" und installieren Sie den Eintrag mit der Bezeichnung "Spring Tools (aka Spring IDE und Spring Tool Suite)." Dieses Plug-in, das in [Spring Tools](https://spring.io/tools/) beschrieben ist, bietet weltweit führende Unterstützung für Spring-basierte Anwendungen und integriert sich nahtlos in Eclipse für Funktionen wie Projekt-Erstellung und Debugging.

Für die Integration mit IBM Websphere Liberty installieren Sie die IBM Liberty Developer Tools, die ebenfalls über den Eclipse Marketplace verfügbar sind, indem Sie nach "IBM Liberty Developer Tools" suchen. Dieses Plug-in, das für Eclipse 2024-06 getestet wurde, wie in [IBM Liberty Developer Tools](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools) angegeben, erleichtert das Erstellen und Bereitstellen von Java EE-Anwendungen auf Liberty, mit Unterstützung für Versionen ab 2019-12.

#### Erstellen eines Spring Boot-Projekts
Es gibt zwei Hauptmethoden, um ein Spring Boot-Projekt in Eclipse mit installiertem STS zu erstellen:

1. **Verwendung von Spring Initializr**: Besuchen Sie [Spring Initializr](https://start.spring.io/), wählen Sie Maven als Build-Tool, geben Sie Ihre Projektmetadaten (Gruppe, Artefakt usw.) ein und fügen Sie Abhängigkeiten wie Spring Web hinzu. Generieren Sie das Projekt als ZIP-Datei, entpacken Sie es und importieren Sie es in Eclipse über Datei -> Importieren -> Existierendes Maven-Projekt, indem Sie den entpackten Ordner auswählen.

2. **Direkte Verwendung von STS**: Öffnen Sie Eclipse, gehen Sie zu Datei -> Neu -> Anderes, erweitern Sie Spring Boot und wählen Sie "Spring Starter Project." Folgen Sie dem Assistenten und stellen Sie sicher, dass Maven als Typ ausgewählt ist, und wählen Sie Abhängigkeiten. Diese Methode, wie in [Erstellen eines Spring Boot-Projekts mit Eclipse und Maven](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven) beschrieben, wird bevorzugt für ihre Integration in den Eclipse-Arbeitsbereich.

Beide Methoden stellen sicher, dass ein Maven-basiertes Projekt erstellt wird, das für das Abhängigkeitsmanagement mit Spring Boot entscheidend ist.

#### Konfiguration für die Bereitstellung auf Websphere Liberty
Um auf Websphere Liberty bereitzustellen, passen Sie Ihre Spring Boot-Anwendung so an, dass sie auf dem Web-Container von Liberty läuft, anstatt einen eingebetteten Server zu starten. Dies umfasst:

- Stellen Sie sicher, dass die Hauptanwendungsklasse `SpringBootServletInitializer` erweitert. Zum Beispiel:

  ```java
  @SpringBootApplication
  public class MyApplication extends SpringBootServletInitializer {
      // Keine Hauptmethode; Liberty übernimmt den Start
  }
  ```

- Aktualisieren Sie die pom.xml, um als WAR-Datei zu packen, indem Sie hinzufügen:

  ```xml
  <packaging>war</packaging>
  ```

  Dies ist für die Bereitstellung in einem traditionellen Servlet-Container notwendig, wie in [Bereitstellen von Spring Boot-Anwendungen](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet) angegeben.

Websphere Liberty, insbesondere seine Open-Source-Variante Open Liberty, unterstützt Spring Boot-Anwendungen mit spezifischen Funktionen. Stellen Sie sicher, dass die server.xml des Liberty-Servers `<feature>springBoot-2.0</feature>` für die Unterstützung von Spring Boot 2.x enthält, wie in den [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html) beschrieben. Diese Konfiguration deaktiviert den eingebetteten Web-Container und nutzt stattdessen den von Liberty.

#### Einrichtung und Konfiguration des Websphere Liberty-Servers in Eclipse
Mit den installierten IBM Liberty Developer Tools richten Sie einen Liberty-Server ein:

- Navigieren Sie zu Fenster -> Einstellungen -> Server -> Laufzeitumgebungen, klicken Sie auf "Hinzufügen" und wählen Sie "WebSphere Application Server Liberty." Folgen Sie dem Assistenten, um Ihre Liberty-Installation zu finden, die sich normalerweise in einem Verzeichnis wie `<Liberty_Root>/wlp` befindet, wie in [Liberty und Eclipse](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9) erwähnt.

- Erstellen Sie eine neue Serverinstanz über Datei -> Neu -> Anderes -> Server, wählen Sie "WebSphere Application Server Liberty" und die von Ihnen konfigurierte Laufzeit. Benennen Sie den Server und passen Sie die Einstellungen nach Bedarf an.

- Bearbeiten Sie die server.xml des Servers, die über die Servers-Ansicht zugänglich ist, um notwendige Funktionen hinzuzufügen. Für Spring Boot fügen Sie hinzu:

  ```xml
  <featureManager>
      <feature>springBoot-2.0</feature>
      <!-- Weitere Funktionen wie servlet-3.1 für Web-Unterstützung -->
  </featureManager>
  ```

Diese Einrichtung, die von [IBM WebSphere Liberty](https://www.ibm.com/docs/en/was-liberty/base?topic=liberty-overview) unterstützt wird, stellt die Kompatibilität mit Spring Boot-Anwendungen sicher.

#### Bereitstellen und Ausführen der Anwendung
Um bereitzustellen, klicken Sie mit der rechten Maustaste auf Ihr Projekt im Projekt-Explorer, wählen Sie "Als -> Auf Server ausführen," wählen Sie Ihren Liberty-Server und klicken Sie auf Fertig stellen. Eclipse stellt die WAR-Datei auf dem Liberty-Server bereit, und Sie können die Protokolle in der Konsole-Ansicht überwachen. Stellen Sie sicher, dass der Anwendungskontextpfad in der server.xml korrekt eingestellt ist, normalerweise unter `<webApplication>`-Tags, um auf Ihre Anwendung über die entsprechende URL zuzugreifen, z. B. `http://localhost:9080/yourapp`.

Für das Debugging verwenden Sie die Debug-Perspektive, setzen Sie Haltepunkte nach Bedarf und nutzen Sie die Unterstützung von Liberty für das Remote-Debugging, wie in [Debugging mit Eclipse und Liberty](https://stackoverflow.com/questions/41428156/how-to-debug-web-service-with-eclipse-websphere-liberty) diskutiert.

#### Zusätzliche Überlegungen
- **Packaging-Optionen**: Während WAR für Servlet-Container Standard ist, unterstützt Open Liberty auch JAR-Bereitstellungen, wie in [Konfigurieren und Bereitstellen von Spring Boot auf Open Liberty](https://openliberty.io/docs/latest/deploy-spring-boot.html) zu sehen. Für JAR stellen Sie sicher, dass die Anwendung so konfiguriert ist, dass kein eingebetteter Server startet, was zusätzliche Liberty-Funktionen oder -Konfigurationen erfordern kann.
- **Maven-Integration**: Verwenden Sie Maven für das Abhängigkeitsmanagement und stellen Sie sicher, dass das `liberty-maven-plugin` für die automatisierte Bereitstellung enthalten ist, wie in [IBM Liberty Maven Plugin](https://github.com/WASdev/ci.maven#liberty-maven-plugin) angegeben.
- **Fehlerbehebung**: Wenn Probleme auftreten, überprüfen Sie die Serverprotokolle im `logs`-Verzeichnis unter Ihrer Liberty-Serverinstanz und stellen Sie die Kompatibilität zwischen der Liberty-Version und Spring Boot sicher, da Versionen wie Liberty 8.5.5.9 oder höher ausführbare JARs unterstützen, wie in der [Stack Overflow-Diskussion](https://stackoverflow.com/questions/36132791/how-to-use-websphere-liberty-in-spring-boot-application) erwähnt.

Diese umfassende Einrichtung stellt die effektive Nutzung von Eclipse für die Entwicklung und Bereitstellung von Spring Boot-Anwendungen auf IBM Websphere Liberty sicher, wobei Maven für das Build-Management genutzt wird.

#### Tabelle: Vergleich der Bereitstellungsoptionen

| Bereitstellungstyp | Vorteile                                      | Nachteile                                      | Konfigurationshinweise                          |
|-------------------|-----------------------------------------------|-----------------------------------------------|----------------------------------------------|
| WAR-Datei          | Standard für Servlet-Container, weit verbreitet | Erfordert die Erweiterung von `SpringBootServletInitializer` | Setzen Sie `<packaging>war</packaging>` in der pom.xml  |
| JAR-Datei          | Einfacher für die Entwicklung, unterstützt von Open Liberty | Kann zusätzliche Liberty-Funktionen erfordern   | Stellen Sie sicher, dass kein eingebetteter Server startet, verwenden Sie die springBoot-Funktion |

Diese Tabelle, abgeleitet aus den [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html), hilft bei der Wahl der geeigneten Bereitstellungsstrategie basierend auf den Projektanforderungen.

### Wichtige Zitate
- [Erstellen eines Spring Boot-Projekts mit Eclipse und Maven, Schritt-für-Schritt-Anleitung](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)
- [IBM Liberty Developer Tools, Eclipse-Plug-in für Java EE-Anwendungen](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)
- [Open Liberty Docs, Bereitstellen von Spring Boot-Anwendungen](https://openliberty.io/docs/latest/deploy-spring-boot.html)
- [Spring Tools, Next-Generation-Tooling für die Spring-Entwicklung](https://spring.io/tools/)
- [Eclipse Downloads, Pakete für die Unternehmens-Java-Entwicklung](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers)
- [Liberty und Eclipse, Installieren der Entwicklungsumgebung](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9)
- [Bereitstellen von Spring Boot-Anwendungen, Spring Boot-Referenz](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet)