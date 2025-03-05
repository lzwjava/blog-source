---
audio: false
generated: true
lang: de
layout: post
title: Konsoleneingabe in Java lesen
translated: true
---

Um das `org.jline.reader`-Paket in Java zu verwenden, das Teil der JLine-Bibliothek zur Handhabung von Konsoleneingaben mit erweiterten Funktionen wie Zeilenbearbeitung, Verlauf und Vervollständigung ist, befolgen Sie diese Schritte. Diese Anleitung bietet einen vollständigen und praktischen Ansatz, um Sie zum Start zu bringen.

### Voraussetzungen
Stellen Sie sicher, dass die JLine-Bibliothek zu Ihrem Projekt hinzugefügt ist. Wenn Sie Maven verwenden, fügen Sie die folgende Abhängigkeit in Ihre `pom.xml` ein:

```xml
<dependency>
    <groupId>org.jline</groupId>
    <artifactId>jline</artifactId>
    <version>3.21.0</version> <!-- Verwenden Sie die neueste Version -->
</dependency>
```

### Grundlegende Schritte zur Verwendung von `org.jline.reader`

1. **Erstellen Sie eine Terminal-Instanz**
   - Verwenden Sie die `TerminalBuilder`-Klasse aus `org.jline.terminal`, um ein `Terminal`-Objekt zu erstellen. Dies stellt die Konsolenumgebung dar, in der die Eingabe gelesen wird.
   - Beispiel:
     ```java
     import org.jline.terminal.Terminal;
     import org.jline.terminal.TerminalBuilder;

     Terminal terminal = TerminalBuilder.builder().build();
     ```
   - Die `build()`-Methode erstellt ein Standard-Terminal, das für die meisten Umgebungen geeignet ist. Sie können es weiter anpassen (z. B. Festlegen des Terminaltyps), aber das Standard-Terminal ist oft ausreichend.

2. **Erstellen Sie eine LineReader-Instanz**
   - Verwenden Sie die `LineReaderBuilder`-Klasse aus `org.jline.reader`, um ein `LineReader`-Objekt zu erstellen, und übergeben Sie die `Terminal`-Instanz daran.
   - Der `LineReader` ist die Hauptschnittstelle zum Lesen der Benutzereingabe mit JLines Funktionen.
   - Beispiel:
     ```java
     import org.jline.reader.LineReader;
     import org.jline.reader.LineReaderBuilder;

     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .build();
     ```

3. **Lesen Sie die Eingabe vom Benutzer**
   - Verwenden Sie die `readLine()`-Methode von `LineReader`, um eine vom Benutzer eingegebene Textzeile zu lesen. Sie können optional eine Eingabeaufforderung angeben, die angezeigt werden soll.
   - Beispiel:
     ```java
     String line = reader.readLine("> ");
     ```
   - Dies zeigt `> ` als Eingabeaufforderung an, wartet auf die Benutzereingabe und gibt die eingegebene Zeichenfolge zurück, wenn der Benutzer die Eingabetaste drückt.

### Einfaches Beispiel
Hier ist ein vollständiges, minimales Beispiel, das die Benutzereingabe in einer Schleife liest, bis der Benutzer "exit" eingibt:

```java
import org.jline.reader.LineReader;
import org.jline.reader.LineReaderBuilder;
import org.jline.terminal.Terminal;
import org.jline.terminal.TerminalBuilder;

public class ConsoleExample {
    public static void main(String[] args) throws Exception {
        // Erstellen Sie Terminal
        Terminal terminal = TerminalBuilder.builder().build();

        // Erstellen Sie LineReader
        LineReader reader = LineReaderBuilder.builder()
            .terminal(terminal)
            .build();

        // Lesen Sie die Eingabe in einer Schleife
        String line;
        while ((line = reader.readLine("> ")) != null) {
            System.out.println("Sie haben eingegeben: " + line);
            if (line.equals("exit")) {
                break;
            }
        }
    }
}
```

- **Ausgabe**: Wenn Sie dies ausführen, wird eine `> ` Eingabeaufforderung angezeigt. Sie können Text eingeben, die Rücktaste oder Pfeiltasten zur Bearbeitung verwenden (Funktionen, die mit `System.in` nicht so einfach verfügbar sind) und die Eingabetaste drücken. Das Eingeben von "exit" beendet das Programm.

### Optionale Funktionen
Sie können den `LineReader` mit zusätzlicher Funktionalität erweitern:

#### 1. **Aktivieren Sie den Befehlsverlauf**
   - Fügen Sie ein `History`-Objekt hinzu, um frühere Eingaben zu speichern und wieder aufzurufen (z. B. mit den Pfeiltasten nach oben/unten).
   - Beispiel:
     ```java
     import org.jline.reader.impl.history.DefaultHistory;
     import org.jline.reader.History;

     History history = new DefaultHistory();
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .history(history)
         .build();
     ```
   - Jetzt kann der Benutzer durch seinen Eingabeverlauf navigieren.

#### 2. **Fügen Sie Auto-Vervollständigung hinzu**
   - Implementieren Sie einen `Completer`, um Vorschläge zu machen, wenn der Benutzer die Tab-Taste drückt.
   - Beispiel mit einem einfachen Zeichenketten-Completer:
     ```java
     import org.jline.reader.Completer;
     import org.jline.reader.impl.completer.StringsCompleter;

     Completer completer = new StringsCompleter("foo", "bar", "baz");
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .completer(completer)
         .build();
     ```
   - Das Eingeben von "f" und Drücken der Tab-Taste schlägt "foo" vor.

#### 3. **Lesen Sie Passwörter (maskierte Eingabe)**
   - Verwenden Sie `readLine()` mit einem Maskierungszeichen, um die Eingabe zu verbergen (z. B. für Passwörter).
   - Beispiel:
     ```java
     String password = reader.readLine("Geben Sie das Passwort ein: ", '*');
     ```
   - Zeigt Sternchen (`*`) anstelle der eingegebenen Zeichen an.

### Ressourcenverwaltung
Für robuste Anwendungen schließen Sie das `Terminal`, wenn Sie fertig sind, um Ressourcen freizugeben. Da `Terminal` `Closeable` implementiert, verwenden Sie einen try-with-resources-Block:

```java
try (Terminal terminal = TerminalBuilder.builder().build()) {
    LineReader reader = LineReaderBuilder.builder()
        .terminal(terminal)
        .build();
    String line = reader.readLine("> ");
    System.out.println("Sie haben eingegeben: " + line);
}
```

### Warum `org.jline.reader` verwenden?
Im Gegensatz zur grundlegenden Eingabe mit `System.in` und `BufferedReader` bietet `org.jline.reader`:
- **Zeilenbearbeitung**: Rücktaste, Cursorbewegung usw.
- **Verlauf**: Frühere Eingaben wieder aufrufen.
- **Vervollständigung**: Vorschläge automatisch anzeigen.
- **Plattformübergreifende Terminalverwaltung**: Funktioniert konsistent in verschiedenen Umgebungen.

### Hinweise
- Wenn Sie kein `Terminal` in `LineReaderBuilder` angeben, erstellt es ein Standard-Terminal intern, sodass `LineReader reader = LineReaderBuilder.builder().build();` für einfache Fälle funktioniert.
- Vermeiden Sie das Aufrufen von `readLine()` aus mehreren Threads gleichzeitig, da `LineReader` nicht für gleichzeitige Lesevorgänge thread-sicher ist.
- Für fortgeschrittene Anwendungsfälle (z. B. mehrzeilige Eingabe, benutzerdefinierte Tastenkombinationen) erkunden Sie zusätzliche JLine-Funktionen wie Parser oder Tastenkarten.

Dies deckt die Grundlagen der Verwendung von `org.jline.reader` ab, um Konsoleneingaben in Java effektiv zu lesen. Beginnen Sie mit der grundlegenden Einrichtung und fügen Sie Funktionen wie Verlauf oder Vervollständigung hinzu, wie es für Ihre Anwendung erforderlich ist!