---
audio: false
generated: false
lang: de
layout: post
title: Mit WebSphere Liberty und Eclipse arbeiten
translated: true
---

Um die WebSphere-Plugin-Tools in Eclipse zu verwenden und sie für die Arbeit mit WebSphere Liberty zu integrieren, können Sie zwischen zwei Hauptoptionen wählen: **IBM Liberty Developer Tools** und **Liberty Tools**. Beide sind über den Eclipse Marketplace verfügbar und bieten Funktionen zum Erstellen, Bereitstellen und Verwalten von Anwendungen auf WebSphere Liberty, einem leichten, produktionsbereiten Server für Java EE und cloud-native Anwendungen. Im Folgenden finden Sie eine detaillierte Anleitung zur Verwendung und Integration dieser Tools.

---

### **Übersicht der Tools**
- **IBM Liberty Developer Tools**: Ein traditionelles Plugin, das von IBM zur Verwaltung von Liberty-Servern innerhalb von Eclipse bereitgestellt wird. Es ermöglicht Ihnen, Liberty-Server zu erstellen und zu verwalten, Anwendungen bereitzustellen und direkt aus der IDE zu debuggen. Dieses Tool ist ideal für einen serverzentrierten Workflow oder für Projekte, die Maven oder Gradle nicht verwenden.
- **Liberty Tools**: Eine next-generation, Open-Source-Alternative, die sich auf Maven- und Gradle-Projekte konzentriert. Es bietet eine engere Integration mit Build-Tools, eine automatische Erkennung von Liberty-Projekten und Unterstützung für den Entwicklungsmodus (dev mode) von Liberty. Dieses Tool ist besser für moderne, build-toolzentrierte Workflows geeignet.

Beide Tools vereinfachen die Entwicklung für WebSphere Liberty, unterscheiden sich jedoch in ihrem Ansatz. Wählen Sie dasjenige, das am besten zu Ihrem Projekt und Ihren Entwicklungspräferenzen passt.

---

### **Installation**
1. **Installieren Sie Eclipse**:
   - Verwenden Sie eine kompatible Version, wie **Eclipse for Enterprise Java and Web Developers**.
   - Stellen Sie sicher, dass Ihre Eclipse-Version das Plugin unterstützt, das Sie auswählen (überprüfen Sie die Kompatibilität in der Marketplace-Liste).

2. **Installieren Sie das Plugin**:
   - Öffnen Sie Eclipse und gehen Sie zu **Help > Eclipse Marketplace**.
   - Suchen Sie nach:
     - "IBM Liberty Developer Tools" für das traditionelle IBM-Toolset oder
     - "Liberty Tools" für die Open-Source-Alternative.
   - Installieren Sie das gewünschte Plugin, indem Sie den Anweisungen folgen.

---

### **Einrichten der Liberty-Runtime**
- **Herunterladen von Liberty**:
  - Wenn Sie dies noch nicht getan haben, laden Sie die WebSphere Liberty-Runtime von der [offiziellen IBM-Website](https://www.ibm.com/docs/en/was-liberty) herunter.
  - Stellen Sie sicher, dass die Liberty-Version mit dem installierten Plugin kompatibel ist.

- **Konfigurieren der Runtime in Eclipse**:
  - Für **IBM Liberty Developer Tools**:
    - Gehen Sie zu **Window > Preferences > Server > Runtime Environments**.
    - Klicken Sie auf "Add," wählen Sie "Liberty Server" und geben Sie den Pfad zu Ihrem Liberty-Installationsverzeichnis an.
  - Für **Liberty Tools**:
    - Es ist keine explizite Runtime-Konfiguration erforderlich. Liberty Tools erkennen Liberty-Projekte über Maven- oder Gradle-Konfigurationen, stellen Sie daher sicher, dass Ihr Projekt ordnungsgemäß eingerichtet ist (siehe unten).

---

### **Integrieren mit Ihrem Projekt**
Der Integrationsprozess unterscheidet sich leicht zwischen den beiden Tools. Folgen Sie den untenstehenden Schritten, basierend auf dem Tool, das Sie installiert haben.

#### **Für IBM Liberty Developer Tools**
1. **Erstellen Sie einen Liberty-Server**:
   - Öffnen Sie die **Servers**-Ansicht (**Window > Show View > Servers**).
   - Klicken Sie mit der rechten Maustaste in der Servers-Ansicht und wählen Sie **New > Server**.
   - Wählen Sie "Liberty Server" aus der Liste und folgen Sie dem Assistenten, um den Server zu konfigurieren, einschließlich der Angabe des Pfades zu Ihrer Liberty-Installation.

2. **Fügen Sie Ihr Projekt hinzu**:
   - Klicken Sie mit der rechten Maustaste auf den Server in der Servers-Ansicht und wählen Sie **Add and Remove...**.
   - Wählen Sie Ihr Projekt und verschieben Sie es auf die Seite "Configured".

3. **Starten Sie den Server**:
   - Klicken Sie mit der rechten Maustaste auf den Server und wählen Sie **Start** oder **Debug**, um Ihre Anwendung auszuführen.
   - Greifen Sie auf Ihre Anwendung über die angegebene URL zu (Standard: `http://localhost:9080/<context-root>`).

#### **Für Liberty Tools (Maven/Gradle-Projekte)**
1. **Stellen Sie die Projektkonfiguration sicher**:
   - Ihr Projekt muss das erforderliche Liberty-Plugin enthalten:
     - Für Maven: Fügen Sie das `liberty-maven-plugin` zu Ihrer `pom.xml` hinzu.
     - Für Gradle: Fügen Sie das `liberty-gradle-plugin` zu Ihrer `build.gradle` hinzu.
   - Die `server.xml`-Konfigurationsdatei sollte sich an der Standardposition befinden:
     - Für Maven: `src/main/liberty/config`.
     - Für Gradle: Passen Sie dies basierend auf Ihrer Projektstruktur an.

2. **Verwenden Sie das Liberty-Dashboard**:
   - Klicken Sie auf das Liberty-Symbol in der Eclipse-Symbolleiste, um das **Liberty-Dashboard** zu öffnen.
   - Liberty Tools erkennen automatisch und listen Ihre Liberty-Projekte im Dashboard auf.
   - Klicken Sie mit der rechten Maustaste auf Ihr Projekt im Dashboard, um Befehle wie Folgende zuzugreifen:
     - "Start in dev mode" (automatisch neu bereitstellen von Änderungen ohne Neustart des Servers).
     - "Run tests."
     - "View test reports."

3. **Greifen Sie auf Ihre Anwendung zu**:
   - Sobald der Server läuft, greifen Sie auf Ihre Anwendung über die angegebene URL zu (Standard: `http://localhost:9080/<context-root>`).
   - Im Entwicklungsmodus nehmen Sie Änderungen an Ihrem Code vor, und Liberty stellt sie automatisch neu bereit.

---

### **Wichtige Funktionen**
Beide Tools bieten leistungsstarke Funktionen zur Steigerung der Produktivität:

- **Serververwaltung**:
  - Starten, stoppen und debuggen Sie Liberty-Server direkt aus Eclipse.
- **Anwendungsbereitstellung**:
  - Stellen Sie Anwendungen einfach bereit und stellen Sie sie erneut bereit.
- **Konfigurationshilfe**:
  - Beide Tools bieten Code-Vervollständigung, Validierung und Hover-Beschreibungen für Liberty-Konfigurationsdateien (z. B. `server.xml`).
- **Entwicklungsmodus**:
  - Erkennen und stellen Sie Codeänderungen automatisch neu bereit, ohne den Server neu zu starten (insbesondere mit Liberty Tools im Entwicklungsmodus).
- **Debugging**:
  - Hängen Sie den Eclipse-Debugger an den Liberty-Server an, um Probleme zu beheben.

---

### **Überlegungen und mögliche Probleme**
- **Versionskompatibilität**:
  - Stellen Sie sicher, dass Ihre Versionen von Eclipse, dem Plugin und der Liberty-Runtime kompatibel sind. Überprüfen Sie die Dokumentation für spezifische Anforderungen.
- **Projektkonfiguration**:
  - Für Liberty Tools muss Ihr Projekt ein ordnungsgemäß konfiguriertes Maven- oder Gradle-Projekt mit dem enthaltenen Liberty-Plugin sein.
  - Stellen Sie sicher, dass `server.xml` sich an der erwarteten Position befindet, damit die Tools Ihr Projekt erkennen.
- **Netzwerkeinstellungen**:
  - Stellen Sie sicher, dass die Standard-Liberty-Ports (z. B. 9080 für HTTP, 9443 für HTTPS) geöffnet und nicht durch Firewalls blockiert sind.
- **Java-Kompatibilität**:
  - Liberty ist ein Java-basierter Server, stellen Sie daher sicher, dass Sie eine kompatible Java-Version für Ihre Liberty-Runtime installiert haben.

---

### **Schnellstart mit Liberty Tools (Maven/Gradle)**
Wenn Sie Maven oder Gradle verwenden, bieten Liberty Tools eine vereinfachte Erfahrung. Hier ist eine Schritt-für-Schritt-Anleitung:

1. Installieren Sie **Eclipse for Enterprise Java and Web Developers**.
2. Gehen Sie zu **Help > Eclipse Marketplace**, suchen Sie nach "Liberty Tools" und installieren Sie das Plugin.
3. Erstellen oder importieren Sie ein Maven/Gradle-Projekt, das für Liberty konfiguriert ist:
   - Sie können den [Open Liberty Starter](https://openliberty.io/start/) verwenden, um ein Beispielprojekt zu generieren.
4. Stellen Sie sicher, dass Ihr Projekt das `liberty-maven-plugin` (für Maven) oder `liberty-gradle-plugin` (für Gradle) konfiguriert hat.
5. Öffnen Sie das **Liberty-Dashboard**, indem Sie auf das Liberty-Symbol in der Symbolleiste klicken.
6. Ihr Projekt sollte im Dashboard erscheinen. Klicken Sie mit der rechten Maustaste darauf und wählen Sie "Start in dev mode."
7. Greifen Sie auf Ihre Anwendung über die angegebene URL zu (Standard: `http://localhost:9080/<context-root>`).
8. Nehmen Sie Änderungen an Ihrem Code vor; Liberty dev mode stellt sie automatisch neu bereit.
9. Verwenden Sie das Dashboard, um Tests auszuführen oder Testberichte anzuzeigen, wie erforderlich.

---

### **Wahl zwischen den Tools**
- **IBM Liberty Developer Tools**:
  - Ideal für einen traditionellen serververwaltungsorientierten Ansatz oder für Projekte, die Maven oder Gradle nicht verwenden.
  - Bietet eine Servers-Ansicht zur expliziten Verwaltung von Liberty-Servern.
- **Liberty Tools**:
  - Besser geeignet für Maven- oder Gradle-Projekte mit engerer Integration in diese Build-Systeme.
  - Bietet ein Liberty-Dashboard für projektzentrierte Verwaltung und Unterstützung für den Entwicklungsmodus.
  - Open-Source, was Community-Beiträge und -Aktualisierungen ermöglicht.

Beide Tools sind über den Eclipse Marketplace verfügbar, sodass Sie beide ausprobieren und dasjenige auswählen können, das am besten zu Ihrem Workflow passt.

---

Zusammengefasst umfasst die Verwendung der WebSphere-Plugin-Tools in Eclipse die Installation des entsprechenden Plugins, die Einrichtung der Liberty-Runtime und die Konfiguration Ihres Projekts für die Arbeit mit Liberty. Ob Sie sich für IBM Liberty Developer Tools oder Liberty Tools entscheiden, beide bieten leistungsstarke Funktionen, um die Entwicklung für WebSphere Liberty innerhalb der Eclipse-IDE zu vereinfachen.