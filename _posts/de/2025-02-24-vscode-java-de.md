---
audio: false
generated: true
lang: de
layout: post
title: Konfigurieren des Java-Compilers in Visual Studio Code
translated: true
type: note
---

Hallo! Um den Java-Compiler in Visual Studio Code (VSCode) Version 1.96.4 unter Windows zu konfigurieren, insbesondere da du bereits das Java Extension Pack installiert hast, musst du den Pfad zum Java Development Kit (JDK) einrichten. Der Java-Compiler ist Teil des JDK, und VSCode muss wissen, wo es ihn finden kann, um deinen Java-Code zu kompilieren. Hier ist eine Schritt-für-Schritt-Anleitung, die dich einrichtet:

---

### Schritt 1: Stelle sicher, dass ein JDK installiert ist
Bevor du etwas in VSCode konfigurierst, stelle sicher, dass ein JDK (nicht nur eine JRE) auf deinem Windows-Rechner installiert ist. Das JDK enthält den Java-Compiler (`javac`). Wenn du es noch nicht installiert hast, kannst du es von einem Anbieter wie Oracle, OpenJDK oder Adoptium herunterladen (z. B. JDK 17 oder eine andere Version, die mit deinem Projekt kompatibel ist). Notiere dir nach der Installation den Installationspfad (z. B. `C:\Program Files\Java\jdk-17.0.1`).

---

### Schritt 2: Öffne die VSCode-Einstellungen
Um VSCode mitzuteilen, wo sich dein JDK befindet, musst du die Einstellungen anpassen:

- **Über die Einstellungen-Oberfläche:**
  - Drücke `Strg + ,`, um den Einstellungsbereich zu öffnen.
  - Oder gehe zu `Datei > Einstellungen > Einstellungen`.
- **Über settings.json (optional):**
  - Drücke `Strg + Umschalt + P`, um die Befehlspalette zu öffnen.
  - Tippe **"Open Settings (JSON)"** ein und wähle es aus, um die Datei `settings.json` direkt zu bearbeiten.

---

### Schritt 3: Setze den JDK-Pfad mit `java.home`
Das Java Extension Pack verwendet die Einstellung `java.home`, um dein JDK für die Kompilierung und Sprachfunktionen (wie IntelliSense) zu finden. So konfigurierst du es:

- **In der Einstellungen-Oberfläche:**
  - Suche im Einstellungsbereich nach **"java.home"**.
  - Gib im Feld "Java: Home" den vollständigen Pfad zu deiner JDK-Installation ein. Zum Beispiel:
    ```
    C:\Program Files\Java\jdk-17.0.1
    ```
  - Verwende Backslashes (`\`), da du unter Windows arbeitest, und stelle sicher, dass der Pfad zum JDK-Stammverzeichnis zeigt (es sollte einen `bin`-Ordner mit `javac.exe` enthalten).

- **In der settings.json:**
  - Wenn du die `settings.json` bearbeitest, füge diese Zeile hinzu (ersetze den Pfad mit deinem tatsächlichen JDK-Installationsort):
    ```json
    "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    ```
  - Beispiel für eine vollständige `settings.json`:
    ```json
    {
        "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    }
    ```
  - Speichere die Datei nach der Bearbeitung.

---

### Schritt 4: Überprüfe den Pfad
Stelle sicher, dass:
- Der Pfad zu einem JDK (nicht zu einer JRE) zeigt. Der `bin`-Ordner des JDK sollte `javac.exe` enthalten.
- Es keine Tippfehler im Pfad gibt und er mit deinem JDK-Installationsort übereinstimmt (z. B. `C:\Program Files\Java\jdk-17.0.1`).

Wenn du unsicher bist, wo dein JDK installiert ist, kannst du in `C:\Program Files\Java` oder an dem von dir gewählten Installationsort nachsehen.

---

### Schritt 5: Optional - Konfiguriere mehrere JDKs
Wenn du mehrere JDK-Versionen installiert hast und zwischen ihnen wechseln möchtest (z. B. JDK 8 für ein Projekt, JDK 17 für ein anderes), kannst du die Einstellung `java.configuration.runtimes` verwenden:

- Füge dies zu deiner `settings.json` hinzu:
  ```json
  "java.configuration.runtimes": [
      {
          "name": "JavaSE-1.8",
          "path": "C:\\Program Files\\Java\\jdk1.8.0_291"
      },
      {
          "name": "JavaSE-17",
          "path": "C:\\Program Files\\Java\\jdk-17.0.1",
          "default": true
      }
  ]
  ```
- Die Option `default: true` setzt die Standard-Laufzeitumgebung für die Ausführung deines Codes. Für die Kompilierung verwendet die Java-Erweiterung jedoch primär das in `java.home` angegebene JDK.

---

### Schritt 6: Lade VSCode neu oder starte es neu
Nachdem du `java.home` gesetzt hast, musst du möglicherweise:
- Das VSCode-Fenster neu laden (drücke `Strg + Umschalt + P`, tippe **"Reload Window"** ein und wähle es aus).
- Oder VSCode vollständig neu starten, damit die Änderungen wirksam werden.

---

### Hinweise zur Kompilierung
- **Einzelne Java-Dateien:** Wenn du mit einzelnen `.java`-Dateien arbeitest (ohne Build-Tools), verwendet die "Language Support for Java(TM) by Red Hat" des Java Extension Packs das JDK aus `java.home`, um deinen Code zu kompilieren und auszuführen. Du kannst die "Run"-Schaltfläche oder den Befehl **"Java: Run"** verwenden.
- **Projekte mit Build-Tools:** Wenn du Maven, Gradle oder ein anderes Build-Tool verwendest, wird der Compiler durch die Konfiguration des Build-Tools verwaltet (z. B. die Umgebungsvariable `JAVA_HOME`, `pom.xml` für Maven oder `build.gradle` für Gradle). Die Einstellung von `java.home` stellt jedoch weiterhin sicher, dass die Sprachfunktionen von VSCode korrekt funktionieren.

---

### Problembehandlung
- **Pfadprobleme:** Wenn VSCode das JDK nicht finden kann, überprüfe den Pfad in `java.home` erneut. Vermeide zusätzliche Leerzeichen oder Anführungszeichen, es sei denn, sie sind notwendig.
- **JDK nicht installiert:** Wenn du Fehler über ein fehlendes `javac` erhältst, stelle sicher, dass ein JDK installiert ist.
- **Versionskompatibilität:** Stelle sicher, dass deine JDK-Version den Anforderungen deines Projekts entspricht (z. B. JDK 8, 11, 17).

---

Das war's! Du solltest den Java-Compiler nun in VSCode konfiguriert haben. Wenn du auf Probleme stößt oder weitere Fragen hast – z. B. zur Arbeit mit einem bestimmten Build-Tool – kannst du dich gerne bei mir melden, ich helfe dir gerne weiter! 😊

---

Setze `maven.terminal.userJavaHome` auf true. Du kannst die Java-Version im Terminal überprüfen.