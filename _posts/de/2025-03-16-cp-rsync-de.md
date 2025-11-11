---
audio: false
generated: true
lang: de
layout: post
title: Kopieren von Dateien mit Verzeichnisstruktur
translated: true
type: note
---

Basierend auf Ihrer `find`-Befehlsausgabe möchten Sie alle `.log`-Dateien nach `/Users/lzwjava/projects/logs` kopieren und dabei ihre Verzeichnisstruktur beibehalten. Beispielsweise soll eine Datei wie `./CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` schließlich als `/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` enden. Ich zeige Ihnen, wie Sie dies mit `find` in Kombination mit `cp` oder `rsync` erreichen können, wobei die Verzeichnishierarchie erhalten bleibt.

---

### **Lösung 1: `find` mit `cp` verwenden**
Sie können `find` verwenden, um die `.log`-Dateien zu finden, und `cp` mit der Option `--parents`, um sie unter Beibehaltung ihrer Verzeichnisstruktur zu kopieren.

#### **Befehl**
```bash
find . -name "*.log" -exec cp --parents {} /Users/lzwjava/projects/logs \;
```

#### **Erklärung**
- **`find . -name "*.log"`**: Findet alle `.log`-Dateien im aktuellen Verzeichnis und seinen Unterverzeichnissen (wie in Ihrem Beispiel).
- **`-exec cp --parents {} /Users/lzwjava/projects/logs \;`**:
  - `cp --parents`: Kopiert die Datei und erstellt ihren Verzeichnispfad relativ zur Quelle (`.`) neu.
  - `{}`: Platzhalter für jede von `find` gefundene Datei.
  - `/Users/lzwjava/projects/logs`: Zielverzeichnis.
  - `\;`: Beendet den `-exec`-Befehl.

#### **Ergebnis**
- `./CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` → `/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log`
- Die Verzeichnisstruktur unter `CoreSimulator` bleibt erhalten.

#### **Vor dem Ausführen**
- Stellen Sie sicher, dass `/Users/lzwjava/projects/logs` existiert:
  ```bash
  mkdir -p /Users/lzwjava/projects/logs
  ```

---

### **Lösung 2: `rsync` verwenden**
`rsync` ist ein weiteres leistungsstarkes Tool, das Dateien unter Beibehaltung der Verzeichnisstruktur kopieren kann und oft effizienter für Massenvorgänge ist.

#### **Befehl**
```bash
find . -name "*.log" -exec rsync -R -a {} /Users/lzwjava/projects/logs \;
```

#### **Erklärung**
- **`-R`**: Verwendet relative Pfade und bewahrt die Verzeichnisstruktur der Quelle (`.`) auf.
- **`-a`**: Archivmodus (erhält Zeitstempel, Berechtigungen usw.).
- `{}`: Jede gefundene `.log`-Datei.
- `/Users/lzwjava/projects/logs`: Zielverzeichnis.

#### **Ergebnis**
Wie oben – Dateien werden mit ihren vollständigen relativen Pfaden kopiert.

#### **Vor dem Ausführen**
- Erstellen Sie das Zielverzeichnis, falls es nicht existiert:
  ```bash
  mkdir -p /Users/lzwjava/projects/logs
  ```

---

### **Überprüfen des Kopiervorgangs**
Nach dem Ausführen eines der Befehle überprüfen Sie das Ziel:
```bash
ls -R /Users/lzwjava/projects/logs
```
Sie sollten sehen:
```
/Users/lzwjava/projects/logs:
CoreSimulator

/Users/lzwjava/projects/logs/CoreSimulator:
CoreSimulator.log  FC275C39-59CC-4483-A64E-5D459D7A1D57  Simulator.log

/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57:
com.apple.itunesstored  system.log

/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/com.apple.itunesstored:
itunesstored.log
```

---

### **Wichtige Hinweise**
- **Berechtigungen:** Stellen Sie sicher, dass Sie Schreibzugriff auf `/Users/lzwjava/projects/logs` haben. Verwenden Sie andernfalls `sudo` (z.B. `sudo cp ...`) oder passen Sie die Berechtigungen an:
  ```bash
  chmod -R u+w /Users/lzwjava/projects/logs
  ```
- **Überschreiben:** Wenn Dateien am Zielort bereits existieren:
  - `cp` überschreibt sie ohne Warnung.
  - `rsync -a` überschreibt ebenfalls, aber Sie können `--ignore-existing` hinzufügen, um vorhandene Dateien zu überspringen:
    ```bash
    find . -name "*.log" -exec rsync -R -a --ignore-existing {} /Users/lzwjava/projects/logs \;
    ```
- **Dry Run (Zuerst testen):**
  - Für `cp`, fügen Sie `echo` hinzu, um eine Vorschau zu sehen:
    ```bash
    find . -name "*.log" -exec echo cp --parents {} /Users/lzwjava/projects/logs \;
    ```
  - Für `rsync`, verwenden Sie `--dry-run`:
    ```bash
    find . -name "*.log" -exec rsync -R -a --dry-run {} /Users/lzwjava/projects/logs \;
    ```

---

### **Was sollten Sie wählen?**
- **`cp`**: Einfacher, keine zusätzlichen Tools erforderlich (auf allen Unix-ähnlichen Systemen verfügbar).
- **`rsync`**: Flexibler (z.B. zum Synchronisieren, Überspringen von Duplikaten), erfordert aber, dass `rsync` installiert ist (auf den meisten Systemen Standard).

Beide funktionieren in Ihrem Fall. Ich empfehle, der Einfachheit halber mit `cp --parents` zu beginnen.

---

### **Finaler Befehl (Empfohlen)**
```bash
mkdir -p /Users/lzwjava/projects/logs
find . -name "*.log" -exec cp --parents {} /Users/lzwjava/projects/logs \;
```

Führen Sie dies aus Ihrem `Logs`-Verzeichnis aus (`lzwjava@anonymous Logs %`), und Sie sind fertig! Lassen Sie mich wissen, wenn Sie auf Probleme stoßen oder das Verhalten anpassen möchten (z.B. um die Struktur abzuflachen).