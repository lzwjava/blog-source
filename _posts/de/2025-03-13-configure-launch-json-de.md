---
audio: false
generated: true
lang: de
layout: post
title: Konfiguration von launch.json für Spring Boot in VSCode
translated: true
type: note
---

Um die `launch.json`-Datei für ein Maven Spring Boot Projekt in Visual Studio Code (VSCode) zu konfigurieren, müssen Sie eine Launch-Konfiguration einrichten, die es VSCode ermöglicht, Ihre Anwendung mit seinen Java-Erweiterungen auszuführen und zu debuggen. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung, die Ihnen dabei hilft.

### Voraussetzungen
Bevor Sie fortfahren, stellen Sie Folgendes sicher:
- Sie haben das **Java Extension Pack** in VSCode installiert. Dieses Paket enthält essentielle Erweiterungen wie "Debugger for Java" und "Language Support for Java" von Red Hat, die Unterstützung für das Ausführen und Debuggen von Java-Anwendungen, einschließlich Spring Boot Projekten, bieten.
- Ihr Spring Boot Projekt ist ein Maven-Projekt mit einer gültigen `pom.xml`-Datei.
- Das Projekt hat eine Hauptklasse, die mit `@SpringBootApplication` annotiert ist und die `main`-Methode zum Starten der Anwendung enthält.

### Schritte zur Konfiguration von `launch.json`
1. **Hauptklasse lokalisieren**
   - In einem typischen Spring Boot Projekt befindet sich die Hauptklasse im Verzeichnis `src/main/java` und ist mit `@SpringBootApplication` annotiert. Sie könnte beispielsweise `com.example.demo.DemoApplication` heißen.
   - Öffnen Sie Ihr Projekt in VSCode und identifizieren Sie den vollqualifizierten Namen dieser Klasse (z.B. `com.example.demo.DemoApplication`).

2. **Projektnamen bestimmen**
   - Der Projektname in einem Maven-Projekt entspricht dem `artifactId`, der in Ihrer `pom.xml`-Datei definiert ist.
   - Öffnen Sie Ihre `pom.xml`-Datei und suchen Sie nach dem `<artifactId>`-Tag. Zum Beispiel:
     ```xml
     <artifactId>demo</artifactId>
     ```
     Hier wäre der Projektname `demo`.

3. **Debug-Ansicht öffnen**
   - Klicken Sie in VSCode auf das **Debug**-Symbol in der linken Seitenleiste (oder drücken Sie `Strg+Umschalt+D` / `Befehl+Umschalt+D` auf dem Mac).
   - Klicken Sie auf das Zahnradsymbol ⚙️ neben dem Dropdown-Menü "Run and Debug", um die Launch-Einstellungen zu konfigurieren. Wenn keine `launch.json` existiert, wird VSCode Sie auffordern, eine zu erstellen.

4. **`launch.json` erstellen oder bearbeiten**
   - Wenn Sie aufgefordert werden, eine Umgebung auszuwählen, wählen Sie **Java**. Dies generiert eine grundlegende `launch.json`-Datei im `.vscode`-Ordner Ihres Projekts.
   - Öffnen Sie die `launch.json`-Datei. Wenn sie bereits existiert, können Sie sie direkt bearbeiten.

5. **Eine Launch-Konfiguration hinzufügen**
   - Fügen Sie die folgende Konfiguration innerhalb des `"configurations"`-Arrays in `launch.json` hinzu. Ersetzen Sie die Platzhalter mit den Details Ihres Projekts:
     ```json
     {
         "type": "java",
         "name": "Launch Spring Boot App",
         "request": "launch",
         "mainClass": "com.example.demo.DemoApplication",
         "projectName": "demo"
     }
     ```
     - **Erklärung der Felder:**
       - `"type": "java"`: Gibt an, dass es sich um eine Java-Launch-Konfiguration handelt.
       - `"name": "Launch Spring Boot App"`: Ein beschreibender Name für diese Konfiguration, der im Debug-Dropdown erscheint.
       - `"request": "launch"`: Zeigt an, dass VSCode die Anwendung starten soll (im Gegensatz zum Verbinden mit einem existierenden Prozess).
       - `"mainClass"`: Der vollqualifizierte Name Ihrer Spring Boot Hauptklasse (z.B. `com.example.demo.DemoApplication`).
       - `"projectName"`: Der `artifactId` aus Ihrer `pom.xml` (z.B. `demo`), der VSCode hilft, das Projekt in einem Multi-Modul-Setup zu lokalisieren.

   - Hier ist ein Beispiel einer vollständigen `launch.json`-Datei mit dieser Konfiguration:
     ```json
     {
         "version": "0.2.0",
         "configurations": [
             {
                 "type": "java",
                 "name": "Launch Spring Boot App",
                 "request": "launch",
                 "mainClass": "com.example.demo.DemoApplication",
                 "projectName": "demo"
             }
         ]
     }
     ```

6. **Optional: VM-Argumente oder Programmargumente hinzufügen**
   - Wenn Ihre Anwendung zusätzliche Einstellungen benötigt (z.B. das Aktivieren eines Spring Profils), können Sie diese mit `"vmArgs"` oder `"args"` hinzufügen:
     - Beispiel mit einem Spring Profil:
       ```json
       {
           "type": "java",
           "name": "Launch Spring Boot App with Profile",
           "request": "launch",
           "mainClass": "com.example.demo.DemoApplication",
           "projectName": "demo",
           "vmArgs": "-Dspring.profiles.active=dev"
       }
       ```
       Dies setzt die Eigenschaft `spring.profiles.active` auf `dev`.
     - Beispiel mit Programmargumenten:
       ```json
       "args": ["arg1", "arg2"]
       ```

7. **Speichern und Ausführen**
   - Speichern Sie die `launch.json`-Datei.
   - Gehen Sie zurück zur Debug-Ansicht, wählen Sie **"Launch Spring Boot App"** aus dem Dropdown-Menü aus und klicken Sie auf den grünen Play-Button (oder drücken Sie `F5`).
   - VSCode wird Ihre Spring Boot Anwendung mit Maven und der Java-Erweiterung bauen und ausführen. Sie sollten die Spring Boot Start-Logs in der Debug-Konsole sehen.

### Überprüfen der Konfiguration
- Wenn Ihre Spring Boot Anwendung eine Webanwendung ist, öffnen Sie einen Browser und navigieren Sie zu `http://localhost:8080` (oder dem in Ihrer `application.properties` oder `application.yml`-Datei angegebenen Port), um zu bestätigen, dass sie läuft.
- Sie können auch Breakpoints in Ihrem Code setzen und die Debug-Steuerelemente (Pause, Step Over, etc.) verwenden, um Ihre Anwendung zu debuggen.

### Hinweise
- Die Java-Erweiterungen in VSCode handhaben den Classpath und Build-Prozess automatisch basierend auf Ihrer `pom.xml`, daher müssen Sie typischerweise nicht manuell vorher `mvn clean install` ausführen.
- Wenn Ihr Projekt Teil eines Multi-Modul Maven-Setups ist, stellen Sie sicher, dass der `projectName` mit dem korrekten `artifactId` des Moduls übereinstimmt.
- Für erweiterte Konfigurationen (z.B. benutzerdefinierte Arbeitsverzeichnisse oder Pre-Launch Tasks), konsultieren Sie die [VSCode Java Debugging Dokumentation](https://code.visualstudio.com/docs/java/java-debugging).

Mit diesem Setup sollte Ihre `launch.json` korrekt konfiguriert sein, um Ihr Maven Spring Boot Projekt in VSCode auszuführen und zu debuggen!