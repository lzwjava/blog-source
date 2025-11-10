---
audio: false
generated: true
lang: de
layout: post
title: 'Erste Schritte mit JShell: Eine Kurzanleitung'
translated: true
type: note
---

JShell ist ein interaktives REPL (Read-Eval-Print Loop)-Tool, das ab JDK 9 im Java Development Kit (JDK) enthalten ist. Es ermöglicht die interaktive Ausführung von Java-Code-Snippets, ohne ein vollständiges Programm schreiben zu müssen. Hier ist eine kurze Anleitung zur Verwendung von JShell:

### 1. **JShell starten**
- **JDK-Installation sicherstellen**: Stellen Sie sicher, dass JDK 9 oder höher installiert ist. Überprüfen Sie dies mit `java -version` in Ihrem Terminal oder Ihrer Eingabeaufforderung.
- **JShell starten**:
  - Öffnen Sie ein Terminal oder eine Eingabeaufforderung.
  - Geben Sie `jshell` ein und drücken Sie die Eingabetaste.
  - Eine Eingabeaufforderung wie `jshell>` erscheint, sobald JShell bereit ist.

### 2. **Grundlegende Verwendung**
- **Java-Code ausführen**:
  - Geben Sie Java-Ausdrücke, Anweisungen oder Deklarationen direkt an der Eingabeaufforderung ein.
  - Beispiel:
    ```java
    jshell> System.out.println("Hello, JShell!")
    Hello, JShell!
    ```
  - JShell wertet die Eingabe sofort aus und zeigt das Ergebnis an.

- **Variablen und Ausdrücke**:
  - Deklarieren Sie Variablen oder werten Sie Ausdrücke aus:
    ```java
    jshell> int x = 10
    x ==> 10
    jshell> x * 2
    $2 ==> 20
    ```
  - JShell weist Ergebnissen automatisch temporäre Namen zu (z.B. `$2`).

- **Methoden und Klassen definieren**:
  - Sie können Methoden oder Klassen definieren:
    ```java
    jshell> void sayHello() { System.out.println("Hello!"); }
    |  created method sayHello()
    jshell> sayHello()
    Hello!
    ```
    ```java
    jshell> class Test { int x = 5; }
    |  created class Test
    jshell> Test t = new Test()
    t ==> Test@7c417213
    jshell> t.x
    $5 ==> 5
    ```

### 3. **Wichtige Befehle**
JShell bietet integrierte Befehle, die mit `/` beginnen. Hier sind einige wesentliche:
- **Alle Codes anzeigen**: `/list` – Zeigt alle eingegebenen Snippets der Sitzung.
  ```java
  jshell> /list
  ```
- **Code bearbeiten**: `/edit <id>` – Öffnet einen GUI-Editor für das Snippet mit der angegebenen ID (aus `/list`).
- **Sitzung speichern**: `/save myfile.java` – Speichert alle Snippets in einer Datei.
- **Datei laden**: `/open myfile.java` – Lädt und führt Code aus einer Datei aus.
- **Variablen anzeigen**: `/vars` – Listet alle deklarierten Variablen auf.
  ```java
  jshell> /vars
  |    int x = 10
  ```
- **Methoden anzeigen**: `/methods` – Listet alle definierten Methoden auf.
- **JShell beenden**: `/exit` – Schließt die JShell-Sitzung.
- **Hilfe**: `/help` – Zeigt alle verfügbaren Befehle an.

### 4. **Pakete importieren**
- JShell importiert automatisch gängige Pakete (z.B. `java.util`, `java.io`). Um andere zu verwenden, importieren Sie sie manuell:
  ```java
  jshell> import java.time.LocalDate
  jshell> LocalDate.now()
  $3 ==> 2025-06-27
  ```

### 5. **Code bearbeiten und korrigieren**
- **Bestehenden Code ändern**:
  - Verwenden Sie `/list`, um die ID eines Snippets zu finden.
  - Definieren Sie es neu, indem Sie eine neue Version eingeben. JShell überschreibt die alte Definition.
    ```java
    jshell> int x = 5
    x ==> 5
    jshell> int x = 10
    x ==> 10
    ```
- **Snippet entfernen**: `/drop <id>` – Entfernt ein bestimmtes Snippet anhand seiner ID.

### 6. **Tab-Vervollständigung**
- Drücken Sie `Tab`, um Klassennamen, Methoden oder Befehle automatisch zu vervollständigen.
- Beispiel:
  ```java
  jshell> System.out.pr<tab>
  ```
  Schlägt `println`, `print`, usw. vor.

### 7. **Externe Skripte ausführen**
- Laden und führen Sie eine Java-Datei aus:
  ```java
  jshell> /open MyScript.java
  ```
- Sie können JShell auch mit einem Skript starten:
  ```bash
  jshell MyScript.java
  ```

### 8. **JShell anpassen**
- **Startskripts**: Erstellen Sie eine Datei (z.B. `startup.jsh`) mit Importen oder häufig verwendetem Code und laden Sie sie mit `/open startup.jsh` oder setzen Sie sie als Standard-Startskript:
  ```bash
  jshell --start startup.jsh
  ```
- **Feedback-Modi**: Passen Sie die Ausführlichkeit der Ausgabe mit `/set feedback <mode>` an (z.B. `normal`, `concise`, `verbose`).

### 9. **Tipps**
- **Schnelles Prototyping**: Verwenden Sie JShell, um kleine Code-Snippets zu testen, mit APIs zu experimentieren oder Java-Syntax zu lernen.
- **Fehlerbehandlung**: JShell liefert klare Fehlermeldungen und ermöglicht die sofortige Korrektur von Fehlern.
- **Mehrzeilige Eingabe**: Für komplexen Code unterstützt JShell mehrzeilige Bearbeitung. Beenden Sie eine Zeile mit einem Backslash (`\`), um fortzufahren:
  ```java
  jshell> int sum(int a, int b) { \
      ...> return a + b; \
      ...> }
  ```

### 10. **Problembehandlung**
- **JShell nicht gefunden**: Stellen Sie sicher, dass das JDK-`bin`-Verzeichnis im PATH Ihres Systems enthalten ist.
- **Langsamer Start**: Auf einigen Systemen kann JShell einen Moment zur Initialisierung benötigen. Stellen Sie sicher, dass Ihr JDK auf dem neuesten Stand ist.
- **Sitzung zurücksetzen**: Verwenden Sie `/reset`, um alle Snippets zu löschen und neu zu starten.

Weitere Details finden Sie in der offiziellen JDK-Dokumentation oder führen Sie `/help` in JShell aus. Wenn Sie bestimmte Aufgaben oder Code in JShell ausprobieren möchten, lassen Sie es mich wissen – ich kann Sie weiter unterstützen!