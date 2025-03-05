---
audio: false
generated: true
lang: de
layout: post
title: Befehlszeilenargumente in Java analysieren
translated: true
---

Um `net.sourceforge.argparse4j` zu verwenden, eine Java-Bibliothek zum Parsen von Befehlszeilenargumenten, die von Pythons `argparse` inspiriert ist, befolgen Sie diese Schritte:

---

### 1. **Abhängigkeit hinzufügen**
Um `argparse4j` in Ihr Projekt zu integrieren, fügen Sie es als Abhängigkeit hinzu. Wenn Sie Maven verwenden, aktualisieren Sie Ihre `pom.xml` wie folgt:

```xml
<dependency>
    <groupId>net.sourceforge.argparse4j</groupId>
    <artifactId>argparse4j</artifactId>
    <version>0.9.0</version>
</dependency>
```

Für andere Build-Tools wie Gradle, überprüfen Sie das [Maven Central Repository](https://central.sonatype.com/artifact/net.sourceforge.argparse4j/argparse4j) für die entsprechende Konfiguration.

---

### 2. **Erstellen Sie ein `ArgumentParser`-Objekt**
Erstellen Sie eine `ArgumentParser`-Instanz mit `ArgumentParsers.newFor("prog").build()`, wobei `"prog"` der Name Ihres Programms ist. Sie können auch eine Beschreibung hinzufügen und die automatische Hilfeerstellung aktivieren.

**Beispiel:**
```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;

ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
    .defaultHelp(true)  // Aktiviert die -h/--help-Option
    .description("Berechne die Prüfsumme der angegebenen Dateien.");
```

---

### 3. **Argument hinzufügen**
Definieren Sie die Befehlszeilenargumente, die Ihr Programm akzeptieren wird, mit `parser.addArgument()`. Sie können:
- **Optionale Argumente** (z.B. `-t`, `--type`) mit Flags, Auswahlmöglichkeiten, Standardwerten und Hilfetexten.
- **Positionale Argumente** (z.B. `file`) mit optionaler Unterstützung für variable Längen mit `.nargs("*")`.

**Beispiel:**
```java
parser.addArgument("-t", "--type")
    .choices("SHA-256", "SHA-512", "SHA1")  // Beschränken auf diese Optionen
    .setDefault("SHA-256")                  // Standardwert, wenn nicht angegeben
    .help("Geben Sie die zu verwendende Hash-Funktion an");  // Beschreibung für die Hilfemeldung

parser.addArgument("file")
    .nargs("*")                             // Akzeptiert null oder mehr Argumente
    .help("Datei, für die die Prüfsumme berechnet werden soll");    // Beschreibung für die Hilfemeldung
```

---

### 4. **Befehlszeilenargumente parsen**
Parsen Sie die Befehlszeilenargumente (normalerweise als `String[] args` aus Ihrer `main`-Methode) mit `parser.parseArgs()`. Umfassen Sie dies in einen try-catch-Block, um Parsing-Fehler anmutig zu behandeln.

**Beispiel:**
```java
import net.sourceforge.argparse4j.inf.Namespace;
import net.sourceforge.argparse4j.inf.ArgumentParserException;

public class Checksum {
    public static void main(String[] args) {
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("Berechne die Prüfsumme der angegebenen Dateien.");

        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("Geben Sie die zu verwendende Hash-Funktion an");
        parser.addArgument("file").nargs("*")
            .help("Datei, für die die Prüfsumme berechnet werden soll");

        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);  // Argumente parsen
        } catch (ArgumentParserException e) {
            parser.handleError(e);        // Fehler und Hilfemeldung ausgeben
            System.exit(1);               // Beim Fehler beenden
        }
    }
}
```

---

### 5. **Geparste Werte abrufen**
Die Methode `parseArgs()` gibt ein `Namespace`-Objekt zurück, das die geparsten Argumentwerte enthält. Verwenden Sie Methoden wie `getString()` oder `getList()`, um diese abzurufen.

**Beispiel:**
```java
String hashType = ns.getString("type");  // z.B. "SHA-256"
List<String> files = ns.getList("file"); // Liste der Dateinamen

System.out.println("Hash-Typ: " + hashType);
System.out.println("Dateien: " + files);
```

---

### Alles zusammen
Hier ist ein vollständiges Beispiel:

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
            .description("Berechne die Prüfsumme der angegebenen Dateien.");

        // Schritt 3: Argumente hinzufügen
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("Geben Sie die zu verwendende Hash-Funktion an");
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

        // Schritt 5: Geparste Werte abrufen
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
- **Automatische Hilfe**: Führen Sie Ihr Programm mit `-h` oder `--help` aus, um eine generierte Hilfemeldung zu sehen.
- **Unterbefehle**: Verwenden Sie `parser.addSubparsers()` für komplexe Befehle (z.B. `git commit`, `git push`).
- **Annotations**: Binden Sie Argumente mit Annotationen an Klassenfelder (siehe Benutzerhandbuch für Details).

Für eine erweiterte Nutzung konsultieren Sie das [Argparse4j Benutzerhandbuch](https://argparse4j.github.io/userguide.html).

---

Dieser Workflow ermöglicht es Ihnen, Befehlszeilenargumente in Ihrer Java-Anwendung mit `net.sourceforge.argparse4j` einfach zu parsen und zu verarbeiten.