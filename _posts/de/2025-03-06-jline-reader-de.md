---
audio: false
generated: true
lang: de
layout: post
title: Lesen von Konsoleneingaben in Java
translated: true
type: note
---

Um das Paket `org.jline.reader` in Java zu verwenden, das Teil der JLine-Bibliothek für die Behandlung von Konsoleneingaben mit erweiterten Funktionen wie Zeileneditierung, History und Vervollständigung ist, folgen Sie diesen Schritten. Diese Anleitung bietet einen vollständigen und praktischen Ansatz für den Einstieg.

### Voraussetzungen
Stellen Sie sicher, dass die JLine-Bibliothek zu Ihrem Projekt hinzugefügt wurde. Wenn Sie Maven verwenden, fügen Sie die folgende Abhängigkeit in Ihre `pom.xml` ein:

```xml
<dependency>
    <groupId>org.jline</groupId>
    <artifactId>jline</artifactId>
    <version>3.21.0</version> <!-- Verwenden Sie die neueste Version -->
</dependency>
```

### Grundlegende Schritte zur Verwendung von `org.jline.reader`

1. **Erstellen einer Terminal-Instanz**
   - Verwenden Sie die Klasse `TerminalBuilder` aus `org.jline.terminal`, um ein `Terminal`-Objekt zu erstellen. Dies repräsentiert die Konsolenumgebung, in der Eingaben gelesen werden.
   - Beispiel:
     ```java
     import org.jline.terminal.Terminal;
     import org.jline.terminal.TerminalBuilder;

     Terminal terminal = TerminalBuilder.builder().build();
     ```
   - Die Methode `build()` erstellt ein Standard-Terminal, das für die meisten Umgebungen geeignet ist. Sie können es weiter anpassen (z.B. durch Setzen des Terminaltyps), aber die Standardeinstellung ist oft ausreichend.

2. **Erstellen einer LineReader-Instanz**
   - Verwenden Sie die Klasse `LineReaderBuilder` aus `org.jline.reader`, um ein `LineReader`-Objekt zu erstellen, und übergeben Sie ihm die `Terminal`-Instanz.
   - Der `LineReader` ist die Hauptschnittstelle zum Lesen von Benutzereingaben mit JLine-Funktionen.
   - Beispiel:
     ```java
     import org.jline.reader.LineReader;
     import org.jline.reader.LineReaderBuilder;

     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .build();
     ```

3. **Eingabe vom Benutzer lesen**
   - Verwenden Sie die Methode `readLine()` von `LineReader`, um eine vom Benutzer eingegebene Textzeile zu lesen. Optional können Sie einen anzuzeigenden Prompt angeben.
   - Beispiel:
     ```java
     String line = reader.readLine("> ");
     ```
   - Dies zeigt `> ` als Prompt an, wartet auf die Benutzereingabe und gibt die eingegebene Zeichenkette zurück, wenn der Benutzer die Eingabetaste drückt.

### Einfaches Beispiel
Hier ist ein vollständiges, minimales Beispiel, das Benutzereingaben in einer Schleife liest, bis der Benutzer "exit" eingibt:

```java
import org.jline.reader.LineReader;
import org.jline.reader.LineReaderBuilder;
import org.jline.terminal.Terminal;
import org.jline.terminal.TerminalBuilder;

public class ConsoleExample {
    public static void main(String[] args) throws Exception {
        // Terminal erstellen
        Terminal terminal = TerminalBuilder.builder().build();
        
        // LineReader erstellen
        LineReader reader = LineReaderBuilder.builder()
            .terminal(terminal)
            .build();
        
        // Eingabe in einer Schleife lesen
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

- **Ausgabe**: Wenn Sie dies ausführen, wird ein `> ` Prompt angezeigt. Sie können Text eingeben, die Rücktaste oder Pfeiltasten zur Bearbeitung verwenden (Funktionen, die mit `System.in` nicht einfach verfügbar sind) und die Eingabetaste drücken. Die Eingabe von "exit" beendet das Programm.

### Optionale Funktionen
Sie können den `LineReader` mit zusätzlicher Funktionalität erweitern:

#### 1. **Befehlsverlauf aktivieren**
   - Fügen Sie ein `History`-Objekt hinzu, um vorherige Eingaben zu speichern und abzurufen (z.B. mit den Pfeiltasten nach oben/unten).
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
   - Nun kann der Benutzer durch seinen Eingabeverlauf navigieren.

#### 2. **Auto-Completion hinzufügen**
   - Implementieren Sie einen `Completer`, um Vervollständigungen vorzuschlagen, wenn der Benutzer die Tab-Taste drückt.
   - Beispiel mit einem einfachen String-Completer:
     ```java
     import org.jline.reader.Completer;
     import org.jline.reader.impl.completer.StringsCompleter;

     Completer completer = new StringsCompleter("foo", "bar", "baz");
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .completer(completer)
         .build();
     ```
   - Die Eingabe von "f" und das Drücken der Tab-Taste schlägt "foo" vor.

#### 3. **Passwörter lesen (maskierte Eingabe)**
   - Verwenden Sie `readLine()` mit einem Maskierungszeichen, um die Eingabe zu verbergen (z.B. für Passwörter).
   - Beispiel:
     ```java
     String password = reader.readLine("Passwort eingeben: ", '*');
     ```
   - Zeigt Sternchen (`*`) anstelle der eingegebenen Zeichen an.

### Ressourcenverwaltung
Für robuste Anwendungen sollten Sie das `Terminal` schließen, wenn Sie fertig sind, um Ressourcen freizugeben. Da `Terminal` `Closeable` implementiert, verwenden Sie einen try-with-resources-Block:

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
Im Gegensatz zu grundlegenden Eingaben mit `System.in` und `BufferedReader` bietet `org.jline.reader`:
- **Zeileneditierung**: Rücktaste, Cursor-Bewegung usw.
- **Verlauf**: Abruf vorheriger Eingaben.
- **Vervollständigung**: Automatisches Vorschlagen von Optionen.
- **Plattformübergreifende Terminalbehandlung**: Funktioniert konsistent in verschiedenen Umgebungen.

### Hinweise
- Wenn Sie kein `Terminal` in `LineReaderBuilder` angeben, wird intern ein Standard-Terminal erstellt, daher funktioniert `LineReader reader = LineReaderBuilder.builder().build();` für einfache Fälle.
- Vermeiden Sie es, `readLine()` gleichzeitig von mehreren Threads aus aufzurufen, da `LineReader` nicht thread-safe für gleichzeitige Lesevorgänge ist.
- Für fortgeschrittene Anwendungsfälle (z.B. mehrzeilige Eingabe, benutzerdefinierte Tastenzuordnungen) erkunden Sie zusätzliche JLine-Funktionen wie Parser oder Key Maps.

Dies behandelt die Grundlagen der Verwendung von `org.jline.reader`, um Konsoleneingaben in Java effektiv zu lesen. Beginnen Sie mit dem grundlegenden Setup und fügen Sie je nach Bedarf Ihrer Anwendung Funktionen wie History oder Completion hinzu!