---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: JavaCC-Quell- und Klassenverzeichnisse
translated: true
type: note
---

### JavaCC-Übersicht
JavaCC (Java Compiler Compiler) ist ein Tool, das Java-Quellcode (z.B. Parser-Klassen) aus Grammatik-Spezifikationsdateien (.jj-Dateien) erzeugt. Es kompiliert Code **nicht** direkt in Bytecode (.class-Dateien) – das übernimmt ein standard Java-Compiler wie `javac`. Wenn Sie JavaCC programmatisch verwenden (z.B. in einer IDE oder Laufzeitumgebung), um dynamischen Code zu generieren und zu kompilieren, hängen die Ausgabepfade von Ihrer Konfiguration ab. Ich werde dies Schritt für Schritt basierend auf dem standardmäßigen JavaCC-Verhalten und gängigen Nutzungsmustern aufschlüsseln.

### Wo JavaCC Quelldateien erzeugt
- **Standardausgabeverzeichnis**: JavaCC gibt generierte `.java`-Dateien im **aktuellen Arbeitsverzeichnis** aus (oder in einem Unterverzeichnis namens "output", falls nicht anders angegeben). Sie können dies mit Kommandozeilenoptionen wie `-OUTPUT_DIRECTORY=<Pfad>` überschreiben oder programmatisch über die `JavaCCOptions`-Klasse, wenn Sie es im Code aufrufen.
- **Beispiel für Kommandozeilenverwendung**:
  ```
  javacc -OUTPUT_DIRECTORY=/pfad/zu/generiert MyGrammar.jj
  ```
  Dies würde `.java`-Dateien (z.B. `Token`, `Parser`, `ParseException`) in `/pfad/zu/generiert` erstellen.
- **Programmatische Verwendung**: Wenn Sie JavaCC aus Ihrer Java-Anwendung heraus aufrufen (z.B. mit `org.javacc.JavaCC.main()` oder ähnlichen APIs), können Sie Optionen setzen, um den Ausgabepfad anzugeben. Die Quelldateien sind einfache `.java`-Dateien, die noch kompiliert werden müssen.

Dies entspricht der offiziellen JavaCC-Dokumentation (z.B. vom legacy JavaCC-Projekt auf SourceForge oder Maven-basierten Distributionen), die besagt, dass generierte Klassen als Quellcode im angegebenen Verzeichnis ausgegeben werden, nicht als Bytecode.

### Wo kompilierte Klassen gespeichert werden, wenn Sie den generierten Code kompilieren
JavaCC selbst kompiliert nicht in `.class`-Dateien – Sie müssen dies manuell erledigen oder in Ihrem Code automatisieren. So geht es weiter:

- **Manuelle Kompilierung**: Verwenden Sie `javac` für die generierten `.java`-Dateien:
  ```
  javac -d /pfad/zu/classes MyGeneratedParser.java
  ```
  - Das `-d`-Flag gibt das Ausgabeverzeichnis für `.class`-Dateien an, oft ein `classes/`-Ordner oder das Build-Target Ihres Projekts (z.B. `target/classes/` in Maven/Gradle).
  - Übliche Orte: `bin/`, `build/classes/` oder `target/classes/` abhängig von Ihrem Build-System (z.B. Ant, Maven).

- **Dynamische Kompilierung im Code**: Wenn Sie JavaCC zur Laufzeit verwenden, um Parser für dynamischen Code zu generieren (z.B. für Skript-Interpretation oder On-the-Fly-Parsing), würden Sie typischerweise:
  1. Die `.java`-Dateien programmatisch generieren (z.B. durch Schreiben in ein Temp-Verzeichnis wie `System.getProperty("java.io.tmpdir")`).
  2. Sie mit der Java Compiler API (javax.tools.JavaCompiler) oder einer Bibliothek wie Janino kompilieren.
     - Beispiel: Setzen Sie die Kompilierungsausgabe auf ein benutzerdefiniertes Verzeichnis, wie `new File("generated/classes")`.
     - Die kompilierten `.class`-Dateien werden in diesem Verzeichnis gespeichert. Zur Laufzeit verwenden Sie einen benutzerdefinierten ClassLoader, um sie von dort oder aus In-Memory-Puffern zu laden.
  - **JVM-Standard**: Ohne benutzerdefinierte Pfade landen Klassen standardmäßig in `target/classes`, wenn Build-Tools verwendet werden, oder in einem beliebigen Verzeichnis, das Sie in der Kompilierungsaufgabe angeben.

- **Häufige dynamische Szenarien**:
  - **In-Memory-Kompilierung**: Bibliotheken wie die Compiler API erlauben Kompilierung ohne Schreiben auf die Festplatte, wobei Bytecode via `ClassLoader.defineClass()` im Speicher gespeichert wird. Es findet keine physische Speicherung statt.
  - **Temporäre Speicherung**: Wenn der generierte Code kompiliert und persistent gespeichert wird, landet er oft in `/tmp/` auf Unix-ähnlichen Systemen oder temporären Ordnern. Für Produktions-Apps verwenden Sie ein dediziertes `generated/`- oder `cache/`-Verzeichnis im Dateisystem Ihres Projekts.
  - **Frameworks**: Tools wie ANTLR (Alternative zu JavaCC) oder benutzerdefinierte Runner automatisieren dies möglicherweise und speichern Klassen im RAM oder in einem Classpath-Ordner (z.B. `CLASSPATH`-Einträge).

### Wichtige Überlegungen und Best Practices
- **Laufzeitsicherheit**: Dynamisches Kompilieren von Code birgt Risiken (z.B. Sicherheitsprobleme). Stellen Sie sicher, dass benutzergenerierte Grammatiken in einer Sandbox laufen.
- **Build-Tools-Integration**: Bei Verwendung von Maven oder Gradle geben JavaCC-Plugins (z.B. `javacc-maven-plugin`) Quellcode in `target/generated-sources/javacc/` und kompilierte Klassen in `target/classes/` aus, konfigurierbar in Ihrer `pom.xml` oder `build.gradle`.
- **Debugging**: Wenn die Kompilierung fehlschlägt, überprüfen Sie die JavaCC-Fehlerausgabe oder Logs. Generierte Dateien werden typischerweise dort gespeichert, wo Ihre App läuft, nicht global.
- **Belege aus der Dokumentation**: Laut dem offiziellen JavaCC-Leitfaden (javacc.github.io oder legacy-Docs) ist die Ausgabe verzeichnisbasiert und die Nachbearbeitung liegt in der Hand des Benutzers. Beispiele aus der Praxis in GitHub-Repositories (z.B. Suche nach JavaCC-Verwendung) zeigen benutzerdefinierte Ausgabeverzeichnisse wie `src/main/generated/`.

Wenn dies nicht Ihrer Einrichtung entspricht (z.B. ein bestimmtes Framework oder eine IDE), geben Sie mehr Details wie Ihren Code-Snippet oder Ihre Umgebung an, und ich kann die Antwort verfeinern!