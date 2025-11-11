---
audio: false
generated: true
lang: de
layout: post
title: Debuggen von Spring Boot-Anwendungen in Visual Studio Code
translated: true
type: note
---

Um ein Maven Spring Boot Projekt in Visual Studio Code (VSCode) zu debuggen, können Sie diese einfachen Schritte befolgen, um Ihre Anwendung im Debug-Modus einzurichten und auszuführen. Diese Anleitung setzt voraus, dass Sie ein grundlegendes Maven Spring Boot Projekt mit einer `pom.xml`-Datei und einer Hauptklasse mit der Annotation `@SpringBootApplication` haben. So gehen Sie vor:

### Schritt 1: Notwendige Erweiterungen installieren
Stellen Sie sicher, dass VSCode mit den erforderlichen Erweiterungen für die Java- und Spring Boot-Entwicklung ausgestattet ist:
- **Java Extension Pack**: Dies umfasst wichtige Tools wie Language Support for Java by Red Hat, das Debugging-Fähigkeiten bietet, sowie andere Hilfsprogramme für die Java-Entwicklung.
- **Spring Boot Extension Pack**: Dieser Pack verbessert die Spring Boot-Entwicklung mit Funktionen wie dem Spring Boot Dashboard, Spring Boot Tools und mehr.

So installieren Sie diese:
1. Öffnen Sie VSCode.
2. Gehen Sie zur Erweiterungsansicht (`Strg+Umschalt+X` oder `Cmd+Umschalt+X` auf macOS).
3. Suchen Sie nach "Java Extension Pack" und "Spring Boot Extension Pack" und klicken Sie für jedes auf **Installieren**.

### Schritt 2: Öffnen Sie Ihr Maven Spring Boot Projekt
- Starten Sie VSCode und öffnen Sie Ihren Projektordner, indem Sie **Datei > Ordner öffnen** wählen und das Verzeichnis auswählen, das Ihre `pom.xml`-Datei enthält.
- VSCode erkennt die `pom.xml`, und der Java Extension Pack indiziert das Projekt automatisch und löst die Abhängigkeiten auf. Dies kann einen Moment dauern. Warten Sie, bis der Vorgang abgeschlossen ist (Sie sehen den Fortschritt in der Statusleiste unten rechts).

### Schritt 3: Erstellen oder Bearbeiten der `launch.json`-Datei
Um das Debugging zu konfigurieren, müssen Sie eine `launch.json`-Datei in VSCode einrichten:
1. Öffnen Sie die Ansicht **Run and Debug**, indem Sie auf das Käfer-und-Play-Symbol in der Seitenleiste klicken oder `Strg+Umschalt+D` drücken.
2. Wenn keine Debug-Konfiguration existiert, klicken Sie auf **"create a launch.json file"**. Wenn bereits eine existiert, klicken Sie auf das Zahnradsymbol, um sie zu bearbeiten.
3. Wenn Sie aufgefordert werden, wählen Sie **Java** als Umgebung aus. VSCode generiert eine standardmäßige `launch.json`-Datei in einem `.vscode`-Ordner innerhalb Ihres Projekts.
4. Fügen Sie eine Debug-Konfiguration für Ihre Spring Boot-Anwendung hinzu oder ändern Sie sie. Hier ist eine Beispielkonfiguration:

    ```json
    {
        "type": "java",
        "name": "Debug Spring Boot",
        "request": "launch",
        "mainClass": "com.example.demo.DemoApplication",
        "projectName": "demo"
    }
    ```

    - Ersetzen Sie `"com.example.demo.DemoApplication"` durch den vollqualifizierten Namen Ihrer Hauptklasse (z.B. `com.yourcompany.yourapp.YourApplication`).
    - Ersetzen Sie `"demo"` durch den Namen Ihres Projekts, typischerweise den `<artifactId>` aus Ihrer `pom.xml`.

5. Speichern Sie die `launch.json`-Datei.

#### Optional: Argumente hinzufügen
Wenn Ihre Anwendung spezifische Argumente benötigt (z.B. Spring Profile), können Sie diese hinzufügen:
```json
{
    "type": "java",
    "name": "Debug Spring Boot",
    "request": "launch",
    "mainClass": "com.example.demo.DemoApplication",
    "projectName": "demo",
    "args": "--spring.profiles.active=dev"
}
```

### Schritt 4: Debugging starten
- Wählen Sie in der Ansicht **Run and Debug** die Option **"Debug Spring Boot"** aus dem Dropdown-Menü oben aus.
- Klicken Sie auf den grünen Play-Button (oder drücken Sie `F5`), um die Anwendung im Debug-Modus zu starten.
- VSCode kompiliert das Projekt mit Maven, startet die Spring Boot-Anwendung und fügt den Debugger automatisch an.

### Schritt 5: Breakpoints setzen und debuggen
- Öffnen Sie eine Java-Datei in Ihrem Projekt (z.B. eine Controller- oder Service-Klasse).
- Setzen Sie Breakpoints, indem Sie links neben den Zeilennummern in den Gutter klicken, wo ein roter Punkt erscheint.
- Interagieren Sie mit Ihrer Anwendung (z.B. über einen Browser oder API-Client). Wenn die Ausführung einen Breakpoint erreicht, hält VSCode an und ermöglicht Ihnen:
  - Variablen im **Variables**-Panel zu inspizieren.
  - Mit Steuerungselementen wie **Step Over** (`F10`), **Step Into** (`F11`) oder **Continue** (`F5`) durch den Code zu schreiten.
  - Die Aufrufliste und mehr in der Debug-Seitenleiste anzuzeigen.

### Alternative Methoden
Während die `launch.json`-Methode aufgrund ihrer Flexibilität empfohlen wird, können Sie auch debuggen mit:
- **Maven-Ansicht**:
  1. Öffnen Sie die Maven-Ansicht in der Seitenleiste (suchen Sie nach dem "M"-Symbol oder aktivieren Sie sie über Erweiterungen).
  2. Erweitern Sie Ihr Projekt, navigieren Sie zu `spring-boot` unter Plugins, klicken Sie mit der rechten Maustaste auf `spring-boot:run` und wählen Sie **Debug**.
  3. Die Anwendung startet und der Debugger wird angefügt.
- **Spring Boot Dashboard**:
  1. Öffnen Sie das Spring Boot Dashboard (normalerweise in der Explorer-Ansicht oder über die Befehlspalette: `Spring Boot Dashboard`).
  2. Suchen Sie Ihre Anwendung, klicken Sie mit der rechten Maustaste darauf und wählen Sie **Debug** (falls verfügbar).

### Voraussetzungen und Hinweise
- Stellen Sie sicher, dass **Maven** auf Ihrem System installiert und über die Befehlszeile erreichbar ist, oder verlassen Sie sich auf das eingebettete Maven von VSCode (falls benötigt, über die Einstellungen konfigurierbar).
- Vergewissern Sie sich, dass Ihr Projekt erfolgreich gebaut wird (`mvn clean install`), um Laufzeitfehler während des Debuggens zu vermeiden.
- Verwenden Sie eine kompatible Java-Version, wie in Ihrer `pom.xml` angegeben (z.B. über `<java.version>`).

Indem Sie diese Schritte befolgen, können Sie Ihr Maven Spring Boot Projekt effektiv in VSCode debuggen und seine leistungsstarken Debugging-Tools nutzen, um Probleme in Ihrem Code zu identifizieren und zu beheben.