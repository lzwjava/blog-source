---
audio: false
generated: true
lang: de
layout: post
title: Kommandozeilenargumente in Java parsen
translated: true
type: note
---

Um `net.sourceforge.argparse4j`, eine Java-Bibliothek zum Parsen von Kommandozeilenargumenten, inspiriert von Pythons `argparse`, zu verwenden, folgen Sie diesen Schritten:

---

### 1. **Abhängigkeit hinzufügen**
Um `argparse4j` in Ihr Projekt einzubinden, fügen Sie es als Abhängigkeit hinzu. Wenn Sie Maven verwenden, aktualisieren Sie Ihre `pom.xml` mit folgendem Eintrag:

```xml
<dependency>
    <groupId>net.sourceforge.argparse4j</groupId>
    <artifactId>argparse4j</artifactId>
    <version>0.9.0</version>
</dependency>
```

Für andere Build-Tools wie Gradle, prüfen Sie das [Maven Central Repository](https://central.sonatype.com/artifact/net.sourceforge.argparse4j/argparse4j) für die entsprechende Konfiguration.

---

### 2. **Ein `ArgumentParser`-Objekt erstellen**
Beginnen Sie mit der Erstellung einer `ArgumentParser`-Instanz mittels `ArgumentParsers.newFor("prog").build()`, wobei `"prog"` der Name Ihres Programms ist. Sie können auch eine Beschreibung hinzufügen und die automatische Hilfe-Generierung aktivieren.

**Beispiel:**
```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;

ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
    .defaultHelp(true)  // Aktiviert die -h/--help Option
    .description("Berechnet die Prüfsumme der angegebenen Dateien.");
```

---

### 3. **Argumente hinzufügen**
Definieren Sie die Kommandozeilenargumente, die Ihr Programm akzeptieren soll, mit `parser.addArgument()`. Sie können angeben:
- **Optionale Argumente** (z.B. `-t`, `--type`) mit Flags, Auswahlmöglichkeiten, Standardwerten und Hilfetext.
- **Positionelle Argumente** (z.B. `file`) mit optionaler Unterstützung für variabler Länge mittels `.nargs("*")`.

**Beispiel:**
```java
parser.addArgument("-t", "--type")
    .choices("SHA-256", "SHA-512", "SHA1")  // Beschränkung auf diese Optionen
    .setDefault("SHA-256")                  // Standardwert, falls nicht angegeben
    .help("Spezifiziert die zu verwendende Hash-Funktion");  // Beschreibung für die Hilfenachricht

parser.addArgument("file")
    .nargs("*")                             // Akzeptiert null oder mehr Argumente
    .help("Datei, für die die Prüfsumme berechnet werden soll"); // Beschreibung für die Hilfenachricht
```

---

### 4. **Kommandozeilenargumente parsen**
Parsen Sie die Kommandozeilenargumente (typischerweise als `String[] args` aus Ihrer `main`-Methode übergeben) mit `parser.parseArgs()`. Umschließen Sie dies mit einem try-catch-Block, um Parsing-Fehler abzufangen.

**Beispiel:**
```java
import net.sourceforge.argparse4j.inf.Namespace;
import net.sourceforge.argparse4j.inf.ArgumentParserException;

public class Checksum {
    public static void main(String[] args) {
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("Berechnet die Prüfsumme der angegebenen Dateien.");
        
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("Spezifiziert die zu verwendende Hash-Funktion");
        parser.addArgument("file").nargs("*")
            .help("Datei, für die die Prüfsumme berechnet werden soll");

        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);  // Argumente parsen
        } catch (ArgumentParserException e) {
            parser.handleError(e);        // Druckt Fehler und Hilfenachricht
            System.exit(1);               // Beendet bei Fehler
        }
    }
}
```

---

### 5. **Auf geparste Werte zugreifen**
Die Methode `parseArgs()` gibt ein `Namespace`-Objekt zurück, das die geparsten Argumentwerte enthält. Verwenden Sie Methoden wie `getString()` oder `getList()`, um sie abzurufen.

**Beispiel:**
```java
String hashType = ns.getString("type");  // z.B. "SHA-256"
List<String> files = ns.getList("file"); // Liste der Dateinamen

System.out.println("Hash-Typ: " + hashType);
System.out.println("Dateien: " + files);
```

---

### Alles zusammen
Hier ein vollständiges Beispiel:

```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;
import net.sourceforge.argparse4j.inf.ArgumentParserException;
import net.sourceforge.argparse4j.inf.Namespace;
import java.util.List;

public class Checksum {
    public static void main(String[] args) {
        // Schritt 2: Parser erstellen
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("Berechnet die Prüfsumme der angegebenen Dateien.");

        // Schritt 3: Argumente hinzufügen
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("Spezifiziert die zu verwendende Hash-Funktion");
        parser.addArgument("file").nargs("*")
            .help("Datei, für die die Prüfsumme berechnet werden soll");

        // Schritt 4: Argumente parsen
        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);
        } catch (ArgumentParserException e) {
            parser.handleError(e);
            System.exit(1);
        }

        // Schritt 5: Auf geparste Werte zugreifen
        String hashType = ns.getString("type");
        List<String> files = ns.getList("file");

        // Beispielausgabe
        System.out.println("Hash-Typ: " + hashType);
        System.out.println("Dateien: " + files);
    }
}
```

---

### Zusätzliche Funktionen
- **Automatische Hilfe**: Führen Sie Ihr Programm mit `-h` oder `--help` aus, um eine generierte Hilfenachricht zu sehen.
- **Subcommands**: Verwenden Sie `parser.addSubparsers()` für komplexe Befehle (z.B. `git commit`, `git push`).
- **Annotationen**: Binden Sie Argumente an Klassenfelder mittels Annotationen (siehe Benutzerhandbuch für Details).

Für fortgeschrittene Verwendung, konsultieren Sie das [Argparse4j Benutzerhandbuch](https://argparse4j.github.io/userguide.html).

---

Dieser Arbeitsablauf ermöglicht es Ihnen, Kommandozeilenargumente in Ihrer Java-Anwendung einfach mit `net.sourceforge.argparse4j` zu parsen und zu verarbeiten.