---
audio: false
generated: false
lang: de
layout: post
title: Mit WebSphere Liberty Server in VSCode arbeiten
translated: true
---

Um den WebSphere Liberty-Server in Visual Studio Code (VSCode) zu verwenden, können Sie die **Liberty Tools**-Erweiterung nutzen, die sowohl Open Liberty als auch WebSphere Liberty unterstützt. Diese Erweiterung ermöglicht es Ihnen, Ihren Liberty-Server zu verwalten, Anwendungen zu deployen und direkt in VSCode zu debuggen, wodurch Ihr Entwicklungsworkflow optimiert wird.

### Schritte zur Verwendung von WebSphere Liberty in VSCode

#### 1. **Installieren Sie die Liberty Tools-Erweiterung**
   - Öffnen Sie VSCode und navigieren Sie zur Ansicht Erweiterungen, indem Sie auf das Symbol Erweiterungen in der Aktivitätsleiste klicken oder `Strg+Umschalt+X` drücken.
   - Suchen Sie im Erweiterungsmarktplatz nach "Liberty Tools".
   - Klicken Sie auf "Installieren", um die Erweiterung zu VSCode hinzuzufügen.
   - Laden Sie VSCode neu, falls dies zur Aktivierung der Erweiterung erforderlich ist.

#### 2. **Einrichten der Voraussetzungen**
   - **Java**: Stellen Sie sicher, dass eine kompatible Version von Java installiert ist (Java 8 oder höher wird empfohlen). Liberty ist ein Java-basierter Server, daher ist Java für dessen Ausführung unerlässlich.
   - **WebSphere Liberty**: Laden Sie die WebSphere Liberty-Runtime herunter und installieren Sie sie, falls Sie dies noch nicht getan haben. Sie können sie von der [offiziellen IBM-Website](https://www.ibm.com/docs/en/was-liberty) erhalten. Notieren Sie sich das Installationsverzeichnis, da Sie es zur Konfiguration der Erweiterung benötigen.

#### 3. **Konfigurieren Sie die Liberty Tools-Erweiterung**
   - Nach der Installation der Erweiterung konfigurieren Sie diese, um auf Ihre Liberty-Installation zu verweisen.
   - Öffnen Sie die Befehlspalette in VSCode, indem Sie `Strg+Umschalt+P` drücken.
   - Geben Sie "Liberty: Add Liberty Runtime" ein und wählen Sie den Befehl aus.
   - Geben Sie den Pfad zu Ihrem Liberty-Installationsverzeichnis an (z.B. `/opt/ibm/wlp`).
   - Die Erweiterung erkennt die Liberty-Runtime und macht sie in VSCode verfügbar.

#### 4. **Verwalten Sie Ihren Liberty-Server**
   - Sobald die Konfiguration abgeschlossen ist, können Sie Ihren Liberty-Server direkt in VSCode verwalten.
   - **Liberty-Dashboard**: Greifen Sie auf die Ansicht des Liberty-Dashboards im Explorer-Bereich oder über die Befehlspalette zu. Dieses Dashboard listet Ihre Liberty-Projekte und -Server auf.
   - **Server starten/stoppen**: Klicken Sie mit der rechten Maustaste auf Ihren Server im Dashboard, um ihn zu starten, zu stoppen oder neu zu starten.
   - **Anwendungen deployen**: Für Liberty-Projekte (z.B. Maven- oder Gradle-Projekte mit Liberty-Plugins) klicken Sie mit der rechten Maustaste auf das Projekt und wählen Sie "Deploy to Liberty", um Anwendungen zu deployen.
   - **Entwicklungsmodus (Dev Mode)**: Für Maven- oder Gradle-Projekte starten Sie den Server im Dev-Modus, der Codeänderungen automatisch erkennt, neu kompiliert und die Anwendung neu deployt, ohne den Server neu zu starten. Dies ist ideal für iterative Entwicklung.

#### 5. **Debugging und Testen**
   - **Debugging**: Hängen Sie einen Debugger an Ihren laufenden Liberty-Server direkt in VSCode an. Verwenden Sie die "Debug"-Option im Liberty-Dashboard oder richten Sie eine Debug-Konfiguration in der Ansicht "Run and Debug" von VSCode ein.
   - **Tests ausführen**: Wenn Ihr Projekt Tests enthält, führen Sie diese vom Dashboard aus und sehen Sie sich die Ergebnisse in VSCode an.

#### 6. **Zusätzliche Funktionen**
   - **Konfigurationshilfe**: Die Erweiterung bietet Code-Vervollständigung, -Validierung und Hover-Beschreibungen für Liberty-Konfigurationsdateien (z.B. `server.xml`), wodurch die Serverkonfiguration vereinfacht wird.
   - **Sprachunterstützung**: Sie unterstützt Java, MicroProfile und Jakarta EE-APIs, wodurch Ihre Entwicklungsarbeit verbessert wird.

### Wichtige Vorteile
- **Nahtlose Integration**: Verwalten Sie Ihren Liberty-Server, ohne VSCode zu verlassen, und verbessern Sie so die Effizienz.
- **Automatisches Deployen**: Im Dev-Modus werden Codeänderungen automatisch erkannt und deployt, wodurch Zeit während der Entwicklung gespart wird.
- **Debugging-Unterstützung**: Hängen Sie einen Debugger einfach an Ihren Server an, um Probleme zu beheben.
- **Leichtgewichtig und effizient**: Liberty Tools ist so gestaltet, dass es leichtgewichtig ist und sich an Libertys Fokus auf Geschwindigkeit und Effizienz anpasst.

### Zusätzliche Ressourcen
- Für detaillierte Anleitungen verweisen Sie auf die [Open Liberty-Dokumentation](https://openliberty.io/docs/) und die [Liberty Tools VSCode-Dokumentation](https://openliberty.io/docs/latest/develop/liberty-tools.html).
- Wenn Probleme auftreten, überprüfen Sie den Abschnitt zur Fehlerbehebung der Erweiterung oder suchen Sie Hilfe in der Community auf Plattformen wie Stack Overflow.

Durch die Beachtung dieser Schritte können Sie WebSphere Liberty effektiv innerhalb von VSCode nutzen und dessen Funktionen nutzen, um Ihren Entwicklungsprozess zu verbessern.