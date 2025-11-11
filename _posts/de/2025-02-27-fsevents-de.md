---
audio: false
generated: true
lang: de
layout: post
title: Überwachung von Verzeichnisänderungen mit der FSEvents-API
translated: true
type: note
---

Ich habe einen Jekyll-Blog verwendet, und als ich `bundle exec jekyll serve --incremental` ausführte, zeigte das Terminal `fsevent_watch` an. Daher habe ich eine KI dazu befragt.

---

Es scheint, dass Sie sich vielleicht auf `fsevent_watch` beziehen, was in den meisten Programmierkontexten kein standardmäßiges, eigenständiges Tool oder Funktion ist. Basierend auf Ihrer Frage und gängigen Konventionen gehe ich davon aus, dass Sie nach der Arbeit mit der **FSEvents API** unter macOS fragen, um Dateisystemereignisse zu überwachen – vielleicht meinten Sie so etwas wie `fsevents` oder ein verwandtes Utility. Falls ich mich irre, klären Sie mich bitte auf!

Die FSEvents API ist ein macOS-spezifisches Framework, das Anwendungen erlaubt, Benachrichtigungen über Änderungen in einem Verzeichnisbaum zu erhalten. Es wird häufig in der C-, Objective-C- oder Swift-Programmierung verwendet, um Dateisystemereignisse wie das Erstellen, Löschen oder Ändern von Dateien zu beobachten. Da `fsevent_watch` kein anerkannter Befehl oder Funktion ist (es könnte ein Tippfehler oder ein Tool eines Drittanbieters sein), erkläre ich, wie man die FSEvents API direkt verwendet, was wahrscheinlich das ist, was Sie suchen.

Hier ist eine praktische Anleitung zur Verwendung von FSEvents zur Überwachung eines Verzeichnisses:

### Verwendung von FSEvents in C/Objective-C
Die FSEvents API ist Teil des CoreServices Frameworks unter macOS. Unten ist ein grundlegendes Beispiel in C, um ein Verzeichnis auf Änderungen zu überwachen:

1. **Notwendige Header einbinden**:
   Sie müssen den FSEvents-Header aus dem CoreServices Framework einbinden.

2. **Event Stream einrichten**:
   Erstellen Sie einen Event Stream, um ein bestimmtes Verzeichnis zu überwachen, definieren Sie eine Callback-Funktion zur Behandlung von Ereignissen und planen Sie ihn in einem Run Loop ein.

3. **Ereignisse behandeln**:
   Der Callback verarbeitet die Ereignisse (z.B. geänderte, gelöschte Dateien) und liefert Pfade und Flags.

Hier ist ein minimales Beispiel:

```c
#include <CoreServices/CoreServices.h>
#include <stdio.h>

// Callback-Funktion zur Behandlung von Dateisystemereignissen
void callback(
    ConstFSEventStreamRef streamRef,
    void *clientCallBackInfo,
    size_t numEvents,
    void *eventPaths,
    const FSEventStreamEventFlags eventFlags[],
    const FSEventStreamEventId eventIds[])
{
    char **paths = (char **)eventPaths;
    for (size_t i = 0; i < numEvents; i++) {
        printf("Änderung erkannt in: %s (Flags: 0x%x)\n", paths[i], eventFlags[i]);
    }
}

int main() {
    // Zu überwachender Pfad (z.B. Ihr Home-Verzeichnis)
    CFStringRef myPath = CFStringCreateWithCString(NULL, "/Users/ihrbenutzername", kCFStringEncodingUTF8);
    CFArrayRef pathsToWatch = CFArrayCreate(NULL, (const void **)&myPath, 1, NULL);

    // Erstellen des Event Streams
    FSEventStreamRef stream = FSEventStreamCreate(
        NULL,           // Allocator
        &callback,      // Callback-Funktion
        NULL,           // Callback-Info (Kontext)
        pathsToWatch,   // Zu überwachende Pfade
        kFSEventStreamEventIdSinceNow, // Beginne mit Ereignissen ab jetzt
        1.0,            // Latenz in Sekunden (Batch-Verzögerung)
        kFSEventStreamCreateFlagNone // Flags (kann kFSEventStreamCreateFlagFileEvents für Datei-Ereignisse verwenden)
    );

    // Den Stream im aktuellen Run Loop planen
    FSEventStreamScheduleWithRunLoop(stream, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);

    // Den Stream starten
    FSEventStreamStart(stream);

    // Den Loop ausführen, um auf Ereignisse zu warten
    printf("Überwache /Users/ihrbenutzername... Drücken Sie Strg+C zum Beenden.\n");
    CFRunLoopRun();

    // Aufräumen (in diesem Beispiel nicht erreichbar, es sei denn, es wird gestoppt)
    FSEventStreamStop(stream);
    FSEventStreamInvalidate(stream);
    FSEventStreamRelease(stream);
    CFRelease(pathsToWatch);
    CFRelease(myPath);

    return 0;
}
```

#### Erklärte Schritte:
- **Zu überwachende Pfade**: Sie geben ein oder mehrere Verzeichnisse (z.B. `/Users/ihrbenutzername`) in einem `CFArray` an.
- **Callback**: Die `callback`-Funktion wird aufgerufen, wenn Änderungen auftreten. Sie erhält ein Array der betroffenen Pfade und Flags (z.B. `kFSEventStreamEventFlagItemCreated`).
- **Stream-Erstellung**: `FSEventStreamCreate` richtet den Watcher ein. Die Latenz (z.B. `1.0` Sekunden) bündelt Ereignisse, um eine Überlastung des Callbacks zu vermeiden.
- **Run Loop**: Der Stream wird in einen Run Loop (wie `CFRunLoopRun`) integriert, um das Programm am Leben und reaktionsfähig zu halten.
- **Aufräumen**: Stoppen und geben Sie den Stream frei, wenn Sie fertig sind (in diesem Endlosschleifen-Beispiel nicht gezeigt).

#### Kompilierung:
Kompilieren Sie mit dem CoreServices Framework:
```bash
gcc -o fsevents_example fsevents_example.c -framework CoreServices
```

Führen Sie es aus:
```bash
./fsevents_example
```

### Wichtige Punkte:
- **Granularität**: Standardmäßig überwacht FSEvents Änderungen auf Verzeichnisebene. Für Ereignisse auf Dateiebene (z.B. spezifische Dateiänderungen) fügen Sie das Flag `kFSEventStreamCreateFlagFileEvents` hinzu.
- **Latenz**: Der Latenzparameter (z.B. `1.0`) steuert, wie oft der Callback ausgelöst wird. Niedrigere Werte geben schnellere Updates, aber mehr Aufrufe.
- **Umfang**: FSEvents überwacht den gesamten Verzeichnisbaum rekursiv – es müssen keine Unterverzeichnisse angegeben werden.

### Alternative: Verwendung eines Tools
Wenn Sie ein Kommandozeilen-Tool suchen, anstatt es selbst zu programmieren, gibt es kein `fsevent_watch` im Standard-macOS-Toolkit. Tools von Drittanbietern wie `fswatch` nutzen jedoch FSEvents. So verwenden Sie `fswatch`:

1. **fswatch installieren** (z.B. via Homebrew):
   ```bash
   brew install fswatch
   ```

2. **Ausführen**:
   ```bash
   fswatch /pfad/zum/überwachen
   ```
   Dies gibt Pfade aus, sobald Änderungen auftreten. Zum Beispiel:
   ```bash
   fswatch ~/Dokumente
   ```
   Sie sehen Zeilen wie `/Users/ihrbenutzername/Dokumente/datei.txt`, wenn sich Dateien ändern.

3. **Mit einem Skript**:
   Leiten Sie die Ausgabe in ein Skript für benutzerdefinierte Aktionen um:
   ```bash
   fswatch ~/Dokumente | while read -r file; do echo "Geändert: $file"; done
   ```

### Falls Sie etwas anderes gemeint haben
Wenn `fsevent_watch` sich auf eine bestimmte Bibliothek, ein Tool oder einen Tippfehler bezieht (z.B. `fsevents-watch`), geben Sie bitte mehr Kontext an – wie die Programmiersprache oder die Umgebung, in der Sie arbeiten – und ich werde die Antwort entsprechend anpassen.

Lassen Sie mich wissen, wie ich das für Sie verfeinern kann!