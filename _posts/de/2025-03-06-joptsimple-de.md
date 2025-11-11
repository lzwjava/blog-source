---
audio: false
generated: true
lang: de
layout: post
title: Kommandozeilenoptionen in Java parsen
translated: true
type: note
---

JOptSimple ist eine Java-Bibliothek, die entwickelt wurde, um das Parsen von Kommandozeilenoptionen in Ihren Anwendungen zu vereinfachen. Sie ermöglicht es Ihnen, Optionen wie Flags (z.B. `-v` für den ausführlichen Modus) und Optionen mit Argumenten (z.B. `--file input.txt`) auf flexible und intuitive Weise zu definieren und zu verarbeiten. Nachfolgend finden Sie eine Schritt-für-Schritt-Anleitung zur effektiven Verwendung von JOptSimple.

---

### **Schritt 1: JOptSimple zu Ihrem Projekt hinzufügen**
Um JOptSimple zu verwenden, müssen Sie es zunächst in Ihr Java-Projekt einbinden. Wenn Sie Maven verwenden, fügen Sie die folgende Abhängigkeit zu Ihrer `pom.xml`-Datei hinzu:

```xml
<dependency>
    <groupId>net.sf.jopt-simple</groupId>
    <artifactId>jopt-simple</artifactId>
    <version>5.0.4</version>
</dependency>
```

Stellen Sie sicher, dass Sie die neueste Version auf Maven Central überprüfen, da `5.0.4` möglicherweise nicht die aktuellste ist. Für andere Build-Tools wie Gradle können Sie die Abhängigkeit entsprechend anpassen (z.B. `implementation 'net.sf.jopt-simple:jopt-simple:5.0.4'`).

---

### **Schritt 2: Einen OptionParser erstellen**
Das Herzstück von JOptSimple ist die Klasse `OptionParser`, die Sie zum Definieren und Parsen von Kommandozeilenoptionen verwenden. Beginnen Sie, indem Sie eine Instanz davon in Ihrer `main`-Methode erstellen:

```java
import joptsimple.OptionParser;
import joptsimple.OptionSet;

public class MyApp {
    public static void main(String[] args) {
        OptionParser parser = new OptionParser();
        // Optionen hier definieren (siehe Schritt 3)
    }
}
```

---

### **Schritt 3: Kommandozeilenoptionen definieren**
Sie können Optionen mit den Methoden `accepts` oder `acceptsAll` definieren. Optionen können Flags (ohne Argumente) oder Optionen sein, die Argumente erfordern (z.B. ein Dateiname oder eine Zahl). So richten Sie sie ein:

- **Flags**: Verwenden Sie `accepts` für einen einzelnen Optionsnamen oder `acceptsAll`, um Aliase anzugeben (z.B. `-v` und `--verbose`):
  ```java
  parser.acceptsAll(Arrays.asList("v", "verbose"), "aktiviert den ausführlichen Modus");
  ```

- **Optionen mit Argumenten**: Verwenden Sie `withRequiredArg()`, um anzuzeigen, dass eine Option einen Wert benötigt, und geben Sie optional ihren Typ mit `ofType()` an:
  ```java
  parser.acceptsAll(Arrays.asList("f", "file"), "gibt die Eingabedatei an").withRequiredArg();
  parser.acceptsAll(Arrays.asList("c", "count"), "gibt die Anzahl an").withRequiredArg().ofType(Integer.class).defaultsTo(0);
  ```

  - `defaultsTo(0)` setzt einen Standardwert (z.B. `0`), wenn die Option nicht angegeben wird.
  - `ofType(Integer.class)` stellt sicher, dass das Argument als Integer geparst wird.

- **Hilfe-Option**: Fügen Sie ein Hilfe-Flag hinzu (z.B. `-h` oder `--help`), um Nutzungsinformationen anzuzeigen:
  ```java
  parser.acceptsAll(Arrays.asList("h", "help"), "zeigt diese Hilfenachricht an");
  ```

---

### **Schritt 4: Die Kommandozeilenargumente parsen**
Übergeben Sie das `args`-Array aus Ihrer `main`-Methode an den Parser, um die Kommandozeileneingabe zu verarbeiten. Dies gibt ein `OptionSet`-Objekt zurück, das die geparsten Optionen enthält:

```java
OptionSet options = parser.parse(args);
```

Setzen Sie dies in einen `try-catch`-Block, um Parsing-Fehler abzufangen (z.B. ungültige Optionen oder fehlende Argumente):

```java
try {
    OptionSet options = parser.parse(args);
    // Optionen verarbeiten (siehe Schritt 5)
} catch (Exception e) {
    System.err.println("Fehler: " + e.getMessage());
    try {
        parser.printHelpOn(System.err);
    } catch (IOException ex) {
        ex.printStackTrace();
    }
    System.exit(1);
}
```

---

### **Schritt 5: Auf geparste Optionen zugreifen**
Verwenden Sie das `OptionSet`, um nach Flags zu suchen, Optionswerte abzurufen und Nicht-Optionsargumente zu erhalten:

- **Auf Flags prüfen**: Verwenden Sie `has()`, um zu prüfen, ob ein Flag vorhanden ist:
  ```java
  boolean verbose = options.has("v");
  if (verbose) {
      System.out.println("Ausführlicher Modus aktiviert");
  }
  ```

- **Optionswerte abrufen**: Verwenden Sie `valueOf()`, um das Argument einer Option abzurufen, und casten Sie es bei Bedarf auf den entsprechenden Typ:
  ```java
  String fileName = (String) options.valueOf("f"); // Gibt null zurück, wenn nicht angegeben
  int count = (Integer) options.valueOf("c");     // Gibt 0 zurück aufgrund von defaultsTo(0)
  ```

  Wenn Sie `ofType()` und `defaultsTo()` angegeben haben, gibt `valueOf()` den typisierten Wert oder den Standardwert zurück.

- **Nicht-Optionsargumente**: Holen Sie sich Argumente, die nicht an Optionen gebunden sind (z.B. eine Liste von Dateien), mit `nonOptionArguments()`:
  ```java
  List<String> files = options.nonOptionArguments();
  System.out.println("Dateien: " + files);
  ```

- **Hilfe behandeln**: Drucken Sie Nutzungsinformationen, wenn die Hilfe-Option vorhanden ist:
  ```java
  if (options.has("h")) {
      parser.printHelpOn(System.out);
      System.exit(0);
  }
  ```

---

### **Beispiel: Alles zusammenfügen**
Hier ist ein vollständiges Beispiel eines Programms, das ein ausführliches Flag, eine Zähloption und eine Liste von Dateien akzeptiert:

```java
import joptsimple.OptionParser;
import joptsimple.OptionSet;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

public class MyApp {
    public static void main(String[] args) {
        OptionParser parser = new OptionParser();
        parser.acceptsAll(Arrays.asList("v", "verbose"), "aktiviert den ausführlichen Modus");
        parser.acceptsAll(Arrays.asList("c", "count"), "gibt die Anzahl an")
              .withRequiredArg()
              .ofType(Integer.class)
              .defaultsTo(0);
        parser.acceptsAll(Arrays.asList("h", "help"), "zeigt diese Hilfenachricht an");

        try {
            OptionSet options = parser.parse(args);

            if (options.has("h")) {
                parser.printHelpOn(System.out);
                System.exit(0);
            }

            boolean verbose = options.has("v");
            int count = (Integer) options.valueOf("c");
            List<String> files = options.nonOptionArguments();

            if (verbose) {
                System.out.println("Ausführlicher Modus aktiviert");
            }
            System.out.println("Anzahl: " + count);
            System.out.println("Dateien: " + files);

        } catch (Exception e) {
            System.err.println("Fehler: " + e.getMessage());
            try {
                parser.printHelpOn(System.err);
            } catch (IOException ex) {
                ex.printStackTrace();
            }
            System.exit(1);
        }
    }
}
```

Führen Sie dies aus mit: `java MyApp -v -c 5 datei1 datei2`, und es gibt aus:
```
Ausführlicher Modus aktiviert
Anzahl: 5
Dateien: [datei1, datei2]
```

Führen Sie es mit `-h` aus, und es zeigt die Nutzungsnachricht mit allen definierten Optionen an.

---

### **Zusätzliche Funktionen**
- **Mehrere Werte**: Erlauben Sie, dass eine Option mehrmals vorkommt (z.B. `-I verz1 -I verz2`):
  ```java
  parser.accepts("I").withRequiredArg().ofType(String.class);
  List<String> includes = options.valuesOf("I"); // Gibt eine Liste zurück
  ```

- **Optionale Argumente**: Verwenden Sie `withOptionalArg()` anstelle von `withRequiredArg()`, wenn ein Argument nicht zwingend erforderlich ist:
  ```java
  parser.accepts("o").withOptionalArg().ofType(String.class);
  ```

- **Fehlerbehandlung**: JOptSimple wirft eine `OptionException` für Parsing-Fehler, die Sie abfangen können, um benutzerfreundliches Feedback zu geben.

---

### **Zusammenfassung**
JOptSimple macht es einfach, Kommandozeilenoptionen in Java zu behandeln. Sie:
1. Fügen die Bibliothek zu Ihrem Projekt hinzu.
2. Erstellen einen `OptionParser` und definieren Optionen (Flags, Argumente, Standardwerte).
3. Parsen das `args`-Array in ein `OptionSet`.
4. Verwenden das `OptionSet`, um auf Flags, Werte und Nicht-Optionsargumente zuzugreifen.
5. Behandeln Fehler und stellen bei Bedarf Hilfe bereit.

Mit dieser Grundlage können Sie robuste Kommandozeilenschnittstellen erstellen, die auf die Bedürfnisse Ihrer Anwendung zugeschnitten sind!