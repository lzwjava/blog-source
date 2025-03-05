---
audio: false
generated: true
lang: de
layout: post
title: 'Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java


  Parsing Command-line Options in Java'
translated: true
---

JOptSimple ist eine Java-Bibliothek, die entwickelt wurde, um das Parsen von Befehlszeilenoptionen in Ihren Anwendungen zu vereinfachen. Sie ermöglicht es Ihnen, Optionen wie Flags (z. B. `-v` für den ausführlichen Modus) und Optionen mit Argumenten (z. B. `--file input.txt`) auf flexible und intuitive Weise zu definieren und zu verarbeiten. Hier ist eine Schritt-für-Schritt-Anleitung zur effektiven Verwendung von JOptSimple.

---

### **Schritt 1: JOptSimple zu Ihrem Projekt hinzufügen**
Um JOptSimple zu verwenden, müssen Sie es zuerst in Ihr Java-Projekt einbinden. Wenn Sie Maven verwenden, fügen Sie die folgende Abhängigkeit zu Ihrer `pom.xml`-Datei hinzu:

```xml
<dependency>
    <groupId>net.sf.jopt-simple</groupId>
    <artifactId>jopt-simple</artifactId>
    <version>5.0.4</version>
</dependency>
```

Stellen Sie sicher, dass Sie die neueste Version auf Maven Central überprüfen, da `5.0.4` möglicherweise nicht die aktuellste ist. Für andere Build-Tools wie Gradle können Sie die Abhängigkeit entsprechend anpassen (z. B. `implementation 'net.sf.jopt-simple:jopt-simple:5.0.4'`).

---

### **Schritt 2: Erstellen eines OptionParsers**
Das Herzstück von JOptSimple ist die `OptionParser`-Klasse, die Sie verwenden, um Befehlszeilenoptionen zu definieren und zu parsen. Beginnen Sie damit, eine Instanz davon in Ihrer `main`-Methode zu erstellen:

```java
import joptsimple.OptionParser;
import joptsimple.OptionSet;

public class MyApp {
    public static void main(String[] args) {
        OptionParser parser = new OptionParser();
        // Definieren Sie hier Optionen (siehe Schritt 3)
    }
}
```

---

### **Schritt 3: Definieren von Befehlszeilenoptionen**
Sie können Optionen mit den Methoden `accepts` oder `acceptsAll` definieren. Optionen können Flags (keine Argumente) oder Optionen sein, die Argumente benötigen (z. B. ein Dateiname oder eine Zahl). Hier ist, wie Sie sie einrichten:

- **Flags**: Verwenden Sie `accepts` für einen einzelnen Optionsnamen oder `acceptsAll`, um Aliase zu spezifizieren (z. B. `-v` und `--verbose`):
  ```java
  parser.acceptsAll(Arrays.asList("v", "verbose"), "Aktivieren Sie den ausführlichen Modus");
  ```

- **Optionen mit Argumenten**: Verwenden Sie `withRequiredArg()`, um anzugeben, dass eine Option einen Wert benötigt, und optional den Typ mit `ofType()` spezifizieren:
  ```java
  parser.acceptsAll(Arrays.asList("f", "file"), "Geben Sie die Eingabedatei an").withRequiredArg();
  parser.acceptsAll(Arrays.asList("c", "count"), "Geben Sie die Anzahl an").withRequiredArg().ofType(Integer.class).defaultsTo(0);
  ```

  - `defaultsTo(0)` setzt einen Standardwert (z. B. `0`), wenn die Option nicht angegeben ist.
  - `ofType(Integer.class)` stellt sicher, dass das Argument als Ganzzahl geparst wird.

- **Hilfe-Option**: Fügen Sie eine Hilfe-Flag (z. B. `-h` oder `--help`) hinzu, um Nutzungsinformationen anzuzeigen:
  ```java
  parser.acceptsAll(Arrays.asList("h", "help"), "Zeigen Sie diese Hilfemeldung an");
  ```

---

### **Schritt 4: Parsen der Befehlszeilenargumente**
Geben Sie das `args`-Array aus Ihrer `main`-Methode an den Parser weiter, um die Befehlszeileneingabe zu verarbeiten. Dies gibt ein `OptionSet`-Objekt zurück, das die geparsten Optionen enthält:

```java
OptionSet options = parser.parse(args);
```

Umhüllen Sie dies in einem `try-catch`-Block, um Parsing-Fehler (z. B. ungültige Optionen oder fehlende Argumente) zu behandeln:

```java
try {
    OptionSet options = parser.parse(args);
    // Verarbeiten Sie Optionen (siehe Schritt 5)
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

### **Schritt 5: Zugriff auf geparste Optionen**
Verwenden Sie das `OptionSet`, um Flags zu überprüfen, Optionenwerte abzurufen und nicht-Option-Argumente zu erhalten:

- **Überprüfen von Flags**: Verwenden Sie `has()`, um zu sehen, ob ein Flag vorhanden ist:
  ```java
  boolean verbose = options.has("v");
  if (verbose) {
      System.out.println("Ausführlicher Modus aktiviert");
  }
  ```

- **Abrufen von Optionswerten**: Verwenden Sie `valueOf()`, um das Argument einer Option abzurufen, und gießen Sie es bei Bedarf in den entsprechenden Typ:
  ```java
  String fileName = (String) options.valueOf("f"); // Gibt null zurück, wenn nicht angegeben
  int count = (Integer) options.valueOf("c");     // Gibt 0 aufgrund von defaultsTo(0) zurück
  ```

  Wenn Sie `ofType()` und `defaultsTo()` angegeben haben, gibt `valueOf()` den typisierten Wert oder den Standardwert zurück.

- **Nicht-Option-Argumente**: Holen Sie sich Argumente, die nicht an Optionen gebunden sind (z. B. eine Liste von Dateien) mit `nonOptionArguments()`:
  ```java
  List<String> files = options.nonOptionArguments();
  System.out.println("Dateien: " + files);
  ```

- **Hilfe behandeln**: Zeigen Sie Nutzungsinformationen an, wenn die Hilfe-Option vorhanden ist:
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
        parser.acceptsAll(Arrays.asList("v", "verbose"), "Aktivieren Sie den ausführlichen Modus");
        parser.acceptsAll(Arrays.asList("c", "count"), "Geben Sie die Anzahl an")
              .withRequiredArg()
              .ofType(Integer.class)
              .defaultsTo(0);
        parser.acceptsAll(Arrays.asList("h", "help"), "Zeigen Sie diese Hilfemeldung an");

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

Führen Sie dies mit `java MyApp -v -c 5 file1 file2` aus, und es gibt aus:
```
Ausführlicher Modus aktiviert
Anzahl: 5
Dateien: [file1, file2]
```

Führen Sie es mit `-h` aus, und es zeigt die Nutzungsmeldung mit allen definierten Optionen an.

---

### **Zusätzliche Funktionen**
- **Mehrere Werte**: Erlauben Sie einer Option, mehrfach aufzutreten (z. B. `-I dir1 -I dir2`):
  ```java
  parser.accepts("I").withRequiredArg().ofType(String.class);
  List<String> includes = options.valuesOf("I"); // Gibt eine Liste zurück
  ```

- **Optionale Argumente**: Verwenden Sie `withOptionalArg()` anstelle von `withRequiredArg()`, wenn ein Argument nicht verpflichtend ist:
  ```java
  parser.accepts("o").withOptionalArg().ofType(String.class);
  ```

- **Fehlerbehandlung**: JOptSimple wirft eine `OptionException` bei Parsing-Fehlern, die Sie fangen können, um benutzerfreundliche Rückmeldungen zu geben.

---

### **Zusammenfassung**
JOptSimple macht es einfach, Befehlszeilenoptionen in Java zu verarbeiten. Sie:
1. Fügen Sie die Bibliothek zu Ihrem Projekt hinzu.
2. Erstellen Sie einen `OptionParser` und definieren Sie Optionen (Flags, Argumente, Standards).
3. Parsen Sie das `args`-Array in ein `OptionSet`.
4. Verwenden Sie das `OptionSet`, um auf Flags, Werte und nicht-Option-Argumente zuzugreifen.
5. Behandeln Sie Fehler und bieten Sie Hilfe nach Bedarf an.

Mit dieser Grundlage können Sie robuste Befehlszeilenschnittstellen erstellen, die auf die Bedürfnisse Ihrer Anwendung zugeschnitten sind!