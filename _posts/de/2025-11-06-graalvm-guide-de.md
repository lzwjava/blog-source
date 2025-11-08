---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GraalVM-Installation und Nutzungsanleitung
translated: true
type: note
---

## Was ist GraalVM?

GraalVM ist eine quelloffene, hochperformante Laufzeitumgebung (JDK-Distribution), die mehrere Programmiersprachen wie Java, JavaScript, Python und mehr unterstützt. Sie zeichnet sich durch einen fortschrittlichen JIT-Compiler für schnellere Ausführung aus und ermöglicht die Kompilierung von Java-Anwendungen zu nativen Executables über Native Image, wodurch die Startzeit und der Speicherbedarf reduziert werden.

## Installation

1.  **GraalVM herunterladen**:
    *   Gehen Sie zur offiziellen GraalVM-Download-Seite.
    *   Wählen Sie die Community Edition (kostenlos) oder Oracle GraalVM (mit zusätzlichen Funktionen).
    *   Wählen Sie die Version für Ihre Plattform (z.B. Linux, macOS, Windows) und Architektur (x64 oder ARM).
    *   Stand 2025 ist der neueste stabile Release GraalVM für JDK 22 oder 23 – prüfen Sie die Website auf die aktuellste Version.

2.  **Entpacken und Installieren**:
    *   Entpacken Sie das heruntergeladene Archiv in ein Verzeichnis, z.B. `/opt/graalvm` unter Linux/macOS oder `C:\Program Files\GraalVM` unter Windows.
    *   Es ist kein Installer erforderlich; es handelt sich um eine portable Distribution.

3.  **Umgebungsvariablen setzen**:
    *   Setzen Sie `JAVA_HOME` auf das GraalVM-Verzeichnis (z.B. `export JAVA_HOME=/opt/graalvm` unter Linux/macOS).
    *   Fügen Sie das `bin`-Verzeichnis zu Ihrem `PATH` hinzu (z.B. `export PATH=$JAVA_HOME/bin:$PATH`).
    *   Überprüfen Sie die Installation mit `java -version`; die Ausgabe sollte GraalVM-Details anzeigen.

4.  **Zusätzliche Komponenten installieren (Optional)**:
    *   Verwenden Sie `gu` (GraalVM Updater) für Sprachlaufzeiten oder Native Image: `gu install native-image` (erfordert Build-Tools wie `build-essential` unter Linux).

## Erstellen eines Hello-World-Programms

Wir verwenden Java für dieses Beispiel, da es die Hauptsprache von GraalVM ist. Erstellen Sie eine einfache "Hello World"-App, kompilieren Sie sie und führen Sie sie aus.

### Schritt 1: Code schreiben
Erstellen Sie eine Datei namens `HelloWorld.java`:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World from GraalVM!");
    }
}
```

### Schritt 2: Kompilieren
Öffnen Sie ein Terminal im Verzeichnis mit der Datei und führen Sie aus:
```
javac HelloWorld.java
```
Dies erzeugt `HelloWorld.class`.

### Schritt 3: Ausführen
```
java HelloWorld
```
Ausgabe:
```
Hello, World from GraalVM!
```

### Erweitert: Zu nativem Executable kompilieren
Die Native Image-Funktion von GraalVM ermöglicht es Ihnen, einen eigenständigen Binary zu erstellen.

1.  Stellen Sie sicher, dass Native Image installiert ist: `gu install native-image`.
2.  Erzeugen Sie eine Konfiguration (der erste Lauf kann dies erfordern):
    ```
    native-image --no-fallback -H:+ReportExceptionStackTraces HelloWorld
    ```
    *   Dies erstellt `HelloWorld` (oder `helloworld.exe` unter Windows), einen nativen Binary.
    *   Beim ersten Build analysiert es die App und kann einige Minuten dauern.

3.  Führen Sie den nativen Binary aus:
    ```
    ./HelloWorld
    ```
    Die Ausgabe ist identisch, startet jedoch sofort und mit geringem Speicherverbrauch.

## Tipps für die Verwendung von GraalVM
*   **JDKs wechseln**: Verwenden Sie SDKMAN! (`sdk install java 22.0.2-graal`) zur einfachen Verwaltung.
*   **Multi-Language**: Führen Sie Node.js-Code mit `node` von GraalVM aus, oder Python mit `python`.
*   **Performance**: Aktivieren Sie den JIT-Compiler von GraalVM mit `-XX:+UnlockExperimentalVMOptions -XX:+UseJVMCICompiler`.
*   **Fehlerbehebung**: Überprüfen Sie die Protokolle in `~/.gu/` bei Problemen; stellen Sie sicher, dass Ihr System über einen C-Compiler für Native Image verfügt.

Weitere Details finden Sie in der offiziellen Dokumentation.

[GraalVM Downloads](https://www.graalvm.org/downloads/)  
[GraalVM Benutzerhandbuch](https://www.graalvm.org/latest/reference-manual/)  
[Native Image Tutorial](https://www.graalvm.org/latest/reference-manual/native-image/)