---
audio: false
generated: true
image: false
lang: de
layout: post
title: Windows Taskkill-Befehlsreferenz
translated: true
type: note
---

Unter Windows ist `taskkill` ein integriertes Befehlszeilen-Tool, mit dem Sie Prozesse anhand ihrer **Prozess-ID (PID)** oder ihres **Image-Namens (Name der ausführbaren Datei)** beenden (killen) können.

### Grundlegende Syntax

```bat
taskkill /PID <Prozess-ID> [/F]
taskkill /IM <Image-Name> [/F]
```

* `/PID <Prozess-ID>` → Beendet anhand der Prozess-ID.
* `/IM <Image-Name>` → Beendet anhand des Prozessnamens (z.B. `notepad.exe`).
* `/F` → Beendet den Prozess erzwungenermaßen.
* `/T` → Beendet den angegebenen Prozess und alle untergeordneten Prozesse.

---

### Beispiele

1. **Einen Prozess anhand der PID beenden:**

```bat
taskkill /PID 1234
```

Dies wird versuchen, den Prozess mit der PID 1234 zu stoppen.

2. **Einen Prozess anhand der PID erzwungen beenden:**

```bat
taskkill /PID 1234 /F
```

3. **Einen Prozess anhand des Namens beenden:**

```bat
taskkill /IM notepad.exe
```

4. **Einen Prozess anhand des Namens erzwungen beenden:**

```bat
taskkill /IM notepad.exe /F
```

5. **Einen Prozess und seine untergeordneten Prozesse beenden:**

```bat
taskkill /IM cmd.exe /T /F
```

---

### Die PID herausfinden

Falls Sie die PID nicht kennen:

```bat
tasklist
```

Dies listet alle laufenden Prozesse mit ihren PIDs auf. Anschließend können Sie `taskkill /PID` für den gewünschten Prozess verwenden.

---

⚠️ **Hinweise**

* Einige Systemprozesse können nicht beendet werden.
* Möglicherweise müssen Sie die Eingabeaufforderung als **Administrator** ausführen, um geschützte Prozesse zu beenden.

---

Möchten Sie, dass ich Ihnen auch zeige, wie man `tasklist` und `taskkill` in einem Befehl kombiniert (z.B. um alle Prozesse, die einem Namen entsprechen, automatisch zu beenden)?