---
audio: false
generated: true
lang: de
layout: post
title: Liberty Tools Erweiterung in Visual Studio Code
translated: true
type: note
---

Hier ist eine Übersicht, wie Sie die Liberty Tools-Erweiterung in Visual Studio Code verwenden können, um mit einem WebSphere Liberty-Server zu arbeiten:

---

### 1. Installieren der Liberty Tools-Erweiterung
- **Suchen und Installieren:**  
  Öffnen Sie die Erweiterungsansicht in VS Code, suchen Sie nach **"IBM WebSphere Liberty Tools"** und installieren Sie sie.
- **Vorteile der Erweiterung:**  
  Diese Erweiterung integriert Serververwaltung, Anwendungsbereitstellung und Debugging in VS Code.

---

### 2. Bereiten Sie Ihren WebSphere Liberty-Server vor
- **Installieren oder auf eine Liberty-Laufzeitumgebung verweisen:**  
  Wenn Sie noch keinen Liberty-Server installiert haben, laden Sie einen von IBM herunter und installieren Sie ihn. Falls er bereits installiert ist, notieren Sie sich das Installationsverzeichnis.
- **Kompatibilität sicherstellen:**  
  Vergewissern Sie sich, dass Ihre Liberty-Laufzeitversion mit der Erweiterung kompatibel ist.

---

### 3. Konfigurieren Sie Ihren Liberty-Server in VS Code
- **Erstellen einer neuen Serverinstanz:**  
  Öffnen Sie die Befehlspalette (`Strg+Umschalt+P` oder `Cmd+Umschalt+P`) und führen Sie den Befehl aus:  
  `Liberty: Create Server`  
  Folgen Sie den Anweisungen, um:
  - Den Installationsordner der Laufzeitumgebung auszuwählen.
  - Die Serverkonfigurationsdatei (typischerweise `server.xml`) anzugeben.
- **Bestehende Projekte:**  
  Wenn Sie bereits eine Liberty-basierte Anwendung haben, öffnen Sie den Arbeitsbereich, damit die Erweiterung Ihre Servereinstellungen erkennen und verwalten kann.

---

### 4. Hinzufügen Ihrer Anwendung
- **Bereitstellen der App:**  
  Sie können Ihre Anwendung zum Server hinzufügen, indem Sie entweder:
  - Die `server.xml` bearbeiten, um den Kontext und die Bereitstellungsdetails Ihrer Anwendung aufzunehmen, oder
  - Die UI-Optionen der Erweiterung (oft in der Liberty-Ansicht verfügbar) verwenden, um "Add Application" oder "Deploy Application" auszuwählen.
- **Build-Integration:**  
  Wenn Sie Maven oder Gradle verwenden, bietet die Erweiterung möglicherweise auch Tasks an, die Ihre Anwendung vor der Bereitstellung bauen.

---

### 5. Server starten, stoppen und debuggen
- **Starten des Servers:**  
  Klicken Sie in der Liberty-Ansicht (oft als dediziertes Panel oder Baumansicht in VS Code verfügbar) mit der rechten Maustaste auf Ihren konfigurierten Server und wählen Sie **"Start Server"**.  
  Im Ausgabefenster werden die Start-Logs und alle Konfigurationsmeldungen angezeigt.
- **Stoppen des Servers:**  
  Klicken Sie auf ähnliche Weise mit der rechten Maustaste und wählen Sie **"Stop Server"**, um Ihre Instanz herunterzufahren.
- **Debugging:**  
  Wenn Sie Ihre Anwendung debuggen müssen:
  - Setzen Sie Breakpoints in Ihrem Code.
  - Verwenden Sie die Befehlspalette, um **"Liberty: Debug Server"** auszuführen (oder verwenden Sie die Debug-Optionen in der Liberty-Ansicht), um den VS Code-Debugger an Ihren laufenden Server anzuhängen.
  - Ihre Breakpoints sollten nun getroffen werden, wenn Ihre Anwendung Anfragen verarbeitet.

---

### 6. Zusätzliche Funktionen und Tipps
- **Live-Log-Überwachung:**  
  Die Erweiterung bietet eine Möglichkeit, die Liberty-Server-Logs in Echtzeit einzusehen, was die Fehlerdiagnose erleichtert.
- **Bearbeiten der Serverkonfiguration:**  
  Profitieren Sie von IntelliSense und Vorschlägen beim direkten Bearbeiten Ihrer `server.xml` innerhalb von VS Code.
- **Task-Integration:**  
  Nutzen Sie die Tasks von VS Code, wenn Sie automatisierte Builds oder Bereitstellungen als Teil Ihres Entwicklungs-Workflows ausführen.
- **Container- und Remote-Unterstützung:**  
  Je nach Ihrem Setup können Sie Liberty möglicherweise auch so konfigurieren, dass es innerhalb von Containern oder Remote-Umgebungen läuft, wobei zusätzliche Befehle in der Erweiterung verfügbar sind.

---

### Abschließende Hinweise
Die Verwendung der Liberty Tools-Erweiterung rationalisiert den Prozess der Entwicklung, Bereitstellung und Fehlersuche für Ihre WebSphere Liberty-Anwendungen direkt innerhalb von VS Code. Diese Integration hilft, Kontextwechsel zu reduzieren und beschleunigt Ihren Entwicklungszyklus.

Weitere Informationen zu erweiterten Konfigurationen oder Schritten zur Problembehebung finden Sie in der offiziellen IBM-Dokumentation zur Liberty Tools-Erweiterung.