---
audio: false
date: 2025-09-09
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Verwaltung von Windows-Ports und Prozessen
translated: true
type: note
---

Unter Windows können Sie überprüfen, welche Ports abgehört werden – und von welchem Prozess (PID) – indem Sie `netstat` verwenden und diese Prozesse dann mit `taskkill` verwalten oder beenden. Dies ist oft beim Debugging von Backend-Projekten wie Java Spring Boot Apps, Redis oder MySQL notwendig. So geht's:

---

### 1. Abgehörte Ports überprüfen

Führen Sie die **Eingabeaufforderung (cmd)** oder **PowerShell** als Administrator aus:

```bash
netstat -ano | findstr LISTENING
```

* `-a` → zeigt alle Verbindungen und abgehörten Ports an
* `-n` → zeigt Adressen und Ports in numerischer Form an
* `-o` → schließt die PID (Process ID) ein

Beispielausgabe:

```
TCP    0.0.0.0:8080     0.0.0.0:0     LISTENING     12345
TCP    0.0.0.0:3306     0.0.0.0:0     LISTENING     6789
```

Hier:

* Port `8080` wird von PID `12345` verwendet (wahrscheinlich Ihre Spring Boot App).
* Port `3306` wird von PID `6789` verwendet (MySQL).

---

### 2. Herausfinden, zu welchem Prozess diese PID gehört

Sie können die PID einem Prozessnamen zuordnen:

```bash
tasklist | findstr 12345
```

Die Ausgabe könnte zeigen:

```
java.exe                  12345 Console                    1     512,000 K
```

Das bedeutet, dass Ihre Spring Boot App auf Port 8080 läuft.

---

### 3. Prozess bei Bedarf beenden

Wenn Sie diesen Prozess stoppen möchten:

```bash
taskkill /PID 12345 /F
```

* `/PID` → gibt die Prozess-ID an
* `/F` → erzwingt das Beenden

---

### 4. Typische Ports für gängige Backend-Dienste

* **Spring Boot (Java App):** 8080, 8081, etc.
* **MySQL:** 3306
* **Redis:** 6379
* **PostgreSQL:** 5432

Wenn Sie diese Ports also in der `netstat`-Ausgabe sehen, wissen Sie, welcher Dienst läuft.

---

👉 Pro-Tipp: Sie können diese Befehle kombinieren, um direkt herauszufinden, welcher Prozess einen bestimmten Port (z.B. 8080) verwendet:

```bash
netstat -ano | findstr :8080
```

Nehmen Sie dann die PID und überprüfen Sie sie mit `tasklist`.

---

Möchten Sie, dass ich Ihnen auch einen **PowerShell-One-Liner** zeige, der Ports direkt Prozessnamen zuordnet, ohne dass Sie separat mit `tasklist` nachschlagen müssen?