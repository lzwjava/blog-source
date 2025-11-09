---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Hot Deployment in WebSphere WAS
translated: true
type: note
---

### Verständnis von Hot Deployment und Hotswap in WebSphere Application Server (WAS)

Hot Deployment (auch bekannt als Hot Reloading oder Hot Swapping) ist eine Entwicklungstechnik, mit der Sie Änderungen an Ihrer Anwendung – wie Code, Konfiguration oder Ressourcen – aktualisieren und bereitstellen können, ohne einen vollständigen Neustart des Application Servers zu benötigen. Dies ist besonders wertvoll während iterativer Entwicklungszyklen, in denen häufige Codeänderungen (z.B. das Beheben von Fehlern, das Anpassen von Logik oder das Aktualisieren von UI-Elementen) ansonsten durch lange Serverstartzeiten verlangsamt würden, insbesondere in Unternehmensumgebungen wie dem IBM WebSphere Application Server (WAS). Das Neustarten einer WAS-Instanz kann Minuten oder sogar länger für große Anwendungen dauern, was Arbeitsabläufe und Tests unterbricht.

Der von Ihnen bereitgestellte Ausschnitt konzentriert sich auf praktische Strategien zur Erzielung schnellerer Iterationen in WAS, mit Schwerpunkt auf "explodierten" WAR-Deployments und Tools für erweitertes Hot Swapping. Ich werde dies Schritt für Schritt aufschlüsseln, die Konzepte erklären, wie sie funktionieren, ihre Grenzen und Implementierungstipps geben.

#### 1. Bereitstellen als "explodierte" WAR (Entpacktes Deployment)
Eine WAR-Datei (Web Application Archive) ist im Wesentlichen ein gezipptes Bündel, das die Ressourcen Ihrer Webanwendung enthält: JSPs, Servlets, Java-Klassen, statische Dateien (HTML/CSS/JS), Bibliotheken (JARs) und Konfigurationsdateien (z.B. web.xml). Standardmäßig werden WARs als **gepackte** (gezippte) Dateien bereitgestellt, die WAS als unveränderlich behandelt – jede Änderung erfordert das erneute Verpacken und Bereitstellen des gesamten Archivs.

Eine **explodierte WAR** bezieht sich darauf, die WAR-Datei vor der Bereitstellung in eine Verzeichnisstruktur zu entpacken (entzippen). Dies ermöglicht es, einzelne Dateien oder Unterverzeichnisse direkt auf dem Dateisystem des Servers zu ändern, ohne das gesamte Archiv anzufassen.

**Warum es schnellere Iterationen ermöglicht:**
- **Dateibasierte Updates:** Sie können eine einzelne JSP- oder Java-Klassendatei bearbeiten, und WAS kann nur diese Komponente erkennen und neu laden.
- **Kein erneutes Verpacken:** Vermeidet den Overhead des wiederholten Zippens/Entzippens großer WAR-Dateien.
- **Synergie mit Hot Reloading:** Erleichtert es dem Server, geänderte Dateien zu überwachen und zu aktualisieren.

**Wie man eine explodierte WAR in WAS bereitstellt:**
- **Verwenden der Admin Console:**
  1. Melden Sie sich bei der WAS Integrated Solutions Console an (typischerweise unter `http://localhost:9060/ibm/console`).
  2. Navigieren Sie zu **Applications > New Application > New Enterprise Application**.
  3. Zeigen Sie anstelle der Auswahl einer gepackten WAR-Datei auf das Stammverzeichnis Ihrer entpackten WAR (z.B. `/pfad/zu/meineapp.war/` – beachten Sie den nachgestellten Schrägstrich, um anzuzeigen, dass es sich um ein Verzeichnis handelt).
  4. Schließen Sie den Bereitstellungs-Assistenten ab und stellen Sie sicher, dass "Deploy Web services" und andere Optionen Ihrer App entsprechen.
- **Verwenden von wsadmin (Skript-Tool):**
  ```bash
  wsadmin.sh -c "AdminApp.install('/pfad/zu/meineapp', '[ -MapWebModToVH [[meineapp .* default_host.* virtual_host ]]]')"
  ```
  Ersetzen Sie `/pfad/zu/meineapp` durch Ihr explodiertes Verzeichnis.
- **Entwicklungsserver (z.B. Liberty Profile):** Für leichtere Tests verwenden Sie Open Liberty (eine WAS-Variante) mit `server start` und platzieren Sie Ihre explodierte App im `dropins`-Ordner für automatische Bereitstellung.

**Bewährte Verfahren:**
- Verwenden Sie ein Source-Control-Tool (z.B. Git), um Änderungen von Ihrer IDE mit dem explodierten Verzeichnis zu synchronisieren.
- Überwachen Sie den Speicherplatz, da explodierte Deployments mehr Speicher verbrauchen.
- Verwenden Sie in der Produktion gepackte WARs aus Sicherheitsgründen und für Konsistenz – Hot Deployment ist hauptsächlich für Dev/Test.

Sobald explodiert bereitgestellt, können die eingebauten Mechanismen von WAS für partielles Hot Reloading greifen.

#### 2. Eingebaute Hot-Reload-Unterstützung von WAS
WAS bietet native Unterstützung für das Hot Reloading bestimmter Komponenten ohne vollständigen Neustart, aber diese ist begrenzt. Dies beruht auf dem **File Polling**-Mechanismus des Servers, bei dem WAS periodisch das explodierte Bereitstellungsverzeichnis auf Änderungen scannt (konfigurierbar über JVM-Args wie `-DwasStatusCheckInterval=5` für 5-Sekunden-Checks).

**Was WAS out-of-the-box unterstützt:**
- **JSPs (JavaServer Pages):**
  - JSPs werden beim ersten Zugriff dynamisch in Servlets kompiliert. Wenn Sie eine JSP-Datei in einer explodierten WAR ändern, kann WAS die Änderung erkennen, sie neu kompilieren und das Servlet neu laden.
  - **Wie es funktioniert:** Setzen Sie `reloadInterval` in `ibm-web-ext.xmi` (unter WEB-INF) auf einen niedrigen Wert (z.B. 1 Sekunde) für häufige Checks. Oder verwenden Sie die globale Einstellung in **Servers > Server Types > WebSphere application servers > [Ihr_Server] > Java and Process Management > Process definition > Java Virtual Machine > Custom properties** mit `com.ibm.ws.webcontainer.invokefilterscompatibility=true`.
  - **Einschränkungen:** Funktioniert nur für JSPs, die nicht aggressiv gecached wurden. Komplexe JSPs mit Includes oder Tags erfordern möglicherweise einen Modul-Neustart.
- **Einige Java-Klassen (Servlets und EJBs):**
  - Für explodierte Deployments kann WAS einzelne Klassendateien neu laden, wenn sie sich in den WEB-INF/classes- oder lib-Verzeichnissen befinden.
  - **Wie es funktioniert:** Aktivieren Sie "Application reload" im Deployment Descriptor oder über die Konsole: **Applications > [Ihre_App] > Manage Modules > [Modul] > Reload behavior > Reload enabled**.
  - Dies löst einen **Modul-Level-Reload** aus, der schneller ist als ein vollständiger App-Neustart, aber dennoch das gesamte Modul (z.B. Ihre Web-App) entlädt/nachlädt.

**Einschränkungen der eingebauten Unterstützung:**
- **Kein echtes Hotswap:** Änderungen an der Kernanwendungslogik (z.B. das Ändern einer Methode in einer laufenden Servlet-Klasse) werden ohne Entladen des alten Classloaders nicht wirksam. Sie könnten `ClassNotFoundException` oder veralteten Code sehen.
- **Zustandsverlust:** Sitzungen, Singletons oder Datenbankverbindungen können zurückgesetzt werden.
- **IBM JDK-Besonderheiten:** WAS verwendet oft IBMs JDK, das Eigenheiten beim Neuladen von Klassen im Vergleich zu OpenJDK/HotSpot aufweist.
- **Keine Unterstützung für strukturelle Änderungen:** Das Hinzufügen neuer Klassen, das Ändern von Methodensignaturen oder das Aktualisieren von Anmerkungen erfordert einen Neustart.
- **Performance-Overhead:** Häufiges Polling kann Ressourcen in der Entwicklung belasten.

Für grundlegende UI-Anpassungen (JSP-Bearbeitungen) oder einfache Klassenupdates ist dies ausreichend und kostenlos. Aber für "Full Hotswap" – bei dem Sie laufenden Code während der Ausführung bearbeiten können, ohne jeglichen Reload – benötigen Sie Drittanbieter-Tools.

#### 3. Vollständige Hotswap-Lösungen
Um nahtlose Codeänderungen zu erreichen (z.B. das Bearbeiten eines Methodenkörpers in einer Debugger-verbundenen IDE wie Eclipse oder IntelliJ und das sofortige Anwenden der Änderung), verwenden Sie Plugins, die das Classloading und die Instrumentierung der JVM patchen.

**Option 1: JRebel (Kostenpflichtiges Plugin)**
- **Was es ist:** Ein kommerzielles Tool von Perforce (früher ZeroTurnaround), das umfassendes Hotswap für Java-Apps bietet. Es instrumentiert Ihren Bytecode beim Start und ermöglicht das Neuladen von Klassen, Ressourcen und sogar frameworkspezifischen Änderungen (z.B. Spring Beans, Hibernate Entities).
- **Warum es mit WAS verwenden:**
  - Tiefe Integration mit WAS, einschließlich Unterstützung für explodierte WARs, OSGi-Bundles und IBM JDK.
  - Bewältigt komplexe Szenarien wie das Ändern von Methodensignaturen oder das Hinzufügen von Feldern (jenseits der standardmäßigen JVMTI-Hotswap-Grenzen).
  - **Funktionen:** Automatische Erkennung von Änderungen aus Ihrer IDE; keine manuellen Redeploys; bewahrt den App-Zustand.
- **Wie man es einrichtet:**
  1. Laden Sie JRebel von der offiziellen Seite herunter und installieren Sie es als Eclipse/IntelliJ-Plugin.
  2. Generieren Sie eine `rebel.xml`-Konfigurationsdatei für Ihr Projekt (automatisch generiert oder manuell).
  3. Fügen Sie JVM-Args zu Ihrem WAS-Server hinzu: `-javaagent:/pfad/zu/jrebel.jar` (vollständiger Pfad zur Agent-JAR).
  4. Starten Sie WAS im Debug-Modus (`-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=8000`).
  5. Verbinden Sie Ihren IDE-Debugger und bearbeiten Sie Code – JRebel synchronisiert Änderungen live.
- **Kosten:** Abonnementbasiert (~400 $/Benutzer/Jahr für Einzelpersonen; Enterprise-Lizenzierung variiert). Kostenlose Testversion verfügbar.
- **Vorteile:** Zuverlässig, benutzerfreundlich, ausgezeichnete WAS-Unterstützung.
- **Nachteile:** Kostenpflichtig; erfordert Einrichtung pro Projekt.

**Option 2: DCEVM + HotSwapAgent (Kostenlose Alternative)**
- **Was es ist:** Eine Open-Source-Kombination für erweitertes Hotswapping.
  - **DCEVM (Dynamic Code Evolution VM):** Eine modifizierte JVM, die HotSpots JVMTI (Java Virtual Machine Tool Interface) erweitert, um aggressivere Klassenneudefinitionen zu ermöglichen (z.B. Hinzufügen/Entfernen von Methoden, Ändern von Hierarchien).
  - **HotSwapAgent:** Ein Agent, der auf DCEVM aufbaut und IDE-Integration für automatisches Neuladen von Klassen bietet.
- **Warum es mit WAS verwenden:**
  - Kostenlos und leistungsstark für die Entwicklung, ahmt JRebels Fähigkeiten nach.
  - Unterstützt Methodenkörperänderungen, Ressourcenupdates und sogar einige Framework-Reloads (über Plugins).
- **Kompatibilitätshinweis mit WASs IBM JDK:**
  - WAS liefert typischerweise IBMs J9 JDK aus, das **DCEVM nicht nativ unterstützt** (DCEVM ist HotSpot-spezifisch).
  - **Workaround:** Wechseln Sie für die Entwicklung zu OpenJDK/HotSpot (z.B. über `JAVA_HOME`-Überschreibung in `setInitial.sh` oder Libertys `jvm.options`). Testen Sie gründlich – IBMs JDK-Garbage Collection und Sicherheitsfunktionen könnten sich unterscheiden.
  - In der Produktion wechseln Sie zurück zu IBM JDK; dies ist nur für die Entwicklung.
- **Wie man es einrichtet:**
  1. **DCEVM installieren:**
     - Laden Sie den DCEVM-Patcher-JAR von GitHub herunter (z.B. `dcevm-11.0.0+7-full.jar` für JDK 11+).
     - Führen Sie aus: `java -jar dcevm.jar /pfad/zu/ihrem/jdk/jre/lib/server/jvm.dll server` (Windows) oder entsprechend für Linux (`libjvm.so`).
     - Dies patcht die JVM-Binärdatei Ihres JDKs – sichern Sie zuerst!
  2. **HotSwapAgent installieren:**
     - Laden Sie `hotswap-agent.jar` von GitHub herunter.
     - Fügen Sie zu WAS JVM-Args hinzu: `-XXaltjvm=dcevm -XX:+TraceClassLoading -javaagent:/pfad/zu/hotswap-agent.jar=DCEVM` (plus alle Plugins, z.B. `=hotswap-spring` für Spring).
  3. **IDE-Integration:**
     - Installieren Sie das HotSwapAgent-Plugin für IntelliJ/Eclipse.
     - Starten Sie WAS mit Debug-Args wie oben.
     - Bearbeiten und speichern Sie Code in der IDE – der Agent lädt automatisch neu.
  4. **Kompatibilität testen:**
     - Führen Sie einen Smoke-Test durch: Stellen Sie ein einfaches Servlet bereit, bearbeiten Sie eine Methode (z.B. fügen Sie eine Log-Zeile hinzu), rufen Sie den Endpunkt auf und verifizieren Sie die Änderung ohne Neustart.
     - Überprüfen Sie die Logs auf Fehler wie `HotSwap failed: method limit reached` (DCEVM hat Grenzen für Änderungen pro Klasse).
- **Vorteile:** Kostenlos, anpassbar (über Plugins für Spring, CDI, etc.), community-unterstützt.
- **Nachteile:** Einrichtung ist knifflig; mögliche Instabilität mit nicht-standard JVMs; beschränkt auf HotSpot (IBM JDK-Wechsel sorgfältig testen); nicht so ausgereift wie JRebel.

#### Wann man was verwendet
- **Explodierte WAR + Eingebauter Reload:** Für schnelle JSP/statische Datei-Anpassungen in der frühen Entwicklung.
- **JRebel:** Wenn das Budget es erlaubt und Sie unternehmensgerechte Zuverlässigkeit benötigen.
- **DCEVM + HotSwapAgent:** Für kostenlosen Full Hotswap, aber planen Sie Zeit für JVM-Kompatibilitätstests ein.

Zusammenfassend transformieren diese Techniken WAS von einem schwergewichtigen Server in eine agilere Entwicklungsumgebung und reduzieren Iterationszeiten von Minuten auf Sekunden. Beginnen Sie mit explodierten WARs für sofortige Gewinne und setzen Sie dann bei Bedarf Tools darauf auf. Wenn Sie auf spezifische Fehler stoßen, teilen Sie weitere Details zur Fehlerbehebung mit.

**Referenzen:**  
[JRebel Dokumentation für WebSphere](https://www.jrebel.com/products/jrebel/tutorials/deploy-jrebel-websphere)  
[DCEVM GitHub Repo](https://github.com/dcevm/dcevm)  
[HotSwapAgent GitHub Repo](https://github.com/HotswapProjects/HotswapAgent)  
[IBM Knowledge Center: WebSphere Hot Deployment](https://www.ibm.com/docs/en/was/9.0.5?topic=applications-hot-deployment)